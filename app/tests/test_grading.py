import unittest
from pathlib import Path

from studyapp.grading import canon, grade, typed_matches
from studyapp.parser import parse_file

SAMPLE = Path(__file__).resolve().parent / "fixtures" / "sample-all-types.md"


def q(qid):
    deck, _ = parse_file(SAMPLE)
    for x in deck.questions:
        if x.id == qid:
            return x
    raise KeyError(qid)


class TypedMatching(unittest.TestCase):
    def test_case_space_punctuation_hyphen(self):
        self.assertTrue(typed_matches("  Pre-Shared   KEY ", ["preshared key"]))
        self.assertTrue(typed_matches("pre shared key", ["Pre-Shared Key"]))
        self.assertTrue(typed_matches("SHA256", ["SHA-256"]))

    def test_leading_article_on_user_side(self):
        self.assertTrue(typed_matches("a firewall", ["firewall"]))
        self.assertTrue(typed_matches("The evil twin", ["evil twin"]))

    def test_article_that_is_part_of_the_answer(self):
        # "A record" (DNS) must not collapse to "record".
        self.assertTrue(typed_matches("A record", ["A record"]))
        self.assertFalse(typed_matches("record", ["A record"]))
        self.assertFalse(typed_matches("AAAA record", ["A record"]))

    def test_no_typo_tolerance(self):
        self.assertFalse(typed_matches("DES", ["AES"]))
        self.assertFalse(typed_matches("SSL", ["SSH"]))
        self.assertFalse(typed_matches("SAM", ["SAML"]))

    def test_no_plural_stripping(self):
        self.assertFalse(typed_matches("HTTP", ["HTTPS"]))
        self.assertFalse(typed_matches("firewalls", ["firewall"]))

    def test_numbers_keep_their_dots(self):
        self.assertTrue(typed_matches("10.0.0.1", ["10.0.0.1"]))
        self.assertFalse(typed_matches("100.0.1", ["10.0.0.1"]))
        self.assertTrue(typed_matches("802.1x", ["802.1X"]))
        self.assertFalse(typed_matches("8021x", ["802.1X"]))
        self.assertTrue(typed_matches("10.0.0.0/8", ["10.0.0.0/8"]))

    def test_aliases(self):
        aliases = [{"MFA", "multifactor authentication"}]
        self.assertTrue(typed_matches("Multi-factor authentication", ["MFA"], aliases))
        self.assertTrue(typed_matches("mfa", ["multifactor authentication"], aliases))
        self.assertFalse(typed_matches("MFA token", ["MFA"], aliases))

    def test_empty_never_matches(self):
        self.assertFalse(typed_matches("", ["x"]))
        self.assertFalse(typed_matches("---", ["x"]))
        self.assertEqual(canon("  "), "")

    def test_wrong_answer_is_identified(self):
        r = grade(q("s-whaling-2"), {"text": "Spear-phishing"})
        self.assertFalse(r["correct"])
        self.assertEqual(r["matched_wrong"]["answer"], "spear phishing")


class Grading(unittest.TestCase):
    def test_single(self):
        x = q("s-whaling-1")
        right = next(i for i, o in enumerate(x.options) if o.correct)
        self.assertTrue(grade(x, {"choice": right})["correct"])
        self.assertFalse(grade(x, {"choice": (right + 1) % 4})["correct"])
        self.assertFalse(grade(x, {"choice": 99})["correct"])

    def test_multi_exact_set(self):
        x = q("s-mfa-inherence-1")
        right = [i for i, o in enumerate(x.options) if o.correct]
        self.assertTrue(grade(x, {"choices": right})["correct"])
        self.assertFalse(grade(x, {"choices": right[:1]})["correct"])
        self.assertFalse(grade(x, {"choices": right + [4]})["correct"])

    def test_order(self):
        x = q("s-ir-order-1")
        self.assertTrue(grade(x, {"sequence": [0, 1, 2, 3, 4]})["correct"])
        r = grade(x, {"sequence": [1, 0, 2, 3, 4]})
        self.assertFalse(r["correct"])
        self.assertEqual(r["positions"], [False, False, True, True, True])

    def test_match_allows_reused_value(self):
        x = q("s-secure-ports-1")
        r = grade(x, {"answers": ["22", "443", "636", "22"]})
        self.assertTrue(r["correct"])
        r = grade(x, {"answers": ["22", "443", "389", "22"]})
        self.assertFalse(r["correct"])
        self.assertEqual(r["rows"], [True, True, False, True])

    def test_pbq_all_or_nothing(self):
        x = q("s-pbq-ssh-spray")
        a, b, c = x.parts
        good = {a.id: {"choice": 0}, b.id: {"choices": [0, 1]}, c.id: {"text": "203.0.113.45"}}
        self.assertTrue(grade(x, {"parts": good})["correct"])
        bad = dict(good, **{c.id: {"text": "203.0.113.4"}})
        r = grade(x, {"parts": bad})
        self.assertFalse(r["correct"])
        self.assertTrue(r["parts"][a.id]["correct"])
        self.assertFalse(r["parts"][c.id]["correct"])

    def test_dont_know_and_malformed(self):
        x = q("s-whaling-1")
        self.assertEqual(grade(x, None), {"correct": False, "dont_know": True})
        self.assertFalse(grade(x, {"choices": "nonsense"})["correct"])
        self.assertFalse(grade(q("s-ir-order-1"), {"sequence": ["x"]})["correct"])


if __name__ == "__main__":
    unittest.main()
