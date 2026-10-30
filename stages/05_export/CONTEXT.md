# 05_export/CONTEXT.md: Layer 2 · Stage Contract

**One job:** produce the files the creator keeps and imports. Nothing is decided or edited here.

## Inputs

| Layer | What | Where | Section |
|---|---|---|---|
| 4 (working) | The specification | `../03_spec/output/<slug>.json` | Full file |
| 4 (working) | The check report, approved | `../04_check/output/<slug>.check.md` | Header (the hash), Verdict, Decision |
| 3 (reference) | What each exported file is for | `references/deliverables.md` | Full file |
| 3 (reference) | The steps after export | `../../HOW_IT_WORKS.md` | Canva workflow |

## Process

Run commands from the project root.

1. Open the check report. Its verdict must not be **FAIL**, and the line
   `- [x] Approved for export` must be ticked by the person. If either is missing, stop and
   say which. Do not tick it yourself.
2. Confirm the specification is the one that was checked. Compute its SHA-256 and compare
   it with the hash in the report's header. If they differ, the file changed after approval:
   stop and go back to stage 04.

   ```bash
   python -c "import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest())" stages/03_spec/output/<slug>.json
   ```

3. Generate the finished planner:

   ```bash
   python planner_factory.py stages/03_spec/output/<slug>.json stages/05_export/output/<slug>.html
   ```

4. Copy the specification beside it, so the export folder holds everything the creator
   needs: `stages/03_spec/output/<slug>.json` to `stages/05_export/output/<slug>.json`.
5. Tell the person what was written and where, and point them at the Canva workflow for the
   import and the checks that follow it. If the report's Sensitive topic section says yes,
   repeat that the set still needs review by an appropriately qualified professional before
   it is published or sold. Export does not replace that review.

## Outputs

| Artifact | Location | Format |
|---|---|---|
| The finished planner | `output/<slug>.html` | HTML, self-contained, ready for Canva import |
| The editable project | `output/<slug>.json` | JSON, which Planner Studio can open again |

## Human gate

The person imports the HTML into Canva and checks every page there before treating the
planner as finished. A planner about mental health, trauma, disability, medication or crisis
is also reviewed by a qualified professional before publication. This is the end of the run.
