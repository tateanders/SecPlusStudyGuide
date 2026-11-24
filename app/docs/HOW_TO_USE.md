# How to Use the Study App

A quick-reference guide for coming back after time away. Everything runs on your laptop, offline.

## 1. Start studying

The Study Guide folder holds just four things you use: `study.py` (starts the app), `questions/` (your decks), `FORMAT.md` (how to write questions) and this PDF. Everything else (code, settings, your progress) lives in `app/`.


Open Terminal and run:

```
cd ~/Desktop/"Study Guide"
python3 study.py
```

Your browser opens on the home screen. Tick the decks you want (they're remembered from last time), then press **Enter** or click **Start**. That's it.

To stop, close the tab and press **Ctrl+C** in Terminal. Progress is saved after every single answer, so quitting mid-session loses nothing.

Shortcut: if you've added the `study` alias (see the README), just type `study` in any Terminal window.

## 2. The home screen

Each deck (question file) shows:

- **questions**: how many questions the file has.
- **new**: concepts you've never answered.
- **learning**: concepts you've missed recently, answered unsure, or haven't confirmed yet.
- **solid**: concepts you've proven you know (details in section 5).
- **due**: concepts whose review date has arrived.
- The bar: green = solid, amber = learning, grey = new.

You pick which decks to include; the app picks everything else. It decides the mix of due reviews, things you missed, and new material. Sessions never run out; stop whenever you like.

**Exam mode** (press **E**, or click **Exam mode**) gives you a timed practice exam from the selected decks instead. See section 6.

If a question file has a mistake, a yellow box on the home screen lists each problem as `file:line: message`. Those questions are skipped until fixed; the rest of the file still works.

## 3. Answering questions

For every question you have three choices:

- **Answer normally**: you're confident.
- **Answer and mark "Not sure"**: press **L** first, or submit with **Shift+Enter**. Be honest here. A correct-but-unsure answer is treated as shaky and comes back sooner. This is how the app tells "knew it" from "got lucky".
- **Don't know**: press **D**. Counts as a miss. Use it instead of guessing; guessing hides what you don't know.

The buttons sit under the question: **Don't know** and **Not sure** next to **Submit** on the right, and **← Previous** on the left.

**Went past a feedback screen too fast?** Press **B** (or **←**, or click **← Previous**) to bring back the previous question's feedback. Press it again to go further back. **Enter**, **→** or **Esc** brings you back to where you were, with any answer you'd started still filled in. This is review only: answers you already submitted stay recorded.

### Keyboard

| Key | What it does |
|---|---|
| 1 - 9, 0 | Pick an option (toggle it in "select N" questions). 0 = tenth option. |
| Enter | Submit. On the feedback screen: next question. While reviewing: back toward where you were. |
| Shift+Enter | Submit as "Not sure". |
| L | Toggle "Not sure" before submitting. |
| D | Don't know. |
| Esc | Leave a text box (so L, D and number keys work again). |
| Backspace | Ordering questions: undo the last placed item. |
| Up / Down | Matching questions: move between rows. |
| Tab / Shift+Tab | Scenario (PBQ) questions: move between parts. |
| B or ← | Review the previous question's feedback (press again to go further back). |
| → or Esc | While reviewing: go forward again. |
| Q | End the session. |
| P / H | Progress / Home (from the home and summary screens). |

### Question types

- **Pick one**: classic multiple choice.
- **Select N**: pick exactly the right set; partly right counts as missed.
- **Typed answer**: type the term. Case, spaces, hyphens and punctuation don't matter, but spelling does: there's no typo tolerance, because AES/DES and SSH/SSL are one letter apart.
- **Ordering**: press the items in the order they should happen. They appear in "Your order" as you go.
- **Matching**: for each row, press the number of its match (or use the dropdown). Some values match more than one row; some match nothing.
- **Scenario (PBQ)**: an exhibit (log, config, table) plus several parts. Answer every part, then submit once. All parts must be right for it to count as correct.

Options are shuffled every time. A question you miss comes back as the *same* question within about 10 questions, so you can check that the correction stuck. Later reviews of that concept use a *different* question, so memorizing positions or wording doesn't help.

## 4. The feedback screen

After every answer you see, in this order:

1. **The verdict**: Correct (green), Correct but not sure (amber), or Missed / Don't know (red).
2. **Why your answer was wrong**: the explanation for the exact option you picked (or the wrong term you typed, or the wrong match).
3. The question again, with the correct answer marked ✓, your wrong pick marked ✗, and a one-line reason under every wrong option.
4. **Explanation** of the correct answer.
5. The concept's new status and box number.

Press **Enter** (or click **Next**, bottom right) for the next question, or **B** to look at the one before.

## 5. How the app decides what to ask

You don't need to manage any of this, but it helps to know what the labels mean.

**Concepts, not questions.** Questions that test the same idea are grouped (a "variant group"). The app schedules the *concept*, and each time it comes up it asks the variant you've seen least, so you can't memorize one question's wording.

**Boxes.** Each concept sits in a box from 0 to 6:

| Box | Comes back |
|---|---|
| 0 | Later this session (it's being learned) |
| 1 | 1 day |
| 2 | 3 days |
| 3 | 7 days |
| 4 | 14 days |
| 5 | 30 days |
| 6 | 60 days |

- **Correct and confident**: up one box.
- **Correct but not sure**: same box, back in half the time.
- **Missed or Don't know**: back to box 0. The exact question you missed returns 3 to 10 questions later in the same session. If you've missed the concept again and again lately, it comes back sooner (3 to 6 questions).
- **Right after being wrong**: when you get it right after missing it in the same session, the concept comes back once more about 11 to 20 questions later, as a *different* variant, to check that you understood the idea rather than remembered the question.
- **The luck check**: a concept can't go past box 2 until you've answered **two different variants** correctly and confidently, **on two different days**. One lucky guess never makes anything solid.
- **Cram mode** (the *Cram mode* checkbox on the home screen, or press `C` there): no time rules. A concept you get right, or right but not sure, comes back later in the same session as a different variant until it's solid, and the luck check only needs two different variants, not two days. Concepts still in learning from earlier days are asked right away instead of waiting for their date. Three confident correct answers in one session make a concept solid. Turn it off after the exam for normal spaced review. The change applies to the next session you start.

**Status labels:** *new* = never answered. *learning* = box 0 to 2. *solid* = box 3 or higher.

**Your track record counts.** The app keeps a running "weakness" score for every concept. Recent answers count most: misses and Don't know push it up, confident correct answers bring it down. It uses that score to:

- put the concepts you've been missing first when several are due;
- bring them back sooner between days (a concept you keep missing might return in 2 days instead of 3);
- choose what to review when nothing is due. It mostly picks weak concepts, skips anything you've already got right this session, and leaves alone concepts you've answered right several times in a row.

So concepts you keep getting right fade into the background, and the ones you miss keep coming back.

**New material.** New concepts are mixed in about one for every three reviews. If 10 or more concepts are stuck in box 0 (you're missing a lot), new material pauses until those settle. When nothing is due and new material is paused, the app keeps reviewing your weak concepts so a long session never runs dry.

## 6. Exam mode

Exam mode simulates the real test. Select the decks on the home screen, then press **E** (or click **Exam mode**).

- **90 questions, 90 minutes** by default (change them in `app/config.toml`, see Settings). Questions are spread across the selected decks by each deck's `exam_weight` (set in the deck's front matter), with one question per concept. Scenario (PBQ) questions come first, like the real exam.
- **No feedback until the end.** Answer in any order. **→** / **N** / **Enter** go to the next question, **←** / **B** to the previous one, and you can change any answer until you finish.
- **Flag** a question with **F** to come back to it. **R** opens the review grid: every question as a numbered tile, shaded once answered and marked ⚑ if flagged. Click a tile to jump to it.
- **Finish** from the review grid. The app warns you about unanswered and flagged questions first. When the timer runs out, the exam is submitted automatically. The timer turns red in the last 5 minutes.
- **Results** show your percentage, how many you got right, wrong and left blank, a score per domain, the topics you missed, and every question as a green or red tile. Click a tile to see the full answer and explanation.

Exam answers count toward your progress. Unanswered questions count as missed, and a flagged question you got right counts as "not sure", so the questions you missed in the exam come up in your normal study sessions afterwards. Closing or leaving the exam before you finish throws away its answers.

## 7. The Progress screen

Click **Progress** (top right), or press **P** on the home screen. For each deck:

- The overall bar and counts (new / learning / solid / due).
- A line chart of solid (green) and learning (amber) concepts over time, one point per day you studied.
- A **topics table**, sorted by how often you missed each topic over the last 30 days. **Not sure** is the share of correct answers you flagged as unsure. A high Not-sure rate means a topic you're guessing on.

There is no readiness score and no streak. It only shows where you stand.

## 8. Adding and editing questions

1. Put `.md` files in the `questions/` folder. One file per section or domain works well.
2. Refresh the browser home page. New and changed files are picked up automatically; no restart needed.
3. Before dropping a new file in, you can check it:

```
python3 study.py validate questions/new-file.md
```

   With no file names, it checks everything in `questions/`. ERRORs are skipped by the app until fixed; WARNs are writing problems (giveaways, missing explanations) but the question still loads.

The full format is in **FORMAT.md** in the project folder. Key rules to remember:

- Every question starts with `## some-id`. **Progress is tied to that ID.** Reword, reorder or move questions freely, but don't rename IDs.
- If you change a question's correct answer, the app quietly makes that concept due again so you re-check it.
- Deleting a question hides its history; if the ID returns, so does its history.
- `questions/_aliases.md` lists interchangeable terms for typed answers (e.g. `MFA = multifactor authentication`).

## 9. Getting Claude to write questions

1. Open FORMAT.md, scroll to section 5 ("Prompt to give Claude"), and copy the prompt.
2. Fill in the objective (for Security+: e.g. *2.2, Explain common threat vectors and attack surfaces*) and the ID prefix (e.g. `d2-`).
3. Attach or paste FORMAT.md along with the prompt.
4. Save Claude's output as a new `.md` file in `questions/`.
5. Run `python3 study.py validate questions/<file>.md`. If it reports errors **or warnings**, paste them back to Claude and ask it to fix them. A file that follows FORMAT.md should come back with zero warnings. The validator flags stems that contain the answer, and correct options more than 10 characters longer than the longest wrong one.
6. Refresh the home page.

Tip: to avoid duplicate IDs, give Claude the list of existing ones. This command prints them:

```
grep -h '^## ' questions/*.md
```

## 10. Settings

`app/config.toml` holds the tunable numbers. Restart the app after editing.

- `intervals_days`: how long each box waits.
- `cram`: the starting value for cram mode (see section 5). Once you use the home-screen checkbox, the checkbox wins and this line is ignored.
- `new_concept_cap`: how many box-0 concepts pause new material (default 10).
- `new_every`: at most one new concept per this many questions when reviews are waiting (default 3).
- `requeue_min` / `requeue_max`: how many questions later a missed question comes back (default 3 to 10).
- `[exam]` `questions` / `minutes`: exam mode length and time limit (default 90 and 90).
- `port`, `open_browser`.

## 11. Your data

All progress lives in one file: `app/data/progress.db`.

- **Back up:** copy that file somewhere.
- **Start over:** open **Progress** and click **Reset all progress** at the bottom. This erases every answer for every deck (your question files and settings stay). Quitting the app and deleting the file does the same thing.
- **Move to another laptop:** copy the whole Study Guide folder (it includes `app/data/`).
- **Share with someone else:** reset your progress first, or leave out `app/data/` when you copy the folder. It's created again on first run.

## 12. Troubleshooting

- **Browser didn't open:** copy the address Terminal prints (e.g. `http://127.0.0.1:8765/`) into your browser.
- **"Port in use":** the app automatically tries the next port; use the address it prints. You may have a second copy running in another Terminal window.
- **"Can't reach the study app":** the Terminal window running it was closed or stopped. Start it again; nothing is lost.
- **Questions missing:** check the yellow problem box on the home screen, or run `python3 study.py validate`.
- **Run the tests:** `cd app && python3 -m unittest`.

## 13. Rebuilding this PDF

This guide is generated from `app/docs/HOW_TO_USE.md`. After editing it, from the Study Guide folder:

```
python3 -m venv app/.venv-dev
app/.venv-dev/bin/pip install -r app/requirements-dev.txt
app/.venv-dev/bin/python app/tools/build_pdf.py
```

(The first two lines are one-time setup.)
