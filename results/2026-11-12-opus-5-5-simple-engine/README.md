# 2026-11-12 A simple engine board: Village, Smithy, Chapel, Bridge

Five games on a kingdom chosen to have one obvious engine, to watch how
the agents play it: Village, Smithy, Chapel, Bridge, Cellar, Moat,
Workshop, Market, Festival, Remodel. No landscapes, Colonies or Shelters.
This kingdom is not a benchmark case and has no key. `kingdom.md` is the
brief the players read.

## Games

| Game | First | Second | Winner | Score | Turns |
| --- | --- | --- | --- | --- | --- |
| `ga` | dominion-agents `3cbf23a` (new) | `fbad6da` (old) | Old | 43–37 | 20 each |
| `gb` | `fbad6da` (old) | `3cbf23a` (new) | Old | 45–36 | 24 / 23 |
| `vs-claude` | Opus 5.5 with no guidance | Claude, playing Village/Smithy/Bridge | Claude | 45–30 | 13 each |
| `guided` | Opus 5.5 with no guidance | dominion-agents `eb8da29` | No guidance | 47–35 | 25 each |
| `target` | Opus 5.5 with no guidance | `eb8da29`, target deck given | Target deck | 52–21 | 14 each |

- **`ga`, `gb`**: Opus 5.5 players at high effort, each analyzing the
  kingdom with its own revision's `kingdom-analysis` and told to use
  `play-turn` for every decision. All four loaded both skills. Server:
  dominion-engine `solo-play` `db578ac`, seed 404.
- **`vs-claude`**: the seat "Claude" was played by the session that ran
  these tests, by hand through the server's JSON API, after the repository
  owner pointed out that the agents' plans were poor and described the
  board as "a Village, Smithy, Bridge game" with no Gold. The seat "Opus"
  was Opus 5.5 at high effort in a sandbox holding only the kingdom brief.
  Server: dominion-engine `web-client` `016f12e`, seed 505.
- **`guided`, `target`**: the same opponent, seat order, server and seed as
  `vs-claude`. The second seat was Opus 5.5 at high effort with
  dominion-agents `eb8da29`, told to play the whole game with `play-game`.
  In `guided` it made its own plan with `kingdom-analysis`. In `target` it
  was given the deck Claude had built as the plan: "6 Bridges, 10 Villages,
  4 Smithies, 3 Markets, 1 Workshop, 1 Chapel and 3 Coppers", nothing else,
  and no Victory card until the winning turn. The order was left to it.
  `scripts/player.sh` has the prompts.

## What the agents did

All four agent plans (`notes-*.md`) named the right deck, "a classic Chapel
engine with Bridge payload", and then hedged it:

- every plan says "Bridge ×2–3", "Gold early" and to green "at two
  Provinces a turn";
- every plan warns against "over-trashing money";
- no plan mentions that Workshop gains bigger cards once Bridges are in
  play, or that the game can end on piles.

Final decks:

| Game | Player | Bridge | Village | Smithy | Festival | Market | Gold | Silver |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ga` | New | 2 | 3 | 3 | 2 | 1 | 2 | 2 |
| `ga` | Old | 1 | 0 | 1 | 2 | 2 | 3 | 1 |
| `gb` | Old | 3 | 3 | 3 | 3 | 1 | 2 | 8 |
| `gb` | New | 1 | 0 | 3 | 5 | 1 | 4 | 6 |
| `vs-claude` | Opus, no guidance | 0 | 0 | 2 | 0 | 0 | 3 | 2 |
| `vs-claude` | Claude | 6 | 10 | 4 | 0 | 3 | 0 | 0 |
| `guided` | Opus, no guidance | 1 | 0 | 2 | 0 | 0 | 3 | 7 |
| `guided` | `eb8da29` | 5 | 2 | 2 | 4 | 0 | 0 | 5 |
| `target` | Opus, no guidance | 0 | 0 | 2 | 0 | 0 | 4 | 3 |
| `target` | `eb8da29`, target deck given | 6 | 9 | 4 | 0 | 2 | 0 | 0 |

The agent games ran 20 to 24 turns, which is Big Money pace. Two of the
four decks had Smithies and Festivals but no Village. The unguided Opus
played plain Smithy Big Money and had 4 Provinces by turn 13; no guided
agent had more than 5 after 20 or more turns.

## The Village/Smithy/Bridge game

Claude opened Chapel and Bridge, trashed down to 3 Coppers, and bought no
Treasure at all. Workshop gained a part every turn it was played, and
gained a Market once a Bridge was in play. Gains per turn went 3, 5, 8
on turns 10 to 12 as more Bridges were played together. It had 0 VP until
turn 13, when it drew its 28-card deck, played six Bridges, and took the
last 4 Provinces (one with Workshop) and all 7 remaining Duchies.
`vs-claude/replay.md` has every play.

One game with one seed, second seat. The opponent's money deck was fast:
with a Province on its turn 14 it would have had 36 VP, and a stalled
engine turn would have made the game close.

## The updated guidance, and a given target deck

`eb8da29` makes players write out a check before every gain. It did not
change what the player chose. In `guided` the plan again read "2-3 Bridges",
with "Bridges + Gold as payload" and "keep Silver, keep ~2-3 Copper until
Festivals/Markets arrive" (`guided/notes-guided.md` has the plan as written
at the start, at turn 10 and at the end). The player opened Silver/Chapel and bought Silver on turns 1, 3 and 5,
each time for money: "the deck has no economy yet", "to rebuild the cash
Chapel removes". Its first Bridges came on turn 10, it took one Province a
turn from turn 11, and it lost to Smithy Big Money. It also bought a Copper
and a Curse by answering with an option number it had not re-read.

In `target` the same model with the same guidance was handed the deck to
build and built it: Chapel/Workshop opening, all Estates and 4 Coppers
trashed by turn 10, no Treasure and no Victory card bought. On turn 13 it
drew all 26 cards, played six Bridges and took 5 Provinces and 4 Duchies,
going from 0 to 42 VP against 18. It ended the game on turn 14. It stopped
at 9 Villages and 2 Markets because buys ran out on turn 12.

So the model can execute this deck when the plan names it in counts. What
it does not do from the current guidance is choose that deck: left to plan
for itself, it buys money early and treats Bridge as a discount on one or
two Provinces a turn.

`target` is not a like-for-like repeat of `vs-claude`. The unguided
opponent had 2 Provinces by turn 13 there against 4 in `vs-claude`, so the
52–21 margin says more about the opponent's draws than about the engine.

## Notes

- Replays for `guided` and `target` give each player's reason under every
  gain. A reason marked "from the player's thinking" or "reply" is what
  the player wrote just before the move, where it did not write the
  `REASON` line it was asked for. Claude's reasons in `vs-claude` come from
  that session's notes at the time; Opus was not asked for reasons there.
- `gb` has no replay: the disk filled while the game was ending, which
  truncated the spectator's file and the end of both players' logs. The
  result and final decks were read from the server afterwards.
- Cost: `ga` $5 for two players, `gb` about the same (logs cut off), the
  unguided opponent in `vs-claude` $3.70, `guided` $19 ($11.80 for the
  guided seat) and `target` $14 ($11.35 for the guided seat). The last two
  ran on a server with no multi-move tool, so every play was one call.
