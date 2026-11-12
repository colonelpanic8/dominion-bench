## Kingdom analysis: Villa, Band of Misfits, Junk Dealer, Lost City, Vault, Lighthouse, Sentinel, Caravan, Harbor Village, Tools (Innovation, Borrow)

**Recommendation:** play a trimmed money deck. Open Silver/Sentinel, buy one or two Lost Cities as extra draw, then Gold and Provinces. In solo test games this beat my Villa engine line clearly: 4 Provinces by turn 13 and 5 by turn 14, against a first Province on turn 11 for the engine.

**Inventory:** 2 players, no Colonies, no Shelters, normal 7 Copper / 3 Estate deck, so the opening is 4/3 or 5/2.
- $2: Lighthouse (Duration).
- $3: Sentinel.
- $4: Villa, Caravan (Duration), Harbor Village, Tools (Treasure).
- $5: Band of Misfits, Junk Dealer, Lost City, Vault. This price is crowded.
- Landscapes: Innovation (Project, $6) and Borrow (Event, $0).
- Nothing on the board adds non-Supply piles. There are no attacks or junkers. Lighthouse's protection does nothing here.

**Board:** you score with Provinces and Duchies only. Nothing gives VP tokens or alternative VP, and the game ends on Provinces. There are lots of +Actions (Villa, Lost City, Harbor Village) and +Buy (Villa, Borrow), but almost no draw:
- Lost City nets +1 card.
- Vault nets +1 card and is terminal.
- Caravan nets +1 card, on your next turn.
- Each Villa you play nets −1 card.

The deck can't draw itself, so this is not an engine board. Sentinel gives quick trashing, which makes a thin money deck strong.

**Key interactions:**
- **Villa bought in the Buy phase:** Villa goes to your hand and you go back to your Action phase. The simulator confirmed that you can play Treasures again afterwards. So a bought Villa costs a net $3 and gives +Buy, and late in the game it turns $12–13 into Province + Duchy.
- **Tools copies anything in play.** With a Gold played first, Tools gains a Gold every time you play it. With a Villa in play, it gains a Villa to your hand, which gives +$1 and +Buy and sends you back to your Action phase. Tools can also copy itself.
- **Borrow is +$1 for the cost of a card in your next hand.** It's only worth it when the $1 reaches a price point: $3→Sentinel, $4→Villa, $7→Province. In my first engine line, using it nearly every turn kept hands at 4 cards and slowed the deck down.
- **Sentinel thins fast.** Trash Estates and some Coppers, then stack the next hand. Gold + Silver + Silver on top set up the Provinces on turns 8 and 11.
- **Lost City gives the opponent a card** each time you gain one. It's symmetric in a mirror, but it's a small tax on buying many.

**Other cards:**
- **Lighthouse:** non-terminal $1 now and $1 next turn. A good $2 buy, and its attack protection is irrelevant.
- **Junk Dealer:** cantrip trasher. A second trasher if your split is 5/2.
- **Harbor Village:** only adds anything next to Villa, Junk Dealer or Lighthouse (+$1). Weak.
- **Caravan:** a mild lab-like card. Acceptable at $4 if there's nothing else.
- **Vault:** +2 cards, and Villa's Actions fix it being terminal. Too weak to build around, and it lets the opponent sift.
- **Band of Misfits:** in practice a $5 Villa without Villa's on-gain bonus, or a second Sentinel. Skip it.
- **Innovation:** plays a gained Lost City or Vault once per turn. A money deck gains too few Actions for it. Skip it.

**Plans considered:**
1. **Trimmed money with Lost City (pick):** Silver/Sentinel, Lost City at $5, Gold at $6–7, Province at $8, Lighthouse at $2. The solo line had $6+ on turn 6, the first Province on turn 8, and 5 Provinces by turn 14.
2. **Villa / Lost City / Borrow engine:** many Villas, Lost Cities and Junk Dealer, with Borrow as the +Buy. The solo line had 0 VP through turn 10, its first Province on turn 11, and no multi-Province turns in sight. It's limited by the draw, not by Actions.
3. **Money with Tools:** Tools copies a played Gold. It's plausible as a later addition to plan 1 but untested.

### Build lines (from `dominion solo`, seed 1, no interference)
- **Money (pick):**
  - T1–2: Silver / Sentinel.
  - T3: Sentinel trashes Estate and Copper; buy Silver.
  - T4: Lost City.
  - T5: Sentinel trashes 2 Coppers; buy Lighthouse.
  - T6: Gold.
  - T7: Silver.
  - T8: Sentinel trashes 2 Estates; buy **Province**.
  - T9: Gold.
  - T10–11: **Province, Province**.
  - T12: Gold.
  - T13–14: **Province, Province**, giving 30 VP on turn 14 from a 17-card deck.
- **Engine (rejected):**
  - T1–3: Silver, Sentinel, then Villa via Borrow.
  - T4–8: Lost City, Junk Dealer, Villa, Lost City, Lost City, using Borrow almost every turn.
  - T9: three Villas, with treasures played after the Villa return; $1 left over.
  - T10: Gold.
  - T11: the first **Province** (6 VP), against 18 VP for the money line by then.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| Money + Lost City | T8 | ~T16–17 (alone) | 1 Province, Province + Duchy with Villa or Borrow | half the Provinces plus Duchies |
| Villa engine | T11 | later than T18 | about Province + small | same |

**Against their best plan:** in a money mirror, the plan with the faster first Gold and Province wins. That makes the Sentinel opening and Sentinel's deck-stacking decisive, and the Villa/Borrow double buys decide the Duchy dance at the end. An engine opponent falls behind by about two Provinces by turn 11 and can't catch up, because it has no multi-Province turn.

**Advocate's case (engine):** Villa has the second-highest rating on the board (5.77), and returning to the Action phase gives unlimited Actions and Buys. Even its best version still needs net draw. Each Lost City gives only +1, so drawing a 15-card deck would take about 10 of them. Vault and Caravan add at most +1 each. The engine falls behind on turn 8, when money takes its first Province, and is 3 Provinces down by turn 11. The pick stands.

**Open:**
- **4/3:** Silver / Sentinel.
- **5/2:** Lost City, then on turn 2 use Borrow to reach $3 for Sentinel. That costs a 4-card turn 3. Junk Dealer / Lighthouse is the fallback.

**Buy priorities:**
- Province at $8, or at $7 with Borrow once the deck has 2 Golds.
- Gold at $6–7.
- Lost City at $5 (one or two copies), then Silver or Lighthouse.
- Sentinel stays your only trasher. Trash Estates first, and keep about 3 Coppers.
- Add one Villa around turn 10+ for +Buy.
- Duchy at $5–7 once 4 Provinces are left, and Province + Duchy at $13 with Villa or Borrow.

**Ending:** the Provinces run out around turns 15–17 in a mirror. No pile is a realistic three-pile threat.

**Watch out for:**
- Overusing Borrow: only spend it to reach a price point.
- An opponent's Lost City gains give you cards, and yours give them cards.
- With 3+ players, Lost City's gift is spread across more opponents, but the plan stays the same.

**How the pick loses:** to a better-optimised money mirror, for example faster Golds through Tools, or luckier Sentinel stacks. An opponent can't see this from your opening, because both sides open the same way.

**Least sure of:** whether Tools, copying a played Gold, beats Silver or Lighthouse at $4 in this money deck. I didn't play a Tools line. One seeded game with Tools from turn 5 on would settle it.

**Assumed:**
- **Rules readings, taken from the simulator:** you can play Treasures again after Villa sends you back to the Action phase, and Borrow's +1 Buy only replaces the Buy it uses.
- **Single seed:** each line was played once, on seed 1, with no opponent. The gap between the plans is about three Provinces by turn 11, which is too big for the shuffle to explain, but the exact turns may move by one.
- **Weak engine play:** my engine line probably over-bought Villa and overused Borrow. The verdict rests on the draw count above, not on that line.
