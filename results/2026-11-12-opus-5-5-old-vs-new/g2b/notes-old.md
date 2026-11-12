# Game g4 — P1 — plan

**Board:** Lost City (lab-village) is real non-terminal draw; Villa gives +Actions/+Buy/+$1 (and gained-to-hand); Sentinel + Junk Dealer trash; Borrow gives +Buy. No junker, no attacks except none (Lighthouse defends nothing relevant). Provinces-only scoring. Engine is feasible.
**Key interactions:**
- Tools (treasure) gains a copy of a card in play: with Lost City/Villa in play each Tools = extra engine piece per turn without Action.
- Villa bought in Buy phase -> to hand, back to Action phase: play it plus any Actions left.
- Innovation: first gained Action each turn gets played (bought Lost City draws 2 at once). Mid-priority at $6.
- Band of Misfits = Villa/Harbor Village/Sentinel copy (worse than just buying them).
**Plans:** (a) BM+Vault: ~4 Provinces by T15. (b) Engine: Sentinel trash, Lost City x4-6, Villas for buy, Vault/Junk Dealer/Gold payload, Borrow +Buy -> double Provinces ~T12-14.
**Recommendation:** Engine (b).
**Open:** 4/3: Silver/Sentinel (or Tools/Sentinel). 5/2: Junk Dealer/Lighthouse (or nothing).
**Buy priorities:** $5 Lost City (first 1-2 even before Gold), $4 Villa / Tools, $6 Gold early or Innovation once 2+ LC, $3 Sentinel (only 1-2) else Silver. Trash Estates/Coppers keeping ~$6 money. Add Vault 1-2 as drawing payload once actions plentiful.
**Green:** when deck produces $13+ with 2 buys, or Provinces <=4 left. Watch PPR.

## Turn log
- LESSON: after answering Sentinel, phase may already be Buy — never start steps with `end` without checking phase.
- Villa trick: buy Villa in buy phase -> `play Villa; end; buy X` gives +$1 +Buy.
- FINAL: won 32-30 (Provinces out, T15). Last Province bought with exactly $8 using Lighthouse + Villa + Borrow.
- T13: me 25 (3P,2D,E) vs opp 21 (3P,1D). 2 Provinces left -> Duchy dance; don't take penultimate Province unless lead after it > opp's best reply (6+).
- T9: opp mirrors (LC x3, Villa x2, Golds, Junk Dealer). LC pile 4 left. No VP yet either side.
