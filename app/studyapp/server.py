"""Local HTTP server: JSON API + static front end. Standard library only."""
from __future__ import annotations

import json
import random
import socket
import threading
import time
import webbrowser
from collections import defaultdict
from dataclasses import replace
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from . import scheduler as sch
from .exam import ExamSession, build_exam
from .grading import grade
from .mdrender import inline, render
from .model import Library, Question
from .parser import Loader
from .scheduler import Config
from .session import Session
from .store import Store

STATIC = Path(__file__).parent / "static"
CONTENT_TYPES = {".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8",
                 ".css": "text/css; charset=utf-8", ".svg": "image/svg+xml", ".ico": "image/x-icon"}


# --- presenting questions ---------------------------------------------------

def present(q: Question, rng: random.Random) -> dict:
    """What the browser needs to show a question. Never includes the answer."""
    d = {"qid": q.id, "type": q.type, "stem": render(q.stem), "exhibit": render(q.exhibit)}

    def order(n: int) -> list[int]:
        idx = list(range(n))
        if q.shuffle:
            rng.shuffle(idx)
        return idx

    if q.type in ("single", "multi"):
        d["options"] = [{"idx": i, "html": inline(q.options[i].text)} for i in order(len(q.options))]
        if q.type == "multi":
            d["select"] = sum(o.correct for o in q.options)
    elif q.type == "order":
        idx = list(range(len(q.order)))
        while len(idx) > 1 and idx == list(range(len(q.order))):
            rng.shuffle(idx)  # never show the items already in the right order
        d["items"] = [{"idx": i, "html": inline(q.order[i].text)} for i in idx]
    elif q.type == "match":
        d["rows"] = [{"idx": i, "html": inline(q.pairs[i][0])} for i in order(len(q.pairs))]
        choices = q.match_choices()
        if q.shuffle:
            rng.shuffle(choices)
        d["choices"] = [{"value": v, "html": inline(v)} for v in choices]
    elif q.type == "pbq":
        d["parts"] = [present(p, rng) for p in q.parts]
    return d


def feedback(q: Question, result: dict) -> dict:
    """Everything needed to show why the answer was right or wrong."""
    d = {"qid": q.id, "type": q.type, "correct": result.get("correct", False),
         "dont_know": result.get("dont_know", False), "explanation": render(q.explanation),
         "yours": []}  # the user's specific mistakes, each {"html", "why"}
    t = q.type
    if t in ("single", "multi"):
        chosen = set(result.get("chosen", []))
        d["options"] = [{"idx": i, "html": inline(o.text), "correct": o.correct, "chosen": i in chosen,
                         "why": inline(o.why)} for i, o in enumerate(q.options)]
        for i, o in enumerate(q.options):
            if i in chosen and not o.correct:
                d["yours"].append({"html": inline(o.text), "why": inline(o.why) or "This option is incorrect."})
            elif t == "multi" and o.correct and i not in chosen and chosen:
                d["yours"].append({"html": inline(o.text), "why": "You left this out, but it is correct."})
    elif t == "typed":
        d["your_text"] = result.get("text", "")
        d["accepted"] = q.accept
        mw = result.get("matched_wrong")
        if mw:
            d["yours"].append({"html": inline(mw["answer"]), "why": inline(mw["why"])})
    elif t == "order":
        seq = result.get("sequence", [])
        positions = result.get("positions", [])
        d["correct_order"] = [{"html": inline(o.text), "why": inline(o.why)} for o in q.order]
        d["your_order"] = [{"html": inline(q.order[i].text) if 0 <= i < len(q.order) else "?",
                            "ok": positions[n] if n < len(positions) else False}
                           for n, i in enumerate(seq)]
    elif t == "match":
        answers = result.get("answers", [None] * len(q.pairs))
        rows = result.get("rows", [False] * len(q.pairs))
        distractor_why = dict(q.distractors)
        right_of = defaultdict(list)
        for left, right in q.pairs:
            right_of[right].append(left)
        d["rows"] = []
        for i, (left, right) in enumerate(q.pairs):
            yours = answers[i] if i < len(answers) else None
            ok = rows[i] if i < len(rows) else False
            why = ""
            if not ok and yours:
                if yours in distractor_why:
                    why = distractor_why[yours]
                elif yours in right_of:
                    why = f"{yours} goes with {', '.join(right_of[yours])}, not {left}."
            d["rows"].append({"left": inline(left), "right": inline(right),
                              "yours": inline(yours) if yours else "", "ok": ok, "why": inline(why)})
            if not ok and yours and why:
                d["yours"].append({"html": inline(f"{left} → {yours}"), "why": inline(why)})
    elif t == "pbq":
        parts = result.get("parts", {})
        d["parts"] = []
        for p in q.parts:
            pf = feedback(p, parts.get(p.id, {"correct": False, "dont_know": True}))
            pf["stem"] = render(p.stem)
            d["parts"].append(pf)
            d["yours"].extend(pf["yours"])
    return d


# --- application state ------------------------------------------------------

class App:
    def __init__(self, root: Path, cfg: Config, store: Store, questions_dir: Path | None = None,
                 clock=time.time):
        self.root = root
        self.store = store
        cram = store.get_setting("cram")  # the home-screen toggle overrides config.toml once used
        self.cfg = cfg if cram is None else replace(cfg, cram=bool(cram))
        self.clock = clock
        self.loader = Loader(questions_dir or root / "questions")
        self.states = store.load_states()
        self.sessions: dict[str, Session] = {}
        self.exams: dict[str, ExamSession] = {}
        self.lock = threading.RLock()
        self.rng = random.Random()

    def library(self) -> Library:
        lib = self.loader.load()
        now = self.clock()
        for q in self.store.changed_answer_keys(lib.questions()):
            st = self.states.get(q.concept_id)
            if st:
                self.states[q.concept_id] = sch.mark_answer_key_changed(st, q.id, now)
                self.store.save_state(self.states[q.concept_id])
            self.store.accept_answer_key(q)
        return lib

    def deck_counts(self, lib: Library, deck_id: str) -> dict:
        deck = lib.deck(deck_id)
        cids = {q.concept_id for q in deck.questions} if deck else set()
        now = self.clock()
        c = {"unseen": 0, "learning": 0, "solid": 0, "due": 0, "concepts": len(cids),
             "questions": len(deck.questions) if deck else 0}
        for cid in cids:
            st = self.states.get(cid)
            c[sch.status(st, self.cfg)] += 1
            if st and sch.is_due(st, now):
                c["due"] += 1
        return c

    def snapshot(self, lib: Library) -> None:
        day = sch.local_day(self.clock())
        for d in lib.decks:
            c = self.deck_counts(lib, d.id)
            self.store.snapshot(day, d.id, c["unseen"], c["learning"], c["solid"])

    # --- API ---
    def home(self) -> dict:
        with self.lock:
            lib = self.library()
            self.snapshot(lib)
            saved = self.store.get_setting("selected_decks")
            ids = [d.id for d in lib.decks]
            selected = [i for i in (saved or ids) if i in ids] or ids
            return {
                "decks": [{"id": d.id, "name": d.name, "section": d.section, "file": Path(d.path).name,
                           "counts": self.deck_counts(lib, d.id)} for d in lib.decks],
                "selected": selected,
                "issues": [i.to_dict() for i in lib.issues],
                "exam": {"questions": self.cfg.exam_questions, "minutes": self.cfg.exam_minutes},
                "cram": self.cfg.cram,
            }

    def set_cram(self, on: bool) -> dict:
        """Takes effect for sessions started from now on."""
        with self.lock:
            self.cfg = replace(self.cfg, cram=on)
            self.store.set_setting("cram", on)
            return {"cram": on}

    def reset_progress(self) -> dict:
        with self.lock:
            self.store.reset_progress()
            self.states.clear()  # in place: sessions share this dict
            self.sessions.clear()
            self.exams.clear()
            return {"ok": True}

    def start(self, deck_ids: list[str]) -> dict:
        with self.lock:
            lib = self.library()
            deck_ids = [d.id for d in lib.decks if d.id in deck_ids]
            if not deck_ids:
                return {"error": "Pick at least one deck."}
            self.store.set_setting("selected_decks", deck_ids)
            s = Session(lib.questions(deck_ids), self.states, self.store.seen_counts(), self.cfg,
                        clock=self.clock, deck_ids=deck_ids)
            s.aliases = lib.aliases
            s.lib = lib
            self.sessions[s.id] = s
            return {"session": s.id}

    def next(self, sid: str) -> dict:
        with self.lock:
            s = self.sessions.get(sid)
            if not s:
                return {"error": "session not found", "expired": True}
            q = s.next()
            if q is None:
                return {"done": True}
            if getattr(s, "presented_for", None) != q.id:
                s.presented = present(q, self.rng)
                s.presented_for = q.id
                s.started_at = self.clock()
            return {"question": s.presented, "answered": s.count}

    def answer(self, sid: str, body: dict) -> dict:
        with self.lock:
            s = self.sessions.get(sid)
            if not s:
                return {"error": "session not found", "expired": True}
            q = s.current
            if q is None or body.get("qid") != q.id:
                return {"error": "that question is no longer current; reload to continue"}
            dont_know = bool(body.get("dont_know"))
            low_conf = bool(body.get("low_conf"))
            response = None if dont_know else body.get("response")
            result = grade(q, response, s.aliases)
            verdict = sch.verdict_for(result["correct"], low_conf, dont_know)
            state = s.record(q, verdict)
            now = self.clock()
            ms = body.get("ms")
            self.store.record_answer(ts=now, session_id=s.id, question=q, verdict=verdict, low_conf=low_conf,
                                     dont_know=dont_know, response=response,
                                     ms_taken=int(ms) if isinstance(ms, (int, float)) else None, state=state)
            self.snapshot(s.lib)
            fb = feedback(q, result)
            fb["verdict"] = verdict
            fb["box"] = state.box
            fb["status"] = sch.status(state, self.cfg)
            fb["answered"] = s.count
            fb["requeue_max"] = self.cfg.requeue_max
            return fb

    def end(self, sid: str) -> dict:
        with self.lock:
            s = self.sessions.pop(sid, None)
            if not s:
                return {"answered": 0, "correct": 0, "shaky": 0, "missed": 0, "missed_topics": []}
            out = s.summary()
            out["missed_topics"] = [
                {"deck": (s.lib.deck(deck).name if s.lib.deck(deck) else deck), "topic": topic,
                 "name": s.lib.topic_name(deck, topic), "misses": n}
                for (deck, topic), n in s.missed_topics.most_common()]
            return out

    def start_exam(self, deck_ids: list[str]) -> dict:
        with self.lock:
            lib = self.library()
            decks = [d for d in lib.decks if d.id in deck_ids]
            if not decks:
                return {"error": "Pick at least one deck."}
            self.store.set_setting("selected_decks", [d.id for d in decks])
            qs = build_exam(lib.questions([d.id for d in decks]), decks, self.cfg.exam_questions,
                            self.rng, self.store.seen_counts())
            ex = ExamSession(qs, [present(q, self.rng) for q in qs], [d.id for d in decks],
                             self.clock(), self.cfg.exam_minutes)
            ex.lib = lib
            self.exams[ex.id] = ex
            return {"exam": ex.id, "questions": ex.presented, "seconds_left": int(ex.deadline - ex.started)}

    def finish_exam(self, eid: str, body: dict) -> dict:
        """Grade every question at once. Unanswered counts as don't know; flagged as not sure."""
        with self.lock:
            ex = self.exams.pop(eid, None)
            if not ex:
                return {"error": "exam not found", "expired": True}
            responses = body.get("responses") or {}
            flagged = set(body.get("flagged") or [])
            ms = body.get("ms") or {}
            variants = defaultdict(int)
            for q in ex.lib.questions(ex.deck_ids):
                variants[q.concept_id] += 1
            items, by_deck, missed_topics = [], {}, defaultdict(int)
            correct = unanswered = 0
            for q in ex.questions:
                response = responses.get(q.id)
                dont_know = response is None
                unanswered += dont_know
                result = grade(q, response, ex.lib.aliases)
                verdict = sch.verdict_for(result["correct"], q.id in flagged, dont_know)
                self._record(ex.id, q, verdict, q.id in flagged, dont_know, response, ms.get(q.id),
                             variants[q.concept_id])
                ok = result["correct"]
                correct += ok
                d = by_deck.setdefault(q.deck_id, {"name": ex.lib.deck(q.deck_id).name, "correct": 0, "total": 0})
                d["correct"] += ok
                d["total"] += 1
                if not ok:
                    missed_topics[(q.deck_id, q.topic)] += 1
                fb = feedback(q, result)
                fb["verdict"] = verdict
                items.append({"qid": q.id, "verdict": verdict, "flagged": q.id in flagged, "fb": fb})
            self.snapshot(ex.lib)
            total = len(ex.questions)
            return {"total": total, "correct": correct, "unanswered": unanswered,
                    "percent": round(100 * correct / total) if total else 0,
                    "minutes": round((self.clock() - ex.started) / 60),
                    "by_deck": [by_deck[i] for i in ex.deck_ids if i in by_deck],
                    "missed_topics": [{"deck": ex.lib.deck(deck).name, "topic": topic,
                                       "name": ex.lib.topic_name(deck, topic), "misses": n}
                                      for (deck, topic), n in sorted(missed_topics.items(), key=lambda kv: -kv[1])],
                    "items": items}

    def _record(self, session_id: str, q: Question, verdict: str, low_conf: bool, dont_know: bool,
                response, ms, n_variants: int) -> sch.ConceptState:
        """Update the concept's schedule and log the answer."""
        now = self.clock()
        old = self.states.get(q.concept_id) or sch.ConceptState(concept_id=q.concept_id)
        state = sch.apply(old, verdict, q.id, q.type, n_variants, now, self.cfg)
        self.states[q.concept_id] = state
        self.store.record_answer(ts=now, session_id=session_id, question=q, verdict=verdict, low_conf=low_conf,
                                 dont_know=dont_know, response=response,
                                 ms_taken=int(ms) if isinstance(ms, (int, float)) else None, state=state)
        return state

    def progress(self) -> dict:
        with self.lock:
            lib = self.library()
            self.snapshot(lib)
            now = self.clock()
            recent = self.store.answers_since(now - 30 * sch.DAY)
            snaps = defaultdict(list)
            for day, deck_id, unseen, learning, solid in self.store.snapshots():
                snaps[deck_id].append({"day": day, "unseen": unseen, "learning": learning, "solid": solid})
            current = {q.id: q for q in lib.questions()}
            for q in list(current.values()):
                for p in q.parts:
                    current[p.id] = p
            decks = []
            for d in lib.decks:
                # Concept status per topic.
                topics: dict[str, dict] = {}
                for q in d.questions:
                    t = topics.setdefault(q.topic, {"topic": q.topic, "name": d.topics.get(q.topic, ""),
                                                     "concepts": set(), "attempts": 0, "misses": 0, "shaky": 0})
                    t["concepts"].add(q.concept_id)
                for a in recent:
                    if a["deck_id"] != d.id or a["question_id"] not in current or a["topic"] not in topics:
                        continue
                    t = topics[a["topic"]]
                    t["attempts"] += 1
                    t["misses"] += a["verdict"] == sch.MISSED
                    t["shaky"] += a["verdict"] == sch.SHAKY
                rows = []
                for t in topics.values():
                    st = {"unseen": 0, "learning": 0, "solid": 0}
                    for cid in t.pop("concepts"):
                        st[sch.status(self.states.get(cid), self.cfg)] += 1
                    t.update(st)
                    t["miss_rate"] = t["misses"] / t["attempts"] if t["attempts"] else None
                    t["shaky_rate"] = t["shaky"] / t["attempts"] if t["attempts"] else None
                    rows.append(t)
                rows.sort(key=lambda t: (t["miss_rate"] is None, -(t["miss_rate"] or 0), _topic_key(t["topic"])))
                decks.append({"id": d.id, "name": d.name, "section": d.section,
                              "counts": self.deck_counts(lib, d.id), "timeline": snaps.get(d.id, []),
                              "topics": rows})
            return {"decks": decks, "boxes": self.cfg.intervals_days, "solid_box": self.cfg.solid_box}


def _topic_key(topic: str):
    return [int(p) if p.isdigit() else p for p in topic.replace("-", ".").split(".")]


# --- HTTP -------------------------------------------------------------------

def make_handler(app: App):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):  # keep the terminal quiet
            pass

        def _json(self, data: dict, status: int = 200) -> None:
            body = json.dumps(data).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _body(self) -> dict:
            n = int(self.headers.get("Content-Length") or 0)
            if not n:
                return {}
            try:
                return json.loads(self.rfile.read(n))
            except json.JSONDecodeError:
                return {}

        def do_GET(self):
            path = self.path.split("?")[0]
            try:
                if path == "/api/home":
                    return self._json(app.home())
                if path == "/api/progress":
                    return self._json(app.progress())
                if path.startswith("/api/session/") and path.endswith("/next"):
                    return self._json(app.next(path.split("/")[3]))
            except Exception as e:  # never take the server down over one request
                return self._json({"error": f"{type(e).__name__}: {e}"}, 500)
            self._static(path)

        def do_POST(self):
            path = self.path.split("?")[0]
            body = self._body()
            try:
                if path == "/api/session":
                    return self._json(app.start(list(body.get("decks", []))))
                if path == "/api/exam":
                    return self._json(app.start_exam(list(body.get("decks", []))))
                if path == "/api/settings/cram":
                    return self._json(app.set_cram(bool(body.get("on"))))
                if path == "/api/reset":
                    return self._json(app.reset_progress())
                parts = path.split("/")
                if path.startswith("/api/exam/") and len(parts) == 5 and parts[4] == "finish":
                    return self._json(app.finish_exam(parts[3], body))
                if path.startswith("/api/session/") and len(parts) == 5:
                    sid, action = parts[3], parts[4]
                    if action == "answer":
                        return self._json(app.answer(sid, body))
                    if action == "end":
                        return self._json(app.end(sid))
            except Exception as e:
                return self._json({"error": f"{type(e).__name__}: {e}"}, 500)
            self._json({"error": "not found"}, 404)

        def _static(self, path: str) -> None:
            name = "index.html" if path in ("/", "") else path.lstrip("/")
            f = (STATIC / name).resolve()
            if STATIC.resolve() not in f.parents or not f.is_file():
                self.send_error(404)
                return
            data = f.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", CONTENT_TYPES.get(f.suffix, "application/octet-stream"))
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

    return Handler


def _free_port(preferred: int) -> int:
    for port in range(preferred, preferred + 20):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    return 0


def serve(root: Path, cfg: Config, data_dir: Path | None = None, open_browser: bool = True,
          port: int | None = None) -> None:
    store = Store((data_dir or root / "data") / "progress.db")
    app = App(root, cfg, store)
    port = _free_port(port or cfg.port)
    httpd = ThreadingHTTPServer(("127.0.0.1", port), make_handler(app))
    url = f"http://127.0.0.1:{httpd.server_address[1]}/"
    lib = app.loader.load()
    errors = sum(1 for i in lib.issues if i.level == "error")
    print(f"Study app running at {url}", flush=True)
    print(f"Loaded {sum(len(d.questions) for d in lib.decks)} questions from {len(lib.decks)} file(s)"
          + (f", {errors} error(s) (details on the home page)" if errors else ""))
    print("Press Ctrl+C to stop. Progress is saved after every answer.", flush=True)
    if open_browser:
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        httpd.server_close()
