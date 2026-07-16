#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
INDEX = SITE / "index.html"
APP = SITE / "app.js"

VOID_TAGS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, int]] = []
        self.errors: list[str] = []
        self.ids: set[str] = set()
        self.fragment_links: list[tuple[str, int]] = []
        self.local_assets: list[tuple[str, int]] = []
        self.i18n_keys: list[tuple[str, int]] = []
        self.heading_counts: Counter[str] = Counter()
        self.main_count = 0
        self.body_count = 0
        self.html_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        line, _ = self.getpos()
        attrs_dict = dict(attrs)

        if tag not in VOID_TAGS:
            self.stack.append((tag, line))

        element_id = attrs_dict.get("id")
        if element_id:
            if element_id in self.ids:
                self.errors.append(f"site/index.html:{line}: duplicate id: {element_id}")
            self.ids.add(element_id)

        href = attrs_dict.get("href")
        if href:
            if href.startswith("#") and len(href) > 1:
                self.fragment_links.append((href[1:], line))
            elif tag == "link":
                self._record_local_asset(href, line)

        src = attrs_dict.get("src")
        if src and tag == "script":
            self._record_local_asset(src, line)

        i18n_key = attrs_dict.get("data-i18n")
        if i18n_key:
            self.i18n_keys.append((i18n_key, line))

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.heading_counts[tag] += 1
        elif tag == "main":
            self.main_count += 1
        elif tag == "body":
            self.body_count += 1
        elif tag == "html":
            self.html_count += 1

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in VOID_TAGS and self.stack and self.stack[-1][0] == tag:
            self.stack.pop()

    def handle_endtag(self, tag: str) -> None:
        line, _ = self.getpos()
        if tag in VOID_TAGS:
            return
        if not self.stack:
            self.errors.append(f"site/index.html:{line}: unexpected closing tag </{tag}>")
            return
        open_tag, open_line = self.stack.pop()
        if open_tag != tag:
            self.errors.append(
                f"site/index.html:{line}: closing </{tag}> does not match <{open_tag}> from line {open_line}"
            )

    def _record_local_asset(self, value: str, line: int) -> None:
        parsed = urlparse(value)
        if not parsed.scheme and not parsed.netloc and not value.startswith(("#", "data:")):
            self.local_assets.append((parsed.path, line))


TRANSLATION_KEY = re.compile(r'^\s+"([^"]+)"\s*:', re.MULTILINE)


def check_site() -> list[str]:
    errors: list[str] = []
    for required in (INDEX, APP, SITE / "styles.css", SITE / "sections.css"):
        if not required.is_file():
            errors.append(f"missing required site file: {required.relative_to(ROOT)}")

    if errors:
        return errors

    html = INDEX.read_text(encoding="utf-8")
    parser = SiteParser()
    parser.feed(html)
    parser.close()
    errors.extend(parser.errors)

    for tag, line in reversed(parser.stack):
        errors.append(f"site/index.html:{line}: unclosed <{tag}> tag")

    if not html.rstrip().endswith("</html>"):
        errors.append("site/index.html: document must end with </html>")
    if parser.html_count != 1:
        errors.append(f"site/index.html: expected one html element, found {parser.html_count}")
    if parser.body_count != 1:
        errors.append(f"site/index.html: expected one body element, found {parser.body_count}")
    if parser.main_count != 1:
        errors.append(f"site/index.html: expected one main element, found {parser.main_count}")
    if parser.heading_counts["h1"] != 1:
        errors.append(f"site/index.html: expected one h1, found {parser.heading_counts['h1']}")

    for target, line in parser.fragment_links:
        if target not in parser.ids:
            errors.append(f"site/index.html:{line}: fragment target does not exist: #{target}")

    for asset, line in parser.local_assets:
        candidate = (SITE / asset).resolve()
        try:
            candidate.relative_to(SITE.resolve())
        except ValueError:
            errors.append(f"site/index.html:{line}: local asset escapes site directory: {asset}")
            continue
        if not candidate.is_file():
            errors.append(f"site/index.html:{line}: missing local asset: {asset}")

    translations = Counter(TRANSLATION_KEY.findall(APP.read_text(encoding="utf-8")))
    for key, line in parser.i18n_keys:
        count = translations[key]
        if count != 2:
            errors.append(
                f"site/index.html:{line}: data-i18n key {key!r} must occur once in each locale; found {count}"
            )

    duplicated_translation_keys = sorted(key for key, count in translations.items() if count != 2)
    for key in duplicated_translation_keys:
        if not any(item_key == key for item_key, _ in parser.i18n_keys):
            errors.append(f"site/app.js: translation key {key!r} occurs {translations[key]} times; expected 2")

    return errors


def main() -> int:
    errors = check_site()
    if errors:
        print("Static site integrity checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Static site integrity checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
