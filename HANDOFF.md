# Handoff

Written 2026-10-29, when the repository was laid out as an ICM workspace; brought up to date
2026-10-30 after a review of the root files. It holds the state of the work and what to do
next. Why things are the way they are is in [`DECISIONS.md`](DECISIONS.md).

## State

- The repository lives at `github.com/smiln32/stg-planner-pages`, public, created
  2026-10-30. `main` is at 74aa097 and CI passed on it. The `icm-structure` branch is ahead
  of `main` by the review fixes of 2026-10-30, listed below, and two handoff updates. Merge
  it into `main` locally, push, and delete the branch.
- The ICM structure is in place and `tests/test_stages.py` holds it. The walk in
  `records/icm-audit.md` passes.
- No planner has been taken through the five stages yet. Every stage's `output/` holds only
  `.gitkeep`.
- The engine is unchanged in behaviour but for one fix: the overlap check in
  `planner_factory.py` raised `TypeError` on a numeric string coordinate such as `"28"`
  instead of reporting a finding. It now parses geometry once and compares integers, with a
  test. The suite is twenty checks. CI compiles `planner_studio.py` as well, reads the
  examples from `shared/examples/`, and carries the product's new name.
- An independent review on 2026-10-29 found seven gaps in the contracts: no way for stage
  05 to know the checked specification was the exported one, stale downstream files on a
  revision, stage 04 missing the inputs its report needs, an undefined warning note in
  stage 03, a wrong relative path in the report template, and two document claims. All
  seven are corrected. A second read found two more, also corrected: stage 04 took its
  verdict from generation, which exits 0 even with warnings, and a clean revision could
  leave an old warning note for stage 04 to read. The export gate is still contract-only.
- A review of the root files on 2026-10-30 corrected three documents: `HOW_IT_WORKS.md`
  said exit code 1 meant warnings, when only `--validate-only` returns it and plain
  generation exits 0 with warnings printed; the export contract was the one stage with no
  sensitive-topics line, so `CLAUDE.md`'s "every stage says so" was untrue; and
  `RIGHTS_AND_ATTRIBUTION.md` named Perplexity, which nothing else mentioned. The four
  pictures in `assets/design/` are now cited from `_config/design-system.md`. Two local
  tags, v2.0.0 and v2.1.0, were left over from the old repository's history and were
  deleted; the remote has v1.0.0 and v1.1.0 only, matching the code.

## Next

1. **A cold walk.** Give an assistant only "make me a planner about X" and watch it go from
   `CLAUDE.md` through all five stages without being told anything else. The contracts were
   written by the person who laid out the folders, not tried by a stranger. That is the real
   test of the structure. Include an interrupted revision and an edit to the specification
   after approval: those exercise the hash and the archive rule.
2. **Enforce the export gate in code**, if the cold walk shows an assistant ticking
   **Approved for export** itself. A small command that reads the check report, compares
   the hash and refuses to generate unless the line is ticked would do it.
3. **`_config/design-system.md` has drifted from the Studio.** Of seven colour tokens
   sampled, three do not appear in `studio/styles.css`, and the palette specimen in
   `assets/design/working-atelier-palette.png` shows heading sizes and gutters that differ
   from the file's tokens. Bring the table back in line with the stylesheet, or the
   stylesheet with the table; the file now says the tokens win over the pictures.
4. **Small cosmetic items**, none blocking: `--init` without `--topic` titles the page
   "My My Focus"; the default document title is still "Canva Planner Set" in
   `planner_factory.py` and `references/SPECIFICATION.md`, so change both or neither;
   `planner_studio.py` accepts `--host 0.0.0.0` with no authentication and its help text
   does not say so; the README's structure block omits `LICENSE`,
   `RIGHTS_AND_ATTRIBUTION.md` and `.github/` while `HOW_IT_WORKS.md` lists `.github/`.
