"""Grade responses. Everything is all-or-nothing; the details say which parts were right.

Response shapes (indices always refer to the order in the file, not the shuffled display order):
    single: {"choice": 2}
    multi:  {"choices": [0, 3]}
    typed:  {"text": "whaling"}
    order:  {"sequence": [1, 0, 2, 3]}
    match:  {"answers": ["22", "443", null]}   # one per pair, in file order
    pbq:    {"parts": {"<part id>": <part response>, ...}}
A response of None means "Don't know".
"""
from __future__ import annotations

import re
import unicodedata

from .model import Question

ARTICLE_RE = re.compile(r"^(the|an|a)\s+")
KEEP_BETWEEN = "./:"


def canon(text: str) -> str:
    """Compare-form of a typed answer: lowercase, no spaces/punctuation/hyphens.

    '.', '/' and ':' are kept when they sit between a digit and a letter/digit,
    so '10.0.0.1' != '100.0.1' and '802.1X' keeps its dot.
    """
    s = unicodedata.normalize("NFKC", text).lower().strip()
    out = []
    for i, ch in enumerate(s):
        if ch.isalnum():
            out.append(ch)
        elif ch in KEEP_BETWEEN and 0 < i < len(s) - 1:
            a, b = s[i - 1], s[i + 1]
            if a.isalnum() and b.isalnum() and (a.isdigit() or b.isdigit()):
                out.append(ch)
    return "".join(out)


def _forms(user: str) -> set[str]:
    """The user's answer as typed, and with one leading article removed."""
    low = unicodedata.normalize("NFKC", user).lower().strip()
    forms = {canon(low), canon(ARTICLE_RE.sub("", low, count=1))}
    forms.discard("")
    return forms


def accepted_forms(answers: list[str], aliases: list[set[str]] | None = None) -> set[str]:
    targets = {canon(a) for a in answers}
    for group in aliases or []:
        cgroup = {canon(t) for t in group}
        if targets & cgroup:
            targets |= cgroup
    targets.discard("")
    return targets


def typed_matches(user: str, answers: list[str], aliases: list[set[str]] | None = None) -> bool:
    return bool(_forms(user) & accepted_forms(answers, aliases))


def grade(q: Question, response: dict | None, aliases: list[set[str]] | None = None) -> dict:
    """Return {"correct": bool, ...type-specific detail...}."""
    if response is None:
        if q.type == "pbq":
            return {"correct": False, "dont_know": True,
                    "parts": {p.id: grade(p, None, aliases) for p in q.parts}}
        return {"correct": False, "dont_know": True}
    try:
        return _grade(q, response, aliases)
    except (TypeError, ValueError, KeyError, IndexError, AttributeError):
        return {"correct": False, "malformed": True}


def _grade(q: Question, r: dict, aliases) -> dict:
    t = q.type
    if t == "single":
        choice = r.get("choice")
        ok = isinstance(choice, int) and 0 <= choice < len(q.options) and q.options[choice].correct
        return {"correct": ok, "chosen": [choice] if isinstance(choice, int) else []}
    if t == "multi":
        chosen = sorted({int(c) for c in r.get("choices", [])})
        right = sorted(i for i, o in enumerate(q.options) if o.correct)
        return {"correct": chosen == right, "chosen": chosen}
    if t == "typed":
        text = str(r.get("text", ""))
        ok = typed_matches(text, q.accept, aliases)
        matched_wrong = None
        if not ok:
            for ans, why in q.wrong_answers:
                if _forms(text) & accepted_forms([ans]):
                    matched_wrong = {"answer": ans, "why": why}
                    break
        return {"correct": ok, "text": text, "matched_wrong": matched_wrong}
    if t == "order":
        seq = [int(x) for x in r.get("sequence", [])]
        n = len(q.order)
        positions = [i < len(seq) and seq[i] == i for i in range(n)]
        return {"correct": seq == list(range(n)), "sequence": seq, "positions": positions}
    if t == "match":
        answers = list(r.get("answers", []))
        answers += [None] * (len(q.pairs) - len(answers))
        rows = [answers[i] == right for i, (_, right) in enumerate(q.pairs)]
        return {"correct": all(rows), "answers": answers[:len(q.pairs)], "rows": rows}
    if t == "pbq":
        given = r.get("parts", {}) or {}
        parts = {p.id: grade(p, given.get(p.id), aliases) if given.get(p.id) is not None
                 else {"correct": False, "dont_know": True} for p in q.parts}
        return {"correct": all(v["correct"] for v in parts.values()), "parts": parts}
    return {"correct": False}
