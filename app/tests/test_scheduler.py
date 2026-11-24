import unittest

from studyapp import scheduler as sch
from studyapp.scheduler import CORRECT, DAY, MISSED, SHAKY, Config, ConceptState

T0 = 1_700_000_000.0  # fixed clock
CFG = Config()


def run(state, verdict, qid="q1", now=T0, n_variants=3):
    return sch.apply(state, verdict, qid, "single", n_variants, now, CFG)


class Boxes(unittest.TestCase):
    def test_new_correct_goes_to_box_1_due_tomorrow(self):
        s = run(ConceptState("c"), CORRECT)
        self.assertEqual(s.box, 1)
        self.assertAlmostEqual(s.due_at, T0 + DAY)
        self.assertEqual(sch.status(s, CFG), "learning")

    def test_miss_resets_to_box_0_due_now_and_clears_evidence(self):
        s = ConceptState("c", box=4, evidence=[["q1", "2024-01-01"], ["q2", "2024-01-02"]])
        s = run(s, MISSED)
        self.assertEqual((s.box, s.due_at, s.misses, s.evidence), (0, T0, 1, []))

    def test_shaky_keeps_box_and_halves_interval(self):
        s = run(ConceptState("c", box=4), SHAKY)
        self.assertEqual(s.box, 4)
        self.assertAlmostEqual(s.due_at, T0 + 7 * DAY)  # box 4 = 14 days, halved

    def test_shaky_minimum_one_day(self):
        s = run(ConceptState("c", box=1), SHAKY)
        self.assertAlmostEqual(s.due_at, T0 + DAY)

    def test_shaky_in_box_0_stays_due(self):
        s = run(ConceptState("c", box=0), SHAKY)
        self.assertEqual((s.box, s.due_at), (0, T0))

    def test_box_caps_at_max(self):
        s = run(ConceptState("c", box=CFG.max_box, evidence=[["a", "d1"], ["b", "d2"]]), CORRECT)
        self.assertEqual(s.box, CFG.max_box)

    def test_unseen_status(self):
        self.assertEqual(sch.status(None, CFG), "unseen")


class AntiLuckGate(unittest.TestCase):
    def test_same_variant_cannot_pass_box_2(self):
        s = ConceptState("c")
        for day in range(4):
            s = run(s, CORRECT, qid="q1", now=T0 + day * 5 * DAY)
        self.assertEqual(s.box, 2)
        self.assertEqual(sch.status(s, CFG), "learning")

    def test_two_variants_same_day_cannot_pass_box_2(self):
        s = ConceptState("c", box=2)
        s = run(s, CORRECT, qid="q1")
        s = run(s, CORRECT, qid="q2", now=T0 + 60)
        self.assertEqual(s.box, 2)

    def test_two_variants_on_two_days_passes(self):
        s = ConceptState("c")
        s = run(s, CORRECT, qid="q1", now=T0)
        s = run(s, CORRECT, qid="q2", now=T0 + 2 * DAY)
        s = run(s, CORRECT, qid="q1", now=T0 + 6 * DAY)
        self.assertEqual(s.box, 3)
        self.assertEqual(sch.status(s, CFG), "solid")

    def test_single_variant_concept_is_not_gated(self):
        s = ConceptState("c")
        for i in range(3):
            s = run(s, CORRECT, qid="only", n_variants=1, now=T0 + i * 10 * DAY)
        self.assertEqual(s.box, 3)

    def test_shaky_answers_are_not_evidence(self):
        s = ConceptState("c", box=2, evidence=[["q1", "2024-01-01"]])
        s = run(s, SHAKY, qid="q2")
        self.assertEqual(s.evidence, [["q1", "2024-01-01"]])

    def test_gate_helper(self):
        self.assertFalse(sch.gate_passed([["a", "d1"], ["a", "d2"]]))
        self.assertFalse(sch.gate_passed([["a", "d1"], ["b", "d1"]]))
        self.assertTrue(sch.gate_passed([["a", "d1"], ["b", "d1"], ["b", "d2"]]))

    def test_gate_without_days(self):
        self.assertTrue(sch.gate_passed([["a", "d1"], ["b", "d1"]], need_days=False))
        self.assertFalse(sch.gate_passed([["a", "d1"], ["a", "d1"]], need_days=False))

    def test_cram_two_variants_same_day_passes(self):
        cfg = Config(cram=True)
        s = ConceptState("c")
        for i, qid in enumerate(["q1", "q2", "q1"]):
            s = sch.apply(s, CORRECT, qid, "single", 3, T0 + i * 60, cfg)
        self.assertEqual(sch.status(s, cfg), "solid")

    def test_cram_same_variant_still_cannot_pass_box_2(self):
        cfg = Config(cram=True)
        s = ConceptState("c")
        for i in range(4):
            s = sch.apply(s, CORRECT, "q1", "single", 3, T0 + i * 60, cfg)
        self.assertEqual(s.box, 2)


class Misc(unittest.TestCase):
    def test_verdicts(self):
        self.assertEqual(sch.verdict_for(True, False, False), CORRECT)
        self.assertEqual(sch.verdict_for(True, True, False), SHAKY)
        self.assertEqual(sch.verdict_for(False, False, False), MISSED)
        self.assertEqual(sch.verdict_for(True, False, True), MISSED)

    def test_urgency_puts_box_0_first(self):
        a = ConceptState("a", box=0, due_at=T0)
        b = ConceptState("b", box=3, due_at=T0 - 30 * DAY)
        self.assertGreater(sch.urgency(a, T0, CFG), sch.urgency(b, T0, CFG))

    def test_answer_key_change(self):
        s = ConceptState("c", box=4, due_at=T0 + 10 * DAY, evidence=[["q1", "d1"], ["q2", "d2"]])
        s = sch.mark_answer_key_changed(s, "q1", T0)
        self.assertEqual(s.due_at, T0)
        self.assertEqual(s.evidence, [["q2", "d2"]])

    def test_load_config_overrides(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "c.toml"
            p.write_text("[scheduling]\nnew_concept_cap = 4\n[server]\nport = 9000\n")
            cfg = sch.load_config(p)
            self.assertEqual((cfg.new_concept_cap, cfg.port, cfg.solid_box), (4, 9000, 3))
        self.assertEqual(sch.load_config("/nonexistent.toml"), Config())


if __name__ == "__main__":
    unittest.main()


class Weakness(unittest.TestCase):
    def test_misses_raise_weakness_and_correct_answers_lower_it(self):
        s = ConceptState("c")
        s = run(s, MISSED)
        self.assertAlmostEqual(s.weak, 0.4)
        s = run(s, MISSED)
        self.assertAlmostEqual(s.weak, 0.64)
        s = run(s, CORRECT)
        self.assertAlmostEqual(s.weak, 0.384)
        self.assertEqual(s.streak, 1)

    def test_streak_counts_confident_corrects_only(self):
        s = run(run(ConceptState("c"), CORRECT), CORRECT)
        self.assertEqual(s.streak, 2)
        self.assertTrue(sch.is_strong(s))
        self.assertEqual(run(s, SHAKY).streak, 0)
        self.assertEqual(run(s, MISSED).streak, 0)

    def test_weak_concepts_come_back_sooner(self):
        strong = run(ConceptState("c", box=1), CORRECT)
        weak = run(ConceptState("c", box=1, weak=0.8), CORRECT)
        self.assertAlmostEqual(strong.due_at, T0 + 3 * DAY)
        self.assertLess(weak.due_at, strong.due_at)
