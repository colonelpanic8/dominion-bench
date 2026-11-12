# dominion-bench

A benchmark for Dominion kingdom analysis: kingdoms with expert analysis,
used to grade how well an agent reads a board before the game. It is built
to test the context and skills in
[dominion-agents](https://github.com/colonelpanic8/dominion-agents), but any
analyst can be graded against it. Each case pairs a kingdom (what the agent sees) with an
answer key built from published human analysis (what the grader sees).

There is no true ground truth for most kingdoms: almost every board is played
once, and experts disagree. The keys record what strong players said and how
much to trust it. Grade against the key's rubric, not against one game's
result.

## Layout

- `cases/<id>/case.json`: the kingdom and metadata. Safe to show the analyst.
- `cases/<id>/key.md`: the answer key. **Never show it to the analyst.**
- `raw/`: fetched source text, transcripts and images, kept locally for
  re-grading. It is gitignored because the sources are other people's work;
  the keys paraphrase them, with short quotes and links.
- `scripts/bench.py`: validate cases, render a kingdom brief, build a blind
  sandbox.
- `grading.md`: the grader's instructions and score sheet.
- `results/<date>-<name>/`: past runs: the analyses, grades and a README
  saying what was run (dominion-agents commit, model, cases).

## Sources

| Source | Case ids | Notes |
| --- | --- | --- |
| Adam Horton's tournament write-ups | `horton-*` | Kingdoms he designed and playtested, 2017–2026 |
| Online Championship and World Cup finals | `oc-*`, `worldcup-*` | Commentated on YouTube; kingdoms read from video frames |
| Making Luck podcast | `makingluck-*` | Transcribed with whisper; many boards were played between episodes |
| r/dominion Kingdom of the Week | `kotw-*` | Threads via the Arctic Shift archive, 2021–2025 |
| Dominion Strategy blog | `ds-*` | Annotated games (2011–12) and kingdom articles |

## Case IDs

`<source>-<date>-<slug>`, e.g. `kotw-2021-09-12-butcher-city-quarter`,
`horton-2026-09-finals`, `ds-annotated-09`, `oc-2023-final-g3`.

## case.json

```json
{
  "id": "kotw-2021-09-12-butcher-city-quarter",
  "title": "KotW 9/12/2021: Butcher, City Quarter, Tunnel",
  "source_type": "reddit-kotw",
  "date": "2021-09-12",
  "sources": [{"url": "https://www.reddit.com/r/dominion/comments/pn49ed/", "kind": "thread",
               "author": "r/dominion", "note": "24 comments"}],
  "quality": "B",
  "quality_note": "Two strong commenters with concrete lines; others agree on payload.",
  "kingdom": {
    "cards": ["Butcher", "City Quarter", "Embassy", "Faithful Hound", "Fool's Gold",
              "Merchant Guild", "Night Watchman", "Nomad Camp", "Pooka", "Tunnel"],
    "landscapes": ["Ritual", "Tower"],
    "traits": {},
    "bane": null,
    "colonies": false,
    "shelters": false,
    "players": 2,
    "setup_notes": "",
    "extra_cards": []
  },
  "kingdom_confidence": "exact",
  "edition": "Uses first-edition Embassy."
}
```

- `source_type`: `designed-tournament`, `blog-analysis`, `annotated-game`,
  `reddit-kotw`, `commentated-match`, `podcast` or `forum`.
- `kingdom.cards`: the 10 Kingdom piles, named as dominion-engine names a
  card or pile (`Catapult`, `Castles`, `Knights`, `Augurs`). A different
  count needs `kingdom.card_count_note`.
- `landscapes`: Events, Projects, Landmarks, Ways, Allies, Prophecies.
  Traits go in `traits` as `{"Trait": "Pile"}`.
- `colonies`, `shelters`: `true`, `false`, or `null` if the source doesn't
  say.
- `setup_notes`: anything else the analyst needs (Way of the Mouse's card,
  Obelisk's pile, player count oddities). Don't put analysis here.
- `extra_cards`: non-Supply cards whose text the brief should include and
  which aren't named on a Kingdom card.
- `kingdom_confidence`: `exact`, or `partial` with an explanation (e.g.
  read from a blurry screenshot, or landscapes not stated).
- `quality`:
  - **A**: designed or playtested by a top player, or a clear consensus of
    several strong players with concrete lines.
  - **B**: one strong, concrete analysis, or a thread with real agreement.
  - **C**: thin or conflicting discussion. Useful for spotting interactions,
    weak for judging the plan.

## key.md

```markdown
# Key: <title>

## Sources
- <link>: who, what kind of source, how strong the players are.

## Expert summary
One or two paragraphs: the plan the strongest voices settled on, and why.

## Rubric
- **R1** [core] (consensus) Opens Butcher/Night Watchman. "quote" (who)
- **R2** [core] (single expert) Night Watchman topdecks City Quarter ...
- **R3** [supporting] (majority) ...

## Traps
- **T1** (consensus) Berserker is weak here. "quote" (who)

## Disagreements
- Where strong voices split, and on what.

## Grader notes
- What the key can't settle; credit for good ideas the sources missed.
```

- Rubric items are specific, checkable claims an analysis should make: the
  main plan, key interactions, opening, payload, ending, matchups. Mark each
  `[core]` (the analysis is wrong without it) or `[supporting]`, and tag the
  support: `(consensus)`, `(majority)`, `(single expert)`, `(designer)`,
  `(result)` for what actually happened in play.
- Traps are tempting plays or cards the experts said were wrong.
- Quotes stay short (a sentence or less) and name who said them.

## Running a benchmark

1. Build a blind sandbox:
   `scripts/bench.py sandbox [--agents PATH] [--rev REV] <scratch-dir> <case-id>...`.
   It holds dominion-agents' context, skills and data (the working tree, or
   commit `REV`), and `kingdoms/<id>.md` briefs with exact card text. Nothing
   from this repo goes in except the briefs. Use `--rev` to compare two
   versions of the skills on the same cases.
2. Run each analyst with that sandbox as its working directory and no
   network access, asking it to analyze `kingdoms/<id>.md` with the
   `kingdom-analysis` skill. Afterwards, check its tool calls touched nothing
   outside the sandbox.
3. Grade each analysis against `key.md` with `grading.md`.
4. Save the analyses and grades under `results/`, with the dominion-agents
   commit and model used.

A blind run costs roughly 100k tokens and five minutes per kingdom. Sample:
all post-cutoff cases plus a spread of A-tier ones is a good default.

## Contamination

Analysts may have seen older sources in training. Prefer cases dated after
the model's knowledge cutoff when comparing models, and report scores for
pre- and post-cutoff cases separately.

## Checks

`scripts/bench.py check` validates every case and checks card names against
dominion-engine. `just check` runs it, with dominion-engine pinned as a flake
input (`nix flake update dominion-engine` to move it).
