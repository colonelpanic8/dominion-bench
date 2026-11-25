# 2026-11-25 GPT-6.2 Sol, dominion-agents 3cbf23a

Eighteen blind analyses by GPT-6.2 Sol (`gpt-6.2-sol`, high reasoning effort) with the `kingdom-analysis` skill at `3cbf23a`. That is the context Opus 5.5 had in `../2026-11-12-opus-5-5-3cbf23a`; the repository is now dominion-playbook. The cases are the same 16 as that run, plus the two `arena-*` cases.

## Setup

- **Analysts:** one sandbox per case, built with `scripts/bench.py sandbox --agents ~/projects/dominion-playbook --rev 3cbf23a`.
  - Each analyst was a headless `codex exec` (codex-cli 0.172.0) with the sandbox as its working directory, `-s read-only` (no network) and `--ephemeral`.
  - It used a fresh `CODEX_HOME` holding only the login and `model = "gpt-6.2-sol"`, `model_reasoning_effort = "high"`, so no user-level instructions or skills reached it.
  - The prompt: "Use the kingdom-analysis skill to write a full analysis of the kingdom in kingdoms/<case>.md."
- **Blindness:** every shell command in the 18 logs used relative paths inside the sandbox. Each run read the skill, the brief and the context files, took 4–6 minutes and wrote about 12k output tokens.
- **Grading:** nine Opus 5.5 graders at high effort, two cases each, following `grading.md`, as in the Opus runs. They were told not to read `results/` or any other grade. These are not the graders that scored the Opus runs, and two gradings of one analysis can differ.

## Scores

Rubric / traps fell / plan match. "Post" means dated after June 2026, Opus 5.5's knowledge cutoff. Sol's own cutoff isn't known here, so the split is less telling for Sol.

| Case | Cutoff | Sol | Opus 5.5 at `3cbf23a` | Sol's main miss |
| --- | --- | --- | --- | --- |
| horton-2019-09-finals1 | pre | 0.75 / 0 / 6 | 0.35 / 0 / 4 | Madman as the main village; Diplomat secondary |
| horton-2025-10-designed3 | pre | 0.69 / 0 / 6 | 0.13 / 0 / 3 | Opens Exploration/Steward, not Tent/Exploration; one Garrison |
| horton-2026-04-finals | pre | 0.64 / 0 / 6 | 0.36 / 1 / 4 | Finds every mechanism but goes Governor first; Tactician optional |
| horton-2026-09-finals | post | 0.77 / 1 / 6 | 0.73 / 0 / 6 | Pairs of Triumphs from turn 8–10, not one turn-7 megaturn; a Potion |
| horton-2026-09-semi1 | post | 0.71 / 0 / 6 | 0.79 / 0 / 6 | Kitsune/Highway engine; Transmute a side line |
| horton-2026-09-semi2 | post | 0.50 / 0 / 4 | 0.69 / 1 / 6 | Souk first, Ronin support; misses Armory → Transmogrify |
| kotw-2021-06-27-bank-counting-house | pre | 0.91 / 0 / 8 | 0.41 / 0 / 4 | Pace: multi-Province turns 8–12, not a finish by 8–9 |
| kotw-2021-09-12-butcher-city-quarter | pre | 0.55 / 2 / 5 | 0.45 / 0 / 5 | Night Watchman and Tunnel as afterthoughts; Fool's Gold payload |
| kotw-2022-04-24-courtier-mandarin | pre | 0.50 / 1 / 4 | 0.75 / 1 / 5 | Never combines Courtier and Mandarin; scores through Displace |
| makingluck-ep101-scrying-pool-hunting-grounds-forge | pre | 0.72 / 0 / 7 | 0.67 / 1 / 6 | Opens Potion/Silver, not Silver/Silver |
| oc-2025-final-g2 | pre | 0.82 / 0 / 8 | 0.86 / 1 / 6 | Misses early greening under Grotto |
| oc-2026-final-g1 | post | 0.69 / 0 / 5 | 0.69 / 0 / 5 | Provinces the main plan; Vineyards and three piles secondary |
| oc-2026-final-g2 | post | 0.90 / 0 / 8 | 0.80 / 0 / 7 | Rope a support card, not the bulk buy |
| oc-2026-final-g3 | post | 0.61 / 1 / 4 | 0.40 / 1 / 3 | One or two Horns, not six or seven; opens Forager |
| oc-2026-final-g4 | post | 0.75 / 0 / 6 | 0.69 / 1 / 6 | Ritual on Flag Bearer and the Flag war minor |
| oc-2026-final-g5 | post | 0.55 / 1 / 6 | 0.60 / 1 / 6 | Villa/Sentinel opening; Junk Dealer as co-trasher |
| arena-2026-11-23-siren-transport | post | 0.75 / 0 / 7 | – | Finds double Transport into Siren; second Siren late |
| arena-2026-11-22-anvil-sycophant | post | 0.33 / 1 / 3 | – | Anvil gains on Blessed Village, not Sycophants: Neon's trap |

Means over the 16 shared cases (rubric / plan match / traps fell in all):

| Set | Sol | Opus 5.5 at `3cbf23a` |
| --- | --- | --- |
| Post-cutoff (8) | 0.69 / 5.6 / 3 | 0.67 / 5.6 / 4 |
| Pre-cutoff (8) | 0.70 / 6.2 / 3 | 0.50 / 4.6 / 4 |
| All (16) | 0.69 / 5.9 / 6 | 0.59 / 5.1 / 8 |

## Reading it

- **Sol scores higher, 0.69 to 0.59, all from the pre-cutoff boards.** Sol scored higher on 10 of 16 cases. The mean difference is 0.11, with a standard error of 0.06. On the post-cutoff boards the two are level, 0.69 to 0.67.
- **The pre-cutoff gap is the boards Opus missed most.** On horton-2025-10-designed3, horton-2019-09-finals1 and the Bank/Counting House board, Sol is 0.4–0.56 higher. Those are older published boards, so training contamination can't be ruled out for either model. Opus's own runs moved by 0.13 per case between two runs of the same revision.
- **Sol shares Neon's Anvil/Sycophant misread.** It saw Sycophant's Favors and Mountain Folk, but spent the Anvil gains on Blessed Village, the line that lost the source game and lost all three self-play games for the untold seat. It found the Siren line (Transport into a turn-3 Siren), which Neon missed.
- **Its misses look like the Opus ones.** It finds most mechanisms, then centres the plan on the safer, more general engine: Governor over Tactician, Souk over Ronin, one or two Horns, Provinces over Vineyards.
- **Caveats:**
  - Different grader runs scored the two models, so some of the gap may be the graders.
  - No `--rev` run of Sol on current dominion-playbook has been made.
  - Both arena keys are B quality.
