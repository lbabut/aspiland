#!/usr/bin/env python3

from __future__ import annotations

import argparse
import collections
import json
import re
import subprocess
from pathlib import Path

TARGET_ROOTS = {
    "admini",
    "archive",
    "embassies",
    "sharedassets",
    "users",
}

BINARY_OR_ARCHIVE_SUFFIXES = {
    ".7z", ".bak", ".bin", ".db", ".dll", ".dmp", ".exe", ".gz",
    ".jar", ".mdb", ".pdb", ".rar", ".sqlite", ".tar", ".tgz", ".zip",
}

BUILD_PARTS = {"bin", "build", "dist", "obj", "out", "release"}

RULES: dict[str, re.Pattern[str]] = {
    "email_address": re.compile(r"(?i)(?<![\w.+-])[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}(?![\w.-])"),
    "international_phone": re.compile(r"(?<!\w)\+\d(?:[\s().-]*\d){7,14}(?!\d)"),
    "possible_personal_identifier": re.compile(r"(?<!\d)\d{11}(?!\d)"),
    "privacy_or_health_marker": re.compile(
        r"(?i)\b(address|adres|adresse|birthday|birth date|date of birth|diagnos\w*|"
        r"disease|email|e-mail|f[øo]dselsnummer|health|hospital|medical|medycz\w*|"
        r"pesel|phone|personnummer|telefon|ulica)\b"
    ),
}


def tracked_files() -> list[Path]:
    completed = subprocess.run(
        ["git", "ls-files", "-z"],
        check=True,
        stdout=subprocess.PIPE,
    )
    return [Path(item.decode("utf-8", errors="surrogateescape")) for item in completed.stdout.split(b"\0") if item]


def is_target(path: Path) -> bool:
    parts = [part.lower() for part in path.parts]
    if not parts:
        return False
    if parts[0] in TARGET_ROOTS:
        return True
    if path.name.lower() == "publicchat.txt":
        return True
    if any(part in BUILD_PARTS for part in parts):
        return True
    if path.suffix.lower() in BINARY_OR_ARCHIVE_SUFFIXES:
        return True
    return False


def group_for(path: Path) -> str:
    if not path.parts:
        return "root"
    first = path.parts[0]
    if first.lower() in TARGET_ROOTS:
        return first
    if path.name.lower() == "publicchat.txt":
        return "PublicChat.txt"
    if path.suffix.lower() in BINARY_OR_ARCHIVE_SUFFIXES:
        return "binary-or-archive"
    return "build-output"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", required=True)
    parser.add_argument("--details", required=True)
    parser.add_argument("--max-text-bytes", type=int, default=5_000_000)
    args = parser.parse_args()

    details: list[dict[str, object]] = []
    files_considered = 0
    text_files_scanned = 0
    unreadable_files = 0

    for path in tracked_files():
        if not is_target(path):
            continue
        files_considered += 1
        group = group_for(path)

        if path.suffix.lower() in BINARY_OR_ARCHIVE_SUFFIXES or any(
            part.lower() in BUILD_PARTS for part in path.parts
        ):
            details.append({"path": str(path), "line": None, "rule": "binary_or_generated_artifact", "group": group})
            continue

        try:
            raw = path.read_bytes()
        except OSError:
            unreadable_files += 1
            details.append({"path": str(path), "line": None, "rule": "unreadable_file", "group": group})
            continue

        if len(raw) > args.max_text_bytes or b"\0" in raw[:8192]:
            details.append({"path": str(path), "line": None, "rule": "binary_or_large_file", "group": group})
            continue

        text_files_scanned += 1
        text = raw.decode("utf-8", errors="replace")
        seen: set[tuple[str, int]] = set()
        for line_number, line in enumerate(text.splitlines(), start=1):
            for rule_id, pattern in RULES.items():
                if pattern.search(line) and (rule_id, line_number) not in seen:
                    seen.add((rule_id, line_number))
                    details.append({"path": str(path), "line": line_number, "rule": rule_id, "group": group})

    rule_counts = collections.Counter(str(item["rule"]) for item in details)
    group_counts = collections.Counter(str(item["group"]) for item in details)

    summary = {
        "status": "review-required" if details else "passed",
        "files_considered": files_considered,
        "text_files_scanned": text_files_scanned,
        "unreadable_files": unreadable_files,
        "suspected_locations": len(details),
        "rule_counts": dict(sorted(rule_counts.items())),
        "group_counts": dict(sorted(group_counts.items())),
        "content_included": False,
        "paths_included": False,
    }

    summary_path = Path(args.summary)
    details_path = Path(args.details)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    details_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    details_path.write_text(json.dumps(details, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(
        "Legacy privacy scan completed: "
        f"files={files_considered}, locations={len(details)}; content and paths suppressed from logs."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
