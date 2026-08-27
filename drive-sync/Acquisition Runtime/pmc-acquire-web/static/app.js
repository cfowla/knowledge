const form = document.querySelector('#acquire-form');
const pmidInput = document.querySelector('#pmid');
const emailInput = document.querySelector('#email');
const button = document.querySelector('#acquire-button');
const progress = document.querySelector('#progress');
const result = document.querySelector('#result');
const errorBox = document.querySelector('#error');

emailInput.value = localStorage.getItem('pmcAcquireEmail') || '';

function text(value, fallback = '—') {
  return value === null || value === undefined || value === '' ? fallback : String(value);
}

function bytes(value) {
  if (!Number.isFinite(Number(value))) return '—';
  const n = Number(value);
  if (n < 1024) return `${n} B`;
  if (n < 1024 ** 2) return `${(n / 1024).toFixed(1)} KB`;
  return `${(n / 1024 ** 2).toFixed(2)} MB`;
}

function shortHash(value) {
  if (!value) return '—';
  return `${value.slice(0, 12)}…${value.slice(-8)}`;
}

function fillDl(selector, entries) {
  const dl = document.querySelector(selector);
  dl.replaceChildren();
  for (const [label, value] of entries) {
    const dt = document.createElement('dt');
    dt.textContent = label;
    const dd = document.createElement('dd');
    dd.textContent = text(value);
    dl.append(dt, dd);
  }
}

function renderManifest(manifest) {
  result.classList.remove('hidden');
  document.querySelector('#state').textContent = text(manifest.terminal_state);
  document.querySelector('#state').dataset.state = text(manifest.terminal_state);
  document.querySelector('#reason').textContent = text(manifest.terminal_reason, '');

  const id = manifest.resolved_identity || {};
  fillDl('#identity', [
    ['Requested PMID', manifest.requested?.pmid],
    ['Resolved PMID', id.pmid],
    ['PMCID', id.pmcid],
    ['PMC version', id.versioned_pmcid],
    ['DOI', id.doi],
  ]);

  const meta = manifest.dataset_metadata || {};
  fillDl('#provenance', [
    ['Provider', manifest.provider],
    ['Title', meta.title],
    ['License', meta.license_code],
    ['PMC open access', meta.is_pmc_openaccess],
    ['Manuscript', meta.is_manuscript],
  ]);

  const tbody = document.querySelector('#artifacts');
  tbody.replaceChildren();
  for (const artifact of manifest.artifacts || []) {
    const tr = document.createElement('tr');
    const kind = artifact.kind === 'xml' ? 'JATS XML' : artifact.kind?.toUpperCase();
    const cells = [kind, artifact.valid ? 'PASS' : 'FAIL', bytes(artifact.byte_size), shortHash(artifact.sha256)];
    for (const value of cells) {
      const td = document.createElement('td');
      td.textContent = text(value);
      if (value === 'PASS') td.className = 'pass';
      tr.append(td);
    }
    const action = document.createElement('td');
    if (artifact.download_url) {
      const link = document.createElement('a');
      link.href = artifact.download_url;
      link.className = 'secondary-button';
      link.textContent = 'Download';
      action.append(link);
    }
    tr.append(action);
    tbody.append(tr);
  }
  if (!tbody.children.length) {
    const tr = document.createElement('tr');
    const td = document.createElement('td');
    td.colSpan = 5;
    td.textContent = 'No validated artifact was materialized.';
    td.className = 'muted';
    tr.append(td);
    tbody.append(tr);
  }

  const handoff = manifest.atom_sea_handoff || {};
  fillDl('#handoff', [
    ['Preferred input', handoff.preferred_input ? handoff.preferred_input.split('/').pop() : null],
    ['Secondary input', handoff.secondary_input ? handoff.secondary_input.split('/').pop() : null],
  ]);

  const manifestLink = document.querySelector('#manifest-link');
  manifestLink.href = manifest.manifest_url || '#';
  document.querySelector('#raw-manifest').textContent = JSON.stringify(manifest, null, 2);
}

async function checkHealth() {
  const health = document.querySelector('#health');
  try {
    const response = await fetch('/api/health', {cache: 'no-store'});
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    health.textContent = 'Server ready';
    health.classList.add('ready');
  } catch {
    health.textContent = 'Server unavailable';
    health.classList.add('down');
  }
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  errorBox.classList.add('hidden');
  result.classList.add('hidden');
  progress.classList.remove('hidden');
  button.disabled = true;
  button.textContent = 'Acquiring…';

  const email = emailInput.value.trim();
  localStorage.setItem('pmcAcquireEmail', email);

  try {
    const response = await fetch('/api/acquire', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({pmid: pmidInput.value.trim(), email}),
    });
    const payload = await response.json();
    if (!response.ok) throw new Error(payload.error || `HTTP ${response.status}`);
    renderManifest(payload.manifest);
  } catch (error) {
    errorBox.textContent = error.message || String(error);
    errorBox.classList.remove('hidden');
  } finally {
    progress.classList.add('hidden');
    button.disabled = false;
    button.textContent = 'Acquire';
  }
});

checkHealth();
