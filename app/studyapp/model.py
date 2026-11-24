"""Data classes shared by the parser, grader, scheduler and server."""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field

QUESTION_TYPES = ("single", "multi", "typed", "order", "match", "pbq")
PART_TYPES = ("single", "multi", "typed", "order", "match")


@dataclass
class Issue:
    """A problem found while loading a question file."""
    file: str
    line: int
    level: str  # "error" or "warn"
    message: str
    qid: str | None = None

    def __str__(self) -> str:
        return f"{self.file}:{self.line}: {self.level.upper()} {self.message}"

    def to_dict(self) -> dict:
        return {"file": self.file, "line": self.line, "level": self.level,
                "message": self.message, "qid": self.qid}


@dataclass
class Option:
    text: str
    correct: bool = False
    why: str = ""
    line: int = 0


@dataclass
class Question:
    id: str
    type: str
    file: str
    line: int
    topic: str = ""
    group: str = ""
    tags: list[str] = field(default_factory=list)
    shuffle: bool = True
    stem: str = ""
    exhibit: str = ""
    explanation: str = ""
    options: list[Option] = field(default_factory=list)        # single, multi
    accept: list[str] = field(default_factory=list)            # typed
    wrong_answers: list[tuple[str, str]] = field(default_factory=list)  # typed: (answer, why)
    order: list[Option] = field(default_factory=list)          # order: items in correct order
    pairs: list[tuple[str, str]] = field(default_factory=list)  # match: (left, right)
    distractors: list[tuple[str, str]] = field(default_factory=list)  # match: (right value, why)
    parts: list["Question"] = field(default_factory=list)      # pbq
    deck_id: str = ""

    @property
    def concept_id(self) -> str:
        """Scheduling unit: the variant group, or the question itself if ungrouped."""
        return self.group or f"q:{self.id}"

    @property
    def is_part(self) -> bool:
        return "/" in self.id

    def answer_key(self) -> dict:
        """Everything that decides right vs wrong. Wording changes don't affect it."""
        if self.type in ("single", "multi"):
            return {"t": self.type, "o": [(o.text, o.correct) for o in self.options]}
        if self.type == "typed":
            return {"t": self.type, "a": sorted(self.accept)}
        if self.type == "order":
            return {"t": self.type, "o": [o.text for o in self.order]}
        if self.type == "match":
            return {"t": self.type, "p": self.pairs}
        if self.type == "pbq":
            return {"t": self.type, "parts": [p.answer_key() for p in self.parts]}
        return {"t": self.type}

    def answer_key_hash(self) -> str:
        blob = json.dumps(self.answer_key(), sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(blob.encode()).hexdigest()[:16]

    def match_choices(self) -> list[str]:
        """Unique right-hand values plus distractors, in first-seen order."""
        seen: list[str] = []
        for _, right in self.pairs:
            if right not in seen:
                seen.append(right)
        for value, _ in self.distractors:
            if value not in seen:
                seen.append(value)
        return seen


@dataclass
class Deck:
    id: str            # file name without .md; stable key for selections and snapshots
    path: str
    name: str
    section: str = ""
    topics: dict[str, str] = field(default_factory=dict)
    exam_weight: float | None = None  # share of an exam's questions; None = by concept count
    questions: list[Question] = field(default_factory=list)  # top-level questions only (parts live in pbq.parts)


@dataclass
class Library:
    """Everything loaded from the questions directory."""
    decks: list[Deck] = field(default_factory=list)
    issues: list[Issue] = field(default_factory=list)
    aliases: list[set[str]] = field(default_factory=list)

    def questions(self, deck_ids: list[str] | None = None) -> list[Question]:
        out = []
        for d in self.decks:
            if deck_ids is None or d.id in deck_ids:
                out.extend(d.questions)
        return out

    def by_id(self) -> dict[str, Question]:
        return {q.id: q for q in self.questions()}

    def deck(self, deck_id: str) -> Deck | None:
        return next((d for d in self.decks if d.id == deck_id), None)

    def topic_name(self, deck_id: str, topic: str) -> str:
        d = self.deck(deck_id)
        return d.topics.get(topic, "") if d else ""
