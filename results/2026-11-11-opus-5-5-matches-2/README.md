# 2026-11-11 Opus 5.5 matches, round 2: seats swapped, better play instructions

The three pairings from `../2026-11-11-opus-5-5-matches`, each played from
both seats, after changing how the players were set up.

## What changed from round 1

- **Players**: dominion-agents `ec1d23e` (tag `bench-2026-11-11` there).
  Its `play-turn` skill adds a stock-take of the whole deck before every
  gain, a plan and race review after each reshuffle, and written score
  math in the endgame.
- **Prompt**: round 1 told players to keep their reasoning short; this
  one told them to follow the skill and play to win. High effort.
- **Notes**: each player could write one file, `notes.md` (all other
  writes denied), for the target deck, milestones and the opponent's clock.
- **Expert plans**: round 1 handed the expert the raw `key.md` (sources,
  rubric, grader notes). This round it got a playbook written from the key
  in the shape of an analysis (`plans/`), with the parts the key doesn't
  give marked as filled in.
- **Analyst plans**: unchanged, so these games compare with round 1.
- **Seats**: each pairing played twice on the same seed, seats swapped.
  Server: dominion-engine `solo-play` `105289f`, 2 players, no Colonies
  or Shelters.

## Results

| Game | Kingdom | First | Winner | Score | Turns | Ended on |
| --- | --- | --- | --- | --- | --- | --- |
| g1a | oc-2026-final-g1 | Analyst | Expert | 71–58 | 24 each | piles |
| g1b | oc-2026-final-g1 | Expert | Analyst | 66–64 | 30 each | turn limit |
| g2a | oc-2026-final-g5 | Expert | Analyst | 46–24 | 17 each | Provinces |
| g2b | oc-2026-final-g5 | Analyst | Analyst | 45–22 | 18 / 17 | Provinces |
| g3a | courtier-mandarin | Analyst | Analyst | 54–36 | 19 / 18 | Provinces |
| g3b | courtier-mandarin | Expert | Analyst | 38–30 | 15 each | Provinces |

Round 1, same seeds and seat order as the `a` games: g1 Expert 66–64, g2
Analyst 39–23, g3 Analyst 38–26.

## What happened

- **Vineyards (g1)** is the one board where the expert plan works. In g1a
  it won by 13 on a three-pile ending it controlled, since only the
  expert had Potions. In g1b it came back from well behind to lead, then
  lost by 2 when the game hit the turn cap (below) while it was setting
  up a pile ending for the next turn.
- **Sentinel/Tools (g2)**: the money plan won both seats by over 20. The
  engine never had a double-Province turn and never bought Innovation.
  One expert bought Tools before any money or +Buy and ended with 9
  Villas; the other was still building on turn 11. Both money decks had
  their first Province on turn 8.
- **Courtier/Mandarin (g3)**: money won both seats. The combo was never
  assembled: one expert bought a single Courtier, the other had the
  pieces by turn 10 but never in the same turn. Both played it as a
  Courtier money deck in the end.
- **The money side played better than in round 1.** The reports show the
  new instructions in use: Duchies from 3 Provinces left with the score
  math written out, Barge's draw held for a sure Province turn, Lost City
  left unplayed to keep Golds for the next shuffle.

## Reading it

- With more thinking, notes, a playbook and both seats, the expert plans
  still lost on Sentinel/Tools and Courtier/Mandarin, by more than in
  round 1. On these boards this model doesn't execute the engine or the
  combo well enough to beat a tuned money deck. Its reports say so too:
  pieces bought in the wrong order, the deck not drawing itself, the
  combo never in one hand.
- The comparison still favours the analysts somewhat. Their plans for g2
  and g3 came with turn-by-turn build lines from solo test games; the
  expert playbooks give the experts' ideas but no tested build order.
- Vineyards worked because its build is simple: buy many cheap Actions
  and Vineyards. Both Vineyard games were close or won.

## Problems in this run

- **Turn cap**: `turn_limit: 60` counts both players' turns, so games
  stopped at 30 turns each. That decided g1b. The view doesn't show the
  cap, so players couldn't plan around it.
- **A `steps` bug cost two experts a buy**: after the last Action the
  phase moves on to Buy by itself, and an `end` in the same call then
  ended the Buy phase (g2a turn 7, g2b turn 9). Fixed in dominion-engine
  `solo-play` `41418c3`. Neither game was close.
- **Auto-memory**: two players saved notes to Claude Code's auto-memory
  folder (about the turn cap and the `end` bug). Each folder was keyed to
  that player's own sandbox, so nothing reached another player. The notes
  were deleted after the run.

Players read nothing outside their sandboxes. Apart from one tool timeout,
the only errors were a "not joined" call at the start of each game.

Cost: $50 for the 12 players ($2.30–8.40 each; the long Vineyard games
cost most). Output was about 2,000 tokens per turn on the expert side,
against about 1,400 in round 1.

Each game folder has both players' final views, their reports and their
`notes.md`.
