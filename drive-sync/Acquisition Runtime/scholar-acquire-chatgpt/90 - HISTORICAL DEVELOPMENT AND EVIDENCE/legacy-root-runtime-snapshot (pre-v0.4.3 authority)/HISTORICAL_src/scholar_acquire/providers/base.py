from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol

from ..cache import DiskCache
from ..config import Settings
from ..http import HttpClient
from ..models import AcquisitionPolicy, Attempt, LocationCandidate, ProviderOutcome, ResolvedIds


@dataclass
class AcquisitionContext:
    ids: ResolvedIds
    policy: AcquisitionPolicy
    http: HttpClient
    cache: DiskCache
    settings: Settings
    attempts: list[Attempt]
    publisher_locations: list[LocationCandidate] = field(default_factory=list)
    repository_locations: list[LocationCandidate] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

    def add_attempt(self, attempt: Attempt) -> None:
        self.attempts.append(attempt)


class Provider(Protocol):
    name: str

    def run(self, ctx: AcquisitionContext) -> ProviderOutcome:
        ...
