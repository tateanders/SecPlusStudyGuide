import random
import shutil
import tempfile
import unittest
from pathlib import Path

from studyapp.exam import allocate, build_exam
from studyapp.model import Deck, Question
from studyapp.scheduler import MISSED, SHAKY, Config
from studyapp.server import App
from studyapp.store import Store

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def deck(did, n_concepts, weight=None, variants=2):
    d = Deck(id=did, path=f"{did}.md", name=did.upper(), exam_weight=weight)
    for c in range(n_concepts):
        for v in range(variants):
            d.questions.append(Question(id=f"{did}-c{c}-{v}", type="single", file=d.path, line=1,
                                        topic="1", group=f"{did}-c{c}", deck_id=did))
    return d


class Allocation(unittest.TestCase):
    def test_follows_exam_weight(self):
        decks = [deck("a", 50, 25), deck("b", 50, 75)]
        self.assertEqual(allocate(decks, {"a": 50, "b": 50}, 40), {"a": 10, "b": 30})

    def test_without_weights_uses_concept_counts(self):
        decks = [deck("a", 30), deck("b", 10)]
        self.assertEqual(allocate(decks, {"a": 30, "b": 10}, 20), {"a": 15, "b": 5})

    def test_small_deck_gives_its_leftover_to_others(self):
        decks = [deck("a", 3, 50), deck("b", 40, 50)]
        self.assertEqual(allocate(decks, {"a": 3, "b": 40}, 20), {"a": 3, "b": 17})

    def test_exam_shrinks_when_there_are_too_few_concepts(self):
        decks = [deck("a", 4), deck("b", 3)]
        self.assertEqual(sum(allocate(decks, {"a": 4, "b": 3}, 90).values()), 7)


class Build(unittest.TestCase):
    def test_one_question_per_concept_and_least_seen_variant(self):
        decks = [deck("a", 20, 50), deck("b", 20, 50)]
        qs = [q for d in decks for q in d.questions]
        seen = {q.id: 5 for q in qs if q.id.endswith("-0")}
        exam = build_exam(qs, decks, 30, random.Random(1), seen)
        self.assertEqual(len(exam), 30)
        self.assertEqual(len({q.concept_id for q in exam}), 30)
        self.assertTrue(all(q.id.endswith("-1") for q in exam))

    def test_scenario_questions_come_first(self):
        d = deck("a", 10, variants=1)
        d.questions[0].type = "pbq"
        exam = build_exam(d.questions, [d], 10, random.Random(3), {})
        self.assertEqual(exam[0].type, "pbq")


class ExamFlow(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        (self.dir / "questions").mkdir()
        shutil.copy(FIXTURES / "sample-all-types.md", self.dir / "questions" / "sample.md")
        self.app = App(self.dir, Config(exam_questions=90), Store(self.dir / "data" / "p.db"))

    def tearDown(self):
        self.tmp.cleanup()

    def test_start_never_leaks_answers(self):
        r = self.app.start_exam(["sample"])
        self.assertTrue(r["questions"])
        text = str(r["questions"])
        for bad in ("correct", "explanation", "why", "accept"):
            self.assertNotIn(f"'{bad}'", text)

    def test_finish_grades_records_and_schedules(self):
        r = self.app.start_exam(["sample"])
        ex = self.app.exams[r["exam"]]
        singles = [q for q in ex.questions if q.type == "single"]
        right = singles[0]
        responses = {right.id: {"choice": next(i for i, o in enumerate(right.options) if o.correct)}}
        out = self.app.finish_exam(r["exam"], {"responses": responses, "flagged": [right.id]})
        self.assertEqual(out["total"], len(ex.questions))
        self.assertEqual(out["correct"], 1)
        self.assertEqual(out["unanswered"], len(ex.questions) - 1)
        verdicts = {it["qid"]: it["verdict"] for it in out["items"]}
        self.assertEqual(verdicts[right.id], SHAKY)  # flagged but right
        self.assertTrue(all(v == MISSED for q, v in verdicts.items() if q != right.id))
        self.assertTrue(all(it["fb"]["explanation"] for it in out["items"]))
        for q in ex.questions:
            self.assertIn(q.concept_id, self.app.states)
        self.assertEqual(len(self.app.store.answers_since(0)), len(ex.questions))
        self.assertNotIn(r["exam"], self.app.exams)


if __name__ == "__main__":
    unittest.main()
