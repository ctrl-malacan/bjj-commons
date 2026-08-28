#!/usr/bin/env python3
"""Verify every relative markdown link and heading anchor in the project."""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

def slug(h):
    h = h.strip().lower()
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")

def main():
    files = [f for f in ROOT.rglob("*.md")]
    anchors = {f.resolve(): {slug(m.group(1)) for m in re.finditer(r"^#{1,6}\s+(.+?)\s*$", f.read_text(), re.M)} for f in files}
    bad = 0
    for f in files:
        for m in re.finditer(r"\]\(([^)\s]+)\)", f.read_text()):
            link = m.group(1)
            if link.startswith(("http://", "https://", "mailto:")):
                continue
            path, _, frag = link.partition("#")
            tgt = (f.parent / path).resolve() if path else f.resolve()
            rel = f.relative_to(ROOT)
            if not tgt.exists():
                print(f"MISSING FILE  {rel}: {link}"); bad += 1; continue
            if frag and frag not in anchors.get(tgt, set()):
                print(f"BAD ANCHOR    {rel}: {link}"); bad += 1
    print(f"{len(files)} files checked; {bad} problem(s)")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
