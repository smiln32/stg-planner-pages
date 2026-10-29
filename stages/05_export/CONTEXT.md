# 05_export/CONTEXT.md: Layer 2 · Stage Contract

**One job:** produce the files the creator keeps and imports. Nothing is decided or edited here.

## Inputs

| Layer | What | Where | Section |
|---|---|---|---|
| 4 (working) | The specification | `../03_spec/output/<slug>.json` | Full file |
| 4 (working) | The check report, approved | `../04_check/output/<slug>.check.md` | Verdict, Decision |
| 3 (reference) | What each exported file is for | `references/deliverables.md` | Full file |
| 3 (reference) | The steps after export | `../../HOW_IT_WORKS.md` | Canva workflow |

## Process

Run commands from the project root.

1. Open the check report. Its verdict must not be **FAIL**, and the line
   `- [x] Approved for export` must be ticked by the person. If either is missing, stop and
   say which. Do not tick it yourself.
2. Confirm the specification has not changed since it was checked. If it has, go back to
   stage 04.
3. Generate the finished planner:

   ```bash
   python planner_factory.py stages/03_spec/output/<slug>.json stages/05_export/output/<slug>.html
   ```

4. Copy the specification beside it, so the export folder holds everything the creator
   needs: `stages/03_spec/output/<slug>.json` to `stages/05_export/output/<slug>.json`.
5. Tell the person what was written and where, and point them at the Canva workflow for the
   import and the checks that follow it.

## Outputs

| Artifact | Location | Format |
|---|---|---|
| The finished planner | `output/<slug>.html` | HTML, self-contained, ready for Canva import |
| The editable project | `output/<slug>.json` | JSON, which Planner Studio can open again |

## Human gate

The person imports the HTML into Canva and checks every page there before treating the
planner as finished. This is the end of the run.
