#!/usr/bin/env python3
"""Start the study app, or validate question files.

    python3 study.py                         start the app and open the browser
    python3 study.py validate FILE [FILE...] check question files before dropping them in
    python3 study.py validate                check everything in questions/
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP = ROOT / "app"  # code, tests, docs, config and progress live here
sys.path.insert(0, str(APP))

from studyapp.parser import validate_paths  # noqa: E402
from studyapp.scheduler import load_config  # noqa: E402


def cmd_validate(paths: list[str]) -> int:
    if not paths:
        paths = sorted(str(p) for p in (ROOT / "questions").glob("*.md") if not p.name.startswith("_"))
    missing = [p for p in paths if not Path(p).is_file()]
    for p in missing:
        print(f"{p}: ERROR file not found")
    decks, issues = validate_paths([p for p in paths if p not in missing])
    for i in sorted(issues, key=lambda i: (i.file, i.line)):
        print(i)
    errors = sum(1 for i in issues if i.level == "error") + len(missing)
    warns = sum(1 for i in issues if i.level == "warn")
    total = sum(len(d.questions) for d in decks)
    print(f"\n{total} valid question(s) in {len(decks)} file(s): {errors} error(s), {warns} warning(s).")
    if errors:
        print("Questions with errors are skipped by the app until fixed.")
    return 1 if errors else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Local offline study app.")
    ap.add_argument("--port", type=int, help="port to listen on (default from config.toml, 8765)")
    ap.add_argument("--no-browser", action="store_true", help="don't open the browser automatically")
    sub = ap.add_subparsers(dest="cmd")
    v = sub.add_parser("validate", help="check question files and report problems")
    v.add_argument("files", nargs="*", help="files to check (default: everything in questions/)")
    args = ap.parse_args(argv)

    if args.cmd == "validate":
        return cmd_validate(args.files)

    from studyapp.server import serve
    cfg = load_config(APP / "config.toml")
    serve(ROOT, cfg, data_dir=APP / "data", open_browser=cfg.open_browser and not args.no_browser,
          port=args.port)
    return 0


if __name__ == "__main__":
    sys.exit(main())
