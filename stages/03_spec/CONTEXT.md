# 03_spec/CONTEXT.md: Layer 2 · Stage Contract

**One job:** turn the plan into a planner specification that validates cleanly.

This stage writes the JSON file the engine reads. Layout and wording both happen here,
because the validator judges them together.

## Inputs

| Layer | What | Where | Section |
|---|---|---|---|
| 4 (working) | The approved plan | `../02_pages/output/<slug>.plan.md` | Full file |
| 4 (working) | The brief, for the title, footer, tone and colour | `../01_brief/output/<slug>.brief.md` | Full file |
| 3 (reference) | The file format, field by field | `../../references/SPECIFICATION.md` | Full file |
| 3 (reference) | Standard block positions on the grid | `references/layout-recipes.md` | Full file |
| 3 (reference) | How a prompt should read | `../../references/CONTENT_GUIDE.md` | Prompt design, Content review checklist |
| 3 (reference) | The visual rules a page must obey | `../../references/DESIGN_STANDARD.md` | Canvas and geometry, Required checks |
| 3 (shared) | A specification to start from | `../../shared/planner_spec_template.json` | Full file |

## Process

Run commands from the project root.

1. Start from the template. Set `set_title` and `footer_label` from the brief.
2. For each plan row, write one page: `concept` word for word from the plan, a `title` of
   about 22 characters, a one-line `subtitle`, the brief's `theme`, and blocks laid out on
   the recipe that matches the row's composition.
3. Write every prompt, section title, checklist item and option so that it is specific,
   answerable and used nowhere else in the set. Prefer the standard content types; do not use
   `custom_html` unless the plan names an interaction no type can express.
4. Fill each page to y=980 or lower without crossing y=1030. Writing space is content.
5. Validate, and fix every finding before the gate:

   ```bash
   python planner_factory.py stages/03_spec/output/<slug>.json stages/04_check/output/<slug>.proof.html --validate-only
   ```

   Validation writes no file. Exit code 2 is an error, 1 a warning, 0 clean.

## Audit

| Check | Pass condition |
|---|---|
| Validation | Exit code 0, or every remaining warning is explained in the handoff note |
| Plan fidelity | One page per plan row, same order, same concepts |
| Sensitive topic | If the brief says yes, the named page carries the scope and support note |

## Outputs

| Artifact | Location | Format |
|---|---|---|
| The specification | `output/<slug>.json` | JSON, as `../../references/SPECIFICATION.md` describes |

## Human gate

The person may edit the file, or open it in Planner Studio and change it there. Do not start
stage 04 until they say it is ready.

## Next

`../04_check/CONTEXT.md`
