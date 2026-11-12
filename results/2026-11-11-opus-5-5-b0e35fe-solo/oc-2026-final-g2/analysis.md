# Kingdom analysis: oc-2026-final-g2

**My pick: a Horse engine built on Cursed Village, Wayfarer, Livery, Mastermind and Rope.** I played every candidate out with `dominion solo`. On the same shuffle (seed 2), the engine had 6 Provinces by turn 13 and the best money-style deck had 4.

**Board:** 2 players, no Colonies or Shelters. Cards by cost: $3 Chariot Race; $4 Abundance, Rope; $5 Cursed Village, Livery, Mastermind, Artificer, Corsair; $6 Captain, Wayfarer (its cost varies). Landscapes are Road Network (a $5 Project) and Colonnade (a Landmark holding 12 VP). Non-Supply piles are Horses (30) and the Hexes that Cursed Village brings. Durations are in play. Every key card costs $5 or more, there is no $2 card, and openings are 4/3 or 5/2.

You score with Provinces, Colonnade's 12 VP (2 VP per trigger) and Chariot Race tokens. Cursed Village's Misery Hex costs −2/−4 VP. Expect the Provinces to run out.

- **Draw:** Wayfarer (+3 Cards), Horses (+2 Cards +1 Action, no Action cost) and Cursed Village's draw up to 6.
- **Village:** Cursed Village is the only one, and each one gained hands you a Hex.
- **Trashing:** Rope only, one card a turn.
- **+Buy:** Rope and Abundance.
- **Open question:** whether one village with a Hex attached can carry an engine. The solo lines say yes, because Horses and Mastermind supply the extra Actions and cards.

**Key interactions:**
- **Rope's +Buy + Wayfarer's cost:** Wayfarer costs the same as the last other card you gained this turn. Buy a Copper, and Wayfarer costs $0. I checked this in the engine. If Wayfarer's own Silver was gained first, every Wayfarer that turn costs $3. So a second Buy turns into a free draw card.
- **Mastermind + Livery:** next turn Livery is played three times. That is +$9, and every card costing $4+ you gain that turn also gives 3 Horses. In the seed-1 line this produced Province + Livery + 6 Horses on turn 10.
- **Mastermind + Wayfarer:** +9 cards at the start of your turn without spending an Action, so the whole deck gets drawn. In the seed-2 line that was a 13-card hand on turn 10 and 2 Provinces.
- **Mastermind + Horse:** I checked that all three plays still happen after the Horse returns to its pile. That's +6 Cards +3 Actions.
- **Livery + any $4+ gain:** a Horse each time. Gaining Province, Wayfarer at $6 or Livery keeps refilling your draw for free.
- **Colonnade:** you get 2 VP when you buy an Action while a copy of it is in play. Livery-into-Livery, Cursed Village-into-Cursed Village and Wayfarer-into-Wayfarer all work. With Rope, Copper plus a $0 Wayfarer with a Wayfarer in play is a free 2 VP. A Livery played by Mastermind counts as in play (checked).

**Other cards:**
- **Abundance:** best partner is buying Actions (Wayfarer or Livery). It refunds +$3 and gives +Buy, which makes double-Province turns easier. A reasonable $4 buy after Rope.
- **Artificer:** discards dead Provinces and puts a gain on top of your deck. It is also a 1-Buy way to set up a cheap Wayfarer. Decent, not needed.
- **Captain:** the only card it can play is Chariot Race. Horses aren't in the Supply, Abundance and Rope are Treasures, and Captain can't play Durations or Commands. Its high rating (3.76) doesn't apply on this board, so skip it.
- **Chariot Race:** best partner is a deck full of Provinces, because Province ($8) on top beats almost any card the opponent reveals, for +$1 +1 VP. Fine late filler, and a Colonnade target.
- **Corsair:** best partner is the opponent's Silver-heavy economy. Both plans here pay with Silver, Gold and Livery. It's rated −2.75, which is a bit harsh on this board. Consider one copy against a money opponent, as a terminal your villages can absorb.
- **Road Network:** draws you a card when the opponent gains a Victory card. Rated −2.99. Only worth a spare $5 Buy late, while the opponent is greening.

**Plans considered:**
1. **Horse engine (Cursed Village, Wayfarer, Livery, Mastermind, Rope):** draws the deck from about turn 10 and buys 2 Provinces most turns. It needs 2 Cursed Villages, 3 Wayfarers, Livery and Mastermind. Its weakness is the Hexes: Misery, Deluded and Plague all showed up in testing.
2. **Livery/Mastermind/Rope money (no village):** Livery is played most turns and Horses come free. It reached $8 on turn 8 and had 4 Provinces by turn 13. Its weakness is that it peaks at one Province per turn.
3. **Livery Big Money (floor):** after a 5/2 opening, Provinces came on turns 9 and 13, with 17 VP on turn 13.

### Build lines (from `dominion solo`)
- **Engine (seed 2, 4/3):**
  - T1–2: Rope / Silver.
  - T3: Livery. T4: Cursed Village (Fear Hex). T5: Copper + $0 Wayfarer.
  - T6: Cursed Village + Livery for $8, bought Wayfarer (+Horse). T7: Cursed Village (Misery, −2 VP). T8: Mastermind (+Horse). T9: Wayfarer, played Mastermind.
  - **T10:** Mastermind played Wayfarer 3×, then 2 Horses, 2 Cursed Villages, Wayfarer and Livery: $22 with 2 Buys, bought **2 Provinces**.
  - T11: Province. T12: Province.
  - **T13:** Mastermind played a Horse 3×, then 3 Wayfarers: $19, **2 Provinces**.
  - Result: 6 Provinces and 34 VP net after turn 13. It never used Colonnade, Abundance or Chariot Race, so there is headroom.
- **Livery/Mastermind/Rope (seed 2):**
  - T1–2: Rope / Silver. T3: Livery. T4: Mastermind. T5: Livery. T6: Gold.
  - Provinces on T8, T9, T11 and T13 (the T13 turn was Mastermind playing Livery 3× for $14).
  - Result: 25 VP after turn 13.
- **Engine, first attempt (seed 1, 5/2):** I opened Livery, wasted a Mastermind, and Deluded stopped me buying Actions one turn. Even so it had 17 VP on turn 12. Building it poorly costs about two turns.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| Horse engine | T10 | ~T13–14 | 2 Provinces (12) + Colonnade | Provinces + Colonnade + Duchies |
| Livery/Mastermind money | T8 | ~T17+ alone | 1 Province | about half the Provinces |
| Livery BM | T9 | ~T18+ | 1 Province | about half the Provinces |

**Against their best plan:**
- **Engine vs money:** money leads up to about turn 11 (19–16 on seed 2), but the engine has 4 Provinces by turn 12 against money's 4 by turn 13, then keeps taking 2 a turn. Money can't empty three piles, because the only piles that drain are Horses (not in the Supply) and Provinces. So money's only weapon is one Corsair hitting your Silvers. That's worth about one fewer Province turn, not enough.
- **Engine mirror:** the Colonnade VP and the Wayfarer/Cursed Village splits matter. Green a turn earlier than you would against money.

**Advocate's case:** the rejected plan with the highest ceiling is the engine itself, so I played it for real (step 8 above). It drew level on turn 12 and was 9 VP ahead on turn 13. The rejected money plan never leads after turn 11.

**Recommendation:** build the Horse engine. Get 2 Cursed Villages (accept the Hexes), about 3 Wayfarers (bought free via Rope + Copper, or at $3 after a Silver gain), 1–2 Liveries for payload and Horses, and Mastermind aimed at Wayfarer early and Livery later. Use Rope for +Buy and trashing Estates.

**Open:**
- **4/3:** Rope / Silver.
- **5/2:** Livery / nothing. There is no useful $2 card, and opening Cursed Village means a Hex on turn 1. Pick up Rope at the first $4.

**Buy priorities:**
- **Shuffles 1–3:** Rope, Livery, 2 Cursed Villages, Mastermind. Turn any spare Buy into a $0 Wayfarer: buy Copper first, then Wayfarer.
- **Next:** a third Wayfarer, then Abundance for Buys. Prefer gains costing $4+ while a Livery is in play, for the Horses.
- **Colonnade:** take its 2 VP whenever it's free (buy an Action you have in play).
- **Greening:** start once a turn reliably reaches $16 with 2 Buys, around turn 10. Late, take Chariot Race or a Duchy with leftover Buys.

**Ending:** the Province pile, around turns 13–15. Horses (30) aren't in the Supply, so three piles is unlikely.

**How the pick loses:** bad Hexes (Twice Miserable is −4, Plague is a Curse, Deluded stops you buying Actions that turn), a Mastermind with nothing to play, or a Corsair-heavy opponent stripping the Silver payload. The opponent can see the first two in your deck, but can't cause them.

**Watch out for:** an opponent Corsair (lean on Livery and Horses instead of Silver), Deluded turns, and Misery's VP loss in a close race.

**Least sure of:** the size of the engine's lead. It comes from one seed, with no opponent attacks and Hex luck that was average to bad. I'd test it with a second seed of both lines and a Corsair opponent.

**Assumed:** I checked these in the engine:
- Wayfarer costs $0 after a Copper gain and $3 after a Silver gain.
- Mastermind playing a Horse still gives 3 plays after it returns to its pile.
- A Livery played by Mastermind counts as in play for Colonnade.

I worked out from the card text that Captain's only legal target is Chariot Race.
