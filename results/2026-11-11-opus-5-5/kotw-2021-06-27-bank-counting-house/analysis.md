# Bank / Counting House kingdom (KotW 2021-06-27): full analysis

**First-edition-only cards on this board:** Counting House, Talisman, Farming Village and Horse Traders. All card text below is from the kingdom file.

**Inventory:**
- **$2:** Raze, Settlers/Bustling Village (a split pile with Bustling Village at $5), and the Event Travelling Fair.
- **$3:** Enchantress.
- **$4:** Farming Village, Horse Traders, Talisman.
- **$5:** Counting House, Haunted Woods, Jester.
- **$7:** Bank.
- **Landmark:** Tower.

There are no Colonies or Shelters, so the starting deck is 7 Copper and 3 Estate and the opening split is 4/3 or 5/2. The $5 slot is crowded and $6 is empty. The Copper pile has 46 cards in a 2-player game.

**Board:** Copper is the payload here. Counting House returns every Copper in your discard pile to your hand, Bank pays $1 more for every one of them, Talisman doubles each Copper you buy, and Travelling Fair supplies +Buys. Travelling Fair also lets you put cards gained that turn on top of your deck, so the next hand always holds a Counting House. Tower gives 1 VP for each card you own from any non-Victory pile that empties, which can include Counting House, Bank or Copper.

The open questions were how Counting House copes early, when your discard pile is small, and how to stop a reshuffle from moving the Coppers out of the discard pile. Travelling Fair answers both.

**Key interactions:**
- **Counting House + Travelling Fair (the lock).** This combo is listed in `combos.md`. Each turn you buy Travelling Fair, buy a new Counting House and put it on your deck, and optionally put some Coppers on top too.
  - Next turn, Counting House takes back every Copper you played this turn, because they all went to your discard pile.
  - Because each turn draws only from what you put on top, you never reshuffle, and the Coppers stay in your discard pile.
  - Keeping it going costs $7 a turn (Travelling Fair $2 + Counting House $5). It needs only one Action, so no village is required.
  - With N Coppers you make about $N+3 a turn. At about 15 Coppers that is $18: the lock plus one Province.
- **+ Bank.** Buy a Bank ($7) and put it on your deck as well. It then pays about N+3 on top of that, so each turn makes about $2N+6.
  - With N = 15 that is about $36. After paying the $14 to keep the lock going, you have about $22 left: two Provinces and spare $.
  - The game ends after roughly 3–4 of these turns.
- **Talisman + Copper or Travelling Fair.** Each $0 Copper you buy brings a second copy with each Talisman in play. Two extra Buys from Travelling Fair plus one Talisman add 4 Coppers for $2.
  - Talisman also copies Settlers, Raze and Talisman itself, since each costs $4 or less.
- **Tower + empty piles.** The lock uses roughly one Counting House a turn, so the Counting House pile (10 cards) is likely to empty: about +8 VP. An empty Bank or Copper pile adds more.
  - Each empty pile also brings a three-pile ending closer, and you are the player it favours.

**Other cards:**
- **Raze:** good with the Estates. It is a non-terminal way to trash them and the only junk this deck has. It also takes the hit from an opponent's Enchantress.
- **Settlers:** a cantrip that also gives back a Copper, about +$1, before the lock starts. Like Raze, it can take the Enchantress hit, and it costs $2.
- **Bustling Village:** none. You don't need Actions.
- **Farming Village:** a weak fit with Counting House, because it stops at the first Copper instead of discarding it. You only need it if you add Jester or Haunted Woods.
- **Horse Traders:** +Buy for Talisman's Copper doubling early on. It is terminal and collides with Counting House. It is a reasonable piece of a money deck.
- **Jester:** in a money deck it gives you copies of the opponent's Silver and Gold and Curses on their Victory cards. Against the lock it discards the top card of the deck, so put a Copper on top as a decoy.
- **Enchantress:** this is the real threat to the lock. The first Action you play becomes +1 Card +1 Action, which wastes the Counting House. Counter it by putting a Settlers or Raze on your deck and playing it first.
- **Haunted Woods:** a decent money attack. Against the lock it is nearly harmless, because your hand is empty by the time you buy.

**Ratings check:** Counting House (−3.1, deprecated), Bank (−1.6) and Talisman (−1.5) all rate low because on most boards they are weak. This board is the exception: it supplies both the Copper discard pile and the topdeck that those cards need.

### Build lines
- **Counting House lock (4/3):**
  - T1 Talisman. T2 Silver.
  - T3 $5: Counting House. T4 $4: Talisman, with Talisman in play, so you gain 2.
  - T5–T6 at about $4 each: Travelling Fair, then Settlers or Raze plus Copper. Talisman doubles both, about +4 Coppers in total.
  - T7: Counting House turn with about 5 Coppers in your discard pile, about $8: Bank.
  - T8 $5: second Counting House. T9: Travelling Fair plus Copper buys.
  - T10: Counting House with about 6 Coppers in your discard pile, about $10. Start the lock: Travelling Fair ×2, Counting House and a Copper, all put on your deck.
  - T11: Counting House takes back about 12 Coppers, about $15: lock plus the first Province.
  - T12: about $18: lock plus a Province plus Coppers.
  - T13 on, once a Bank is in the hand: about $30+, two Provinces a turn.
  - Built turn: Counting House, 4 cards you put on top and about 18 Coppers, with Bank, gives about $40 and 4–5 Buys, which is 2 Provinces plus the lock.
- **Jester/Haunted Woods money (baseline):**
  - Open Silver/Silver, or Silver/Horse Traders.
  - Buy Jester at $5, then Haunted Woods, then Gold. A Province turn and an attack play about every other turn.
  - First Province about T10. 4 Provinces by about T15–16.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| Counting House lock | ~T11 | ~T15–16 | 2 Provinces | Provinces + about 8–10 Tower VP |
| Jester/Haunted Woods money | ~T10 | ~T20 | 1 Province | about half the Provinces + Duchies |
| Talisman money | ~T11 | ~T20 | 1 Province | Provinces |

**Plans considered:**
- **Counting House lock (above).**
  - Needs: about 12–15 Coppers, Travelling Fair every turn, and about 6–8 Counting Houses out of 10.
  - Weakness: a slow and swingy setup (T7–T10), and Enchantress.
- **Jester or Haunted Woods money.**
  - Reliable, but its ceiling is 1 Province a turn.
  - It loses the race once the lock starts producing two Provinces a turn.
- **Talisman/Silver money with Travelling Fair.**
  - Talisman copies Silver (2 Silvers per buy).
  - Weaker than Jester money.

**Against their best plan:**
- **Against money:** the money player takes about 3 Provinces by T13. The lock takes 2 a turn from T13–14 and adds Tower VP, so it wins unless it stalls badly.
- **Against Enchantress money:** the lock costs $2 a turn more for the Settlers or Raze decoy. It still wins.
- **Mirror:** the Counting House pile is shared, and whoever starts the lock first gets most of it and most of the Tower VP. Get your second Counting House early.

**Challenged:**
- **The rejected money plan, retried:** at its best (two Jesters and Gold), it still only reaches 4 Provinces by about T15. That is behind the lock unless the lock first starts after T13.
- **How the lock loses:**
  - The reshuffle comes before the first lock turn, so the Coppers go back into your deck.
  - The opponent plays Enchantress when you have no decoy.
  - The opponent mirrors you and takes half the Counting House pile.

**Recommendation:** go for the Counting House and Travelling Fair lock, with Talisman for Coppers and Bank as the payoff. It needs only one Action, the opponent's attacks have counters, and it scores twice as fast as anything else here. Play attacks only in a money deck.

**Open:**
- **4/3:** Talisman / Silver. Raze instead of Silver if you want to trash Estates.
- **5/2:** Counting House / Raze, or Jester / Raze if the opponent is playing money. A Jester hitting their Copper also gives you a Copper.

**Buy priorities:**
1. Two Counting Houses, then Talisman copies.
2. Travelling Fair plus Coppers whenever a Talisman is in play.
3. One Bank at $7.
4. Start the lock as soon as one turn can afford Travelling Fair, a Counting House on top of your deck and enough cards on top to avoid a reshuffle.
5. Then buy Provinces. Buy Bank when you can put it on your deck the same turn.

**Ending:** the Provinces run out by about T15–17. Three piles can also end it, with Counting House, then Bank or Copper, then Provinces or Settlers. Tower favours the lock player because their piles are the ones emptying.

**Watch out for:**
- **Reshuffle before the lock:** when your deck runs low, put enough cards on top to avoid reshuffling the Coppers away.
- **Enchantress or Jester on the board:** put a decoy (Settlers or Raze) or a Copper on top.
- **An opponent going for Counting Houses:** take them faster.
- **3+ players:** more attacks hit you and the Counting House pile is spread thinner, so the lock weakens.

**Least sure of:** when the lock first starts (the T10 estimate). Any delay past about T13 favours money. Test it by playing the setup out from several real shuffles.

**Assumed:**
- Travelling Fair's "put it onto your deck" applies to each gain, including Talisman's copies.
- Tower counts starting Coppers if the Copper pile empties.
- Enchantress affects only the first Action each turn.
- Haunted Woods puts your hand on your deck after the gain. Your hand is empty by then in the lock, so it does nothing.
