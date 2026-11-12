I played the engine line in `dominion solo` (seed 1, 4/3 opening) up to turn 13. It scored 33 VP on turn 9 and had 49 VP by turn 12. I didn't simulate the other plans: on paper, none of them comes close.

# Kingdom analysis: River Shrine, Hostelry, Change, Alchemist, Stonemason, Vineyard, Witch's Hut, Weaver, Footpad, Artificer · Exploration, Triumph, Flourishing Trade

**Board:** The board is about Triumph, made huge by two other cards:
- **Footpad's rule applies to everyone:** whenever you gain a card in your Action phase, you draw a card. That turns every gainer here into a draw card.
- **Flourishing Trade:** once it's active, cards cost $1 less and every unused Action counts as a Buy.

River Shrine is the board's only Omen (+1 Sun), so five River Shrine plays, counting both players', switch Flourishing Trade on. River Shrine is also the opening trasher.

The open question was where Triumph's Buys come from, since the Kingdom has no +Buy. Flourishing Trade answers it: Hostelry's +2 Actions become Buys. The real limit is the Estate pile. Only 8 Estates means only 8 scoring Triumphs, shared by both players.

**Key interactions:**
- **Footpad's rule + Weaver:** Weaver's "two Silvers" becomes +2 Cards. Weaver gaining a Hostelry gives +1 Card, plus one Horse (and another card) for each Treasure you discard. From turn 8 in the solo line, every turn drew deep this way.
- **Hostelry's when-gained ability, at any time:** when River Shrine gains a Hostelry at Clean-up, you can discard the Coppers you didn't use for Horses. On turn 7 that turned 3 Coppers into 3 Horses.
- **Witch's Hut or Artificer discarding Weaver:** Weaver plays itself without using an Action. Witch's Hut discarding Weaver plus another Action also gives the opponent a Curse.
- **Artificer + Footpad's rule:** Artificer gains onto your deck and Footpad's rule draws it straight away. Discarding 2 dead cards gets you a Silver in hand right now.
- **River Shrine + no-buy turns:** trash 2 cards, buy nothing, and gain a $4 card at Clean-up. Once Flourishing Trade is active, that $4 card can be a Duchy. With Exploration you also get +1 Coffers and +1 Villager, and a Villager becomes a Buy.
- **Triumph + many gains + Flourishing Trade's Buys:** this is the payload. Each Triumph scores the turn's gain count so far, plus 1 for its own Estate. Its Debt is $5, paid off before the next purchase. On turn 9: 7 gains, then Stonemason (8), then three Triumphs scored 9 + 10 + 11 = 30 VP tokens, plus 3 Estates. That's 33 VP in one turn, for $16 and 4 Buys.
- **Stonemason's overpay:** it costs $1 once Flourishing Trade is active. With $4 you get Stonemason plus 2 Weavers or Hostelries, which is 3 gains for one Buy. It's a strong way to raise the gain count before Triumph.

**Other cards:**
- **Change:** best partner is Flourishing Trade. Trashing a Duchy ($4) gains a Province ($7) for 3 Debt, and the gain draws a card. But the Debt blocks Triumph turns, so it's only a late-game tool.
- **Footpad (the card):** +2 Coffers and a hand-size attack. Its rule matters far more than the card itself. A minor buy.
- **Exploration:** pairs with River Shrine's no-buy turns, and its Villagers become Buys under Flourishing Trade. Good, but optional (I didn't test it).
- **Alchemist / Vineyard:** this deck is full of Actions (about 18), so each Vineyard would be worth 6 VP. But each one needs a Potion in play, which means one Vineyard per turn. That's far behind Triumph. At most, a late extra once the Estates are gone.
- **Ratings check:**
  - Weaver (+0.6) and Footpad (−0.4) rate as average cards, but Footpad's rule turns Weaver into draw here.
  - Flourishing Trade (−0.1) and Exploration (−1.4) also rate low, but both are central here.
  - Triumph (+2.7) and Hostelry (+2.4) agree with this view.

**Plans considered:**
- **Triumph engine (the pick):** River Shrine opening, Weaver, Hostelry, Witch's Hut and Artificer. Played out, first big turn was turn 9. It needs Flourishing Trade active, about 2 Weavers, 4–5 Hostelries and 2 Witch's Huts. Main weakness: the 8 Estates are shared with the opponent.
- **Province engine:** the same deck, buying $7 Provinces with spare Actions as Buys. It's weaker than Triumph while Estates remain (a Province is 6 VP for $7; a Triumph is 8–11 VP for $5). It's the plan once the Estates are gone.
- **Money with Witch's Hut (the floor):** about 4 Provinces (24 VP) by turn 13–15, even with $7 Provinces. The engine had 33 VP on turn 9, so this isn't close.

### Build lines
- **Triumph engine (solo, seed 1):**
  - T1: River Shrine. T2: Silver.
  - T3: River Shrine trashes 2 Estates, no buy, gains a second River Shrine.
  - T4: Weaver.
  - T5: River Shrine trashes Estate and Copper, gains Hostelry (Copper discarded for a Horse).
  - T6: River Shrine trashes 2 Coppers, gains Weaver.
  - T7: River Shrine, gains Hostelry, discarding 3 Coppers for 3 Horses.
  - T8: Horses and Hostelries draw; the 5th River Shrine play switches Flourishing Trade on. Weaver gains a Hostelry (2 Horses), the other Weaver gains 2 Silvers. Buys: Artificer and Witch's Hut with $10.
  - T9: 33 VP turn (see above).
  - T10: Stonemason overpaid for 2 Weavers, then a Triumph: +8 VP, total 41.
  - T11: stall, 1 VP.
  - T12: Weaver gains Hostelry (2 Horses), then a Triumph: 49 VP.
  - The stalls came once the Horses were used up and the deck had only one Witch's Hut. A second Witch's Hut would fix that.
  - The idle opponent played no River Shrines. A real one would switch Flourishing Trade on sooner.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| Triumph engine | T9 | ~T13–15 (piles) | 30+ | 8 Triumphs (~80) + Provinces and Duchies |
| Money with Witch's Hut | T6–7 | T15+ | 6 | half the Provinces |
| Vineyard on the side | T10+ | — | ~6 | 8 Vineyards × ~6 |

**Against their best plan:** In the mirror, the race is for the 8 Estates. Whoever runs the first big Triumph turn takes three of them, and with them about 30 VP. If the opponent plays money, the engine wins easily. Their Witch's Hut Curses are weak against a deck that draws this much, and River Shrine can trash them.

**Advocate's case:** I argued for Vineyard, the highest-ceiling plan I rejected:
- It would use Alchemist as draw and add 8 Vineyards to an Action-heavy deck, for about 48 VP. Each Vineyard bought also counts as a gain for Triumph.
- It falls behind straight away. Each Vineyard needs a Potion in play, so it's one per turn (about 6 VP). The Triumph engine scored 30 VP on turn 9, and Potion and Alchemist slow the build down.
- What survives: once Estates run out, a lone Potion for late Vineyards is a reasonable extra.

**Recommendation:** Build the Triumph engine. Thin and switch on Flourishing Trade with River Shrine, build with Weaver, Hostelry and Footpad's free draws, then spend spare Actions as Buys on Triumph turns.

**Open:**
- **4/3 (choose this, since you can arrange your deck):** River Shrine / Silver.
- **5/2:** River Shrine and nothing. A $5 Footpad is the alternative. Stonemason is bad at $2: before Flourishing Trade, trashing an Estate gains only Coppers or Curses.

**Buy priorities:**
1. Shrine turns early: trash, buy nothing, gain River Shrine, Weaver or Hostelry. Use Hostelry's when-gained ability to turn leftover Coppers into Horses.
2. Weaver ×2–4, Hostelry ×4–5, then Artificer and Witch's Hut ×2 once Flourishing Trade is active. Exploration if you have a spare $4 early.
3. Start Triumph turns as soon as one turn has 5+ gains and $10 or more. Don't wait.
4. Late: Stonemason overpaid before each Triumph to raise the gain count.

**Ending:** Estates (only 8) run out first. After that, Triumph does nothing and the deck switches to $7 Provinces and Duchies (gained by Weaver, River Shrine or Artificer). Hostelry and Weaver are the next piles to run out, so a three-pile ending around turns 13–16 is likely.

**Watch out for:**
- **Estate denial:** taking Estates by buying them at $1 or gaining them with Weaver also starves the opponent's Triumph.
- **Gains in the Action phase draw for everyone:** a Curse given during your Action phase draws the opponent a card.
- **Debt from Change blocks Buys:** don't take Debt on a Triumph turn.

**Least sure of:** Mirror timing.
- Whether to rush a smaller Triumph turn (5–6 gains) to grab Estates first, or build for one bigger turn. The test is a two-player game.
- How much Exploration adds; I didn't play it.

**How the pick loses:** An opponent who builds faster takes 4 or more Estates in Triumph turns first. Or they three-pile you on Estates, Hostelry and Weaver while ahead.

**Assumed:**
- "Action plays as Buys" means unused Actions can be spent as Buys. That's how `dominion solo` ran it.
- Footpad's rule applies even if nobody buys Footpad, and it draws for any player who gains in their own Action phase.
- Projects and Debt costs are not reduced by Flourishing Trade (the simulator showed Exploration still at $4).
- The opponent's River Shrine plays count toward the 5 Sun.
