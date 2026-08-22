"""Sufficiency validation for literature atoms.

The domain model answers: "Is this structurally valid?"
This module answers: "Does this atom contain enough information for its kind?"
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from cds.domain.literature import AtomKind, ExposureRole, LiteratureAtom


class IssueSeverity(str, Enum):
    ERROR = "error"
    WARNING = "warning"


@dataclass(frozen=True, slots=True)
class ValidationIssue:
    code: str
    field: str
    message: str
    severity: IssueSeverity = IssueSeverity.ERROR


@dataclass(frozen=True, slots=True)
class ValidationResult:
    issues: tuple[ValidationIssue, ...] = ()

    @property
    def is_valid(self) -> bool:
        return not any(issue.severity is IssueSeverity.ERROR for issue in self.issues)

    @property
    def errors(self) -> tuple[ValidationIssue, ...]:
        return tuple(
            issue for issue in self.issues if issue.severity is IssueSeverity.ERROR
        )

    @property
    def warnings(self) -> tuple[ValidationIssue, ...]:
        return tuple(
            issue for issue in self.issues if issue.severity is IssueSeverity.WARNING
        )


_REQUIRED_FIELDS_BY_KIND: dict[AtomKind, tuple[str, ...]] = {
    AtomKind.ELIGIBILITY_CRITERION: ("population",),
    AtomKind.POPULATION_DESCRIPTION: ("population",),
    AtomKind.INTERVENTION_DESCRIPTION: ("exposures",),
    AtomKind.EXPOSURE_DESCRIPTION: ("exposures",),
    AtomKind.COMPARATOR_DESCRIPTION: ("exposures",),
    AtomKind.OUTCOME_DEFINITION: ("outcome",),
    AtomKind.QUANTITATIVE_RESULT: (
        "population",
        "exposures",
        "outcome",
        "quantitative_result",
    ),
    AtomKind.ADVERSE_EVENT: (
        "exposures",
        "outcome",
        "quantitative_result",
    ),
    AtomKind.SUBGROUP_RESULT: (
        "population",
        "exposures",
        "outcome",
        "quantitative_result",
    ),
}


def validate_literature_atom_sufficiency(atom: LiteratureAtom) -> ValidationResult:
    """Return structured sufficiency issues without mutating the atom."""
    issues: list[ValidationIssue] = []

    for field_name in _REQUIRED_FIELDS_BY_KIND.get(atom.atom_kind, ()):
        value = getattr(atom, field_name)
        missing = value is None or value == ()
        if missing:
            issues.append(
                ValidationIssue(
                    code="required_for_atom_kind",
                    field=field_name,
                    message=(
                        f"{field_name} is required for atom kind "
                        f"{atom.atom_kind.value}"
                    ),
                )
            )

    if atom.atom_kind is AtomKind.INTERVENTION_DESCRIPTION and atom.exposures:
        if not any(
            exposure.role is ExposureRole.INTERVENTION
            for exposure in atom.exposures
        ):
            issues.append(
                ValidationIssue(
                    code="missing_intervention_role",
                    field="exposures",
                    message=(
                        "intervention_description requires at least one exposure "
                        "with role=intervention"
                    ),
                )
            )

    if atom.atom_kind is AtomKind.EXPOSURE_DESCRIPTION and atom.exposures:
        if not any(
            exposure.role is ExposureRole.EXPOSURE for exposure in atom.exposures
        ):
            issues.append(
                ValidationIssue(
                    code="missing_exposure_role",
                    field="exposures",
                    message=(
                        "exposure_description requires at least one exposure "
                        "with role=exposure"
                    ),
                )
            )

    if atom.atom_kind is AtomKind.COMPARATOR_DESCRIPTION and atom.exposures:
        comparator_roles = {ExposureRole.COMPARATOR, ExposureRole.CONTROL}
        if not any(exposure.role in comparator_roles for exposure in atom.exposures):
            issues.append(
                ValidationIssue(
                    code="missing_comparator_role",
                    field="exposures",
                    message=(
                        "comparator_description requires at least one exposure "
                        "with role=comparator or control"
                    ),
                )
            )

    if atom.atom_kind is AtomKind.SUBGROUP_RESULT and atom.population is not None:
        if atom.population.subgroup is not True:
            issues.append(
                ValidationIssue(
                    code="subgroup_not_marked",
                    field="population.subgroup",
                    message="subgroup_result requires population.subgroup=true",
                )
            )

    if atom.quantitative_result is not None and atom.outcome is None:
        issues.append(
            ValidationIssue(
                code="quantitative_result_without_outcome",
                field="outcome",
                message="an outcome is required when quantitative_result is present",
            )
        )

    if atom.atom_kind is AtomKind.QUALITATIVE_RESULT and atom.quantitative_result is not None:
        issues.append(
            ValidationIssue(
                code="unexpected_quantitative_result",
                field="quantitative_result",
                message=(
                    "qualitative_result contains quantitative_result; consider "
                    "splitting this into a separate quantitative_result atom"
                ),
                severity=IssueSeverity.WARNING,
            )
        )

    return ValidationResult(issues=tuple(issues))
