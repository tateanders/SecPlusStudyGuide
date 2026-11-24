# Study App

A local, offline, test-first study app. It throws questions at you, shows you exactly why you were wrong, brings missed concepts back later as *different* questions, and tracks the difference between "knew it" and "got lucky". All content comes from markdown files in `questions/`; nothing about any particular exam is built in.

- **How to use it:** [HOW_TO_USE.pdf](../HOW_TO_USE.pdf) (source: `app/docs/HOW_TO_USE.md`)
- **How to write question files:** [FORMAT.md](../FORMAT.md)

## Setup

Requires Python 3.11 or newer (for `tomllib`). macOS and Linux. No packages to install, and no internet needed.

```
python3 --version        # 3.11+
```

## Run

```
cd ~/Desktop/"Study Guide"
python3 study.py
```

The browser opens on the home screen. Options: `--port 9000`, `--no-browser`.

**One-command start from anywhere:** add an alias to `~/.zshrc` (macOS) or `~/.bashrc` (Linux):

```
alias study='python3 "$HOME/Desktop/Study Guide/study.py"'
```

Open a new Terminal window and type `study`.

## Validate question files

```
python3 study.py validate questions/my-new-file.md   # one or more files
python3 study.py validate                            # everything in questions/
```

Prints `file:line: ERROR|WARN message` and exits non-zero if there are errors. The app runs the same checks on load and skips broken questions instead of crashing.

## Tests

```
cd app && python3 -m unittest
```

Covers the parser (including every example in FORMAT.md and the sample deck), typed-answer matching, grading, the scheduler, the session picker, and an end-to-end flow through the app (persistence, restart, answer-key changes).

## Rebuild the PDF guide

```
python3 -m venv app/.venv-dev && app/.venv-dev/bin/pip install -r app/requirements-dev.txt   # once
app/.venv-dev/bin/python app/tools/build_pdf.py
```

## Project layout

```
study.py                 entry point: serve (default) or `validate`
questions/               your decks (*.md); _aliases.md = typed-answer equivalences
FORMAT.md                question file spec
HOW_TO_USE.pdf           user guide
app/
 config.toml             scheduling and server settings
 data/progress.db        all progress (SQLite), created on first run; back up by copying
 studyapp/
   parser.py              question files -> Decks, with file:line errors and lint warnings
   grading.py             per-type grading and typed-answer normalization
   scheduler.py           concept-level Leitner boxes + anti-luck gate
   session.py             in-session picker: requeues, due reviews, new-concept cap, variety rules
   store.py               SQLite persistence (every answer committed immediately)
   server.py              local HTTP server + JSON API (stdlib only)
   mdrender.py            small safe markdown renderer for question text
   static/                the browser UI (vanilla JS/CSS, no CDN)
 tests/                  unittest suite (fixtures/sample-all-types.md covers every type)
 docs/HOW_TO_USE.md      source of HOW_TO_USE.pdf
 tools/build_pdf.py      builds the PDF
```

## Design notes

- **Performance weighting:** each concept also keeps `weak` (a recency-weighted miss rate, 0.6 decay) and `streak` (confident corrects in a row). Weak concepts get shorter intervals, come first among due reviews, and dominate the "nothing due" fallback, which picks at weighted random and skips strong concepts and anything already answered right this session. A correct answer right after an in-session miss earns one more check later in the session. Old databases are migrated and backfilled from the `answers` history.
- **Scheduling:** concept-level Leitner boxes (0, 1, 3, 7, 14, 30, 60 days). Leitner was chosen over SM-2 and FSRS because it stays transparent ("box 3 = back in a week"), doesn't fall into SM-2's "ease hell" when you learn by failing, and doesn't need the hundreds of reviews FSRS needs to fit its parameters. A concept can't become *solid* (box 3+) until two different variants have been answered correctly and confidently on two different days (in cram mode, `cram = true` in config.toml, the day rule is off and a concept keeps coming back in the same session until it's solid).
- **Storage:** SQLite rather than JSON. Each answer is one atomic transaction, so a crash or quit can't corrupt or lose progress, and the progress-over-time views are simple queries.
- **Identity:** progress is keyed by the question ID in the file, so rewording, reordering and moving questions is safe. Answer-key changes are detected by hash and make that concept due again.
- **Future exam mode:** `Session` takes a picker object (`LearningPicker` today), so a timed exam mode can be added as a new picker plus a results screen.
