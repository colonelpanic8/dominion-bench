I couldn't save the analysis: the harness refused to let a subagent write `/tmp/claude-1000/-home-imalison-projects-dominion-agents/a631d71b-c39f-4667-8a5e-fd864af8e735/scratchpad/kotw/k1/analysis.md`. I didn't try another way around that block. The full analysis is below for you to save there.

**Summary**
1. **Plan:** a Tunnel Gold flood cashed in by Butcher. Embassy and Night Watchman discard Tunnels to gain Golds. Each Butcher play turns a Gold into a Province for no net Coffers ($6 plus the 2 Coffers it gives = $8).
2. **Openings:** Cursed Gold makes the turn 1–2 total $9 (5/4 about 41%, 6/3 48%, 7/2 12%), so 4/3 and 5/2 never come up. Open Embassy/Tunnel on 5/4 or 6/3, and Embassy with nothing (or Faithful Hound) on 7/2. Then add the first Butcher, 2 Night Watchman and 3–5 Tunnels.
3. **Key interaction:** Tunnel with Embassy and Night Watchman makes Golds; Butcher turns Gold into Province. Tower also counts Curses, and the 10-Curse pile (2p) will often empty from Cursed Gold and Ritual, which refunds each held Curse. A Fool's Gold player who takes most of the 10 can get up to +10 VP from Tower; buying 2–3 cheap ones counters it.
4. **Rejected:** the City Quarter engine is too slow (8D per copy, weak thinning, only terminal draw). Fool's Gold + Tower is fragile because the opponent can split the bonus for $2 a card. Embassy Big Money is the baseline and plan 1 beats it.
5. **Blindness:** I used no network access (no WebSearch, WebFetch, browser or curl). I read only the repo, `cardtext.py` and the k1 directory.

---

# Kingdom analysis: Butcher, City Quarter, Embassy, Faithful Hound, Fool's Gold, Merchant Guild, Night Watchman, Nomad Camp, Pooka, Tunnel · Ritual · Tower

2 players, Dominion Online. No Colonies, no Shelters. Every player starts with **Cursed Gold** in place of one Copper (Pooka's Heirloom). Embassy and Nomad Camp are **first-edition-only** cards.

**Board summary:** There's no Attack, and the only real trashing is Butcher (a remodel) and Pooka (Treasures only), so this is a race. The engine pieces are weak: City Quarter (8D) is the only village, and all the draw is terminal (Embassy, Pooka, Faithful Hound). The board's strength is **discard-for-benefit**. Tunnel gains a Gold when discarded, Embassy discards 3 from hand, and Night Watchman discards from the top of your deck as a non-terminal Night card. Together they make a Gold flood, and **Butcher cashes each Gold in for a Province at no net cost**. The payload ceiling is about 1 Province per turn, plus a second via Butcher, plus Tunnel VP. Two side rules matter. **Cursed Gold makes every opening total $9**, so every split includes a $5+ hand. And **Tower counts Curses** (they're non-Victory). The 2p Curse pile is only 10 and will often empty, which refunds +1 VP per Curse held.

| Card | Cost | Role | Notes (Glicko prior) |
| --- | --- | --- | --- |
| Butcher | $5 | both: remodel/trasher + Coffers | **Centerpiece.** Gold→Province free. Estate→Tunnel (1 Coffer). Curse→FG/Hound. Cursed Gold→Gold (2 Coffers). Otherwise bank Coffers. (3.71) |
| City Quarter | 8D | deck control: village + draw | Only village. Needs action-dense hands and costs a turn of debt per copy. Under-supported here. (3.66) |
| Embassy (1E) | $5 | deck control: terminal draw/sifter | **Key Tunnel enabler.** Sifts Curses and Estates. Gifts the opponent a Silver. (−1.59) |
| Night Watchman | $3 | deck control: non-terminal sifter | **Second Tunnel enabler.** Gained to hand, works that night. Stacks FGs and dumps Curses. (−3.00, much better here) |
| Tunnel | $3 | both: 2 VP + Gold when discarded | "Green that makes Gold." 8 in the pile, contested. (−1.71) |
| Merchant Guild | $5 | payload: +Buy, +$1, Coffers per Buy-phase gain | Late +Buy for Province + Tunnel/Ritual/Duchy. (1.34) |
| Nomad Camp (1E) | $4 | payload: +$2 +Buy | Gained onto deck, so a turn-1 buy is played on turn 2. Terminal. (−1.57) |
| Fool's Gold | $2 | payload: economy in multiples | Reacts to opponent Provinces (Butcher gains count). **Empty FG pile + Tower = 1 VP per FG held.** (−1.57) |
| Faithful Hound | $2 | deck control: weak terminal draw | Discarded by Embassy or NW, it returns for a 6-card hand. Filler. (−3.02) |
| Pooka | $5 | deck control: terminal draw + Copper trashing | Draws dead Tunnels, no village. Mainly brings Cursed Gold. (−2.17) |
| Cursed Gold | Heirloom | payload: $3, gain a Curse | Optional to play. Play it on turns 1–2 and when it changes the buy. A free $3 once Curses are gone. |
| Ritual (Event) | $4 | payload: VP conversion; drains Curses | A Gold held in hand gives **+5 net VP**. Cursed Gold gives +3. Late game with +Buy. (−4.48) |
| Tower (Landmark) | – | scoring | Realistic empty piles: Curses (likely) and FG (if someone commits). Tunnels are Victory, so they don't count. |

### Interactions found
- **Tunnel + Embassy / Night Watchman:** the main Gold source. Embassy averages about 1.5 Golds per play with 3 Tunnels in an 18-card deck. Each NW gives about 0.6–1, and several NWs dig sequentially.
- **Gold source + Butcher:** Gold→Province for free.
- **Butcher + junk:** Estate, Curse or Copper becomes a Tunnel or NW.
- **Cursed Gold + Curse pile + Tower + Ritual:** the pile probably empties. Held Curses then net 0 VP, and Ritual is the finisher.
- **Fool's Gold + Tower + NW/+Buy:** up to about +10 VP if one player gets most of the pile. Each FG the opponent buys is a 2 VP swing.
- **FG reaction vs. Butcher:** Butcher's Provinces trigger the opponent's FGs.
- **Faithful Hound + Embassy/NW:** a 6-card next hand. Minor.
- No combo from `context/combos.md` is present.

### Gate answers
1. **Trashing:** weak. Butcher removes one card a play but replaces it, Pooka hits Treasures only, Ritual adds a Curse.
2. **Junking:** no Attack. You junk yourself with Cursed Gold and Ritual, and Tower may refund it.
3. **Draw:** only City Quarter in action-dense hands is real draw. The rest is terminal.
4. **Payload ceiling:** about 1 Province from the buy plus 1 from Butcher, plus +Buy extras.
5. **Outliers:** Butcher, the Tunnel flood, and Tower on Curses and FG.
6. **Scoring routes and piles:** Provinces, Duchies, Tunnels (16 VP total), Tower, Ritual. A Curses + Tunnels + FG three-pile is plausible.

### Candidate strategies
1. **Tunnel Gold flood with Butcher (recommended).** Payload is Butcher, Golds, Tunnels and late Merchant Guild + Ritual. Deck control is 1–2 Embassy and 2 NW. It needs Embassy in the opening, 3–5 Tunnels and 2 NW by about turn 8, Butcher by turn 5–7, and at most 3 terminals. Weaknesses: Tunnels without Embassy are dead, the Tunnel pile is contested, Embassy gifts Silver, and Butcher's Provinces feed an FG opponent.
2. **Fool's Gold + Tower money.** 8–10 FGs, Nomad Camp or Merchant Guild for +Buy, and NW to stack FGs. It's fragile because denial is cheap.
3. **City Quarter engine.** CQ ×3–4 plus Hound and Nomad Camp for action density. 24–32D, no Estate trashing, and too slow.
4. **Baseline: Embassy Big Money.** Plan 1 is a strict superset.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| 1. Tunnel/Butcher | ~T7–9 | ~T16–18 | Province + Butcher-Province (~12) | Most Provinces + 8–10 Tunnel VP + Ritual |
| 2. FG + Tower | ~T10 | ~T17 | ~Province | Provinces + up to 10 Tower |
| 3. CQ engine | ~T13–14 | ~T18+ | 2 Provinces | High, but too late |
| 4. Embassy-BM | ~T9 | ~T18–20 | Province | ~4–5 Provinces by T14–15 |

| You \ Opponent | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| 1. Tunnel/Butcher | even: Tunnel split and NW count | slightly favored: cuts Tower with 2–3 FGs | favored: race and three-pile | favored: superset |
| 2. FG/Tower | slightly unfavored | even: FG split | favored | even |
| 3. CQ engine | unfavored | unfavored | even | even-to-unfavored |
| 4. Embassy-BM | unfavored | even | even-to-favored | even |

**Robust vs. fragile:** Plan 1 is robust. FG/Tower and the CQ engine are fragile.

**Recommendation:** Plan 1, against both strong and unknown opponents. Against an FG player, add 2–3 FGs. What would flip it:
- The opponent building City Quarter: race and three-pile.
- 3+ players: Silver gifts multiply and the Curse pile is 20+, so lean to Butcher money and FG.

### Openings
Playing Cursed Gold on turns 1–2 gives $9: 5/4 about 41%, 6/3 48%, 7/2 12%. Turns 1–2 never give 4/3 or 5/2.
- **5/4 or 6/3:** Embassy / Tunnel. Silver also works, or Nomad Camp when the $4 is turn 1.
- **7/2:** Embassy / nothing, or Faithful Hound.
- **Night Watchman on turns 1–2:** don't discard with it unless you deliberately want the turn-2 early-reshuffle trick.

### Buy priorities
- **Shuffles 2–3:** Gold at $6–7. Butcher at $5 (first copy). Tunnel at $3–4 (4–5 total). Night Watchman (2 total). Second Embassy only after Butcher.
- **Butcher targets:** Gold→Province once you have 3+ Golds or Provinces ≤ 6. Otherwise Estate→Tunnel, Curse→Tunnel/FG, or Cursed Gold→Gold. Bank Coffers.
- **Around turn 9–10:** one Merchant Guild or Nomad Camp for +Buy.
- **Greening:** Province from about turn 7. Duchy once Provinces ≤ 4. Tunnels throughout. Ritual on a held Gold in the last 2–3 turns.
- **Adapting:** contest Tunnels against an Embassy/Tunnel opener, buy 2–3 FGs against an FG player, and push piles against City Quarter.

### Endgame and piles
- **Curses:** likely empty around turns 14–18. If you hold more Curses, use Ritual to empty the pile. If you hold fewer, avoid emptying it and stop playing Cursed Gold when it doesn't change the buy.
- **Tunnels and FG:** possible second and third piles. A three-pile ending favors the player who scored early.
- **Otherwise:** a Province ending with a Duchy dance. Apply the penultimate Province rule, counting the opponent's Butcher, Coffers and Golds topdecked by FG.

**Watch out for:** the Tunnel split, a Tower windfall for an FG player left alone, and converting Golds with Butcher before you have 3 or more.

## Process notes
- **Files read:**
  - Repo: `CLAUDE.md`, `context/rules.md`, `context/strategy.md`, `context/card-power.md`, `context/combos.md` (provided as session context), `skills/kingdom-analysis/SKILL.md`, and `data/card-glicko/{cards,events-projects,landmarks}.csv` plus `FETCHED`.
  - The kingdom file `k1/kingdom.md`.
  - `cardtext.py` for Curse and Gold.
  - No network access, and no other scratchpad paths.
- **Misleading:** the skill's output format assumes 4/3 and 5/2, and `context/strategy.md` says "Turns 1–2 give $7". Heirlooms change that, and neither file mentions them.
- **Missing:**
  - That Curses count as "non-Victory" for Tower and similar Landmarks.
  - Faithful Hound's "at end of turn" timing. I used the ruling that it returns after Clean-up's draw, and that is unconfirmed by repo context.
  - The risk of Night Watchman forcing an early reshuffle on turn 2.
- **Priors misleading here:** Night Watchman, Tunnel and Ritual are central on this board despite bottom-tier ratings. The skill does warn about this. Embassy and Nomad Camp are "deprecated" with phi 1.00, so their priors are weak.
- **No simulator or density guidance:** the speed and VP estimates are judgment.