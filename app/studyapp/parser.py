"""Parse question files (see FORMAT.md) into Decks, collecting errors instead of crashing.

A question with any error is skipped; warnings are reported but the question is kept.
"""
from __future__ import annotations

import os
import re
import unicodedata
from pathlib import Path

from .model import PART_TYPES, QUESTION_TYPES, Deck, Issue, Library, Option, Question

ID_RE = re.compile(r"^[a-z0-9][a-z0-9.\-]*(/[a-z0-9][a-z0-9.\-]*)?$")
META_RE = re.compile(r"^([a-z_]+):\s*(.*)$")
ITEM_RE = re.compile(r"^(?:[-*]|\d+[.)])\s+(.*)$")
OPTION_RE = re.compile(r"^\[( |x|X)\]\s+(.*)$")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")

META_KEYS = {"type", "topic", "group", "tags", "shuffle"}
FRONT_MATTER_KEYS = {"deck", "section", "topic", "topics", "exam_weight"}
SECTIONS = {"options", "accept", "wrong answers", "order", "match", "distractors", "exhibit", "explanation"}
ALLOWED_SECTIONS = {
    "single": {"options", "exhibit", "explanation"},
    "multi": {"options", "exhibit", "explanation"},
    "typed": {"accept", "wrong answers", "exhibit", "explanation"},
    "order": {"order", "exhibit", "explanation"},
    "match": {"match", "distractors", "exhibit", "explanation"},
    "pbq": {"exhibit", "explanation"},
}
ABSOLUTE_WORDS = re.compile(r"\b(always|never)\b", re.I)
ABOVE_RE = re.compile(r"\b(all|none|both|neither) of the (above|options)\b", re.I)
WORD_RE = re.compile(r"[a-z0-9]+")
MAX_LENGTH_LEAD = 10  # characters the correct option may be longer than the longest wrong one


class _Collector:
    """Gathers issues and remembers which question IDs had errors."""

    def __init__(self, file: str):
        self.file = file
        self.issues: list[Issue] = []
        self.failed: set[str] = set()

    def error(self, line: int, msg: str, qid: str | None = None) -> None:
        self.issues.append(Issue(self.file, line, "error", msg, qid))
        if qid:
            self.failed.add(qid)

    def warn(self, line: int, msg: str, qid: str | None = None) -> None:
        self.issues.append(Issue(self.file, line, "warn", msg, qid))


def _unquote(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def _fence_mask(lines: list[str]) -> list[bool]:
    """True for every line that is a fence line or inside a fenced code block."""
    mask = [False] * len(lines)
    opener: str | None = None
    for i, line in enumerate(lines):
        m = FENCE_RE.match(line)
        if opener is None:
            if m:
                opener = m.group(1)
                mask[i] = True
        else:
            mask[i] = True
            if m and m.group(1)[0] == opener[0] and len(m.group(1)) >= len(opener) \
                    and line.strip() == m.group(1):
                opener = None
    return mask


def _parse_front_matter(lines: list[str], col: _Collector) -> tuple[dict, dict, int]:
    if not lines or lines[0].strip() != "---":
        return {}, {}, 0
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        col.error(1, "front matter starts with '---' but is never closed with another '---'")
        return {}, {}, 0
    meta: dict[str, str] = {}
    topics: dict[str, str] = {}
    in_topics = False
    for i in range(1, end):
        raw = lines[i]
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw[0] in " \t":
            if not in_topics:
                col.warn(i + 1, "indented line in front matter is only allowed under 'topics:'")
                continue
            k, sep, v = raw.strip().partition(":")
            if not sep:
                col.warn(i + 1, "topic entries look like '  2.3: Topic name'")
                continue
            topics[_unquote(k)] = _unquote(v)
            continue
        k, sep, v = raw.partition(":")
        key = k.strip()
        if not sep:
            col.warn(i + 1, f"front matter line is not 'key: value': {raw.strip()!r}")
            continue
        if key not in FRONT_MATTER_KEYS:
            col.warn(i + 1, f"unknown front matter key {key!r} (known: {', '.join(sorted(FRONT_MATTER_KEYS))})")
        in_topics = key == "topics"
        if not in_topics:
            meta[key] = _unquote(v)
    return meta, topics, end + 1


def _list_items(body: list[tuple[int, str]], section: str, col: _Collector, qid: str):
    """Split a section body into list items: (line, first-line text, why, extra text lines)."""
    items: list[dict] = []
    for ln, raw in body:
        if not raw.strip():
            continue
        if raw[0] in " \t":
            if not items:
                col.error(ln, f"indented text in ### {section.title()} before any list item", qid)
                continue
            text = raw.strip()
            cur = items[-1]
            if text.lower().startswith("why:"):
                cur["why"] = text[4:].strip()
                cur["in_why"] = True
            elif cur["in_why"]:
                cur["why"] += " " + text
            else:
                cur["text"] += " " + text
            continue
        m = ITEM_RE.match(raw)
        if not m:
            col.error(ln, f"expected a list item ('- ...') in ### {section.title()}, got: {raw.strip()!r}", qid)
            continue
        items.append({"line": ln, "text": m.group(1).strip(), "why": "", "in_why": False})
    return items


def _split_why(text: str) -> tuple[str, str]:
    """'answer: why it is wrong' -> (answer, why). Splits on the first ': '."""
    head, sep, tail = text.partition(": ")
    if sep:
        return head.strip(), tail.strip()
    return text.strip(), ""


def _parse_block(heading_line: int, qid: str, body: list[tuple[int, str]], mask_body: list[bool],
                 deck: Deck, default_topic: str, col: _Collector) -> Question | None:
    q = Question(id=qid, type="", file=col.file, line=heading_line, deck_id=deck.id)

    # Metadata lines directly under the heading.
    i = 0
    meta_seen: dict[str, str] = {}
    while i < len(body):
        ln, raw = body[i]
        m = META_RE.match(raw)
        if not raw.strip() or not m or mask_body[i]:
            break
        key, val = m.group(1), m.group(2).strip()
        if key not in META_KEYS:
            if meta_seen:
                col.error(ln, f"unknown metadata key {key!r} (known: {', '.join(sorted(META_KEYS))})", qid)
                i += 1
                continue
            break  # first line isn't a known key: treat as the start of the stem
        meta_seen[key] = val
        i += 1

    q.type = meta_seen.get("type", "").lower()
    q.topic = meta_seen.get("topic", "") or ("" if q.is_part else default_topic)
    q.group = meta_seen.get("group", "")
    q.tags = [t.strip() for t in meta_seen.get("tags", "").split(",") if t.strip()]
    q.shuffle = meta_seen.get("shuffle", "yes").lower() not in ("no", "false", "0")

    if not q.type:
        col.error(heading_line, "missing 'type:' line (one of: " + ", ".join(QUESTION_TYPES) + ")", qid)
    elif q.type not in QUESTION_TYPES:
        col.error(heading_line, f"unknown type {q.type!r} (one of: {', '.join(QUESTION_TYPES)})", qid)

    # Stem, then ### sections.
    stem: list[str] = []
    sections: dict[str, list[tuple[int, str]]] = {}
    section_line: dict[str, int] = {}
    current: str | None = None
    for j in range(i, len(body)):
        ln, raw = body[j]
        if not mask_body[j] and raw.startswith("### "):
            name = raw[4:].strip().lower()
            if name not in SECTIONS:
                col.error(ln, f"unknown section '### {raw[4:].strip()}' (known: "
                              + ", ".join(s.title() for s in sorted(SECTIONS)) + ")", qid)
                current = "__unknown__"
                continue
            if name in sections:
                col.error(ln, f"duplicate section '### {name.title()}'", qid)
            current = name
            sections[name] = []
            section_line[name] = ln
            continue
        if raw.startswith("#### ") and not mask_body[j]:
            col.error(ln, "'####' headings are not used; PBQ parts are separate '## parent/part' questions", qid)
            continue
        if current is None:
            stem.append(raw)
        elif current != "__unknown__":
            sections[current].append((ln, raw))

    q.stem = "\n".join(stem).strip()
    q.exhibit = "\n".join(r for _, r in sections.get("exhibit", [])).strip()
    q.explanation = "\n".join(r for _, r in sections.get("explanation", [])).strip()

    if q.type in ALLOWED_SECTIONS:
        for name in sections:
            if name not in ALLOWED_SECTIONS[q.type]:
                col.error(section_line[name], f"section '### {name.title()}' is not used by type {q.type!r}", qid)

    if "options" in sections:
        for it in _list_items(sections["options"], "options", col, qid):
            m = OPTION_RE.match(it["text"])
            if not m:
                col.error(it["line"], "option must start with '[x] ' (correct) or '[ ] ' (wrong)", qid)
                continue
            q.options.append(Option(m.group(2).strip(), m.group(1).lower() == "x", it["why"], it["line"]))
    if "accept" in sections:
        q.accept = [it["text"] for it in _list_items(sections["accept"], "accept", col, qid)]
    if "wrong answers" in sections:
        for it in _list_items(sections["wrong answers"], "wrong answers", col, qid):
            ans, why = _split_why(it["text"])
            q.wrong_answers.append((ans, it["why"] or why))
    if "order" in sections:
        for it in _list_items(sections["order"], "order", col, qid):
            q.order.append(Option(it["text"], True, it["why"], it["line"]))
    if "match" in sections:
        for it in _list_items(sections["match"], "match", col, qid):
            left, sep, right = it["text"].partition("=>")
            if not sep or not left.strip() or not right.strip():
                col.error(it["line"], "match pairs look like '- left => right'", qid)
                continue
            q.pairs.append((left.strip(), right.strip()))
    if "distractors" in sections:
        for it in _list_items(sections["distractors"], "distractors", col, qid):
            val, why = _split_why(it["text"])
            q.distractors.append((val, it["why"] or why))

    _validate(q, col, sections)
    return q


def _validate(q: Question, col: _Collector, sections: dict) -> None:
    qid, ln = q.id, q.line
    if q.is_part and q.type == "pbq":
        col.error(ln, "a PBQ part can't itself be type 'pbq'", qid)
    if not q.stem:
        col.error(ln, "question has no stem (the text between the metadata and the first ### section)", qid)
    if not q.is_part and not q.topic:
        col.error(ln, "missing 'topic:' (or set a default 'topic:' in the file's front matter)", qid)
    if not q.is_part and not q.explanation:
        col.error(ln, "missing '### Explanation' section", qid)
    if q.is_part and q.group:
        col.warn(ln, "'group:' on a PBQ part is ignored; parts belong to the parent's group", qid)

    t = q.type
    if t in ("single", "multi"):
        if "options" not in sections:
            col.error(ln, "missing '### Options' section", qid)
            return
        correct = [o for o in q.options if o.correct]
        if t == "single":
            if len(correct) != 1:
                col.error(ln, f"type 'single' needs exactly one [x] option, found {len(correct)}", qid)
            if len(q.options) < 2:
                col.error(ln, "needs at least 2 options", qid)
            elif len(q.options) != 4:
                col.warn(ln, f"single-answer questions usually have 4 options, this one has {len(q.options)}", qid)
        else:
            if len(correct) < 2:
                col.error(ln, f"type 'multi' needs at least 2 [x] options, found {len(correct)}", qid)
            if correct and len(correct) == len(q.options):
                col.error(ln, "every option is marked [x]; a multi question needs wrong options too", qid)
            if len(q.options) - len(correct) < 2:
                col.warn(ln, "fewer than 2 wrong options makes 'choose N' easy to solve by elimination", qid)
        _lint_options(q, col)
    elif t == "typed":
        if not q.accept:
            col.error(ln, "type 'typed' needs a '### Accept' list with at least one answer", qid)
        for a in q.accept:
            if _in_stem(a, q.stem):
                col.warn(ln, f"the stem contains the accepted answer {a!r} (a giveaway)", qid)
                break
    elif t == "order":
        if len(q.order) < 3:
            col.error(ln, f"type 'order' needs at least 3 items in '### Order', found {len(q.order)}", qid)
        if len({o.text for o in q.order}) != len(q.order):
            col.error(ln, "order items must be distinct", qid)
    elif t == "match":
        if len(q.pairs) < 2:
            col.error(ln, f"type 'match' needs at least 2 pairs in '### Match', found {len(q.pairs)}", qid)
        if len({left for left, _ in q.pairs}) != len(q.pairs):
            col.error(ln, "left-hand match items must be distinct", qid)
        rights = {r for _, r in q.pairs}
        for val, _ in q.distractors:
            if val in rights:
                col.error(ln, f"distractor {val!r} is also a correct match", qid)
        for val, why in q.distractors:
            if not why:
                col.warn(ln, f"distractor {val!r} has no explanation ('- {val}: why it's wrong')", qid)


def _lint_options(q: Question, col: _Collector) -> None:
    for o in q.options:
        if not o.correct and not o.why:
            col.warn(o.line, f"wrong option {o.text!r} has no 'why:' line", q.id)
        if ABOVE_RE.search(o.text):
            col.warn(o.line, "avoid 'all/none of the above' style options; they are guessable", q.id)
    wrong = [o for o in q.options if not o.correct]
    correct = [o for o in q.options if o.correct]
    if wrong and correct:
        longest = max(correct, key=lambda o: len(o.text))
        lead = len(longest.text) - max(len(o.text) for o in wrong)
        if lead > MAX_LENGTH_LEAD:
            col.warn(longest.line, f"the correct option is {lead} characters longer than the longest wrong option "
                                   f"(max {MAX_LENGTH_LEAD}; a giveaway)", q.id)
        echoed = [o for o in correct if _in_stem(o.text, q.stem, min_chars=4)]
        if echoed and not any(_in_stem(o.text, q.stem, min_chars=4) for o in wrong):
            col.warn(echoed[0].line, f"the stem contains the correct option {echoed[0].text!r} (a giveaway)", q.id)
        if any(ABSOLUTE_WORDS.search(o.text) for o in wrong) and not any(ABSOLUTE_WORDS.search(o.text) for o in correct):
            col.warn(q.line, "'always'/'never' only appear in wrong options (a giveaway)", q.id)


def _words(text: str) -> list[str]:
    return WORD_RE.findall(unicodedata.normalize("NFKC", text).lower())


def _in_stem(answer: str, stem: str, min_chars: int = 2) -> bool:
    """True if the answer's words appear, in order and side by side, in the stem."""
    a, s = _words(answer), _words(stem)
    if not a or len("".join(a)) < min_chars:
        return False
    return any(s[i:i + len(a)] == a for i in range(len(s) - len(a) + 1))


def _correct_is_longest(q: Question) -> bool:
    if q.type not in ("single", "multi") or not q.options:
        return False
    top = max(len(o.text) for o in q.options)
    longest = [o for o in q.options if len(o.text) == top]
    return len(longest) == 1 and longest[0].correct


def parse_text(text: str, file: str, deck_id: str | None = None) -> tuple[Deck, list[Issue]]:
    col = _Collector(file)
    lines = text.splitlines()
    fm, topics, start = _parse_front_matter(lines, col)
    deck_id = deck_id or Path(file).stem
    if "deck" not in fm:
        col.warn(1, f"no 'deck:' name in front matter; using {deck_id!r}")
    deck = Deck(id=deck_id, path=file, name=fm.get("deck") or deck_id,
                section=fm.get("section", ""), topics=topics)
    if fm.get("exam_weight"):
        try:
            deck.exam_weight = float(fm["exam_weight"].rstrip("%"))
        except ValueError:
            col.warn(1, f"exam_weight must be a number, got {fm['exam_weight']!r}")
    default_topic = fm.get("topic", "")

    mask = _fence_mask(lines)
    # Find '## ' headings outside code fences.
    heads = [i for i in range(start, len(lines)) if not mask[i] and lines[i].startswith("## ")]
    if not heads:
        col.warn(start + 1, "no questions found (each question starts with a '## <id>' heading)")

    questions: list[Question] = []
    seen: set[str] = set()
    by_id: dict[str, Question] = {}
    for n, h in enumerate(heads):
        end = heads[n + 1] if n + 1 < len(heads) else len(lines)
        qid = lines[h][3:].strip()
        body = [(k + 1, lines[k]) for k in range(h + 1, end)]
        mbody = mask[h + 1:end]
        if not ID_RE.match(qid):
            col.error(h + 1, f"invalid question id {qid!r}: use lowercase letters, digits, '-' and '.', "
                             "plus one '/' for PBQ parts (e.g. 'd2-phishing-1' or 'd4-pbq-1/a')", qid or None)
            continue
        if qid in seen:
            col.error(h + 1, f"duplicate id {qid!r} in this file; this copy is skipped", None)
            continue
        seen.add(qid)
        q = _parse_block(h + 1, qid, body, mbody, deck, default_topic, col)
        if q is None:
            continue
        by_id[qid] = q
        if q.is_part:
            parent_id = qid.split("/")[0]
            parent = by_id.get(parent_id)
            if parent is None:
                col.error(h + 1, f"PBQ part's parent {parent_id!r} not found earlier in this file", qid)
                continue
            if parent.type != "pbq":
                col.error(h + 1, f"{parent_id!r} is type {parent.type!r}, not 'pbq', so it can't have parts", qid)
                continue
            q.topic = parent.topic
            q.group = ""
            parent.parts.append(q)
            if qid in col.failed:
                col.failed.add(parent_id)
        else:
            questions.append(q)

    for q in questions:
        if q.type == "pbq" and not q.parts:
            col.error(q.line, "PBQ has no parts (add questions with ids like "
                              f"'{q.id}/a', '{q.id}/b' after it)", q.id)
        if q.type == "pbq" and q.id in col.failed and any(p.id in col.failed for p in q.parts):
            bad = [p.id for p in q.parts if p.id in col.failed]
            col.error(q.line, f"PBQ skipped because these parts have errors: {', '.join(bad)}", None)

    deck.questions = [q for q in questions if q.id not in col.failed]

    scored = [q for q in deck.questions if q.type in ("single", "multi")]
    if len(scored) >= 5:
        share = sum(_correct_is_longest(q) for q in scored) / len(scored)
        if share > 0.4:
            col.warn(1, f"the correct option is the longest in {share:.0%} of choice questions; "
                        "vary option lengths so length isn't a cue")
    return deck, col.issues


def parse_file(path: str | os.PathLike) -> tuple[Deck, list[Issue]]:
    p = Path(path)
    try:
        text = p.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        return Deck(id=p.stem, path=str(p), name=p.stem), [Issue(str(p), 1, "error", f"can't read file: {e}")]
    return parse_text(text, str(p))


def parse_aliases(path: str | os.PathLike) -> tuple[list[set[str]], list[Issue]]:
    """`_aliases.md`: lines like '- MFA = multifactor authentication = multi-factor authentication'."""
    p = Path(path)
    out: list[set[str]] = []
    issues: list[Issue] = []
    if not p.exists():
        return out, issues
    for n, raw in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        m = ITEM_RE.match(line)
        if not m:
            continue
        terms = {t.strip() for t in m.group(1).split("=") if t.strip()}
        if len(terms) < 2:
            issues.append(Issue(str(p), n, "warn", "alias line needs at least two terms joined by '='"))
            continue
        out.append(terms)
    return out, issues


def _group_warnings(decks: list[Deck]) -> list[Issue]:
    counts: dict[str, list[Question]] = {}
    for d in decks:
        for q in d.questions:
            if q.group:
                counts.setdefault(q.group, []).append(q)
    out = []
    for g, qs in counts.items():
        if len(qs) == 1:
            q = qs[0]
            out.append(Issue(q.file, q.line, "warn",
                             f"group {g!r} has only one variant; add reworded versions so a miss can come back differently",
                             q.id))
    return out


class Loader:
    """Loads a questions directory, re-parsing only files whose mtime/size changed."""

    def __init__(self, directory: str | os.PathLike):
        self.dir = Path(directory)
        self._cache: dict[str, tuple[tuple, Deck, list[Issue]]] = {}

    def load(self) -> Library:
        lib = Library()
        files = sorted(p for p in self.dir.glob("*.md") if not p.name.startswith("_"))
        live = set()
        for p in files:
            st = p.stat()
            key = (st.st_mtime_ns, st.st_size)
            live.add(str(p))
            cached = self._cache.get(str(p))
            if cached and cached[0] == key:
                deck, issues = cached[1], cached[2]
            else:
                deck, issues = parse_file(p)
                self._cache[str(p)] = (key, deck, issues)
            lib.decks.append(deck)
            lib.issues.extend(issues)
        for k in list(self._cache):
            if k not in live:
                del self._cache[k]
        lib.issues.extend(_dedupe_across_files(lib.decks))
        lib.issues.extend(_group_warnings(lib.decks))
        lib.aliases, alias_issues = parse_aliases(self.dir / "_aliases.md")
        lib.issues.extend(alias_issues)
        return lib


def _dedupe_across_files(decks: list[Deck]) -> list[Issue]:
    """IDs are global. The first file (alphabetically) wins; later copies are dropped."""
    seen: dict[str, Question] = {}
    issues = []
    for d in decks:
        keep = []
        for q in d.questions:
            if q.id in seen:
                first = seen[q.id]
                issues.append(Issue(q.file, q.line, "error",
                                    f"duplicate id {q.id!r} (already used at {first.file}:{first.line}); skipped",
                                    q.id))
                continue
            seen[q.id] = q
            keep.append(q)
        d.questions = keep
    return issues


def load_library(directory: str | os.PathLike) -> Library:
    return Loader(directory).load()


def validate_paths(paths: list[str]) -> tuple[list[Deck], list[Issue]]:
    """Used by `study.py validate`: parse the given files together, as the app would."""
    decks, issues = [], []
    for p in paths:
        d, iss = parse_file(p)
        decks.append(d)
        issues.extend(iss)
    issues.extend(_dedupe_across_files(decks))
    issues.extend(_group_warnings(decks))
    return decks, issues
