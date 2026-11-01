# Handoff

Written 2026-10-29, when the repository was laid out as an ICM workspace; brought up to date
2026-10-31. It holds the state of the work and what to do next. Why things are the way they
are is in [`DECISIONS.md`](DECISIONS.md).

## State

- The repository lives at `github.com/smiln32/stg-planner-pages`, public, created
  2026-10-30. `main` is at c9a9726 and matches the remote. The `drop-canva` branch holds the
  Canva removal and the pivot documents of 2026-10-31, listed below; merge it into `main`,
  push, and delete it.
- The ICM structure is in place and `tests/test_stages.py` holds it. The walk in
  `records/icm-audit.md` passes.
- No planner has been taken through the five stages yet. Every stage's `output/` holds only
  `.gitkeep`.
- The engine is unchanged in behaviour but for one fix: the overlap check in
  `planner_factory.py` raised `TypeError` on a numeric string coordinate such as `"28"`
  instead of reporting a finding. It now parses geometry once and compares integers, with a
  test. The suite is twenty-three checks. CI compiles `planner_studio.py` as well, reads the
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
- On 2026-10-31 `_config/design-system.md` and `studio/styles.css` were reconciled. The
  stylesheet's canvas went to `#ececec`, the value the document, the palette specimen and
  the page engine share; its literal colours became tokens; two near-duplicate blues and
  two greens collapsed into one each; and the preview footer took the engine's `#8c8c8c`.
  The document gained the tokens the Studio needed (`ink-soft` corrected, `chrome-soft`,
  `surface-soft`, `focus`, `sage-deep`, `error`), a hero type level, the real button and
  input sizes, and a note that the page preview's colours belong to the engine.
  `tests/test_design_tokens.py` fails if the stylesheet uses a colour the token table does
  not name, or names one nothing in `studio/` uses.
- On 2026-10-31 every Canva reference was removed. The deliverable is now a PDF printed from
  the browser; the HTML is the generation format and stays editable. The
  `data-document-role="page"` marker on each section stays because the tests and CI count
  pages by it.
- The product is pivoting to topical Bible studies quoting the NASB 2020; `DECISIONS.md`
  records the terms and `README.md`, `CLAUDE.md` and `HOW_IT_WORKS.md` describe the
  direction. The stage contracts, `references/`, `shared/` and the Studio still speak only
  of planners, which is accurate until the study build exists. No study has been briefed.
  Doctrinal review was proposed and the owner declined it as a rule; do not add it to
  `CLAUDE.md` or the contracts. The two program files keep their planner names until the
  owner chooses new ones.

## Next

1. **Rename the program files**, once the owner has chosen the names. `planner_factory.py`
   and `planner_studio.py` are named for the old product; "Planner Studio" in
   `_config/product.md`, the Studio's own title and the repository name are the same
   decision. The rename is mechanical: `git mv` the two files, change the import in the
   server, then update every reference in `tests/test_planner_factory.py` (sixteen),
   `tests/test_design_tokens.py`, `.github/workflows/validate.yml`, `CLAUDE.md`,
   `CONTEXT.md`, `README.md`, `HOW_IT_WORKS.md`, `references/SPECIFICATION.md`, the
   contracts of stages 03, 04 and 05, `records/icm-audit.md`, `_config/design-system.md`,
   `DECISIONS.md` and this file. Re-run the ICM audit walk afterwards, because the structure
   changed.
2. **The first study, through the stages as they are.** Give stage 01 a real study, six
   sessions on one subject, and take it through stage 02 only. The plan will show which
   pages the current blocks cannot express and how the whole-set uniqueness rule objects to
   a session shape that repeats. The engine changes in item 3 should come out of that plan,
   not out of a list.
3. **The study build**, in the order the first study demands:
   uniqueness per session rather than per set; the study content types (a passage with
   observation space, a cross-reference table, a memory-verse card, numbered discussion
   questions, a prayer page), each added to the engine, `references/SPECIFICATION.md` and an
   example; a study content guide, observation then interpretation then application; a verse
   count in stage 04 that fails above 500 and reports the proportion of the work that is
   Scripture; the NASB 2020 notice printed by stage 05, with the wording copied from
   lockman.org once; and a study example in `shared/examples/` to stand beside or replace the
   wellness ones.
4. **A cold walk.** Give an assistant only "make me a study about X" and watch it go from
   `CLAUDE.md` through all five stages without being told anything else. The contracts were
   written by the person who laid out the folders, not tried by a stranger. That is the real
   test of the structure. Include an interrupted revision and an edit to the specification
   after approval: those exercise the hash and the archive rule.
5. **Enforce the export gate in code**, if the cold walk shows an assistant ticking
   **Approved for export** itself. A small command that reads the check report, compares
   the hash and refuses to generate unless the line is ticked would do it.
6. **The page engine and the page standard disagree on two colours.**
   `references/DESIGN_STANDARD.md` gives block borders as `#606864` and rules as `#aeb7b2`;
   `planner_factory.py` draws them `#5c5c5c` and `#b9b9b9`, and the Studio preview copies
   the engine. Change the standard or the engine, not the Studio. Changing the engine alters
   every generated page and the approved reference HTML in `shared/examples/`, so if the
   engine moves, regenerate those and look at them.
7. **Small cosmetic items**, none blocking: `--init` without `--topic` titles the page
   "My My Focus"; `planner_studio.py` accepts `--host 0.0.0.0` with no authentication and
   its help text does not say so.
