# 2026-11-12 Opus 5.5 games: dominion-agents 3cbf23a against fbad6da

Six games between two Claude Opus 5.5 players that differ only in the
dominion-agents revision in their sandbox: `3cbf23a` ("new", master after
the rework) and `fbad6da` ("old", before any of the changes these runs
tested). Unlike the two rounds in `../2026-11-11-opus-5-5-matches*`, nobody
was handed a plan: each player analyzed the kingdom itself with its own
revision's `kingdom-analysis` skill, wrote the plan to `notes.md`, and
played.

## Setup

- Three kingdoms, each played twice on one seed with the seats swapped:
  oc-2026-final-g1, oc-2026-final-g5 and kotw-2022-04-24-courtier-mandarin.
- Both sides got the same prompt: analyze, then use the repository's
  context and skills for every decision. It named no skill and gave no
  playing advice. High effort. Each could write only `notes.md`;
  auto-memory was off.
- Server: dominion-engine `solo-play` `41418c3`, 2 players, no Colonies or
  Shelters, at most 50 turns each. Players were named Ash (new) and Birch
  (old) in the game.
- No player read outside its sandbox, and none needed resuming.

## Results

| Game | Kingdom | First | New's plan | Old's plan | Winner | Score | Turns |
| --- | --- | --- | --- | --- | --- | --- | --- |
| g1a | Vineyards board | New | Council Room/Litter engine, Jester, Market Square | Jester/Council Room money with one Litter | Old | 50–47 | 24 each |
| g1b | Vineyards board | Old | Litter/Patrol engine | Council Room/Jester money | Old | 52–45 | 22 each |
| g2a | Sentinel/Tools | New | Lost City/Villa/Tools engine | Lost City/Villa/Tools engine | New | 38–30 | 17 / 16 |
| g2b | Sentinel/Tools | Old | Lost City/Villa engine | Lost City/Villa engine | Old | 32–30 | 14 / 15 |
| g3a | Courtier/Mandarin | New | Courtier gaining Golds, Village Green | Village Green/Barge/Steward engine | New | 40–22 | 14 / 13 |
| g3b | Courtier/Mandarin | Old | Cardinal/Steward/Village Green/Barge engine | Barge/Courtier money | Old | 56–30 | 19 / 20 |

Old won 4, new won 2. The first player won 5 of the 6. Every game ended on
Provinces.

## Reading it

- **No sign that the new revision plays better.** Six games can't show a
  small edge either way, and seat order explains most of the results.
- **The money-leaning deck beat the engine every time they met.** Old's
  Council Room money beat new's Litter engine twice (by 3 and by 7). On
  Courtier/Mandarin the side that played Courtier for Golds won both
  games, new once and old once. The Sentinel/Tools games were mirrors and
  went to the first player by 8 and by 2.
- **The new revision picks an engine more often**: 5 of its 6 plans,
  against 3 of 6 for the old one. When its engine met a money deck it
  lost all three. That fits the two earlier rounds: this model builds
  engines too slowly and too thinly to beat a tuned money deck. The
  engine players' own reports name it: no +Buy in a deck that drew itself
  (g1b), a 60-card deck (g1a), too little money after trashing Coppers
  (g2b), one copy of each piece by turn 10 (g3a, the old side).
- **So the two tests pull apart.** The same lean toward engines raises
  the analysis score against expert keys (`../2026-11-12-opus-5-5-3cbf23a`)
  and loses games when this model has to play the engine.
- **Plans vary from run to run at one revision.** On Courtier/Mandarin
  each revision built an engine in one game and played Courtier for Golds
  in the other, and that choice decided both games.
- **Nobody tried the experts' plan on two boards.** No one bought a
  Vineyard (eight Vineyards won that board in round 2), and no one built
  around Mandarin replaying Golds; one player gained a single Mandarin
  late.

## What this run did not test

- **The `play-turn` rewrite was mostly not loaded.** With a prompt that
  names no skill, only 2 of the 6 new players loaded `play-turn`. Three
  loaded `play-game` instead and never opened `play-turn`; one loaded
  neither. Three of the 6 old players loaded their `play-turn`. So this
  run compares the strategy context and the plans it leads to, not the
  decision skill.
- `play-game` names the tools of the `dominion/play@1` protocol. The
  server here still serves its older tool names, and the prompt said to
  use those.

## Problems

- **Lost buys from `steps`' `end`.** Three players sent `end` when the
  Action phase had already ended by itself in an earlier call, which
  ended the Buy phase: g2a new (turn 7, $7), g2a old (turn 5, $6), g2b
  old (turn 9, $9). `41418c3` only covers an `end` in the same call.
- Borrow uses the Buy it gives, which several players learned by losing
  a purchase.

Cost: $44 for the 12 players ($2.30–4.80 each).

Each game folder has both players' final views, their reports and their
`notes.md` (the plan each made is at the top).
