"""One study session: decides what to ask next and tracks in-session requeues.

The Session owns bookkeeping (history, requeues, stats). A Picker decides what comes next,
so a future exam mode can plug in a different picker without touching the rest.
"""
from __future__ import annotations

import random
import time
import uuid
from collections import Counter
from typing import Callable

from . import scheduler as sch
from .model import Question
from .scheduler import Config, ConceptState

HARD_TO_BLUFF = {"typed", "multi"}


class Session:
    def __init__(self, questions: list[Question], states: dict[str, ConceptState],
                 seen_counts: dict[str, int], cfg: Config,
                 rng: random.Random | None = None, clock: Callable[[], float] = time.time,
                 picker: "LearningPicker | None" = None, deck_ids: list[str] | None = None):
        self.id = uuid.uuid4().hex[:12]
        self.deck_ids = deck_ids or []
        self.cfg = cfg
        self.rng = rng or random.Random()
        self.clock = clock
        self.states = states            # shared, mutated as answers come in
        self.seen_counts = seen_counts  # question id -> times answered (all time)
        self.picker = picker or LearningPicker()
        self.aliases: list[set[str]] = []  # typed-answer equivalences, set by the server
        self.lib = None                     # the Library this session was built from

        self.concepts: dict[str, list[Question]] = {}
        self.deck_of: dict[str, str] = {}
        for q in questions:
            self.concepts.setdefault(q.concept_id, []).append(q)
            self.deck_of.setdefault(q.concept_id, q.deck_id)
        self.by_id = {q.id: q for q in questions}

        self.count = 0                      # questions answered this session
        self.history: list[Question] = []   # questions answered, in order
        self.answered: set[str] = set()     # concept ids answered this session
        self.requeue: dict[str, int] = {}   # concept id -> answer count at which it comes back
        self.requeue_qid: dict[str, str] = {}  # concept id -> missed question to ask again, as is
        self.shaky_requeued: set[str] = set()
        self.last_verdict: dict[str, str] = {}  # concept id -> its latest verdict this session
        self.last_new_at = -10**9
        self.current: Question | None = None
        self.stats = Counter()
        self.missed_topics: Counter = Counter()

    def next(self) -> Question | None:
        if self.current is None:
            self.current = self.picker.pick(self)
        return self.current

    def record(self, q: Question, verdict: str) -> ConceptState:
        """Apply one graded answer. Returns the concept's new state."""
        cid = q.concept_id
        now = self.clock()
        was_new = cid not in self.states
        old = self.states.get(cid) or ConceptState(concept_id=cid)
        new = sch.apply(old, verdict, q.id, q.type, len(self.concepts.get(cid, [q])), now, self.cfg)
        self.states[cid] = new
        self.seen_counts[q.id] = self.seen_counts.get(q.id, 0) + 1

        self.count += 1
        if was_new:
            self.last_new_at = self.count
        self.history.append(q)
        self.answered.add(cid)
        self.current = None
        self.stats[verdict] += 1
        lo, hi = self.cfg.requeue_min, self.cfg.requeue_max
        self.requeue_qid.pop(cid, None)
        if verdict == sch.MISSED:
            self.missed_topics[(q.deck_id, q.topic)] += 1
            if new.weak >= 0.6:  # missed again and again lately: bring it back sooner
                hi = max(lo, (lo + hi) // 2)
            self.requeue[cid] = self.count + self.rng.randint(lo, hi)
            self.requeue_qid[cid] = q.id  # the exact question comes back, not a variant
        elif verdict == sch.SHAKY and new.box == 0 and cid not in self.shaky_requeued and not self.cfg.cram:
            self.shaky_requeued.add(cid)
            self.requeue[cid] = self.count + self.rng.randint(lo + 1, hi + 1)
        elif verdict == sch.CORRECT and self.last_verdict.get(cid) == sch.MISSED:
            # Right after being wrong: check once more, further out, that it stuck.
            self.requeue[cid] = self.count + self.rng.randint(hi + 1, 2 * hi)
        elif self.cfg.cram and new.box < self.cfg.solid_box:
            # Cram mode: keep coming back this session, as another variant, until solid.
            self.requeue[cid] = self.count + self.rng.randint(lo, hi)
        else:
            self.requeue.pop(cid, None)
        self.last_verdict[cid] = verdict
        return new

    def summary(self) -> dict:
        return {"answered": self.count, "correct": self.stats[sch.CORRECT],
                "shaky": self.stats[sch.SHAKY], "missed": self.stats[sch.MISSED]}


class LearningPicker:
    """Requeued misses, then due reviews, then new concepts (capped), then weakest-first review."""

    TOP_K = 6

    def pick(self, s: Session) -> Question | None:
        if not s.concepts:
            return None
        now = s.clock()
        cfg = s.cfg

        ready = sorted((c for c, at in s.requeue.items() if at <= s.count and c in s.concepts),
                       key=lambda c: s.requeue[c])
        if ready:
            return self._choose(s, ready, missed=True)

        seen = [c for c in s.concepts if c in s.states]
        due = [c for c in seen if c not in s.answered and c not in s.requeue
               and (sch.is_due(s.states[c], now)
                    or (cfg.cram and s.states[c].box < cfg.solid_box))]
        due.sort(key=lambda c: -(sch.urgency(s.states[c], now, cfg) + 2 * s.states[c].weak))

        learning = sum(1 for c in seen if s.states[c].box == 0)
        new = self._new_order(s) if learning < cfg.new_concept_cap else []

        if due and new:
            if s.count - s.last_new_at >= cfg.new_every:
                return self._choose(s, new, limit=3)
            return self._choose(s, due)
        if due:
            return self._choose(s, due)
        if new:
            return self._choose(s, new, limit=3)

        # Nothing due and no new allowed: review weak concepts, avoiding recent ones and ones
        # already answered right this session. Strong concepts only if nothing else is left.
        recent = {q.concept_id for q in s.history[-min(10, max(len(seen) - 1, 0)):]} if s.history else set()
        pool = [c for c in seen if c not in s.requeue and c not in recent
                and s.last_verdict.get(c) != sch.CORRECT]
        pool = [c for c in pool if not sch.is_strong(s.states[c])] or pool
        last = s.history[-1].concept_id if s.history else None
        if not pool and s.requeue:
            # Small deck, everything is waiting to come back: pull the soonest one forward.
            waiting = sorted((c for c in s.requeue if c != last), key=lambda c: s.requeue[c])
            if waiting:
                return self._choose(s, waiting, missed=True)
        if not pool:
            pool = [c for c in s.concepts if c != last] or list(s.concepts)
        return self._choose(s, self._weighted_order(s, pool))

    def _weighted_order(self, s: Session, pool: list[str]) -> list[str]:
        """Random order where weak concepts tend to come first and long right-streaks last."""
        def weight(c: str) -> float:
            st = s.states.get(c)
            return (0.05 + st.weak) / (1 + st.streak) if st else 0.55
        return sorted(pool, key=lambda c: -(s.rng.random() ** (1 / weight(c))))

    def _new_order(self, s: Session) -> list[str]:
        """Unseen concepts in file order, interleaved round-robin across decks.

        The deck with the smallest share of concepts seen goes first, so coverage stays even.
        """
        per_deck: dict[str, list[str]] = {}
        totals: dict[str, int] = {}
        for c in s.concepts:
            d = s.deck_of[c]
            totals[d] = totals.get(d, 0) + 1
            if c not in s.states:
                per_deck.setdefault(d, []).append(c)
        out: list[str] = []
        ranked = sorted(per_deck, key=lambda d: 1 - len(per_deck[d]) / totals[d])
        queues = [per_deck[d] for d in ranked]
        while any(queues):
            for qd in queues:
                if qd:
                    out.append(qd.pop(0))
        return out

    def _variant(self, s: Session, cid: str, missed: bool) -> Question:
        again = s.requeue_qid.get(cid)
        if missed and again in s.by_id:
            return s.by_id[again]
        qs = s.concepts[cid]
        st = s.states.get(cid)
        last_qid = st.last_qid if st else ""
        last_type = st.last_type if st else ""
        return min(qs, key=lambda q: (
            len(qs) > 1 and q.id == last_qid,
            missed and q.type not in HARD_TO_BLUFF,
            s.seen_counts.get(q.id, 0),
            q.type == last_type,
            s.rng.random(),
        ))

    def _choose(self, s: Session, candidates: list[str], missed: bool = False, limit: int | None = None) -> Question:
        """Take the first candidate whose variant doesn't break the mixing rules."""
        top = candidates[:limit or self.TOP_K]
        picks = [self._variant(s, c, missed) for c in top]
        last = s.history[-1] if s.history else None
        last2_types = [q.type for q in s.history[-2:]]
        for q in picks:
            same_type_run = len(last2_types) == 2 and all(t == q.type for t in last2_types)
            same_topic = last is not None and q.topic == last.topic and q.deck_id == last.deck_id
            if not same_type_run and not same_topic:
                return q
        return picks[0]
