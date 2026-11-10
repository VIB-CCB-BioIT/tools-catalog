#!/usr/bin/env python3
"""Validate tools.yaml and regenerate README.md (catalog tables) and catalog.csv.

Usage:
    python scripts/build_catalog.py          # rebuild files
    python scripts/build_catalog.py --check  # exit 1 if generated files are out of date

Requires: PyYAML
"""
import csv
import io
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools.yaml"
README = ROOT / "README.md"
CSV_OUT = ROOT / "catalog.csv"

START, END = "<!-- CATALOG:START -->", "<!-- CATALOG:END -->"

# Order in which categories appear. Add new ones here.
CATEGORIES = [
    "Single-cell transcriptomics",
    "Spatial omics",
    "Long-read & DNA sequencing",
    "Bulk RNA-seq & proteomics",
    "Imaging & microscopy",
]
STATUSES = {
    "public": "Public",
    "internal": "Internal – ask contact",
    "building": "In development",
}
REQUIRED = ["id", "name", "category", "summary", "status", "contact"]


def load():
    data = yaml.safe_load(SRC.read_text(encoding="utf-8"))
    return data["tools"]


def validate(tools):
    errors, todo = [], []
    seen = set()
    for t in tools:
        tid = t.get("id", "<no id>")
        for f in REQUIRED:
            if not t.get(f):
                errors.append(f"{tid}: missing '{f}'")
        if tid in seen:
            errors.append(f"{tid}: duplicate id")
        seen.add(tid)
        if t.get("status") not in STATUSES:
            errors.append(f"{tid}: status must be one of {list(STATUSES)}")
        if t.get("category") not in CATEGORIES:
            errors.append(f"{tid}: unknown category '{t.get('category')}'")
        if t.get("status") == "public" and not t.get("repo"):
            todo.append(f"{tid}: public but no repo URL yet")
        if "(name TBD)" in t.get("name", ""):
            todo.append(f"{tid}: needs a proper name")
    return errors, todo


def esc(s):
    return str(s or "").replace("|", "\\|").replace("\n", " ").strip()


def render(tools):
    out = []
    by_cat = defaultdict(list)
    for t in tools:
        by_cat[t["category"]].append(t)
    for cat in CATEGORIES:
        items = sorted(by_cat.get(cat, []), key=lambda t: (t["status"] != "public", t["name"].lower()))
        if not items:
            continue
        out += [f"### {cat}", "", "| Name | What it does | Data / topic | Language | Status | Contact |",
                "|---|---|---|---|---|---|"]
        for t in items:
            name = f"[{esc(t['name'])}]({t['repo']})" if t.get("repo") else esc(t["name"])
            data = esc(t.get("data"))
            if t.get("topic"):
                data += f" · {esc(t['topic'])}"
            contact = f"{esc(t['contact'])} ({esc(t.get('lab'))})" if t.get("lab") else esc(t["contact"])
            out.append(f"| {name} | {esc(t['summary'])} | {data} | {esc(t.get('language'))} | "
                       f"{STATUSES[t['status']]} | {contact} |")
        out.append("")
    return "\n".join(out)


def to_csv(tools):
    cols = ["id", "name", "category", "summary", "data", "step", "topic", "language",
            "status", "repo", "contact", "lab", "share", "notes"]
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    for t in tools:
        w.writerow({c: t.get(c, "") or "" for c in cols})
    return buf.getvalue()


def main():
    check = "--check" in sys.argv
    tools = load()
    errors, todo = validate(tools)
    if errors:
        print("ERRORS:\n  " + "\n  ".join(errors))
        sys.exit(1)

    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        print(f"README.md must contain {START} and {END}")
        sys.exit(1)
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new_readme = f"{head}{START}\n{render(tools)}\n{END}{tail}"
    new_csv = to_csv(tools)

    if check:
        if new_readme != text or not CSV_OUT.exists() or new_csv != CSV_OUT.read_text(encoding="utf-8"):
            print("Generated files are out of date. Run: python scripts/build_catalog.py")
            sys.exit(1)
        print("Up to date.")
        return

    README.write_text(new_readme, encoding="utf-8")
    CSV_OUT.write_text(new_csv, encoding="utf-8")
    print(f"Wrote README.md and catalog.csv ({len(tools)} entries).")
    if todo:
        print(f"\n{len(todo)} cleanup items (not errors):")
        for t in todo:
            print("  -", t)


if __name__ == "__main__":
    main()
