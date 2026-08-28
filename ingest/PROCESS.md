# Ingesting voice notes

How new notes — class notes, seminar notes, your own drilling — get folded into the reference. The goal is that a note ingested in March and one ingested in November are handled the same way.

## Input

Either of:

- a **plain transcript** — one note per `.md`/`.txt` file. Drop it in `inbox/` (gitignored, so it is never committed by accident). Start the filename with the class date if you know it: `2026-08-24-hip-bump.md`.
- a **CSV** in the format `triage.py` expects (`id, parent_id, description, enhanced, date, tags`; `enhanced` = cleaned text if any; `parent_id` = the note this one amends). Adapt other exports to it.

Raw note text does not belong in the repository. `ingest/log.tsv` (note IDs, dates, pages touched, a one-line summary) is the only record that ships.

## 1. Triage

```
python3 ingest/triage.py inbox/2026-08-24-hip-bump.md --out /tmp/triage.md
python3 ingest/triage.py ~/path/to/export.csv --out /tmp/triage.md
```

`--out` is the scratch file (any path outside the repo). For plain files the note id is the filename stem, so renaming a file makes it look new.

Writes every note not yet in `ingest/log.tsv`, oldest first, with its text, tags, and follow-up linkage. Read the whole file before editing anything — later notes often correct earlier ones in the same batch.

## 2. Fold, one note at a time, in date order

For each note:

1. **Clean if raw.** A raw transcript needs the filler stripped and the sides made consistent before it's usable. Do this in the scratch file, not in the repo.
2. **Classify.** Which position page(s)? Which chain(s), if it describes a decision tree? Is it a correction (follow-ups usually are)? Is it `gi`, `nogi`, or `both`? Unmarked page material is no-gi; gi-specific additions get a **Gi.** label (see CONTRIBUTING → Style).
3. **Diff against the page.** Read the relevant section. Decide which it is:
   - *Already covered* — log it, move on.
   - *New detail on an existing technique* — add in place, under the existing heading.
   - *New technique or variation* — add a new `###` under the right `##`, in the page's existing order.
   - *Correction* — fix it. If it's a plain error (wrong name, flipped side), just fix. If it's a legitimate difference between sources, keep both, with a `Source:` note (see CONTRIBUTING → Attribution).
   - *Reflection / question with no technique content* — log as `skipped`, don't add.
4. **Write in the page's voice.** Second person, present tense, the page's declared side convention, no first person, no "in class today." Match the density of the surrounding text — a section should stay readable between rounds.
5. **Propagate.** New decision branch → update the chain diagram and its link list. New submission → add to `submissions.md`. New transition → add a row to `position-map.md`.
6. **Log it.** Append a row to `ingest/log.tsv` with columns `note_id, note_date, ingested (today), gi, pages, summary`. Skipped notes get `-` for pages and a summary starting `skipped:`. Never put note text in the log.

## 3. Verify and ship

- Run the link checker (below) — zero problems.
- One branch and PR per batch. Branch name: `ingest/<YYYY-MM-DD>-<short-slug>`. PR body lists each note's date and what changed, page by page.
- First contribution? Add yourself to `CONTRIBUTORS.md` in the same PR.

## Link checker

```
python3 ingest/checklinks.py
```

Validates every relative link and heading anchor across the project.
