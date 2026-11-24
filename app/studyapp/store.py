"""SQLite persistence. Every answer is committed immediately, so quitting loses nothing."""
from __future__ import annotations

import json
import sqlite3
import threading
from pathlib import Path

from .scheduler import CORRECT, ConceptState, update_weak

SCHEMA = """
CREATE TABLE IF NOT EXISTS answers (
    id          INTEGER PRIMARY KEY,
    ts          REAL NOT NULL,
    session_id  TEXT NOT NULL,
    question_id TEXT NOT NULL,
    concept_id  TEXT NOT NULL,
    deck_id     TEXT NOT NULL,
    topic       TEXT NOT NULL,
    qtype       TEXT NOT NULL,
    verdict     TEXT NOT NULL,           -- correct | shaky | missed
    low_conf    INTEGER NOT NULL,
    dont_know   INTEGER NOT NULL,
    response    TEXT,                    -- JSON
    ms_taken    INTEGER
);
CREATE INDEX IF NOT EXISTS answers_ts ON answers(ts);
CREATE INDEX IF NOT EXISTS answers_q ON answers(question_id);

CREATE TABLE IF NOT EXISTS concepts (
    concept_id TEXT PRIMARY KEY,
    box        INTEGER NOT NULL,
    due_at     REAL NOT NULL,
    misses     INTEGER NOT NULL,
    reviews    INTEGER NOT NULL,
    last_seen  REAL NOT NULL,
    last_qid   TEXT NOT NULL,
    last_type  TEXT NOT NULL,
    evidence   TEXT NOT NULL,          -- JSON list of [question id, date]
    weak       REAL NOT NULL DEFAULT 0, -- recency-weighted miss rate
    streak     INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS questions_seen (
    question_id     TEXT PRIMARY KEY,
    answer_key_hash TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS daily_snapshot (
    day      TEXT NOT NULL,
    deck_id  TEXT NOT NULL,
    unseen   INTEGER NOT NULL,
    learning INTEGER NOT NULL,
    solid    INTEGER NOT NULL,
    PRIMARY KEY (day, deck_id)
);

CREATE TABLE IF NOT EXISTS settings (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
"""


class Store:
    def __init__(self, path: str | Path):
        self.path = str(path)
        if self.path != ":memory:":
            Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self.db = sqlite3.connect(self.path, check_same_thread=False)
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.executescript(SCHEMA)
        self._migrate()
        self.db.commit()

    def _migrate(self) -> None:
        """Databases from before weak/streak existed: add the columns and fill them from past answers."""
        cols = {r[1] for r in self.db.execute("PRAGMA table_info(concepts)")}
        if {"weak", "streak"} <= cols:
            return
        self.db.execute("ALTER TABLE concepts ADD COLUMN weak REAL NOT NULL DEFAULT 0")
        self.db.execute("ALTER TABLE concepts ADD COLUMN streak INTEGER NOT NULL DEFAULT 0")
        replay: dict[str, tuple[float, int]] = {}
        for cid, verdict in self.db.execute("SELECT concept_id, verdict FROM answers ORDER BY ts, id"):
            weak, streak = replay.get(cid, (0.0, 0))
            replay[cid] = (update_weak(weak, verdict), streak + 1 if verdict == CORRECT else 0)
        self.db.executemany("UPDATE concepts SET weak=?, streak=? WHERE concept_id=?",
                            [(w, s, cid) for cid, (w, s) in replay.items()])

    # --- concept state ---------------------------------------------------
    def load_states(self) -> dict[str, ConceptState]:
        rows = self.db.execute("SELECT concept_id, box, due_at, misses, reviews, last_seen, "
                               "last_qid, last_type, evidence, weak, streak FROM concepts").fetchall()
        return {r[0]: ConceptState(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], json.loads(r[8]), r[9], r[10])
                for r in rows}

    def _save_state(self, s: ConceptState) -> None:
        self.db.execute(
            "INSERT OR REPLACE INTO concepts (concept_id, box, due_at, misses, reviews, last_seen, last_qid,"
            " last_type, evidence, weak, streak) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (s.concept_id, s.box, s.due_at, s.misses, s.reviews, s.last_seen,
             s.last_qid, s.last_type, json.dumps(s.evidence), s.weak, s.streak))

    def save_state(self, s: ConceptState) -> None:
        with self._lock:
            self._save_state(s)
            self.db.commit()

    # --- answers ---------------------------------------------------------
    def record_answer(self, *, ts: float, session_id: str, question, verdict: str, low_conf: bool,
                      dont_know: bool, response, ms_taken: int | None, state: ConceptState) -> None:
        """Log the answer and save the concept's new state in one transaction."""
        with self._lock:
            self.db.execute(
                "INSERT INTO answers (ts, session_id, question_id, concept_id, deck_id, topic, qtype, verdict,"
                " low_conf, dont_know, response, ms_taken) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                (ts, session_id, question.id, question.concept_id, question.deck_id, question.topic,
                 question.type, verdict, int(low_conf), int(dont_know), json.dumps(response), ms_taken))
            self._save_state(state)
            self.db.execute("INSERT OR REPLACE INTO questions_seen VALUES (?,?)",
                            (question.id, question.answer_key_hash()))
            self.db.commit()

    def seen_counts(self) -> dict[str, int]:
        return dict(self.db.execute("SELECT question_id, COUNT(*) FROM answers GROUP BY question_id"))

    def answers_since(self, ts: float) -> list[dict]:
        cur = self.db.execute("SELECT ts, question_id, concept_id, deck_id, topic, verdict FROM answers "
                              "WHERE ts >= ? ORDER BY ts", (ts,))
        cols = [c[0] for c in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]

    # --- answer-key change detection --------------------------------------
    def changed_answer_keys(self, questions) -> list:
        """Questions answered before whose answer key has since changed in the file."""
        known = dict(self.db.execute("SELECT question_id, answer_key_hash FROM questions_seen"))
        return [q for q in questions if q.id in known and known[q.id] != q.answer_key_hash()]

    def accept_answer_key(self, question) -> None:
        with self._lock:
            self.db.execute("INSERT OR REPLACE INTO questions_seen VALUES (?,?)",
                            (question.id, question.answer_key_hash()))
            self.db.commit()

    # --- snapshots & settings ---------------------------------------------
    def snapshot(self, day: str, deck_id: str, unseen: int, learning: int, solid: int) -> None:
        with self._lock:
            self.db.execute("INSERT OR REPLACE INTO daily_snapshot VALUES (?,?,?,?,?)",
                            (day, deck_id, unseen, learning, solid))
            self.db.commit()

    def snapshots(self) -> list[tuple]:
        return self.db.execute("SELECT day, deck_id, unseen, learning, solid FROM daily_snapshot "
                               "ORDER BY day").fetchall()

    def get_setting(self, key: str, default=None):
        row = self.db.execute("SELECT value FROM settings WHERE key=?", (key,)).fetchone()
        return json.loads(row[0]) if row else default

    def set_setting(self, key: str, value) -> None:
        with self._lock:
            self.db.execute("INSERT OR REPLACE INTO settings VALUES (?,?)", (key, json.dumps(value)))
            self.db.commit()

    # --- reset ---------------------------------------------------------------
    def reset_progress(self) -> None:
        """Erase every answer and concept state. Settings (deck selection, cram) are kept."""
        with self._lock:
            for table in ("answers", "concepts", "questions_seen", "daily_snapshot"):
                self.db.execute(f"DELETE FROM {table}")
            self.db.commit()
