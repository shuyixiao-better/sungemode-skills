#!/usr/bin/env python3
"""Dependency-free validation of this repository's deliberately simple frontmatter."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    errors = []
    entries = sorted((root / "skills").glob("*/SKILL.md"))
    if not entries:
        errors.append("No skills found")
    for entry in entries:
        for path in (entry, entry.with_name("SKILL.en.md")):
            if not path.exists():
                errors.append(f"Missing English entry: {path}")
                continue
            text = path.read_text(encoding="utf-8")
            match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
            if not match:
                errors.append(f"Invalid frontmatter: {path}")
                continue
            fields = {}
            try:
                for line in match[1].splitlines():
                    key, value = line.split(":", 1)
                    fields[key] = json.loads(value.strip())
            except (ValueError, json.JSONDecodeError):
                errors.append(f"Frontmatter must use single-line JSON-quoted YAML strings: {path}")
                continue
            name = fields.get("name", "")
            desc = fields.get("description", "")
            if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64 or name != entry.parent.name:
                errors.append(f"Invalid name: {path}")
            if not isinstance(desc, str) or not 1 <= len(desc) <= 1024:
                errors.append(f"Invalid description: {path}")
            if fields.get("license") != "MIT":
                errors.append(f"Missing MIT license: {path}")
            for ui in ("openai.yaml", "openai.en.yaml"):
                metadata = entry.parent / "agents" / ui
                if not metadata.exists() or f"${name}" not in metadata.read_text(encoding="utf-8"):
                    errors.append(f"Missing invocation metadata: {metadata}")
    for path in sorted(root.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        for href in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", path.read_text(encoding="utf-8")):
            link = urlsplit(href)
            if link.scheme or not link.path:
                continue
            target = (path.parent / unquote(link.path)).resolve()
            if not target.exists():
                errors.append(f"Broken local link in {path}: {href}")
    for error in errors:
        print(error, file=sys.stderr)
    if not errors:
        print(f"Validated {len(entries)} skills in both languages; local Markdown links resolve.")
    return not errors


if __name__ == "__main__":
    sys.exit(0 if validate() else 1)

