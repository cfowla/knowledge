# v0.4.3 Prompt 1 API migration

## Production acquisition

v0.4.2 exposed a prepared evidence object as the production entry point.

```python
execution = acquire_one(spec, root)
```

That call could receive resolved identity, route attempts, materialized artifact paths, metrics, and a requested terminal state through `AcquisitionSpec`.

v0.4.3 production acquisition starts with a PMID and configuration. The host only answers requests emitted by Python.

```python
execution = acquire_one(
    identifier="24782981",
    config=AcquisitionConfig(...),
    root=Path("runs"),
    host=host_adapter,
    transports=TransportRegistry(),
)
```

`AcquisitionConfig` has no fields for terminal state, resolved identity, route outcome, attempts, or artifact paths.

## Replay

Prepared evidence remains available under explicit replay names.

```python
spec = AcquisitionReplaySpec(...)
execution = replay_acquisition(spec, root)
```

Replay may contain prepared identity, attempts, artifacts, metrics, and terminal-state requests. It cannot be used as the public `acquire_one()` contract.

## Host observation contract

Python emits `HostRequest` objects for two operations in Prompt 1.

1. `resolve_identity` requests metadata evidence for the requested PMID.
2. `observe_route` requests facts for one Python-selected route.

The host can return `IdentityObservation` or `RouteObservation`. A materialized artifact observation includes bytes by file reference plus source, access basis, and discovery provenance. Python performs identity verification, format validation, hashing, route accounting, and terminal-state assignment.

## Route capability state

`RouteCapabilityRegistry` replaces production boolean route flags. Each route is `supported`, `experimental`, or `disabled`. Prompt 1 initializes PMC, publisher OA, Unpaywall, and repository routes as `experimental`. The real check uses publisher OA while it remains experimental, so the check does not promote route support before Prompt 3.

`RouteFlags` remains only as a compatibility input for historical replay data. The runtime converts it to capability states before route decisions.

## Exhaustion

`EXHAUSTED` now requires definitive negative evidence for every enabled route. Error, timeout, CAPTCHA, non-materializable response, unknown result, search absence, skipped route, and unexecuted route do not satisfy that requirement.

## Prompt 1 boundaries

The production controller accepts PMID input in this repair step. DOI and PMCID production entry points remain for later work. `TransportRegistry` is only a placeholder in Prompt 1. Prompt 2 defines and proves the shared native and remote transport contract.
