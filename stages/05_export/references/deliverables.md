# Deliverables

What stage 05 writes, and what each file is for.

| File | What it is | Who uses it |
|---|---|---|
| `<slug>.html` | The whole planner as one self-contained HTML document, one `<section>` per page at exactly 816 x 1056 | The creator, to import into a US Letter Canva design and to print from a browser |
| `<slug>.json` | The specification the HTML was generated from | The creator, to open in Planner Studio or hand back to stage 03 for a revision |

## What is not written here

- **A PDF.** This engine renders HTML only. Print to PDF from the browser at US Letter with
  no margins, or export from Canva after import.
- **Page images.** The HTML is ordinary text, borders and tables so Canva keeps them editable.
  Flattening it defeats the point.

## Naming

Both files share the run's slug, so a folder listing shows which planner they belong to
and `CONTEXT.md`'s "carry on with X" rule can find them.
