#!/usr/bin/env python3
"""Triage new notes against the ingest log.

Usage:
  triage.py EXPORT.csv [--out scratch.md]      # voice-notes app export
  triage.py NOTE.md|NOTE.txt [--out scratch.md] # one plain transcript
  triage.py DIRECTORY [--out scratch.md]        # every .md/.txt/.csv inside

Writes every note not yet in log.tsv (oldest first) to a markdown scratch
file for an agent to fold into the position pages, following PROCESS.md.

CSV columns expected: id, parent_id, description, enhanced, date, tags.
Plain files: the whole file is one note; the id is the filename stem; the
date is a leading YYYY-MM-DD in the filename, else today.
"""
import csv, sys, pathlib, argparse, datetime, re

HERE = pathlib.Path(__file__).parent
LOG = HERE / "log.tsv"

def load_log():
    if not LOG.exists():
        return {}
    with LOG.open() as f:
        return {r["note_id"]: r for r in csv.DictReader(f, delimiter="\t")}

def read_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))

def read_plain(path):
    p = pathlib.Path(path)
    m = re.match(r"(\d{4}-\d{2}-\d{2})", p.stem)
    date = m.group(1) if m else datetime.date.today().isoformat()
    text = p.read_text().strip()
    return [{"id": p.stem, "parent_id": "", "description": text, "enhanced": "", "date": date, "tags": ""}]

def read_any(path):
    p = pathlib.Path(path)
    if p.is_dir():
        notes = []
        for f in sorted(p.iterdir()):
            if f.suffix.lower() in (".csv", ".md", ".txt"):
                notes += read_any(f)
        return notes
    if p.suffix.lower() == ".csv":
        return read_csv(p)
    return read_plain(p)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--out", default=None)
    ap.add_argument("--all", action="store_true", help="include already-ingested notes")
    a = ap.parse_args()

    notes = read_any(a.source)
    by_id = {n["id"]: n for n in notes}
    log = load_log()
    new = [n for n in notes if a.all or n["id"] not in log]
    new.sort(key=lambda n: (n["date"], n["id"]))

    out = [f"# Triage: {len(new)} new of {len(notes)} notes ({len(log)} already in the log)\n"]
    for n in new:
        parent = by_id.get(n.get("parent_id", "")) if n.get("parent_id") else None
        text = (n.get("enhanced") or "").strip() or n["description"].strip()
        src = "enhanced" if (n.get("enhanced") or "").strip() else "RAW transcript — clean up first"
        out.append(f"\n---\n\n## {n['date']} · `{n['id'][:12]}`")
        if parent:
            pstat = "in the log" if parent["id"] in log else "NOT in the log"
            out.append(f"**Follow-up to** `{parent['id'][:12]}` ({parent['date']}, {pstat}) — treat as a correction/addition to that note's content.")
        out.append(f"**Tags:** {n.get('tags') or '(none)'}  \n**Text source:** {src}\n")
        out.append(text)
    body = "\n".join(out) + "\n"
    if a.out:
        pathlib.Path(a.out).write_text(body)
        print(f"{len(new)} new notes -> {a.out}")
    else:
        sys.stdout.write(body)

if __name__ == "__main__":
    main()
