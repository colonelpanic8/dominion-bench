I couldn't save `/tmp/claude-1000/-home-imalison-projects-dominion-agents/a631d71b-c39f-4667-8a5e-fd864af8e735/scratchpad/kotw/k5/analysis.md`: the Write tool refused because subagents may not write report files. I didn't try to get around that through the shell. The full analysis is below for you to save there.

**Summary:**
1. **Plan:** a Sea Witch + Wharf duration-draw deck. Get 2 Sea Witches, then 4–5 Wharves, with 1–2 Crossroads as the only village and Sailors for trashing. Berserker is the second buy when Wharf gives a spare Buy. Sea Witch/Wharf money is the fallback.
2. **Openings:** 4/3 is Sailor/Silver (Weaver/Silver is close). 5/2 is Sea Witch/Crossroads.
3. **Key interactions:** a Sailor played this turn auto-plays a Sea Witch or Wharf you buy, so the Curse lands a shuffle early. Berserker plays itself when bought with any Action in play.
4. **More interactions:** Trail makes Weaver and Berserker non-terminal. Discards from your own Berserker play the opponent's Weaver/Trail. Wharf's start-of-turn draw blunts Berserker's discard attack.
5. **No network access:** I made no web, browser or curl calls and read only the repo, the k5 kingdom file and Glicko rows. I didn't need cardtext.py.

---

# Kingdom analysis: Berserker, Crossroads, Guard Dog, Sailor, Salvager, Sea Witch, Trail, Warehouse, Weaver, Wharf

2 players, Dominion Online rules, no landscapes, no Colonies or Shelters. The special rule in play is Durations (Sailor, Sea Witch, Wharf). There are no non-Supply piles, and the Curse pile has 10 cards.

**Board summary:** The two best cards here are Wharf (Glicko 6.30, rank 6 overall) and Sea Witch (5.20, rank 12), and both cost $5. Sea Witch is the only junker, so the Curse split matters a lot. Trashing is slow: Sailor trashes one card at the start of your next turn, and Salvager is terminal. The only real village is Crossroads, and only the first copy each turn gives +3 Actions, so you get about 3 terminal plays per turn. Wharf's and Sea Witch's next-turn draw needs no Actions, though, so a Crossroads + Wharf + Sea Witch duration-draw deck works. Payload is plain Treasure plus Sailor's +$2, with +Buy from Wharf (and Salvager). The ceiling is about 2 Provinces, or a Province + Duchy, per turn. No combo from `combos.md` is here, but the interactions listed in the summary are real.

| Card | Cost | Role | Notes (Glicko) |
| --- | --- | --- | --- |
| Wharf | $5 | both: terminal draw + Buy, duration | 6.30. The best card here. Its next-turn +2 Cards +1 Buy needs no Action. You want 4–5, and both players will want the 10-card pile |
| Sea Witch | $5 | both: junking attack + draw/sift | 5.20. The only junker. +2 Cards now, then +2 Cards and discard 2 next turn, which sifts out Curses and Estates and can trigger Weaver/Trail |
| Berserker | $5 | payload: discard-to-3 attack + gain a card costing up to $4 | 3.01. Buying it with any Action in play plays it at once: attack plus a free Silver, Sailor or Trail. Played from hand and gaining Trail, it acts like a cantrip Militia |
| Trail | $4 | deck control: cantrip | 2.22. Plays itself when gained or discarded outside Clean-up. This makes Weaver→Trail and Berserker→Trail non-terminal, softens Berserker, and gives Sea Witch's discard some value |
| Sailor | $4 | both: non-terminal, +$2 + trash 1 next turn | 1.68. When you gain a Duration the turn you play Sailor, you may play it. A bought Sea Witch then curses at once, and a bought Wharf gives +1 Buy now and draws next turn. Also trashes Curses and Estates |
| Weaver | $4 | payload: gain 2 Silvers or a card costing up to $4 | 0.59. Plays itself when discarded outside Clean-up: Sea Witch's next-turn discard, Warehouse, or an opposing Berserker. Gaining Trail makes it a cantrip gainer |
| Salvager | $4 | both: terminal trasher + Buy | 0.28. Trashes a Curse for $0 or an Estate for $2. Uses terminal space Wharf wants |
| Crossroads | $2 | deck control: village (first copy each turn only), draw per Victory card | 0.28. The only real village. Draws more once you green. With no Victory card in hand it costs you a card |
| Guard Dog | $3 | deck control: terminal draw + Attack reaction | −1.20. +4 Cards if played from a hand of 4 or fewer (counting itself), otherwise +2. As a reaction it nets about +1 card for your next turn: a 6-card hand against Sea Witch, best 3 of 6 against Berserker |
| Warehouse | $3 | deck control: sifter | −1.97. Sifts out Curses, and discarding Weaver or Trail plays them. Low priority |

The board is built around **Sea Witch** (the Curse split) and **Wharf** (draw + Buy). Support cards: Crossroads (room for terminals), Sailor (trashing, auto-plays, economy), Berserker (spare-buy payload), and Trail/Weaver (discard and gain tricks).

## Interactions that matter

1. **Sailor + a bought Duration.** Buy a Sea Witch with a Sailor played this turn and it plays at once, so the opponent gains a Curse a full shuffle early. A Wharf bought this way gives +1 Buy immediately (its +2 Cards are wasted in the Buy phase), then +2 Cards +1 Buy next turn. Berserker gaining a Sailor while a Sailor is in play also plays the new Sailor.
2. **Berserker plays itself on gain.** "If you have an Action in play" is almost always true in a Wharf, Sailor or Crossroads deck. So buying Berserker gets you Berserker, a card up to $4 (Silver, Sailor or Trail), and a discard attack on the opponent's next hand. That makes it a strong second buy on $10–13 turns with a Wharf Buy.
3. **Trail as a refund.** When Weaver or Berserker gains a Trail, the Trail plays immediately for +1 Card +1 Action, so the gainer becomes a cantrip. This drains the Trail pile, which can become a third empty pile.
4. **Discard triggers (Weaver/Trail).** Sea Witch's next-turn discard, Warehouse, and an opponent's Berserker all play a discarded Weaver (2 Silvers) or Trail (+1 Card). So Berserker is weaker against a deck holding Weaver or Trail, and Guard Dog also blunts it.
5. **Duration draw vs. the discard attack.** Wharf and Sea Witch draw at the start of the victim's turn, after Berserker's discard. A Wharf deck shrugs off Berserker; a money deck without durations doesn't.
6. **Crossroads action cap.** Only the first Crossroads each turn gives +3 Actions, so you get about 3 terminal plays per turn; extra copies only draw Victory cards. Plan around those 3 plays plus the duration halves, which need no Actions.

## Gate questions

1. **Trashing:** weak to moderate. Sailor trashes 1 card per play and is non-terminal. Salvager is terminal. Sea Witch and Warehouse sift but don't trash. That's enough to remove Estates and some Curses, not to thin hard.
2. **Junking:** Sea Witch, and both players will buy it. It can't be blocked (Guard Dog only draws). Sailor can trash some Curses, Sea Witch sifts them, and Wharf outdraws them. The Curse split is the main early fight.
3. **Draw:** Wharf (terminal, plus next-turn draw with no Action), Sea Witch (same shape), and Guard Dog (+4 from a small hand). Crossroads allows 2 extra terminal plays per turn. Durations from the previous turn add 2–6 cards at the start of the turn with no Actions. The deck can draw most of itself but not reliably all of it: Actions are the limit, and Curses dilute it.
4. **Payload ceiling:** Silver and Gold, Sailor's +$2, and Wharf's Buys. A good turn is about $13–18 with 3+ Buys: 2 Provinces, or Province + Duchy, plus a Berserker. There are no VP tokens or alternative VP.
5. **Outliers:** Wharf and Sea Witch are both top tier. No game-deciding combo. Sailor auto-playing a bought Sea Witch is a real tempo edge in the Curse war.
6. **Scoring routes and piles:** Provinces (8), Duchies (8), Estates, and Curses (−10 VP split between the two players). Curses should run out around turns 11–13. Wharf can run out if both players buy 4–5. Trail drains if Berserker or Weaver keep gaining it. Curses + Wharf + Trail is a plausible late three-pile ending, but the game usually ends on Provinces.

## Candidate strategies

1. **Sea Witch / Wharf money (the BM+X baseline).** 1 Sea Witch and 2–3 Wharves, no village, then Silver, Gold and Provinces.
   - Typical turn: 7 cards thanks to a Wharf's next-turn draw, one terminal played, about $8.
   - Needs: Sea Witch by turns 3–5, and 2 Wharves by about turn 8.
   - Weaknesses: terminal collisions, fewer Witch plays than a deck with Crossroads (so it loses the Curse split), and a plateau of about a Province every other turn once cursed.
2. **Crossroads duration-draw deck (Sea Witch + Wharf + Sailor).** 1–2 Crossroads, 4–5 Wharves, Sailors, and Sea Witch for sifting. Payload is 2 Sea Witches early, then Silver and Gold, Sailor's +$2, and Berserker on spare buys.
   - Typical built turn (turn 11 on): start with 9–11 cards from 2–3 Wharves played last turn. Play Crossroads, 2–3 of Wharf or Sea Witch, and any Sailors. That's about 14–16 cards, $14–18 and 3–5 Buys: 2 Provinces, or Province + Duchy, plus a Berserker.
   - Needs: Sea Witch first and both Witches by about turn 7. 3 Wharves and 1 Crossroads by about turn 9, and 4–5 Wharves by turn 12. Wharf is the scarce pile: if the opponent also wants 4–5, the split matters.
   - Weaknesses: terminals collide on turns without Crossroads (a second Crossroads fixes most of that). It needs both $5 piles. Curses still dilute it.
3. **Berserker / Trail / Weaver attack deck (with 1 Sea Witch).** Several Berserkers gaining Trails act as non-terminal discard attacks, Weaver gains Silvers, and Warehouse or Sea Witch discards trigger Weaver.
   - Needs: about 3 Berserkers and some Trails by turn 8.
   - Weaknesses: discarding down to 3 barely hurts a Wharf or Sea Witch deck, and it gives free plays to an opponent holding Weaver or Trail. Without Wharf it has no +Buy, so it tops out at one Province per turn. It's mainly a way to use Berserker inside plans 1–2, not a plan of its own.

A deck that skips Sea Witch isn't listed: you can't outpace 7 or more Curses here.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| 1. Witch/Wharf money | ~T9–10 | ~T18–20 alone (cursed) | a Province every 1.5–2 turns | about half the Provinces + late Duchies |
| 2. Crossroads duration-draw | ~T11–12 | ~T16–17 | 2 Provinces or Province + Duchy | most Provinces and Duchies, with the Curse split in your favor |
| 3. Berserker/Trail attack deck | ~T10 | ~T20+ | ~1 Province | about one Province per turn; loses the Curse split |

| You \ Opponent | 1. Witch/Wharf money | 2. Crossroads duration-draw | 3. Berserker attack deck |
| --- | --- | --- | --- |
| 1. Witch/Wharf money | even: decided by the Curse split and turn order | unfavored: fewer Witch plays, and its scoring flattens just as plan 2's double-Province turns start (~T12) | favored: Wharf blunts the discard attack, and it has more Buys and junks better |
| 2. Crossroads duration-draw | favored: wins the Curse split (2 Witches + Crossroads + Sailor auto-play) and outscales by T12–14. Don't panic-green early | even: decided by the Witch and Wharf splits. Green a bit earlier than against money, and watch the Curse, Wharf and Trail piles | favored: Wharf's draw shrugs off the attack, and it has far more payload |
| 3. Berserker attack deck | unfavored: loses the Curse split, and its attack barely lands | unfavored | even |

**Robust vs. fragile:** Plan 2 is robust: at least even against everything, and it beats money because it plays Sea Witch more often and scales past one Province per turn. Plan 1 is a sound fallback and fine in the mirror, but plan 2 outscales it. Plan 3 is fragile: it needs an opponent without Wharf, Sea Witch, Weaver or Trail.

**Recommendation:** Plan 2. Open toward Sea Witch, get both Witches, then build up Wharves, and add 1–2 Crossroads so you can play Witches and Wharves on the same turn. Use Sailors to trash Curses and Estates and to auto-play the Sea Witches and Wharves you buy. Spend spare Buys on Berserker, which plays itself and gains a Sailor or Silver. This is also the pick against an unknown or weak opponent; against a weak one, one Sea Witch is enough and you can switch to Wharves sooner.

What would change the plan:
- If the opponent skips Sea Witch, one Witch is enough: buy more Wharves and win on draw.
- If you lose the Wharf race (they get 5+ and the pile runs low), switch toward money: Gold plus 3 Wharves, and keep cursing.
- With 3+ players, Curses split more widely, Guard Dog gets better, Berserker hits more hands, and Wharves are scarcer. Lean toward plan 1 and pick up Guard Dog.

**Open:** 4/3: **Sailor / Silver.** Two economy cards to reach $5 on turns 3–4, and a Sailor played then auto-plays any Sea Witch or Wharf you buy that turn. Weaver / Silver is close: two more Silvers is better long-term money, and a later Sea Witch discard plays it again. · 5/2: **Sea Witch / Crossroads.** Curses start a shuffle early. Crossroads works as a cantrip early because it draws your Estates, and you'll need it as your village anyway. Sea Witch / nothing is close.

**Buy priority, first 2–3 shuffles:**
1. Sea Witch.
2. Wharf.
3. A second Sea Witch by about turn 7. Skip it if the opponent has no Witch.
4. More Wharves, up to 4–5.
5. Crossroads on a spare Buy or $2–3: one at first, a second once you have about 5 terminals.
6. Sailor at $4. Get a second once Curses arrive.
7. Gold at $6–7 once you have 3 Wharves.
8. Silver.

Once Wharves give you Buys, Berserker is the second buy for spare $5. Start buying Victory cards when you reliably hit $13+ with 2 Buys (about turns 11–13). Against a money deck, don't start greening early just because they're 1–2 Provinces ahead at turns 10–12.

**Adapting:**
- If the opponent opens Sea Witch: get your second Witch and second Sailor earlier.
- If they open Berserker: rely on Wharf's next-turn draw, and add a Trail or Weaver so their discards help you. Only buy Guard Dog if they get 3+ Berserkers.
- If they go Wharf-heavy: contest Wharf early. A 5–5 split is fine; 4–6 isn't.

**Watch out for:**
- **The Curse split.** Losing it 3–7 is very hard to recover from with this little trashing. Prioritize playing Sea Witch (Crossroads, Sailor auto-play) in the first 10 turns.
- **Three empty piles.** Curses (empty by about turn 12), Wharf (if both players build it) and Trail (if Berserker or Weaver keep gaining it). Count gains before you let an opponent who's ahead end the game on piles. Duchies are the fourth pile to watch.
- **Collisions.** Without Crossroads in hand, Wharf + Sea Witch + Wharf collide. Keep about 1 Crossroads per 5–6 terminals, and lean on next-turn duration draw, Sailor and Trail, which use no Actions.

## Endgame and piles

The game usually ends on Provinces, with Duchy dancing late; Wharf's +Buy makes Province + Duchy turns common. The Curse pile is usually empty by midgame. A three-pile ending needs Wharf plus one more pile (Trail, Duchy or Sea Witch), which is only realistic in a Wharf mirror where both players buy Berserkers that gain Trails. Whoever is ahead once Curses run out should track the Trail and Wharf counts. Crossroads draws more as you green, which keeps a greening deck working longer.

## Process notes

**Files read:**
- /home/imalison/projects/dominion-agents/CLAUDE.md
- /home/imalison/projects/dominion-agents/context/rules.md, context/strategy.md, context/card-power.md and context/combos.md (included in full in the session context through CLAUDE.md's `@` includes)
- /home/imalison/projects/dominion-agents/skills/kingdom-analysis/SKILL.md, plus a directory listing of skills/kingdom-analysis/
- /home/imalison/projects/dominion-agents/data/card-glicko/: a directory listing, FETCHED, the cards.csv header, and the rows for the 10 kingdom cards
- /tmp/claude-1000/-home-imalison-projects-dominion-agents/a631d71b-c39f-4667-8a5e-fd864af8e735/scratchpad/kotw/k5/kingdom.md

I didn't need cardtext.py: there are no non-Supply cards, and kingdom.md had all the card text.

**Where the repo context was unclear, missing or misleading:**
- **Grep hint.** The skill's `grep -i '<name>' data/card-glicko/*.csv` works, but matching on the Card column (`,Name,`) avoids false hits. Minor.
- **Duration timing.**
  - rules.md doesn't say whether a Duration's "once this turn" ability (Sailor's) still applies on the turn its delayed effect happens. The card text settles it.
  - It also doesn't cover cards drawn in the Buy phase, e.g. by a Wharf or Sea Witch auto-played after buying. They're dead, since no Treasures can be played after a buy.
  - Both mattered for the Sailor interaction.
- **Reactions on another player's turn.** rules.md doesn't say when a Reaction played on another player's turn (Guard Dog) is discarded, or how drawing on the opponent's turn affects your next hand. I worked it out from the cards, but a line in rules.md would help.
- **Cards that play themselves.** strategy.md's interaction list covers "gainers + on-gain effects" and "discard for benefit", but not a gained or discarded card that plays itself and gives back an Action (Trail turning a terminal gainer into a cantrip). It also doesn't warn that your own discard attack can trigger the opponent's discard reactions. Both changed how I valued cards here.
- **Curse-war guidance.** strategy.md gives no concrete numbers for how many junkers to buy in 2-player games, when a second Witch is worth it, or how fast 10 Curses run out. I had to estimate.
- **Money benchmarks.** strategy.md only has generic Big Money + X numbers (4 Provinces by turns 14–17). Wharf-money and Witch-money are faster than that, so the race clock is imprecise.
- **Once-per-turn villages.** The village definition ("lets you play more than one terminal") classifies Crossroads correctly. Nothing warns that a village that works once per turn caps your terminal plays; I got that from the card text.