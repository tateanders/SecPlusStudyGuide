"""Exam mode: a fixed set of questions answered in any order, graded all at once at the end."""
from __future__ import annotations

import random
import uuid

from .model import Deck, Question


def allocate(decks: list[Deck], available: dict[str, int], n: int) -> dict[str, int]:
    """Split n question slots across decks by exam_weight (or concept count), largest remainder first.

    A deck never gets more slots than it has concepts; its leftover goes to the others.
    """
    slots = {d.id: 0 for d in decks}
    left = min(n, sum(available.values()))
    open_decks = [d for d in decks if available.get(d.id, 0) > 0]
    while left > 0 and open_decks:
        weights = {d.id: d.exam_weight if d.exam_weight is not None else available[d.id] for d in open_decks}
        total = sum(weights.values()) or len(open_decks)
        share = {i: left * (w or 1) / total for i, w in weights.items()}
        give = {i: int(share[i]) for i in share}
        for i in sorted(share, key=lambda i: -(share[i] - give[i]))[:left - sum(give.values())]:
            give[i] += 1
        for i, g in give.items():
            room = available[i] - slots[i]
            take = min(g, room)
            slots[i] += take
            left -= take
        open_decks = [d for d in open_decks if slots[d.id] < available[d.id]]
    return slots


def build_exam(questions: list[Question], decks: list[Deck], n: int, rng: random.Random,
               seen_counts: dict[str, int]) -> list[Question]:
    """One question per concept, decks weighted, scenario (pbq) questions first like the real thing."""
    by_deck: dict[str, dict[str, list[Question]]] = {}
    for q in questions:
        by_deck.setdefault(q.deck_id, {}).setdefault(q.concept_id, []).append(q)
    decks = [d for d in decks if d.id in by_deck]
    slots = allocate(decks, {d.id: len(by_deck[d.id]) for d in decks}, n)
    picked: list[Question] = []
    for d in decks:
        concepts = list(by_deck[d.id].values())
        rng.shuffle(concepts)
        for variants in concepts[:slots[d.id]]:
            picked.append(min(variants, key=lambda q: (seen_counts.get(q.id, 0), rng.random())))
    rng.shuffle(picked)
    return [q for q in picked if q.type == "pbq"] + [q for q in picked if q.type != "pbq"]


class ExamSession:
    def __init__(self, questions: list[Question], presented: list[dict], deck_ids: list[str],
                 started: float, minutes: float):
        self.id = "exam-" + uuid.uuid4().hex[:12]
        self.questions = questions
        self.presented = presented   # shown once, so option order stays put while moving around
        self.deck_ids = deck_ids
        self.started = started
        self.deadline = started + minutes * 60
        self.lib = None
