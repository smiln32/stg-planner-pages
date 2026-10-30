# Handoff

Written 2026-10-29, when the repository was laid out as an ICM workspace. It holds the state
of the work and what to do next. Why things are the way they are is in
[`DECISIONS.md`](DECISIONS.md).

## State

- The ICM structure is in place and `tests/test_stages.py` holds it. The walk in
  `records/icm-audit.md` passes.
- No planner has been taken through the five stages yet. Every stage's `output/` holds only
  `.gitkeep`.
- The engine and the Studio are unchanged. The tests gained `test_stages.py`, seven checks
  on the structure. CI now compiles `planner_studio.py` as well, reads the examples from
  `shared/examples/`, and carries the product's new name.
- An independent review on 2026-10-29 found seven gaps in the contracts: no way for stage
  05 to know the checked specification was the exported one, stale downstream files on a
  revision, stage 04 missing the inputs its report needs, an undefined warning note in
  stage 03, a wrong relative path in the report template, and two document claims. All
  seven are corrected. A second read found two more, also corrected: stage 04 took its
  verdict from generation, which exits 0 even with warnings, and a clean revision could
  leave an old warning note for stage 04 to read. The export gate is still contract-only.

## Rename to STG Planner Pages, 2026-10-29

The documents now link to `smiln32/stg-planner-pages`. The GitHub repository is still named
`planner-factory` until the owner renames it there; after that, repoint the local remote:

```bash
git remote set-url origin https://github.com/smiln32/stg-planner-pages.git
```

## Next

1. **A cold walk.** Give an assistant only "make me a planner about X" and watch it go from
   `CLAUDE.md` through all five stages without being told anything else. The contracts were
   written by the person who laid out the folders, not tried by a stranger. That is the real
   test of the structure. Include an interrupted revision and an edit to the specification
   after approval: those exercise the hash and the archive rule.
2. **Enforce the export gate in code**, if the cold walk shows an assistant ticking
   **Approved for export** itself. The sibling repository's `shared/tools/planner.py export`
   refuses an unapproved check and is the model.
