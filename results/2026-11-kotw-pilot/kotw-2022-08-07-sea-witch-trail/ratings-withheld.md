**Summary**
- **Plan:** a Sea Witch + Wharf Duration deck with 2–3 Sailors, so that Sea Witches and Wharves bought while a Sailor is live are played the turn you gain them and Curses get trashed.
- **Openings:** 4/3 is Sailor + Silver; 5/2 is Sea Witch + Crossroads.
- **Key interactions:** Sailor plays a gained Sea Witch, Wharf or Sailor at once. Berserker plays itself on gain whenever a Duration is in play. Weaver or Berserker gaining Trail gets its Action and card back.
- **Board shape:** one unblockable junker and only one-card-at-a-time trashing, so both players must curse; the Curse split and the Wharf split decide it, with Province + Duchy or two Provinces as the peak turn.
- **Blindness:** no network access; nothing under `data/card-glicko/` opened or listed; no rating used in the reasoning. One leak: `context/card-power.md` was auto-loaded into my context, so its "Headline picture" tier list (which names cards on this board) was visible to me. I disregarded it, but the run was not perfectly blind (see Process notes).

All turn numbers below are rough estimates from reasoning, not simulation.

---

**Board summary:** Sea Witch is an unblockable junker, and the only trashing is slow (Sailor: one card per play, a turn later; Salvager: one card, terminal), so both players have to curse and the 10-Curse split matters a lot. Wharf is real draw on its own, because its next-turn half costs no Action or card, and it carries the +Buy. Crossroads is the only village, and only its first play each turn gives Actions. The deck cannot be thinned fast enough to draw itself reliably, so the realistic ceiling is 9–12 cards seen per turn with 2–3 Buys: Province + Duchy, sometimes two Provinces. There is no alt VP, no VP tokens and no combo from `context/combos.md`.

Setup: 2 players, no landscapes, no Colonies or Shelters, 10 Curses, 8 Provinces, 8 Duchies. Special rules in play: Durations and Reactions only. Every strong card costs $5; nothing in the Kingdom costs $6+, so Gold is the only $6–7 single buy.

| Card | Cost | Role | Notes |
| --- | --- | --- | --- |
| Crossroads | $2 | deck control: village (first play only), draw per Victory card | Only village. Does not draw for Curses. Improves as you green; a second copy in a turn only draws. Support. |
| Guard Dog | $3 | deck control: terminal draw, attack reaction | From a normal 5-card hand it is only +2 (hand goes to 6, so the bonus fails). Reacting to an opponent's Sea Witch or Berserker gives a 6-card hand without using your Action. Does not stop the Curse. Support. |
| Warehouse | $3 | deck control: sifter | Discards Curses and green. Discarding Trail or Weaver plays them. Support. |
| Sailor | $4 | both: non-terminal trasher, +$2 next turn, plays a gained Duration | The only trasher that never costs an Action. Makes a gained Sea Witch, Wharf or Sailor act immediately. Build-around enabler. |
| Salvager | $4 | both: terminal trasher, +$, +Buy | Estate gives +$2. Trail gives +$4 and Trail plays itself, so Salvager becomes non-terminal. A Curse gives $0. Late: Gold for +$6 or Province for +$8. Support. |
| Trail | $4 | deck control: cantrip that plays itself when gained, trashed or discarded | Pure cantrip from hand. Its value is the reaction. Support. |
| Weaver | $4 | payload: gainer (two Silvers, or a card up to $4) | Terminal, but gaining Trail returns +1 Card +1 Action. Plays free when discarded to your own Sea Witch or Warehouse, or to an opponent's Berserker. Support. |
| Berserker | $5 | payload: gainer (up to $4) plus handsize attack | Plays itself on gain if any Action is in play, including a Duration from last turn. Gaining Trail makes it a cantrip. Support. |
| Sea Witch | $5 | both: junking attack, terminal draw now, sift next turn | Each copy is in play for two turns, so it takes 2 copies to attack every turn. Centerpiece. |
| Wharf | $5 | both: draw and +Buy now and next turn | Only reliable +Buy. Durations collide less because they are out of the deck half the time. Centerpiece. |

**Interactions that matter here**
- **Sailor + Sea Witch / Wharf / Sailor:** buy one with a Sailor played that turn and it plays immediately. Sea Witch curses the turn you buy it; Wharf gives a Buy now and a 7-card hand next turn. A Sailor gained this way carries its own trigger, so with a spare Buy you can chain Sailor, then Wharf.
- **Shuffle caveat:** the play is optional. Decline it if the +2 Cards would trigger a reshuffle while your Durations are in play.
- **Berserker + Durations:** with any Sailor, Wharf or Sea Witch in play, a bought Berserker attacks and gains a $4 card on the spot. If a Sailor was played this turn, gain a Sailor and it plays too.
- **Weaver or Berserker gaining Trail:** the Trail plays on gain, so the terminal gets its card and Action back.
- **Sea Witch's "discard 2" + Trail / Weaver:** discarding them at start of turn plays them for free. Warehouse does the same.
- **Berserker's attack is weak on this board:** Trail and Weaver react to the discard, Guard Dog reacts to the play, start-of-turn Wharf and Sailor effects are untouched, and cursed hands have junk to throw away.
- **Start-of-turn ordering:** resolve Wharf's draw before Sailor's trash so there is a bigger hand to find a Curse in.

### Candidate strategies
1. **Sea Witch + Wharf money (the BM+X baseline):** open Silver/Silver, buy 2 Sea Witches, then 2–3 Wharves, Gold and Provinces.
   - Needs: first Sea Witch by T3–4, second by about T7.
   - Weaknesses: cannot remove Curses, Sea Witch and Wharf collide with no village, and new Durations wait a full shuffle before doing anything.
2. **Sailor-tempo Duration deck (recommended):** 2–3 Sailors, 2 Sea Witches, 3–4 Wharves, 1–2 Crossroads, Silver and Gold as payload, and optionally one Berserker (gaining Trail or Sailor) and a late Salvager.
   - Good turn: an 8–10 card hand with +$2 to +$4 from Sailors, 2–3 Buys, and a Curse or Estate trashed.
   - Needs: a Sailor from the opening, a second Sailor by about T5, 2 Sea Witches by about T7, 3 Wharves by about T11.
   - Weaknesses: all three key piles cost $5; the opponent wants the same Wharves and Sailors; each Sailor takes a hand slot on the turn it is played.
3. **Crossroads/Wharf engine:** plan 2 pushed further, with 4–5 Wharves, 2 Crossroads, 3–4 Sailors thinning, Weaver and Berserker gaining Trails and Sailors, and Warehouse, aiming for two Provinces a turn.
   - Needs: at least half the Wharf pile, Curses trashed about as fast as they arrive, roughly 1.5–2 Sailor trashes per turn by T8.
   - Weaknesses: slow under cursing, one Crossroads supplies all the Actions, and it loses to an early three-pile or early greening.

Not a candidate: skipping Sea Witch for Guard Dog + Wharf money. Guard Dog only draws, the Curses still arrive, and you would take close to all ten.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| 1. Sea Witch + Wharf money | ~T10 | ~T19–21 | one Province, not every turn | about half the Provinces plus Duchies, minus ~5 untrashed Curses |
| 2. Sailor-tempo Durations | ~T10–11 | ~T17–19 | Province + Duchy, sometimes two Provinces | Provinces and Duchies, with most Curses trashed |
| 3. Crossroads/Wharf engine | ~T13–14 | ~T17–19 | two Provinces | highest if it gets built; can also end on piles |

| You \ Opponent | 1. Money | 2. Sailor-tempo | 3. Engine |
| --- | --- | --- | --- |
| 1. Money | even: Curse split and turn order decide | slightly unfavored: they trash Curses and get Durations into play sooner | even: a race, you must be well ahead by about T14 |
| 2. Sailor-tempo | favored: cleaner deck, more Buys | even: Curse and Wharf splits decide | slightly favored: you green earlier and can contest Wharves |
| 3. Engine | even to slightly favored if the Curses are handled | slightly unfavored: out-tempoed, Wharves contested | even: Wharf split decides |

**Robust vs. fragile:** Plan 2 is robust. It curses as fast as anything, trashes what it receives, and can green early or keep building. Plan 1 is simple but has no answer to its own Curses. Plan 3 is fragile: it needs the Wharf split and an opponent who lets the game run long.

**Recommendation:** Plan 2. Against a strong opponent stay there; against a weak one, or one who skips Sea Witch, lean toward plan 3 (more Wharves, Sailors and Crossroads, with Weaver and Berserker gaining Trails) for two-Province turns.

**Open:** 4/3: Sailor + Silver. Sailor is non-terminal, makes T4–5 hit $5 almost every time, and with $4 while it is live a second Sailor plays immediately. · 5/2: Sea Witch + Crossroads. The junker comes first, and Crossroads is the only $2, roughly replaces itself with three Estates, and is the village you will need anyway.

**Buy priority, first 2–3 shuffles:**
1. Sea Witch, until you have 2.
2. Wharf, up to 3–4.
3. Sailor, up to 2–3, and always at $4 when a Sailor is live.
4. Gold at $6–7 once you have 2 Sea Witches and 2 Wharves.
5. Crossroads with a spare Buy once you hold 3 or more terminals.
6. Silver.

Good double buys: $9 is Wharf + Sailor, $10 is two $5 cards, $7 is Wharf + Crossroads. Consider one Berserker when a Duration is in play and you already have both Sea Witches. Trash with Sailor in the order Curse, Estate, Copper, and keep an Estate or two if you rely on Crossroads.

**Greening:** Province at $8 from about T10–11, or once the Curses are nearly gone. Duchy at $5–7 when 4–5 Provinces remain, and Province + Duchy at $13.

**Adapting to the opponent:**
- They skip Sea Witch: thin harder and scale toward plan 3.
- You are losing the Curse split badly: add Warehouse and Weaver for Silvers, and take Duchies earlier.
- They attack every turn: one Guard Dog is a cheap pickup.

**Watch out for:**
1. **Three-pile ending.** Curses will empty around T12–15. Wharves can empty if both players take 4–5, and Sailors or Trails can be a third pile once Weaver, Berserker and extra Buys are gaining. Count gains before buying the card that lets the opponent end it.
2. **The opponent's visible next turn.** Wharves, Sailors and Sea Witches in play show the extra cards, Buys and $ they start with. Check them before the penultimate Province. Salvager on a Gold (+$6) or Province (+$8) is a hidden burst.
3. **Collisions and shuffles.** Sea Witch + Wharf in one hand with no Crossroads wastes one, and an immediate play that triggers a reshuffle leaves your Durations out of it.

With 3+ players, more Curses arrive per turn, so Guard Dog and Sailor trashing gain value, your own Sea Witch matters relatively less, and the Wharf and Sailor piles are contested harder, so a three-pile ending comes sooner.

## Process notes

**Files read**
- `/home/imalison/projects/dominion-agents/skills/kingdom-analysis/SKILL.md` (read from disk).
- `/tmp/claude-1000/-home-imalison-projects-dominion-agents/a631d71b-c39f-4667-8a5e-fd864af8e735/scratchpad/abl/k5/kingdom.md` (read from disk).
- `CLAUDE.md`, `context/rules.md`, `context/strategy.md`, `context/card-power.md` and `context/combos.md` were already inlined in my context and were not re-read from disk.
- `cardtext.py` was never run or opened; `kingdom.md` had all ten card texts. No Bash commands and no network tools were used.

**Blindness leak**
- `CLAUDE.md` inlines `context/card-power.md` via its `@` link, so the "Headline picture" tier list was in my context before the task began. It names Wharf and Sea Witch. A truly blind run needs that section moved out of the mandatory context or the file withheld.

**Unclear, missing or misleading in the repo**
- **Output format vs. procedure:** the skill's output format has no slot for step 3 (interactions), step 9 (buy priority, greening, adapting) or step 10 (piles and endgame). I added extra lines for them.
- **Durations in strategy.md:** nothing says a Duration's next-turn draw is draw on its own, that Durations collide less because they sit in play, or that a Duration attack needs 2 copies to "play an attack every turn".
- **Rules I had to infer** (rules.md is silent on each):
  - A Duration in play from last turn counts as "an Action in play" for Berserker.
  - Sailor's "once this turn" applies only on the turn it is played.
  - Cards played on gain during the Buy phase resolve fully, though drawn Treasures cannot be played after a buy.
  - A Trail or Weaver discarded to "discard down to 3" still plays, leaving you above 3 cards. This is my assumption and worth a rules.md line on discard reactions.
  - Guard Dog's "first play this" resolves fully before the attack.
- **Cursed-mirror clock:** the Big Money clock (4 Provinces by T14–17) has no adjustment for a mutual-junking game. I guessed about +3 turns.
- **Opening a village:** "Opening a plain village is almost never right" gives no help on a 5/2 where the only $2 is a village that also draws (Crossroads). A note on what to do with a forced $2 would help.
- **combos.md:** it has nothing for this board, which is fine, but there is no home for strong non-game-deciding synergies such as Sailor + Durations or Weaver/Berserker + Trail. The patterns list in strategy.md did prompt me to find them.
- **Costs in the skill:** it never asks you to note that all key cards share one price point or that there is no $6+ Kingdom card. Both shaped the buy priorities here.