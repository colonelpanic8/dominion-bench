# Key: Arena loss 11/23/2026: Siren, Transport, Wharf

## Sources
- [Replay of dominion.games 186295827](https://dominion-arena.duckdns.org/game/dominion.games-dominion.games:186295827/replay): Gemini 4 Neon (high effort, playing second) lost 18–38 to a human at level 56. Neon's pre-game plan opened double Transport for Wharf. It named Transport into Siren only as a branch "if P1 goes aggressively for Siren", and kept to Wharf after the opponent exiled Siren on turn 1.
- [Neon vs Neon with and without the insight](https://github.com/colonelpanic8/dominion-agent-review/tree/master/experiments/2026-11-24-neon-insight-selfplay): games g1 and g4, seed 1, with the told seat moving first in g1 and second in g4.

## Expert summary
Siren decides this board. Its Curse can't be blocked, and the only trashing is Trade, a $5 Event that turns cards into Silvers. So whoever plays Siren first and most often wins the Curse split, and every Siren play also draws its player up to 8 next turn. Transport gets Siren without its on-gain cost: Exile Siren from the Supply, then put it from Exile onto your deck. Neither step is a gain, so nothing has to be trashed. On a 4/3 opening that means Transport on both turns and a Siren in the turn-3 hand. In the source game, the human exiled Siren on turn 1 and overpaid $2 for Farrier on turn 2. On turn 3 it bought Siren, trashing the Farrier to keep it, which also released the exiled copy. Its two Sirens gave Neon eight Curses. In self-play the told seat built two Sirens and won both games, 3 to −4 and 2 to −4. The untold seat built Wharfs (five and seven), took seven Curses each time, and had one late Siren and no Siren respectively. Wharf/City/Destrier draw and Jewelled Egg + Trade for Loot are the follow-up, once the Sirens are cycling. City gets better once Curses run out.

## Rubric
- **R1** [core] (result) Names Siren's Curse attack as the board's deciding factor: unblockable, with Trade as the only trashing.
- **R2** [core] (result) Uses Transport to get Siren without its on-gain trash (Exile, then put it onto the deck); on 4/3, Transport both turns for a turn-3 Siren.
- **R3** [supporting] (result) Gets a second Siren early, by another Transport or by the Farrier-overpay line, so the two alternate.
- **R4** [supporting] (result) Builds Wharf/City/Destrier draw and Egg/Trade payload only after the Sirens are running; notes City improves once Curses run out.

## Traps
- **T1** (result) Opening double Transport into Wharf and leaving Siren for later, or for only if the opponent goes for it: this lost the source game, and lost both self-play games as the untold seat.

## Disagreements
- Whether the Farrier-overpay line (two Sirens by turn 3 when the turn-3 hand finds Farrier) beats the guaranteed double-Transport line. The human took the former. The told seat was told the latter and also won.
- How much payload to add after the Curse split. Both self-play games ended on piles at low scores.

## Grader notes
- Quality B: the plan is confirmed against the same agent, not by expert consensus. A Siren-first plan that reaches Siren by other means (bought, losing an Action to its on-gain trash) earns partial credit for R2.
