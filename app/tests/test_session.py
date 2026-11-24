import random
import tempfile
import unittest
from pathlib import Path

from studyapp import scheduler as sch
from studyapp.model import Question
from studyapp.scheduler import CORRECT, DAY, MISSED, SHAKY, Config, ConceptState
from studyapp.server import App, present
from studyapp.session import Session
from studyapp.store import Store

T0 = 1_700_000_000.0
TYPES = ["single", "typed", "multi"]


def make_questions(n_concepts, variants=3, topics=4, deck="d"):
    qs = []
    for c in range(n_concepts):
        for v in range(variants):
            qs.append(Question(id=f"{deck}-c{c}-{v}", type=TYPES[v % 3], file="f.md", line=1,
                               topic=f"t{c % topics}", group=f"{deck}-c{c}", deck_id=deck))
    return qs


class Clock:
    def __init__(self, t=T0):
        self.t = t

    def __call__(self):
        return self.t


def session(qs, states=None, cfg=None, seed=1, clock=None):
    return Session(qs, states if states is not None else {}, {}, cfg or Config(),
                   rng=random.Random(seed), clock=clock or Clock())


class Requeue(unittest.TestCase):
    def test_missed_question_returns_3_to_10_questions_later_as_the_same_question(self):
        for seed in range(20):
            s = session(make_questions(30), seed=seed)
            first = s.next()
            s.record(first, MISSED)
            gap = None
            for i in range(1, 15):
                q = s.next()
                if q.concept_id == first.concept_id:
                    gap = i
                    self.assertEqual(q.id, first.id)
                    break
                s.record(q, CORRECT)
            self.assertIsNotNone(gap, f"seed {seed}: missed concept never came back")
            self.assertGreaterEqual(gap, 4)  # 3 other questions at minimum in between
            self.assertLessEqual(gap, 11)

    def test_tiny_deck_all_missed_still_spaces_and_varies(self):
        s = session(make_questions(5))
        prev = None
        for _ in range(40):
            q = s.next()
            if prev:
                self.assertNotEqual(q.concept_id, prev.concept_id)
            s.record(q, MISSED)
            prev = q

    def test_missed_concept_is_not_asked_immediately(self):
        s = session(make_questions(30))
        q = s.next()
        s.record(q, MISSED)
        self.assertNotEqual(s.next().concept_id, q.concept_id)

    def test_shaky_in_box_0_comes_back_once(self):
        s = session(make_questions(80))
        q = s.next()
        s.record(q, MISSED)
        returns = 0
        for _ in range(40):
            n = s.next()
            if n.concept_id == q.concept_id:
                returns += 1
                s.record(n, SHAKY)  # still unsure, stays in box 0
            else:
                s.record(n, CORRECT)
        self.assertEqual(returns, 2)  # once after the miss, once more after the shaky answer


class NewConceptCap(unittest.TestCase):
    def test_new_concepts_stop_when_too_many_are_in_box_0(self):
        cfg = Config(new_concept_cap=5)
        s = session(make_questions(40), cfg=cfg)
        for _ in range(30):
            q = s.next()
            s.record(q, MISSED)
        seen = len(s.states)
        self.assertLessEqual(seen, 5)

    def test_new_concepts_flow_when_doing_well(self):
        s = session(make_questions(40))
        for _ in range(30):
            s.record(s.next(), CORRECT)
        self.assertEqual(len(s.states), 30)

    def test_due_reviews_come_before_new_and_new_is_rationed(self):
        qs = make_questions(20)
        states = {f"d-c{c}": ConceptState(f"d-c{c}", box=2, due_at=T0 - DAY, last_seen=T0 - 4 * DAY)
                  for c in range(10)}
        s = session(qs, states=states)
        picks = []
        for _ in range(9):
            q = s.next()
            picks.append(q.concept_id in states and states[q.concept_id].reviews == 0)
            s.record(q, CORRECT)
        new_count = sum(1 for cid in s.states if int(cid.split("c")[-1]) >= 10)
        self.assertLessEqual(new_count, 3)
        self.assertGreaterEqual(new_count, 2)


class Variety(unittest.TestCase):
    def test_no_three_of_the_same_type_in_a_row_when_avoidable(self):
        s = session(make_questions(30))
        types = []
        for _ in range(25):
            q = s.next()
            types.append(q.type)
            s.record(q, CORRECT)
        runs = [types[i] == types[i + 1] == types[i + 2] for i in range(len(types) - 2)]
        self.assertFalse(any(runs), types)

    def test_least_seen_variant_is_preferred(self):
        qs = make_questions(1)
        s = Session(qs, {}, {"d-c0-0": 5, "d-c0-1": 0, "d-c0-2": 5}, Config(), rng=random.Random(0), clock=Clock())
        self.assertEqual(s.next().id, "d-c0-1")

    def test_session_never_runs_dry(self):
        s = session(make_questions(3))
        for _ in range(50):
            q = s.next()
            self.assertIsNotNone(q)
            s.record(q, CORRECT)

    def test_new_concepts_interleave_decks(self):
        qs = make_questions(5, deck="a") + make_questions(5, deck="b")
        s = session(qs)
        decks = []
        for _ in range(4):
            q = s.next()
            decks.append(q.deck_id)
            s.record(q, CORRECT)
        self.assertEqual(set(decks), {"a", "b"})


class FollowsPerformance(unittest.TestCase):
    def test_repeatedly_missed_concept_comes_back_sooner(self):
        for seed in range(20):
            states = {"d-c0": ConceptState("d-c0", box=0, weak=0.7)}
            s = session(make_questions(30), states=states, seed=seed)
            q = next(x for x in s.concepts["d-c0"])
            s.current = q
            s.record(q, MISSED)
            self.assertLessEqual(s.requeue["d-c0"] - s.count, 6)  # 3..6 instead of 3..10

    def test_correct_after_a_miss_gets_one_more_check_later(self):
        s = session(make_questions(30))
        q = s.next()
        s.record(q, MISSED)
        while True:
            nq = s.next()
            if nq.concept_id == q.concept_id:
                break
            s.record(nq, CORRECT)
        s.record(nq, CORRECT)
        gap = s.requeue[q.concept_id] - s.count
        self.assertGreaterEqual(gap, 11)
        self.assertLessEqual(gap, 20)
        # Answering it right again lets it go.
        s.current = nq
        s.record(nq, CORRECT)
        self.assertNotIn(q.concept_id, s.requeue)

    def test_fallback_prefers_weak_concepts_over_strong_not_due_ones(self):
        later = T0 + 5 * DAY
        states = {}
        for c in range(40):
            strong = c < 20
            states[f"d-c{c}"] = ConceptState(f"d-c{c}", box=2, due_at=later, last_seen=T0 - DAY,
                                             weak=0.0 if strong else 0.5, streak=3 if strong else 0)
        cfg = Config(new_concept_cap=0)
        s = session(make_questions(40), states=states, cfg=cfg)
        counts = {"strong": 0, "weak": 0}
        for _ in range(40):
            q = s.next()
            counts["strong" if int(q.concept_id[3:]) < 20 else "weak"] += 1
            s.record(q, SHAKY)  # keeps every concept eligible without changing its strength much
            s.states[q.concept_id].due_at = later
            s.states[q.concept_id].weak = states[q.concept_id].weak
            s.states[q.concept_id].streak = states[q.concept_id].streak
        self.assertEqual(counts["strong"], 0)

    def test_concept_answered_right_this_session_is_not_drilled_again(self):
        later = T0 + 5 * DAY
        states = {f"d-c{c}": ConceptState(f"d-c{c}", box=1, due_at=later, weak=0.3) for c in range(20)}
        s = session(make_questions(20), states=states, cfg=Config(new_concept_cap=0))
        right = set()
        for _ in range(15):
            q = s.next()
            self.assertNotIn(q.concept_id, right)
            s.record(q, CORRECT)
            right.add(q.concept_id)


class Cram(unittest.TestCase):
    def test_concept_becomes_solid_in_one_session_then_stops_coming_back(self):
        for seed in range(10):
            s = session(make_questions(30), cfg=Config(cram=True), seed=seed)
            first = s.next()
            cid = first.concept_id
            asked = []
            for _ in range(60):
                q = s.next()
                if q.concept_id == cid:
                    asked.append(q.id)
                s.record(q, CORRECT)
                if sch.status(s.states[cid], s.cfg) == "solid":
                    break
            self.assertEqual(sch.status(s.states[cid], s.cfg), "solid", f"seed {seed}")
            self.assertEqual(len(asked), 3)
            self.assertGreater(len(set(asked)), 1)  # different variants
            self.assertNotIn(cid, s.requeue)

    def test_learning_concepts_not_yet_due_are_asked(self):
        later = T0 + 5 * DAY
        states = {"d-c0": ConceptState("d-c0", box=2, due_at=later),
                  "d-c1": ConceptState("d-c1", box=3, due_at=later)}
        s = session(make_questions(2), states=states, cfg=Config(cram=True, new_concept_cap=0))
        self.assertEqual(s.next().concept_id, "d-c0")

    def test_shaky_keeps_coming_back(self):
        s = session(make_questions(30), cfg=Config(cram=True))
        q = s.next()
        s.record(q, SHAKY)
        self.assertIn(q.concept_id, s.requeue)
        s.states[q.concept_id].box = 1
        s.record(q, SHAKY)
        self.assertIn(q.concept_id, s.requeue)


class AppFlow(unittest.TestCase):
    """End-to-end through the App (no HTTP): answer, persist, reload, edit answer key."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        (self.dir / "questions").mkdir()
        src = Path(__file__).resolve().parent / "fixtures" / "sample-all-types.md"
        self.qfile = self.dir / "questions" / "sample.md"
        self.qfile.write_text(src.read_text())
        self.clock = Clock()

    def tearDown(self):
        self.tmp.cleanup()

    def app(self):
        return App(self.dir, Config(), Store(self.dir / "data" / "p.db"), clock=self.clock)

    def test_progress_survives_restart_and_answer_key_change_makes_due(self):
        app = self.app()
        home = app.home()
        self.assertEqual(home["decks"][0]["counts"]["unseen"], 5)
        sid = app.start(["sample"])["session"]
        q = app.next(sid)["question"]
        fb = app.answer(sid, {"qid": q["qid"], "dont_know": True})
        self.assertEqual(fb["verdict"], MISSED)
        self.assertTrue(fb["explanation"])

        # Restart: a fresh App reads the same database.
        app2 = self.app()
        self.assertEqual(app2.home()["decks"][0]["counts"]["learning"], 1)

        # Answer a whaling question correctly so its concept is due tomorrow, then change its answer key.
        sid = app2.start(["sample"])["session"]
        s = app2.sessions[sid]
        whaling = next(x for x in s.concepts["whaling"] if x.id == "s-whaling-1")
        s.current = whaling
        right = next(i for i, o in enumerate(whaling.options) if o.correct)
        app2.answer(sid, {"qid": whaling.id, "response": {"choice": right}})
        self.assertGreater(app2.states["whaling"].due_at, self.clock.t)

        self.qfile.write_text(self.qfile.read_text().replace("- [ ] Vishing", "- [ ] Vishing over the phone"))
        home = app2.home()
        self.assertEqual(app2.states["whaling"].due_at, self.clock.t)
        self.assertNotIn("notices", home)  # re-checked quietly, no banner

    def test_reset_progress_erases_everything(self):
        app = self.app()
        sid = app.start(["sample"])["session"]
        q = app.next(sid)["question"]
        app.answer(sid, {"qid": q["qid"], "dont_know": True})
        self.assertEqual(app.home()["decks"][0]["counts"]["learning"], 1)

        app.reset_progress()
        self.assertEqual(app.home()["decks"][0]["counts"]["unseen"], 5)
        self.assertEqual(app.store.seen_counts(), {})
        self.assertEqual(app.next(sid), {"error": "session not found", "expired": True})
        self.assertEqual(self.app().home()["decks"][0]["counts"]["unseen"], 5)

    def test_cram_toggle_overrides_config_and_persists(self):
        app = App(self.dir, Config(cram=True), Store(self.dir / "data" / "p.db"), clock=self.clock)
        self.assertTrue(app.home()["cram"])
        app.set_cram(False)
        self.assertFalse(app.home()["cram"])
        app2 = App(self.dir, Config(cram=True), Store(self.dir / "data" / "p.db"), clock=self.clock)
        self.assertFalse(app2.cfg.cram)

    def test_present_never_leaks_answers(self):
        app = self.app()
        lib = app.library()
        for q in lib.questions():
            d = present(q, random.Random(0))
            d.pop("qid")
            blob = repr(d)
            self.assertNotIn("'correct'", blob)
            self.assertNotIn("why", blob)
            if q.type == "typed":
                for a in q.accept:
                    self.assertNotIn(a, blob.replace(q.stem, ""))

    def test_order_is_never_presented_already_solved(self):
        app = self.app()
        q = next(x for x in app.library().questions() if x.type == "order")
        for seed in range(30):
            items = present(q, random.Random(seed))["items"]
            self.assertNotEqual([i["idx"] for i in items], list(range(len(items))))

    def test_progress_view_runs(self):
        app = self.app()
        sid = app.start(["sample"])["session"]
        for _ in range(4):
            q = app.next(sid)["question"]
            app.answer(sid, {"qid": q["qid"], "dont_know": True})
        p = app.progress()
        topics = p["decks"][0]["topics"]
        self.assertTrue(any(t["misses"] for t in topics))
        summary = app.end(sid)
        self.assertEqual(summary["missed"], 4)
        self.assertTrue(summary["missed_topics"])


if __name__ == "__main__":
    unittest.main()


class Migration(unittest.TestCase):
    def test_old_database_gets_weak_and_streak_from_its_history(self):
        import sqlite3
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "old.db"
            db = sqlite3.connect(path)
            db.executescript("""
                CREATE TABLE answers (id INTEGER PRIMARY KEY, ts REAL NOT NULL, session_id TEXT NOT NULL,
                    question_id TEXT NOT NULL, concept_id TEXT NOT NULL, deck_id TEXT NOT NULL, topic TEXT NOT NULL,
                    qtype TEXT NOT NULL, verdict TEXT NOT NULL, low_conf INTEGER NOT NULL, dont_know INTEGER NOT NULL,
                    response TEXT, ms_taken INTEGER);
                CREATE TABLE concepts (concept_id TEXT PRIMARY KEY, box INTEGER NOT NULL, due_at REAL NOT NULL,
                    misses INTEGER NOT NULL, reviews INTEGER NOT NULL, last_seen REAL NOT NULL,
                    last_qid TEXT NOT NULL, last_type TEXT NOT NULL, evidence TEXT NOT NULL);
                INSERT INTO concepts VALUES ('a', 1, 0, 2, 4, 0, 'a-1', 'single', '[]');
                INSERT INTO concepts VALUES ('b', 2, 0, 0, 2, 0, 'b-1', 'single', '[]');
            """)
            for ts, cid, verdict in [(1, "a", "missed"), (2, "b", "correct"), (3, "a", "missed"),
                                     (4, "b", "correct"), (5, "a", "correct")]:
                db.execute("INSERT INTO answers (ts, session_id, question_id, concept_id, deck_id, topic, qtype,"
                           " verdict, low_conf, dont_know) VALUES (?, 's', ?, ?, 'd', 't', 'single', ?, 0, 0)",
                           (ts, cid + "-1", cid, verdict))
            db.commit()
            db.close()
            store = Store(path)
            states = store.load_states()
            self.assertAlmostEqual(states["a"].weak, 0.384)
            self.assertEqual((states["a"].streak, states["a"].box, states["a"].misses), (1, 1, 2))
            self.assertEqual((states["b"].weak, states["b"].streak), (0.0, 2))
            store.save_state(states["a"])  # writing works with the new columns
            store.db.close()
