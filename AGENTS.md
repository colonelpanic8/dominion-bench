# dominion-bench

A benchmark for Dominion kingdom analysis. Each case pairs a kingdom with an
answer key built from published expert analysis. `README.md` is the spec for
the case format, sources, and how to run and grade a benchmark;
`grading.md` is the grader's rubric.

## Layout

- `cases/<id>/case.json`: the kingdom and metadata.
- `cases/<id>/key.md`: the answer key.
- `scripts/bench.py`: `check`, `render`, `list`, `sandbox`.
- `results/<date>-<name>/`: past runs with analyses and grades.
- `raw/`: local-only source material (gitignored).

## Invariants

- **Never analyze a kingdom from inside this repo.** Analysts run in a
  sandbox from `scripts/bench.py sandbox`, which contains only
  dominion-agents' files and the kingdom briefs. An agent that has read any
  `key.md` can't be an analyst for that case.
- Keys paraphrase their sources. Quotes stay a sentence or shorter and are
  attributed. Raw source text stays in `raw/`.
- Card and pile names in `case.json` match dominion-engine's data.
- `case.json` holds only what a player sees at setup. Analysis goes in
  `key.md`.

## Checks

`just check` (inside the dev shell: `direnv allow`, or
`nix develop -c just check`) checks Nix formatting and validates every case
against the pinned dominion-engine card data. `nix flake check` runs the
same case validation.
