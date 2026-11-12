# 2026-11-11 Opus 5.5 matches: an analyst's plan against the expert plan

Three games, one per kingdom, to see whether the plans the experts chose
actually beat the analysts' plans when the same model plays both sides.
Each kingdom is one where an analyst recommended money and the key's experts
built something else.

## Setup

- **Players**: two headless Claude Opus 5.5 sessions per game, each in its
  own sandbox with dominion-agents' context and skills (branch
  `engine-default`, `ea37c96`), the kingdom brief, and a `plan.md`. Each saw
  only its own plan. Tools: Read, Glob, Grep, Skill and the game's MCP tools;
  no shell, no web.
  - **Analyst** plays the analysis it was given (`plan.md` is an
    `analysis.md` from an earlier run).
  - **Expert** plays the case's `key.md`.
- **Games**: dominion-engine's MCP server (branch `solo-play`, `105289f`),
  which adds a `steps` tool so a player can take a whole turn in one call.
  2 players, no Colonies or Shelters, a 60-turn cap, fixed seeds 101, 202
  and 303.
- Each player followed `play-turn` and its plan, and wrote a report when the
  game ended. No player needed resuming.

| Game | Kingdom | Analyst's plan (its rubric score) | Expert plan | First |
| --- | --- | --- | --- | --- |
| g1 | oc-2026-final-g1 | Council Room money with Jester (0.13, `../2026-11-11-opus-5-5`) | Litter, cheap Actions and Vineyards; three-pile ending | Analyst |
| g2 | oc-2026-final-g5 | Trimmed money with Sentinel and a Lost City (0.30, `../2026-11-11-opus-5-5-b0e35fe-solo`) | Sentinel/Caravan, Tools gaining copies, many Lost Cities, Innovation | Expert |
| g3 | kotw-2022-04-24-courtier-mandarin | Barge/Courtier money (0.25, same run) | Courtier with Mandarin topdecking the Golds | Analyst |

## Results

| Game | Winner | Score | Turns | Ended on |
| --- | --- | --- | --- | --- |
| g1 | Expert | 66–64 | 25 each | Provinces |
| g2 | Analyst | 39–23 | 14 each | Provinces |
| g3 | Analyst | 38–26 | 15 / 14 | Provinces |

Final decks:

- **g1** Analyst: 7 Province, 6 Duchy, 5 Gold, 5 Silver, Council Room, Jester,
  Litter, 2 Border Guard. Expert: 8 Vineyard (7 VP each), 1 Province, 4
  Litter, 6 Market Square, 8 Border Guard, 3 Jester, 3 Potion.
- **g2** Analyst: 6 Province, 1 Duchy, 3 Gold, 2 Silver, 3 Copper, Sentinel,
  Lost City (17 cards). Expert: 2 Province, 3 Duchy, 6 Villa, 5 Lost City, 2
  Tools, Caravan, Sentinel, 2 Gold.
- **g3** Analyst: 5 Province, Duchy, Silk Road, 5 Gold, 2 Courtier, Barge.
  Expert: 3 Province, Duchy, Silk Road, 2 Gold, Courtier, Mandarin, Steward,
  Village Green.

## What happened

- **g1, Vineyards won by 2.** The money deck took 7 of 8 Provinces and led
  45–38 on turn 19; the expert took all 8 Vineyards at 7 VP each and won on
  the last Province. The analyst broke the penultimate-Province rule on turn
  25, so it was close to a coin flip. The expert's report says its Potions
  often sat unused, and it greened late.
- **g2, the engine never came together.** The expert opened as the key says
  but took its first Province on turn 9, never had a double-Province turn,
  never bought Innovation, and fed the money deck 5 cards with Lost City.
  The money deck had 2 Provinces by turn 8.
- **g3, the combo never came together.** The analyst opened 5/2 with
  Courtier on turn 1 and had a Province on turn 6; the expert opened 4/3 and
  had Mandarin and Village Green only by turns 6–8, then switched to
  Provinces.

## Reading it

- Three games, one seed each, no seat swap, so these are anecdotes. g3
  turned partly on a 5/2 against a 4/3 opening.
- In g2 and g3 the expert plan lost on execution: the model playing it
  couldn't build the engine or combo fast enough. A key says what strong
  humans would build, not that this player can build it. The same gap
  showed in the solo-tool run, where analysts played engines badly and
  then rejected them.
- So these games don't show the keys are wrong, and they don't show the
  analysts' money plans are right. They show that with this model as the
  player, the simple plan is the safer one to hand it, and that a
  benchmark scored only against expert keys rewards plans this player
  may not be able to execute.
- A fairer test would swap seats and seeds and play each pairing several
  times, ideally with a stronger player for the complex plan.

Cost: $18 for the six players ($1.60–6.60 each; g1 ran 25 turns a side).

The dominion-agents and dominion-engine commits cited here were rebased
onto a newer master after these runs. The originals are kept by the
`bench-2026-11-11` tag in each repository (`b0e35fe` stays on
dominion-agents' `solo-lines` branch).
