# Key: DS Building the First Game Engine: Village/Smithy vs Smithy Big Money

## Sources
- [Building the First Game Engine](https://dominionstrategy.com/2012/07/30/building-the-first-game-engine/),
  2012-07-30: Geronimoo (author of the first Dominion simulator) builds engines for
  the base game's First Game set step by step and tests each against Smithy Big
  Money in his simulator. An addendum reports michaeljb's stronger bot from a
  forum challenge.

## Expert summary
Smithy Big Money takes four Provinces in about 15 turns, and a beginner's engine
won't beat it. A plain Village/Smithy engine (one Silver, alternate Villages and
Smithies, Villages at least equal to Smithies) needs about 18.5 turns. Adding
Markets for +Buy (open Smithy/Silver, one Gold, about five Markets, then
Villages/Smithies) still wins only about 1 in 4. Opening Militia instead of Smithy
and adding a couple of Cellars brings it to about even. The final ingredient is
Remodel, turning Estates into engine pieces and late Golds into Provinces: open
Remodel/Silver, two Golds, one Militia, about four Markets, Villages and Smithies,
up to two Cellars, green at about five Smithies, which wins about 3 in 4 against
Smithy BM. michaeljb's bot reached 89% by using Mine instead of buying Treasure,
Remodel and Workshop to gain engine pieces, Villages early, some Markets, Militia
after a few Smithies, and up to three Cellars.

## Rubric
- **R1** [core] (simulation) Smithy Big Money is the benchmark and a naive Village/Smithy engine without +Buy or trashing loses to it.
- **R2** [core] (simulation) A winning engine combines Village/Smithy draw with Market (+Buy), Remodel (Estates into engine parts, Gold into Province), a Militia, and Cellar filtering.
- **R3** [supporting] (simulation) Keep at least as many Villages as Smithies.
- **R4** [supporting] (simulation) Keep Treasure minimal (one Silver, one or two Golds) and green late, at about five Smithies; Duchies from about 3 Provinces left.
- **R5** [supporting] (simulation) Militia early slows the money deck; an engine can play it every turn.
- **R6** [supporting] (forum bot result) Workshop and Remodel gain engine pieces, and Mine can improve Treasures instead of buying them; this beat Smithy BM about 89%.

## Traps
- **T1** (simulation) Village/Smithy with no +Buy or trashing: slower than Smithy BM.
- **T2** (simulation) Extra Treasure or early green cards in the engine: they stop it drawing the deck.

## Disagreements
- Geronimoo's own bot doesn't use Workshop or Mine; michaeljb's better bot does.

## Grader notes
- Engine bots play worse than strong humans (context/card-power.md on
  simulators), so the win rates understate the engine. The direction (engine with
  Remodel/Market/Militia beats Smithy BM) is the claim to grade.
- First-edition Base (Woodcutter). Moat isn't analyzed.
