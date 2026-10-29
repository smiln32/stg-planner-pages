# Decisions

What has been settled and why. Read the relevant part before arguing with a decision. What to
do next is in `HANDOFF.md`.

## The workspace

**This repository follows ICM, by choice.** Decided by the owner 2026-10-29. The workspace
follows the Interpretable Context Methodology of Jake Van Clief and David McDermott
(https://arxiv.org/abs/2603.16021), laid out the way the owner's sibling repository
`cw-planner-factory` already is, so an assistant moving between the two finds the same
shape. `CLAUDE.md` says where you are, `CONTEXT.md` routes, each stage's `CONTEXT.md` is its
contract, `_config/`, `references/` and `shared/` hold what is stable, and each stage's
`output/` holds what a run writes. Keep it so:

- A new step in the planner build is a new numbered stage with its own contract,
  `references/` and `output/`, not a script somewhere else.
- New reference material goes in `_config/`, `references/`, `shared/` or a stage's own
  `references/`, not at the root.
- After any change to the folder structure, re-run the walk in `records/icm-audit.md`.
  `tests/test_stages.py` fails if a stage loses its contract, a contract names a file that is
  not there, or the router stops naming a stage.

**Stage folders are `stages/NN_name/`, underscore, from 01.** The paper's Figure 2 style,
which the owner chose over the hyphenated `01-name` style on 2026-07-16 for all their
workspaces. The standalone ICM audit tool recognises only this dialect.

**The engine stays at the root.** `planner_factory.py`, `planner_studio.py`, `studio/`,
`tests/` and `assets/` did not move. The paper describes staged content work, not
application source, and keeping the engine where the commands, the tests and CI expect it
means the restructure changed no code path. The stages call the engine; they do not hold it.

**Five stages, matching the sibling.** `01_brief`, `02_pages`, `03_spec`, `04_check`,
`05_export`. The third is `spec` rather than the sibling's `edit` because here the assistant
writes the specification from the plan; there is no page library to build from.

**Moved documents keep their names.** `SPECIFICATION.md`, `DESIGN_STANDARD.md` and
`CONTENT_GUIDE.md` went to `references/` unrenamed so that links, history and the sibling's
`references/SPECIFICATION.md` still correspond. `PRODUCT.md` and `DESIGN.md` became
`_config/product.md` and `_config/design-system.md`, lower case like the sibling's
`_config/`, because they describe the Studio product rather than the printed page.

**`HOW_IT_WORKS.md` stays at the root.** It is written for a person setting the tool up, the
way the sibling's `MEMBER-GUIDE.md` is. The stage contracts route to its sections rather than
copy them.

**The chatbot prompt is kept, in `shared/`.** `new-chat-starter-prompt.md` is for someone
using an assistant that cannot read this folder. It duplicates what the stages say and
nothing regenerates it; `shared/CONTEXT.md` says so.

**Stage output is ignored by git.** A run is the creator's work, not the product. The
folders stay, held by `.gitkeep`, because a stage with no `output/` is not a stage.

**The root `output/` folder stays.** It holds the owner's scratch files and was already
ignored. The ignore rule became `/output/` so it no longer swallows the stages' own
`output/` folders.

**No tool enforces the export gate.** The sibling's export command refuses an unapproved
check; here stage 05's contract makes the same demand of the assistant and `HANDOFF.md`
lists the enforcement as a possible next step.
