# Key: Arena loss 11/22/2026: Anvil, Sycophant, Mountain Folk

## Sources
- [Replay of dominion.games 186276838](https://dominion-arena.duckdns.org/game/dominion.games-dominion.games:186276838/replay): Gemini 4 Neon (high effort, playing first) lost 34–49 to a human at level 56. Neon's plan opened Temple/Anvil, spent Anvil gains mainly on Blessed Village, and aimed to reach Expand through Crucible. It called Sycophant cycling "Free bonus if we cycle Sycophants, not worth forcing."
- [Neon vs Neon with and without the insight](https://github.com/colonelpanic8/dominion-agent-review/tree/master/experiments/2026-11-24-neon-insight-selfplay): games g20 and g24 (seed 1, told seat first, then second) and g27 (seed 2, told seat first).

## Expert summary
Favors are the engine on this board. Sycophant gives +2 Favors whenever it is gained or trashed. Mountain Folk spends 5 Favors for +3 Cards at the start of a turn. Way of the Horse turns any Action into +2 Cards and +1 Action and returns it to its pile, so a Sycophant played that way can be gained again for 2 more Favors. Anvil gains a card costing up to $4 for a discarded Treasure, and the Coppers and Lucky Coin's Silvers feed it.

So open Anvil/Anvil and put the early Anvil gains into Sycophants, with a Temple for thinning. Two Sycophant gains plus the starting Favor pay for +3 Cards by turn 4. That early draw reaches Expand quickly, without waiting on Crucible. From there, Sycophants cycle through Horse and Anvil for a steady supply of Favors, and spare Anvil gains take Temple for its VP.

In the source game the human opened Anvil/Anvil, gained Temple and Sycophant with the first pair, bought another Sycophant, used Mountain Folk from turn 4 and reached Expand early. Neon reached Expand four turns later.

In all three self-play games, the told seat used Mountain Folk first on turn 4 and gained its first Expand on turn 4 or 5. The untold seat repeated the Blessed Village/Temple plan, used Mountain Folk first on turns 6–9 and gained its first Expand on turns 6–9. The told seat won 37–28, 41–35 and 44–32.

## Rubric
- **R1** [core] (result) Identifies Sycophant's +2 Favors on gain and on trash, with Mountain Folk's 5 Favors for +3 Cards, as the board's draw engine.
- **R2** [core] (result) Opens Anvil/Anvil, or another opening that gains Sycophants on turns 3–4, and puts early gains into Sycophants so Mountain Folk fires by turn 4.
- **R3** [supporting] (result) Cycles Sycophants: plays spare ones as Way of the Horse (returning them to the pile) and regains them with Anvil for fresh Favors.
- **R4** [supporting] (result) Gets Expand early off the Favor draw rather than through Crucible, and uses spare gains on Temple for VP and thinning.

## Traps
- **T1** (result) Treating Sycophant/Mountain Folk as a side bonus and building Blessed Village draw toward a Crucible-funded Expand. This lost the source game, and the untold seat lost all three self-play games with it.

## Disagreements
- How many Sycophants to hold at once versus cycling them through Horse. The human and the told seats kept gaining them throughout. The right count depends on how often Mountain Folk fires.
- Whether Temple belongs in the opening. The human gained it with an early Anvil.

## Grader notes
- Quality B: the plan is confirmed against the same agent, not by expert consensus, and over three games rather than six. A Favor-draw plan that reaches Sycophants by buying rather than Anvil earns partial credit for R2.
