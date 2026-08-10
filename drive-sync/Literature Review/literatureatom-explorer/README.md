# LiteratureAtom Explorer

A local, dependency-free viewer for LiteratureAtom JSON extraction batches and companion validation reports.

## Run

Keep these files together:

- `index.html`
- `styles.css`
- `app.js`

Open `index.html` in a modern browser. No server or build step is required.

## Use

1. Click **Add JSON files** or drag multiple `.json` files onto the drop area.
2. Load atom arrays and their companion validation files together.
3. The viewer pairs batches primarily by `extraction_run_id`, with a conservative publication-ID + atom-count fallback for reports that omit the run ID.
4. Use **Atoms** to search, filter, sort, choose columns, inspect full records, and export subsets.
5. Use **Validation** to inspect normalized structural/schema/sufficiency checks and extraction limitations.
6. Use **Overview** and **Batches** for counts and cross-file consistency flags.

All file parsing occurs in the browser. The app does not upload data to a server.
