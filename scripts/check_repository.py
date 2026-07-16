#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MAINTAINED_ROOTS = (
    "canon/",
    "docs/",
    "projects/",
    "protocols/",
    "public/",
    "rfc/",
)
MAINTAINED_ROOT_FILES = {
    "README.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
}
IGNORED_LINK_SCHEMES = {
    "data",
    "ftp",
    "http",
    "https",
    "irc",
    "mailto",
    "tel",
}
FORBIDDEN_GENERATED_PARTS = {
    ".idea",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".venv",
    ".vs",
    ".vscode",
    "__pycache__",
    "build",
    "dist",
    "htmlcov",
    "muminki_dreams",
    "muminki_memory",
    "venv",
}
FORBIDDEN_GENERATED_SUFFIXES = {
    ".bak",
    ".log",
    ".pyc",
    ".pyo",
    ".suo",
    ".tmp",
    ".user",
}
FORBIDDEN_GENERATED_NAMES = {
    ".coverage",
    ".env",
    "Thumbs.db",
    "world_state.pkl",
}
MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+\S")


def run_git(*args: str) -> list[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=REPOSITORY_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line for line in result.stdout.splitlines() if line]


def is_valid_base(base: str | None) -> bool:
    if not base or set(base) == {"0"}:
        return False
    try:
        subprocess.run(
            ["git", "cat-file", "-e", f"{base}^{{commit}}"],
            cwd=REPOSITORY_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def changed_paths(base: str | None) -> list[Path]:
    if is_valid_base(base):
        names = run_git("diff", "--name-only", "--diff-filter=ACMR", f"{base}...HEAD")
    else:
        names = run_git("ls-files")
    return [Path(name) for name in names]


def added_paths(base: str | None) -> list[Path]:
    if not is_valid_base(base):
        return []
    names = run_git("diff", "--name-only", "--diff-filter=A", f"{base}...HEAD")
    return [Path(name) for name in names]


def is_maintained_markdown(path: Path) -> bool:
    normalized = path.as_posix()
    return path.suffix.lower() == ".md" and (
        normalized in MAINTAINED_ROOT_FILES
        or normalized.startswith(MAINTAINED_ROOTS)
    )


def parse_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    return target.split(maxsplit=1)[0]


def check_markdown_file(path: Path) -> list[str]:
    errors: list[str] = []
    absolute_path = REPOSITORY_ROOT / path
    if not absolute_path.is_file():
        return errors

    text = absolute_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    heading_levels: list[tuple[int, int]] = []

    in_fence = False
    fence_marker = ""
    for line_number, line in enumerate(lines, start=1):
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue
        if in_fence:
            continue

        heading_match = HEADING_PATTERN.match(line)
        if heading_match:
            heading_levels.append((line_number, len(heading_match.group(1))))

        for link_match in MARKDOWN_LINK_PATTERN.finditer(line):
            target = parse_link_target(link_match.group(1))
            if not target or target.startswith("#"):
                continue

            parsed = urlparse(target)
            if parsed.scheme.lower() in IGNORED_LINK_SCHEMES or parsed.netloc:
                continue

            decoded_path = unquote(parsed.path)
            if not decoded_path:
                continue

            if decoded_path.startswith("/"):
                candidate = REPOSITORY_ROOT / decoded_path.lstrip("/")
            else:
                candidate = absolute_path.parent / decoded_path

            candidate = candidate.resolve()
            try:
                candidate.relative_to(REPOSITORY_ROOT)
            except ValueError:
                errors.append(f"{path}:{line_number}: relative link escapes the repository: {target}")
                continue

            if not candidate.exists():
                errors.append(f"{path}:{line_number}: broken relative link: {target}")

    if not heading_levels:
        errors.append(f"{path}: missing Markdown heading")
        return errors

    first_line, first_level = heading_levels[0]
    if first_level != 1:
        errors.append(f"{path}:{first_line}: first heading must be level 1")

    h1_count = sum(1 for _, level in heading_levels if level == 1)
    if h1_count != 1:
        errors.append(f"{path}: expected exactly one level-1 heading, found {h1_count}")

    previous_level = heading_levels[0][1]
    for line_number, level in heading_levels[1:]:
        if level > previous_level + 1:
            errors.append(
                f"{path}:{line_number}: heading jumps from level {previous_level} to level {level}"
            )
        previous_level = level

    return errors


def check_added_generated_files(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in paths:
        parts = set(path.parts)
        name = path.name
        suffix = path.suffix.lower()

        forbidden = (
            bool(parts & FORBIDDEN_GENERATED_PARTS)
            or name in FORBIDDEN_GENERATED_NAMES
            or suffix in FORBIDDEN_GENERATED_SUFFIXES
            or name.startswith(".env.") and name != ".env.example"
            or name == ".DS_Store"
        )
        if forbidden:
            errors.append(f"new generated, local or secret-like file is not allowed: {path}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default=None)
    args = parser.parse_args()

    changed = changed_paths(args.base)
    markdown_files = sorted(path for path in changed if is_maintained_markdown(path))

    errors: list[str] = []
    for markdown_file in markdown_files:
        errors.extend(check_markdown_file(markdown_file))
    errors.extend(check_added_generated_files(added_paths(args.base)))

    if errors:
        print("Repository quality checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Repository quality checks passed for {len(markdown_files)} maintained Markdown file(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
