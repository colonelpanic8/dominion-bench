I used the kingdom-analysis skill and did the full version (steps 1–8). Everything comes from the kingdom file, the repo context and the local Glicko CSVs. The build lines below are worked by hand on paper; I didn't simulate anything.

---

## Inventory

- **Kingdom:** Vassal $3, Hermit $3, Caravan $4, Bridge $4, Diplomat $4, Treasure Trove $5, Outpost $5, Rogue $5, Old Witch $5, Hireling $6.
- **Landscapes:**
  - Sewers ($3 Project): when you trash a card other than with Sewers, you may also trash a card from your hand.
  - Ferry ($3 Event): moves your own −$2 token to an Action pile.
- **Non-Supply pile:** Madman, from Hermit.
- **Setup:** no Colonies and no Shelters. 2 players. Curses: 10.
- **Durations:** Caravan, Hireling, Outpost.
- **Price points:**
  - $5 is crowded.
  - $6+ has only Hireling and Gold.
  - $2 has nothing.
  - Ferry can drop any one Action pile by $2. It can be moved again later.
- **Starting deck:** 7 Copper and 3 Estates. Under the tournament rule you choose your split, so it's 4/3 or 5/2 by choice, not by luck.
- **Hermit rule (2018–19 wording):** when Hermit is discarded from play on a turn you bought no *cards*, it is **trashed** and you gain a Madman. Two things follow:
  - Buying Ferry or Sewers is not buying a card, so it doesn't stop the Madman.
  - Hermit's own self-trash triggers Sewers, and it puts a $3 card in the trash for Rogue.

## Old Witch, Hermit, Sewers and Ferry

**Board:** This is a Curse slog built around Old Witch. Trashing is good: Hermit plus Sewers trashes two cards per play. Ferry makes Old Witch cost $3, so you can open it on a 4/3 and Hermit can gain more copies.

Villages are weak. Diplomat only gives Actions if your hand is small, and Madman is used up when played. So a full engine that draws your whole deck isn't realistic. Bridge is the only +Buy. Scoring is Provinces and Duchies, with Curses as minus points.

**Key interactions:**
- **Ferry on Old Witch.** Old Witch costs $3 on your turns. That has three effects:
  - A 4/3 opens Ferry and Old Witch. That beats a 5/2 Old Witch with nothing at $2.
  - Every Hermit play can gain another Old Witch.
  - Each player has their own token, so expect the mirror.
- **Hermit and Sewers.**
  - Hermit trashes an Estate or Curse from your **discard pile** or hand. Sewers then trashes a card from your hand, such as a Copper or Curse. That's 2 junk cards gone per Hermit, plus a gain worth up to $3.
  - If you don't buy a card that turn, Hermit trashes itself. That fires Sewers again, if your hand still holds a card at that point (see Assumed). You also get a Madman.
  - From about turn 5, that removes roughly 2–3 junk cards per Hermit play. That outpaces one Curse every other turn.
- **Old Witch's victim and Sewers.** When Old Witch hits you, you may trash a Curse from your hand. That counts as you trashing, so your own Sewers also trashes a second card from your hand. Sewers is defence as well as thinning.
- **Madman and Old Witch.**
  - Madman played from a 5-card hand gives +2 Actions and draws 4 cards, which lets you play 2 Old Witches or Old Witch plus Hermit.
  - A Hermit turn where you buy nothing is the cost of a Madman. You still gain a card from Hermit, and buying Ferry or Sewers that turn is allowed.
- **Rogue and the trash.** Every Hermit that becomes a Madman leaves a $3 card in the trash, from either player. So Rogue is reliably +$2 and gains a Hermit, which goes on gaining and thinning. Rogue's rating is −3.28, but it's much better here.
- **Bridge, Ferry and Hermit.**
  - With Bridge in play, Hermit can gain $4 cards: Bridge, Caravan or Diplomat.
  - If you later move Ferry to Treasure Trove, a Trove costs $3, so Hermit can gain one each play. Each Trove then makes $2 and gains a Gold.

**Other cards:**
- **Vassal:** its best partner is Old Witch or Hermit flipped off the top of the deck and played for free. It's a cheap target for Hermit to gain, close to a Silver.
- **Caravan:** pairs with Outpost and Hireling for bigger hands. It's harmless, non-terminal filler.
- **Diplomat:** pairs with Old Witch as a reaction (draw 2, discard 3, so you can dump Curses). It only acts as a village late in a turn, after playing Bridge or Hermit, with 3 or fewer cards in hand.
- **Hireling:** suits the long slog, where +1 card every turn adds up over about 15 turns. One copy, around turn 8–12.
- **Outpost:** pairs with Old Witch, because the extra turn is an extra attack. It also pairs with Hireling and Caravan, which make the 3-card extra hand bigger. It's a late $5 option, not core.
- **Treasure Trove:** pairs with Bridge or Ferry, and Sewers can trash the Copper it gains. It's the main way to turn a junked deck into money for Provinces.

**Ratings check:**

| Card | Rating | Board-specific reason for any gap |
| --- | --- | --- |
| Ferry | 4.14 | Matches: Ferry here enables the whole opening. |
| Bridge | 4.07 | Lower here: few villages, so it's only +Buy. |
| Hermit | 3.68 | Rating is for the current wording. The old wording here is stronger: it combos with Sewers and Rogue. |
| Old Witch | 3.38 | Matches. |
| Sewers | 0.69 | Much higher here: two trashers trigger it, including Old Witch's Curse-trash. |
| Rogue | −3.28 | Higher here, because Hermits keep landing in the trash. |

## Build lines

- **Old Witch/Hermit slog (recommended).** Open 4/3: Ferry on Old Witch, then Old Witch.
  - T3–4: Hermit and Sewers. With 2 Buys you can add a Silver.
  - T5–7: Hermit trashes Estates from your discard pile while Sewers trashes Coppers from your hand. Hermit gains Old Witch #2 at $3. One turn with no card bought gives a Madman. Old Witch gives about 1 Curse every other turn.
  - Shuffle 3 (T8–10): the deck is about 2 Old Witches, 2 Hermits, a Madman, 1–2 Silvers, ~5 Coppers, 1 Estate and 1–2 Curses. A Madman turn with 2 Old Witches gives 2 Curses and draws 9+ cards.
  - Add economy from about T9: Gold or Treasure Trove, plus Bridge for +Buy. Province hands start around T11–12.
  - A typical built turn: Madman, Old Witch, Bridge, then Gold, Silver and a Trove. That's about $9 with 2 Buys: a Province plus an Estate, or a Duchy plus a Silver.
- **Old Witch Big Money (baseline).** 4/3: Ferry/Old Witch, then Silver, Gold and a second Old Witch.
  - First $6 around T4–5, first $8 around T7–9.
  - It plays Old Witch about 50–60% of turns.
  - It has no Curse removal, so its deck rots after T10.
- **Bridge engine.** Ferry on Bridge, so Bridges cost $2, and $1 with one in play. Madmen and Diplomat supply the Actions.
  - Madmen are used up and Diplomat is conditional, so in practice you play 2–3 Bridges about every third turn.
  - That's about 2 Provinces on a big turn, and much less while Curses are coming in.

| Plan | Starts scoring | Can end by | Peak VP/turn | VP ceiling |
| --- | --- | --- | --- | --- |
| Old Witch/Hermit slog | ~T11 | ~T18–22 (Provinces, or Curses + Hermits + 1 pile) | Province + Estate/Duchy | Provinces + Duchies, minus few Curses |
| Old Witch BM | ~T8 | ~T20+ | 1 Province | Fades as Curses pile up |
| Bridge engine | ~T12 | ~T18 | ~2 Provinces, unreliable | Capped by weak villages |

**Against their best plan:**
- **Recommended plan against the mirror:** the Curse split decides it. Hermit gaining Old Witches at $3, plus Madman turns with 2 Old Witches, gets ahead in Curses. Sewers clears your Curses for free when you're attacked.
- **Recommended plan against Old Witch BM:** BM scores first, but takes more Curses and can't remove them, so the slog overtakes it around T14–16.
- **Runner-up (Old Witch BM) against the slog:** it loses the long game. Its only hope is a fast Province lead before the Curses bite.

**Challenged:** I re-tested the Bridge engine with Ferry on Bridge and Hermit gaining Bridges. The problem is still Actions: each Madman costs a turn with no card bought, and Diplomat fails after drawing. It works as a late add of 1–2 Bridges, not as the plan.

The recommendation loses in three ways:
- the opponent wins the Curse split by drawing Old Witch more often, or
- you buy cards every turn and never get Madmen, or
- you over-thin and can't reach $8 at the end.

The opponent will see Ferry/Old Witch and mirror it. That's fine, because the trashing, not the opening, is the edge.

## Recommendation

**Recommendation:** an Old Witch slog with Hermit and Sewers. Ferry goes on Old Witch first. You have the better junker, the fastest Curse removal, and Rogue and Madmen as extras. It holds up against both the Old Witch mirror and money.

**Open:**
- 4/3: Ferry (on Old Witch) with the $4, then Old Witch at $3. The order doesn't matter.
- 5/2: worse, because it's Old Witch plus nothing. Choose 4/3.

**Buy priorities:**
1. Shuffle 2: Hermit and Sewers.
2. Then Old Witch #2 or #3, gained by Hermit at $3.
3. Then Hermit chains: gain more Hermits, Vassals and Silvers.
4. Take deliberate no-buy Hermit turns for Madmen. Buying Ferry or Sewers that turn is still allowed.
5. Around T8–10: 1–2 Bridges, Gold or Treasure Trove, 1 Hireling. Rogue once the trash holds Hermits. Consider moving Ferry to Treasure Trove once the Curses are gone.

Start greening once you reliably hit $8, around T12. Take Duchies early, because Curses keep the game long.

**Ending:** most likely the Provinces run out, around T18–22. The Curse pile will run out, and the Hermit pile may too, because Hermit gains Hermits and trashed copies never return. Then a third pile (Duchies or Old Witch) would end the game, so count piles once Curses are gone.

**Watch out for:**
- **Rogue's attack.** When the trash has no $3–6 cards, Rogue trashes the opponent's Silvers, Golds or Hermits. Rogue gaining your trashed Hermits feeds them.
- **A three-pile ending** once Curses and Hermits are low.
- **Diplomat's reaction** filters away Curses only slightly. It doesn't change the plan.

**Least sure of:** whether Old Witch BM with Ferry builds a big enough early Province lead before the slog overtakes it around T14–16. To test it, play both lines on paper through T16 with the expected Curse split.

**Assumed:**
- I'm reading Hermit's tournament wording literally: buying Events or Projects doesn't count as buying a card.
- When Hermit trashes itself in Clean-up, Sewers can still trash from your hand only if Hermit is discarded before your hand. I haven't confirmed that ordering. If your hand is discarded first, that self-trash gets no Sewers bonus.
- Ferry's token belongs to each player and only applies on that player's turns.
