# 04_check/CONTEXT.md: Layer 2 · Stage Contract

**One job:** find out whether the planner is fit to export. Change nothing.

The validator sees geometry and repetition. It cannot see a clipped heading, a cramped
writing area or a prompt that is not worth answering. This stage renders a proof and
writes down what a person must judge.

## Inputs

| Layer | What | Where | Section |
|---|---|---|---|
| 4 (working) | The specification | `../03_spec/output/<slug>.json` | Full file |
| 4 (working) | The brief, for the sensitive-topic flag | `../01_brief/output/<slug>.brief.md` | Sensitive topic |
| 3 (reference) | The shape of the check report | `references/check-report-template.md` | Full file |
| 3 (reference) | What to look at in the browser | `../../HOW_IT_WORKS.md` | Reviewing generated pages |
| 3 (reference) | What a page must satisfy | `../../references/DESIGN_STANDARD.md` | Required checks |
| 3 (reference) | What a page's words must satisfy | `../../references/CONTENT_GUIDE.md` | Content review checklist |

## Process

Run the command from the project root.

1. Render the proof. This also validates, and prints every finding:

   ```bash
   python planner_factory.py stages/03_spec/output/<slug>.json stages/04_check/output/<slug>.proof.html
   ```

2. Copy `references/check-report-template.md` to `output/<slug>.check.md`. Record the exit
   code and every finding, word for word.
3. Give a verdict: **PASS** with exit 0, **PASS WITH WARNINGS** with exit 1, **FAIL** with
   exit 2 or no proof written.
4. On **FAIL**, go back to stage 03 and say what the report names. Do not edit the
   specification from this stage.
5. Leave the **Human review** list unticked. It is the person's to tick.

## Outputs

| Artifact | Location | Format |
|---|---|---|
| The check report | `output/<slug>.check.md` | Markdown, the template filled in |
| The proof | `output/<slug>.proof.html` | HTML, every page at true size |

## Human gate

The person opens the proof at 100% and in print preview, works through the Human review
list, and ticks **Approved for export** or sends it back. Stage 05 does not run until that
line is ticked.

## Next

`../05_export/CONTEXT.md`
