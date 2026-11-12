I played the main plan twice in the solo engine, with two different shuffles. On this board the cards that rate weakest in general are the ones that win.

**Board:** Tower gives 1 VP for each non-Victory card you own from a Supply pile that is empty at game end. So **Copper becomes a Victory card if its pile empties**. The pile holds 46, and with your starting 7 that is up to 53 VP. Talisman makes each cheap buy (Copper, Raze, Talisman itself) gain one extra copy per Talisman in play. Travelling Fair is +2 Buys for $2 and can put gains on top of your deck. Counting House puts every Copper in your discard pile into your hand. Together they make a three-pile rush in which every card you gain is a point. The Province pile (48 VP) is smaller than what this rush scores.

**Key interactions:**
- **Talisman + Talisman + Tower:** buying a Talisman with k Talismans in play gains k+1. The pile of 10 empties by about turn 7, which is the first empty pile and 10 VP that only you hold.
- **Talisman + Travelling Fair + Copper:** each Travelling Fair is a net +1 Buy for $2. Each $0 Copper buy gains 1+k Coppers. Turn 6 of seed 1 (3 Talismans in play): Talisman + Copper bought, 4 Talismans + 4 Coppers gained.
- **Counting House + Copper flood:** the Coppers you gain land in your discard pile. One Counting House turn picked up 25 Coppers (seed 1, turn 12) and, on the other seed, 23 and then 35. That is $24–37 and 15+ Buys through repeated Travelling Fair, which empties Copper as the third pile.
- **Travelling Fair puts a fresh Counting House on top of your deck:** buy it, top-deck it with exactly enough cards to make next turn's hand, and the deck never reshuffles. Next turn the Counting House picks up every Copper again. This is the first-edition "Counting House + Travelling Fair" combo in `context/combos.md`.
- **Raze** (10 at $2, Talisman copies it) is the cleanest second pile to empty. Curse also qualifies: it costs $0, isn't a Victory card and Talisman copies it, so each Curse scores −1 +1 = 0 once its pile is empty. That makes it a free emergency pile.

**Other cards:**
- **Horse Traders:** the early +Buy before you can afford Travelling Fair. It also reacts to Enchantress, Haunted Woods and Jester. Careful: its +1 Card next turn can force a reshuffle when your deck is set up empty.
- **Enchantress:** the best disruption against a Counting House turn, because it turns the first Action played into a cantrip. Absorb it by playing Raze or Settlers first. It is also $3 and copied by Talisman.
- **Settlers / Bustling Village:** can soak up Enchantress. It's a split pile, so it is harder to empty than Raze.
- **Bank:** worth $20+ alongside 20 Coppers in play, so it is optional extra $ on the big turn. Talisman doesn't copy it.
- **Farming Village:** costs $4, so Talisman copies it and it could be a backup pile. Otherwise it has no partner here.
- **Haunted Woods:** good in a money deck. Against the rush it does little, since Treasures are already played before the first buy.
- **Jester:** against a Copper deck it nets you a Copper now and then. Minor.
- **Ratings:** Counting House (−3.1), Talisman (−1.5, first edition, wide uncertainty), Bank (−1.6) and Settlers (−2.4) all rate low. Tower and the Copper pile explain the gap. Combos.md also lists Counting House + Travelling Fair as a combo.

### Build lines (`dominion solo`)
- **Talisman rush, seed 1 (4/3):**
  - T1–2: Talisman / Silver.
  - T3: Talisman (gained 2).
  - T4: Horse Traders.
  - T5: Horse Traders → Counting House + Copper.
  - T6: Travelling Fair, Talisman (gained 4, all top-decked), Copper (gained 4).
  - T7: last 3 Talismans; pile empty, 13 VP.
  - T8–11: Travelling Fair plus Raze and Copper buys, gaining 3–4 per buy. Raze pile empty on T11, 23 VP.
  - T12: Counting House picks up 25 Coppers, $29 → 8× Travelling Fair, Province, 8 Copper buys gaining 24 Coppers.
  - Copper pile empty on T12. **Game over T12, 82 VP** (53 Copper + 10 Talisman + 10 Raze + Province + Estates).
- **Same plan, seed 2 (3/4):**
  - Talismans gone on T8.
  - T11: Counting House for $18, then a new Counting House and 2 Razes top-decked.
  - T12: $24, Raze pile empty, top-deck again.
  - T13: Counting House picks up 35 Coppers, 15× Travelling Fair, 16 Copper buys.
  - **Game over T13, 76 VP.**
- **Big Money with Haunted Woods or Horse Traders:** reference clock only, not simulated. About 4 Provinces (~27 VP) by T14–17.
- **Province engine** (Farming Village + Haunted Woods/Enchantress draw + Horse Traders): not simulated. The draw is weak, and even all 8 Provinces (48 VP) is below the rush's total.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| Talisman/Copper Tower rush | T7 (Talisman pile) | T12–13 | 40–50 on the final turn | ~75–80 (Copper + Talisman + Raze) |
| Haunted Woods / Horse Traders money | ~T9 | ~T20+ | 6 | 48 + Duchies |
| Farming Village engine | ~T11? | ~T15? | ~12 | 48 + Duchies |

**Plans considered:**
1. **Talisman/Copper Tower rush.** Builds as above, and needs about 5+ Talismans, 1–3 Counting Houses and Travelling Fair. Its weaknesses are a split of the Talisman pile and Enchantress.
2. **Big Money with Haunted Woods or Horse Traders.** First $6 around T3–5, $8 around T5–7. It can't reach 40 VP before T13.
3. **Province engine.** The draw is thin, it's slow, and its ceiling is below the rush.

**Against their best plan:** money or an engine loses outright: the rush scores ~75 VP by T13, and Enchantress or Haunted Woods costs it a turn at most. Their best reply is the **mirror**. Each Copper they gain is also a point for them once the pile empties, so it comes down to the Talisman split, who wins the race for the Copper pile, and who chooses when the game ends.

In the mirror:
- Buy Talismans before anything else.
- Buy Coppers in bulk early: each one you take is a point denied to them.
- Pick a third pile where you hold the majority: Raze, or Curse for $0.
- Whoever is ahead on the Tower count ends the game at once. Whoever is behind avoids emptying Copper and adds Provinces.

**Advocate's case** (a Province engine or money with attacks, built to stop the rush): Enchantress plus Haunted Woods plus Jester can't stop $0 gains, and Jester mostly feeds Coppers to the rusher. Against seed 1, the rush is at 13 VP by T7 and 23 by T11. A money deck at T11 has about 2–3 Provinces (12–18 VP). On T12 the rush jumps to 82 while money is still under 30. It falls behind for good on the rush's single big turn.

**Recommendation:** the **Talisman / Travelling Fair / Counting House Tower rush**. Expect to end the game on Copper + Talisman + Raze around turns 12–13 with 70+ VP. If the opponent mirrors, win the Talisman split and control the ending.

**Open:**
- **4/3:** Talisman / Silver. Enchantress instead of Silver is an option if the opponent is also going for Counting House.
- **5/2:** Talisman / Raze. Raze trashes Estates to help reach $4. Never trash a Copper with it.

**Buy priorities:**
1. Talisman whenever you have $4. With Talismans in play it gains multiple copies; empty the pile.
2. Horse Traders as early +Buy, and 1 Counting House by about T5–7.
3. Then Travelling Fair every turn, plus a Raze buy and as many Copper buys as you have Buys. Top-deck Talismans and Counting Houses; send Coppers to the discard pile.
4. Set up the finish by top-decking a fresh Counting House with Travelling Fair so the deck doesn't reshuffle. Then spend one Counting House turn emptying Copper.
5. Green only with spare $8 on the final turn (one Province).

**Ending:** three piles: Talisman, Raze (or Curse) and Copper, all on your own turns. The Province pile is irrelevant.

**Watch out for:**
1. **Enchantress on your Counting House turn.** Lead with Raze or Settlers. Leave one extra card in your deck so that absorber's +1 Card doesn't force a reshuffle.
2. **Accidental reshuffles.** Raze, Horse Traders' reaction or Haunted Woods' +3 Cards drawing from an empty deck mixes your Coppers back into it.
3. **A contested Talisman pile.** More players also means fewer Coppers in the pile and a faster game, and more attacks to absorb.

**Least sure of:** the mirror. The solo games show the rush's speed with no interference. They don't show how a 5–5 Talisman split and a shared Copper pile change the timing and who wins. To check it, play both seats of a mirror.

**Assumed:**
- Settlers/Bustling Village behaves as one split pile, empty only when all 10 are gone, so I used Raze as the third pile.
- Curse counts as a non-Victory card for Tower and as costing $4 or less for Talisman. This follows the card text; I didn't play it out.
- Counting House and Talisman are first-edition-only cards.
