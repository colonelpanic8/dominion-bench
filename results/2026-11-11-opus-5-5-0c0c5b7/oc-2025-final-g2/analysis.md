# Kingdom analysis: oc-2025-final-g2

**Board:** Nothing here draws more cards within a turn. Farmhands and Peddler only replace themselves. What grows your hand is the *next* turn: Grotto (park up to 4 dead cards now, draw that many at the start of next turn), Enchantress (+2 Cards next turn) and Way of the Squirrel (+2 Cards at end of turn). That gives 7–9 card hands. The main payload is Peddler. It costs $8 but only in your Buy phase it gets cheaper, and Durations from last turn (Grotto, Amulet, Enchantress) still count as Actions in play. Outside the Buy phase a Peddler costs $8, so **Remodel turns it into a Province**. +Buy comes only from Loot (via Foray) and Fortune, so how many cards you can gain each turn is the open question.

**Key interactions:**
- **Peddler + Durations / Farmhands → Remodel:** with 2–4 Actions in play, Peddler costs $4–$0 to buy. Remodel trashes it as an $8 card and gains a Province. From about turn 10: one Province per Remodel play, plus whatever you buy.
- **Grotto / Enchantress / Squirrel → hand size:** each Grotto turns this turn's Estates and spare cards into up to +4 cards next turn. Farmhands gives a spare Action, so a terminal you can't use (spare Remodel, Gladiator, Transmute) can be played as Squirrel for +2 Cards. Typical next hand: 7–9 cards.
- **Foray + big hands → Loot:** for $3 and a Buy, discard 3 differently named unplayed cards and gain a $7 Treasure, usually +$3 and +1 Buy. In a 5-card hand that is hard. In an 8-card hand with Estate, Copper and a spare Action it is easy. Loot is the main source of +Buy for free Peddlers, and Hammer can gain a Peddler directly in the Buy phase.
- **Monastery + gains:** each gain (Amulet's Silver, Peddlers, Loot, Doubloons' Gold, Fortune's Golds) lets you trash a card from hand or a Copper you've already played. Thinning costs no Action and no money that turn.
- **Gladiators → Fortune:** Fortune is the board's highest ceiling. Played after $12, it makes $24 with a Buy, which is three Provinces when Loot adds Buys. But first the Gladiator pile has to be drained, then you need $8 plus 8 Debt.

**Other cards:**
- **Enchantress:** best partner is Farmhands (spare Action), and it doubles as next-turn draw. Every opener here is a non-village Action, so its attack wipes out the opponent's Amulet, Remodel or Grotto on turns 3–5. Later they dodge it by leading with Peddler or Farmhands.
- **Farmhands:** the village. When gained, it can set aside a stuck terminal or a spare Copper to play next turn.
- **Amulet:** trashes Estates early, gains Silvers that also count as gains for Monastery, and counts toward the Peddler discount on two turns.
- **Guardian:** blocks Enchantress and Sword, and is a cheap gain for Monastery. A $2 filler if the opponent plays Enchantress every turn.
- **Gladiator:** a terminal +$3 that you need only for the Fortune route.
- **Transmute:** best partner is Peddler (Peddler → Duchy), but Remodel does the same job better (Peddler → Province). Skip it.
- **Ratings check:** Glicko agrees on Grotto (3.41) and on skipping Transmute (−6.84). I rate several cards above their ratings because of this board:
  - Foray (−1.52): bigger hands make the 3-name condition easy.
  - Monastery (−0.91): there are lots of gains to feed it.
  - Remodel (−0.09): it turns Peddler into a Province.
  - Peddler (1.52): Durations keep it cheap.

### Build lines
- **Peddler/Remodel engine** (going first, 4/3), average draws:
  - T1 Remodel. T2 Amulet.
  - T3: Amulet trashes an Estate. Buy Enchantress.
  - T4: Amulet gains a Silver. Remodel an Estate into Farmhands and set aside a Copper. Buy Grotto with $2.
  - T5: the set-aside Copper, Farmhands and Enchantress make $6. Buy Gold, which can later be Remodeled into a Province.
  - T6: Enchantress gives a 7-card hand. Grotto parks Estate and Remodel. Amulet trashes a Copper. Grotto, Amulet and Enchantress are 3 Actions in play, so Peddler costs $2: buy it.
  - T7–9: add Peddlers at $0–2, a second Farmhands and Grotto, and Foray for Loot once hands reach 7 or more cards. Add one Monastery on a $2 hand.
  - Built turn (about T10–11):
    - In play: 2 Farmhands, 3 Peddlers, Remodel, Gold, Silver, Loot, 2 Copper.
    - Remodel a Peddler into a Province.
    - The rest makes $3 + 3 + 2 + 3 + 2 = $13 with 2 Buys: Province plus a free Peddler, or Province plus Foray.
    - That is **about 2 Provinces per turn**.
- **Enchantress/Gladiator money + Foray:** open Enchantress/Silver. First $6 around T4–5, first $8 around T6–8. Enchantress is played about 1 turn in 3, or 1 in 2 with two copies. 4 Provinces around T15–16, and no +Buy beyond Loot.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| Peddler/Remodel engine | ~T10 | ~T14–15 | 2 Provinces | Provinces + Duchies |
| Engine + Fortune | ~T11 | ~T13–14 | 3 Provinces | same, but sooner |
| Enchantress-BM + Foray | ~T8 | ~T20+ | 1 Province, every other turn | ~half the Provinces |

**Plans considered:**
1. **Peddler/Remodel engine:** Grotto, Enchantress and Squirrel for hand size, Amulet and Monastery to thin, Farmhands for Actions. Needs 3–4 Peddlers, 1–2 Remodels and +Buy from Loot by about T10. Weakness: no draw within the turn, so a bad Grotto turn stalls it.
2. **Engine + one Fortune:** the same deck plus 2 Gladiators early as economy, then Fortune when you have $8 spare. Higher ceiling, but needs the Gladiator pile drained and costs a turn paying off Debt.
3. **Enchantress-BM:** the floor. Too slow against plan 1.

**Against their best plan:** in the engine mirror, Enchantress decides the early turns. Turns 3–5 matter most, so going first, open with it, or buy it on turn 3. Later both players lead with cantrips and its attack fades. Peddlers (10) could become a contested pile, so buy them early while they're cheap. Against money, the engine is ahead by about T12 and scores twice as fast.

**Advocate's case (Fortune route):**
- T3–4: 2 Gladiators. Reveal a card the opponent is unlikely to hold, so most plays are unmatched.
- About T8: the Gladiator pile is drained (2 bought plus 3 unmatched plays).
- T9–10: Fortune for $8 + 8D. With Farmhands, play both Gladiators that turn to gain 2 Golds.
- T11: pay off the Debt (a weak turn).
- T12+: $12–15 doubled is $24–30 with 2–3 Buys, which is 3 Provinces.

It falls behind plan 1 on T10–11, losing about 2 Provinces' worth while it buys Fortune and pays off the Debt. It catches up by about T13. That is close, and it depends on the opponent not matching Gladiators. So I treat Fortune as an add-on once the engine runs, not the core plan.

**Recommendation:** the Peddler/Remodel engine. Add Fortune in the midgame only if the Gladiator pile is already low, for example because the opponent bought Gladiators.

**Open:**
- **4/3:** Remodel/Amulet. Going first, Enchantress/Amulet is a strong alternative.
- **5/2:** Remodel/Grotto. Alternative: Farmhands with $5, setting aside the fifth Copper, which gives $3 on T2 for Amulet.

**Buy priorities:**
- Shuffles 1–2: Enchantress, Grotto, Farmhands, Monastery on a $2 hand, Remodel an Estate into Farmhands.
- Then: Peddlers whenever they cost $4 or less, Foray whenever you hold 3 dead cards with different names, a second Grotto and Remodel, one Gold.
- Green around T10: Remodel Peddlers (and Golds) into Provinces, and buy Provinces and Duchies with the rest.

**Ending:** most likely the Provinces run out around T14–16. A three-pile ending is possible if both players drain Peddler, Farmhands and Grotto. Remodeling a Province into a Province can speed up the ending when you're ahead.

**How the pick loses:** an opponent who plays Enchantress on most turns, combined with Grotto turns that miss, leaves hands of 5 dead cards. Answer: lead with Peddler or Farmhands, keep a Guardian, and keep 2 Grottos so one fires each turn. With more players, Enchantress and Guardian get stronger and Provinces rise to 12, which favours the engine further.

**Watch out for:**
- Opponent Enchantress on T3–4 hitting your opener.
- Peddler pile pressure.
- Over-trashing Coppers before you have Loot or Peddler income.

**Least sure of:** how fast Peddlers and Loot come in while you have only one Buy before turn 8. If Foray rarely triggers, the engine slips to 1.5 Provinces per turn. The test is the T6–9 line above: whether it really has 3+ Actions in play on most turns.

**Assumed:**
- Way of the Squirrel draws after the Clean-up draw, so the next hand is 7 cards.
- Durations with effects still to come (Grotto, Amulet, Enchantress) stay in play and count toward Peddler's discount.
- Remodel and Transmute see Peddler at $8, because they act outside the Buy phase.
- Remodel can't gain Fortune, because of its Debt cost.
- Hammer gains during the Buy phase, so it gets the Peddler discount.
