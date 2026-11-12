**Summary**
1. Recommended plan: a Village Green + Barge engine, thinned by Steward and Way of the Goat, built by Lurker pairs, paid off by Courtier, with one Displace turning Golds into Provinces.
2. Openings: 4/3 is Steward + Silver; 5/2 is Courtier + Lurker (Steward at the next $3).
3. Key interactions: Courtier revealing Village Green (3 types) gives +1 Action, +$3 and a Buy or a Gold; two Lurker plays gain any $5 Action without a Buy.
4. Displace turns a Gold into a Province, and any later Gold gain brings the Exiled Golds back; Cardinal backfires on this board because its discard triggers Tunnel and Village Green and Exiling green cards helps the victim.
5. Main risks: Village Green is the only village (10 copies), every draw and payload piece costs $5, and Lurker makes a three-pile ending real in a mirror.

Confirmation: I used no network access and no ratings. I did not open `data/card-glicko/` and did not reason from any tier list. All turn numbers below are my rough estimates, not simulated.

---

**Board summary:** Trashing is decent (Steward two at a time, Way of the Goat one per Action play, Displace as an Exile-remodel). There is no junking; the only attack, Cardinal, is weak and often helps the victim here. Real draw exists only as Village Green + Barge, and the payload ceiling is well above one Province per turn: about $16–18 with two or more Buys plus a Displace Province. No combo from `context/combos.md` is present (Mandarin is here without Capital).

| Card | Cost | Role | Notes |
| --- | --- | --- | --- |
| Village Green | $4 | deck control: village (Duration, Reaction) | The only village; 10 copies, contested. "Next turn" mode gives a 6-card, 3-Action start. Three types, so it is the best Courtier reveal. If Gamble or an opponent's Cardinal discards it, you may play it. Build-around piece. |
| Barge | $5 | both: terminal draw (+3) and +Buy | Net draw only with Village Green. "Next turn" mode gives an 8-card hand without spending that turn's Action, so it also works with no village. Two types for Courtier. Build-around piece. |
| Courtier | $5 | payload: +$3, +Buy, Gold gain | Reveal Village Green: +Action, +$3, and +Buy or Gold. Reveal Barge or Cardinal: +Action, +$3. Reveal Tunnel: +$3 and a Gold. Reveal a Treasure: plain terminal +$3. Main payload. |
| Lurker | $2 | payload (builder): gainer, pile control | Two plays gain one Action from the Supply (any $5) with no Buy, and it keeps your Action. Not a cantrip: it is a stop card. Played as Goat it loses its +Action. Either player can gain what you trashed. Support, but it sets the build rate. |
| Steward | $3 | deck control: trashing (2), flexible +2 Cards or +$2 | Fastest thinner on the board; opening priority. Terminal. |
| Displace | $5 | both: thinning by Exile, plus gaining up to +$2 | Gold → Province. Estate → Village Green or Silk Road, keeping the Estate's 1 VP. Tunnel or Silk Road → Duchy, keeping their VP. Exiled Golds return when you gain any Gold. Terminal. Closer. |
| Mandarin | $5 | payload: terminal +$3 | Must topdeck a card, which is harmless if you then draw it. Gained via Lurker in the Action phase, its on-gain does nothing. Enables Gamble tricks. Courtier is better here. |
| Cardinal | $4 | payload: terminal +$2, weak attack | The victim chooses what to Exile, Exiled cards still score, and they return on the next gain of that name. Its discard can trigger the victim's Tunnel (Gold) or Village Green. Mostly a terminal Silver; skip unless the opponent is a thin engine or pure Silver/Gold money. |
| Tunnel | $3 | payload: 2 VP, Gold on discard | Discard sources are few: Gamble (top of deck, settable by Mandarin) and an opponent's Cardinal. Its main use is as Courtier's two-type reveal. Dead in an engine. |
| Silk Road | $4 | payload: alternative VP | 1 VP per 4 Victory cards; I assume Exiled Victory cards count. Beats a Duchy only at 16 or more Victory cards. An endgame pickup, not a plan. |
| Gamble (Event) | $2 | payload: +Buy, small sift | Plays the top card if it is an Action or Treasure, without using an Action. Discards a topdecked Tunnel for a Gold. Supplies +Buy to decks without Barge or Courtier. |
| Way of the Goat (Way) | – | deck control: trashing | Any Action can trash one card from hand instead of its text. Use spare Lurkers, Stewards or Village Greens on Coppers. |

### Candidate strategies

1. **Village Green / Barge engine with Courtier, Lurker and Displace**
   - How it works: Steward and Goat thin the deck; Village Green + Barge draw it; Lurker pairs add a $5 per turn on top of your buys. A built turn has 3 Courtiers revealing Village Green or Barge ($9) plus Golds and leftover Treasure for $16+ with Buys from Barge and Courtier, and Displace turns a Gold into a third Province. Surplus Village Greens and Barges go to "next turn" mode to guarantee the next start.
   - Needs: Steward by turn 2, down to about 4 Coppers by turn 7–8; at least 4 Village Greens, 3–4 Barges, 2–3 Courtiers, 3–4 Lurkers and 1 Displace by about turn 12. That is roughly 15 gains, so Lurker pairs and extra Buys are required.
   - Weaknesses: every draw and payload piece costs $5; the single village pile is contested, and an opposing Lurker can trash or take Village Greens; Lurkers are stop cards; an opponent's Cardinal Exiles parts until you regain a copy; it scores nothing before about turn 12.

2. **Barge Big Money (Barge as the X, with a Courtier)**
   - How it works: 2 Barges, 1 Courtier, then Treasure and green on the standard money priorities. Use Barge's "next turn" mode when it collides with another terminal. Barge's Buy, or Gamble at $10, adds a Duchy or Estate late.
   - Needs: $5 by turns 3–5. It contests no scarce pile.
   - Weaknesses: capped at about one Province per turn; has no answer to an engine taking 2–3 per turn; Cardinal Exiles its Silvers and Golds until it buys that Treasure again.

3. **Good-stuff: Courtier / Tunnel / Displace with Barge and Gamble**
   - How it works: no village. Barge in "next turn" mode makes 8-card hands so pairs line up: Courtier + Tunnel gives +$3 and a Gold, and Displace + Gold gives a Province with the Golds returning on the next Gold gain. Late, Displace turns Tunnels and Silk Roads into Duchies while they keep scoring. Mandarin topdecking a Tunnel or a stranded terminal, then Gamble, is an optional extra.
   - Needs: 2 Courtiers, 2 Barges, 1–2 Displaces and 3–4 Tunnels; one terminal per turn.
   - Weaknesses: collision-dependent and high variance; Tunnels are dead cards when they miss; terminal collisions with no village; still about 1–2 gains per turn.

A Tunnel / Silk Road slog is not a candidate. There is no cheap Victory gainer and too little +Buy to reach the 16–20 Victory cards that make Silk Road pay, and no junking to slow the opponent down.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| 1. Engine | ~T12–13 | ~T16–18 on Provinces or piles | 2 Provinces + a Displace Province (12–18) | All Provinces and Duchies; controls the ending |
| 2. Barge money | ~T9–10 | Not alone before ~T22+; 4 Provinces by ~T15 | One Province, sometimes plus a Duchy or Estate | About half the Provinces plus Duchies |
| 3. Good-stuff | ~T7–8 (Tunnels) | ~T20+; 4 Provinces and 3–4 Tunnels by ~T15–16 | Province + a Displace gain (9–12) on good turns | Provinces, 16 VP of Tunnels, Duchies, late Silk Roads |

| You \ Opponent | 1. Engine | 2. Barge money | 3. Good-stuff |
| --- | --- | --- | --- |
| 1. Engine | Even: the Village Green split and Lurker tempo decide it; three-pile threat | Favored: 2–3 Provinces per turn from ~T13 beats one per turn, if online by T13 | Slightly favored: steeper curve and pile control, but it scores earlier, so don't stall |
| 2. Barge money | Unfavored: no way to stop double-Province turns; one Cardinal helps a little | Even: the Cardinal exchange and shuffle luck decide it | Slightly unfavored: it gets the same Provinces plus Tunnel VP and Displace gains |
| 3. Good-stuff | Slightly unfavored: must hold a lead through about T14 | Slightly favored: extra VP from Tunnels and Displace | Even: Tunnel split and Courtier collisions; Cardinal backfires |

**Robust vs. fragile:** The engine is the most robust plan as long as you secure at least 4 Village Greens. Its fragile point is that pile. It shares Courtier, Barge and Displace with the good-stuff deck, so if the village split goes badly you can stop buying villages and continue as plan 3. Barge money is safe but capped and loses to a competent engine. Good-stuff is a sound fallback with high variance.

**Recommendation:** Build the engine. The board passes the engine tests in `context/strategy.md`: real draw with a working village, fast enough thinning, payload beyond one Province per turn, and Lurker offsetting the $5 prices. I would pick the same plan against a strong or an unknown opponent. Against a strong mirror, take Village Greens earlier and never leave a Lurker-trashed $5 in the trash when the opponent holds Lurkers.

What flips it:
- With 3 or more players, the 10 Village Greens split too thin and the game is shorter per player, so play good-stuff.
- If the opponent takes 6 or more Village Greens or keeps trashing them, pivot to plan 3.
- A 5/2 opening without Steward slows thinning but does not change the plan.

**Open:** 4/3: Steward + Silver — trashing first, and Silver reaches the first $5. · 5/2: Courtier + Lurker — Courtier's +$3 buys the next $5s and Lurker starts the trash-and-gain cycle. Add Steward at the first $3–4 and use Goat on spare Actions.

**Buy priority, shuffles 2–4:**
1. On Steward turns, trash two cards (Estates first, then Coppers down to about 3–4). Spend a leftover $2–3 on a Lurker, up to 3–4.
2. At $5, take Courtier first, then Barge, then alternate to 3–4 Barges and 2–3 Courtiers.
3. At $4, take Village Green, keeping villages at or above the number of Barges plus other terminals.
4. Use Lurker pairs to trash and gain a $5 in the same turn where possible.
5. Add one Displace once Courtier is producing Golds (Estate → Village Green before then if you still have Estates).
6. Skip Tunnel, Silk Road, Mandarin and Cardinal while building.

**Greening:** Start when the deck makes about $16 with two Buys, or $13 plus a Displace on a Gold. Green earlier in a mirror, once about 4 Provinces remain. Late on, Silk Road beats a Duchy only at 16 or more Victory cards.

**Endgame and piles:** Lurker can trash only Action piles. In a mirror, Village Green and Lurker both run out, and Barge or Courtier at 6–8 taken can be finished by Lurker trashing, so count the opponent's Lurker plays each turn. Use the same threat yourself when ahead. The usual Province-count rules apply.

**Watch out for:**
- The Village Green split: fewer than 4 means stop adding terminals and go good-stuff.
- An opponent's Cardinal: regain any Exiled part by gaining another copy (Lurker does this without a Buy), and don't buy Cardinal yourself against a Tunnel or green-heavy deck.
- Over-thinning below the money needed for $5, and Lurker clog before the draw can carry it.

## Process notes

**Files read**
- `/home/imalison/projects/dominion-agents/skills/kingdom-analysis/SKILL.md`
- `/tmp/claude-1000/-home-imalison-projects-dominion-agents/a631d71b-c39f-4667-8a5e-fd864af8e735/scratchpad/abl/k6/kingdom.md`
- `CLAUDE.md`, `context/rules.md`, `context/strategy.md`, `context/card-power.md` and `context/combos.md` were already inlined in full in my context, so I did not reopen them.
- I did not run `cardtext.py`; the kingdom file and `rules.md` covered every card I needed. Nothing was written.

**Blindness caveat**
- `CLAUDE.md` auto-inlines `context/card-power.md`, so its "Headline picture" tier lists were in my context even though ratings were withheld. None of this kingdom's cards or landscapes appear in those lists, and I did not use them.

**Where the repo was unclear or missing something**
- `rules.md` on Exile says Exiled cards "still score" but not whether they count as cards you have for counting effects such as Silk Road. I assumed they do. It also doesn't say that reclaiming Exiled copies is all-or-nothing per name.
- `rules.md` on Ways doesn't say the Way replaces the whole text (so Lurker as Goat loses its +Action), or what happens to a Duration played as a Way.
- `rules.md` on reshuffling lists "draw, reveal or look at" but not discarding from the deck (Gamble on an empty deck). I assumed it reshuffles.
- `rules.md` has nothing on Reactions that play themselves outside your turn (Village Green discarded by Cardinal), on Durations with a "now or next turn" choice, or on cards played by an Event in the Buy phase not costing an Action.
- `strategy.md` names only hand discarders and Militia for Tunnel. It doesn't mention top-of-deck discards (Gamble, Cardinal) or topdeckers (Mandarin) as enablers.
- `strategy.md`'s engine test "pieces affordable: not all at $5+" gives no guidance on how a gainer like Lurker changes that. This board is borderline on that test.
- `strategy.md` has no note that "choose which to Exile" attacks backfire against green-heavy decks; its attack section covers junking, handsize and trashing attacks only.
- The skill's output format has no slot for buy priorities, greening timing or the endgame, although steps 9–10 require them. I added those lines. "Watch out for: 1–3 risks" is also tight when a board has both pile and attack risks.
- The skill's step 2 rating lookup was skipped as instructed. The skill has no "ratings unavailable" branch.
- The skill doesn't prompt counting card types, which matters for Courtier; a line under "Inventory" for type-count or name-count payoffs would help.