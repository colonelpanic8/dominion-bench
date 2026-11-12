# Kingdom analysis: oc-2026-final-g1

**Board:** There are no trashers here. The only card that ever gets trashed is Cage, which trashes itself, so every deck keeps its 7 Coppers and 3 Estates. The draw cards are Council Room (+4 Cards, +1 Buy, and it gives the opponent a card), Patrol (+3 Cards) and Litter. Litter acts as both village and draw: net +1 Card and +1 Action, but each play costs $1 of Debt. Way of the Squirrel can turn any spare Action into 2 extra cards in your next hand. The only scoring is Provinces, Duchies, Tunnels (2 VP each) and Vineyards, and the game almost certainly ends on Provinces.

What's still open: is an engine with no trashing and a Debt-taxed village ever faster than Council Room money? And do the Gold gainers (Tunnel and Market Square) have anything that triggers them?

**Inventory:**
- **Kingdom:** Border Guard $2, Cage $2, Tunnel $3, Astrolabe $3, Market Square $3, Council Room $5, Jester $5, Litter $5, Patrol $5, Vineyard $0 plus a Potion.
- **Landscapes:** Way of the Squirrel and Seaway ($5 Event).
- **Extras that come with the cards:** the Potion pile, the Lantern and Horn Artifacts, Debt (from Litter), and Duration Treasures (Cage, Astrolabe).
- **Price points:** $5 is crowded. Council Room, Jester, Litter, Patrol and Seaway all compete for every $5 hand. There is nothing above $5 except Gold and Province.
- **Starting deck:** the standard 7 Copper and 3 Estates, so the opening splits are 4/3 or 5/2.

**Key interactions:**
- **Litter + Council Room (and Patrol):** Litter is the only real village. Litter, Litter, Council Room turns a 5-card hand into 10 cards with 2 Actions left, but costs $2 of Debt.
  - Each Litter play is +1 card for $1, so it is a Laboratory with a tax.
  - In a money deck, one Litter alongside two Council Rooms stops them colliding. In an engine you need about 4 Litters plus 2 Council Rooms to draw a deck of about 23 cards.
- **Way of the Squirrel + spare Actions:** any Action played with your last spare Action (a Border Guard, Market Square, or a Council Room drawn when nothing is left to draw) gives 2 extra cards at end of turn. That means a next hand of 7 or more.
  - Each Squirrel use trades the card's own effect for those 2 cards. It only pays when you have Actions to spare, which in practice means Litter decks.
- **Border Guard + Tunnel:** this is the only steady way to discard Tunnel outside Clean-up. When Tunnel is one of the revealed cards, discarding it gains a Gold.
  - With 3 Tunnels in 20 cards, a Border Guard play reveals one about 28% of the time.
  - Lantern raises this, since it reveals 3 cards. But you only take Lantern when Border Guard reveals 2 Actions, which happens only in Action-dense decks.
  - Patrol works against this: it puts revealed Tunnels into your hand as dead cards.
- **Cage + Market Square:** Cage trashing itself is the board's only trash. Gaining any Victory card (a Province, Tunnel or Vineyard) with Cage in play, while holding Market Square, gains a Gold.
  - The best case is spending $3 and 2 Buys on a Tunnel plus a Gold. You then rebuy Cage for $2.
  - It's real but slow, and it means holding Market Square in hand instead of playing it.
- **The opponent's Jester + your Tunnel:** if they flip your Tunnel, you gain a Gold and a Curse. This partly cancels Jester's junking.

**Other cards:**
- **Patrol:** a Council Room substitute in a money deck that doesn't feed the opponent, but has no +Buy. It works against Tunnels.
- **Jester:** best partner is none. It's a weak $2 terminal attack. Against money it often hands the opponent a Copper and occasionally takes their Silver or Gold, and its Curses depend on hitting Victory cards. Skip it.
- **Astrolabe:** +Buy and $1 now and next turn. It's a minor engine payload piece, and Silver is better in a money deck.
- **Vineyard:** pairs with cheap Actions (Border Guard at $2, Market Square at $3, Seaway). Needs a Potion at $4, and 8 copies are available. See the plans below.
- **Seaway:** can only gain Border Guard or Market Square (Tunnel and Vineyard aren't Actions). Weak.
- **Market Square:** besides the Cage interaction, it's a +Buy cantrip for engines. Weak in money.
- **Cage:** besides Market Square, it can store surplus cards and return them after your next Victory gain, making a bigger next hand. It's a $0 stop card in hand, so mostly skip it.
- **Ratings check (Glicko):** Way of the Squirrel 1.82, Border Guard 1.57, Market Square 1.27, Vineyard 0.64, Litter 0.54, Cage 0.09, Astrolabe −0.47, Patrol −0.50, Council Room −0.94, Tunnel −1.71, Jester −1.81.
  - My view rates Council Room higher than its −0.94. On this board it's the best X for a money deck, and there's no trashing for an engine to exploit.
  - It rates Market Square lower than its 1.27, because there's almost no trashing to trigger it.
  - No combo from `context/combos.md` is present. Market Square needs Hermit or Donate for its combo, and neither is here.

### Build lines
- **Council Room + Litter money (pick), 4/3:**
  - T1–2: Silver/Silver.
  - T3–4: Council Room at $5, Silver at $4. The deck is now 14 cards worth $13.
  - T5–7: a Council Room turn gives about $7, so buy Gold. Then Litter at $5 and Silver at $4.
  - T8–10: the deck is 17 cards worth about $18. Litter, then Council Room, draws 9 cards for about $9 minus $1 Debt, enough for a Province on T8. Then Gold, and a second Council Room on T10.
  - From T11: about one Province every 1.5 turns, so 4 Provinces by about T14–15.
  - Council Room's +Buy turns late $11 hands into Province + Tunnel, and $13 into Province + Duchy.
  - With 2 Council Rooms in about 18 cards you play one on about 50% of turns, and Litter covers collisions.
- **Litter/Council Room engine:**
  - T1–2: Silver/Silver.
  - T3–6: Litter ×2, Council Room, Litter.
  - T7–10: Market Square, Astrolabe, Council Room, Gold, Litter.
  - First Province about T11. It draws its deck reliably from about T13, with Squirrel used on spare Actions.
  - Built turn, from 23–25 cards: 7 Coppers + 2 Golds + 1 Silver + Astrolabe gives about $17, minus about $4 of Debt, so about $13 with 3–4 Buys. That's Province + Duchy, and only sometimes 2 Provinces.
  - Greening clogs it, because nothing trashes.
- **Border Guard/Market Square/Vineyard alt-VP:**
  - Buy cheap cantrips plus 1–2 Potions. With about 15 Actions, each Vineyard is worth 5 VP.
  - Without Silver or Gold, hands are about $3–4. That's about 1 Vineyard plus 1 cantrip per turn, so 8 Vineyards (about 35–40 VP) take until T18 or later.
  - The opponent can contest Vineyards with one Potion.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| Council Room/Litter money | ~T8 | ~T18 (Province split) | Province, or Province + Tunnel/Duchy | all Provinces + Duchies |
| Litter/Council Room engine | ~T11 | ~T17 | Province + Duchy (9) | same, but slower to collect |
| Cantrip/Vineyard | ~T8 (low rate) | ~T20 (3-pile) | ~5 | ~40 |

**Plans considered:**
- **Council Room-BM** (baseline): $6 about T5, $8 about T8, 4 Provinces by about T14–15. Needs 2 Council Rooms. Its weakness is that each Council Room play gives the opponent a card.
- **Council Room + Litter money** (the pick): the same line, but Litter makes the two Council Rooms play together and adds a cheap Laboratory effect. Borders Guards fill $2 hands.
- **Patrol-BM:** about equal speed, with no gift to the opponent but no +Buy. Prefer it if the opponent is clearly money and racing.
- **Litter engine:** first Province about T11, Province + Duchy from about T13. Needs about 4 Litters and 2 Council Rooms, all bought at $5. It falls 12–18 VP behind early and only breaks even around T17–18, which is about when the Provinces run out.
- **Vineyard cantrip deck:** too poor to fund itself.
- **Jester-BM:** weak, rejected.

**Recommendation:** play Council Room money with one or two Litters and a Border Guard or two.
- It hits the Big Money clock (4 Provinces by about T15), and Council Room's +Buy gives it late Tunnel and Duchy flexibility.
- The engine needs six $5 pieces with no trashing, and pays a Debt tax on every Litter. Its payload tops out around Province + Duchy, so it doesn't clearly beat this race.

**Against their best plan:**
- **Mirror:** both sides' Council Room gifts roughly cancel, and turn order plus Province and Duchy timing decide it.
- **Against the Litter engine:** I'm about 2 Provinces up by T13, so I take the Penultimate Province decision and Duchies first. My Council Room gifts help their draw slightly, so lean toward Patrol for the second copy.
- **Against Jester:** it occasionally copies my Gold for them, but more often hands me Coppers or Curses. If Jester starts cursing me, Tunnels in my deck at least turn its hits into Golds. It doesn't change the plan.

**Challenged:**
- **Engine re-tested with Squirrel:** spending 2–3 spare Actions on Squirrel starts each turn with 9–11 cards, which fixes consistency from about T12. But the payload is still capped by 7 Coppers and the Debt tax, so it stays the runner-up.
- **When to switch to it:** if a slog develops (heavy Jester cursing, slow Province split), or if Litters come cheaply via early $5/$5 hands.
- **How the pick loses:** a bad Council Room collision streak, or the opponent's T3–4 Jester stealing early Silvers. Both are variance, not a structural problem.

**Open:**
- **4/3:** Silver / Silver.
- **5/2:** Council Room / Border Guard. Border Guard is a free sifting cantrip in money.

**Buy priorities:**
- Province at $8.
- Gold at $6–7.
- At $5: first Council Room, then Litter, then a second Council Room (or Patrol). No more terminals after that.
- Silver at $3–4. Border Guard on a $2 hand.
- **Greening:** Duchy at $5–7 from about 4 Provinces left. Late, Tunnel at $3–4 instead of Estate. With +Buy, $11 buys Province + Tunnel.

**Ending:** Provinces run out around T17–19. A three-pile ending is unlikely, unless a Vineyard player drains Border Guard, Market Square and Vineyard; the Duchy and Tunnel piles may thin late.

**Watch out for:**
1. **The opponent committing to Vineyards with a Potion:** count their Actions, and buy one Potion to contest only if their Vineyards would be worth 4 VP or more each.
2. **The opponent's Jester:** keep buying Gold over cantrips.
3. **More players:** Council Room's gift scales with each opponent (prefer Patrol), and Jester's attack gets stronger.

**Least sure of:** whether the Squirrel-assisted Litter engine actually reaches Province + Duchy turns by T12 rather than T14. To test it, play both lines out solo for 14 turns with real shuffles. If the engine hits $13+ with 3 Buys by T12, switch to it.

**Assumed:**
- Cage's set-aside cards and Way of the Squirrel's cards arrive at end of turn, after the Clean-up draw, so they enlarge the next hand.
- Litter's Debt must be paid off before buying.
- Seaway can't gain Tunnel, Vineyard or Treasures.
- Vineyard counts Market Square, which is an Action–Reaction.

All of this comes from the card text in the kingdom file and the repo's rules and strategy context, with Glicko ratings from the July 2026 snapshot. The build lines are average-draw estimates, not simulations.
