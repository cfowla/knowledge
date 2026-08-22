"""Typed domain models for primary-literature atoms.

This module contains stable data objects and structural validation only.
Task-specific sufficiency rules live in ``cds.validation.literature_atoms``.
"""

from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
from typing import Annotated
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, field_validator, model_validator


NonEmptyStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
SchemaVersion = Annotated[
    str,
    StringConstraints(strip_whitespace=True, pattern=r"^\d+\.\d+(?:\.\d+)?$"),
]


def utc_now() -> datetime:
    """Return an aware UTC timestamp."""
    return datetime.now(timezone.utc)


class DomainModel(BaseModel):
    """Shared configuration for serializable, strict domain models."""

    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=False,
    )


class AtomKind(str, Enum):
    STUDY_OBJECTIVE = "study_objective"
    ELIGIBILITY_CRITERION = "eligibility_criterion"
    POPULATION_DESCRIPTION = "population_description"
    INTERVENTION_DESCRIPTION = "intervention_description"
    EXPOSURE_DESCRIPTION = "exposure_description"
    COMPARATOR_DESCRIPTION = "comparator_description"
    OUTCOME_DEFINITION = "outcome_definition"
    METHOD = "method"
    QUANTITATIVE_RESULT = "quantitative_result"
    QUALITATIVE_RESULT = "qualitative_result"
    ADVERSE_EVENT = "adverse_event"
    SUBGROUP_RESULT = "subgroup_result"
    AUTHOR_CONCLUSION = "author_conclusion"
    LIMITATION = "limitation"
    FUNDING_DISCLOSURE = "funding_disclosure"
    CONFLICT_OF_INTEREST = "conflict_of_interest"
    DATA_AVAILABILITY = "data_availability"
    OTHER = "other"


class AssertionOrigin(str, Enum):
    DIRECTLY_REPORTED = "directly_reported"
    NORMALIZED_FROM_SOURCE = "normalized_from_source"
    CALCULATED_FROM_REPORTED_DATA = "calculated_from_reported_data"
    EXTRACTOR_INFERENCE = "extractor_inference"


class SourceSection(str, Enum):
    ABSTRACT = "abstract"
    INTRODUCTION = "introduction"
    METHODS = "methods"
    RESULTS = "results"
    DISCUSSION = "discussion"
    CONCLUSION = "conclusion"
    TABLE = "table"
    FIGURE = "figure"
    SUPPLEMENT = "supplement"
    OTHER = "other"


class ExtractorType(str, Enum):
    HUMAN = "human"
    LANGUAGE_MODEL = "language_model"
    RULE_BASED = "rule_based"
    IMPORT = "import"
    HYBRID = "hybrid"


class ReviewStatus(str, Enum):
    DRAFT = "draft"
    EXTRACTED = "extracted"
    NEEDS_REVIEW = "needs_review"
    VERIFIED = "verified"
    REJECTED = "rejected"
    SUPERSEDED = "superseded"


class ExposureRole(str, Enum):
    INTERVENTION = "intervention"
    EXPOSURE = "exposure"
    COMPARATOR = "comparator"
    CONTROL = "control"
    DIAGNOSTIC_TEST = "diagnostic_test"
    REFERENCE_STANDARD = "reference_standard"


class OutcomeType(str, Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    EXPLORATORY = "exploratory"
    SAFETY = "safety"
    SURROGATE = "surrogate"
    COMPOSITE = "composite"
    NOT_SPECIFIED = "not_specified"


class IntervalType(str, Enum):
    CONFIDENCE_INTERVAL = "confidence_interval"
    CREDIBLE_INTERVAL = "credible_interval"
    PREDICTION_INTERVAL = "prediction_interval"
    RANGE = "range"
    INTERQUARTILE_RANGE = "interquartile_range"
    OTHER = "other"


class ConceptRef(DomainModel):
    text: NonEmptyStr
    code: NonEmptyStr | None = None
    system: NonEmptyStr | None = None
    version: NonEmptyStr | None = None

    @model_validator(mode="after")
    def require_code_system_pair(self) -> ConceptRef:
        if (self.code is None) != (self.system is None):
            raise ValueError("code and system must be provided together")
        return self


class PopulationDescriptor(DomainModel):
    label: NonEmptyStr | None = None
    sample_size: Annotated[int, Field(gt=0)] | None = None
    subgroup: bool = False
    inclusion_criteria: tuple[NonEmptyStr, ...] = ()
    exclusion_criteria: tuple[NonEmptyStr, ...] = ()

    @model_validator(mode="after")
    def require_some_population_detail(self) -> PopulationDescriptor:
        if not any(
            (
                self.label,
                self.sample_size,
                self.inclusion_criteria,
                self.exclusion_criteria,
            )
        ):
            raise ValueError("population must contain at least one descriptive field")
        return self


class ExposureDescriptor(DomainModel):
    concept: ConceptRef
    role: ExposureRole
    dose_value: Decimal | None = None
    dose_unit: NonEmptyStr | None = None
    route: NonEmptyStr | None = None
    frequency: NonEmptyStr | None = None
    duration: NonEmptyStr | None = None
    details: NonEmptyStr | None = None

    @model_validator(mode="after")
    def validate_dose_pair(self) -> ExposureDescriptor:
        if (self.dose_value is None) != (self.dose_unit is None):
            raise ValueError("dose_value and dose_unit must be provided together")
        if self.dose_value is not None and self.dose_value < 0:
            raise ValueError("dose_value cannot be negative")
        return self


class OutcomeDescriptor(DomainModel):
    concept: ConceptRef
    definition: NonEmptyStr | None = None
    outcome_type: OutcomeType = OutcomeType.NOT_SPECIFIED
    measurement_method: NonEmptyStr | None = None
    time_horizon_value: Decimal | None = None
    time_horizon_unit: NonEmptyStr | None = None

    @model_validator(mode="after")
    def validate_time_horizon_pair(self) -> OutcomeDescriptor:
        if (self.time_horizon_value is None) != (self.time_horizon_unit is None):
            raise ValueError(
                "time_horizon_value and time_horizon_unit must be provided together"
            )
        if self.time_horizon_value is not None and self.time_horizon_value < 0:
            raise ValueError("time_horizon_value cannot be negative")
        return self


class IntervalEstimate(DomainModel):
    lower: Decimal
    upper: Decimal
    confidence_level_percent: Annotated[Decimal, Field(gt=0, le=100)] | None = Decimal("95")
    interval_type: IntervalType = IntervalType.CONFIDENCE_INTERVAL

    @model_validator(mode="after")
    def validate_bounds(self) -> IntervalEstimate:
        if self.lower > self.upper:
            raise ValueError("interval lower bound cannot exceed upper bound")
        return self


class ArmObservation(DomainModel):
    arm_label: NonEmptyStr
    event_count: Annotated[int, Field(ge=0)] | None = None
    sample_size: Annotated[int, Field(gt=0)] | None = None
    value: Decimal | None = None
    unit: NonEmptyStr | None = None

    @model_validator(mode="after")
    def validate_observation(self) -> ArmObservation:
        if self.event_count is not None and self.sample_size is None:
            raise ValueError("sample_size is required when event_count is present")
        if (
            self.event_count is not None
            and self.sample_size is not None
            and self.event_count > self.sample_size
        ):
            raise ValueError("event_count cannot exceed sample_size")
        if (self.value is None) != (self.unit is None):
            raise ValueError("value and unit must be provided together")
        return self


class QuantitativeResult(DomainModel):
    effect_measure: NonEmptyStr
    estimate: Decimal
    interval: IntervalEstimate | None = None
    p_value: Annotated[Decimal, Field(ge=0, le=1)] | None = None
    p_value_text: NonEmptyStr | None = None
    adjusted: bool | None = None
    adjustment_variables: tuple[NonEmptyStr, ...] = ()
    arms: tuple[ArmObservation, ...] = ()
    original_result_text: NonEmptyStr | None = None

    @model_validator(mode="after")
    def validate_adjustment_and_p_value(self) -> QuantitativeResult:
        if self.adjustment_variables and self.adjusted is not True:
            raise ValueError(
                "adjusted must be true when adjustment_variables are present"
            )
        if self.p_value is not None and self.p_value_text is not None:
            raise ValueError("provide either p_value or p_value_text, not both")
        return self


class SourceAnchor(DomainModel):
    section: SourceSection
    page: NonEmptyStr | None = None
    paragraph: NonEmptyStr | None = None
    sentence: NonEmptyStr | None = None
    table: NonEmptyStr | None = None
    table_row: NonEmptyStr | None = None
    table_column: NonEmptyStr | None = None
    figure: NonEmptyStr | None = None
    supplement: NonEmptyStr | None = None
    character_start: Annotated[int, Field(ge=0)] | None = None
    character_end: Annotated[int, Field(gt=0)] | None = None
    verbatim_excerpt: NonEmptyStr | None = None
    excerpt_hash: NonEmptyStr | None = None

    @model_validator(mode="after")
    def validate_locator(self) -> SourceAnchor:
        reliable_locator_present = any(
            (
                self.page,
                self.paragraph,
                self.sentence,
                self.table,
                self.figure,
                self.supplement,
                self.character_start is not None,
                self.verbatim_excerpt,
                self.excerpt_hash,
            )
        )
        if not reliable_locator_present:
            raise ValueError(
                "source_anchor requires section plus at least one reliable locator"
            )

        if (self.character_start is None) != (self.character_end is None):
            raise ValueError(
                "character_start and character_end must be provided together"
            )
        if (
            self.character_start is not None
            and self.character_end is not None
            and self.character_start >= self.character_end
        ):
            raise ValueError("character_start must be less than character_end")

        if self.table_row is not None and self.table is None:
            raise ValueError("table is required when table_row is provided")
        if self.table_column is not None and self.table is None:
            raise ValueError("table is required when table_column is provided")
        return self


class ExtractionProvenance(DomainModel):
    extractor_type: ExtractorType
    extractor_identifier: NonEmptyStr
    extracted_at: datetime
    software_name: NonEmptyStr | None = None
    software_version: NonEmptyStr | None = None
    model_name: NonEmptyStr | None = None
    model_version: NonEmptyStr | None = None
    prompt_version: NonEmptyStr | None = None
    input_document_hash: NonEmptyStr | None = None
    extraction_run_id: NonEmptyStr | None = None
    reviewer_identifier: NonEmptyStr | None = None
    reviewed_at: datetime | None = None

    @field_validator("extracted_at", "reviewed_at")
    @classmethod
    def require_timezone_aware_timestamp(cls, value: datetime | None) -> datetime | None:
        if value is not None and (value.tzinfo is None or value.utcoffset() is None):
            raise ValueError("timestamps must be timezone-aware")
        return value

    @model_validator(mode="after")
    def validate_review_pair(self) -> ExtractionProvenance:
        if (self.reviewer_identifier is None) != (self.reviewed_at is None):
            raise ValueError(
                "reviewer_identifier and reviewed_at must be provided together"
            )
        return self


class LiteratureAtom(DomainModel):
    """Minimum viable atom with optional normalized result context.

    System-owned identifiers and timestamps are generated when omitted but are
    always present on a validated instance and in serialized output.
    """

    atom_id: UUID = Field(default_factory=uuid4)
    publication_id: UUID
    atom_kind: AtomKind
    canonical_statement: NonEmptyStr
    assertion_origin: AssertionOrigin
    source_anchor: SourceAnchor
    provenance: ExtractionProvenance
    review_status: ReviewStatus = ReviewStatus.DRAFT
    schema_version: SchemaVersion = "1.0"
    atom_version: Annotated[int, Field(ge=1)] = 1
    created_at: datetime = Field(default_factory=utc_now)

    population: PopulationDescriptor | None = None
    exposures: tuple[ExposureDescriptor, ...] = ()
    outcome: OutcomeDescriptor | None = None
    quantitative_result: QuantitativeResult | None = None

    supersedes_atom_id: UUID | None = None
    tags: tuple[NonEmptyStr, ...] = ()

    @field_validator("created_at")
    @classmethod
    def require_aware_created_at(cls, value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("created_at must be timezone-aware")
        return value

    @model_validator(mode="after")
    def validate_versioning(self) -> LiteratureAtom:
        if self.supersedes_atom_id == self.atom_id:
            raise ValueError("an atom cannot supersede itself")
        if self.review_status is ReviewStatus.SUPERSEDED and self.supersedes_atom_id is None:
            raise ValueError(
                "supersedes_atom_id is required when review_status is superseded"
            )
        if self.created_at < self.provenance.extracted_at:
            raise ValueError("created_at cannot precede provenance.extracted_at")
        return self
