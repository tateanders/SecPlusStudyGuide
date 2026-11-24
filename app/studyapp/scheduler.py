"""Concept-level Leitner scheduling.

A concept is a variant group (or a single ungrouped question). Each concept sits in a box;
higher boxes come back less often. Pure functions: the caller passes the current time.
"""
from __future__ import annotations

import time
import tomllib
from dataclasses import asdict, dataclass, field, replace
from pathlib import Path

DAY = 86400.0
CORRECT, SHAKY, MISSED = "correct", "shaky", "missed"


@dataclass
class Config:
    intervals_days: list[float] = field(default_factory=lambda: [0, 1, 3, 7, 14, 30, 60])
    solid_box: int = 3          # box at which a concept counts as "solid"
    cram: bool = False          # no time rules: a concept can become solid in one session
    new_concept_cap: int = 10   # stop adding new concepts while this many are in box 0
    new_every: int = 3          # at most one new concept per this many questions when reviews are waiting
    requeue_min: int = 3        # a missed concept comes back this many questions later, at least...
    requeue_max: int = 10       # ...and at most
    exam_questions: int = 90    # exam mode length...
    exam_minutes: int = 90      # ...and time limit
    port: int = 8765
    open_browser: bool = True

    @property
    def max_box(self) -> int:
        return len(self.intervals_days) - 1


def load_config(path: str | Path) -> Config:
    cfg = Config()
    p = Path(path)
    if not p.exists():
        return cfg
    with p.open("rb") as f:
        data = tomllib.load(f)
    flat = {**data.get("scheduling", {}), **data.get("server", {}),
            **{f"exam_{k}": v for k, v in data.get("exam", {}).items()}}
    known = {k: v for k, v in flat.items() if k in Config.__dataclass_fields__}
    return replace(cfg, **known)


@dataclass
class ConceptState:
    concept_id: str
    box: int = 0
    due_at: float = 0.0
    misses: int = 0
    reviews: int = 0
    last_seen: float = 0.0
    last_qid: str = ""
    last_type: str = ""
    # Confident correct answers since the last miss: [question id, local date].
    evidence: list[list[str]] = field(default_factory=list)
    # Recency-weighted miss rate, 0 (always right lately) to 1 (always missed lately).
    weak: float = 0.0
    # Confident correct answers in a row.
    streak: int = 0

    def to_dict(self) -> dict:
        return asdict(self)


def local_day(ts: float) -> str:
    return time.strftime("%Y-%m-%d", time.localtime(ts))


def verdict_for(correct: bool, low_confidence: bool, dont_know: bool) -> str:
    if dont_know or not correct:
        return MISSED
    return SHAKY if low_confidence else CORRECT


def status(state: ConceptState | None, cfg: Config) -> str:
    if state is None:
        return "unseen"
    return "solid" if state.box >= cfg.solid_box else "learning"


WEAK_DECAY = 0.6  # weight kept by the old weakness on each answer
WEAK_SCORE = {MISSED: 1.0, SHAKY: 0.5, CORRECT: 0.0}


def update_weak(weak: float, verdict: str) -> float:
    return WEAK_DECAY * weak + (1 - WEAK_DECAY) * WEAK_SCORE[verdict]


def is_strong(state: ConceptState) -> bool:
    """Answered right, confidently, several times in a row lately: no need to drill it."""
    return state.streak >= 2 and state.weak < 0.2


def gate_passed(evidence: list[list[str]], need_days: bool = True) -> bool:
    """Two different variants answered correctly and confidently on two different days
    (any day, if need_days is False)."""
    for i, (q1, d1) in enumerate(evidence):
        for q2, d2 in evidence[i + 1:]:
            if q1 != q2 and (d1 != d2 or not need_days):
                return True
    return False


def apply(state: ConceptState, verdict: str, qid: str, qtype: str, n_variants: int,
          now: float, cfg: Config) -> ConceptState:
    """Return the concept's new state after one answer."""
    s = replace(state, evidence=[list(e) for e in state.evidence])
    s.reviews += 1
    s.last_seen = now
    s.last_qid = qid
    s.last_type = qtype
    s.weak = update_weak(s.weak, verdict)
    s.streak = s.streak + 1 if verdict == CORRECT else 0
    iv = cfg.intervals_days

    if verdict == MISSED:
        s.box = 0
        s.misses += 1
        s.evidence = []
        s.due_at = now
    elif verdict == SHAKY:
        if s.box == 0:
            s.due_at = now
        else:
            s.due_at = now + max(1.0, iv[s.box] / 2) * DAY
    else:
        s.evidence.append([qid, local_day(now)])
        s.evidence = s.evidence[-12:]
        new_box = min(s.box + 1, cfg.max_box)
        # Anti-luck gate: one variant (or one day) can't make a concept solid.
        if n_variants >= 2 and new_box >= cfg.solid_box and not gate_passed(s.evidence, need_days=not cfg.cram):
            new_box = min(new_box, cfg.solid_box - 1)
        s.box = new_box
        # Concepts missed a lot lately come back sooner than the box alone says.
        s.due_at = now + iv[s.box] * (1 - 0.5 * s.weak) * DAY
    return s


def is_due(state: ConceptState, now: float) -> bool:
    return state.due_at <= now


def urgency(state: ConceptState, now: float, cfg: Config) -> float:
    """How overdue a concept is relative to its interval. Box-0 concepts always come first."""
    interval = max(cfg.intervals_days[state.box], 1.0) * DAY
    score = (now - state.due_at) / interval
    return score + (100.0 if state.box == 0 else 0.0)


def mark_answer_key_changed(state: ConceptState, qid: str, now: float) -> ConceptState:
    """The correct answer for qid changed in the file: drop its evidence and make the concept due."""
    s = replace(state, evidence=[e for e in state.evidence if e[0] != qid])
    s.due_at = min(s.due_at, now)
    return s
