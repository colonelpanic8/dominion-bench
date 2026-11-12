# 2026-11-11 Opus 5.5, dominion-agents fbad6da

Sixteen blind analyses by Claude Opus 5.5 (`claude-opus-5-5`, knowledge
cutoff June 2026) with the `kingdom-analysis` skill at dominion-agents
`fbad6da`. Each case is in its own `<case>/` folder with `analysis.md` and
`grade.md`.

## Setup

- **Analysts:** one sandbox per case, built with `scripts/bench.py sandbox`.
  Each analyst was a headless `claude -p` run inside its sandbox with tools
  `Read,Glob,Grep,Skill`, `--setting-sources project`,
  `--strict-mcp-config --no-chrome --disallowedTools "mcp__*"`, and default
  effort. The prompt asked for a full analysis of `kingdoms/<case>.md`.
- **Blindness:** the tool-call logs show no analyst read a file outside its
  sandbox. Every run loaded the skill, grepped the Glicko CSVs and read its
  brief. Each cost $0.56–0.81 and took 2.5–4.5 minutes, $11 in all.
- **Grading:** eight Opus 5.5 graders (high effort) with two cases each,
  following `grading.md`.

## Scores

Post-cutoff cases are those dated after June 2026.

| Case | Quality | Cutoff | Rubric | Traps fell | Plan match | Main miss |
| --- | --- | --- | --- | --- | --- | --- |
| oc-2026-final-g2 | B | post | 0.95 | 0 | 8 | Skipped the Copper-first $0 Wayfarer trick behind the wide Artificer deck |
| oc-2026-final-g5 | B | post | 0.75 | 1 | 7 | Opened Junk Dealer over Caravan; missed Villa making Innovation work |
| horton-2026-09-finals | A | post | 0.69 | 0 | 6 | Found the engine but expected a slow cash-in, not one ~55 VP turn around T7 |
| oc-2026-final-g4 | C | post | 0.69 | 0 | 6 | Ritual on Flag Bearer reclaiming the Flag mentioned only in passing |
| horton-2026-09-semi2 | A | post | 0.44 | 1 | 4 | Souk engine with one Ronin; dismissed the Armory → Transmogrify opening |
| horton-2026-09-semi1 | B | post | 0.43 | 1 | 3 | Called Reckless Transmute too slow; no Lurker/Transmute endgame |
| oc-2026-final-g3 | B | post | 0.39 | 1 | 4 | Forager/Scrounge engine with 2 Horns, not many distinct $5s for one big Horn turn |
| oc-2026-final-g1 | C | post | 0.13 | 1 | 2 | Rejected Vineyards, the Litter engine and the three-pile ending that won |
| kotw-2022-04-24-courtier-mandarin | C | pre | 0.63 | 0 | 5 | Saw Mandarin's gain effect only as a late one-off |
| oc-2025-final-g2 | A | pre | 0.59 | 0 | 5 | Gladiator/Fortune money; rejected the Farmhands/Peddler engine |
| makingluck-ep101-scrying-pool-hunting-grounds-forge | A | pre | 0.56 | 1 | 6 | Opened Trader/Silver; missed Scrying Pool setting up Noble Brigand |
| kotw-2021-06-27-bank-counting-house | A | pre | 0.55 | 0 | 6 | Slow Talisman build instead of Coppers and Banks; finish T15–17 vs T8–9 |
| horton-2026-04-finals | A | pre | 0.50 | 1 | 4 | Rated Tactician "Skip", the card the board was designed around |
| kotw-2021-09-12-butcher-city-quarter | B | pre | 0.45 | 1 | 5 | Dismissed Night Watchman topdecking City Quarter |
| horton-2019-09-finals1 | A | pre | 0.35 | 0 | 4 | Rejected the Diplomat/Bridge engine; called the Sewers–Hermit trick useless |
| horton-2025-10-designed3 | A | pre | 0.31 | 1 | 3 | Tent/Cabin Boy money; dismissed Garrison, Exploration and Reckless Guide |

| Set | Cases | Mean rubric | Mean plan match | Traps fell |
| --- | --- | --- | --- | --- |
| Post-cutoff | 8 | 0.56 | 5.0 | 5 |
| Pre-cutoff | 8 | 0.49 | 4.75 | 4 |
| All | 16 | 0.53 | 4.9 | 9 |

## Against the pilot

The pilot (`../2026-11-kotw-pilot`) scored the old skill at `aa01fbc` with
0–10 judgments, not rubric scores. Butcher/City Quarter went from 5 to a
plan match of 5, and Courtier/Mandarin from 4 to 5. Both still make the
pilot's misses: Night Watchman setting up City Quarter, and Mandarin as the
centerpiece.

## Patterns

- **Turns down the experts' plan.** The most common miss is rejecting the
  plan the experts chose, usually an engine or a non-Province scoring route
  (Vineyards, Diplomat/Bridge, Tactician, Reckless Transmute, Farmhands),
  and building money or a smaller hybrid instead. Most traps it fell into
  come from this.
- **Underrates cross-turn tricks.** It misses plays that set up a later
  turn: topdecking (Night Watchman, Mandarin), making a card cost $0 before
  buying it (Wayfarer), and holding off for one very large turn (Horn,
  Weaver/Triumph). This matches the pilot's finding.
- **Overestimates game length.** Expected finish turns run long (T12 or
  T15–17 where the key has T7–9).
- **Arithmetic and rules slips.** A few, none of which changed a score:
  Bridge cost reduction, Ritual VP, and Weaver gaining Gold under Flourishing
  Trade.
