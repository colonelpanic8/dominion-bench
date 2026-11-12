# Grading an analysis

You are given one kingdom analysis and the case's `key.md`. Grade how well
the analysis matches what strong players concluded about this board. You
are not grading writing quality.

## Per rubric item

For each **R** item, assign:

- **hit** (1): the analysis makes the claim, or a clearly equivalent one.
- **partial** (0.5): it gets close: names the interaction but not its role,
  mentions the right plan as a secondary option, gives the right opening
  with the wrong reason.
- **miss** (0): it doesn't make the claim.
- **contradicted** (0, flagged): it argues the opposite, e.g. dismisses the
  card the key's plan centers on.

Weight `[core]` items 2 and `[supporting]` items 1.

For each **T** (trap) item, flag **fell** if the analysis recommends the
trap, otherwise **avoided**.

## Score

```
rubric = sum(weight * credit) / sum(weight)       # 0..1
traps_fell = number of T items fell
```

Also give a holistic **plan match** from 0 to 10: would a player who
followed this analysis play roughly the way the key's strongest voices
would? Ground it in the items above. A plan that gets the main idea right
but misses a supporting trick is a 7–8. One that builds around a card the
experts dismissed is 4 or lower.

## Credit beyond the key

Keys are incomplete. List any claims the analysis makes that the sources
don't cover, and mark each as **plausible**, **doubtful** or **wrong**,
with one line of reasoning from card text. These don't change the score.
They are worth reporting, both as missed points in the key and as
hallucinations.

## Output

```markdown
# Grade: <case id>

| Item | Weight | Credit | Note |
|---|---|---|---|
| R1 | 2 | hit | ... |
| T1 | - | avoided | ... |

rubric: 0.72  traps_fell: 0  plan_match: 7/10

## Beyond the key
- <claim>: plausible. <reason>

## Summary
Two or three sentences.
```
