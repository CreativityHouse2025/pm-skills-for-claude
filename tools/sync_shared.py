#!/usr/bin/env python3
"""Copy the shared reference files from project-companion to the skills that reuse them.

project-companion is the source of truth for the catalog, agile list,
review checklists and Arabic terms. Run this after editing any of them.

Usage: python3 tools/sync_shared.py
"""
import pathlib
import shutil

root = pathlib.Path(__file__).resolve().parent.parent / "skills"
source = root / "project-companion" / "references"
shared = ["catalog.md", "agile.md", "review-checklists.md", "arabic-terms.md"]
targets = ["trainer-toolkit", "pmo-kit"]

for t in targets:
    for name in shared:
        shutil.copyfile(source / name, root / t / "references" / name)
        print(f"{t}/references/{name} updated")
