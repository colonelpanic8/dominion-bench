**Summary**
- **Plan:** Embassy + Tunnel + Night Watchman money: Embassy and Night Watchman discard Tunnels for free Golds, then buy Provinces. Ritual on a held-back Gold is a small bonus on $7 hands.
- **Openings:** Cursed Gold replaces a Copper, so the splits are 5/4 (40%), 6/3 (48%) and 7/2 (12%), not 4/3 and 5/2. Open Embassy + Tunnel, or Embassy + Faithful Hound on 7/2.
- **Key interactions:** Tunnel with Embassy and Night Watchman; Ritual on Gold for 6 VP at $4; Tower cancels Curses only if the Curse pile empties.
- **Cursed Gold:** play it on turns 1–2, then only for a big upgrade (a Province, a missing Embassy, a Ritual). Each play is usually −1 VP and a dead card.
- **Alternatives:** the City Quarter engine and a Fool's Gold flood both look too slow; the engine verdict is judgment, not simulated.

I used no network access and no ratings: nothing under `data/card-glicko/` was opened, and the "Headline picture" tiers were disregarded. Speed and matchup numbers for the money decks come from a crude Monte Carlo I ran inline (no files written). It covers Embassy, Tunnel, Night Watchman, Ritual, Cursed Gold and simple Hound, Butcher, Pooka and Fool's Gold variants. It does not model City Quarter, Merchant Guild or Nomad Camp.

---

**Board summary:** There is no attack and no fast thinning: Pooka trashes Coppers, Butcher trashes one card per play, and Ritual swaps a card for a Curse. Draw exists only as City Quarter plus terminals in an Action-dense deck, which this board makes slow to reach. The best payload is Tunnel-fed Gold into one Province per turn, plus Ritual-on-Gold, capped by the 10 Curses.

| Card | Cost | Role | Notes |
| --- | --- | --- | --- |
| Embassy (1st-ed. only) | $5 | deck control: terminal draw + sifting. **Build-around** | +5 Cards, discard 3. Discards trigger Tunnel and Faithful Hound. On gain, the opponent gets a Silver. |
| Tunnel | $3 | both: 2 VP, Gold gainer when discarded | Only 8 in the pile and both players want them. It is a Victory card, so Tower ignores it. |
| Night Watchman | $3 | deck control: sifting (Night, not an Action) | Gained to hand, so it is played the night you buy it. Discards Tunnels and Hounds from the top 5; never collides with Embassy; doesn't count for City Quarter. |
| Faithful Hound | $2 | deck control: weak terminal draw | Discarded by Embassy or Night Watchman, it returns as a 6th card next turn (assuming "end of turn" is after the Clean-up draw). Cheap Action for City Quarter. |
| Butcher | $5 | both: +2 Coffers, trash-to-gain | Gold + 2 Coffers gains a Province. Cursed Gold + 1 Coffers gains a $5. Terminal, so it collides with Embassy. |
| Pooka | $5 | deck control: terminal draw + Copper trashing | +4 Cards only by trashing a Treasure, and it can't trash Cursed Gold. An engine card; bad in money. |
| City Quarter | 8 Debt | deck control: village + draw | Draws only per Action in hand. Night Watchman, Tunnel, Fool's Gold, Curses and Estates all blank it. Ritual on it gives 0 VP. |
| Merchant Guild | $5 | payload: +Buy, +$1, Coffers | Counts every card gained in the Buy phase, including Curses from Ritual and Cursed Gold. Terminal. |
| Nomad Camp (1st-ed. only) | $4 | payload: +Buy, +$2 | Gained onto the deck. Terminal. The only other +Buy. |
| Fool's Gold | $2 | payload: economy | $1, then $4 for each later copy that turn. Reaction: trash it to top-deck a Gold when the opponent gains a Province. Scores 1 VP each under Tower if its pile empties. |
| Ritual (Event) | $4 | payload: VP tokens | Gain a Curse, trash a card from hand, +1 VP per $1 of its cost. The card must still be in hand, so hold the Gold back. At most 10 uses across both players, minus every Cursed Gold play. |
| Tower (Landmark) | – | scoring | 1 VP per non-Victory card from an empty Supply pile. In practice it cancels Curses if the Curse pile empties. |
| Cursed Gold (Heirloom) | $4 | economy with a cost | $3 and a Curse per play. Playing it is optional. Once the Curse pile is empty it is a plain Gold. |

Setup: 2 players, 10 Curses, 8 Tunnels, 8 Provinces, no Colonies or Shelters. Special rules in play: Debt, Coffers, Night, VP tokens. Nothing in `context/combos.md` is on this board.

### Candidate strategies
1. **Tunnel–Embassy money (recommended)**
   - How it works: 2 Embassies, about 3 Tunnels, 1–2 Night Watchmen, then Gold and Provinces. A typical turn is Embassy seeing 9 cards, discarding a Tunnel for a Gold, and buying a Province.
   - Needs: Embassy by turn 2 (always possible if you play Cursed Gold) and 2–3 of the 8 Tunnels. Tunnel count barely mattered in the sim (2 to 5 were all about even).
   - Weaknesses: Tunnels and Curses are dead draws; the opponent wants the same Tunnels.
2. **Plain Embassy Big Money (baseline)**
   - How it works: 2 Embassies, treasure, Provinces.
   - Weaknesses: strictly worse than plan 1 here. A third Embassy made it worse in the sim.
3. **City Quarter engine**
   - How it works: 4–5 City Quarters, 2 Pookas, Hounds as cheap Actions, Merchant Guild and Nomad Camp for Buys; payload is Fool's Gold or Gold into two Provinces a turn, or a multi-Buy Ritual cash-out of unplayed $5–6 cards.
   - Needs: Coppers mostly gone and 3 City Quarters paid off by about turn 10, and Curses still in the pile for the cash-out.
   - Weaknesses: each City Quarter costs 8 Debt; Estates, Curses and Cursed Gold stay in the deck; the opponent can burn the Curses.
4. **Fool's Gold flood**
   - How it works: Embassy plus Fool's Gold on every cheap hand, with Nomad Camp for extra Buys, aiming to empty the pile for Tower.
   - Needs: most of the 10 Fool's Golds.
   - Weaknesses: slow to reach density; Tower's bonus needs the whole pile gone.

The table below gives mean VP from solo simulation for plans 1, 2 and 4; the engine row is an estimate.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| 1. Tunnel–Embassy money | ~T7–8 (18.6 VP at T10, 24.4 at T12, 30.7 at T14, 37.2 at T16) | ~T15–16 in a mirror | Province per turn, ~3 VP/turn on average | Provinces, Tunnels, 1–2 Rituals, late Duchies |
| 2. Plain Embassy BM | ~T9–10 (15.3 VP at T12, 24.0 at T16) | ~T16 against plan 1 | Province every other turn | Provinces and Duchies |
| 3. City Quarter engine | ~T13–15 (estimate) | ~T18+ (estimate) | 12–20 with 2–4 Buys (estimate) | Leftover Provinces, Duchies, leftover Curses × 5–6 VP, Tower on piles it empties |
| 4. Fool's Gold flood (simulated without +Buy) | ~T9–10 (16.9 VP at T12, 27.1 at T16) | ~T16 | Province per turn late | Provinces plus up to 10 from Tower |

| You \ Opponent | 1. Tunnel money | 2. Embassy BM | 3. CQ engine | 4. FG flood |
| --- | --- | --- | --- | --- |
| 1. Tunnel money | even; Tunnel split and Cursed Gold discipline decide | favored, about 65–35 (sim) | favored (judgment): ~30 VP by T14 before the engine fires | favored, about 80–20 (sim, flood without +Buy) |
| 2. Embassy BM | unfavored | even | roughly even to favored (judgment) | slightly favored, 54–42 (sim) |
| 3. CQ engine | unfavored (judgment) | uncertain | builds race; Ritual cash-out decides | probably favored if it gets online |
| 4. FG flood | unfavored | slightly unfavored | uncertain | Fool's Gold split decides |

**Robust vs. fragile:** Plan 1 is robust: nothing here attacks it and it scores from turn 7–8. The engine is fragile, because it needs the money player to leave Curses in the pile and to take about 18 turns. The flood is fragile on the Fool's Gold split.

**Recommendation:** Play Tunnel–Embassy money against any opponent.
- **Buy priority:**
  - $8 or more: Province.
  - A Gold in hand, the rest of the hand making $4, and the total under $8: Ritual on the Gold.
  - $5–7: Embassy until you have 2, then Gold. Switch to Duchy at $6–7 once 4 or fewer Provinces remain, and at $5 once 5 or fewer remain.
  - $3–4: Tunnel up to about 3, Night Watchman 1–2, then Silver. Take Tunnel for its 2 VP once 3 or fewer Provinces remain.
  - $2: Faithful Hound is optional (neutral in the sim).
- **Greening:** take Provinces from the first $8; mirrors lasted about 16 turns.
- **Cursed Gold:** restraint beat always playing it by about 59–39. In mirrors where both players held back, the Curse pile emptied only 10–30% of the time, so those Curses usually score −1.
- **Ritual:** it happened about once per player per game and was worth only a couple of points of win rate. Taking it instead of a Province at $8 lost (about 40–58).
- **Skip:** Butcher was slightly negative in a crude test, and a third Embassy also hurt.

**Open:**
- 5/4: Embassy + Tunnel (Night Watchman is close).
- 6/3: Embassy + Tunnel; Embassy beats Gold at $6.
- 7/2: Embassy + Faithful Hound.
- All three require playing Cursed Gold on turn 1 or 2 and taking one Curse, which is worth it for the Embassy. The standard 4/3 and 5/2 don't occur on this board.

**Watch out for:**
- **Curse pile and Tower:** emptying the pile is worth the difference in Curse counts to whoever holds more. If you hold more, take the last Curse (a Ritual on anything does it). If you hold fewer, leave it. Once the pile is empty, play Cursed Gold freely.
- **An opponent building City Quarters:** deny the Ritual cash-out by using Rituals yourself and playing Cursed Gold more freely once about 4 Curses remain. Count their Buys for a three-pile ending on Curses plus two cheap piles.
- **Endgame:** Ritual on Gold scores 6 VP without taking a Province, which helps when buying the second-to-last Province would hand the opponent the win. An opponent holding Fool's Gold top-decks a Gold each time you gain a Province.
- **With 3+ players:** there are 20 or more Curses, so the pile won't empty and Cursed Gold costs more, while Ritual gets more uses. The 12 Tunnels split thinner.

## Process notes

**Files read**
- `/home/imalison/projects/dominion-agents/skills/kingdom-analysis/SKILL.md`
- `/tmp/claude-1000/-home-imalison-projects-dominion-agents/a631d71b-c39f-4667-8a5e-fd864af8e735/scratchpad/abl/k1/kingdom.md`
- `CLAUDE.md`, `context/rules.md`, `context/strategy.md`, `context/card-power.md` and `context/combos.md` were already in context. I did not use the tier lists in `card-power.md`.
- I ran `cardtext.py` for Curse, Gold, Silver, Province, Duchy, Cursed Gold, Tower and Ritual. I did not open the script itself.

**Where the repo was unclear, missing or misleading**
- **Opening splits:** `strategy.md` ("Turns 1–2 give $7… 4/3 or 5/2") and the skill's `**Open:** 4/3 · 5/2` line assume a plain starting deck. Heirlooms change the total and the splits, and nothing prompts you to recompute them.
- **Self-inflicted Curses:** `strategy.md` says "The Curse pile will empty", which fits junking attacks. On this board I assumed the same and was wrong: with only Cursed Gold and Ritual draining it, the pile usually didn't empty when both players held back.
- **Optional Treasures:** nothing covers when to decline a Treasure with a drawback, which was the largest single decision here.
- **Events and Landmarks as payload:** the skill mentions landscape roles, but not capped VP Events like Ritual or Landmarks that reward empty piles like Tower. Reading the text alone, I overrated Ritual until the sim showed it was about one use per game.
- **Speed estimates:** skill step 6 asks for turn numbers but offers no method. The simulator caveat in `card-power.md` was useful for scoping what to trust. The engine row is still a guess.
- **End-of-turn timing:** `rules.md` doesn't say whether "end of turn" is after the Clean-up draw, which Faithful Hound depends on. I assumed it is.
- **Edition marking:** `CLAUDE.md` asks for first-edition-only cards to be marked. The kingdom file says only "1st ed. cards included", so I inferred Embassy and Nomad Camp from the edition notes in `rules.md`.
- **Ratings step:** skipped as instructed (skill step 2).