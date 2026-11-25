# Key: Arena loss 11/21/2026: Merchant Guild, Cathedral, Cursed Village

## Sources
- [Replay of dominion.games 186232522](https://dominion-arena.duckdns.org/game/dominion.games-dominion.games:186232522/replay): Gemini 4 Neon (high effort, playing first) lost 16–68 to a human at level 57. Neon's plan put "Margrave/Vampire for $5 acceleration + attack" first, then Cursed Village, then Collection and Crown. It listed Merchant Guild only as one payload option among several.
- [Neon vs Neon with and without the insight](https://github.com/colonelpanic8/dominion-agent-review/tree/master/experiments/2026-11-24-neon-insight-selfplay): games g2 and g5, seed 1, with the told seat moving first in g2 and second in g5.

## Expert summary
Merchant Guild is the payload, and it stacks. Every Guild played gives +1 Coffers for each card gained in that Buy phase. Crown or Scepter makes one Guild pay twice. Copper costs $0, so every spare Buy is more Coffers. With several Guilds and Buys (Guild itself, Market, Collection, Way of the Monkey), one turn of buying cheap cards banks a large Coffers stack for a multi-Province turn after it. Every Action gained with Collection in play also scores +1 VP. Cursed Village is what makes the deck run: it draws back up to 6 after Cathedral's compulsory trash and Margrave's attack. Take it early, ahead of Vampire and Margrave. In the source game the human opened Cathedral and took Cardinal on turn 2, Cursed Villages on turns 3, 6 and 7, and Merchant Guild on turn 7. On turn 11 it gained 55 Coffers and 14 Collection VP, then bought seven Provinces on turn 12. In self-play the told seat built two Guilds and three Cursed Villages. The untold seat repeated Neon's original Vampire/Margrave plan with no Guild. The told seat won g2 46–14 and led g5 45–30 at turn 13.

## Rubric
- **R1** [core] (result) Makes Merchant Guild the payload: Coffers per card gained in the Buy phase, stacking across Guilds and doubled by Crown or Scepter, with $0 Copper buys counting.
- **R2** [core] (result) Takes Cursed Village early as the draw that refills the hand after Cathedral and Margrave.
- **R3** [supporting] (result) Plans a turn that buys out cheap cards to bank Coffers, then a multi-Province turn.
- **R4** [supporting] (result) Uses Collection to score the Actions gained on those turns.
- **R5** [supporting] (result) Opens Cathedral on 4/3 (both players in the source game, and both self-play seats).

## Traps
- **T1** (result) Prioritising Vampire and Margrave and treating Merchant Guild as one payload among many: this lost the source game and the self-play games as the untold seat.
- **T2** (result) Buying Crown before the deck has any village (Neon's turn-7 Crown in the source game).

## Disagreements
- How much Cardinal matters. The human used it against Neon's Silvers, but the told self-play seats won without leaning on it.

## Grader notes
- Quality B: the plan is confirmed against the same agent, not by expert consensus. Credit a Guild plan that reaches its Coffers turn through other Buys (Market, Way of the Monkey) as long as R1 and R2 are there.
