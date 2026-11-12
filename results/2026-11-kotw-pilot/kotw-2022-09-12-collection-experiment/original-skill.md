I couldn't save the analysis: the harness blocked writing `/tmp/claude-1000/-home-imalison-projects-dominion-agents/a631d71b-c39f-4667-8a5e-fd864af8e735/scratchpad/kotw/k3/analysis.md` ("Subagents should return findings as text"), so the full text is below for you to save.

**Summary**
1. **Plan:** a Collection–Tiara–Experiment loop. Collection gives +1 VP per Action gained while it's in play, Tiara plays Collection twice, and each $3 Experiment is 2 Action gains. That makes uncapped VP tokens, worth more than Colonies.
2. **Openings:** 4/3 Silver / Lackeys; 5/2 Collection / Lackeys.
3. **Key interaction:** put the Experiments you buy on top of your deck with Tiara. Next turn they chain and draw most of your deck, then go back to their pile, which empties for the opponent's turn. This is the board's real draw.
4. **Mirror:** the Collection split decides it (aim for 5 or more), with Pilgrimage copying Collection, Tiara and Platinum to win it. Expect a three-pile ending on Experiment + Port + Lackeys/Raze around turns 14–17.
5. **No network access:** no web, browser or curl, and no files outside the repo, `cardtext.py` and `k3/`.

---

# Kingdom analysis: Artificer, Collection, Experiment, Forge, Grand Market, Lackeys, Port, Raze, Scholar, Tiara + Pilgrimage, Silos (Colony/Platinum)

**Board summary:** Trashing is weak. Raze trashes one card per play, and Forge is a $7 terminal that only works on Estates. There is no junking attack. Draw is mediocre for a classic engine: Lackeys and Experiment each net only +1 card, Port is a village that draws one card, and Scholar discards the hand you want to keep. Payload is outstanding, though. **Collection** gives +1 VP for every Action you gain while it's in play. **Tiara** plays a Collection twice (and plays other Tiaras twice). **Experiment** gives 2 Action gains for $3, then sits in your deck as a self-returning Lab. Together they make an uncapped VP-token engine that easily outscores Colonies. Tiara topdecking bought Experiments also turns those Experiments into next turn's draw. The real ceiling is the number of Collection plays times the number of cheap Action gains, and the game is decided by the Collection split, the Experiment pile and the three-pile clock.

## Inventory

- Kingdom: Raze $2, Lackeys $2, Experiment $3, Port $4, Tiara $4, Artificer $5, Collection $5, Scholar $5, Grand Market $6, Forge $7.
- Event: Pilgrimage $4. It flips the Journey token, and every second purchase (the token starts face up, so the first buy turns it face down and does nothing) gains copies of up to 3 differently named cards in play. No other Journey-token cards are on the board.
- Project: Silos $4.
- Colony and Platinum are in. No Shelters, no Potion, no Debt. Villagers come from Lackeys.
- Pile notes: Port and Experiment each gain a second copy, so their piles fall 2 per buy (Port runs out after 5 buys). A played Experiment returns to its pile, so that pile refills over time. But **the Experiments sitting in decks at the end of a turn count as missing for the three-pile check.**
- Platinum/Colony text was blank in the card tool. I assumed the standard text from `context/rules.md`: Platinum makes $5, Colony is worth 10 VP.

## Roles

| Card | Cost | Rating (Glicko) | Role | Notes |
| --- | --- | --- | --- | --- |
| Collection | $5 | 4.67 | payload: +$2, +Buy, VP per Action gain | **Centerpiece.** A Treasure, so buying it scores nothing. Several plays stack. The pile of 10 is contested. |
| Tiara | $4 | 1.44 | payload: +Buy, Treasure multiplier, topdecks gains | Doubles Collection (2 VP per gain) or Platinum ($10). Tiara on Tiara doubles two more Treasures. Topdecking feeds the Experiment loop. Rates far above its prior here. |
| Experiment | $3 | 1.72 | both: one-shot Lab; 2 Action gains per buy | Cheapest VP fuel at $1.50 per gain. It leaves the deck after one play, so buying it for VP never clogs the deck. Not in play when Pilgrimage resolves. |
| Lackeys | $2 | 4.47 | deck control: terminal +2 Cards, +2 Villagers on gain | Its Villagers fund its own play. Also a $2 VP-gain target that builds the deck. |
| Port | $4 | 3.41 | deck control: village (+1 Card) | The only real village besides Villagers. 2 Action gains per buy. The pile empties in 5 buys. |
| Grand Market | $6 | 1.92 | both: cantrip, +$2, +Buy | Can't be bought with Copper in play: hold your Coppers back, or let Silos discard them. Can also be gained with Artificer (discard 6), Pilgrimage or Forge. |
| Artificer | $5 | 1.66 | deck control: cantrip, +$1, turns junk into gains onto your deck | Discard 3 to topdeck an Experiment (the second copy goes to your discard pile), 4 for 2 Ports, 6 for a Grand Market. Its gains happen in the Action phase, so they don't trigger Collection. |
| Raze | $2 | 2.00 | deck control: non-terminal trash/sift | Trashing an Estate sifts 2 cards. Late, it trashes itself, so it's also a clean $2 VP gain. |
| Silos | $4 | 0.45 | deck control: turns Coppers into draw | Good here: trashing is weak, so Coppers stay. Discarding them also unlocks Grand Market buys. Get it mid-game. |
| Pilgrimage | $4 | −2.14 | payload/builder: gains copies of cards in play | Better than its prior on this board, because it copies **Collection, Tiara, Platinum and Grand Market** (Port in play also brings its second copy). It's the main way to win the Collection split. |
| Scholar | $5 | −3.22 | deck control: terminal "discard your hand, +7 Cards" | Throws away the Treasures your payload needs. Worth at most 1 late. |
| Forge | $7 | −0.81 | neither (niche) | Turns 3 Estates into a Grand Market or Platinum + Raze into a Colony. Too slow and terminal to matter. |
| Platinum / Colony | $9 / $11 | — | payload / VP | Platinum is fine money, especially doubled by Tiara. Colony is mostly worse than spending the same $ on Experiments (see below). |

Plans are built around Collection (with Tiara + Experiment). Lackeys, Port, Grand Market, Artificer, Silos and Pilgrimage support them.

## Interactions

1. **Collection × Action gainers (the deciding one).** A Collection in play earns 1 VP per Action gain. Experiment ($3) gives 2 gains, Port ($4) gives 2, Lackeys and Raze ($2) give 1, and a Pilgrimage activation gives 2–4 (Port in play brings its extra copy). Buying 3 Experiments with 3 Collection plays scores 18 VP, nearly two Colonies, for $9.
2. **Tiara × Collection.** Tiara plays a Collection twice, so both its VP trigger and its +Buy count twice. Tiara → Tiara → two Collections gives 4 Collection plays, 7 Buys and $8. Tiaras are the multiplier, and they're cheap.
3. **Tiara topdeck × Experiment (the draw loop).** Put the Experiments you buy on top of your deck. Next turn's hand is all Experiments, and playing them chains. Topdecking 2N Experiments draws roughly 5 + 2N real cards next turn: 11 cards after buying 3 Experiments. The Experiments then return to the pile to be bought again. This is the board's real draw, and it beats Port/Lackeys/Scholar.
4. **Experiment pile denial.** Experiments you topdeck stay out of the pile through the opponent's turn. Draining the pile denies them their best VP buy, and the empty pile counts toward a three-pile ending. A mirror swings on this.
5. **Pilgrimage × Treasures in play.** Pilgrimage copies Collection, Tiara and Platinum, not just Actions. It also copies Grand Market, getting around the Copper restriction.
6. **Silos × Grand Market / Copper.** Silos discards Coppers before you could play them, so a Copper-heavy deck can buy Grand Market and cycle its junk.
7. **Artificer × Experiment/Port.** Artificer turns dead cards into an Experiment on top of your deck. It's useful, but it gains in the Action phase, so it gets no Collection VP.

None of the `combos.md` combos are on this board. Collection + cheap double gainers plus Tiara is the board-specific outlier.

## Gate questions

1. **Trashing:** weak. Raze trims Estates slowly. Live with Coppers and use Silos.
2. **Junking:** none. Nothing slows a thin VP-token build.
3. **Draw:** Port + Lackeys nets about +1 card per pair, and Scholar conflicts with Treasure payload. Classic "draw your deck" engines are hard. Experiments topdecked by Tiara are the real draw, and they come free with the VP purchases.
4. **Payload ceiling:** high and uncapped. Collection plays × Action gains, roughly 10–30 VP per turn once you have 3–4 Collection plays and $9–15. Colonies (10 VP each) are a lower ceiling.
5. **Outliers:** Collection (top 20 overall) on a board with $3 double gainers and a Treasure multiplier.
6. **Scoring routes and piles:** Collection VP tokens (dominant), Colonies, Provinces, Duchies. The piles that drain are Collection (contested), Experiment (drained by mass buys), Port (5 buys) and Lackeys/Raze (bought for VP). The game will most likely end on piles: Experiment + two of Port/Lackeys/Raze/Collection. Colonies are unlikely to run out.

## Candidate strategies

1. **Colony Big Money (baseline):** Silver/Gold → Platinum → Colony, with Tiara for Platinum doubling and a Lackeys or two. *Needs:* $11 hands, so it takes Colonies only from about turn 15. *Weaknesses:* slow, one big VP purchase per turn at best, and no answer to token scoring.
2. **Collection money (good-stuff):** Silver/Collection/Grand Market/Platinum economy with 1–2 Lackeys. Every spare Buy goes to Experiments, Lackeys or Raze for tokens. *Needs:* 3+ Collections by turn 9. *Weaknesses:* without Tiaras the VP rate grows linearly and the Experiments arrive at random.
3. **Collection–Tiara–Experiment loop (recommended):** Payload is Collections plus Tiaras, with Grand Market and Platinum later. Deck control is the topdecked Experiments, Lackeys (with its Villagers), Silos, one or two Ports, and optionally Artificer. Pilgrimage builds the economy mid-game. A typical built turn: the hand opens with 4–6 topdecked Experiments that draw most of the deck. Play Tiara→Tiara→Collections for 4–6 Collection plays, $12+ and 7+ Buys. Buy 3–5 Experiments (topdecked again) plus Lackeys or Raze for 20–40 VP. *Needs:* at least 5 Collections (a majority of the pile) and 2–3 Tiaras by about turn 10. *Weaknesses:* the Collection split and the Experiment pile are contested. A turn without Tiara loses the topdeck and the loop breaks for a shuffle. Dead Treasure hands if you overbuild Tiaras with too few Collections.
4. **Port/Lackeys/Scholar engine to Colonies:** villages and Villagers plus Lackeys/Scholar draw, with Grand Market and Platinum payload, double Colony turns. *Needs:* 4+ Ports, 5+ Lackeys and a Grand Market base by about turn 13. *Weaknesses:* weak net draw, no trashing, and Colonies are a lower-yield payload than tokens.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| 1. Colony BM | ~T13 | ~T25+ (8 Colonies) | 10 | 8 Colonies + Provinces |
| 2. Collection money | ~T6 (small) | ~T18 via piles | 8–15 | uncapped tokens |
| 3. Collection–Tiara–Experiment loop | ~T6 small, ~T10 big | ~T14–17 via piles | 20–40 | uncapped tokens |
| 4. Port/Lackeys engine → Colonies | ~T13 | ~T20 | 20 (2 Colonies) | Colonies + Provinces |

## Matchups

| You \ Opponent | 1. Colony BM | 2. Collection money | 3. Tiara loop | 4. Port engine |
| --- | --- | --- | --- | --- |
| 1. Colony BM | even | unfavored: tokens arrive 5+ turns earlier | heavily unfavored | unfavored: slower than either |
| 2. Collection money | favored: tokens from T6, can three-pile | even | unfavored: fewer Collection plays, loses the Experiment pile | favored: tokens ahead before Colonies start |
| 3. Tiara loop | heavily favored | favored: Tiaras multiply the same Collections; topdecking keeps Experiments away from the opponent | even: the Collection split and the Experiment pile decide it | heavily favored: can end on piles before double Colonies arrive |
| 4. Port engine | favored | unfavored | heavily unfavored | even |

**Robust vs. fragile:** Plan 3 is robust. Its weakness is the mirror, and there the Collection split decides it, so contest Collection hard. Plan 2 is fine against non-Collection plans. Plans 1 and 4 are fragile: they only work if the opponent ignores Collection, and even then a single Collection player takes a dominant token lead.

## Recommendation

Play the **Collection–Tiara–Experiment loop**. Collection is the only route to uncapped scoring, and Tiara multiplies it. Topdecked Experiments solve the board's weak draw while scoring. The best response is the mirror, and you win that by getting more Collections (use Pilgrimage to copy them), more Tiaras, and control of the Experiment pile. The plan doesn't change against a weak or unknown opponent. You just win faster, and can end on piles earlier.

What would flip it: if the opponent gets the Collection pile to 7+/3, stop contesting and pivot to Lackeys/Raze denial plus Colonies, and end on piles as fast as possible. With 3+ players, Collections split thinner, so Tiara (more plays per Collection) and pile timing matter more, and the four-pile ending (5–6 players) gives you more time.

## Openings and buy priorities

- **4/3: Silver / Lackeys.** Silver and Lackeys' draw help you hit $5 for Collection on turns 3–4, and the 2 Villagers bank for later Lackeys. Silver / Experiment is an acceptable alternative.
- **5/2: Collection / Lackeys.** Collection arrives a shuffle early. Raze is the alternative $2 if you'd rather clear Estates.
- **First 2–3 shuffles:**
  - $5–7: Collection, aiming for at least 5. At $7–8, Collection + Lackeys or Experiment when you have 2 Buys and a Collection in play.
  - $4: Tiara once you own a Collection, else Silver. Silos once, with a spare $4 and a Buy around turns 6–9.
  - $3: Experiment. $2: Lackeys (Raze if you're still holding Estates).
  - Grand Market at $6 only with no Copper in play and Collections already secured.
  - Pilgrimage with spare $4 once Collection or Tiara or Platinum is regularly in play. Its every-second activation should copy Collection + Tiara + Grand Market/Platinum.
- **When to score:** immediately and continuously. Every buy of Experiment, Lackeys or Raze with a Collection in play is VP and deck improvement at once, so there's no greening penalty.
  - Spend $11 on Experiments plus Lackeys (7 gains) rather than a Colony whenever you have 2+ Collection plays.
  - Buy Colonies or Duchies only when the Experiment, Lackeys and Raze piles are short, or at the end.
  - Platinum is reasonable at $9+ once the Collection pile is gone. Tiara doubles it to $10.
- **Adapting:**
  - If the opponent opens Collection or Tiara, it's a mirror: race the Collection split, and drain and topdeck the Experiment pile on your turns.
  - If they go Colony money or a Port engine, start ending piles as soon as you lead.

## Endgame and piles

- **Three-pile risk:** this is the main ending.
  - Experiment can be emptied in a single turn (5 buys, $15) and stays empty while the copies sit topdecked.
  - Port takes only 5 buys. Lackeys and Raze are $2 each, and every one is VP for a Collection player.
  - Whoever leads on tokens should count the gains needed to empty Experiment + Port + Lackeys/Raze and end it. The trailing player must avoid draining a third pile.
- **End condition:** piles, not Colonies. A Collection deck can still buy a Colony on a turn when the Experiment pile is empty. Track token totals every turn: they swing by 20+ per turn late.

**Watch out for:** (1) losing the Collection split; (2) an opponent emptying the Experiment pile on their turn, which denies your cheapest VP buy, so have Lackeys, Raze or Port as a fallback; (3) turns without Tiara, where your Experiments go to the discard pile and the loop breaks. Keep 2–3 Tiaras.

## Process notes

- **Files read:**
  - `CLAUDE.md`, `context/rules.md`, `context/strategy.md`, `context/card-power.md`, `context/combos.md`. These came in full through the CLAUDE.md `@` includes in my session context, so I did not reopen them separately.
  - `skills/kingdom-analysis/SKILL.md`.
  - `data/card-glicko/cards.csv` and `data/card-glicko/events-projects.csv` (grep for the board's cards), and `data/card-glicko/FETCHED`. I also listed the `skills/kingdom-analysis/` and `data/card-glicko/` directories.
  - `.../kotw/k3/kingdom.md`, plus `cardtext.py` runs for Platinum, Colony and a "Journey" search. Platinum and Colony came back with no text, so I took their values from rules.md.
- **Where the context was unclear, missing or misleading:**
  - **Glicko priors mislead on this board.** Pilgrimage (−2.14) and Tiara (1.44) are far better here than their ratings. Scholar (−3.22) is correctly weak. The skill says to judge cards by role, which helped, but nothing in the context warns that Treasure multipliers and "copy cards in play" Events scale with Colony/Platinum boards.
  - **VP-per-gain effects are missing from the guidance.** Collection-style token scoring (Goons, Collection, and similar "per gain" VP) isn't discussed in `strategy.md` or `combos.md`. The greening guidance (when to buy green) doesn't cover VP sources that don't junk the deck, where scoring starts from turn ~6. Adding a line on "VP that doesn't clog the deck changes the greening clock" would help.
  - **Three-pile rules leave out a subtlety.** `rules.md` doesn't mention that self-returning cards (Experiment, Horses in reverse) still leave their pile empty while they sit in decks, which matters for three-pile counting and denial here.
  - **The draw definition is too narrow here.** `strategy.md`'s definition of "draw" is good, but it doesn't mention topdecking gains (Tiara) as a draw source. On this board that's the main way to draw your deck.
  - **The skill doesn't cover Treasure multipliers.** The Payload ceiling question could prompt checking Treasure multipliers (Tiara, Crown, Capitalism) as well as Action multipliers.
- **Harness note:** writing `analysis.md` was blocked by the subagent harness ("Subagents should return findings as text"), so this content is returned inline for the caller to save.
- No network access was used.