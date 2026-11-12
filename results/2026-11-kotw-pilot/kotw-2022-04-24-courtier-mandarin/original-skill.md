I couldn't save `analysis.md`: the Write tool refuses report files from subagents. I didn't try to get around that, so `/tmp/claude-1000/-home-imalison-projects-dominion-agents/a631d71b-c39f-4667-8a5e-fd864af8e735/scratchpad/kotw/k6/analysis.md` doesn't exist. The full analysis is below for you to save at that path.

**Summary**
1. **Recommended plan:** build an engine on Village Green and Barge with Steward trashing. Courtier is the main payoff and Displace finishes the game. I rate it favored over Big Money + Barge and over a Tunnel/Silk Road green-money plan.
2. **Openings:** on 4/3, Steward/Silver (Steward/Cardinal is acceptable going first). On 5/2, Displace/Lurker, with Courtier/Lurker close behind.
3. **Key interaction:** Courtier reveals a card without using it up. With one Village Green in hand (three types), every Courtier gives +1 Action, +$3 and a Gold. Displace then turns Golds into Provinces, and the next Gold you gain brings the exiled Golds back.
4. **Other findings:** Displacing a Victory card is pure VP, because the exiled card still scores and still counts for Silk Road. Gamble is the only way to discard your own Tunnels for Gold. Cardinal backfires, since it triggers the opponent's Tunnels and Village Greens. The main risk is a three-pile ending on Tunnel, Silk Road and Duchy.
5. **No network access was used.** I read only the repo files, the kingdom file and the Glicko CSVs.

---

# Kingdom analysis: Barge, Cardinal, Courtier, Displace, Lurker, Mandarin, Silk Road, Steward, Tunnel, Village Green + Gamble, Way of the Goat

2 players, Dominion Online rules. No Colonies, no Shelters. Mandarin and Silk Road are **first-edition-only** Hinterlands cards. The analysis uses the exact text from the kingdom file.

**Board summary:** Trashing is good and early:
- Steward is the highest-rated card on the board (Glicko 3.04).
- Way of the Goat turns any spare Action into a trasher.
- Displace removes cards while gaining others.

There's no junking attack. Real draw exists: Village Green (the only village, +1 Card +2 Actions) and Barge (+3 Cards +1 Buy) are both Durations, with Steward as backup draw.

The interaction that defines the board is **Courtier revealing a card with several types**. One Village Green in hand (3 types) can be revealed by every Courtier, each giving +Action, +$3 and a Gold. Barge and Tunnel have 2 types each. **Displace then converts those Golds into Provinces.** The payload ceiling is about 2 Provinces plus a cheap green per turn once built. Victory cards are unusually cheap and plentiful (Tunnel, Silk Road, Displace on green), so a three-pile ending on Tunnel, Silk Road and Duchy is a real factor.

## Inventory and setup notes
- **Kingdom:** Lurker $2, Steward $3, Tunnel $3 (Victory pile of 8), Cardinal $4, Silk Road $4 (Victory pile of 8, 1st ed.), Village Green $4, Barge $5, Courtier $5, Displace $5, Mandarin $5 (1st ed.).
- **Event:** Gamble ($2, +1 Buy, so it is Buy-neutral).
- **Way:** Way of the Goat (trash a card from your hand).
- **Exile:** comes from Cardinal and Displace. Exiled cards still score, and gaining a copy lets you discard the Exiled copies.
- **Durations:** Barge and Village Green.

## Roles
| Card | Cost | Role | Notes |
| --- | --- | --- | --- |
| Steward | $3 | deck control: trashing / terminal draw; payload: +$2 | Top card on the board (3.04). The opening trasher. |
| Village Green | $4 | deck control: village (Duration) | The only village. Best Courtier target (3 types). Plays itself when discarded. Glicko 1.96. |
| Barge | $5 | deck control: terminal draw; payload: +Buy | Engine draw and main +Buy. Use next-turn mode. 2 types. Glicko 2.61. |
| Courtier | $5 | both: +$3 / Gold / +Buy / +Action | Glicko −0.28 generally, but the centerpiece here. Revealing Village Green gives +Action, +$3 and a Gold. Early it gains a Gold off an Estate or Copper. |
| Displace | $5 | both: remover + gainer | Gold→Province, Estate→Steward or Village Green or Silk Road, Silver→$5, Tunnel or Silk Road→Duchy. Exiled Victory cards still score. Glicko 1.04. |
| Lurker | $2 | payload: 2-step Action gainer | Trashes a $5 from the Supply, then gains it with a later play. The trash is shared with the opponent's Lurker. |
| Cardinal | $4 | payload: +$2, Attack | Weak (−2.26). Courtier decks recover exiled Golds, and its discard helps victims with Tunnels and Village Greens. |
| Mandarin | $5 | payload: terminal +$3; topdeck | Courtier does its job better. Its niche is topdecking a Tunnel for Gamble. |
| Tunnel | $3 | payload: 2 VP, Gold source | Gamble discards it for a Gold. Courtier revealing it gives +$3 and a Gold. Counts toward Silk Road. |
| Silk Road | $4 | payload: alt VP | Likely worth 3–5 VP in green-heavy endgames. Displace and Exile keep its count up. |
| Gamble | $2 | payload: spend surplus $ (+Buy-neutral) | Plays the top card, including Treasures after buying. Plays Barge or Village Green in next-turn mode. Turns a Tunnel on top into a Gold. Weak once an engine draws its deck. |
| Way of the Goat | – | deck control: trashing | Colliding terminals become trashers. |

## Interactions
1. **Courtier + Village Green in hand.** One revealed Village Green powers every Courtier that turn, and you still play the Village Green afterwards.
2. **Courtier Golds + Displace + Exile recovery.** Displace a Gold for a Province. The next Gold you gain returns all the exiled Golds to your deck.
3. **Displace on Victory cards.** It's pure VP gain, and each one adds a Victory card for Silk Road.
4. **Gamble + Tunnel / Village Green / Barge.** Gamble is the only way to discard your own Tunnels.
5. **Cardinal backfires** on Tunnel and Village Green decks.
6. **Lurker** drains Action piles. It can't touch the Victory piles.
7. No combo from `context/combos.md` is present.

## Gate questions
1. **Trashing:** strong (Steward, Goat, Displace).
2. **Junking:** none.
3. **Draw:** each Village Green + Barge pair nets +2 cards with Actions unchanged. Village Green is the only village.
4. **Payload ceiling:** N Courtiers give $3N + N Golds. About 2 Provinces plus extra greens per turn.
5. **Outliers:** the Courtier + Village Green interaction, and cheap, deep VP.
6. **Piles:** Provinces, Tunnels, Silk Roads, Duchies, and Gold in Courtier mirrors (around T17–19).

## Candidate strategies
1. **Courtier engine.**
   - How it works: Steward thins; Village Green and Barge draw; Courtiers reveal Village Green. A built turn is $16–20 with 2–3 Buys, plus Displace for a third Province.
   - Needs: thinned by about T8. 2–3 Village Greens, 2 Barges and 2 Courtiers by T10–11. Wants 3–4 of the 10 Village Greens and 3–4 of the 10 Courtiers, both contested in a mirror.
   - Weaknesses: thin early draw, and Golds can clog it.
2. **Big Money + Barge (+ Courtier).**
   - How it works: Gamble absorbs surplus $, Tunnels are the greening.
   - Weaknesses: one Province per turn.
3. **Green money (Courtier / Tunnel / Silk Road).**
   - How it works: green early on Tunnels and Silk Roads, and threaten a three-pile ending.
   - Weaknesses: slow and short on Buys.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| Courtier engine | ~T11–12 | ~T16–17 | 2 Provinces + Tunnel/Duchy | most Provinces + Duchies + a share of Tunnels and Silk Roads |
| BM + Barge/Courtier | ~T8–9 | ~T20–22 | ~3–4 avg | about half the Provinces |
| Green money | ~T7–8 | ~T18–20 (three piles) | ~4–6 | Tunnels + Silk Roads + Duchies, if uncontested |

| You \ Opponent | Engine | BM | Green money |
| --- | --- | --- | --- |
| Engine | even: the Courtier and Village Green split decides it | favored: no junking, and Golds outscale by T14 | favored: contest the piles, count three-pile gains |
| BM | unfavored | even | even |
| Green money | unfavored | even | even: the Tunnel and Silk Road split decides it |

**Robust vs. fragile:** The engine is robust. BM and green money are fragile against it.

**Recommendation:** Build the Courtier / Village Green / Barge engine with Steward trashing and Displace as the finisher. In a mirror:
- Take 2 Courtiers before a third Barge.
- Keep Village Greens ≥ terminals.
- Green earlier than you would against money.

**Open:** 4/3: Steward / Silver (Steward / Cardinal is acceptable going first). 5/2: Displace / Lurker (Courtier / Lurker is close).

**Buy priorities:**
- $5: Courtier, then Barge, then a second Courtier. Add Displace once you have Golds.
- $4: Village Green.
- $3: a second Steward.
- $2: one Lurker.
- Use Goat on colliding terminals.
- Green at $16 with 2 Buys, around T12.

**Adapt:**
- Against Big Money: skip Cardinal.
- Against Tunnels and Silk Roads: take a share of both piles from around T12 and count three-pile gains.
- In a mirror: prioritize Courtiers and Village Greens, and track the Gold pile.

**Watch out for:**
1. Three-pile endings on Tunnel + Silk Road + Duchy, or Gold in a mirror.
2. Trashed Actions feeding the opponent's Lurker.
3. Recount Silk Road values late in the game.

**Endgame:** Provinces end it, with Duchy, Tunnel and Silk Road dancing. With 3+ players, Victory piles are 12 cards and the Courtier and Gold piles drain faster.

## Process notes
**Files read:**
- Repo: CLAUDE.md and the four context files (inlined), and `skills/kingdom-analysis/SKILL.md`.
- Glicko data by grep: `data/card-glicko/cards.csv`, `events-projects.csv`, `ways.csv`, and `FETCHED`.
- Kingdom: `k6/kingdom.md`. `cardtext.py` wasn't needed.

**Gaps or misleading points in the repo:**
- rules.md doesn't say that Gamble's "you may play it" overrides the rule against playing Treasures after buying. I assumed it does.
- rules.md doesn't say whether Exiled cards count for Silk Road. I assumed yes.
- Playing a Duration on another player's turn (Village Green discarded by Cardinal) isn't covered.
- How Courtier counts types (Duration and Reaction count) isn't explained.
- The Glicko priors mislead here. Courtier, Tunnel and Silk Road are much better on this board, and Cardinal is worse. Mandarin and Silk Road are unranked "deprecated" entries.
- strategy.md's "opening a plain village is almost never right" is ambiguous for a village like Village Green.
- The skill has no step for Exile mechanics or for cheap Victory piles as a three-pile risk.