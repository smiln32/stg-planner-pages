# Handoff

Written 2026-10-29, when the repository was laid out as an ICM workspace. It holds the state
of the work and what to do next. Why things are the way they are is in
[`DECISIONS.md`](DECISIONS.md).

## State

- The ICM structure is in place and `tests/test_stages.py` holds it. The walk in
  `records/icm-audit.md` passes.
- No planner has been taken through the five stages yet. Every stage's `output/` holds only
  `.gitkeep`.
- The engine, the Studio, the tests and CI are unchanged apart from the paths to the
  examples, which moved to `shared/examples/`.

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
   test of the structure.
2. **Enforce the export gate in code**, if the cold walk shows an assistant ticking
   **Approved for export** itself. The sibling repository's `shared/tools/planner.py export`
   refuses an unapproved check and is the model.
3. **Decide what `.impeccable/design.json` was for.** It is deleted in the working tree and
   the deletion is not committed. Restore it or commit the removal.
4. **The README preview image alt text** reads `factory''s` with a doubled apostrophe.
