# Key: Arena loss 11/19/2026: Fortress, Advance, Villa, Cavalry

## Sources
- [Arena g340](https://dominion-arena.duckdns.org/game/g340/replay) and [g339](https://dominion-arena.duckdns.org/game/g339/replay): a mirror pair, the same kingdom with the seats swapped. Opus 5.5 (high effort) beat GPT-6.2 Sol (high) 26–12 and 17–4.
  - In g340 Sol opened Silver/Cavalry for a Cavalry/Villa draw deck. Its plan said "Hunting Grounds is the sustained draw; Fortress is backup village support."
  - In g339 Sol opened Groom/Lurker for Hunting Grounds. Its plan noted that "Advance can turn a spare Buy and a Fortress in hand into a Hunting Grounds without losing the Fortress", but did not open for the loop.
  - Opus opened Fortress in both games and ran the loop on turn 4 (g340) and turn 3 (g339).
- [Sol vs Sol with and without the insight](https://github.com/colonelpanic8/dominion-agent-review/tree/master/experiments/2026-11-25-loser-model-selfplay): games g1, g6, g11, g16, g21 and g26.

## Expert summary
Fortress and Advance make a loop that gains Actions for free. Advance is a $0 Event: trash an Action from your hand, gain an Action costing up to $6. A trashed Fortress goes back into your hand. So with Fortress in hand, every Buy spent on Advance gains an Action, and Fortress is ready to trash again.

The loop pays for itself. Villa goes into your hand when gained, with +1 Action, and returns you to your Action phase; played, it gives +2 Actions, +1 Buy and +$1, so the Buy comes back. Gaining Cavalry gives +1 Buy and +2 Cards and returns you to your Action phase too. One Fortress in hand and one Buy can take the whole Villa and Cavalry piles in a turn or two, with Horses and the drawn cards turning it into Provinces.

So get Fortress early (open it, or Lurker it from the trash), keep it in hand rather than playing it, and start looping on turn 3 or 4. Mill is an Action–Victory card costing $4, so Advance gains it too. Score Provinces and Mills before emptying a third pile: two piles go fast.

In the source pair, Opus took all the Villas and Cavalries and a Province on its loop turn and then ended the game on Mills. In the six self-play games the told seat gained its first Advance on turn 3 or 4, made 19–24 Advance buys, and took 9–10 Villas and 7–10 Cavalries. The untold seat made 0–4 Advance buys and at most one Villa.

## Rubric
- **R1** [core] (result) Identifies the Fortress/Advance loop: Advance trashes Fortress, which returns to hand, so each Buy on Advance gains an Action costing up to $6.
- **R2** [core] (result) Sees that Villa (+1 Buy when played, returned to the Action phase on gain) or Cavalry (+1 Buy on gain) replaces the Buy, so the loop repeats within a turn.
- **R3** [core] (result) Makes the loop the opening plan: Fortress on turns 1–2 (or via Lurker) and kept in hand, looping by turn 3–4.
- **R4** [supporting] (result) Plans the ending: Provinces and Mills (Advance gains Mill) before a third pile empties, with Villa and Cavalry as the two fast piles.

## Traps
- **T1** (result) A conventional draw engine (Hunting Grounds, Cavalry/Villa, Highway) with Fortress as a village and Advance as an occasional upgrade. This lost both source games, and the untold seat lost five of six self-play games with it.

## Disagreements
- How early to commit to Mills. Opus used Advance into Mills to end both games; the told seats in self-play often emptied Villa and Cavalry first and scored with Provinces.
- Whether Lurker (trash Fortress from the Supply, then gain it from the trash) is worth it when the split does not reach $4.

## Grader notes
- Quality B: the line is confirmed against the agent that lost, not by expert consensus. A plan that finds the loop but only as a mid-game trick, after a conventional opening, earns partial credit for R3 and does not fall into T1.
