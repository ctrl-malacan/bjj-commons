# Contributing

Opensource BJJ improves the way open-source software does: people who know something fix it, add to it, and disagree in the open. Any belt, any lineage.

## What kind of contributions help

In rough order of how welcome they are:

1. **Corrections.** A detail that's wrong, a side that's flipped, a name that's off (e.g. calling a heart choke an "arm-in choke"). Small PR, one-line explanation. These are the most valuable contributions and the easiest to merge.
2. **Additional detail on an existing technique.** A grip, a weight-distribution cue, a common mistake. Add it in place, under the relevant section.
3. **A variation or alternative.** Your academy does the knee slice entry differently. Add it as a clearly labeled variation rather than replacing what's there — different lineages disagree, and the disagreement is informative.
4. **A new chain.** A decision tree connecting existing techniques, drawn as a [Mermaid](https://mermaid.js.org/) flowchart with edges labeled by the opponent's reaction (see [`chains/`](chains/) for the format). Chains are maps, not manuals: a diagram plus links into the position pages, never the full technique detail — that lives in one place, in `positions/`, so it can't drift.
5. **A new position or technique.** Welcome, but open an issue first so we can agree on where it goes. Keep scope to what a white or blue belt would actually use.
6. **Gi material.** Welcome at any of the levels above. Gi techniques belong here too. Mark them (see Style) so readers of either kind can find or skip them; if a position page needs a gi section, add one.

Things that don't fit: competition-rules commentary, and anything that's a link to a video with no written explanation.

## Attribution

Two layers, both light:

1. **You.** Every contribution is credited to its contributor. Add yourself to [CONTRIBUTORS.md](CONTRIBUTORS.md) in your first PR — name or handle, and optionally your belt and where you train or who you learn from. That's your default source for everything you add.
2. **Your source, when it differs.** If a specific technique comes from somewhere other than your default — a seminar, a different coach, a video you then drilled — say so inline, briefly: *Source: [instructor], [academy or event], [year].* "Own experience" is a fine source too.

If you're correcting something and your source disagrees with what's there, keep both and note the disagreement rather than overwriting. Different lineages disagree, and the disagreement is useful.

## Style

- **Sides.** Follow the page's stated default side. If you must switch, say so.
- **Voice.** Plain second person ("you step your right foot…"). No hype.
- **Length.** A section should be readable between rounds. If a technique needs 800 words, it probably needs to be split into a setup and a finish.
- **Terminology.** Use the term most common in no-gi. Where names vary (D'Arce/brabo, front headlock/head-and-arm), use the one already in use here and mention the alternate once.
- **Links.** Cross-reference other pages with relative links rather than "see the mount page."
- **Gi / no-gi.** Unmarked material is no-gi. Mark gi-specific material with **Gi.** at the start of the paragraph or "(gi)" in the heading; mark material that works in both with **Gi and no-gi.** only where the distinction matters. When ingesting a note, tag it `gi`, `nogi`, or `both` in the log.

## Process

**The easy way.** Record or write up what you learned, save it as a plain text or markdown file in `inbox/` (it is gitignored), and run `/ingest-note inbox/<your-file>` with a coding agent that supports skills. The skill follows [`ingest/PROCESS.md`](ingest/PROCESS.md): it works out which page and section the note belongs to, edits in the page's voice, updates the chain diagram, submissions index, and position map as needed, and logs the note. Review the diff, add yourself to CONTRIBUTORS.md, open the PR. Your raw note is never committed to the repo.

**By hand.**

1. Fork, branch, edit the markdown. First time? Add yourself to CONTRIBUTORS.md.
2. Open a pull request. Explain what you changed and why in a few sentences; for corrections, say what was wrong.
3. Expect questions. If a change conflicts with what's already there, we'll likely keep both with sources noted rather than pick a winner.

By contributing you agree your contribution is licensed under [CC BY-SA 4.0](LICENSE), the same as the rest of the project.

## Origins

Opensource BJJ started in 2026 as one white belt's class notes, and it exists because writing things down after class turned out to be the best way to learn them.

**Scott Kelly** started jiu-jitsu as an adult beginner and trains at Park Slope Academy of Brazilian Jiu-Jitsu in Brooklyn. He builds software for a living, which is where the open-source framing comes from — and, as a white belt, he is the first to say that any mistakes in the early material are his.

**Marc Adami** is his instructor — a Team Checkmat black belt under Fabio Clemente and Leo Vieira, co-founder of [Park Slope Academy](https://www.psabjj.com/), and a multiple-time Pan American and Pan American No-Gi champion. Much of the early material comes from class notes of his lessons. He is a generous and genuinely gifted teacher, and the kind of person you hope to find when you walk into a gym for the first time — if you are anywhere near Brooklyn, you would be lucky to [train with him](https://www.psabjj.com/).

Marc is not involved in this project and has not reviewed it. Nothing here is his or the academy's official material; it began as a student's record of what was taught, and is now a shared reference that anyone can correct.

**Human created, AI written.** The seed content is 116 class notes dictated into a voice-notes app after training, then organized into these pages with an AI assistant following the same ingest process contributors use now (`ingest/PROCESS.md`). Every technique came from a class, every note was spoken by a person, and every change is reviewed by a person before it is merged. The AI does the organizing and the prose. The jiu-jitsu is people's.

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for everyone who has added to it since.
