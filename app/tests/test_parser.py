import re
import tempfile
import textwrap
import unittest
from pathlib import Path

from studyapp.parser import Loader, parse_file, parse_text, validate_paths

ROOT = Path(__file__).resolve().parents[2]  # the Study Guide folder, where FORMAT.md lives
SAMPLE = Path(__file__).resolve().parent / "fixtures" / "sample-all-types.md"

HEADER = "---\ndeck: Test\n---\n\n"


def parse(body: str):
    return parse_text(HEADER + textwrap.dedent(body), "t.md")


def errors(issues):
    return [i for i in issues if i.level == "error"]


GOOD_SINGLE = """\
## t-1
type: single
topic: 1.1
group: g

Which one?

### Options
- [x] Right
- [ ] Wrong A
  why: because A
- [ ] Wrong B
  why: because B
- [ ] Wrong C
  why: because C

### Explanation
Because.
"""


class SampleFile(unittest.TestCase):
    def test_sample_parses_cleanly(self):
        deck, issues = parse_file(SAMPLE)
        self.assertEqual([str(i) for i in issues if i.level == "error"], [])
        types = {q.type for q in deck.questions}
        self.assertEqual(types, {"single", "multi", "typed", "order", "match", "pbq"})

    def test_sample_has_no_warnings_when_loaded_as_library(self):
        lib = Loader(SAMPLE.parent).load()
        sample_issues = [str(i) for i in lib.issues if Path(i.file).name == SAMPLE.name]
        self.assertEqual(sample_issues, [])

    def test_pbq_parts_attach_to_parent(self):
        deck, _ = parse_file(SAMPLE)
        pbq = next(q for q in deck.questions if q.type == "pbq")
        self.assertEqual([p.type for p in pbq.parts], ["single", "multi", "typed"])
        self.assertTrue(all(p.topic == pbq.topic for p in pbq.parts))
        self.assertIn("203.0.113.45", pbq.exhibit)
        self.assertTrue(all(p.concept_id == pbq.concept_id or p.is_part for p in pbq.parts))


class FormatDocExamples(unittest.TestCase):
    """Every complete example in FORMAT.md must parse without errors."""

    def test_format_examples_parse(self):
        text = (ROOT / "FORMAT.md").read_text(encoding="utf-8")
        blocks = re.findall(r"^(`{3,4})markdown\n(.*?)^\1\s*$", text, re.M | re.S)
        examples = [b for _, b in blocks if re.search(r"^## [a-z0-9]", b, re.M) and "type:" in b
                    and not re.search(r"^\.\.\.$", b, re.M)]  # skip the layout skeleton with placeholders
        self.assertGreaterEqual(len(examples), 6)
        seen_types = set()
        for ex in examples:
            deck, issues = parse_text(HEADER + ex, "FORMAT.md")
            self.assertEqual([str(i) for i in errors(issues)], [], ex[:80])
            seen_types |= {q.type for q in deck.questions}
        self.assertEqual(seen_types, {"single", "multi", "typed", "order", "match", "pbq"})


class Basics(unittest.TestCase):
    def test_single(self):
        deck, issues = parse(GOOD_SINGLE)
        self.assertEqual(errors(issues), [])
        q = deck.questions[0]
        self.assertEqual(q.id, "t-1")
        self.assertEqual(q.concept_id, "g")
        self.assertEqual([o.correct for o in q.options], [True, False, False, False])
        self.assertEqual(q.options[1].why, "because A")
        self.assertEqual(q.stem, "Which one?")

    def test_front_matter_topics(self):
        deck, _ = parse_text("---\ndeck: D\nsection: \"2.0\"\ntopics:\n  2.1: Threat actors\n  2.2: Vectors\n---\n", "x.md")
        self.assertEqual(deck.name, "D")
        self.assertEqual(deck.section, "2.0")
        self.assertEqual(deck.topics, {"2.1": "Threat actors", "2.2": "Vectors"})

    def test_default_topic_from_front_matter(self):
        deck, issues = parse_text("---\ndeck: D\ntopic: ch3\n---\n\n" + GOOD_SINGLE.replace("topic: 1.1\n", ""), "x.md")
        self.assertEqual(errors(issues), [])
        self.assertEqual(deck.questions[0].topic, "ch3")

    def test_heading_inside_code_fence_is_not_a_question(self):
        body = GOOD_SINGLE.replace("Which one?", "Which one?\n\n```text\n## not-a-question\n### Options\n```")
        deck, issues = parse(body)
        self.assertEqual(errors(issues), [])
        self.assertEqual(len(deck.questions), 1)
        self.assertIn("## not-a-question", deck.questions[0].stem)

    def test_ungrouped_question_is_its_own_concept(self):
        deck, _ = parse(GOOD_SINGLE.replace("group: g\n", ""))
        self.assertEqual(deck.questions[0].concept_id, "q:t-1")

    def test_typed_wrong_answers_both_styles(self):
        deck, issues = parse("""\
            ## t-2
            type: typed
            topic: 1

            What?

            ### Accept
            - alpha

            ### Wrong answers
            - beta: inline why
            - gamma
              why: indented why

            ### Explanation
            x
            """)
        self.assertEqual(errors(issues), [])
        self.assertEqual(deck.questions[0].wrong_answers, [("beta", "inline why"), ("gamma", "indented why")])

    def test_answer_key_hash_ignores_wording(self):
        a, _ = parse(GOOD_SINGLE)
        b, _ = parse(GOOD_SINGLE.replace("Which one?", "Which one is it?").replace("Because.", "Reworded."))
        c, _ = parse(GOOD_SINGLE.replace("- [x] Right", "- [ ] Right\n  why: x").replace("- [ ] Wrong A", "- [x] Wrong A"))
        self.assertEqual(a.questions[0].answer_key_hash(), b.questions[0].answer_key_hash())
        self.assertNotEqual(a.questions[0].answer_key_hash(), c.questions[0].answer_key_hash())


class Errors(unittest.TestCase):
    def assertError(self, body, fragment, line=None):
        deck, issues = parse(body)
        errs = errors(issues)
        self.assertTrue(any(fragment in i.message for i in errs), [str(i) for i in errs])
        if line is not None:
            self.assertTrue(any(i.line == line for i in errs if fragment in i.message), [str(i) for i in errs])
        return deck

    def test_missing_type_skips_question(self):
        deck = self.assertError(GOOD_SINGLE.replace("type: single\n", ""), "missing 'type:'", line=5)
        self.assertEqual(deck.questions, [])

    def test_unknown_type(self):
        self.assertError(GOOD_SINGLE.replace("type: single", "type: essay"), "unknown type")

    def test_single_with_two_correct(self):
        self.assertError(GOOD_SINGLE.replace("- [ ] Wrong A", "- [x] Wrong A"), "exactly one [x]")

    def test_multi_with_one_correct(self):
        self.assertError(GOOD_SINGLE.replace("type: single", "type: multi"), "at least 2 [x]")

    def test_bad_option_marker(self):
        self.assertError(GOOD_SINGLE.replace("- [ ] Wrong B", "- Wrong B"), "option must start with", line=16)

    def test_missing_explanation(self):
        self.assertError(GOOD_SINGLE.split("### Explanation")[0], "missing '### Explanation'")

    def test_unknown_section(self):
        self.assertError(GOOD_SINGLE.replace("### Explanation", "### Answer"), "unknown section")

    def test_bad_id(self):
        self.assertError(GOOD_SINGLE.replace("## t-1", "## T 1"), "invalid question id")

    def test_duplicate_id_keeps_first(self):
        deck, issues = parse(GOOD_SINGLE + "\n" + GOOD_SINGLE)
        self.assertEqual(len(deck.questions), 1)
        self.assertTrue(any("duplicate id" in i.message for i in errors(issues)))

    def test_bad_question_does_not_affect_good_one(self):
        bad = GOOD_SINGLE.replace("t-1", "t-2").replace("type: single\n", "")
        deck, issues = parse(GOOD_SINGLE + "\n" + bad)
        self.assertEqual([q.id for q in deck.questions], ["t-1"])

    def test_match_pair_syntax(self):
        self.assertError("""\
            ## m-1
            type: match
            topic: 1

            Match.

            ### Match
            - a => 1
            - b -> 2

            ### Explanation
            x
            """, "match pairs look like")

    def test_pbq_part_without_parent(self):
        self.assertError("""\
            ## p-1/a
            type: single

            Q?

            ### Options
            - [x] a
            - [ ] b
              why: no
            """, "parent 'p-1' not found")

    def test_pbq_with_broken_part_is_skipped(self):
        deck, issues = parse("""\
            ## p-1
            type: pbq
            topic: 1

            Scenario.

            ### Explanation
            x

            ## p-1/a
            type: single

            Q?

            ### Options
            - [ ] a
              why: no
            - [ ] b
              why: no
            """)
        self.assertEqual(deck.questions, [])
        self.assertTrue(any("PBQ skipped" in i.message for i in errors(issues)))

    def test_pbq_without_parts(self):
        self.assertError("""\
            ## p-2
            type: pbq
            topic: 1

            Scenario.

            ### Explanation
            x
            """, "PBQ has no parts")

    def test_unclosed_front_matter(self):
        _, issues = parse_text("---\ndeck: D\n\n## a\n", "x.md")
        self.assertTrue(any("never closed" in i.message for i in errors(issues)))


class Warnings(unittest.TestCase):
    def warns(self, body):
        _, issues = parse(body)
        return [i.message for i in issues if i.level == "warn"]

    def test_missing_why(self):
        w = self.warns(GOOD_SINGLE.replace("  why: because A\n", ""))
        self.assertTrue(any("has no 'why:'" in m for m in w))

    def test_longest_correct_option(self):
        w = self.warns(GOOD_SINGLE.replace("- [x] Right", "- [x] Right, because of a long and detailed qualifying reason"))
        self.assertTrue(any("characters longer than the longest wrong option" in m for m in w))

    def test_correct_option_may_lead_by_up_to_10_characters(self):
        # The longest wrong option is "Wrong A" (7 characters).
        for extra, flagged in ((9, False), (10, False), (11, True)):
            w = self.warns(GOOD_SINGLE.replace("- [x] Right", "- [x] " + "R" * (7 + extra)))
            self.assertEqual(any("characters longer" in m for m in w), flagged, extra)

    def test_typed_stem_containing_the_answer(self):
        body = """\
            ## t-2
            type: typed
            topic: 1
            group: g

            Alice sends Bob a secret. Which key does she encrypt it with? Answer like "Bob's public key".

            ### Accept
            - Bob's public key
            - public key

            ### Explanation
            x
            """
        self.assertTrue(any("stem contains the accepted answer" in m for m in self.warns(body)))
        clean = body.replace(' Answer like "Bob\'s public key".', " Name whose key and which kind.")
        self.assertFalse(any("stem contains" in m for m in self.warns(clean)))

    def test_typed_stem_naming_the_answer_to_exclude_it(self):
        body = """\
            ## t-3
            type: typed
            topic: 1
            group: g

            Script in a comment runs in other visitors' browsers. Name the attack (do not give the XSS type).

            ### Accept
            - XSS
            - cross-site scripting

            ### Explanation
            x
            """
        self.assertTrue(any("stem contains the accepted answer 'XSS'" in m for m in self.warns(body)))

    def test_choice_stem_echoing_only_the_correct_option(self):
        w = self.warns(GOOD_SINGLE.replace("Which one?", "Which one is the Right Answer?").replace("- [x] Right", "- [x] Right Answer"))
        self.assertTrue(any("stem contains the correct option" in m for m in w))
        self.assertFalse(any("stem contains" in m for m in self.warns(GOOD_SINGLE)))

    def test_all_of_the_above(self):
        w = self.warns(GOOD_SINGLE.replace("Wrong C", "All of the above"))
        self.assertTrue(any("all/none of the above" in m for m in w))

    def test_single_variant_group(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "a.md"
            p.write_text(HEADER + GOOD_SINGLE)
            _, issues = validate_paths([str(p)])
            self.assertTrue(any("only one variant" in i.message for i in issues))


class LoaderTests(unittest.TestCase):
    def test_duplicate_across_files_and_reload(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "a.md").write_text(HEADER + GOOD_SINGLE)
            (Path(d) / "b.md").write_text(HEADER + GOOD_SINGLE)
            (Path(d) / "_aliases.md").write_text("- MFA = multifactor authentication\n")
            loader = Loader(d)
            lib = loader.load()
            self.assertEqual([len(x.questions) for x in lib.decks], [1, 0])
            self.assertTrue(any("already used at" in i.message for i in lib.issues))
            self.assertEqual(lib.aliases, [{"MFA", "multifactor authentication"}])
            # Edit a file: the loader picks it up.
            (Path(d) / "b.md").write_text(HEADER + GOOD_SINGLE.replace("t-1", "t-9"))
            lib = loader.load()
            self.assertEqual([len(x.questions) for x in lib.decks], [1, 1])


if __name__ == "__main__":
    unittest.main()
