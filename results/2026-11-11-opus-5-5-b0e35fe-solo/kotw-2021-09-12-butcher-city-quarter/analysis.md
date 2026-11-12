I played five solo lines (four on seed 1, one on seed 2), so I'm stopping the tests there and writing up.

# Kingdom analysis: Butcher / City Quarter / Embassy / Faithful Hound / Fool's Gold / Merchant Guild / Night Watchman / Nomad Camp / Pooka / Tunnel, with Ritual and Tower

**Board:** No attacks and no +Cards village. The only village is City Quarter, which costs 8 Debt and draws only when your hand already holds Actions. The draw cards (Embassy, Pooka, Faithful Hound) are all terminal. Each player starts with Cursed Gold in place of one Copper, so both decks curse themselves every shuffle. Tower changes what that costs: once the Curse pile is empty, each Curse you own scores −1 +1 = 0. Tower also gives 1 VP per Fool's Gold you own if the Fool's Gold pile empties. So the board is about a Fool's Gold economy, Butcher turning cards into better cards, and the Curse pile running out.

The open question was whether City Quarter plus Butcher plus Tunnel Golds could make an engine that beats money. In play it only drew level, a turn later and with more variance.

**Setup:** The starting deck is Cursed Gold, 6 Copper and 3 Estates, worth $9 in total. Turns 1–2 split 6/3 (48%), 5/4 (40%) or 7/2 (12%). There is no 4/3. Price points are crowded at $5 (Butcher, Embassy, Merchant Guild, Pooka). City Quarter costs $0 plus 8 Debt.

**Key interactions:**
- **Fool's Gold stacking:** the first Fool's Gold played in a turn gives $1 and every later one gives $4. With 6–8 in the deck, hands of $12–14 were common from turn 8. Each Fool's Gold also scores 1 VP if the pile empties.
- **Butcher spends its own Coffers:** it gives +2 Coffers, and each Coffer spent lets the gained card cost $1 more than the trashed one. So it never costs you anything to use:
  - Cursed Gold → Gold: same $3, but no more self-cursing.
  - Curse → Fool's Gold.
  - Estate → Nomad Camp, which goes on top of your deck.
  - Gold → Province, late in the game.
- **Tunnel plus a discard outlet:** Night Watchman (night, no Action needed) or Embassy discards Tunnels for Golds. It works, but it is slower than Fool's Gold (lines g and a).
- **Ritual plus Tower:** Ritual gives VP equal to the cost of the card it trashes. Keeping a Gold unplayed in hand and Rituals it for 6 VP beats a Duchy. Rituals stop when the Curse pile is empty, and both players' Cursed Golds drain the 10 Curses by about turns 12–15. Once it is empty, Tower makes every Curse worth 0.
- **Faithful Hound plus Night Watchman or Embassy:** a discarded Hound goes back to your hand at end of turn, so the next turn starts with 6 cards.

**Other cards:**
- **City Quarter:** best with Butcher and Hounds in hand. It gave +3 Cards on a good turn, but it is dead when drawn without Actions.
- **Pooka:** pairs with Copper. As an engine opener with Night Watchman it was too slow (line e had 0 VP on turn 9).
- **Merchant Guild:** pairs with $0 buys (Copper, Curse, and Ritual's Curse gain) to make Coffers for Butcher. Not tested, and its +Buy is weaker than Nomad Camp's.
- **Embassy:** pairs with Tunnel. Each one you gain gives the opponent a Silver.
- **Nomad Camp:** the best +Buy here. Fool's Gold hands often reached $13–14 with only one Buy.
- **Ratings check:** Butcher (3.7) and City Quarter (3.7) are rated highest. The gap is City Quarter: on this board it lacks the dense Action deck and non-terminal draw it needs, so it plays far below its rating. Fool's Gold (−1.6) plays above its rating, because Tower pays for its pile emptying and both players stack it.

### Build lines (`dominion solo`, opponent idle)

| Line | What it did |
| --- | --- |
| **h: Fool's Gold + Butcher + Nomad Camp** (pick) | Opened Butcher/Fool's Gold, then bought Fool's Gold ×3. T5 Butcher Curse→Fool's Gold. T7 Gold. Provinces on T8, T10, T11 (Butcher Estate→Nomad Camp the same turn) and T13. **4 Provinces by T13, 24 VP** (2 Curses, 8 Fool's Gold). |
| **f: Fool's Gold + Embassy money** | Embassy/Fool's Gold, Golds on T5–6, Provinces on T8, T9, T13 and T14. 4 Provinces by T14, 22 VP with 5 Curses (27 VP once the Curse pile empties). |
| **g: City Quarter + Butcher + Embassy + Tunnel** | Butcher/Night Watchman, then 2 City Quarters (T4, T7), Nomad Camp, Embassy, a second Butcher and Tunnels. No VP until T12. T12 was the big turn: City Quarter ×2 → Embassy → Tunnel Gold, Butcher Gold→Province, plus $9 for a second Province. 3 Provinces by T14, 23 VP. |
| **e: Pooka + Night Watchman + City Quarter** (seed 2) | Clogged by Curses, 0 VP on T9. Abandoned. |
| **a: Butcher + Tunnel + Night Watchman** (no plan for the Curses) | 2 Provinces by T10, 18 VP on T15. |

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| Fool's Gold + Butcher + Nomad Camp | T8 | ~T16–17 (Provinces) or a three-pile | Province (+Province with Butcher) | Provinces + Fool's Gold via Tower + Ritual |
| City Quarter engine | T12 | ~T16+ | 2 Provinces (once) | Same, but it doesn't keep up |
| Fool's Gold + Embassy | T8 | ~T17 | Province | Provinces |

**Plans considered:**
1. **Fool's Gold + Butcher + Nomad Camp** (pick). Needs a big share of the Fool's Gold pile (about 6+ copies), one Butcher and 1–2 Nomad Camps. Weakness: one Buy per turn wastes big hands, and the opponent will want the same pile.
2. **City Quarter / Butcher / Tunnel engine.** It is the highest-ceiling plan, but its first big turn came on turn 12 and it couldn't repeat it. City Quarter is dead without Actions in hand, and every drawer is terminal.
3. **Fool's Gold + Embassy** is the floor. It is about one Province behind plan 1 and gives the opponent Silvers.

**Recommendation: a Fool's Gold money deck with Butcher and Nomad Camp, finishing with Ritual.**
- Against a mirror, the Fool's Gold split decides it. Each copy is worth $4 in hand and 1 VP if the pile empties.
- Fool's Gold's Reaction helps you in a mirror: when the opponent gains a Province you can trash a Fool's Gold to put a Gold on your deck, which Butcher can later turn into a Province.
- Against the City Quarter engine, you are about two Provinces ahead when it first comes online around turn 12.

**Open:**
- **6/3:** Butcher / Fool's Gold.
- **5/4:** Butcher / Nomad Camp. Fool's Gold is also fine.
- **7/2:** Butcher / Fool's Gold.

**Buy priorities:**
1. Province at $8.
2. Gold at $6–7 in the first two shuffles; it is also Butcher fodder.
3. Fool's Gold at $2–4. Keep buying until you have about 7 or the pile is gone.
4. 1–2 Nomad Camps at $4.
5. A second Butcher or one Embassy at $5 is optional.

Butcher, in order of use: Cursed Gold or a Curse early, then Estates, then Gold→Province late. Green at $8 from about turn 8. At about 4 Provinces left, take Duchy at $5–7. If a hand can pay $4 without the Gold in it, Ritual the Gold for 6 VP instead of a Duchy. Ritual a $5 Action at the very end for 5 VP. Use Tunnel as a $3 green (2 VP).

**Ending:** The Curses will empty (both players' Cursed Golds plus any Rituals). The Fool's Gold pile probably empties in a mirror. Those two plus Tunnels or Hounds would make a three-pile ending. Otherwise Provinces run out around turns 16–18. Track the Curse pile: if it isn't empty at game end, Curses count −1.

**Against their best plan:** In the mirror, the Fool's Gold split and Nomad Camp's +Buy decide it. If they build the City Quarter engine, race them: you are 1–2 Provinces ahead at turn 12, and you can end on piles.

**Advocate's case (engine):** City Quarters and Butchers line each other up, Night Watchman sets up the hand, Tunnel/Embassy makes Golds, and Butcher converts them. Its fastest line (g) falls behind on turn 8, when plan 1 takes its first Province. By turn 11 it is 3 Provinces behind. It closes to 1 Province behind by turn 14, but only after one good turn. It would need repeated 2-Province turns from turn 12, and in my line its next turn bought 1 Province.

**How the pick loses:** The opponent wins the Fool's Gold split and adds +Buy first. Or the Curse pile stalls short of empty because both players stop playing Cursed Gold or trash it, and then my Curses count −1 each.

**Watch out for:**
- Losing the Fool's Gold split. If you get fewer than about 5, lean on Gold, Butcher and Tunnel.
- Curse-pile timing for Ritual and Tower.
- A three-pile ending when you are behind.

**Least sure of:** whether a better-built City Quarter engine (more Hounds, a Merchant Guild Coffers line) can reach 2 Provinces every turn from turn 11. I tested only one seed of each plan, and the engine and the pick were within one Province at turn 14. The test is a second seed of line g against line h.

**Assumed:**
- Solo lines have no opponent: no Fool's Gold contention, no Embassy Silvers received, and no Curses given by them.
- Curses count as non-Victory cards for Tower.
- Ritual does nothing once the Curse pile is empty.
- Faithful Hound's return happens after the Clean-up draw, giving a 6-card hand. The engine handled it this way.
