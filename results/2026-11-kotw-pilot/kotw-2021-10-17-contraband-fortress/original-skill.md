I couldn't save the analysis: the Write tool blocked `/tmp/claude-1000/-home-imalison-projects-dominion-agents/a631d71b-c39f-4667-8a5e-fd864af8e735/scratchpad/kotw/k2/analysis.md` with "Subagents should return findings as text, not write report files". I didn't try to get around that block, so the file doesn't exist. Please save the text below to that path.

**Summary**
1. **Plan:** a Scrying Pool / Fortress / Monument engine (Hermit making Madmen, Hunting Grounds for draw past the Coppers, Contraband as the only +Buy) that cashes out in Vineyards plus Provinces.
2. **Openings:** 4/3 Potion/Hermit. 5/2 Potion/nothing, since no Kingdom card costs $2 and Copper clogs Scrying Pool.
3. **Key interaction:** every Action you add makes Scrying Pool draw more and makes each Vineyard worth more. At 21–24 Actions a Vineyard is worth 7–8 VP for one Potion, and a money deck can't use them.
4. **Matchups:** Big Money + Hunting Grounds loses to this engine. In an engine mirror, the split of the 8 Vineyards and the Monuments decides it. Contraband lets the opponent ban one card, so keep two things worth buying (Province and Vineyard).
5. **No network access:** I used no web search, fetch, browser or curl, and read only the repo, `cardtext.py` and the k2 directory.

---

# Kingdom analysis: Contraband, Fortress, Golem, Hermit, Hunting Grounds, Monument, Quarry, Sage, Scrying Pool, Vineyard

Setup: 2 players, Shelters (Necropolis is an Action village; Hovel and Overgrown Estate are non-Actions), Potion in the Supply, no Colonies. Non-Supply: Madman (10, via Hermit). No landscapes. Vineyard pile is 8 (2p). Contraband is a **first-edition-only** Prosperity card.

**Board summary:** No junking attack, and the only trasher (Hermit) can't touch Treasures, so every deck keeps its 7 Coppers. Real draw exists: Scrying Pool is non-terminal draw in an Action-dense deck, Fortress/Necropolis/Madman are villages, and Hunting Grounds is terminal +4 that draws past the Coppers. The only +Buy is Contraband, and the opponent names a card you can't buy that turn. The payload ceiling is still high: Monument gives $2 and +1 VP per play, and Vineyard is the outlier. In an engine with 21–24 Actions, each Vineyard is worth 7–8 VP (more than a Province) for just a Potion, and a money opponent can't use them. Plan: a Scrying Pool / Fortress / Monument engine that cashes out in Vineyards plus Provinces.

## Roles

| Card | Cost | Role | Notes |
| --- | --- | --- | --- |
| Scrying Pool | $2P | both: non-terminal draw + mild attack | Glicko 3.05 (top ~12%). Each Pool draws a run of Actions and stops at the first non-Action, so it draws about 1 Copper per play. Before drawing, you may discard your own top card (skip a Copper or Vineyard). The attack lets you discard the opponent's top Action or leave their junk on top. Centerpiece. |
| Hermit | $3 | both: shelter trasher + $3 gainer; makes Madman | Glicko 3.68, the strongest card on the board, but its trashing is weak here: non-Treasures only, so just Overgrown Estate (+1 Card when trashed) and Hovel. Its real jobs: gain a $3 card each play (Hermit or Sage for Action count), become a Madman on turns you don't buy, and trash Hunting Grounds for a Duchy late. |
| Madman | (non-Supply) | deck control: village + burst draw | +2 Actions, then +1 Card per card in hand. Played after a Scrying Pool chain, it roughly doubles your hand. A one-shot that returns to its pile. |
| Fortress | $4 | deck control: village | Glicko 2.06. Plain village (+1 Card +2 Actions) and an Action, so Pools draw through it. Its on-trash text barely matters, since Hermit's trash is optional and no other card forces a trash. |
| Necropolis | starter | deck control: village | A free +2 Actions Action that Pools draw through. Keep it; don't trash it with Hermit. |
| Hunting Grounds | $6 ($4 w/ Quarry) | deck control: terminal draw; later payload (VP) | +4 Cards draws past the Coppers that stop Pools. Late, Hermit can trash one from your discard pile for a Duchy or 3 Estates. Glicko 0.60. |
| Monument | $4 ($2 w/ Quarry) | payload: $2 + VP token | Glicko −2.12 on average, but strong here: an engine plays 3–4 a turn, it's an Action (doesn't stop Pools) and it counts for Vineyard. It's the main $ payload. |
| Contraband | $5 | payload: $3 + the only +Buy | The opponent names one card you can't buy, and **each** Contraband you play gets its own name. Play the first, see the name, then decide whether to play the second. Non-Action, so it stops Pools. 1st-ed only. Glicko −3.29. |
| Vineyard | $0P | payload: alt VP | 1 VP per 3 Actions you own. In a 21–24-Action engine it's worth 7–8 VP. It's a non-Action, so buy it late. The pile of 8 can be one of three empty piles. Glicko 0.64. |
| Potion | $4 | payload/enabler | Needed for every Pool and Vineyard. Plan on 2, maybe 3 late (one per Vineyard you buy each turn). |
| Quarry | $4 | payload: cost reduction | Actions cost $2 less this turn: Fortress $2, Monument $2, HG $4, Pool $0P, Hermit/Sage $1. Useful with Contraband in the build phase, but it's a $1 non-Action that stops Pools. 0–1 copies. Glicko 0.82. |
| Sage | $3 | deck control: weak sifting cantrip | Skips cards that don't cost $3+, so it discards Coppers. Under a strict reading it also discards Scrying Pools and Vineyards (see Process notes). It's cheap Action count for Vineyard and nothing more. Glicko −4.00. |
| Golem | $4P | neither (weak) | Plays 2 Actions but discards the Coppers and Potions it passes. It competes with Pools for Potions. Skip. Glicko −3.81. |
| Hovel / Overgrown Estate | starters | dead | Hovel trashes itself when you gain a Victory card (e.g. a Vineyard) with it in hand. Hermit trashes Overgrown Estate for +1 Card. |

Built around: Scrying Pool (with Vineyard as the cash-out). Support: Fortress, Monument, Hermit/Madman, Hunting Grounds, Contraband.

### Interactions that matter

- **Scrying Pool + Action density + Vineyard.** Every Action you add makes Pools draw more and makes every Vineyard worth more. Fortress, Monument, Hermit, HG and Necropolis are all Actions. This is the board's defining synergy.
- **Hermit → Madman → Scrying Pool.** On a build turn with nothing good to buy, play Hermit (gain a Hermit or Sage) and skip the buy to get a Madman. Later, play the Madman after a Pool chain to draw much of the rest of your deck.
- **Hermit + Hunting Grounds (endgame).** Hermit trashes a Hunting Grounds from your discard pile → Duchy (or 3 Estates), and Hermit itself gains an Estate. That's 4 VP from one terminal play, and the 3-Estate mode drains the Estate pile, which is a three-pile lever.
- **Quarry + Contraband.** $4 with 2 Buys and Actions $2 cheaper, e.g. HG + Fortress, or Fortress + Monument. Good during the build. The opponent's name only removes one target.
- **Contraband vs. a two-target payload.** Late, you want Provinces *and* Vineyards. With one Contraband the opponent bans one and you buy the other in bulk. Against a single-target plan, Contraband's +Buy is nearly worthless.
- **Anti-synergy:** Hermit can't trash Copper, so Coppers stay as both your base money and the cards that stop Pools. Hunting Grounds and Madman handle them. Golem and Sage throw away money or Pools.
- No combo from `context/combos.md` is on the board. Hunting Grounds is here, but Lurker isn't, and Hermit can't trash from the Supply.

## Gate questions

1. **Trashing:** weak. Hermit removes 2 shelters at most, and there's no Copper trashing.
2. **Junking:** none. Scrying Pool's attack is mild top-card control.
3. **Draw:** yes. Scrying Pool (non-terminal once Actions dominate), Fortress, Necropolis and Madman as villages, and Hunting Grounds as terminal +4 behind them. With ~4 Pools, 2 HG, 3 Fortress, Necropolis and ~12 non-Actions, a hand draws ~20–25 cards, close to the whole deck, by ~T11–12.
4. **Payload ceiling:** 7 Copper + 2 Contraband + 4 Monument ≈ $21, 2 Potions, 3 Buys, +4 VP tokens. That's two Provinces + Duchy, or two to three Vineyards + a Province-sized buy, depending on what the opponent bans: ~15–20 VP per turn.
5. **Outliers:** Vineyard at 7–8 VP each, uncontested if the opponent plays money. Monument VP tokens. Hermit/HG Duchy conversion.
6. **Scoring routes and piles:** Provinces (8), Duchies (8), Estates (8), Vineyards (8), Monument tokens (pile of 10), Duchies/Estates from trashing HG. The piles likely to empty are Vineyards, then Monuments or Duchies. Estates are possible via Hunting Grounds.

## Candidate strategies

1. **Scrying Pool / Fortress / Monument engine → Vineyards + Provinces (B).** *Deck control:* 4–5 Scrying Pool, 3 Fortress + Necropolis, 2 Hunting Grounds, Hermit (→ Madman). *Payload:* 3–5 Monument, 1–2 Contraband, 2–3 Potion, then Vineyards. Good turn: a Fortress/Pool chain, HG and Madman to draw past the Coppers, play 3–4 Monuments, then $18–21 with PP and 2–3 Buys: Province + Province + Duchy if they ban Vineyard, or 2 Vineyards + Duchy/Province if they ban Province. *Needs:* Potion by T2, 2 Pools by ~T6, 3 villages and 1–2 HG by ~T9, Contraband and a second Potion by ~T10. Count Actions toward 21+ by the end. *Weaknesses:* Pools whiff when Coppers bunch. You can't thin, so it relies on HG and Madman. You need many Potion-turns. In a mirror, the Vineyard split (8) decides a lot.
2. **Fortress / Hunting Grounds / Monument engine, no Alchemy (C).** The same skeleton without Potion: Fortress villages, 3 HG for draw, Monument and Contraband as payload, Provinces + Duchies + tokens. It's about a turn faster to set up, since there's no Potion dead card, but HG is terminal and $6, the deck is less consistent, and it gives up the Vineyard ceiling.
3. **Big Money + Hunting Grounds (A).** The baseline: 1–2 HG, Gold, Silver, maybe one Contraband as Gold-with-a-Buy. ~4 Provinces by T15–16, and ~T21–23 to empty Provinces alone. Simple, but it can't use Vineyards, and a Monument engine outscales it.
4. **Vineyard pile-up without draw (D).** Hermit gains Hermits/Sages, and Quarry + Contraband buys cheap Actions (Sage/Hermit $1, Fortress/Monument $2), plus Potions for 1 Vineyard a turn. ~18 Actions → 6 VP Vineyards. Slow (one Vineyard per Potion-turn) and no draw, so it's fragile. Any engine opponent contests the Vineyards.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| B: Pool engine → Vineyards | tokens ~T7–9; big buys ~T11–12 | ~T16–18 (Provinces, or Vineyards + Monuments/Duchies) | ~15–20 (2 Prov + Duchy + tokens, or 2–3 Vineyards + more) | Most Provinces + all 8 Vineyards vs money (~50 VP) + tokens |
| C: Fortress/HG engine | ~T10–12 | ~T17–19 | ~12–16 (2 Prov + tokens) | Provinces + Duchies + tokens |
| A: BM + HG | ~T8–10 | ~T21–23 alone | ~6 (Province every other turn, rising slightly) | about half the Provinces + Duchies |
| D: Vineyard pile-up | ~T9–10 | ~T20+ | ~6–7 (one Vineyard) + tokens | 8 Vineyards × ~6 + tokens, if uncontested |

## Matchups

| You \ Opponent | A: BM+HG | B: Pool engine | C: Fortress/HG engine | D: Vineyard pile-up |
| --- | --- | --- | --- | --- |
| **A: BM+HG** | even | unfavored: B scores twice as fast from T12 and owns the Vineyards | unfavored: C double-Provinces by ~T13, and A can't end the game before ~T21 | even: D is slow, but A can't touch Vineyards |
| **B: Pool engine** | favored: 8 uncontested Vineyards (~50 VP) plus tokens; A can't shorten the game | even: Vineyard and Monument splits decide it; Pool attack and Contraband bans matter | favored: same speed, higher ceiling, takes the Vineyards C can't buy | favored: draws more and wins the Vineyard race |
| **C: Fortress/HG engine** | favored | unfavored: loses the Vineyard VP and ends up a turn or two short | even | favored |
| **D: Vineyard pile-up** | even | unfavored | unfavored | even |

**Robust vs. fragile:** B is robust: it beats money, beats the no-Potion engine, and is even in the mirror. C is decent but worse than B in every column. A and D are fragile: A only works against slow decks, and D only if nobody contests Vineyards.

**Recommendation:** Build the Scrying Pool / Fortress / Monument engine with Hermit for Madmen, HG for draw past Coppers, and Contraband as the only +Buy. Cash out in Vineyards plus Provinces. Against money, take all 8 Vineyards at leisure and Monument every turn. Money's clock (~T22) is far too slow. Against an engine mirror, start Vineyards ~1–2 turns earlier and get a third Potion, since the 8-card pile splits. Keep Duchies and Hermit→HG as your three-pile lever. The pick doesn't change against a weak or unknown opponent.

**Open:** 4/3: **Potion / Hermit**. The Potion means Scrying Pool on T3/T4 with just $2, and Hermit trashes Overgrown Estate/Hovel and gains an Action (Hermit) every play. 5/2: **Potion / nothing**. There's no Kingdom card at $2, and Copper only clogs Pools. Contraband/nothing is an acceptable alternative that delays the Potion. Don't open Fortress (a plain village) or Quarry.

**Buy priorities:**
- *Shuffles 2–3 (T3–8):* Scrying Pool at $2P (first priority on Potion turns). Hunting Grounds at $6. Fortress at $4 (ahead of Monument until you have ~2–3 villages incl. Necropolis). Contraband at $5. Hermit at $3. With Hermit and no good buy, skip the buy and take a Madman.
- *Shuffle 4+ (T9–12):* a second Potion. Monuments (aim 4–5). A second HG. Pools to 4–5. Keep villages ≥ terminals: count HG, Monument and Hermit as terminals; Fortress, Necropolis and Madman as villages.
- *Greening ~T11–13*, once you reliably hit $16+ with 2 Buys. Vineyards on every Potion you don't need for a Pool, Provinces otherwise. Monument tokens accrue from ~T7 onward.

**Adapting:** If the opponent opens Potion too, it's a mirror. Contest Pools early and start Vineyards sooner. On their Pool plays, discard your top Action if you can; with your Pools, leave Coppers and Vineyards on top of their deck. When they play Contraband, name what they need most: early their key engine piece, late Vineyard if they hold Potions, else Province. If they go money, slow down, build a bigger engine, and take every Vineyard.

## Endgame and piles

- **Three-pile risk:** Vineyards (8) are likely to empty, Monuments (10) maybe. Duchies (8) and Estates (8) can be pushed by Hermit trashing HG ("3 Estates" + Hermit gaining an Estate = 4 Estates per play). Only an engine with Contraband buys can drive a three-pile, so the engine player controls the ending. Money can't threaten one.
- **End condition:** usually Vineyards + Duchies/Monuments run low as the Provinces go. Count Vineyard value (Actions ÷ 3) each turn. Late Duchies don't add Actions, so a Monument can be worth more than a Duchy for its token, its $2 and Vineyard count.
- Hovel: buy a Vineyard or Duchy with Hovel in hand to trash it for free.

**Watch out for:**
1. Too many non-Actions (Contraband, Quarry, Potions, early Vineyards) stalling your Pools. Lean on HG and Madman, and hold Vineyards until the deck draws itself.
2. Contraband bans. Have two payload targets (Province + Vineyard), and don't play a second Contraband unless you need the Buy.
3. An engine mirror racing the Vineyard split. Buy the third Potion earlier and start Vineyards at ~T10.

## Process notes

Files read:
- `/home/imalison/projects/dominion-agents/CLAUDE.md`, `context/rules.md`, `context/strategy.md`, `context/card-power.md`, `context/combos.md` (already loaded into my context), `skills/kingdom-analysis/SKILL.md`
- `data/card-glicko/cards.csv` (grep for the 10 kingdom cards and Potion-cost cards), `data/card-glicko/FETCHED`
- `.../scratchpad/kotw/k2/kingdom.md`, plus `cardtext.py "Estate"`

No network access was used.

Where the repo context was unclear, missing or misleading:
- **Potion-cost comparisons:** `rules.md` says "A card's cost can be compared with another's only when both have the same components." Taken literally, Golem ($4P) isn't "$3 or more" for Sage. As I understand the official rule, costs compare component-wise, so $4P > $3, but $2P vs $3 is incomparable. Sage's interaction with Scrying Pool and Vineyard hinges on this. The wording should be checked and tightened.
- **Opening with no $2 card:** the skill requires a 5/2 opening, but `strategy.md` has no guidance for boards with no useful $2 card, or for Potion openings (Alchemy) in general.
- **Contraband:** nothing in the repo covers how naming plays out (one name per Contraband, playing Treasures one at a time). I reasoned it from card text.
- **Alt-VP valuation:** `strategy.md` names Gardens/Duke but gives no rule of thumb for valuing a Vineyard-type card against Provinces as the deck grows. I estimated it.
- **Dark Ages rules:** `rules.md` doesn't say how big the Madman pile is (I assumed 10), or that "gain a card costing up to $3" excludes Potion-cost cards. It does state the latter in general terms.
- **Glicko:** non-Supply cards (Madman) have no rating. Fine, but worth noting.
- **Saving the analysis:** the harness blocked writing `analysis.md` because subagents may not write report files, so the analysis had to be returned as text.
- The skill procedure and output format were clear and sufficient otherwise.