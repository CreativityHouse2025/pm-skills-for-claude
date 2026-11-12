#!/usr/bin/env python3
"""Merge a skill folder into one self-contained SKILL.md.

Useful where only a single file can be saved. The split folder stays the
source of truth; rerun this after editing it.

Usage: python3 tools/build_single_file.py skills/project-companion dist/SKILL.md
"""
import pathlib
import sys

skill = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
parts = [(skill / "SKILL.md").read_text(encoding="utf-8").rstrip()]
parts.append(
    "\n\n---\n\n# Bundled files (inlined)\n\n"
    "This is the single-file build. Wherever the instructions above name a "
    "file under `references/` or `assets/`, use the section below with that path."
)
for sub in ("references", "assets"):
    for f in sorted((skill / sub).glob("*.md")):
        body = f.read_text(encoding="utf-8").rstrip()
        # demote headings so each bundled file sits under its own heading
        body = "\n".join("#" + l if l.startswith("#") else l for l in body.splitlines())
        parts.append(f"\n\n## File: `{sub}/{f.name}`\n\n{body}")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("".join(parts) + "\n", encoding="utf-8")
print(out, len(out.read_text(encoding="utf-8").splitlines()), "lines")
