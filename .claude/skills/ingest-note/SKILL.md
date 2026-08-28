---
name: ingest-note
description: Fold a raw jiu-jitsu class note (transcript file, or a voice-notes CSV export) into the Opensource BJJ reference — position pages, chains, submissions index, position map. Use when someone drops a note in inbox/ or asks to ingest, fold in, or add a class note.
---

Follow `ingest/PROCESS.md` exactly. In short:

1. Branch from an up-to-date `main`: `ingest/<YYYY-MM-DD>-<short-slug>`.
2. Run `python3 ingest/triage.py <source> --out <any path outside the repo, e.g. /tmp/triage.md>`. The source is `$ARGUMENTS` if given; otherwise look in `inbox/` and ask if it is empty.
3. Read the whole triage file first. Then, for each note in date order, follow PROCESS.md section 2: classify (page, chain, correction?, and `gi` / `nogi` / `both`) → diff against the page → edit in the page's voice; gi-specific additions get a **Gi.** label → propagate to chains / `submissions.md` / `position-map.md` → log. Before editing, show the user a short mapping (note → page/section → kind of change).
4. Append one row per note to `ingest/log.tsv` (columns: note_id, note_date, ingested, gi, pages, summary), including skipped notes. No note text in the log.
5. Run `python3 ingest/checklinks.py`; fix anything it reports.
6. Commit with a conventional message and open a PR whose body lists what changed, page by page. Remind a first-time contributor to add themselves to `CONTRIBUTORS.md`.

Hard rules: never commit raw note text or the scratch file; never write first person or "in class today" into the pages; when a note disagrees with what is on the page and both are plausible, keep both with a `Source:` note rather than overwriting.
