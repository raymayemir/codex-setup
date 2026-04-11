#!/usr/bin/env python3
"""
Load or export language-specific backend best practices.

Examples:
  python scripts/backend_best_practices.py list
  python scripts/backend_best_practices.py show --language golang
  python scripts/backend_best_practices.py export --language python --output /tmp/python-best-practices.md
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

LANGUAGE_ALIASES = {
    "go": "golang",
    "golang": "golang",
    "python": "python",
    "py": "python",
}

LANGUAGE_FILES = {
    "golang": "golang.md",
    "python": "python.md",
}


def references_dir() -> Path:
    return Path(__file__).resolve().parent.parent / "references" / "best-practices"


def normalize_language(value: str) -> str:
    key = value.strip().lower()
    if key not in LANGUAGE_ALIASES:
        supported = ", ".join(sorted({"golang", "python"}))
        raise ValueError(f"Unsupported language '{value}'. Supported: {supported}")
    return LANGUAGE_ALIASES[key]


def reference_path(language: str) -> Path:
    canonical = normalize_language(language)
    return references_dir() / LANGUAGE_FILES[canonical]


def read_reference(language: str) -> str:
    path = reference_path(language)
    if not path.exists():
        raise FileNotFoundError(f"Best-practices file not found: {path}")
    return path.read_text(encoding="utf-8")


def list_languages() -> int:
    base = references_dir()
    print("Supported languages:")
    for language in sorted(LANGUAGE_FILES):
        path = base / LANGUAGE_FILES[language]
        status = "ok" if path.exists() else "missing"
        print(f"- {language}: {path} [{status}]")
    print("Aliases: go->golang, py->python")
    return 0


def show_reference(language: str) -> int:
    content = read_reference(language)
    print(content.rstrip())
    return 0


def export_reference(language: str, output: Path) -> int:
    source = reference_path(language)
    if not source.exists():
        raise FileNotFoundError(f"Best-practices file not found: {source}")

    output = output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, output)
    print(f"Exported {source} -> {output}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Senior backend best-practices helper.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List supported languages and file status.")

    show_cmd = subparsers.add_parser("show", help="Print best-practices for a language.")
    show_cmd.add_argument("--language", required=True, help="golang|go|python|py")

    export_cmd = subparsers.add_parser(
        "export", help="Copy best-practices file for a language to a target path."
    )
    export_cmd.add_argument("--language", required=True, help="golang|go|python|py")
    export_cmd.add_argument("--output", required=True, type=Path, help="Output markdown path")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "list":
            return list_languages()
        if args.command == "show":
            return show_reference(args.language)
        if args.command == "export":
            return export_reference(args.language, args.output)
        parser.error(f"Unknown command: {args.command}")
    except (ValueError, FileNotFoundError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
