#!/usr/bin/env bash
set -euo pipefail

ensure_label() {
  local name="$1"
  local color="$2"
  local description="$3"

  gh label create "$name" \
    --repo "$GH_REPO" \
    --color "$color" \
    --description "$description" \
    --force
}

ensure_label "type: bug"          "D73A4A" "Incorrect or broken behavior"
ensure_label "type: enhancement"  "A2EEEF" "Incremental capability or quality improvement"
ensure_label "type: architecture" "7057FF" "Schema, system design, or structural change"
ensure_label "type: automation"   "1D76DB" "Automation or workflow improvement"

ensure_label "area: atom"         "0E8A16" "LiteratureAtom extraction or atom model"
ensure_label "area: sea"          "5319E7" "SEA synthesis, evaluation, or appraisal"
ensure_label "area: validation"   "FBCA04" "Validation, QA, or testing"
ensure_label "area: provenance"   "BFDADC" "Evidence traceability and provenance"

ensure_label "priority: high"     "B60205" "High-priority actionable work"
ensure_label "priority: normal"   "D4C5F9" "Normal-priority actionable work"

ensure_label "health-check"       "006B75" "Finding or task produced by repository health assessment"
