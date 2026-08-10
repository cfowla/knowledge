(() => {
  "use strict";

  const DEFAULT_COLUMNS = [
    "source_anchor.page",
    "atom_kind",
    "canonical_statement",
    "assertion_origin",
    "tags",
    "review_status"
  ];

  const COLUMN_DEFS = [
    { group: "Core", path: "atom_id", label: "Atom ID" },
    { group: "Core", path: "publication_id", label: "Publication ID" },
    { group: "Core", path: "atom_kind", label: "Kind" },
    { group: "Core", path: "canonical_statement", label: "Canonical statement" },
    { group: "Core", path: "assertion_origin", label: "Assertion origin" },
    { group: "Core", path: "review_status", label: "Review status" },
    { group: "Core", path: "tags", label: "Tags" },

    { group: "Source", path: "source_anchor.page", label: "Page" },
    { group: "Source", path: "source_anchor.section", label: "Section" },
    { group: "Source", path: "source_anchor.paragraph", label: "Paragraph" },
    { group: "Source", path: "source_anchor.sentence", label: "Sentence" },
    { group: "Source", path: "source_anchor.table", label: "Table" },
    { group: "Source", path: "source_anchor.table_row", label: "Table row" },
    { group: "Source", path: "source_anchor.table_column", label: "Table column" },
    { group: "Source", path: "source_anchor.figure", label: "Figure" },
    { group: "Source", path: "source_anchor.supplement", label: "Supplement" },
    { group: "Source", path: "source_anchor.verbatim_excerpt", label: "Verbatim excerpt" },

    { group: "Population", path: "population.label", label: "Population" },
    { group: "Population", path: "population.sample_size", label: "Sample size" },
    { group: "Population", path: "population.subgroup", label: "Subgroup" },
    { group: "Population", path: "population.inclusion_criteria", label: "Inclusion criteria" },
    { group: "Population", path: "population.exclusion_criteria", label: "Exclusion criteria" },

    { group: "Exposure", path: "exposures", label: "Exposures" },

    { group: "Outcome", path: "outcome.concept.text", label: "Outcome" },
    { group: "Outcome", path: "outcome.outcome_type", label: "Outcome type" },
    { group: "Outcome", path: "outcome.definition", label: "Outcome definition" },
    { group: "Outcome", path: "outcome.measurement_method", label: "Measurement method" },
    { group: "Outcome", path: "outcome.time_horizon_value", label: "Time horizon" },
    { group: "Outcome", path: "outcome.time_horizon_unit", label: "Time unit" },

    { group: "Quantitative result", path: "quantitative_result.effect_measure", label: "Effect measure" },
    { group: "Quantitative result", path: "quantitative_result.estimate", label: "Estimate" },
    { group: "Quantitative result", path: "quantitative_result.interval", label: "Interval" },
    { group: "Quantitative result", path: "quantitative_result.p_value", label: "P value" },
    { group: "Quantitative result", path: "quantitative_result.p_value_text", label: "P value text" },
    { group: "Quantitative result", path: "quantitative_result.adjusted", label: "Adjusted" },
    { group: "Quantitative result", path: "quantitative_result.adjustment_variables", label: "Adjustment variables" },
    { group: "Quantitative result", path: "quantitative_result.arms", label: "Arms" },
    { group: "Quantitative result", path: "quantitative_result.original_result_text", label: "Original result" },

    { group: "Provenance", path: "provenance.extraction_run_id", label: "Extraction run" },
    { group: "Provenance", path: "provenance.extractor_type", label: "Extractor type" },
    { group: "Provenance", path: "provenance.extractor_identifier", label: "Extractor" },
    { group: "Provenance", path: "provenance.model_name", label: "Model" },
    { group: "Provenance", path: "provenance.model_version", label: "Model version" },
    { group: "Provenance", path: "provenance.prompt_version", label: "Prompt version" },
    { group: "Provenance", path: "provenance.extracted_at", label: "Extracted at" },
    { group: "Provenance", path: "provenance.reviewer_identifier", label: "Reviewer" },
    { group: "Provenance", path: "provenance.reviewed_at", label: "Reviewed at" },
    { group: "Provenance", path: "provenance.input_document_hash", label: "Input hash" },

    { group: "Versioning", path: "schema_version", label: "Schema version" },
    { group: "Versioning", path: "atom_version", label: "Atom version" },
    { group: "Versioning", path: "created_at", label: "Created at" },
    { group: "Versioning", path: "supersedes_atom_id", label: "Supersedes atom" }
  ];

  const state = {
    files: [],
    atoms: [],
    batches: new Map(),
    validations: new Map(),
    unpairedValidations: [],
    visibleColumns: loadColumns(),
    sort: { path: "source_anchor.page", direction: "asc" },
    page: 1,
    pageSize: 50,
    filters: {
      search: "",
      run: "",
      kind: "",
      page: "",
      tag: "",
      review: "",
      quantOnly: false,
      populationOnly: false
    }
  };

  const $ = (id) => document.getElementById(id);

  const els = {
    fileInput: $("fileInput"),
    loadBtn: $("loadBtn"),
    clearBtn: $("clearBtn"),
    dropZone: $("dropZone"),
    workspace: $("workspace"),
    workspaceMeta: $("workspaceMeta"),
    workspaceTitle: $("workspaceTitle"),
    healthBadge: $("healthBadge"),
    overviewCards: $("overviewCards"),
    kindSummary: $("kindSummary"),
    healthSummary: $("healthSummary"),
    overviewBatches: $("overviewBatches"),
    searchInput: $("searchInput"),
    runFilter: $("runFilter"),
    kindFilter: $("kindFilter"),
    pageFilter: $("pageFilter"),
    tagFilter: $("tagFilter"),
    reviewFilter: $("reviewFilter"),
    quantOnly: $("quantOnly"),
    populationOnly: $("populationOnly"),
    filteredCount: $("filteredCount"),
    atomTable: $("atomTable"),
    pageSize: $("pageSize"),
    pageStatus: $("pageStatus"),
    prevPage: $("prevPage"),
    nextPage: $("nextPage"),
    columnsBtn: $("columnsBtn"),
    resetFiltersBtn: $("resetFiltersBtn"),
    exportBtn: $("exportBtn"),
    exportMenu: $("exportMenu"),
    validationRun: $("validationRun"),
    validationView: $("validationView"),
    batchView: $("batchView"),
    columnsModal: $("columnsModal"),
    columnGroups: $("columnGroups"),
    defaultColumnsBtn: $("defaultColumnsBtn"),
    selectAllColumnsBtn: $("selectAllColumnsBtn"),
    clearColumnsBtn: $("clearColumnsBtn"),
    detailDrawer: $("detailDrawer"),
    drawerBackdrop: $("drawerBackdrop"),
    closeDrawer: $("closeDrawer"),
    drawerEyebrow: $("drawerEyebrow"),
    drawerTitle: $("drawerTitle"),
    drawerBody: $("drawerBody"),
    toast: $("toast")
  };

  function loadColumns() {
    try {
      const parsed = JSON.parse(localStorage.getItem("literatureAtomExplorer.columns"));
      if (Array.isArray(parsed) && parsed.length) {
        return parsed.filter(path => COLUMN_DEFS.some(c => c.path === path));
      }
    } catch (_) {}
    return [...DEFAULT_COLUMNS];
  }

  function saveColumns() {
    localStorage.setItem("literatureAtomExplorer.columns", JSON.stringify(state.visibleColumns));
  }

  function escapeHTML(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function getPath(obj, path) {
    return path.split(".").reduce((acc, key) => acc == null ? undefined : acc[key], obj);
  }

  function valuePresent(v) {
    if (v === null || v === undefined || v === "") return false;
    if (Array.isArray(v)) return v.length > 0;
    if (typeof v === "object") return Object.keys(v).length > 0;
    return true;
  }

  function formatPlain(v) {
    if (!valuePresent(v)) return "—";
    if (Array.isArray(v)) return v.map(x => typeof x === "object" ? summarizeObject(x) : String(x)).join("; ");
    if (typeof v === "object") return summarizeObject(v);
    if (typeof v === "boolean") return v ? "Yes" : "No";
    return String(v);
  }

  function summarizeObject(obj) {
    if (!obj || typeof obj !== "object") return String(obj ?? "");
    if (obj.text) return String(obj.text);
    if (obj.concept?.text) return String(obj.concept.text);
    if (obj.label) return String(obj.label);
    if (obj.lower !== undefined || obj.upper !== undefined) {
      return [obj.lower, obj.upper].filter(v => v !== undefined && v !== null).join("–");
    }
    const parts = Object.entries(obj)
      .filter(([,v]) => valuePresent(v) && typeof v !== "object")
      .slice(0, 4)
      .map(([k,v]) => `${k}: ${v}`);
    return parts.length ? parts.join("; ") : JSON.stringify(obj);
  }

  function inferRunFromFilename(name) {
    return name
      .replace(/\.json$/i, "")
      .replace(/[.-](atoms?|validation)$/i, "")
      .replace(/-validation$/i, "")
      .replace(/-atoms?$/i, "");
  }

  function getValidationRun(data, fileName) {
    const sm = data?.source_metadata || {};
    return sm.extraction_run_id ||
      sm.extraction_label ||
      data.extraction_run_id ||
      inferRunFromFilename(fileName);
  }

  function classifyJSON(data) {
    if (Array.isArray(data) && data.every(x => x && typeof x === "object")) {
      const atomLike = data.length === 0 || data.some(x => "atom_id" in x || "canonical_statement" in x);
      return atomLike ? "atoms" : "array";
    }
    if (data && typeof data === "object") {
      const looksValidation =
        "validation" in data ||
        "structural_validation" in data ||
        "serialization_schema_validation" in data ||
        "sufficiency_validation" in data ||
        "atom_counts" in data ||
        "atom_summary" in data ||
        "atom_count_total" in data;
      return looksValidation ? "validation" : "object";
    }
    return "unknown";
  }

  async function handleFiles(fileList) {
    const files = [...fileList].filter(f => f.name.toLowerCase().endsWith(".json"));
    if (!files.length) {
      showToast("No .json files selected.");
      return;
    }

    let added = 0;
    let failures = [];

    for (const file of files) {
      try {
        const text = await file.text();
        const data = JSON.parse(text);
        const type = classifyJSON(data);
        const fingerprint = `${file.name}:${file.size}:${file.lastModified}`;
        if (state.files.some(f => f.fingerprint === fingerprint)) continue;

        state.files.push({ name: file.name, type, fingerprint, data });
        added++;

        if (type === "atoms") addAtomBatch(file.name, data);
        else if (type === "validation") addValidation(file.name, data);
        else failures.push(`${file.name}: recognized JSON, but not an atom array or validation report`);
      } catch (err) {
        failures.push(`${file.name}: ${err.message}`);
      }
    }

    pairValidations();
    state.page = 1;
    renderAll();

    if (added) showToast(`Loaded ${added} JSON file${added === 1 ? "" : "s"}.`);
    if (failures.length) {
      setTimeout(() => showToast(failures.join(" | ")), 900);
    }
  }

  function addAtomBatch(fileName, atoms) {
    const run = atoms.find(a => a?.provenance?.extraction_run_id)?.provenance?.extraction_run_id
      || inferRunFromFilename(fileName);

    const enriched = atoms.map((atom, index) => ({
      ...atom,
      __viewer: { fileName, run, rowIndex: index }
    }));

    const existing = state.batches.get(run);
    if (existing) {
      existing.files.add(fileName);
      existing.atoms.push(...enriched);
    } else {
      state.batches.set(run, {
        run,
        files: new Set([fileName]),
        atoms: enriched,
        validation: null
      });
    }

    state.atoms.push(...enriched);
  }

  function addValidation(fileName, data) {
    const run = getValidationRun(data, fileName);
    const normalized = normalizeValidation(data, fileName, run);
    if (!state.validations.has(run)) state.validations.set(run, []);
    state.validations.get(run).push(normalized);
  }

  function pairValidations() {
    state.unpairedValidations = [];
    for (const [run, reports] of state.validations.entries()) {
      const batch = state.batches.get(run);
      if (batch) {
        batch.validation = reports[0];
      } else {
        state.unpairedValidations.push(...reports);
      }
    }

    // Secondary fallback: match orphaned validation to atom batch by publication ID + count.
    for (const report of [...state.unpairedValidations]) {
      const candidates = [...state.batches.values()].filter(batch => {
        const pub = batch.atoms.find(a => a.publication_id)?.publication_id;
        const expected = report.reportedAtomCount;
        return pub && report.publicationId === pub &&
          (!expected || expected === batch.atoms.length) &&
          !batch.validation;
      });
      if (candidates.length === 1) {
        candidates[0].validation = report;
        state.unpairedValidations = state.unpairedValidations.filter(r => r !== report);
      }
    }
  }

  function normalizeValidation(data, fileName, run) {
    const validation = data.validation || {};

    const structural = normalizeCheck(
      data.structural_validation ||
      {
        valid: validation.pydantic_structural_valid ??
          validation.all_atoms_structurally_valid ??
          inferFromErrorArray(validation.pydantic_structural_errors),
        errors: validation.pydantic_structural_errors
      }
    );

    const schema = normalizeCheck(
      data.serialization_schema_validation ||
      {
        valid: validation.json_schema_valid ??
          validation.all_atoms_schema_valid ??
          inferFromErrorArray(validation.json_schema_errors),
        errors: validation.json_schema_errors
      }
    );

    const sufficiency = normalizeCheck(
      data.sufficiency_validation ||
      {
        valid: validation.sufficiency_valid ??
          validation.all_atoms_sufficient_for_declared_kind ??
          inferFromErrorArray(validation.sufficiency_errors),
        errors: validation.sufficiency_errors,
        warnings: validation.sufficiency_warnings
      }
    );

    const sm = data.source_metadata || {};
    return {
      fileName,
      run,
      raw: data,
      sourceMetadata: sm,
      publicationId: sm.publication_id || null,
      doi: sm.doi || null,
      structural,
      schema,
      sufficiency,
      limitations: Array.isArray(data.extraction_limitations) ? data.extraction_limitations : [],
      boundaries: data.extraction_boundaries || null,
      reportedAtomCount: getReportedAtomCount(data)
    };
  }

  function inferFromErrorArray(errors) {
    return Array.isArray(errors) ? errors.length === 0 : null;
  }

  function normalizeCheck(check) {
    if (!check || typeof check !== "object") return { valid: null, errors: [], warnings: [] };
    let valid = check.valid;
    if (typeof valid === "string") valid = /^(passed|pass|true|valid)$/i.test(valid);
    if (valid === undefined && "error_count" in check) valid = Number(check.error_count) === 0;
    return {
      valid: valid === undefined ? null : Boolean(valid),
      errors: Array.isArray(check.errors) ? check.errors : [],
      warnings: Array.isArray(check.warnings) ? check.warnings : []
    };
  }

  function getReportedAtomCount(data) {
    return data.atom_count ??
      data.atom_count_total ??
      data.atom_counts?.total ??
      data.atom_summary?.total_atoms ??
      null;
  }

  function renderAll() {
    const hasData = state.atoms.length || state.validations.size;
    els.workspace.classList.toggle("hidden", !hasData);
    els.clearBtn.disabled = !hasData;
    if (!hasData) return;

    const pubCount = new Set(state.atoms.map(a => a.publication_id).filter(Boolean)).size;
    const pageValues = state.atoms.map(a => String(a.source_anchor?.page ?? "")).filter(Boolean);
    els.workspaceTitle.textContent = "LiteratureAtom workspace";
    els.workspaceMeta.textContent =
      `${state.atoms.length.toLocaleString()} atoms · ${state.batches.size} extraction run${state.batches.size === 1 ? "" : "s"} · ${pubCount || 0} publication ID${pubCount === 1 ? "" : "s"}${pageValues.length ? ` · pages ${summarizePages(pageValues)}` : ""}`;

    populateFilters();
    renderOverview();
    renderAtomTable();
    renderValidationSelector();
    renderBatches();
    renderColumns();
  }

  function summarizePages(values) {
    const nums = [];
    const nonNumeric = [];
    for (const v of values) {
      const m = v.match(/^\d+$/);
      if (m) nums.push(Number(v));
      else nonNumeric.push(v);
    }
    if (!nums.length) return [...new Set(nonNumeric)].slice(0,5).join(", ");
    const min = Math.min(...nums);
    const max = Math.max(...nums);
    return min === max ? String(min) : `${min}–${max}`;
  }

  function populateFilters() {
    refillSelect(els.runFilter, ["", ...[...state.batches.keys()].sort()], state.filters.run, "All runs");
    refillSelect(
      els.kindFilter,
      ["", ...uniqueSorted(state.atoms.map(a => a.atom_kind))],
      state.filters.kind,
      "All kinds"
    );
    refillSelect(
      els.reviewFilter,
      ["", ...uniqueSorted(state.atoms.map(a => a.review_status))],
      state.filters.review,
      "All"
    );
  }

  function refillSelect(select, values, current, emptyLabel) {
    select.innerHTML = "";
    for (const value of values) {
      const option = document.createElement("option");
      option.value = value;
      option.textContent = value || emptyLabel;
      if (value === current) option.selected = true;
      select.append(option);
    }
  }

  function uniqueSorted(values) {
    return [...new Set(values.filter(v => v !== null && v !== undefined && v !== ""))]
      .sort((a,b) => String(a).localeCompare(String(b), undefined, { numeric: true }));
  }

  function renderOverview() {
    const validationReports = [...state.batches.values()].filter(b => b.validation).length;
    const publications = new Set(state.atoms.map(a => a.publication_id).filter(Boolean));
    const pages = new Set(state.atoms.map(a => a.source_anchor?.page).filter(valuePresent));

    const metrics = [
      ["Atoms", state.atoms.length.toLocaleString()],
      ["Extraction runs", state.batches.size.toLocaleString()],
      ["Validation reports", validationReports.toLocaleString()],
      ["Source pages", pages.size.toLocaleString()]
    ];

    els.overviewCards.innerHTML = metrics.map(([label, value]) =>
      `<div class="metric"><div class="label">${escapeHTML(label)}</div><div class="value">${escapeHTML(value)}</div></div>`
    ).join("");

    const kindCounts = countBy(state.atoms, a => a.atom_kind || "unknown");
    const max = Math.max(1, ...Object.values(kindCounts));
    els.kindSummary.innerHTML = Object.entries(kindCounts)
      .sort((a,b) => b[1] - a[1])
      .map(([kind,count]) => `
        <div>
          <div class="summary-row"><span>${escapeHTML(kind)}</span><span class="count">${count}</span></div>
          <div class="meter"><span style="width:${Math.max(2, count / max * 100)}%"></span></div>
        </div>
      `).join("");

    const health = computeHealth();
    const severity = health.some(h => h.level === "error") ? "error" :
      health.some(h => h.level === "warn") ? "warn" : "ok";
    const healthLabel = severity === "ok" ? "No consistency issues" :
      `${health.filter(h => h.level !== "ok").length} data-health flag${health.filter(h => h.level !== "ok").length === 1 ? "" : "s"}`;
    els.healthBadge.className = `health-badge ${severity}`;
    els.healthBadge.textContent = healthLabel;

    els.healthSummary.innerHTML = `<div class="health-list">${health.map(item => `
      <div class="health-item ${item.level}">
        <strong>${escapeHTML(item.title)}</strong>
        <span>${escapeHTML(item.detail)}</span>
      </div>
    `).join("")}</div>`;

    els.overviewBatches.innerHTML = [...state.batches.values()]
      .sort((a,b) => a.run.localeCompare(b.run))
      .map(batchCardHTML)
      .join("");
  }

  function computeHealth() {
    const items = [];

    const pubGroups = groupBy(state.atoms, a => a.publication_id || "(missing)");
    const realPubs = Object.keys(pubGroups).filter(x => x !== "(missing)");
    if (realPubs.length > 1) {
      items.push({
        level: "warn",
        title: "Publication identity mismatch",
        detail: `${realPubs.length} publication IDs occur across loaded atom batches. The viewer does not reconcile them automatically.`
      });
    } else {
      items.push({
        level: "ok",
        title: "Publication identity",
        detail: realPubs.length === 1 ? "Loaded atom batches share one publication ID." : "No publication IDs available."
      });
    }

    const hashes = uniqueSorted(state.atoms.map(a => normalizeHash(a.provenance?.input_document_hash)));
    if (hashes.length > 1) {
      items.push({
        level: "warn",
        title: "Input document hash mismatch",
        detail: `${hashes.length} distinct normalized input hashes found.`
      });
    } else if (hashes.length === 1) {
      items.push({ level: "ok", title: "Input document hash", detail: "Loaded atoms share one normalized source-document hash." });
    }

    const schemaVersions = uniqueSorted(state.atoms.map(a => a.schema_version));
    if (schemaVersions.length > 1) {
      items.push({ level: "warn", title: "Schema versions differ", detail: schemaVersions.join(", ") });
    } else if (schemaVersions.length === 1) {
      items.push({ level: "ok", title: "Schema version", detail: `All loaded atoms report schema ${schemaVersions[0]}.` });
    }

    const atomIds = state.atoms.map(a => a.atom_id).filter(Boolean);
    const dupIds = atomIds.filter((id, i) => atomIds.indexOf(id) !== i);
    if (dupIds.length) {
      items.push({ level: "error", title: "Duplicate atom IDs", detail: `${new Set(dupIds).size} duplicate atom ID${new Set(dupIds).size === 1 ? "" : "s"} detected.` });
    } else {
      items.push({ level: "ok", title: "Atom IDs", detail: "No duplicate atom IDs detected." });
    }

    const missingValidation = [...state.batches.values()].filter(b => !b.validation);
    if (missingValidation.length) {
      items.push({
        level: "warn",
        title: "Validation companions missing",
        detail: `${missingValidation.length} atom batch${missingValidation.length === 1 ? "" : "es"} have no paired validation report.`
      });
    } else if (state.batches.size) {
      items.push({ level: "ok", title: "Validation pairing", detail: "Each loaded atom batch has a paired validation report." });
    }

    const countMismatches = [...state.batches.values()].filter(b =>
      b.validation?.reportedAtomCount != null && Number(b.validation.reportedAtomCount) !== b.atoms.length
    );
    if (countMismatches.length) {
      items.push({
        level: "error",
        title: "Atom-count mismatch",
        detail: `${countMismatches.length} batch${countMismatches.length === 1 ? "" : "es"} disagree with their validation-reported atom count.`
      });
    } else if ([...state.batches.values()].some(b => b.validation?.reportedAtomCount != null)) {
      items.push({ level: "ok", title: "Atom counts", detail: "Loaded atom counts agree with available validation reports." });
    }

    if (state.unpairedValidations.length) {
      items.push({
        level: "warn",
        title: "Unpaired validation reports",
        detail: `${state.unpairedValidations.length} validation report${state.unpairedValidations.length === 1 ? "" : "s"} could not be paired to an atom batch.`
      });
    }

    return items;
  }

  function normalizeHash(hash) {
    if (!hash) return null;
    return String(hash).replace(/^sha256:/i, "").trim().toLowerCase();
  }

  function batchCardHTML(batch) {
    const pageValues = batch.atoms.map(a => String(a.source_anchor?.page ?? "")).filter(Boolean);
    const valid = batch.validation ? validationOverall(batch.validation) : null;
    return `
      <div class="batch-card">
        <div class="batch-name">${escapeHTML(batch.run)}</div>
        <div class="batch-stat"><strong>${batch.atoms.length}</strong> atoms</div>
        <div class="batch-stat">${pageValues.length ? `pages <strong>${escapeHTML(summarizePages(pageValues))}</strong>` : "pages —"}</div>
        <div class="batch-stat">${valid === true ? '<span class="status-pill ok">Validated</span>' :
          valid === false ? '<span class="status-pill warn">Validation issues</span>' :
          '<span class="small-pill">No validation</span>'}</div>
      </div>
    `;
  }

  function validationOverall(report) {
    const checks = [report.structural.valid, report.schema.valid, report.sufficiency.valid].filter(v => v !== null);
    if (!checks.length) return null;
    return checks.every(Boolean);
  }

  function getFilteredAtoms() {
    const f = state.filters;
    let rows = state.atoms.filter(atom => {
      if (f.run && atom.__viewer?.run !== f.run) return false;
      if (f.kind && atom.atom_kind !== f.kind) return false;
      if (f.review && atom.review_status !== f.review) return false;
      if (f.quantOnly && !atom.quantitative_result) return false;
      if (f.populationOnly && !atom.population) return false;

      if (f.tag) {
        const needle = f.tag.toLowerCase().trim();
        if (!(atom.tags || []).some(t => String(t).toLowerCase().includes(needle))) return false;
      }

      if (f.page && !pageMatches(atom.source_anchor?.page, f.page)) return false;

      if (f.search) {
        const haystack = searchableText(atom);
        const terms = f.search.toLowerCase().trim().split(/\s+/).filter(Boolean);
        if (!terms.every(term => haystack.includes(term))) return false;
      }
      return true;
    });

    rows = [...rows].sort((a,b) => compareAtoms(a,b,state.sort.path,state.sort.direction));
    return rows;
  }

  function pageMatches(value, query) {
    if (!valuePresent(value)) return false;
    const source = String(value).trim();
    const q = query.trim();
    const range = q.match(/^(\d+)\s*-\s*(\d+)$/);
    if (range) {
      const start = Number(range[1]), end = Number(range[2]);
      const nums = [...source.matchAll(/\d+/g)].map(m => Number(m[0]));
      return nums.some(n => n >= start && n <= end);
    }
    return source.toLowerCase().includes(q.toLowerCase());
  }

  function searchableText(atom) {
    const values = [
      atom.canonical_statement,
      atom.atom_kind,
      atom.assertion_origin,
      atom.review_status,
      ...(atom.tags || []),
      atom.source_anchor?.page,
      atom.source_anchor?.section,
      atom.source_anchor?.paragraph,
      atom.source_anchor?.verbatim_excerpt,
      atom.population?.label,
      atom.outcome?.concept?.text,
      atom.outcome?.definition,
      atom.quantitative_result?.effect_measure,
      atom.quantitative_result?.estimate,
      atom.quantitative_result?.original_result_text,
      atom.provenance?.extraction_run_id,
      ...((atom.exposures || []).map(x => x?.concept?.text))
    ];
    return values.filter(valuePresent).map(v => String(v).toLowerCase()).join(" ");
  }

  function compareAtoms(a,b,path,direction) {
    const va = getPath(a,path);
    const vb = getPath(b,path);
    const dir = direction === "desc" ? -1 : 1;

    if (!valuePresent(va) && !valuePresent(vb)) return 0;
    if (!valuePresent(va)) return 1;
    if (!valuePresent(vb)) return -1;

    const na = Number(va), nb = Number(vb);
    if (!Number.isNaN(na) && !Number.isNaN(nb) && String(va).trim() !== "" && String(vb).trim() !== "") {
      return (na - nb) * dir;
    }
    return String(formatPlain(va)).localeCompare(String(formatPlain(vb)), undefined, { numeric: true }) * dir;
  }

  function renderAtomTable() {
    const rows = getFilteredAtoms();
    state.pageSize = Number(els.pageSize.value || state.pageSize);
    const totalPages = Math.max(1, Math.ceil(rows.length / state.pageSize));
    if (state.page > totalPages) state.page = totalPages;
    const start = (state.page - 1) * state.pageSize;
    const pageRows = rows.slice(start, start + state.pageSize);

    const columns = state.visibleColumns
      .map(path => COLUMN_DEFS.find(c => c.path === path))
      .filter(Boolean);

    els.atomTable.querySelector("thead").innerHTML = `<tr>${columns.map(col => {
      const indicator = state.sort.path === col.path ? (state.sort.direction === "asc" ? " ↑" : " ↓") : "";
      return `<th><button type="button" data-sort="${escapeHTML(col.path)}">${escapeHTML(col.label)}${indicator}</button></th>`;
    }).join("")}</tr>`;

    const tbody = els.atomTable.querySelector("tbody");
    if (!pageRows.length) {
      tbody.innerHTML = `<tr><td colspan="${Math.max(1, columns.length)}"><div class="empty-state">No atoms match the current filters.</div></td></tr>`;
    } else {
      tbody.innerHTML = pageRows.map((atom, i) => `
        <tr class="clickable" data-index="${state.atoms.indexOf(atom)}" tabindex="0">
          ${columns.map(col => renderCell(atom, col)).join("")}
        </tr>
      `).join("");
    }

    const shownStart = rows.length ? start + 1 : 0;
    const shownEnd = Math.min(rows.length, start + state.pageSize);
    els.filteredCount.textContent = `${rows.length.toLocaleString()} of ${state.atoms.length.toLocaleString()} atoms`;
    els.pageStatus.textContent = `Showing ${shownStart.toLocaleString()}–${shownEnd.toLocaleString()} of ${rows.length.toLocaleString()} · page ${state.page} of ${totalPages}`;
    els.prevPage.disabled = state.page <= 1;
    els.nextPage.disabled = state.page >= totalPages;

    els.atomTable.querySelectorAll("[data-sort]").forEach(btn => {
      btn.addEventListener("click", e => {
        e.stopPropagation();
        const path = btn.dataset.sort;
        if (state.sort.path === path) state.sort.direction = state.sort.direction === "asc" ? "desc" : "asc";
        else state.sort = { path, direction: "asc" };
        state.page = 1;
        renderAtomTable();
      });
    });

    tbody.querySelectorAll("tr[data-index]").forEach(row => {
      row.addEventListener("click", () => openDrawer(state.atoms[Number(row.dataset.index)]));
      row.addEventListener("keydown", e => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          openDrawer(state.atoms[Number(row.dataset.index)]);
        }
      });
    });

    tbody.querySelectorAll("button.tag").forEach(btn => {
      btn.addEventListener("click", e => {
        e.stopPropagation();
        state.filters.tag = btn.dataset.tag;
        els.tagFilter.value = btn.dataset.tag;
        state.page = 1;
        renderAtomTable();
      });
    });
  }

  function renderCell(atom, col) {
    const v = getPath(atom, col.path);
    const cls = col.path === "canonical_statement" ? "cell-statement" :
      col.path === "source_anchor.page" ? "cell-page" :
      col.path === "tags" ? "cell-tags" : "";

    if (col.path === "tags") {
      const tags = Array.isArray(v) ? v : [];
      return `<td class="${cls}"><div class="tags">${tags.length ? tags.map(t =>
        `<button type="button" class="tag" data-tag="${escapeHTML(t)}" title="Filter by ${escapeHTML(t)}">${escapeHTML(t)}</button>`
      ).join("") : "—"}</div></td>`;
    }

    if (col.path === "atom_kind") {
      return `<td class="${cls}">${valuePresent(v) ? `<span class="kind-badge">${escapeHTML(v)}</span>` : "—"}</td>`;
    }

    if (col.path === "review_status") {
      const statusClass = String(v).toLowerCase().includes("review") ? "warn" : "ok";
      return `<td class="${cls}">${valuePresent(v) ? `<span class="status-pill ${statusClass}">${escapeHTML(v)}</span>` : "—"}</td>`;
    }

    if (col.path === "canonical_statement") {
      return `<td class="${cls}"><div class="truncate" title="${escapeHTML(formatPlain(v))}">${escapeHTML(formatPlain(v))}</div></td>`;
    }

    return `<td class="${cls}">${escapeHTML(formatPlain(v))}</td>`;
  }

  function renderValidationSelector() {
    const paired = [...state.batches.values()].filter(b => b.validation);
    const current = els.validationRun.value;
    els.validationRun.innerHTML = "";

    if (!paired.length && !state.unpairedValidations.length) {
      els.validationView.innerHTML = `<div class="empty-state">No validation reports loaded.</div>`;
      return;
    }

    for (const batch of paired) {
      const option = document.createElement("option");
      option.value = batch.run;
      option.textContent = batch.run;
      els.validationRun.append(option);
    }
    state.unpairedValidations.forEach((report, i) => {
      const option = document.createElement("option");
      option.value = `__orphan_${i}`;
      option.textContent = `${report.run} (unpaired)`;
      els.validationRun.append(option);
    });

    if ([...els.validationRun.options].some(o => o.value === current)) {
      els.validationRun.value = current;
    }
    renderValidationView();
  }

  function renderValidationView() {
    const key = els.validationRun.value;
    let report;
    let batch = null;
    if (key.startsWith("__orphan_")) {
      report = state.unpairedValidations[Number(key.replace("__orphan_",""))];
    } else {
      batch = state.batches.get(key);
      report = batch?.validation;
    }

    if (!report) {
      els.validationView.innerHTML = `<div class="empty-state">Select a validation report.</div>`;
      return;
    }

    const checks = [
      ["Structural", report.structural],
      ["JSON Schema", report.schema],
      ["Sufficiency", report.sufficiency]
    ];

    const metadata = report.sourceMetadata || {};
    const reportedCount = report.reportedAtomCount;
    const actualCount = batch?.atoms.length ?? null;

    els.validationView.innerHTML = `
      <div class="validation-status-grid">
        ${checks.map(([name, check]) => validationCardHTML(name, check)).join("")}
      </div>

      <section class="panel">
        <div class="panel-heading"><h2>Report summary</h2></div>
        <div class="batch-meta-grid">
          ${metaBox("Run", report.run)}
          ${metaBox("Validation file", report.fileName)}
          ${metaBox("Reported atoms", reportedCount ?? "—")}
          ${metaBox("Loaded atoms", actualCount ?? "—")}
          ${metaBox("Publication ID", report.publicationId ?? "—")}
          ${metaBox("DOI", report.doi ?? "—")}
          ${metaBox("Page scope", metadata.page_range_inclusive || metadata.parsed_page_scope || metadata.requested_page_range || metadata.extraction_scope || metadata.content_scope || "—")}
          ${metaBox("Source type", metadata.source_type || "—")}
        </div>
      </section>

      ${report.limitations.length ? `
        <details open>
          <summary>Extraction limitations (${report.limitations.length})</summary>
          <div class="details-body"><ul>${report.limitations.map(x => `<li>${escapeHTML(x)}</li>`).join("")}</ul></div>
        </details>` : ""}

      ${report.boundaries ? `
        <details>
          <summary>Extraction boundaries</summary>
          <div class="details-body">${renderBoundary(report.boundaries)}</div>
        </details>` : ""}

      <details>
        <summary>Raw validation JSON</summary>
        <div class="details-body"><pre>${escapeHTML(JSON.stringify(report.raw, null, 2))}</pre></div>
      </details>
    `;
  }

  function validationCardHTML(name, check) {
    const stateClass = check.valid === true ? "ok" : check.valid === false ? "error" : "warn";
    const stateText = check.valid === true ? "Passed" : check.valid === false ? "Failed" : "Unknown";
    return `
      <div class="validation-card ${stateClass}">
        <div class="state">${escapeHTML(stateText)}</div>
        <strong>${escapeHTML(name)}</strong>
        <div class="desc">${check.errors.length} error${check.errors.length === 1 ? "" : "s"} · ${check.warnings.length} warning${check.warnings.length === 1 ? "" : "s"}</div>
      </div>`;
  }

  function renderBoundary(boundaries) {
    if (Array.isArray(boundaries)) return `<ul>${boundaries.map(x => `<li>${escapeHTML(x)}</li>`).join("")}</ul>`;
    if (!boundaries || typeof boundaries !== "object") return escapeHTML(formatPlain(boundaries));
    return Object.entries(boundaries).map(([key,val]) => `
      <h3>${escapeHTML(key)}</h3>
      ${Array.isArray(val) ? `<ul>${val.map(x => `<li>${escapeHTML(x)}</li>`).join("")}</ul>` :
        `<p>${escapeHTML(formatPlain(val))}</p>`}
    `).join("");
  }

  function renderBatches() {
    const batches = [...state.batches.values()].sort((a,b) => a.run.localeCompare(b.run));
    if (!batches.length) {
      els.batchView.innerHTML = `<div class="empty-state">No atom batches loaded.</div>`;
      return;
    }

    els.batchView.innerHTML = batches.map(batch => {
      const pub = batch.atoms.find(a => a.publication_id)?.publication_id || "—";
      const hash = normalizeHash(batch.atoms.find(a => a.provenance?.input_document_hash)?.provenance?.input_document_hash) || "—";
      const kinds = countBy(batch.atoms, a => a.atom_kind || "unknown");
      const pages = batch.atoms.map(a => String(a.source_anchor?.page ?? "")).filter(Boolean);
      const validation = batch.validation;
      return `
        <section class="batch-card detail">
          <div class="panel-heading">
            <div>
              <h2 class="mono">${escapeHTML(batch.run)}</h2>
              <div class="muted">${[...batch.files].map(escapeHTML).join(", ")}</div>
            </div>
            ${validationOverall(validation) === true ? '<span class="status-pill ok">Validated</span>' :
              validation ? '<span class="status-pill warn">Review validation</span>' :
              '<span class="small-pill">No validation</span>'}
          </div>

          <div class="batch-meta-grid">
            ${metaBox("Atoms", batch.atoms.length)}
            ${metaBox("Pages", pages.length ? summarizePages(pages) : "—")}
            ${metaBox("Publication ID", pub)}
            ${metaBox("Input hash", hash)}
          </div>

          <div class="tags" style="margin-top:10px">
            ${Object.entries(kinds).sort((a,b) => b[1]-a[1]).map(([k,c]) => `<span class="tag">${escapeHTML(k)} · ${c}</span>`).join("")}
          </div>
        </section>`;
    }).join("");
  }

  function metaBox(k,v) {
    return `<div class="meta-box"><span class="k">${escapeHTML(k)}</span><span class="v">${escapeHTML(v)}</span></div>`;
  }

  function renderColumns() {
    const groups = [...new Set(COLUMN_DEFS.map(c => c.group))];
    els.columnGroups.innerHTML = groups.map(group => {
      const defs = COLUMN_DEFS.filter(c => c.group === group);
      return `
        <section class="column-group">
          <h3>${escapeHTML(group)}</h3>
          ${defs.map(def => {
            const selected = state.visibleColumns.includes(def.path);
            const pos = state.visibleColumns.indexOf(def.path);
            return `
              <div class="column-row">
                <input type="checkbox" data-column="${escapeHTML(def.path)}" ${selected ? "checked" : ""}>
                <div>
                  <div>${escapeHTML(def.label)}</div>
                  <div class="column-path">${escapeHTML(def.path)}</div>
                </div>
                <button type="button" class="reorder-button" data-move="up" data-path="${escapeHTML(def.path)}" ${!selected || pos <= 0 ? "disabled" : ""}>↑</button>
                <button type="button" class="reorder-button" data-move="down" data-path="${escapeHTML(def.path)}" ${!selected || pos < 0 || pos >= state.visibleColumns.length - 1 ? "disabled" : ""}>↓</button>
              </div>`;
          }).join("")}
        </section>`;
    }).join("");

    els.columnGroups.querySelectorAll("[data-column]").forEach(input => {
      input.addEventListener("change", () => {
        const path = input.dataset.column;
        if (input.checked) {
          if (!state.visibleColumns.includes(path)) state.visibleColumns.push(path);
        } else {
          state.visibleColumns = state.visibleColumns.filter(p => p !== path);
          if (!state.visibleColumns.length) state.visibleColumns = ["canonical_statement"];
        }
        saveColumns();
        renderColumns();
        renderAtomTable();
      });
    });

    els.columnGroups.querySelectorAll("[data-move]").forEach(btn => {
      btn.addEventListener("click", () => {
        const path = btn.dataset.path;
        const idx = state.visibleColumns.indexOf(path);
        if (idx < 0) return;
        const next = btn.dataset.move === "up" ? idx - 1 : idx + 1;
        if (next < 0 || next >= state.visibleColumns.length) return;
        [state.visibleColumns[idx], state.visibleColumns[next]] = [state.visibleColumns[next], state.visibleColumns[idx]];
        saveColumns();
        renderColumns();
        renderAtomTable();
      });
    });
  }

  function openDrawer(atom) {
    if (!atom) return;
    els.drawerEyebrow.textContent = `${atom.atom_kind || "atom"} · page ${atom.source_anchor?.page ?? "—"}`;
    els.drawerTitle.textContent = atom.provenance?.extraction_run_id || atom.__viewer?.run || "Atom detail";
    els.drawerBody.innerHTML = detailHTML(atom);
    els.detailDrawer.classList.add("open");
    els.detailDrawer.setAttribute("aria-hidden", "false");
    els.drawerBackdrop.classList.remove("hidden");

    els.drawerBody.querySelectorAll("[data-copy]").forEach(btn => {
      btn.addEventListener("click", async () => {
        const mode = btn.dataset.copy;
        const text = mode === "statement" ? atom.canonical_statement : JSON.stringify(stripViewer(atom), null, 2);
        try {
          await navigator.clipboard.writeText(text || "");
          showToast(mode === "statement" ? "Statement copied." : "Atom JSON copied.");
        } catch (_) {
          showToast("Clipboard access was unavailable.");
        }
      });
    });

    els.drawerBody.querySelectorAll("button.tag").forEach(btn => {
      btn.addEventListener("click", () => {
        state.filters.tag = btn.dataset.tag;
        els.tagFilter.value = btn.dataset.tag;
        closeDrawer();
        activateTab("atoms");
        state.page = 1;
        renderAtomTable();
      });
    });
  }

  function detailHTML(atom) {
    const q = atom.quantitative_result;
    const source = atom.source_anchor || {};
    const prov = atom.provenance || {};
    return `
      <section class="detail-section">
        <h3>Statement</h3>
        <div class="detail-statement">${escapeHTML(atom.canonical_statement || "—")}</div>
        <div style="margin-top:10px"><button class="button compact" data-copy="statement" type="button">Copy statement</button></div>
      </section>

      <section class="detail-section">
        <h3>Classification</h3>
        ${kvGrid([
          ["Atom ID", atom.atom_id],
          ["Kind", atom.atom_kind],
          ["Assertion origin", atom.assertion_origin],
          ["Review status", atom.review_status],
          ["Schema version", atom.schema_version],
          ["Atom version", atom.atom_version]
        ])}
      </section>

      ${atom.population ? `
        <section class="detail-section">
          <h3>Population</h3>
          ${kvGrid([
            ["Label", atom.population.label],
            ["Sample size", atom.population.sample_size],
            ["Subgroup", atom.population.subgroup],
            ["Inclusion criteria", atom.population.inclusion_criteria],
            ["Exclusion criteria", atom.population.exclusion_criteria]
          ])}
        </section>` : ""}

      ${Array.isArray(atom.exposures) && atom.exposures.length ? `
        <section class="detail-section">
          <h3>Exposures</h3>
          ${atom.exposures.map(exposureCard).join("")}
        </section>` : ""}

      ${atom.outcome ? `
        <section class="detail-section">
          <h3>Outcome</h3>
          ${kvGrid([
            ["Concept", atom.outcome.concept?.text],
            ["Definition", atom.outcome.definition],
            ["Outcome type", atom.outcome.outcome_type],
            ["Measurement", atom.outcome.measurement_method],
            ["Time horizon", [atom.outcome.time_horizon_value, atom.outcome.time_horizon_unit].filter(valuePresent).join(" ")]
          ])}
        </section>` : ""}

      ${q ? `
        <section class="detail-section">
          <h3>Quantitative result</h3>
          ${kvGrid([
            ["Effect measure", q.effect_measure],
            ["Estimate", q.estimate],
            ["Interval", q.interval],
            ["P value", q.p_value ?? q.p_value_text],
            ["Adjusted", q.adjusted],
            ["Adjustment variables", q.adjustment_variables],
            ["Original result", q.original_result_text]
          ])}
          ${Array.isArray(q.arms) && q.arms.length ? `
            <details style="margin-top:10px">
              <summary>Arms (${q.arms.length})</summary>
              <div class="details-body"><pre>${escapeHTML(JSON.stringify(q.arms, null, 2))}</pre></div>
            </details>` : ""}
        </section>` : ""}

      <section class="detail-section">
        <h3>Source</h3>
        ${kvGrid([
          ["Page", source.page],
          ["Section", source.section],
          ["Paragraph", source.paragraph],
          ["Sentence", source.sentence],
          ["Table", source.table],
          ["Table row", source.table_row],
          ["Table column", source.table_column],
          ["Figure", source.figure],
          ["Supplement", source.supplement],
          ["Verbatim excerpt", source.verbatim_excerpt]
        ])}
      </section>

      <section class="detail-section">
        <h3>Tags</h3>
        <div class="tags">${(atom.tags || []).length ? atom.tags.map(t =>
          `<button type="button" class="tag" data-tag="${escapeHTML(t)}">${escapeHTML(t)}</button>`
        ).join("") : "—"}</div>
      </section>

      <details>
        <summary>Provenance</summary>
        <div class="details-body">
          ${kvGrid([
            ["Extraction run", prov.extraction_run_id],
            ["Extractor type", prov.extractor_type],
            ["Extractor", prov.extractor_identifier],
            ["Model", prov.model_name],
            ["Model version", prov.model_version],
            ["Prompt version", prov.prompt_version],
            ["Extracted at", prov.extracted_at],
            ["Reviewer", prov.reviewer_identifier],
            ["Reviewed at", prov.reviewed_at],
            ["Input hash", prov.input_document_hash]
          ])}
        </div>
      </details>

      <details>
        <summary>Raw atom JSON</summary>
        <div class="details-body">
          <div style="margin-bottom:8px"><button class="button compact" data-copy="json" type="button">Copy JSON</button></div>
          <pre>${escapeHTML(JSON.stringify(stripViewer(atom), null, 2))}</pre>
        </div>
      </details>
    `;
  }

  function exposureCard(exposure) {
    return `
      <div class="concept-card">
        <strong>${escapeHTML(exposure?.concept?.text || "Exposure")}</strong>
        <span>${escapeHTML([
          exposure?.role,
          [exposure?.dose_value, exposure?.dose_unit].filter(valuePresent).join(" "),
          exposure?.route,
          exposure?.frequency,
          exposure?.duration,
          exposure?.details
        ].filter(valuePresent).join(" · ") || "No additional structured details")}</span>
      </div>`;
  }

  function kvGrid(rows) {
    const meaningful = rows.filter(([,v]) => valuePresent(v));
    if (!meaningful.length) return `<span class="muted">No structured data.</span>`;
    return `<div class="kv-grid">${meaningful.map(([k,v]) =>
      `<div class="key">${escapeHTML(k)}</div><div class="value">${escapeHTML(formatPlain(v))}</div>`
    ).join("")}</div>`;
  }

  function stripViewer(atom) {
    const copy = { ...atom };
    delete copy.__viewer;
    return copy;
  }

  function closeDrawer() {
    els.detailDrawer.classList.remove("open");
    els.detailDrawer.setAttribute("aria-hidden", "true");
    els.drawerBackdrop.classList.add("hidden");
  }

  function countBy(items, fn) {
    return items.reduce((acc,item) => {
      const key = fn(item);
      acc[key] = (acc[key] || 0) + 1;
      return acc;
    }, {});
  }

  function groupBy(items, fn) {
    return items.reduce((acc,item) => {
      const key = fn(item);
      (acc[key] ||= []).push(item);
      return acc;
    }, {});
  }

  function activateTab(name) {
    document.querySelectorAll(".tab").forEach(tab => tab.classList.toggle("active", tab.dataset.tab === name));
    document.querySelectorAll(".tab-panel").forEach(panel => panel.classList.toggle("active", panel.id === `tab-${name}`));
  }

  function resetFilters() {
    state.filters = {
      search: "", run: "", kind: "", page: "", tag: "", review: "",
      quantOnly: false, populationOnly: false
    };
    els.searchInput.value = "";
    els.runFilter.value = "";
    els.kindFilter.value = "";
    els.pageFilter.value = "";
    els.tagFilter.value = "";
    els.reviewFilter.value = "";
    els.quantOnly.checked = false;
    els.populationOnly.checked = false;
    state.page = 1;
    renderAtomTable();
  }

  function clearWorkspace() {
    state.files = [];
    state.atoms = [];
    state.batches = new Map();
    state.validations = new Map();
    state.unpairedValidations = [];
    state.page = 1;
    resetFilters();
    els.fileInput.value = "";
    renderAll();
    els.workspace.classList.add("hidden");
    els.clearBtn.disabled = true;
    showToast("Workspace cleared.");
  }

  function exportData(mode) {
    const atoms = getFilteredAtoms();
    let content, fileName, mime;

    if (mode === "json") {
      content = JSON.stringify(atoms.map(stripViewer), null, 2);
      fileName = "literatureatom-filtered.json";
      mime = "application/json";
    } else {
      const columns = state.visibleColumns
        .map(path => COLUMN_DEFS.find(c => c.path === path))
        .filter(Boolean);
      const rows = atoms.map(atom => Object.fromEntries(columns.map(c => [c.label, exportValue(getPath(atom, c.path))])));

      if (mode === "visible-json") {
        content = JSON.stringify(rows, null, 2);
        fileName = "literatureatom-visible-columns.json";
        mime = "application/json";
      } else {
        const headers = columns.map(c => c.label);
        const csvRows = [
          headers.map(csvEscape).join(","),
          ...rows.map(row => headers.map(h => csvEscape(row[h])).join(","))
        ];
        content = csvRows.join("\r\n");
        fileName = "literatureatom-visible-columns.csv";
        mime = "text/csv;charset=utf-8";
      }
    }

    downloadBlob(content, fileName, mime);
    els.exportMenu.classList.add("hidden");
    els.exportBtn.setAttribute("aria-expanded", "false");
  }

  function exportValue(v) {
    if (!valuePresent(v)) return "";
    if (Array.isArray(v) || typeof v === "object") return JSON.stringify(v);
    return v;
  }

  function csvEscape(value) {
    const s = String(value ?? "");
    return /[",\r\n]/.test(s) ? `"${s.replaceAll('"','""')}"` : s;
  }

  function downloadBlob(content, fileName, mime) {
    const blob = new Blob([content], { type: mime });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = fileName;
    document.body.append(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }

  let toastTimer;
  function showToast(message) {
    clearTimeout(toastTimer);
    els.toast.textContent = message;
    els.toast.classList.remove("hidden");
    toastTimer = setTimeout(() => els.toast.classList.add("hidden"), 3200);
  }

  function bindEvents() {
    els.loadBtn.addEventListener("click", () => els.fileInput.click());
    els.dropZone.addEventListener("click", () => els.fileInput.click());
    els.dropZone.addEventListener("keydown", e => {
      if (e.key === "Enter" || e.key === " ") els.fileInput.click();
    });
    els.fileInput.addEventListener("change", () => handleFiles(els.fileInput.files));

    ["dragenter", "dragover"].forEach(type => els.dropZone.addEventListener(type, e => {
      e.preventDefault();
      els.dropZone.classList.add("dragging");
    }));
    ["dragleave", "drop"].forEach(type => els.dropZone.addEventListener(type, e => {
      e.preventDefault();
      els.dropZone.classList.remove("dragging");
    }));
    els.dropZone.addEventListener("drop", e => handleFiles(e.dataTransfer.files));

    els.clearBtn.addEventListener("click", clearWorkspace);

    document.querySelectorAll(".tab").forEach(tab => tab.addEventListener("click", () => {
      activateTab(tab.dataset.tab);
      if (tab.dataset.tab === "validation") renderValidationView();
    }));

    const filterBindings = [
      [els.searchInput, "search", "input"],
      [els.runFilter, "run", "change"],
      [els.kindFilter, "kind", "change"],
      [els.pageFilter, "page", "input"],
      [els.tagFilter, "tag", "input"],
      [els.reviewFilter, "review", "change"]
    ];
    filterBindings.forEach(([el,key,event]) => el.addEventListener(event, () => {
      state.filters[key] = el.value;
      state.page = 1;
      renderAtomTable();
    }));
    els.quantOnly.addEventListener("change", () => {
      state.filters.quantOnly = els.quantOnly.checked;
      state.page = 1;
      renderAtomTable();
    });
    els.populationOnly.addEventListener("change", () => {
      state.filters.populationOnly = els.populationOnly.checked;
      state.page = 1;
      renderAtomTable();
    });

    els.resetFiltersBtn.addEventListener("click", resetFilters);
    els.pageSize.addEventListener("change", () => { state.page = 1; renderAtomTable(); });
    els.prevPage.addEventListener("click", () => { state.page = Math.max(1, state.page - 1); renderAtomTable(); });
    els.nextPage.addEventListener("click", () => { state.page += 1; renderAtomTable(); });

    els.columnsBtn.addEventListener("click", () => els.columnsModal.classList.remove("hidden"));
    document.querySelectorAll("[data-close]").forEach(btn => btn.addEventListener("click", () => $(btn.dataset.close).classList.add("hidden")));
    els.columnsModal.addEventListener("click", e => { if (e.target === els.columnsModal) els.columnsModal.classList.add("hidden"); });
    els.defaultColumnsBtn.addEventListener("click", () => {
      state.visibleColumns = [...DEFAULT_COLUMNS];
      saveColumns(); renderColumns(); renderAtomTable();
    });
    els.selectAllColumnsBtn.addEventListener("click", () => {
      state.visibleColumns = COLUMN_DEFS.map(c => c.path);
      saveColumns(); renderColumns(); renderAtomTable();
    });
    els.clearColumnsBtn.addEventListener("click", () => {
      state.visibleColumns = ["canonical_statement"];
      saveColumns(); renderColumns(); renderAtomTable();
    });

    els.exportBtn.addEventListener("click", () => {
      const hidden = els.exportMenu.classList.toggle("hidden");
      els.exportBtn.setAttribute("aria-expanded", String(!hidden));
    });
    els.exportMenu.querySelectorAll("[data-export]").forEach(btn => btn.addEventListener("click", () => exportData(btn.dataset.export)));
    document.addEventListener("click", e => {
      if (!e.target.closest(".export-menu")) {
        els.exportMenu.classList.add("hidden");
        els.exportBtn.setAttribute("aria-expanded", "false");
      }
    });

    els.validationRun.addEventListener("change", renderValidationView);
    els.closeDrawer.addEventListener("click", closeDrawer);
    els.drawerBackdrop.addEventListener("click", closeDrawer);

    document.addEventListener("keydown", e => {
      if (e.key === "Escape") {
        closeDrawer();
        els.columnsModal.classList.add("hidden");
        els.exportMenu.classList.add("hidden");
      }
    });
  }

  bindEvents();
  renderColumns();
})();
