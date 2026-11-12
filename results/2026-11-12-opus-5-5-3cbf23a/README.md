# 2026-11-12 Opus 5.5, dominion-agents 3cbf23a

Sixteen blind analyses of the same kingdoms as `../2026-11-11-opus-5-5`,
after dominion-agents was reworked on master (`3cbf23a`): the strategy
context is organized around deck composition, reliability and deck
control, engines are the default plan, step 3 of `kingdom-analysis` is the
engine question, the playouts are gone, and the card ratings are inlined
into the context.

Same analyst and graders as the earlier runs: Claude Opus 5.5, headless,
one sandbox per case, tools `Read,Glob,Grep,Skill`; Opus 5.5 graders at
high effort, two cases each, following `grading.md`. No analyst read a file
outside its sandbox. Each cost $0.54–0.89 and took 1.5–5 minutes, $11 in
all.

## Scores

Rubric / plan match per case. Post-cutoff cases are dated after June 2026.
"Old 1" and "Old 2" are two runs at `fbad6da`; `0c0c5b7` was the first
rewrite (`../2026-11-11-opus-5-5-0c0c5b7`).

| Case | Cutoff | Old 1 | Old 2 | `0c0c5b7` | `3cbf23a` | Traps fell | Main miss at `3cbf23a` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| horton-2019-09-finals1 | pre | 0.35 / 4 | 0.25 / 3 | 0.50 / 4 | 0.35 / 4 | 0 | Old Witch money; rejects Bridge as payload and Diplomat as the village |
| horton-2025-10-designed3 | pre | 0.31 / 3 | 0.63 / 6 | 0.75 / 7 | 0.13 / 3 | 0 | Destrier/Mystic deck; pushes the Forts aside and skips Tent/Exploration and Garrison |
| horton-2026-04-finals | pre | 0.50 / 4 | 0.64 / 5 | 0.36 / 5 | 0.36 / 4 | 1 | Governor engine; dismisses Tactician with Way of the Owl and the Leprechaun Wish line |
| horton-2026-09-finals | post | 0.69 / 6 | 0.62 / 6 | 0.73 / 7 | 0.73 / 6 | 0 | Right engine, but Province turns from turn 10, not one turn-7 turn of several Triumphs |
| horton-2026-09-semi1 | post | 0.43 / 3 | 0.43 / 3 | 0.43 / 4 | 0.79 / 6 | 0 | Reckless Transmute as an optional buy, not the key card; no Lurker/Transmute endgame |
| horton-2026-09-semi2 | post | 0.44 / 4 | 0.19 / 2 | 0.31 / 3 | 0.69 / 6 | 1 | Opens Enlarge/Squire, not Armory into Transmogrify; early $5s before Ronin |
| kotw-2021-06-27-bank-counting-house | pre | 0.55 / 6 | 0.45 / 4 | 0.50 / 5 | 0.41 / 4 | 0 | A Talisman/Tower Copper race, not topdecking every gain; finish turn 13–15 vs 8–9 |
| kotw-2021-09-12-butcher-city-quarter | pre | 0.45 / 5 | 0.55 / 5 | 0.27 / 3 | 0.45 / 5 | 0 | Money with City Quarter added late, not the City Quarter engine |
| kotw-2022-04-24-courtier-mandarin | pre | 0.63 / 5 | 0.50 / 5 | 0.50 / 5 | 0.75 / 5 | 1 | Mandarin's on-gain effect as a one-off; never buys Mandarin; opens Cardinal |
| makingluck-ep101-scrying-pool-hunting-grounds-forge | pre | 0.56 / 6 | 0.50 / 6 | 0.61 / 6 | 0.67 / 6 | 1 | Opens Trader/Silver; dismisses Scrying Pool with Noble Brigand |
| oc-2025-final-g2 | pre | 0.59 / 5 | 0.77 / 7 | 0.82 / 8 | 0.86 / 6 | 1 | Opens Monastery instead of Grotto; the midgame plan matches |
| oc-2026-final-g1 | post | 0.13 / 2 | 0.06 / 2 | 0.63 / 6 | 0.69 / 5 | 0 | Litter engine aimed at Provinces; Vineyards a side source, not a three-pile race |
| oc-2026-final-g2 | post | 0.95 / 8 | 0.65 / 5 | 0.65 / 5 | 0.80 / 7 | 0 | Rope as one of several +Buys; no Copper-first $0 Wayfarer trick |
| oc-2026-final-g3 | post | 0.39 / 4 | 0.39 / 3 | 0.39 / 4 | 0.40 / 3 | 1 | Horn as one payload among others, not 6–7 Horns for one turn; opens Forager |
| oc-2026-final-g4 | post | 0.69 / 6 | 0.63 / 6 | 0.75 / 6 | 0.69 / 6 | 1 | Ritual on Flag Bearer as late payload; never sees the Flag war taking over |
| oc-2026-final-g5 | post | 0.75 / 7 | 0.55 / 6 | 0.70 / 6 | 0.60 / 6 | 1 | Dismisses Innovation; opens Junk Dealer through Borrow instead of Caravan |

Mean rubric / mean plan match / traps fell:

| Set | Old 1 | Old 2 | `0c0c5b7` | `3cbf23a` |
| --- | --- | --- | --- | --- |
| Post-cutoff (8) | 0.56 / 5.0 / 5 | 0.44 / 4.1 / 6 | 0.57 / 5.1 / 6 | 0.67 / 5.6 / 4 |
| Pre-cutoff (8) | 0.49 / 4.8 / 4 | 0.54 / 5.1 / 4 | 0.54 / 5.4 / 4 | 0.50 / 4.6 / 4 |
| All (16) | 0.53 / 4.9 / 9 | 0.49 / 4.6 / 10 | 0.56 / 5.2 / 10 | 0.59 / 5.1 / 8 |

## Reading it

- **The mean is the highest of the four runs, 0.59, but inside the noise.**
  It is 0.08 above the two old-rules runs' average, with a standard error
  of about 0.06 on that difference. Two runs at the same revision differed
  by 0.13 per case on average.
- **The gain is on the post-cutoff boards**: 0.67 against 0.44–0.57
  before. Three cases moved by more than the noise: oc-2026-final-g1 (0.13
  and 0.06 at the old rules, 0.69 now), horton-2026-09-semi1 (0.43 in all
  three earlier runs, 0.79 now) and horton-2026-09-semi2 (0.19–0.44, now
  0.69). Pre-cutoff boards are flat at 0.50.
- **One case fell by more than the noise**: horton-2025-10-designed3, 0.13
  against 0.31–0.75. The analysis built a Destrier/Mystic deck and set the
  Forts aside.
- **The analyst now picks the engine.** Twelve of the 16 recommendations
  are engines, three are money decks and one is a Copper flood. One of
  the money picks agrees with the key (the Forge/Hunting Grounds deck on
  makingluck-ep101). The other two (Old Witch money on
  horton-2019-09-finals1, Butcher money on Butcher/City Quarter) are the
  only boards left with the first run's most common miss, turning down
  the experts' engine for money.
- **What it misses has changed, not gone.** The usual miss is now the
  right kind of deck with the wrong centre: a Province engine where the
  experts raced for Vineyards, Horn as one payload instead of seven, the
  Flag as a side prize. The specific tricks are still missed in every run:
  Tactician with Way of the Owl, the Copper-first $0 Wayfarer, Mandarin
  replaying Golds, Night Watchman setting up City Quarter.
- **Speed estimates are still slow** where the key has a fast finish
  (turn 13–15 against 8–9 on Bank/Counting House, turn 10 against 7 on
  horton-2026-09-finals).
- One grade is soft: Courtier/Mandarin's 0.75 gives partial credit on two
  core items for a plan that never buys Mandarin. The grader put it at
  0.62 with those scored as misses.
