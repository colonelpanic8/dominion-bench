# 2026-11-11 Opus 5.5, rewritten rules, with a noise baseline and a tool run

Three more runs of the 16 kingdoms from `../2026-11-11-opus-5-5`, to test
changes to dominion-agents made after that run. Same analyst (Claude Opus
5.5, headless, sandboxed) and same graders (Opus 5.5, high effort, two cases
each, `grading.md`).

| Run | Folder | dominion-agents | Analyst tools |
| --- | --- | --- | --- |
| Old rules, run 1 | `../2026-11-11-opus-5-5` | `fbad6da` | Read, Glob, Grep, Skill |
| Old rules, run 2 | `../2026-11-11-opus-5-5-repeat` | `fbad6da` | same |
| New rules | this folder | `0c0c5b7` (branch `engine-default`) | same |
| New rules + solo tool | `../2026-11-11-opus-5-5-b0e35fe-solo` | `b0e35fe` (branch `solo-lines`) | plus `dominion solo` |

- **New rules**: money is the floor, not the default; the engine checklist
  is two requirements plus obstacles; reference speeds for each kind of
  deck; candidates always include the highest-ceiling plan; the last step
  argues for the rejected plan.
- **Solo tool**: the same rules, plus a skill step that plays candidate
  lines with `dominion solo` (dominion-engine branch `solo-play`, `48fd4ae`),
  a real game whose other seats sit idle.

## Scores

Rubric / plan match per case. Post-cutoff cases are dated after June 2026.

| Case | Cutoff | Old 1 | Old 2 | New rules | New + solo |
| --- | --- | --- | --- | --- | --- |
| horton-2019-09-finals1 | pre | 0.35 / 4 | 0.25 / 3 | 0.50 / 4 | 0.25 / 3 |
| horton-2025-10-designed3 | pre | 0.31 / 3 | 0.63 / 6 | 0.75 / 7 | 0.06 / 2 |
| horton-2026-04-finals | pre | 0.50 / 4 | 0.64 / 5 | 0.36 / 5 | 0.29 / 4 |
| horton-2026-09-finals | post | 0.69 / 6 | 0.62 / 6 | 0.73 / 7 | 0.69 / 7 |
| horton-2026-09-semi1 | post | 0.43 / 3 | 0.43 / 3 | 0.43 / 4 | 0.50 / 4 |
| horton-2026-09-semi2 | post | 0.44 / 4 | 0.19 / 2 | 0.31 / 3 | 0.50 / 3 |
| kotw-2021-06-27-bank-counting-house | pre | 0.55 / 6 | 0.45 / 4 | 0.50 / 5 | 0.59 / 6 |
| kotw-2021-09-12-butcher-city-quarter | pre | 0.45 / 5 | 0.55 / 5 | 0.27 / 3 | 0.45 / 4 |
| kotw-2022-04-24-courtier-mandarin | pre | 0.63 / 5 | 0.50 / 5 | 0.50 / 5 | 0.25 / 3 |
| makingluck-ep101-scrying-pool-hunting-grounds-forge | pre | 0.56 / 6 | 0.50 / 6 | 0.61 / 6 | 0.39 / 4 |
| oc-2025-final-g2 | pre | 0.59 / 5 | 0.77 / 7 | 0.82 / 8 | 0.50 / 4 |
| oc-2026-final-g1 | post | 0.13 / 2 | 0.06 / 2 | 0.63 / 6 | 0.31 / 2 |
| oc-2026-final-g2 | post | 0.95 / 8 | 0.65 / 5 | 0.65 / 5 | 0.65 / 6 |
| oc-2026-final-g3 | post | 0.39 / 4 | 0.39 / 3 | 0.39 / 4 | 0.22 / 2 |
| oc-2026-final-g4 | post | 0.69 / 6 | 0.63 / 6 | 0.75 / 6 | 0.38 / 4 |
| oc-2026-final-g5 | post | 0.75 / 7 | 0.55 / 6 | 0.70 / 6 | 0.30 / 3 |

| Mean | Old 1 | Old 2 | New rules | New + solo |
| --- | --- | --- | --- | --- |
| Rubric, all 16 | 0.53 | 0.49 | 0.56 | 0.40 |
| Rubric, post-cutoff (8) | 0.56 | 0.44 | 0.57 | 0.44 |
| Rubric, pre-cutoff (8) | 0.49 | 0.54 | 0.54 | 0.35 |
| Plan match, all 16 | 4.9 | 4.6 | 5.25 | 3.8 |
| Traps fell, all 16 | 9 | 10 | 10 | 8 |
| Analyst cost, 16 runs | $11 | $11 | $12 | $39 |

## What the runs show

- **Noise.** The two old-rules runs differ by 0.13 rubric per case on
  average (standard deviation 0.16), and by up to 0.3. One run per case
  can't show a change smaller than about 0.15 on a case, or about 0.05 on
  the mean of 16.
- **New rules: a small gain, inside the noise.** +0.05 rubric over the mean
  of the old runs (standard error 0.05). One case changed for a reason the
  rules aimed at: oc-2026-final-g1 went from Council Room money (0.13,
  0.06) to the Litter deck scoring with Vineyards (0.63). Two cases scored
  below both old runs (butcher-city-quarter, horton-2026-04-finals).
- **The rules don't find the trick.** Reckless Transmute, the Ronin deck,
  Mandarin replaying Golds, several Tacticians with Way of the Owl, and a
  six-Horn turn were missed in every run.
- **The solo tool made analyses worse.** −0.16 rubric against the same
  rules without it (standard error 0.06), lower in 11 of 16 cases. Twelve
  of its 16 recommendations are a money deck, against five without the
  tool. The analyst plays the engine once, on one seed, with misplays it
  admits to, plays money correctly because money is easy, and trusts the
  comparison. An idle opponent also hides what attacks and contested piles
  do.

## Blindness

- **No tool (old 2, new rules):** every tool call stayed inside the
  analyst's sandbox.
- **Solo tool:** the Bash allowlist was `dominion solo` and `dominion card`,
  but Claude Code also allowed read-only commands, and analysts used `cd`,
  `grep`, `head`, `tail`, `sed`, `cat` and `ls`. Every path they named was
  inside the sandbox, apart from one analyst redirecting the tool's own
  output to `/tmp/o`. No analyst changed the kingdom in its solo games.
- An earlier smoke test of the tool is not in these results: the tool could
  not pay off Debt, and the analyst swapped a card out to get past it. That
  was fixed before the run.

The dominion-agents and dominion-engine commits cited here were rebased
onto a newer master after these runs. The originals are kept by the
`bench-2026-11-11` tag in each repository (`b0e35fe` stays on
dominion-agents' `solo-lines` branch).
