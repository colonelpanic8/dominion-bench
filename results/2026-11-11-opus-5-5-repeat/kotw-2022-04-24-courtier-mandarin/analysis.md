I worked through all eight steps of the skill. Ratings come from `data/card-glicko/cards.csv`, `ways.csv` and `events-projects.csv`.

---

## Inventory

- **Kingdom:** Lurker $2 · Steward $3 · Tunnel $3 · Cardinal $4 · Silk Road $4 (1st ed.) · Village Green $4 · Barge $5 · Courtier $5 · Displace $5 · Mandarin $5 (1st ed.)
- **Landscapes:** Gamble (Event, $2), Way of the Goat (Way)
- **Special rules in play:** Exile (Displace, Cardinal), Durations (Barge, Village Green), on-discard Reactions (Tunnel, Village Green).
- **Setup:** Colonies and Shelters aren't specified. No Prosperity or Dark Ages cards are present, so I assume neither. Starting deck is 7 Copper and 3 Estate, giving splits of 4/3 or 5/2.
- **Prices:** $5 is crowded (Barge, Courtier, Displace, Mandarin). $2 has only Lurker and Gamble. Nothing costs more than $5, so Gold and Province are the only things above it.

**Board:** The game is about turning Tunnels into Golds. Three things discard a Tunnel outside Clean-up:
- **Gamble** discards the top card of your deck.
- **Exile**: when you gain a Tunnel you may discard all your Exiled Tunnels. Displace can Exile them, and so can the opponent's Cardinal.
- **The opponent's Cardinal** also discards the cards it reveals.

Courtier also rewards Tunnels: a Tunnel has 2 types, so revealing one gives +$3 *and* a Gold.

Courtier gives 2–3 choices for each multi-type card here. Village Green has 3 types, so Courtier revealing it acts like a Market with +$3. Barge is the only real draw and Village Green the only real village, so a full engine is thin.

Scoring is Provinces plus cheap Victory cards: Tunnel (2 VP), Silk Road and Duchy. Tunnels, which you buy anyway, also count toward Silk Road. Expect a fast, Gold-heavy money game that greens early.

## Key interactions

- **Courtier + Tunnel:** reveal Tunnel for +$3 and a Gold. With a Village Green revealed instead you get +Action, +Buy and +$3, or swap one of those for a Gold. Revealing Barge or Cardinal gives 2 choices. Even revealing a Copper or Estate gives one: +$3 or a Gold. So every play is at least Gold-level, and it works from turn 3.
- **Gamble + Tunnel:** Gamble costs $2 and a Buy and gives +1 Buy back. So you can buy any number of Gambles first and still buy your Province last. You don't need a separate +Buy card.
  - What it discards: a Tunnel gains a Gold. A Treasure or Action can be played.
  - Net cost: Copper −$1, Silver $0, Gold +$1, Mandarin or Courtier about +$1. A Barge or Village Green played this way should be set for next turn.
  - That makes it a near-free way to spend leftover $2–3. It finds the Tunnel about 15–25% of the time once you have 3–5 Tunnels.
- **Displace + Exile:**
  - Exile a Tunnel to gain a $5 card or a Duchy. The next time you gain a Tunnel, discard every Exiled Tunnel and gain a Gold for each.
  - Late game, Exile a Gold to gain a Province. The next Gold you gain from Courtier or a Tunnel brings the Exiled Golds back to your discard pile, so that Province costs you almost nothing.
- **Village Green + Courtier/Barge/Displace:** Village Green lets you play several terminals in one turn. Revealing it to Courtier is also the best reveal.
- **Mandarin + Gamble (minor):** you need 2+ Buys. Buy Mandarin first, which puts your Treasures in play on top of your deck. Each later Gamble then replays one, gaining $1 net per Gold. With 4+ Golds in play, Mandarin costs about $1. If Mandarin is your last buy, your Treasures become next turn's hand.
- **Cardinal backfires against Tunnels or Village Green.** Its discard gives them a Gold or plays their Village Green. Anything it Exiles comes back to them the next time they gain a copy. Their Cardinal against you does the same.

## Other cards

- **Steward** (3.04, top-rated here): a flexible $3, useful as +$2 or +2 Cards to reach $5. Don't trash Estates in a Silk Road game. Trashing Coppers only helps a little.
- **Silk Road:** pairs with Tunnels. A typical late deck has about 3 Estates, 4 Tunnels, 3 Provinces, 2 Duchies and 3 Silk Roads, so each Silk Road is worth about 3–4 VP for $4. Buy them late, ahead of Duchy.
- **Lurker:** none worth building. It could control piles by trashing Village Green or Courtier from the Supply, or slowly regain them from the trash.
- **Way of the Goat:** any Action can trash a card from your hand instead of doing its own text. Useful on a dead Mandarin, Cardinal or Lurker. Minor.
- **Cardinal:** good only against a pure Silver/Gold deck with no Tunnels and no Village Greens, and even then its Exiles come back when they gain a copy.
- **Ratings vs my view:**
  - Courtier is −0.28, but it is much better here because of the multi-type cards.
  - Tunnel is −1.71, but it is much better here because of the Gamble and Exile outlets.
  - Mandarin and Silk Road are deprecated with phi 1.0, so their ratings carry little weight.
  - Cardinal is −2.26, which is about right.
  - Steward 3.04 and Barge 2.61 are a little overrated here.

## Build lines

- **A. Barge-BM (baseline):**
  - T1–2: Silver/Silver.
  - First Barge at the first $5, Gold at $6–7, Province at $8, a second Barge around T8.
  - First $6 around T5–6 and first $8 around T7–9. About 4 Provinces by T14–15.
- **B. Courtier–Tunnel Gold flood (pick):**
  - T1–2 (5/2): Courtier / nothing.
  - T3: Courtier on a Copper for a Gold, then $4 for a Silver.
  - T4: $3 for a Tunnel.
  - Deck: 7C 3E Courtier Gold Silver Tunnel (14 cards).
  - T5: Courtier for a Gold (+$3 if a Tunnel is in hand, about 30%), then $5 for a Barge.
  - T6: $6 for a Gold.
  - T7: $4 for a Village Green, or a Tunnel plus a Gamble.
  - Deck: 7C 3E 3 Gold Silver 2 Tunnel Courtier Barge Village Green (19 cards). About $1 per card, with Barge adding +3 Cards and Courtier adding +$3 and a Gold.
  - T8–9: first Provinces. Barge's Buy or a Gamble takes leftover $2.
  - From then on, about 1 Province per turn, plus Tunnels, Silk Roads and Gambles with leftover money. Golds keep arriving at about 1 every 1–2 turns, which slows the choking from greening.
  - Built turn: Village Green, then Courtier revealing a Tunnel (+$3 and a Gold), then Barge (+3 Cards, +Buy), plus 2–3 Golds. That is about $13–15 and 2–3 Buys: Province + Duchy or Silk Road, or Province + Gambles.
- **C. Village Green/Barge/Steward engine with Courtier payload:**
  - Draw is only Barge, which is +2 net per play under a village and half the time arrives next turn. Drawing the deck needs about 4 Barges, 4 Village Greens and 2–3 Courtiers, roughly 11 buys at $4–5.
  - Draws the deck about T12–13 and peaks at 2 Provinces per turn.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| A Barge-BM | ~T8 | ~T20 (alone) | 1 Province | Provinces + Duchies |
| B Gold flood | ~T8 | ~T16–17 | Province + Tunnel/Silk Road (~9 VP) | Provinces + 16 VP of Tunnels + Silk Roads |
| C Engine | ~T12 | ~T17–18 | 2 Provinces | same as B |

## Plans considered

- **A. Barge-BM:** simple and reliable. Weakness: it ignores the Tunnel and Courtier Golds and takes about one Province every other turn.
- **B. Gold flood:** Courtier, Tunnels, Gamble, one Barge, one or two Village Greens, Displace later. Needs 2 Courtiers by about T8 and 3–5 Tunnels. Weakness: the Tunnel pile (8) is contested in a mirror, and the deck greens early.
- **C. Engine:** the highest ceiling. Weakness: thin, expensive draw that comes online about 4 turns behind B, and its pieces are the same ones B buys anyway.

**Against their best plan:**
- **B vs a B mirror:**
  - Tunnels decide it. Take your share early: they are 2 VP each, they are Gold sources, and they count for Silk Road.
  - Second Courtier vs first Barge matters more than a Gold.
  - The likely three piles are Tunnel, Silk Road and Duchy, so count gains once two piles are low.
- **B vs A:** B is faster, because Courtier is a Gold gainer that also pays now and Tunnels are points that don't choke you.
- **B vs C:** B's lead by T12 is about 3 Provinces plus Tunnels. C needs 2 Provinces a turn from T13 just to catch up, and can't get it.
- **Cardinal:** helps B against them.

**Challenged:**
- **Re-testing the engine:** the best version opens Steward/Silver into Village Green, Barge and Courtier. It is still B with 3 more Barges, and those turns are better spent on Golds and Tunnels. The engine's payload (Courtier reveals, Golds) is B's payload, so B just gets there sooner. I let B grow into a light engine with more Village Greens and Barges if the game runs long.
- **How B loses:** you open without Courtier (4/3) and the opponent gets 2 Courtiers first. Or the opponent hoards Tunnels and three-piles Tunnel, Silk Road and Duchy while ahead. Watch the Tunnel count from the start.

## Recommendation

**Plan B, the Courtier–Tunnel Gold flood.**
- Every Courtier play is worth at least a Gold, and Tunnels are points that become more Golds.
- Gamble acts as +Buy and pays off leftover money.
- Barge adds draw and a Buy. Village Green makes your terminals work together and is Courtier's best reveal.
- Late, Displace turns Golds into Provinces.

It holds up against money, a mirror and Cardinal. Each of them either gives you Golds or loses the race.

**Open:**
- **5/2:** Courtier / nothing (Lurker isn't worth it). Courtier gains a Gold from T3.
- **4/3:** Silver / Steward, to reach $5 for Courtier on T3–4. Silver / Tunnel is close.

**Buy priorities:**
- **Shuffles 1–2:**
  - Courtier first, then a second Courtier.
  - Gold at $6–7.
  - Barge as the third $5.
  - Tunnels at $3. Gamble with leftover $2.
- **Shuffle 3:**
  - One or two Village Greens once you have 3+ terminals.
  - Displace as a fourth $5, for Tunnel→$5 or Gold→Province.
  - A Mandarin is fine on a 2-Buy turn that is heavy in Golds.
- **Greening:**
  - Province at $8 from about T8.
  - Keep taking Tunnels throughout.
  - Silk Road over Duchy once you have about 12+ Victory cards, roughly from mid-game.
  - Duchies at 4 Provinces left. Estates at the end, since they also count toward Silk Road.

**Ending:** Provinces, or three piles (Tunnel, Silk Road, Duchy) in a Tunnel mirror. Tunnels will run out first.

**Watch out for:**
1. The race for the Tunnel pile.
2. Colliding terminals (Courtier, Barge, Displace, Steward) before you have a Village Green.
3. Three-pile timing once Tunnels are gone.

**What would flip it:**
- Shelters would change Courtier's math: Overgrown Estate and Necropolis are 2-type cards.
- With 3+ players there are 12 Tunnels, Courtier is still strong, and Cardinal is even worse because it feeds more decks.

**Least sure of:**
- How well Gamble pays. If Tunnels make up under 15% of the deck, it is near break-even and only a way to spend leftover money.
- Whether 4/3 should open with Tunnel. Test: play out Silver/Steward vs Silver/Tunnel to T8 and count Golds and Courtiers.

**Assumed:**
- No Colonies or Shelters.
- Each Exiled Tunnel discarded on gaining a Tunnel triggers its own Gold.
- Cardinal's discard of revealed cards counts as "other than during Clean-up", so it triggers the victim's Tunnel and Village Green.
- An Action played by Gamble in the Buy phase still resolves fully, so Courtier's +$3 or Gold counts.
- Mandarin and Silk Road are used with their first-edition text, as given in the kingdom file.
