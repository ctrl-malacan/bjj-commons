# Opensource BJJ — context for agents

An open-source reference for Brazilian Jiu-Jitsu (no-gi so far; gi welcome and marked), organized by position and by technique chain. Read `README.md` for what it is and `CONTRIBUTING.md` for how people add to it.

## Layout

- `positions/` — one page per position, numbered sections, prose in second person. The single source of technique detail.
- `chains/` — decision trees as Mermaid flowcharts, edges labeled by the opponent's reaction, plus links into `positions/`. Maps, not manuals: never carry technique detail here.
- `submissions.md` — index of every submission and where it is set up. `position-map.md` — where each position leads.
- `ingest/` — how raw class notes become pages: `PROCESS.md` (the rules), `triage.py`, `checklinks.py`, `log.tsv` (which notes are in; IDs and summaries only).
- `inbox/` — gitignored drop zone for raw transcripts awaiting ingest.
- `.claude/skills/ingest-note/` — the `/ingest-note` skill; it follows `ingest/PROCESS.md`.

## Rules

- Side convention: each page states its default side; techniques are described from one side, mirror implied.
- Gi / no-gi: unmarked material is no-gi; gi-specific material carries a **Gi.** label. Notes are tagged `gi`/`nogi`/`both` in the ingest log.
- Voice: second person, present tense, no first person, no "in class today," no instructor names in `positions/` or `chains/`.
- Technique detail lives once, in `positions/`. Chains, the map, and the submissions index link to it.
- Every relative link and heading anchor must pass `python3 ingest/checklinks.py`.
- Raw note text is never committed. Contributors are credited in `CONTRIBUTORS.md`; where material comes from is recorded per `CONTRIBUTING.md`.
- License is CC BY-SA 4.0; contributions are accepted under the same.

## Ingesting a note

`/ingest-note inbox/<file>` — or follow `ingest/PROCESS.md` by hand. One branch and PR per batch.
