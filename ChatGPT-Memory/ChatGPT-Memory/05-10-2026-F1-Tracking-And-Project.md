---
title: F1 Tracking and Project
source: share
saved_at: 2026-10-05T21:02:15.758348+00:00
stable_key: 1abfa952eea2d59f
tags: [chatgpt, memory]
url: "https://chatgpt.com/share/6ac3ea9e-e96c-83ed-a2c9-37fe67812635"
---

# F1 Tracking and Project

## User

Please read and find out the previous logs/chats @Live F1 Tracking Data and @RaceVision F1 Project.
Please learn and understand the logs and then I may ask you a question.

## Assistant

The output of this plugin was redacted.

## Assistant

Yes. I’ve retrieved and reviewed the available context from the previous **“Live F1 Tracking Data”** and **“RaceVision F1 Project”** work, and I have the project state in context.

### What I’ve carried forward

**RaceVision’s core objective**
- Live F1 telemetry → normalized backend → PostgreSQL → real-time event/streaming pipeline.
- 3D representation of the F1 cars and circuit in **Unity/Blender**.
- Live camera system, telemetry overlays, replay, audio and eventually AI commentary.
- Streaming integration for **OBS, Twitch, Kick and YouTube**.
- Future VR support.
- Persistent telemetry for replay, statistics and analytics.

**Architecture**
- Enterprise/layered architecture with clear separation between:
  - Configuration
  - Domain/models
  - Protocols
  - Providers
  - Normalization/validation
  - Ingestion
  - Persistence
  - Event bus
  - Live runtime
  - Replay
  - API/WebSocket
  - Rendering/Unity/Blender
  - Streaming/OBS
  - AI/analytics
- Shared protocol definitions exist for telemetry, commands, events, responses and errors.
- Streaming has dedicated areas for OBS/Twitch/Kick/YouTube/overlay.
- Simulation, rendering and monitoring are separate architectural layers.

**Telemetry/data-source direction**
- **OpenF1** was selected as the primary live telemetry source.
- **FastF1** is intended primarily for historical/analytical data.
- **Ergast** is useful for historical/metadata information.
- API-Sports and community APIs were considered optional/non-core.
- The architecture deliberately uses a **provider abstraction**, so RaceVision isn't hard-wired to one telemetry provider.

**Database/persistence**
The PostgreSQL foundation and persistence work is substantially complete:
- PostgreSQL 17
- SQLAlchemy 2.x
- Async + sync database engines
- Connection pooling
- Health checks
- Pydantic configuration/environment handling
- Alembic framework
- ORM models
- Generic repositories
- Repository interfaces/ports
- Unit of Work
- Query Objects
- Transaction management
- Soft deletion
- UUIDs
- Timestamp/versioning/audit/tenant fields
- Bulk/high-throughput persistence paths
- Telemetry-oriented indexes and future Timescale/partitioning considerations

Core models include:

`Team → Driver → Car → Track → RaceSession → SessionParticipant → TelemetrySample → Lap → Sector → WeatherSample → RaceEvent → ReplayRecording → ReplayBookmark → CameraEvent → StatisticsSnapshot → ConfigurationEntry`

The telemetry path intentionally avoids naïve ORM eager-loading and has been designed for streaming/bulk workloads.

**Implementation progress**

The previous work progressed substantially beyond the original repository skeleton.

Completed phases currently recorded:

> **00–08 COMPLETE**

including:

1. Repository/Foundation
2. Enterprise Architecture
3. PostgreSQL/SQLAlchemy/Alembic foundation
4. ORM + repositories + Unit of Work + Query Objects
5. Shared protocol layer
6. Provider framework
7. Normalization + validation
8. Ingestion + high-speed persistence + live event bus

The most recent recorded next step is:

> **Phase 09 — Live Runtime**

After that, the intended progression is approximately:

**Live Runtime → Replay Runtime → Unified Runtime → Prediction & Synchronization → Streaming/API/WebSocket → Unity/Blender/OBS → AI/analytics/simulation/rendering/dashboard/social/VR**

### Testing/status I have retained

The database/runtime work had already reached strong test coverage:

- PostgreSQL runtime: **84 tests passing**, approximately **96% coverage**
- Persistence/ORM/repositories/ports: **137 tests passing**, approximately **97% coverage**

Earlier agent work included **Agents 1–5**, followed by the PostgreSQL foundation work in **Agent 06** and its subsequent sub-phases.

There are still known architectural items such as:
- Full cursor pagination
- Async specialized bindings for every entity
- A complete Alembic metadata revision
- Future replica/read routing
- Some remaining domain-specific refinements

### Important original product requirements

I also have the earlier requirements around:

- All cars' live track positions
- Vehicle orientation
- Speed/telemetry
- Collision/damage visualization
- Multiple camera angles
- Chat-controlled cameras such as `/camera 1`
- Simulated engine/tyre/wind/crowd audio
- Replay and bookmarks
- PostgreSQL telemetry history
- Live streaming
- Future AI commentary
- Future VR
- Smoothing/imperfect racing-line reconstruction rather than pretending to have broadcast-grade exact data

And importantly, the system was designed around the reality that **official F1 telemetry access/licensing and exact broadcast-grade data are separate issues from the software architecture**.

So you **do not need to re-explain the RaceVision architecture or the previous implementation phases to me**. I can continue from the current Phase 09 / Live Runtime position and use the previous design decisions as the baseline. memcite

## User

Please check and tell me all the Phases

## Assistant

The output of this plugin was redacted.

## Assistant

{"uri":"skills://plugins/github/github/skill.md","start_line":1,"num_lines":120}

## Assistant

{"paths":["GitHub"],"query":"repository"}

## Assistant

The output of this plugin was redacted.

## Assistant

The output of this plugin was redacted.

## Assistant

The output of this plugin was redacted.

## Assistant

The output of this plugin was redacted.

## Assistant

The output of this plugin was redacted.

## Assistant

Yes. I checked the **current RaceVision repository**, not just the older chat history. There are actually **two different roadmap/phase systems** in the project, because the project evolved from the original product roadmap into the current enterprise implementation plan.

The **current implementation phases** are the ones we should use going forward.

## RaceVision — Current Master Implementation Phases

| Phase | Name | Status |
|---:|---|---|
| **00** | Repository & Foundations | ✅ Complete |
| **01** | Enterprise Architecture | ✅ Complete |
| **02** | PostgreSQL Enterprise Platform | ✅ Complete |
| **03** | Shared Protocol Platform | ✅ Complete |
| **04** | Live Telemetry Ingestion Platform | ✅ Complete |
| **05** | — | 🔄 Integrated into later architecture / numbering evolved |
| **06** | — | 🔄 Integrated into later architecture / numbering evolved |
| **07** | — | 🔄 Integrated into later architecture / numbering evolved |
| **08** | Live Telemetry Provider & Ingestion Pipeline | ✅ Complete |
| **09** | Live Runtime Platform | ✅ Complete |
| **10** | Race Session Domain Platform | 🔄 **In progress** |
| **11** | — | ⏳ Upcoming |
| **12** | — | ⏳ Upcoming |
| **13** | — | ⏳ Upcoming |
| **14** | — | ⏳ Upcoming |
| **15+** | — | ⏳ Future |

However, the repository gives us much more precise information about the **currently implemented phases**, especially Phases 08–10.

### Phase 08 — Live Telemetry/Ingestion

This phase was broken into:

- **08.1** Provider Adapter Framework
- **08.2** LiveF1 Adapter
- **08.3** OpenF1 Adapter
- **08.4** F1LivePulse Adapter
- **08.5** API-Sports Adapter
- **08.6** Replay File Provider
- **08.7** Provider Manager Integration
- **08.8** Telemetry Normalization & Validation
- **08.9** Live Event Bus

The repository confirms the provider framework, normalization, ingestion and Live Event Bus specifications. fileciteturn6file0

### Phase 09 — Live Runtime

This was substantially expanded into:

- **09.0** Live Runtime Core
- **09.1** — Runtime foundation/integration work
- **09.2** Live State Cache
- **09.3** Live Subscription Manager
- **09.4** Live Synchronization Engine
- **09.5** Runtime Health & Monitoring
- **09.6** Runtime Statistics & Diagnostics
- **09.7** Runtime Event Integration
- **09.8** Runtime Recovery & Failover
- **09.9** Phase Integration & Acceptance Testing

And GitHub confirms these commits are actually present, with **09.9 completing the runtime acceptance phase**. citeturn5file0

### Phase 10 — Race Session Domain

This is where the project currently is.

Implemented sequentially:

- **10.0** Race Session Domain
- **10.1** Session Manager Completion
- **10.2** Race Event & Weekend Manager
- **10.3** Track Session Manager
- **10.4** Driver & Car Runtime Registry
- **10.5** Race Timeline Engine

The latest repository commit is currently:

> **Agent 10.5 — Race Timeline Engine**

dated **7 August 2026 at 22:48 UTC**.

So **Phase 10 is currently the active development phase**, and 10.5 is the latest completed agent in that phase.

---

## The original product roadmap

There is also an older, much higher-level product roadmap still present in `docs/Roadmap.md`:

**Phase 0 — Repository & Foundations**

**Phase 1 — Telemetry Core**
- Canonical telemetry
- PostgreSQL
- Collector
- Live persistence
- WebSocket

**Phase 2 — Unity Digital Twin**
- Unity 6
- Telemetry client
- Cars/tracks
- Broadcast cameras

**Phase 3 — Streaming**
- OBS
- Twitch
- Kick
- YouTube
- Overlays

**Phase 4 — Replay**
- Recording
- Seek/speed
- Unity playback

**Phase 5 — Chat & Engagement**
- Twitch chat
- Kick chat
- YouTube chat
- Overlay events

**Phase 6 — AI Commentary**

**Phase 7 — VR**

That older roadmap is still in the repository. fileciteturn5file0

### The important distinction

The **0–7 roadmap is the original product roadmap**.

The **00–10.x structure is the newer engineering/architecture implementation programme** that we've been executing.

The specifications directory confirms that the newer architecture explicitly defines **Phase 09 Runtime** and **Phase 10 Race Session Domain**, including the Session Manager, Weekend Manager, Track Session Manager, Driver/Car Registry and Race Timeline Engine. fileciteturn6file0

So for our work from this point forward, I would treat:

> **Phase 10.5 — Race Timeline Engine**

as the **actual current project position**, rather than the old "Phase 1 Telemetry Core / Phase 2 Unity" numbering.

I also checked the actual GitHub repository, so this isn't based solely on the previous chat summaries. urlRaceVision repositoryhttps://github.com/kanedark316/RaceVision

## User

@GitHub RaceVision folder is there

## Assistant

Yes — the **RaceVision folder/repository is there on GitHub**.

urlRaceVision GitHub repositoryhttps://github.com/kanedark316/RaceVision

If you mean **“is the RaceVision project folder actually present in the repository, and can you inspect all its files/folders?”** — yes, I can inspect the repository structure and use the actual files as the source of truth.

If you want, I can next **audit the entire `RaceVision` repository and produce the definitive Phase 00 → current phase list directly from the files/commits**, including every sub-phase (`09.x`, `10.x`, etc.) and mark each one **Complete / In Progress / Not Started**.

## User

Please give commands for Agent 10.6	Historical Telemetry Provider	Read historical telemetry into Runtime ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. Since **Agent 10.5 — Race Timeline Engine** is the latest completed agent, Agent **10.6** should build on the existing Phase 10 architecture rather than bypassing it.

Below is a **single Cursor-friendly copy/paste prompt**. It tells the coding agent exactly what to inspect, implement, test, document, and commit.

```text
You are the Principal Distributed Systems Architect and Senior Python Engineer working on the RaceVision project.

============================================================
RACEVISION — AGENT 10.6
HISTORICAL TELEMETRY PROVIDER
============================================================

OBJECTIVE
---------

Implement Agent 10.6 — Historical Telemetry Provider.

The purpose of this agent is to allow RaceVision Runtime to consume
historical telemetry through the existing provider/runtime architecture.

Historical telemetry MUST enter Runtime through the same canonical
contracts and orchestration boundaries used by live telemetry.

DO NOT create a separate historical runtime.

DO NOT bypass the provider framework.

DO NOT bypass normalization/validation.

DO NOT create a second telemetry model.

The goal is:

Historical Provider
        ↓
Provider Framework
        ↓
Canonical Telemetry
        ↓
Normalization / Validation
        ↓
Existing Runtime/Event Bus
        ↓
Race Session / Timeline
        ↓
Consumers

============================================================
STEP 0 — READ THE REPOSITORY FIRST
============================================================

Before changing any code:

1. Inspect the complete repository structure.
2. Read:
   - docs/Roadmap.md
   - docs/specifications/README.md
   - docs/specifications/SoftwareRequirementsSpecification.md
   - docs/specifications/SystemArchitectureSpecification.md
   - docs/specifications/TelemetryProtocolSpecification.md
   - docs/specifications/ProviderFrameworkSpecification.md
   - docs/specifications/TelemetryNormalizationSpecification.md
   - docs/specifications/TelemetryValidationSpecification.md
   - docs/specifications/IngestionPipelineSpecification.md
   - docs/specifications/LiveEventBusSpecification.md
   - docs/specifications/LiveRuntimeSpecification.md
   - docs/specifications/LiveStateCacheSpecification.md
   - docs/specifications/LiveSynchronizationEngineSpecification.md
   - docs/specifications/RaceSessionDomainSpecification.md
   - docs/specifications/SessionManagerSpecification.md
   - docs/specifications/RaceEventWeekendManagerSpecification.md
   - docs/specifications/TrackSessionManagerSpecification.md
   - docs/specifications/DriverCarRuntimeRegistrySpecification.md
   - docs/specifications/RaceTimelineEngineSpecification.md

3. Inspect all existing provider implementations.

4. Inspect the current Runtime implementation.

5. Inspect the current Phase 10 domain implementation.

6. Inspect Agent 10.5 implementation and tests.

7. Inspect existing telemetry schemas/protocols.

8. Inspect existing configuration patterns.

9. Inspect existing dependency injection / composition-root patterns.

10. Inspect existing test conventions.

Do not assume filenames or APIs.

Use the actual repository implementation as the source of truth.

============================================================
STEP 1 — ARCHITECTURAL RULES
============================================================

Historical telemetry MUST conform to the existing provider architecture.

Reuse existing:

- Provider interfaces
- Provider registry
- Provider manager
- Provider lifecycle
- Provider configuration
- Canonical telemetry contracts
- Normalization
- Validation
- Ingestion pipeline
- Event Bus
- Runtime
- Session Manager
- Race Timeline Engine

Do NOT introduce:

- A parallel historical runtime
- A historical-only event model
- A historical-only telemetry schema
- Direct Runtime mutation from the provider
- Direct database writes from the provider
- Provider-specific objects leaking into Runtime
- Duplicate session/timeline logic
- Global mutable state
- Hard-coded filesystem paths
- Hard-coded credentials
- Hard-coded API keys

============================================================
STEP 2 — HISTORICAL PROVIDER CONTRACT
============================================================

Implement a historical telemetry provider using the existing provider
abstractions.

The provider must support a request equivalent to:

- championship/season
- event/Grand Prix
- session
- optional driver selection
- optional time range
- optional telemetry channels
- optional sampling/downsampling configuration

Use the project's existing domain/protocol terminology.

Do NOT invent competing terminology if an equivalent abstraction already
exists.

The provider should expose historical telemetry as an asynchronous stream
or the repository's established streaming abstraction.

Conceptually:

HistoricalTelemetryRequest
        ↓
HistoricalTelemetryProvider
        ↓
CanonicalTelemetryFrame stream

The provider must be cancellable.

The provider must support:

- start
- stop
- cancellation
- errors
- completion
- provider health/status where supported by the existing framework

============================================================
STEP 3 — HISTORICAL DATA SOURCE
============================================================

Determine the historical provider/data source already intended by the
repository.

Prefer the existing FastF1/historical-data architecture if that is what
the repository specifies.

DO NOT silently introduce a new external service.

If an existing historical provider abstraction exists, implement against it.

If the repository already contains a historical provider stub, complete it
instead of creating another provider.

The implementation must isolate third-party library/API details behind the
provider boundary.

No FastF1/API-specific objects may leak into:

- domain
- Runtime
- Event Bus
- protocols
- persistence
- session domain

============================================================
STEP 4 — HISTORICAL SESSION LOADING
============================================================

Implement historical session loading.

The provider must be able to:

1. Resolve the requested historical event.
2. Resolve the requested session.
3. Load the required telemetry.
4. Convert source telemetry into RaceVision canonical telemetry.
5. Emit canonical telemetry through the existing ingestion path.
6. Preserve source timestamps.
7. Preserve driver/car identity where available.
8. Preserve lap/session context where available.
9. Respect cancellation.
10. Report failures through existing provider error mechanisms.

Do not implement a new session state machine.

Use the Phase 10 Session Manager and Race Timeline Engine where appropriate.

============================================================
STEP 5 — TIMESTAMP / TIMELINE CORRECTNESS
============================================================

Historical telemetry must preserve temporal ordering.

Ensure:

- timestamps are timezone-aware where required
- telemetry is monotonically ordered before emission
- duplicate samples are handled according to existing ingestion rules
- missing samples do not cause fabricated telemetry
- source timestamps are not replaced with current wall-clock time
- session-relative timing is preserved where available
- race/lap timing remains compatible with Race Timeline Engine

Historical playback must therefore behave like a deterministic telemetry
source rather than pretending the data is live.

============================================================
STEP 6 — RUNTIME INTEGRATION
============================================================

Integrate historical telemetry into the existing Runtime.

Runtime must be able to distinguish:

LIVE
HISTORICAL
REPLAY

if the existing protocol/domain already supports those concepts.

If the repository does not yet support a source/mode distinction, add the
smallest appropriate domain/protocol abstraction required.

Do not duplicate Runtime logic.

Historical telemetry should enter through the same Event Bus and state
processing path wherever architecturally appropriate.

The Runtime must receive canonical telemetry rather than provider-specific
objects.

============================================================
STEP 7 — HISTORICAL MODE
============================================================

Implement a historical execution mode compatible with the current Runtime.

At minimum support:

- load historical session
- begin historical stream
- emit telemetry in deterministic order
- stop historical stream
- cancellation
- completion
- provider failure
- Runtime cleanup

Do not implement full replay controls in this agent unless the existing
Phase 10 architecture requires a minimal timeline hook.

Replay-specific functionality belongs to the later Replay phase.

============================================================
STEP 8 — DRIVER / CAR MAPPING
============================================================

Historical telemetry frequently uses source-specific driver identifiers.

Map source identifiers through the existing:

Driver
Car
Team
SessionParticipant

domain/runtime structures.

Do not create provider-specific driver registries.

Reuse Agent 10.4 Driver & Car Runtime Registry.

Unknown drivers must be handled according to existing validation/error
policies rather than silently producing corrupt state.

============================================================
STEP 9 — SESSION / TRACK INTEGRATION
============================================================

Use the existing:

- Race Event & Weekend Manager
- Track Session Manager
- Session Manager

from Phase 10.

Historical provider must not recreate:

- event identity
- session identity
- track identity
- driver identity
- car identity

It should resolve and populate existing domain structures.

============================================================
STEP 10 — CONFIGURATION
============================================================

Add only the configuration required for the historical provider.

Configuration must use the existing Pydantic/settings architecture.

Support appropriate settings for:

- provider enable/disable
- historical data source
- cache/data directory if required
- network behavior if required
- request timeout
- retry policy if applicable
- sampling/downsampling if applicable

Never hard-code:

- API keys
- credentials
- local machine paths
- URLs that should already be configurable

Do not modify unrelated configuration.

============================================================
STEP 11 — ERROR HANDLING
============================================================

Use the existing provider/runtime error contracts.

Handle at minimum:

- invalid season
- unknown event
- unknown session
- unavailable historical data
- provider initialization failure
- source library failure
- malformed source data
- unsupported telemetry channel
- missing driver mapping
- cancellation
- timeout
- partial telemetry
- unexpected provider exception

Errors must be observable and diagnosable.

Do not swallow exceptions.

Do not expose raw third-party exceptions outside the provider boundary
unless the existing architecture explicitly requires them.

============================================================
STEP 12 — CACHING
============================================================

If the existing architecture supports provider caching, integrate with it.

If no caching architecture exists, DO NOT build a large caching subsystem
for this agent.

A minimal provider-local cache may be implemented only if necessary for
performance and only behind the provider abstraction.

Do not introduce Redis or another infrastructure dependency unless the
existing architecture explicitly requires it.

============================================================
STEP 13 — TESTING
============================================================

Create comprehensive tests.

Minimum coverage should include:

PROVIDER TESTS
---------------

- provider initialization
- configuration
- provider registration
- provider selection
- provider lifecycle
- historical request validation
- session resolution
- successful telemetry loading
- empty telemetry
- malformed telemetry
- cancellation
- provider failure
- completion

MAPPING TESTS
-------------

- driver mapping
- car mapping
- team mapping
- session participant mapping
- unknown identity handling

TEMPORAL TESTS
--------------

- timestamp preservation
- chronological ordering
- duplicate handling
- missing sample handling
- session-relative timing

RUNTIME TESTS
-------------

- historical telemetry enters Runtime
- Event Bus receives canonical events
- State Cache updates correctly
- Synchronization Engine accepts historical time
- Timeline Engine receives correct events
- historical mode cleanup
- cancellation
- provider failure propagation

INTEGRATION TESTS
-----------------

Test:

Historical Provider
        ↓
Normalization
        ↓
Validation
        ↓
Event Bus
        ↓
Runtime
        ↓
Race Session
        ↓
Timeline

Use deterministic fixtures.

Do not depend on a live external API for unit tests.

Mock/isolate the third-party historical telemetry library.

============================================================
STEP 14 — PERFORMANCE
============================================================

Historical telemetry may contain very large datasets.

Do NOT load an entire race telemetry dataset into memory unless the existing
library absolutely requires it.

Prefer:

- streaming
- chunking
- bounded buffers
- generators/async generators
- incremental processing

Avoid:

- unbounded lists
- one giant ORM transaction
- unnecessary object duplication

Do not optimize prematurely beyond the existing architecture.

============================================================
STEP 15 — OBSERVABILITY
============================================================

Use existing logging/metrics conventions.

Expose useful diagnostic information such as:

- provider
- season
- event
- session
- telemetry frames loaded
- frames emitted
- frames rejected
- elapsed time
- source latency where available
- cancellation
- completion
- errors

Do not log credentials or sensitive configuration.

============================================================
STEP 16 — DOCUMENTATION
============================================================

Update the relevant specification/documentation.

Create or update the historical provider specification if the architecture
requires one.

Document:

- purpose
- supported historical source
- request model
- provider lifecycle
- Runtime integration
- configuration
- error handling
- timestamp semantics
- limitations
- testing strategy

Update docs/specifications/README.md if a new specification document is
created.

Update the project roadmap/phase tracking to reflect Agent 10.6.

Do not rewrite unrelated documentation.

============================================================
STEP 17 — CODE QUALITY
============================================================

Follow existing project standards:

- Python 3.11
- PEP 8
- type hints
- async where appropriate
- dependency inversion
- small cohesive modules
- no circular dependencies
- no unnecessary abstractions
- no dead code
- no TODO placeholders for required functionality

Run the project's existing:

- formatter
- linter
- type checker
- unit tests
- integration tests
- coverage checks

Use the actual project commands discovered from:

- pyproject.toml
- Makefile
- scripts
- CI configuration

Do not invent commands if project commands already exist.

============================================================
STEP 18 — REGRESSION SAFETY
============================================================

Before declaring Agent 10.6 complete:

Run the complete relevant test suite.

Confirm that:

- Phase 08 remains green
- Phase 09 remains green
- Phase 10.0 remains green
- Phase 10.1 remains green
- Phase 10.2 remains green
- Phase 10.3 remains green
- Phase 10.4 remains green
- Phase 10.5 remains green
- Agent 10.6 tests pass

Do not break live telemetry functionality.

Historical telemetry must be additive.

============================================================
STEP 19 — ACCEPTANCE CRITERIA
============================================================

Agent 10.6 is COMPLETE only when all are true:

[ ] Historical provider exists.
[ ] Provider uses existing provider framework.
[ ] Historical source is isolated behind provider boundary.
[ ] Historical session can be resolved.
[ ] Historical telemetry can be loaded.
[ ] Telemetry becomes canonical RaceVision telemetry.
[ ] Existing normalization is reused.
[ ] Existing validation is reused.
[ ] Historical telemetry reaches Runtime.
[ ] Event Bus integration works.
[ ] State Cache integration works.
[ ] Session Manager integration works.
[ ] Track Session Manager integration works.
[ ] Driver/Car Registry integration works.
[ ] Race Timeline Engine integration works.
[ ] Timestamp semantics are correct.
[ ] Cancellation works.
[ ] Failure propagation works.
[ ] Configuration is implemented correctly.
[ ] Tests are comprehensive.
[ ] Existing tests remain green.
[ ] Documentation is updated.
[ ] Phase tracking is updated.
[ ] No duplicate runtime was created.
[ ] No provider-specific objects leak into domain/runtime.
[ ] No hard-coded credentials exist.
[ ] No unrelated architecture was changed.

============================================================
STEP 20 — FINAL REPORT
============================================================

When implementation is complete, report:

1. Files created.
2. Files modified.
3. Historical provider/data source used.
4. Provider architecture used.
5. Runtime integration path.
6. Session/domain integration.
7. Timestamp/timeline handling.
8. Error handling.
9. Configuration added.
10. Tests added.
11. Full test result.
12. Coverage result if available.
13. Documentation updated.
14. Any limitations.
15. Any follow-up work required for Agent 10.7.

Do NOT claim completion if tests fail.

============================================================
IMPORTANT
============================================================

This is an implementation task.

Do not merely describe the implementation.

Actually inspect the repository and implement Agent 10.6.

Do not ask for confirmation unless a genuinely destructive or
architecturally irreversible decision is required.

Prefer the existing RaceVision architecture over introducing new patterns.

The repository is the source of truth.

============================================================
START
============================================================

First inspect the repository and existing Phase 10 implementation.

Then implement Agent 10.6 completely.

Run tests.

Fix failures.

Update documentation.

Only then provide the final implementation report.
```

## User

**Agent 10.6 is complete.** Historical telemetry enters Runtime through the existing provider framework — no parallel runtime.

### Architecture

`HistoricalTelemetryRequest` → `FastF1Provider` (`BaseProvider`) → canonical frames (`source_provider=historical_replay`) → Normalizer/Validation → ProviderManager → Event Bus / Cache / Session / Timeline (`TimelineMode.HISTORICAL`)

### Created

- `backend/providers/fastf1/` — adapter, request, settings, in-memory + optional SDK clients, translation, validation, health/stats
- `backend/normalization/translators/fastf1.py`
- `docs/specifications/HistoricalTelemetryProviderSpecification.md`
- Tests: `tests/providers/fastf1/` (20 tests)

### Modified

- Normalizer registry defaults, `TimelineMode.HISTORICAL`, specs README, `docs/Roadmap.md` (10.6 checked)

### Config

`FastF1Settings` — season/event/session, channels, cache dir ref, `enable_network`, `prefer_sdk`, timeout, sample\_hz. No hard-coded credentials/paths.

### Tests

| Suite                                                | Result                                    |
| ---------------------------------------------------- | ----------------------------------------- |
| FastF1 provider                                      | **20 passed**, **96.2%** package coverage |
| Phase 10 + providers                                 | **259 passed**                            |
| Event bus / ingestion / normalization / cache / sync | **244 passed**                            |
| Ruff (fastf1)                                        | clean                                     |

### Limitations / Agent 10.7 follow-ups

- SDK client is a thin boundary — full FastF1 session→packet conversion for all channels is not implemented; unit tests use `InMemoryFastF1Client` offline.
- Replay controls (seek, speed, scrub) belong to **10.7+**, not this agent.

## Assistant

Excellent. **Agent 10.6 should now be treated as complete and accepted.**

The implementation state is clear:

### Current RaceVision position

**Phase 10 — Race Session Domain**

- ✅ 10.0 Race Session Domain
- ✅ 10.1 Session Manager
- ✅ 10.2 Race Event & Weekend Manager
- ✅ 10.3 Track Session Manager
- ✅ 10.4 Driver & Car Runtime Registry
- ✅ 10.5 Race Timeline Engine
- ✅ **10.6 Historical Telemetry Provider**

The important architectural achievement is that historical data is now a **first-class telemetry source**, not a separate replay/runtime implementation:

```text
HistoricalTelemetryRequest
        │
        ▼
FastF1Provider
        │
        ▼
Canonical Telemetry Frames
        │
        ▼
Normalization
        │
        ▼
Validation
        │
        ▼
ProviderManager
        │
        ├──► Event Bus
        ├──► Live State Cache
        ├──► Session Domain
        └──► Race Timeline Engine
```

And the timeline explicitly supports:

```text
TimelineMode.HISTORICAL
```

### Validation

The numbers you supplied give us a strong acceptance result:

- **20/20** FastF1 provider tests
- **96.2%** FastF1 package coverage
- **259/259** Phase 10 + provider tests
- **244/244** Event Bus / ingestion / normalization / cache / synchronization tests
- Ruff clean

So there is no reason to reopen 10.6 unless the real FastF1 SDK integration exposes an issue later.

### The key remaining limitation

The important thing to carry forward is:

> **10.6 has the provider architecture and offline/in-memory historical path, but it does not yet provide complete real FastF1 session → canonical telemetry packet conversion for every supported channel.**

That's a meaningful distinction.

The next work should therefore **not blindly duplicate the provider**. Agent 10.7 should build on this boundary and determine exactly what the next architectural capability requires.

The other explicit boundary is:

> **Replay controls — seek, speed, scrub, deterministic playback control — are not part of 10.6.**

So I would preserve those as the next layer rather than adding them retroactively to 10.6.

**Agent 10.6 = accepted.** memcite

## User

Please give commands for Agent 10.7	Replay Runtime Core	Playback/pause/resume/seek/step ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. Agent **10.7** should build directly on 10.6 and turn the historical telemetry stream into a deterministic replay runtime, while keeping replay controls separate from the existing live Runtime.

Copy/paste the entire block into Cursor:

```text
You are the Principal Distributed Systems Architect and Senior Python Engineer working on the RaceVision project.

============================================================
RACEVISION — AGENT 10.7
REPLAY RUNTIME CORE
============================================================

OBJECTIVE
---------

Implement Agent 10.7 — Replay Runtime Core.

The purpose of this agent is to provide the core deterministic replay
execution layer for historical telemetry.

Agent 10.6 established:

    HistoricalTelemetryRequest
        ↓
    FastF1Provider
        ↓
    Canonical Telemetry
        ↓
    Normalization
        ↓
    Validation
        ↓
    ProviderManager
        ↓
    Event Bus / Cache / Session / Timeline

Agent 10.7 adds controlled playback over historical telemetry:

    Historical Telemetry
          ↓
    Replay Runtime Core
          ↓
    ┌──────────────────────────────┐
    │ PLAY                         │
    │ PAUSE                        │
    │ RESUME                       │
    │ SEEK                         │
    │ STEP FORWARD                 │
    │ STEP BACKWARD                │
    │ STOP                         │
    └──────────────────────────────┘
          ↓
    Existing Runtime/Event Bus
          ↓
    State Cache / Session / Timeline
          ↓
    Consumers

This agent MUST NOT create a second RaceVision runtime.

Replay is a controlled execution mode over historical telemetry.

============================================================
STEP 0 — READ THE REPOSITORY FIRST
============================================================

Before changing code, inspect the actual repository.

Read at minimum:

- docs/Roadmap.md
- docs/specifications/README.md
- docs/specifications/SoftwareRequirementsSpecification.md
- docs/specifications/SystemArchitectureSpecification.md
- docs/specifications/TelemetryProtocolSpecification.md
- docs/specifications/ProviderFrameworkSpecification.md
- docs/specifications/TelemetryNormalizationSpecification.md
- docs/specifications/TelemetryValidationSpecification.md
- docs/specifications/IngestionPipelineSpecification.md
- docs/specifications/LiveEventBusSpecification.md
- docs/specifications/LiveRuntimeSpecification.md
- docs/specifications/LiveStateCacheSpecification.md
- docs/specifications/LiveSynchronizationEngineSpecification.md
- docs/specifications/RuntimeIntegrationSpecification.md
- docs/specifications/RaceSessionDomainSpecification.md
- docs/specifications/SessionManagerSpecification.md
- docs/specifications/RaceEventWeekendManagerSpecification.md
- docs/specifications/TrackSessionManagerSpecification.md
- docs/specifications/DriverCarRuntimeRegistrySpecification.md
- docs/specifications/RaceTimelineEngineSpecification.md
- docs/specifications/HistoricalTelemetryProviderSpecification.md

Also inspect:

- Agent 10.5 implementation
- Agent 10.6 implementation
- TimelineMode
- Race Timeline Engine
- FastF1Provider
- ProviderManager
- Event Bus
- State Cache
- Synchronization Engine
- Session Manager
- existing replay-related code
- existing replay specifications
- existing protocol command/event/response contracts
- existing configuration system
- existing dependency injection/composition root
- existing test conventions

Do NOT assume filenames.

Use the repository implementation as the source of truth.

============================================================
STEP 1 — ARCHITECTURAL PRINCIPLE
============================================================

Replay Runtime Core MUST be implemented as a deterministic control layer.

It must NOT:

- create a second telemetry runtime
- create a second Event Bus
- create a second State Cache
- create a second Session Manager
- create a second Timeline Engine
- duplicate provider logic
- duplicate normalization
- duplicate validation
- directly write telemetry to PostgreSQL
- directly mutate domain entities
- bypass existing Runtime contracts
- introduce provider-specific telemetry objects into Runtime

Replay controls the progression of historical telemetry.

Conceptually:

    Historical Provider
           ↓
    Canonical Telemetry
           ↓
    Replay Runtime
           ↓
    Existing Runtime pipeline

The Replay Runtime is an orchestrator/controller, not a replacement
for the Runtime.

============================================================
STEP 2 — REPLAY STATE MODEL
============================================================

Implement an explicit replay lifecycle/state model using existing
RaceVision conventions.

At minimum support:

    IDLE
    LOADED
    PLAYING
    PAUSED
    SEEKING
    COMPLETED
    STOPPED
    ERROR

If the repository already has an equivalent state model, reuse it.

Do not create duplicate state enums.

Invalid state transitions MUST be rejected deterministically.

Examples:

    IDLE → PLAYING
        invalid unless telemetry/session is loaded

    IDLE → LOADED
        valid

    LOADED → PLAYING
        valid

    PLAYING → PAUSED
        valid

    PAUSED → PLAYING
        valid

    PLAYING → SEEKING
        valid

    PAUSED → SEEKING
        valid

    SEEKING → PAUSED
        valid

    PLAYING → COMPLETED
        valid

    COMPLETED → PLAYING
        valid only after an explicit restart/reset if required

Use the project's existing lifecycle conventions rather than inventing
a conflicting state machine.

============================================================
STEP 3 — REPLAY SESSION
============================================================

Create the appropriate replay session/context abstraction.

It should identify:

- replay/session ID
- source provider
- race event
- session
- timeline
- start timestamp
- current timestamp
- end timestamp
- current playback position
- playback state
- playback rate
- current frame/index if applicable

Do not duplicate RaceSession domain data.

Reference existing domain/runtime session identities.

The replay context should contain playback-specific state only.

============================================================
STEP 4 — PLAYBACK CONTROL
============================================================

Implement:

    play()
    pause()
    resume()
    stop()

Expected semantics:

PLAY
----

Starts playback from the current position.

If the replay is loaded but paused:

    play() == resume()

If already playing:

    play() must be idempotent or rejected according to existing
    command conventions.

PAUSE
-----

Stops advancing replay time.

Pause MUST NOT destroy:

- current position
- loaded telemetry
- session
- timeline
- state needed for resume

RESUME
------

Continues from exactly the paused position.

No telemetry may be skipped accidentally because of resume.

STOP
----

Stops playback and releases active playback resources.

Follow the existing lifecycle convention for whether STOP returns to
LOADED, IDLE, or STOPPED.

Do not guess if the repository already defines this.

============================================================
STEP 5 — SEEK
============================================================

Implement deterministic seeking.

Support seeking to:

- absolute replay timestamp
- session-relative time
- telemetry frame/index where appropriate

Use the existing timeline/time abstractions if available.

Example:

    seek(target_time)

Requirements:

1. Validate the target.
2. Pause or enter SEEKING according to the defined state model.
3. Move the replay cursor.
4. Reconstruct the correct Runtime state at the target.
5. Update Timeline state.
6. Update State Cache through existing contracts.
7. Publish the appropriate state/event notification.
8. Return to the correct paused/playing state.

CRITICAL:

Seeking MUST NOT merely move a cursor while leaving the Runtime state
from the previous point in time.

If seeking from:

    00:32.500

to:

    00:10.000

the Runtime must represent the state at approximately 00:10.000.

Do not allow future telemetry state to remain active after seeking
backwards.

============================================================
STEP 6 — SEEK DIRECTION
============================================================

Support:

    forward seek
    backward seek

Backward seeking is especially important.

The implementation must correctly handle:

    PLAYING
       ↓
    SEEK BACKWARD
       ↓
    reconstructed historical state
       ↓
    PAUSED/PLAYING

Do not assume telemetry can only move forward.

============================================================
STEP 7 — STEP FORWARD
============================================================

Implement:

    step_forward()

The operation must advance exactly one logical replay unit.

Prefer the existing telemetry/timeline abstraction for determining the
next unit.

The logical unit may be:

- telemetry frame
- normalized sample
- timeline event

depending on what the existing architecture defines.

Do not arbitrarily invent a 1 ms or 1 second step.

If the repository already defines a canonical frame/timeline step,
reuse it.

Requirements:

- deterministic
- exactly one logical step
- no accidental continuous playback
- correct state cache update
- correct timeline update
- correct event emission

============================================================
STEP 8 — STEP BACKWARD
============================================================

Implement:

    step_backward()

It must move exactly one logical replay unit backwards.

Requirements:

- deterministic
- correct boundary handling
- no negative timeline position
- correct State Cache reconstruction
- correct Timeline state
- correct Event Bus behavior

At the beginning of a replay:

    step_backward()

must not produce invalid negative time.

============================================================
STEP 9 — PLAYBACK CLOCK
============================================================

Implement a deterministic replay clock.

The clock must be separate from wall-clock time.

Do NOT use:

    datetime.now()

as the source of replay position.

Replay position must derive from:

- historical timestamps
- timeline
- playback clock
- playback rate

The architecture must distinguish:

    wall clock
    replay clock
    source telemetry timestamp

These are not interchangeable.

============================================================
STEP 10 — PLAYBACK RATE
============================================================

Introduce the smallest abstraction required to support playback speed.

At minimum the core should be designed to support:

    0x / paused
    1x
    >1x

If the existing architecture already specifies playback rates, reuse it.

If playback-rate control is not explicitly required yet, implement the
clock so rate can be introduced without redesigning the Replay Runtime.

Do NOT implement an elaborate speed-control UI.

Do NOT add UI code in this agent.

============================================================
STEP 11 — DETERMINISTIC PLAYBACK
============================================================

Given the same:

- telemetry dataset
- initial state
- replay configuration
- commands

the replay MUST produce the same sequence of:

- replay positions
- canonical telemetry emissions
- state transitions
- timeline positions
- state cache results

Do not use randomness.

Do not use uncontrolled wall-clock timing for state decisions.

Do not allow race conditions to determine telemetry ordering.

============================================================
STEP 12 — EVENT BUS INTEGRATION
============================================================

Replay MUST integrate with the existing Event Bus.

Do NOT create:

    ReplayEventBus

or another parallel messaging system.

Use existing event contracts where applicable.

Replay should publish appropriate events for:

- replay loaded
- playback started
- playback paused
- playback resumed
- seek started
- seek completed
- stepped
- playback completed
- replay stopped
- replay error

Reuse existing event types if they already exist.

Create new protocol/domain events only where genuinely required.

Events must contain enough information for consumers to understand:

- replay ID
- session
- current position
- state
- target position for seek where appropriate

============================================================
STEP 13 — STATE CACHE INTEGRATION
============================================================

Replay must integrate with the existing Live State Cache architecture.

Do NOT create:

    ReplayStateCache

The existing State Cache must represent the state corresponding to the
current replay position.

Forward playback:

    frame N
       ↓
    frame N+1
       ↓
    state update

Backward seek:

    frame N
       ↓
    seek to frame K
       ↓
    reconstruct state at K
       ↓
    cache represents K

State must never contain a mixture of:

    old historical state
    and future telemetry state

============================================================
STEP 14 — TIMELINE ENGINE INTEGRATION
============================================================

Agent 10.5 introduced Race Timeline Engine.

Reuse it.

Replay Runtime must treat Race Timeline Engine as the authoritative
timeline abstraction where appropriate.

Do NOT create a second replay timeline.

Replay cursor and timeline position must remain synchronized.

At all times:

    Replay Cursor
          ↕
    Race Timeline Engine
          ↕
    Runtime State

============================================================
STEP 15 — STATE RECONSTRUCTION
============================================================

Seeking backwards requires state reconstruction.

Implement the smallest correct mechanism using the existing architecture.

Possible approach:

    initial/session state
        +
    telemetry/events up to target
        ↓
    reconstructed state

If the existing State Cache already supports snapshots/checkpoints,
reuse them.

If it does not, implement a minimal deterministic reconstruction path.

Do NOT create a complex snapshot subsystem unless required.

The key acceptance requirement is:

    seek backwards → correct state

============================================================
STEP 16 — END OF REPLAY
============================================================

When the replay reaches the final telemetry/timeline position:

- stop advancing
- transition to COMPLETED
- publish completion event
- preserve final state
- preserve final replay position

Do not continue emitting duplicate final frames.

Calling play() after COMPLETED must follow the defined lifecycle
semantics.

If restart behavior is needed, provide an explicit reset/restart path
only if consistent with existing architecture.

Do not silently rewind when play() is called after completion.

============================================================
STEP 17 — EMPTY REPLAY
============================================================

Handle:

- no telemetry
- zero frames
- invalid timeline
- missing session

without crashes.

The replay should enter an appropriate terminal/error state according
to existing conventions.

No infinite playback loops.

============================================================
STEP 18 — CANCELLATION / SHUTDOWN
============================================================

Replay must support clean cancellation.

Handle:

- application shutdown
- session shutdown
- provider cancellation
- replay stop
- task cancellation

No leaked:

- asyncio tasks
- background threads
- subscriptions
- event handlers
- file handles

Use existing lifecycle management.

============================================================
STEP 19 — CONCURRENCY
============================================================

Playback commands may arrive while playback is active.

Protect against races such as:

    play()
    pause()
    play()

or:

    play()
    seek()
    pause()

or:

    seek()
    seek()

Commands must be serialized or otherwise synchronized using the existing
architecture.

There must be exactly one authoritative replay cursor.

Do NOT allow multiple playback loops to run simultaneously.

============================================================
STEP 20 — PROVIDER INTEGRATION
============================================================

Reuse Agent 10.6.

The Replay Runtime should consume the historical provider through the
existing provider framework.

Do not modify FastF1 internals unless required for a clear integration
bug.

Do not copy FastF1 translation logic into Replay.

The boundary must remain:

    Provider
       ↓
    Canonical telemetry
       ↓
    Replay Runtime

============================================================
STEP 21 — PERSISTENCE
============================================================

Do not introduce a new database schema for replay controls unless the
existing specifications explicitly require persistence at this stage.

Agent 10.7 is the Replay Runtime Core.

Persistent replay recordings/bookmarks/session metadata belong to the
appropriate later replay/persistence phase unless already implemented.

Runtime replay state should remain in memory unless existing architecture
requires otherwise.

============================================================
STEP 22 — COMMAND / RESPONSE CONTRACTS
============================================================

Inspect existing:

- Command Protocol
- Response Protocol
- Event Protocol

If replay commands belong in these protocols, implement them consistently.

Potential commands:

    ReplayLoad
    ReplayPlay
    ReplayPause
    ReplayResume
    ReplaySeek
    ReplayStepForward
    ReplayStepBackward
    ReplayStop

Do NOT create these blindly.

First determine whether equivalent contracts already exist.

Use existing protocol naming/versioning conventions.

============================================================
STEP 23 — API / UI
============================================================

DO NOT build:

- REST endpoints
- WebSocket UI
- Unity controls
- OBS controls
- frontend controls

unless the repository already requires a minimal transport contract for
the Replay Runtime itself.

Agent 10.7 is the CORE.

Transport/API/UI integration belongs to the appropriate later phase.

The core must expose clean programmatic interfaces that future API,
Unity, frontend and chat layers can call.

============================================================
STEP 24 — CONFIGURATION
============================================================

Add only configuration genuinely required for replay execution.

Use the existing configuration/Pydantic settings system.

Possible configuration:

- default playback rate
- maximum playback rate
- timing mode
- command serialization behavior
- replay buffer limits

Do not introduce unnecessary configuration.

No hard-coded paths.

============================================================
STEP 25 — OBSERVABILITY
============================================================

Use existing logging/metrics conventions.

Log/measure:

- replay ID
- session ID
- current state
- current position
- target seek position
- playback rate
- frames emitted
- step operations
- seek operations
- completion
- cancellation
- errors

Do not flood logs on every telemetry frame unless existing debug logging
explicitly supports it.

============================================================
STEP 26 — TESTING
============================================================

Create comprehensive deterministic tests.

MINIMUM TEST GROUPS
-------------------

Replay lifecycle:

- create replay
- load replay
- play
- pause
- resume
- stop
- completion
- invalid transitions

Playback:

- play advances frames
- pause stops advancement
- resume continues exactly where paused
- no duplicate playback loops
- deterministic frame ordering

Seek:

- seek forward
- seek backward
- seek while paused
- seek while playing
- seek to beginning
- seek to end
- seek beyond end
- seek before beginning
- seek to exact timestamp
- seek between timestamps if supported

Step:

- step forward once
- step forward at end
- step backward once
- step backward at beginning
- multiple deterministic steps
- step while paused
- step while playing according to defined semantics

Timeline:

- cursor equals timeline position
- timeline advances correctly
- backward seek reconstructs timeline state
- completion at final position

State Cache:

- state advances correctly
- backward seek reconstructs correct state
- no future state remains after backward seek

Event Bus:

- load event
- play event
- pause event
- resume event
- seek events
- step events
- completion event
- stop event
- error event

Concurrency:

- play/play
- play/pause
- play/seek
- seek/seek
- stop during playback
- cancellation during seek

Failure:

- empty telemetry
- invalid session
- provider failure
- malformed timeline
- cancellation
- unexpected exception

============================================================
STEP 27 — DETERMINISM TEST
============================================================

Create at least one explicit deterministic replay test.

Run the same historical fixture twice.

Verify that both runs produce identical:

- replay states
- cursor positions
- emitted telemetry ordering
- timeline positions
- State Cache results

This is a critical acceptance requirement.

============================================================
STEP 28 — PERFORMANCE TEST
============================================================

Use a sufficiently sized deterministic fixture to verify that replay does
not unnecessarily duplicate the complete telemetry dataset.

Check for:

- bounded memory behavior where possible
- no unbounded task creation
- no duplicate event subscriptions
- no duplicate playback loops

Do not build a full benchmark suite unless the project already has one.

============================================================
STEP 29 — DOCUMENTATION
============================================================

Create:

    docs/specifications/ReplayRuntimeCoreSpecification.md

unless an equivalent specification already exists.

Document:

- purpose
- architecture
- replay lifecycle
- playback state machine
- play/pause/resume
- seek
- step
- timeline integration
- state reconstruction
- State Cache integration
- Event Bus integration
- determinism
- concurrency
- cancellation
- limitations
- testing

Update:

    docs/specifications/README.md

Update:

    docs/Roadmap.md

to mark Agent 10.7 complete ONLY after all acceptance criteria pass.

============================================================
STEP 30 — CODE QUALITY
============================================================

Follow existing RaceVision standards:

- Python 3.11
- PEP 8
- type hints
- async architecture where appropriate
- dependency inversion
- clean interfaces
- no circular dependencies
- no global mutable state
- no dead code
- no unnecessary abstractions

Use the repository's actual:

- formatter
- linter
- type checker
- test runner
- coverage tooling

Discover commands from:

- pyproject.toml
- Makefile
- scripts
- CI configuration

Do not invent replacements for existing project tooling.

============================================================
STEP 31 — REGRESSION TESTING
============================================================

Before declaring Agent 10.7 complete, run:

1. FastF1 provider tests
2. Provider tests
3. Normalization tests
4. Validation tests
5. Event Bus tests
6. State Cache tests
7. Synchronization tests
8. Phase 10 tests
9. Agent 10.6 tests
10. Agent 10.7 tests
11. Full relevant project test suite

Confirm that:

- Agent 10.6 remains green
- Phase 10 remains green
- Live telemetry remains functional
- Historical telemetry remains functional
- no provider regression exists

Fix all failures caused by your changes.

============================================================
STEP 32 — ACCEPTANCE CRITERIA
============================================================

Agent 10.7 is COMPLETE only when all are true:

[ ] Replay Runtime Core exists.
[ ] Replay uses the existing Runtime architecture.
[ ] No parallel Runtime exists.
[ ] Historical telemetry can be loaded into replay.
[ ] Replay lifecycle is explicit and deterministic.
[ ] PLAY works.
[ ] PAUSE works.
[ ] RESUME works.
[ ] STOP works.
[ ] SEEK works forward.
[ ] SEEK works backward.
[ ] STEP FORWARD works.
[ ] STEP BACKWARD works.
[ ] Replay cursor is authoritative.
[ ] Replay clock is separate from wall clock.
[ ] Timeline Engine remains authoritative for timeline semantics.
[ ] State Cache reflects replay position.
[ ] Backward seeking reconstructs correct state.
[ ] Event Bus integration works.
[ ] End-of-replay handling works.
[ ] Empty replay handling works.
[ ] Cancellation works.
[ ] Shutdown is clean.
[ ] Concurrent commands are safe.
[ ] No duplicate playback loops can occur.
[ ] Deterministic replay test passes.
[ ] Provider-specific objects do not leak into Runtime.
[ ] No duplicate normalization exists.
[ ] No duplicate validation exists.
[ ] No unnecessary database schema was introduced.
[ ] No UI/API implementation was added unnecessarily.
[ ] Documentation is updated.
[ ] Roadmap is updated.
[ ] All relevant tests pass.
[ ] Existing Agent 10.6 tests remain green.
[ ] Ruff/type checking/quality gates pass.

============================================================
STEP 33 — FINAL REPORT
============================================================

When complete, report:

1. Files created.
2. Files modified.
3. Replay architecture.
4. Replay lifecycle/state machine.
5. Play/pause/resume implementation.
6. Seek implementation.
7. Step forward/backward implementation.
8. Timeline integration.
9. State Cache reconstruction.
10. Event Bus integration.
11. Concurrency strategy.
12. Cancellation/shutdown behavior.
13. Tests added.
14. Full test results.
15. Coverage result.
16. Documentation updated.
17. Roadmap status.
18. Known limitations.
19. Recommended Agent 10.8.

Do NOT claim completion if any required test fails.

============================================================
IMPORTANT
============================================================

This is an implementation task.

Do not merely describe the implementation.

Actually inspect the repository.

Build on Agents 10.5 and 10.6.

Do not rewrite working architecture.

Do not create a parallel runtime.

Do not add UI.

Do not add unnecessary infrastructure.

The repository is the source of truth.

============================================================
START
============================================================

First inspect the existing Phase 10.5 and 10.6 implementation.

Then implement Agent 10.7 completely.

Run the tests.

Fix failures.

Update specifications and roadmap.

Only then provide the final implementation report.
```

## User

**Agent 10.7 is complete.** Replay Runtime Core is a deterministic control layer over historical telemetry — no second Runtime.

### Architecture

```text
Canonical frames → ReplayService.load → FrameBuffer + ReplayClock
  → play/pause/resume/seek/step/tick
  → Timeline (REPLAY) ↔ State Cache ↔ Event Bus
```

### Created

- `backend/runtime/replay/` — service/manager/engine, clock, frame buffer, lifecycle, reconstruction
- `docs/specifications/ReplayRuntimeCoreSpecification.md`
- `tests/runtime/replay/` (core, integration, coverage)

### Modified

- `ReplayState` (+`LOADED`, `STOPPED`)
- Replay protocol events (`ReplayLoaded`, seek/step/stop/error, …) + catalogue
- Roadmap (10.7 ✓), specs README, `docs/Replay.md`, `backend/replay/` pointer

### Controls

| API                                  | Behavior                                                                |
| ------------------------------------ | ----------------------------------------------------------------------- |
| `play` / `pause` / `resume` / `stop` | Explicit `ReplayState` machine; `play` after `FINISHED` needs `reset()` |
| `seek(ms)`                           | Baseline/checkpoint restore + re-apply; timeline sync                   |
| `step_forward` / `step_backward`     | One frame; no negative time                                             |
| `tick(delta)`                        | Cooperative; `delta × rate` via `ReplayClock` (not wall clock)          |

Concurrency: `RLock` on the manager — one cursor, no dual loops.

### Tests

| Suite                   | Result                |
| ----------------------- | --------------------- |
| Replay                  | **17+** passed        |
| Replay package coverage | **\~84%** (≥80% gate) |
| Phase 10 + providers    | **241 passed**        |
| Ruff (replay)           | clean                 |

### Limitations / Agent 10.8

- No REST/WebSocket/Unity UI
- In-memory frame buffer (bounded by `max_frames`); not a recording-persistence product
- Protocol commands exist but are not yet wired through a transport dispatcher

**Recommended 10.8:** Replay transport/command adapter (map `StartReplay`/`JumpToTimestamp`/… onto `ReplayService`) and/or presentation-layer hooks.

## Assistant

Excellent. **Agent 10.7 is accepted as complete.**

The architecture is now at an important milestone:

```text
Historical Provider
       │
       ▼
Canonical Telemetry
       │
       ▼
ReplayService
       │
       ├── FrameBuffer
       ├── ReplayClock
       ├── ReplayState
       └── Reconstruction
       │
       ▼
Timeline (REPLAY)
       │
       ├── State Cache
       └── Event Bus
```

### Phase 10 status

| Agent | Component | Status |
|---|---|---|
| 10.0 | Race Session Domain | ✅ |
| 10.1 | Session Manager | ✅ |
| 10.2 | Race Event & Weekend Manager | ✅ |
| 10.3 | Track Session Manager | ✅ |
| 10.4 | Driver & Car Runtime Registry | ✅ |
| 10.5 | Race Timeline Engine | ✅ |
| 10.6 | Historical Telemetry Provider | ✅ |
| **10.7** | **Replay Runtime Core** | **✅** |

### 10.7 acceptance highlights

The important pieces are all present:

- ✅ Deterministic replay
- ✅ `play`
- ✅ `pause`
- ✅ `resume`
- ✅ `stop`
- ✅ `seek`
- ✅ `step_forward`
- ✅ `step_backward`
- ✅ Cooperative `tick()`
- ✅ Replay-specific clock
- ✅ Timeline synchronization
- ✅ State reconstruction
- ✅ State Cache integration
- ✅ Event Bus integration
- ✅ Single authoritative cursor
- ✅ Concurrency protection
- ✅ No second Runtime
- ✅ No REST/UI coupling
- ✅ ~84% replay package coverage
- ✅ Ruff clean
- ✅ 241 Phase 10/provider tests passing

The distinction between **replay time** and **wall-clock time** is particularly important for what we're building. It gives us a deterministic foundation for later replay, Unity playback, scrubbing, synchronization and eventually broadcast/presentation controls.

### 10.8 boundary

I agree with the stated boundary.

The current system has:

```text
Replay Protocol Commands
        │
        X
        │
ReplayService
```

but does **not yet have the transport/dispatcher bridge**:

```text
WebSocket / API / Command Source
             │
             ▼
      Command Dispatcher
             │
             ▼
       ReplayService
```

That makes **Agent 10.8 — Replay Transport & Command Adapter** the logical next engineering step.

I would **not add Unity UI yet**. The clean architecture is to finish the command/transport boundary first so Unity, WebSocket clients, frontend controls, OBS controls and eventually chat commands can all consume the same replay command interface rather than each talking directly to `ReplayService`.

**10.7 = accepted.** memcite

## User

Please give commands for Agent 10.8	Replay Controller	User-facing replay controls and lifecycle ( 1 click copy and paste cursor friendly)

## Assistant

Yes. **Agent 10.8** should sit above the 10.7 Replay Runtime Core and expose a clean, user-facing controller without coupling the core directly to Unity, REST, WebSocket, OBS, or chat.

Copy/paste the entire block into Cursor:

```text
You are the Principal Distributed Systems Architect and Senior Python Engineer working on the RaceVision project.

============================================================
RACEVISION — AGENT 10.8
REPLAY CONTROLLER
============================================================

OBJECTIVE
---------

Implement Agent 10.8 — Replay Controller.

Agent 10.7 delivered the deterministic Replay Runtime Core:

    Canonical Frames
          ↓
    ReplayService
          ↓
    FrameBuffer + ReplayClock
          ↓
    play / pause / resume / seek / step / tick
          ↓
    Timeline (REPLAY)
          ↓
    State Cache / Event Bus

Agent 10.8 must provide the USER-FACING CONTROL LAYER above that core.

The Replay Controller is responsible for translating user/application
intent into replay commands and exposing a clean replay lifecycle/state
interface to future consumers.

Target architecture:

    User / API / WebSocket / Unity / Chat / UI
                    │
                    ▼
            Replay Controller
                    │
                    ▼
             Replay Command
                    │
                    ▼
              ReplayService
                    │
                    ▼
             Replay Runtime
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
      Timeline            State Cache
          │                   │
          └─────────┬─────────┘
                    ▼
                 Event Bus

IMPORTANT:

The Replay Controller MUST NOT become another Runtime.

It MUST NOT duplicate:

- ReplayService
- ReplayClock
- FrameBuffer
- Timeline Engine
- State Cache
- Event Bus
- historical provider logic
- normalization
- validation

============================================================
STEP 0 — READ THE REPOSITORY FIRST
============================================================

Before modifying anything, inspect the actual repository.

Read:

- docs/Roadmap.md
- docs/Replay.md
- docs/specifications/README.md
- docs/specifications/SoftwareRequirementsSpecification.md
- docs/specifications/SystemArchitectureSpecification.md
- docs/specifications/CommandProtocolSpecification.md
- docs/specifications/ResponseProtocolSpecification.md
- docs/specifications/EventProtocolSpecification.md
- docs/specifications/ErrorProtocolSpecification.md
- docs/specifications/TelemetryProtocolSpecification.md
- docs/specifications/HistoricalTelemetryProviderSpecification.md
- docs/specifications/ReplayRuntimeCoreSpecification.md
- docs/specifications/RaceSessionDomainSpecification.md
- docs/specifications/RaceTimelineEngineSpecification.md
- docs/specifications/LiveRuntimeSpecification.md
- docs/specifications/LiveStateCacheSpecification.md
- docs/specifications/LiveEventBusSpecification.md

Inspect the implementation of:

- backend/runtime/replay/
- ReplayService
- ReplayManager
- ReplayEngine
- ReplayClock
- FrameBuffer
- ReplayState
- reconstruction
- Replay protocol events
- protocol catalogue
- ProviderManager
- Event Bus
- State Cache
- Race Timeline Engine
- Phase 10 Session Manager
- existing command dispatcher infrastructure
- existing controller/application-service patterns
- existing API/WebSocket infrastructure, if present
- dependency injection/composition root
- configuration system
- test conventions

Inspect Agent 10.7 tests before implementation.

Do not assume filenames.

The repository is the source of truth.

============================================================
STEP 1 — ARCHITECTURAL RESPONSIBILITY
============================================================

The Replay Controller is an APPLICATION/CONTROL layer.

Its responsibility is:

    user intent
        ↓
    validate command
        ↓
    resolve replay/session
        ↓
    call ReplayService
        ↓
    return structured result
        ↓
    Event Bus publishes lifecycle events

The Controller should answer:

- What replay is active?
- Can the requested action happen?
- What command is being requested?
- What is the current replay state?
- What is the current position?
- What happened as a result?

The Controller should NOT answer:

- How telemetry is stored
- How frames are reconstructed internally
- How the replay clock works
- How the Timeline Engine works
- How State Cache works

Those responsibilities belong to Agent 10.7 and earlier layers.

============================================================
STEP 2 — CONTROLLER CONTRACT
============================================================

Create a clean Replay Controller abstraction.

Use the repository's existing naming conventions.

Conceptually:

    ReplayController

with operations equivalent to:

    load(...)
    play(...)
    pause(...)
    resume(...)
    stop(...)
    reset(...)
    seek(...)
    step_forward(...)
    step_backward(...)
    get_state(...)
    get_position(...)
    get_status(...)

Do NOT blindly create every method if an equivalent already exists.

Reuse existing ReplayService methods.

The Controller should not expose internal implementation objects.

============================================================
STEP 3 — USER-FACING REPLAY LIFECYCLE
============================================================

Provide a clear lifecycle:

    NO_REPLAY
        ↓
    LOADING
        ↓
    LOADED
        ↓
    PLAYING
        ↕
    PAUSED
        ↓
    SEEKING
        ↓
    PAUSED / PLAYING
        ↓
    FINISHED
        ↓
    RESET
        ↓
    LOADED

If the repository's existing ReplayState differs, reuse it.

Do NOT create duplicate lifecycle enums.

The Controller must expose the current state in a stable form suitable
for future UI/API/WebSocket/Unity consumers.

============================================================
STEP 4 — LOAD REPLAY
============================================================

Implement user-facing replay loading.

The Controller must be able to request loading of an historical replay
using existing abstractions.

Possible inputs include:

- replay/session ID
- race event
- season
- session
- provider
- historical telemetry request

Use the existing Agent 10.6 historical provider.

Do not directly call FastF1 from the Controller.

Required flow:

    Controller
       ↓
    Provider/Replay loading abstraction
       ↓
    Canonical frames
       ↓
    ReplayService.load()

If the repository already provides a replay loading service, use it.

Do not duplicate historical data loading.

============================================================
STEP 5 — PLAY
============================================================

Expose a user-facing PLAY operation.

Behavior:

    LOADED  → PLAYING
    PAUSED  → PLAYING

If already PLAYING:

- operation should be idempotent OR return a structured already-playing
  result according to project conventions.

If FINISHED:

- do NOT silently rewind.
- require reset/reload according to Agent 10.7 semantics.

Return a structured controller response.

============================================================
STEP 6 — PAUSE
============================================================

Expose PAUSE.

Behavior:

    PLAYING → PAUSED

Pause must preserve:

- replay position
- current frame
- timeline position
- State Cache state
- loaded replay

Repeated pause must not corrupt state.

============================================================
STEP 7 — RESUME
============================================================

Expose RESUME.

Behavior:

    PAUSED → PLAYING

Resume must continue from the exact current replay position.

No frame skipping caused by the Controller.

============================================================
STEP 8 — STOP
============================================================

Expose STOP.

Follow the lifecycle semantics implemented by Agent 10.7.

Do not invent different stop behavior.

The Controller should return the resulting lifecycle state.

Stop must cleanly release the active playback execution resources.

============================================================
STEP 9 — RESET
============================================================

Expose RESET because Agent 10.7 specifies:

    play() after FINISHED requires reset()

Reset should return the replay to its initial loaded position/state.

Expected behavior:

    FINISHED → LOADED
    STOPPED  → LOADED
    PAUSED   → LOADED

Use ReplayService.reset() if present.

If reset does not exist, add the smallest appropriate method to the
Replay Runtime Core.

Do not duplicate replay state reconstruction in the Controller.

============================================================
STEP 10 — SEEK
============================================================

Expose user-facing seeking.

Support the existing Agent 10.7 seek semantics.

At minimum:

    seek(milliseconds)

The Controller should validate:

- numeric input
- finite value
- valid replay bounds

Return a structured result containing:

- previous position
- target position
- resulting position
- resulting state
- replay ID

Backward seeking MUST correctly reconstruct the state.

The Controller must not implement reconstruction itself.

============================================================
STEP 11 — STEP CONTROLS
============================================================

Expose:

    step_forward()
    step_backward()

These must call the Agent 10.7 ReplayService operations.

Do not duplicate frame navigation.

The Controller should return:

- previous position
- new position
- current frame/timeline information where appropriate
- resulting replay state

Stepping at boundaries must produce deterministic results.

============================================================
STEP 12 — REPLAY STATUS
============================================================

Implement a read-only status model suitable for UI/API consumers.

Conceptually:

    ReplayStatus

containing only stable public information such as:

- replay_id
- session_id
- state
- position_ms
- duration_ms
- progress
- current_frame
- total_frames
- playback_rate
- source/provider
- timeline_mode
- can_play
- can_pause
- can_resume
- can_seek
- can_step_forward
- can_step_backward
- can_reset
- can_stop

Do not expose internal locks, buffers, tasks or implementation objects.

============================================================
STEP 13 — CONTROL AVAILABILITY
============================================================

The Controller must expose whether commands are currently valid.

For example:

LOADED:

    can_play = true
    can_pause = false
    can_resume = false
    can_seek = true
    can_step_forward = true
    can_step_backward = true
    can_reset = true

PLAYING:

    can_play = false or idempotent
    can_pause = true
    can_resume = false
    can_seek = true
    can_step_forward = defined by architecture
    can_step_backward = defined by architecture
    can_stop = true

PAUSED:

    can_play = true
    can_pause = false
    can_resume = true
    can_seek = true
    can_step_forward = true
    can_step_backward = true

FINISHED:

    can_play = false
    can_pause = false
    can_resume = false
    can_seek = true
    can_reset = true

Use actual Agent 10.7 semantics where they differ.

============================================================
STEP 14 — COMMAND ADAPTER
============================================================

Agent 10.7 already created replay protocol commands.

Inspect the existing protocol definitions.

Identify commands such as:

- StartReplay
- PauseReplay
- ResumeReplay
- StopReplay
- ResetReplay
- JumpToTimestamp
- StepForward
- StepBackward

Use the actual names from the repository.

Implement a command adapter/dispatcher that maps protocol commands to
ReplayController operations.

Conceptually:

    Command
       ↓
    ReplayCommandDispatcher
       ↓
    ReplayController
       ↓
    ReplayService

Do not let transport-specific code call ReplayService directly.

============================================================
STEP 15 — COMMAND VALIDATION
============================================================

Validate commands before invoking ReplayService.

Examples:

- missing replay ID
- invalid timestamp
- negative timestamp
- timestamp outside replay bounds
- invalid playback rate
- command for nonexistent replay
- command for inactive replay
- command invalid for current state

Return existing structured protocol errors.

Do not throw raw ValueError/RuntimeError across protocol boundaries.

Use existing Error Protocol conventions.

============================================================
STEP 16 — COMMAND RESPONSES
============================================================

Use the existing Response Protocol.

Each accepted command should produce a structured response.

Response should include, where appropriate:

- command ID
- replay ID
- success/failure
- resulting state
- resulting position
- error code if failed

Do not invent a second response envelope.

Use the existing shared protocol envelope.

============================================================
STEP 17 — IDEMPOTENCY
============================================================

User-facing controls must be safe when commands are repeated.

At minimum evaluate:

    play → play
    pause → pause
    resume → resume
    stop → stop
    reset → reset

Use the project's command semantics.

Repeated commands must not:

- create multiple playback loops
- duplicate event subscriptions
- corrupt replay state
- move the cursor unexpectedly

============================================================
STEP 18 — CONCURRENCY
============================================================

Reuse Agent 10.7's concurrency strategy.

Do not introduce a second locking system unless necessary.

The Controller must ensure that concurrent commands are serialized
appropriately.

Test:

    play + pause
    play + seek
    seek + seek
    pause + seek
    reset + play
    stop + play

There must remain exactly one authoritative replay cursor.

============================================================
STEP 19 — EVENT SUBSCRIPTION
============================================================

The Controller may subscribe to existing replay lifecycle events if
needed to maintain its public status.

Do NOT create another Event Bus.

Do NOT duplicate replay events.

If the Controller maintains a status snapshot, ensure it is updated from
the authoritative ReplayService/events.

The Controller must never become a second source of truth.

============================================================
STEP 20 — USER-FACING EVENT MODEL
============================================================

Inspect existing Replay events.

Where useful, expose stable lifecycle notifications for consumers:

- ReplayLoaded
- ReplayStarted
- ReplayPaused
- ReplayResumed
- ReplaySeeked
- ReplayStepped
- ReplayStopped
- ReplayReset
- ReplayFinished
- ReplayError

Reuse existing event definitions from Agent 10.7.

Only add missing events where there is a genuine requirement.

Do not create duplicate event names for the same semantic event.

============================================================
STEP 21 — TRANSPORT INDEPENDENCE
============================================================

The Controller and command dispatcher MUST remain transport-independent.

Do NOT tightly couple to:

- FastAPI
- WebSocket
- Unity
- Twitch
- Kick
- YouTube
- OBS

Future adapters must be able to call:

    ReplayController

without knowing ReplayService internals.

If the repository already has a transport dispatcher abstraction, integrate
with it rather than creating a competing architecture.

============================================================
STEP 22 — API / WEBSOCKET PREPARATION
============================================================

Prepare clean interfaces for future:

- REST API
- WebSocket
- Unity
- frontend
- OBS
- chat commands

But do NOT implement full API/UI/Unity/OBS integration in this agent unless
the existing architecture already requires a minimal adapter.

The goal is:

    future consumer
          ↓
    command transport
          ↓
    replay command dispatcher
          ↓
    ReplayController
          ↓
    ReplayService

============================================================
STEP 23 — ERROR HANDLING
============================================================

Handle:

- replay not found
- replay not loaded
- invalid lifecycle transition
- invalid seek
- invalid step
- replay already playing
- replay already paused
- replay finished
- replay stopped
- provider failure
- Runtime failure
- cancellation
- unexpected exception

Map errors to the existing protocol error taxonomy.

Do not swallow errors.

Do not expose third-party exceptions.

============================================================
STEP 24 — CONFIGURATION
============================================================

Use the existing configuration system.

Only add configuration if genuinely necessary.

Do NOT add:

- transport-specific configuration
- UI configuration
- Unity configuration
- OBS configuration

unless already required by the repository.

============================================================
STEP 25 — OBSERVABILITY
============================================================

Use existing logging/metrics.

Record useful controller operations:

- command received
- replay ID
- command ID
- requested operation
- previous state
- resulting state
- previous position
- resulting position
- validation failure
- command failure

Do not log every telemetry frame.

Do not log sensitive information.

============================================================
STEP 26 — TESTING
============================================================

Create comprehensive tests.

Create:

    tests/runtime/replay_controller/

or follow the repository's existing structure.

TEST CONTROLLER LIFECYCLE
-------------------------

Test:

- load
- play
- pause
- resume
- stop
- reset
- finish
- lifecycle transitions
- invalid transitions

TEST CONTROLS
-------------

- play
- pause
- resume
- stop
- reset
- seek forward
- seek backward
- step forward
- step backward

TEST STATUS
-----------

Verify:

- state
- position
- duration
- progress
- current frame
- frame count
- playback rate
- capabilities

TEST COMMAND DISPATCH
---------------------

Test:

- command → controller
- command validation
- command response
- command ID propagation
- replay ID propagation
- error response
- invalid command
- unknown replay

TEST IDEMPOTENCY
----------------

Test:

- play/play
- pause/pause
- resume/resume
- stop/stop
- reset/reset

TEST CONCURRENCY
----------------

Test:

- play/pause
- play/seek
- seek/seek
- pause/seek
- reset/play
- stop/play

Ensure no dual playback loop.

TEST EVENT INTEGRATION
----------------------

Verify:

- loaded
- started
- paused
- resumed
- seeked
- stepped
- stopped
- reset
- finished
- error

Use the existing Event Bus.

TEST ERROR MAPPING
------------------

Verify protocol-level error responses for:

- invalid state
- invalid seek
- missing replay
- invalid command
- provider/runtime failure
- cancellation

============================================================
STEP 27 — DETERMINISM REGRESSION
============================================================

Run the Agent 10.7 deterministic replay test through the Controller.

Verify that using:

    Controller.play()
    Controller.pause()
    Controller.seek()
    Controller.step_forward()
    Controller.step_backward()

does not alter deterministic replay semantics.

The Controller must be a thin orchestration layer.

============================================================
STEP 28 — PUBLIC API QUALITY
============================================================

The Controller API must be easy for future consumers to understand.

Avoid exposing:

- internal frame objects
- locks
- asyncio Tasks
- internal buffers
- provider SDK objects
- database sessions
- Timeline Engine internals

Return stable DTO/value objects.

Use immutable/read-only status/result objects where consistent with the
existing project architecture.

============================================================
STEP 29 — DOCUMENTATION
============================================================

Create:

    docs/specifications/ReplayControllerSpecification.md

unless an equivalent specification already exists.

Document:

- Controller responsibilities
- lifecycle
- commands
- command validation
- responses
- status model
- capability model
- Event Bus integration
- concurrency
- transport independence
- error handling
- future API/WebSocket/Unity integration

Update:

    docs/specifications/README.md

Update:

    docs/Replay.md

Update:

    docs/Roadmap.md

Mark Agent 10.8 complete ONLY after all acceptance criteria and tests pass.

============================================================
STEP 30 — CODE QUALITY
============================================================

Follow RaceVision standards:

- Python 3.11
- PEP 8
- type hints
- dependency inversion
- async where appropriate
- clear application/service boundaries
- no circular imports
- no global mutable state
- no duplicated runtime logic
- no dead code
- no unnecessary abstractions

Use the repository's actual:

- formatter
- linter
- type checker
- test runner
- coverage tooling

Discover commands from:

- pyproject.toml
- Makefile
- scripts
- CI configuration

============================================================
STEP 31 — REGRESSION TESTING
============================================================

Before declaring Agent 10.8 complete, run:

1. FastF1 provider tests
2. Provider tests
3. Normalization tests
4. Validation tests
5. Event Bus tests
6. State Cache tests
7. Synchronization tests
8. Phase 10 tests
9. Agent 10.6 tests
10. Agent 10.7 replay tests
11. Agent 10.8 Controller tests
12. Full relevant project test suite

Confirm:

- historical telemetry still works
- Replay Runtime still works
- deterministic replay still works
- State Cache still works
- Timeline still works
- Event Bus still works
- no live telemetry regression exists

Fix all failures caused by the implementation.

============================================================
STEP 32 — ACCEPTANCE CRITERIA
============================================================

Agent 10.8 is COMPLETE only when all are true:

[ ] Replay Controller exists.
[ ] Controller is above ReplayService.
[ ] Controller does not duplicate ReplayService.
[ ] Controller does not create another Runtime.
[ ] User-facing replay lifecycle exists.
[ ] Load works.
[ ] Play works.
[ ] Pause works.
[ ] Resume works.
[ ] Stop works.
[ ] Reset works.
[ ] Seek works.
[ ] Step forward works.
[ ] Step backward works.
[ ] Public replay status exists.
[ ] Control availability/capabilities are exposed.
[ ] Protocol commands map to Controller operations.
[ ] Existing command contracts are reused.
[ ] Structured responses are returned.
[ ] Existing Error Protocol is reused.
[ ] Invalid lifecycle operations are handled correctly.
[ ] Repeated commands are safe.
[ ] Concurrent commands are serialized safely.
[ ] Event Bus remains the authoritative event mechanism.
[ ] Controller does not become a second source of truth.
[ ] Transport independence is preserved.
[ ] Future API/WebSocket/Unity consumers can call the Controller cleanly.
[ ] No direct FastF1 access exists in Controller.
[ ] No provider-specific objects leak into Controller API.
[ ] Agent 10.7 deterministic behavior remains unchanged.
[ ] Documentation is updated.
[ ] Roadmap is updated.
[ ] All tests pass.
[ ] Ruff/type checking/quality gates pass.

============================================================
STEP 33 — FINAL REPORT
============================================================

When complete, report:

1. Files created.
2. Files modified.
3. Replay Controller architecture.
4. Public Controller API.
5. Lifecycle/state handling.
6. Command dispatcher implementation.
7. Response implementation.
8. Status/capability model.
9. Event integration.
10. Error handling.
11. Concurrency strategy.
12. Transport-independence strategy.
13. Tests added.
14. Test results.
15. Coverage result.
16. Documentation updated.
17. Roadmap status.
18. Known limitations.
19. Recommended Agent 10.9.

Do NOT claim completion if any required test fails.

============================================================
IMPORTANT
============================================================

This is an implementation task.

Do not merely describe the implementation.

Actually inspect and modify the repository.

Build on Agents 10.5, 10.6 and 10.7.

Do not rewrite working Replay Runtime code.

Do not create a second Runtime.

Do not bypass ReplayService.

Do not add a frontend.

Do not add Unity UI.

Do not add OBS integration.

Do not add transport-specific logic unless the repository already provides
the required transport abstraction.

The repository is the source of truth.

============================================================
START
============================================================

First inspect Agent 10.7 and the existing protocol/command architecture.

Then implement Agent 10.8 completely.

Run all relevant tests.

Fix failures.

Update specifications and roadmap.

Only then provide the final implementation report.
```

## User

**Agent 10.8 is complete.** User-facing control plane sits above `ReplayService` — no second Runtime.

### Architecture

```text
Command → ReplayCommandDispatcher → ReplayApplicationController → ReplayService
```

Lifecycle façade `ReplayController` (start/stop/shutdown) is unchanged.

### Created

- `backend/runtime/replay/control/` — application controller, dispatcher, status/capabilities, results, error mapping
- `docs/specifications/ReplayControllerSpecification.md`
- `tests/runtime/replay_controller/`

### Protocol additions

- `ResetReplay` command · `ReplayReset` event
- Richer replay responses (state/position) · `ReplayNotLoaded` / `InvalidState` / `InvalidSeek` errors

### Public API

`load` / `load_historical` · `play`/`pause`/`resume`/`stop`/`reset` · `seek` · `step_*` · `get_status` (with `can_*` capabilities) · structured `ReplayControlResult`

### Tests

| Suite                                   | Result                                    |
| --------------------------------------- | ----------------------------------------- |
| Controller + runtime replay             | **28 passed**, **\~85%** control coverage |
| Broader Phase 10 / providers / eventbus | **178 + 175** passed                      |
| Ruff                                    | clean                                     |

### Docs / roadmap

Specs README, `docs/Replay.md`, Roadmap **10.8 ✓**

### Limitations / Agent 10.9

No REST/WebSocket/Unity transport yet. **Recommended 10.9:** thin HTTP/WS adapter calling `ReplayCommandDispatcher` only.

## Assistant

Excellent. **Agent 10.8 is accepted as complete.**

The Phase 10 replay architecture is now cleanly layered:

```text
Historical Telemetry
        │
        ▼
  FastF1 Provider
        │
        ▼
 Canonical Frames
        │
        ▼
 ReplayService
        │
        ▼
 ReplayApplicationController
        │
        ▼
 ReplayCommandDispatcher
        │
        ▼
 REST / WebSocket / Unity / Frontend / Chat
        │
        ▼
   Future consumers
```

### Phase 10 status

| Agent | Component | Status |
|---|---|---|
| 10.0 | Race Session Domain | ✅ |
| 10.1 | Session Manager | ✅ |
| 10.2 | Race Event & Weekend Manager | ✅ |
| 10.3 | Track Session Manager | ✅ |
| 10.4 | Driver & Car Runtime Registry | ✅ |
| 10.5 | Race Timeline Engine | ✅ |
| 10.6 | Historical Telemetry Provider | ✅ |
| 10.7 | Replay Runtime Core | ✅ |
| **10.8** | **Replay Controller** | **✅** |

### What 10.8 successfully establishes

The key architectural boundary is now:

```text
Transport
   ↓
ReplayCommandDispatcher
   ↓
ReplayApplicationController
   ↓
ReplayService
   ↓
Replay Runtime Core
```

That is exactly the right separation.

The addition of:

- `ResetReplay`
- `ReplayReset`
- structured replay responses
- `ReplayNotLoaded`
- `InvalidState`
- `InvalidSeek`
- `can_*` capabilities
- `ReplayControlResult`

means future clients don't need to understand the internals of `ReplayService`.

The **~85% control coverage** plus the broader Phase 10/provider/event-bus test results are also sufficient to accept the agent given the stated scope.

### 10.9 boundary

Your proposed 10.9 is logical:

> **Replay Transport Adapter — HTTP/WebSocket**

The important constraint should be maintained:

```text
HTTP / WebSocket
       ↓
Transport Adapter
       ↓
ReplayCommandDispatcher
       ↓
ReplayApplicationController
       ↓
ReplayService
```

**Not:**

```text
HTTP / WebSocket
       ↓
ReplayService
```

That would bypass the control plane that 10.8 just established.

I would also keep **Unity, OBS, Twitch/Kick/YouTube and chat integration out of 10.9** unless the existing phase plan explicitly calls for them. The transport adapter should remain thin and protocol-driven.

**Agent 10.8 = accepted.** memcite

## User

Please give commands for Agent 10.9	Replay Synchronization	Synchronize replay with Runtime/Timeline ( 1 click copy and paste cursor friendly)

## Assistant

Yes. **Agent 10.9** should make the replay system a properly synchronized participant in the existing Runtime/Timeline architecture. The key requirement is that **ReplayService, Runtime state, State Cache, and Race Timeline Engine never drift apart**, especially during seek, pause/resume, stepping, and completion.

Copy/paste the entire block into Cursor:

```text
You are the Principal Distributed Systems Architect and Senior Python Engineer working on the RaceVision project.

============================================================
RACEVISION — AGENT 10.9
REPLAY SYNCHRONIZATION
============================================================

OBJECTIVE
---------

Implement Agent 10.9 — Replay Synchronization.

The purpose of this agent is to make Replay Runtime, Runtime State,
State Cache, and Race Timeline Engine operate from one authoritative
replay position without temporal or state drift.

Agent 10.7 implemented the deterministic Replay Runtime Core.

Agent 10.8 implemented the user-facing Replay Controller and command
dispatch layer.

Agent 10.9 must now establish robust synchronization between:

    Replay Runtime
          ↕
    Replay Clock / Cursor
          ↕
    Race Timeline Engine
          ↕
    Runtime State
          ↕
    State Cache
          ↕
    Event Bus

The target architecture is:

    User / Transport
          │
          ▼
    ReplayCommandDispatcher
          │
          ▼
    ReplayApplicationController
          │
          ▼
    ReplayService
          │
          ├── Replay Clock
          ├── Frame Buffer
          ├── Replay Cursor
          └── Reconstruction
          │
          ▼
    Replay Synchronization Layer
          │
          ├──────────────► Race Timeline Engine
          │
          ├──────────────► Runtime State
          │
          └──────────────► State Cache
                           │
                           ▼
                       Event Bus

IMPORTANT:

There MUST remain exactly ONE authoritative replay position.

Do NOT create:

- a second replay clock
- a second timeline
- a second State Cache
- a second Runtime
- a second telemetry cursor
- duplicate state reconstruction
- duplicate normalization
- duplicate validation

============================================================
STEP 0 — READ THE REPOSITORY FIRST
============================================================

Before modifying anything, inspect the actual repository.

Read:

- docs/Roadmap.md
- docs/Replay.md
- docs/specifications/README.md
- docs/specifications/SoftwareRequirementsSpecification.md
- docs/specifications/SystemArchitectureSpecification.md
- docs/specifications/TelemetryProtocolSpecification.md
- docs/specifications/LiveRuntimeSpecification.md
- docs/specifications/LiveStateCacheSpecification.md
- docs/specifications/LiveSynchronizationEngineSpecification.md
- docs/specifications/RaceSessionDomainSpecification.md
- docs/specifications/RaceTimelineEngineSpecification.md
- docs/specifications/HistoricalTelemetryProviderSpecification.md
- docs/specifications/ReplayRuntimeCoreSpecification.md
- docs/specifications/ReplayControllerSpecification.md

Inspect:

- backend/runtime/replay/
- ReplayService
- ReplayManager
- ReplayEngine
- ReplayClock
- FrameBuffer
- ReplayState
- reconstruction
- backend/runtime/replay/control/
- ReplayApplicationController
- ReplayCommandDispatcher
- ReplayController
- State Cache implementation
- Synchronization Engine
- Race Timeline Engine
- Event Bus
- Runtime state models
- telemetry event contracts
- replay protocol events
- existing synchronization code
- Phase 10.5
- Phase 10.6
- Phase 10.7
- Phase 10.8

Inspect all tests related to replay, timeline, state cache, synchronization,
and Event Bus.

Do not assume filenames.

The repository is the source of truth.

============================================================
STEP 1 — CORE SYNCHRONIZATION PRINCIPLE
============================================================

There must be one authoritative replay position.

The authoritative position is owned by the Replay Runtime/Core already
implemented in Agent 10.7.

Do NOT make Timeline Engine authoritative over ReplayService.

Do NOT make State Cache authoritative over ReplayService.

Do NOT create another cursor.

The model must be:

    ReplayService
         │
         │ authoritative position
         ▼
    Synchronization Layer
         │
         ├── Timeline
         ├── Runtime State
         └── State Cache

The synchronization layer mirrors/reconstructs downstream state from
the authoritative replay position.

============================================================
STEP 2 — SYNCHRONIZATION CONTRACT
============================================================

Create an explicit synchronization abstraction using existing project
patterns.

Use an appropriate name such as:

    ReplaySynchronizationService
    ReplayRuntimeSynchronizer

unless an equivalent already exists.

Responsibilities:

- synchronize replay position
- synchronize timeline
- synchronize Runtime state
- synchronize State Cache
- process forward movement
- process backward seek
- process step
- process reset
- process completion
- detect drift
- recover from drift where possible
- publish synchronization events/errors

The synchronizer must NOT own the replay clock.

It observes the ReplayService's authoritative position.

============================================================
STEP 3 — SYNCHRONIZATION SNAPSHOT
============================================================

Create a stable synchronization snapshot/value object.

It should contain only information required to verify consistency.

Conceptually:

    ReplaySynchronizationSnapshot

with:

- replay_id
- session_id
- replay_state
- replay_position_ms
- timeline_position_ms
- state_cache_position_ms
- current_frame_index
- current_frame_timestamp
- timeline_mode
- synchronization_status
- synchronization_version if appropriate

Use existing domain/protocol terminology where possible.

Do not expose internal implementation objects.

============================================================
STEP 4 — POSITION CONSISTENCY
============================================================

Define the invariant:

    replay_position
        ==
    timeline_position
        ==
    state_cache_position

within the project's explicitly defined precision/tolerance.

Do NOT compare floating point values blindly if the system uses floating
point time.

Use a deterministic time representation where possible.

Prefer:

- integer milliseconds
- integer microseconds
- existing Duration/Timecode type

if already defined.

If timestamps are higher precision internally, use the existing canonical
representation.

============================================================
STEP 5 — TEMPORAL TOLERANCE
============================================================

If exact equality is not appropriate, define one central synchronization
tolerance.

For example:

    synchronization_tolerance_ms

Do NOT scatter tolerance values throughout the code.

Configuration should be added only if the existing architecture needs
it.

Document the selected tolerance.

The tolerance must never hide meaningful drift.

============================================================
STEP 6 — FORWARD PLAYBACK SYNCHRONIZATION
============================================================

During normal playback:

    ReplayService
        ↓
    frame N
        ↓
    Synchronization Layer
        ↓
    Timeline
        ↓
    Runtime State
        ↓
    State Cache

Then:

    frame N+1
        ↓
    same synchronization path

Ensure:

- frame order remains deterministic
- timeline advances correctly
- State Cache advances correctly
- Runtime state corresponds to the current frame
- no duplicate frames are applied
- no future frame is applied early

============================================================
STEP 7 — PAUSE SYNCHRONIZATION
============================================================

When replay pauses:

- replay position stops
- timeline position stops
- Runtime state remains unchanged
- State Cache remains unchanged

Pause MUST NOT trigger:

- unintended frame advancement
- timeline drift
- duplicate state updates
- stale synchronization state

The synchronization snapshot must remain internally consistent.

============================================================
STEP 8 — RESUME SYNCHRONIZATION
============================================================

When replay resumes:

- continue from the exact replay position
- synchronize the next frame correctly
- do not skip frames
- do not replay already-applied frames unintentionally

Verify:

    pause at T
    resume
    next position > T

and not:

    next position < T

or:

    next position jumps unexpectedly

============================================================
STEP 9 — FORWARD SEEK
============================================================

For:

    seek(T_future)

the synchronization layer must:

1. pause/enter seeking according to existing lifecycle semantics
2. move ReplayService cursor
3. reconstruct Runtime state at T_future
4. synchronize Timeline
5. synchronize State Cache
6. publish synchronization event
7. restore appropriate replay state

Do NOT simply set:

    timeline.current_time = T_future

without rebuilding downstream state.

The resulting system must represent the world at T_future.

============================================================
STEP 10 — BACKWARD SEEK
============================================================

Backward seeking is the most important synchronization requirement.

Example:

    current = 60 seconds
    seek(20 seconds)

After completion:

    Replay position = 20s
    Timeline = 20s
    State Cache = state at 20s
    Runtime State = state at 20s

There must be NO state left over from 60 seconds.

For example:

- cars from 60s must not remain at 60s positions
- lap state must correspond to 20s
- sector state must correspond to 20s
- race events must not incorrectly remain in the future
- driver/car state must correspond to the target point

Reuse Agent 10.7 reconstruction mechanisms.

Do not duplicate reconstruction logic.

============================================================
STEP 11 — STATE CACHE RECONSTRUCTION
============================================================

When seeking backward:

    Snapshot/initial state
          +
    frames/events through target
          ↓
    reconstructed state
          ↓
    State Cache

Use existing State Cache APIs.

Do not directly mutate internal cache dictionaries if a public API exists.

If the State Cache does not currently support replacement/reconstruction,
add the smallest proper abstraction required.

Do not create ReplayStateCache.

============================================================
STEP 12 — TIMELINE SYNCHRONIZATION
============================================================

Race Timeline Engine from Agent 10.5 remains the canonical timeline
abstraction.

Replay Synchronization must keep it synchronized with ReplayService.

Support:

- forward playback
- pause
- resume
- forward seek
- backward seek
- step forward
- step backward
- reset
- completion

The timeline mode must remain:

    TimelineMode.REPLAY

Do not introduce another timeline mode unless the existing architecture
requires it.

============================================================
STEP 13 — RUNTIME STATE SYNCHRONIZATION
============================================================

Inspect the existing Runtime state architecture.

The synchronized Runtime state must represent the same point in time as:

- ReplayService
- Timeline
- State Cache

Do not create a replay-specific Runtime state model unless the repository
already defines one.

If an existing Runtime state object supports source/mode metadata, use:

    source = historical/replay
    timeline_mode = REPLAY

or the repository's canonical equivalents.

============================================================
STEP 14 — EVENT BUS ORDERING
============================================================

Synchronization events must be emitted in a deterministic order.

For a normal frame:

    Replay position advances
          ↓
    Runtime/Timeline/Cache synchronized
          ↓
    synchronized state available
          ↓
    event published

Consumers should not receive an event claiming:

    "position = T"

while State Cache still represents:

    "position = T-1"

Avoid observable half-updated states.

============================================================
STEP 15 — SYNCHRONIZATION EVENTS
============================================================

Inspect existing replay events.

Reuse them where possible.

If necessary, introduce a synchronization event such as:

    ReplaySynchronized

or an equivalent existing event.

It should contain sufficient information to identify:

- replay ID
- session ID
- replay position
- timeline position
- synchronization status
- frame index
- source/mode

Do not create redundant events for every existing replay event.

============================================================
STEP 16 — DRIFT DETECTION
============================================================

Implement explicit drift detection.

Detect mismatches such as:

    Replay = 10000ms
    Timeline = 10000ms
    Cache = 9500ms

or:

    Replay frame = 50
    Timeline frame = 49

The synchronizer should expose:

    synchronized = true/false

and an appropriate diagnostic status.

Do not silently ignore drift.

============================================================
STEP 17 — DRIFT RECOVERY
============================================================

Where safe, the synchronizer should recover from drift.

For example:

    Replay authoritative = 10000ms
    Timeline = 9500ms

The synchronizer may resynchronize Timeline to 10000ms using the
existing Timeline API.

For State Cache drift, reconstruct from the authoritative replay position
using the existing reconstruction mechanism.

Recovery MUST NOT modify ReplayService's authoritative cursor.

If automatic recovery is unsafe, report a structured synchronization
error instead.

============================================================
STEP 18 — DRIFT ERROR
============================================================

Create or reuse a structured error for unrecoverable synchronization
failure.

Potential categories:

- ReplaySynchronizationError
- TimelineSynchronizationError
- StateCacheSynchronizationError
- SynchronizationDrift

Use existing Error Protocol conventions.

Do not expose raw implementation exceptions across boundaries.

============================================================
STEP 19 — STEP FORWARD
============================================================

When:

    step_forward()

occurs:

1. ReplayService moves exactly one logical frame.
2. Synchronizer receives the new authoritative position.
3. Runtime state updates.
4. Timeline updates.
5. State Cache updates.
6. synchronization is verified.
7. event is published.

No additional frame may be consumed.

============================================================
STEP 20 — STEP BACKWARD
============================================================

When:

    step_backward()

occurs:

1. ReplayService moves exactly one frame backward.
2. Existing reconstruction is used.
3. Runtime state is rebuilt.
4. Timeline is synchronized.
5. State Cache is synchronized.
6. synchronization is verified.
7. event is published.

Do not attempt to reverse arbitrary state mutations unless the existing
architecture explicitly supports reversible operations.

Reconstruction is preferred.

============================================================
STEP 21 — RESET SYNCHRONIZATION
============================================================

When:

    reset()

occurs:

ReplayService
    ↓
initial replay position
    ↓
reconstructed initial state
    ↓
Timeline reset
    ↓
State Cache reset
    ↓
Runtime state reset
    ↓
synchronization verification

After reset:

    replay_position == timeline_position == cache_position

============================================================
STEP 22 — COMPLETION SYNCHRONIZATION
============================================================

At the end of replay:

- ReplayService = FINISHED
- Timeline = final position
- State Cache = final state
- Runtime = final state

No extra frame should be emitted.

No duplicate completion event.

Synchronization must remain valid after completion.

============================================================
STEP 23 — LOAD SYNCHRONIZATION
============================================================

When a replay is loaded:

1. Load canonical telemetry.
2. Establish initial replay position.
3. Initialize Timeline in REPLAY mode.
4. Initialize Runtime state.
5. Initialize State Cache.
6. Create synchronization snapshot.
7. Verify consistency.
8. Only then expose replay as ready.

Do not report LOADED if the downstream Runtime is still at an old replay
position.

============================================================
STEP 24 — REPLAY SWITCHING
============================================================

If the architecture supports multiple replay sessions:

    Replay A
       ↓
    Replay B

ensure all state from Replay A is cleared/replaced before Replay B becomes
active.

No state may leak between replay sessions.

Verify:

- replay ID
- session ID
- timeline
- State Cache
- Runtime state
- event subscriptions

============================================================
STEP 25 — LIVE / HISTORICAL / REPLAY BOUNDARY
============================================================

Replay synchronization MUST NOT corrupt live Runtime state.

Inspect the existing source/mode architecture.

Ensure:

    LIVE
    HISTORICAL
    REPLAY

remain correctly distinguishable.

If a replay is active, its state must not accidentally be treated as
live telemetry.

Do not alter live telemetry behavior.

============================================================
STEP 26 — COMMAND CONTROLLER INTEGRATION
============================================================

Agent 10.8 already provides:

    ReplayCommandDispatcher
    ReplayApplicationController

Do not bypass them.

The synchronization layer should integrate underneath/alongside
ReplayService so that:

    Command
       ↓
    Controller
       ↓
    ReplayService
       ↓
    Synchronization
       ↓
    Runtime/Timeline/Cache

continues to hold.

Do not make the Controller responsible for synchronization internals.

============================================================
STEP 27 — CONCURRENCY
============================================================

Reuse the existing Agent 10.7 concurrency model.

There must be one synchronization operation at a time for a replay
cursor transition.

Protect against:

- play + seek
- seek + seek
- pause + seek
- reset + play
- stop + seek
- step + seek
- completion + seek

No partially synchronized state may become externally observable.

============================================================
STEP 28 — TRANSACTIONAL STATE UPDATE
============================================================

Where practical, synchronize downstream state as one logical operation:

    authoritative replay position
          ↓
    reconstruct/update Runtime state
          ↓
    update Timeline
          ↓
    update State Cache
          ↓
    verify
          ↓
    publish event

If the existing architecture provides transaction/context mechanisms,
reuse them.

Do not introduce a database transaction for in-memory replay state unless
already appropriate.

============================================================
STEP 29 — SYNCHRONIZATION STATUS
============================================================

Expose a read-only status object.

Conceptually:

    ReplaySynchronizationStatus

containing:

- replay_id
- replay_position_ms
- timeline_position_ms
- state_cache_position_ms
- current_frame
- synchronized
- drift_ms
- synchronization_state
- last_sync_time if appropriate
- last_error if appropriate

Use canonical time representation.

Do not expose internal locks/tasks.

============================================================
STEP 30 — OBSERVABILITY
============================================================

Use existing logging/metrics.

Track:

- synchronization operations
- replay position
- timeline position
- cache position
- drift detected
- drift corrected
- reconstruction count
- backward seek count
- synchronization failures

Do not log every telemetry frame at INFO level.

============================================================
STEP 31 — TESTING
============================================================

Create comprehensive tests.

Use:

    tests/runtime/replay_sync/

or the repository's established test structure.

============================================================
TEST GROUP 1 — POSITION SYNCHRONIZATION
============================================================

Test:

- initial load
- first frame
- forward playback
- pause
- resume
- final frame

Verify:

    replay_position == timeline_position == cache_position

============================================================
TEST GROUP 2 — SEEK
============================================================

Test:

- seek forward
- seek backward
- seek to beginning
- seek to exact frame
- seek to final frame
- seek between frames if supported
- repeated seeks

After every seek verify all state layers agree.

============================================================
TEST GROUP 3 — STATE RECONSTRUCTION
============================================================

Create a fixture where telemetry changes state.

Example:

    frame 1: car A position = 10
    frame 2: car A position = 20
    frame 3: car A position = 30
    frame 4: car A position = 40

Then:

    play → frame 4
    seek → frame 2

Verify:

    car A position == 20

NOT:

    car A position == 40

============================================================
TEST GROUP 4 — STEP
============================================================

Test:

- step forward
- step backward
- beginning boundary
- end boundary
- repeated stepping

Verify synchronization after every operation.

============================================================
TEST GROUP 5 — PAUSE / RESUME
============================================================

Verify:

- pause freezes all state
- resume continues correctly
- no duplicate frame
- no timeline drift
- no cache drift

============================================================
TEST GROUP 6 — RESET
============================================================

Verify:

    FINISHED
       ↓
    RESET
       ↓
    initial position/state

All layers must agree.

============================================================
TEST GROUP 7 — COMPLETION
============================================================

Verify:

- final position
- final state
- final timeline
- final cache
- FINISHED state
- one completion event

============================================================
TEST GROUP 8 — DRIFT DETECTION
============================================================

Intentionally introduce:

    timeline_position != replay_position

Verify drift is detected.

Repeat with:

    cache_position != replay_position

Verify drift is detected.

============================================================
TEST GROUP 9 — DRIFT RECOVERY
============================================================

Where supported:

1. Create drift.
2. Run synchronization.
3. Verify downstream state returns to authoritative replay position.
4. Verify no change to ReplayService cursor.

============================================================
TEST GROUP 10 — UNRECOVERABLE DRIFT
============================================================

Simulate a failure where synchronization cannot safely recover.

Verify:

- structured synchronization error
- no corrupted state
- no false success event
- diagnostic information available

============================================================
TEST GROUP 11 — EVENT ORDERING
============================================================

Verify consumers never observe:

    replay position = T
    cache position = T-1

during a published synchronization event.

Events must occur only after the synchronized state is ready.

============================================================
TEST GROUP 12 — REPLAY SWITCHING
============================================================

If supported:

    load replay A
    advance
    load replay B

Verify no state from A remains in:

- Timeline
- State Cache
- Runtime
- synchronization status

============================================================
TEST GROUP 13 — LIVE REGRESSION
============================================================

Verify synchronization changes do not break live telemetry.

Live tests must remain green.

============================================================
TEST GROUP 14 — DETERMINISM
============================================================

Run the same replay sequence twice:

    load
    play
    pause
    seek
    step
    seek backward
    resume
    complete

Verify identical:

- replay positions
- timeline positions
- State Cache results
- Runtime state
- synchronization statuses
- event ordering

============================================================
STEP 32 — PERFORMANCE
============================================================

Do not create an O(n) full replay reconstruction for every normal
forward frame if the existing architecture can incrementally apply
frames.

Use:

- incremental updates for forward playback
- checkpoint/baseline reconstruction for backward seek

Reuse Agent 10.7's FrameBuffer/reconstruction mechanisms.

Do not introduce unnecessary database access.

Do not introduce Redis or external infrastructure.

============================================================
STEP 33 — DOCUMENTATION
============================================================

Create:

    docs/specifications/ReplaySynchronizationSpecification.md

unless an equivalent specification already exists.

Document:

- synchronization architecture
- authoritative clock/cursor
- timeline synchronization
- Runtime synchronization
- State Cache synchronization
- backward seek reconstruction
- drift detection
- drift recovery
- event ordering
- concurrency
- reset/completion behavior
- live/historical/replay boundaries
- failure behavior
- synchronization tolerance

Update:

    docs/specifications/README.md

Update:

    docs/Replay.md

Update:

    docs/Roadmap.md

Mark Agent 10.9 complete ONLY after all acceptance criteria pass.

============================================================
STEP 34 — CODE QUALITY
============================================================

Follow RaceVision standards:

- Python 3.11
- PEP 8
- type hints
- dependency inversion
- async where appropriate
- deterministic behavior
- no global mutable state
- no circular dependencies
- no duplicated state logic
- no dead code

Use the repository's actual:

- formatter
- linter
- type checker
- test runner
- coverage tooling

Discover commands from:

- pyproject.toml
- Makefile
- scripts
- CI configuration

============================================================
STEP 35 — REGRESSION TESTING
============================================================

Before declaring Agent 10.9 complete, run:

1. FastF1 provider tests
2. Provider tests
3. Normalization tests
4. Validation tests
5. Event Bus tests
6. State Cache tests
7. Synchronization Engine tests
8. Race Timeline tests
9. Phase 10 tests
10. Agent 10.6 tests
11. Agent 10.7 replay tests
12. Agent 10.8 controller tests
13. Agent 10.9 synchronization tests
14. Full relevant project test suite

Confirm:

- historical telemetry works
- Replay Runtime works
- Replay Controller works
- Timeline remains synchronized
- State Cache remains synchronized
- Runtime state remains synchronized
- Event Bus ordering remains correct
- live telemetry remains functional

Fix failures caused by your changes.

============================================================
STEP 36 — ACCEPTANCE CRITERIA
============================================================

Agent 10.9 is COMPLETE only when all are true:

[ ] Replay synchronization layer exists.
[ ] ReplayService remains authoritative for replay position.
[ ] No second replay clock exists.
[ ] No second replay cursor exists.
[ ] No second Timeline exists.
[ ] No second State Cache exists.
[ ] Forward playback remains synchronized.
[ ] Pause remains synchronized.
[ ] Resume remains synchronized.
[ ] Forward seek remains synchronized.
[ ] Backward seek reconstructs correct state.
[ ] Step forward remains synchronized.
[ ] Step backward remains synchronized.
[ ] Reset remains synchronized.
[ ] Completion remains synchronized.
[ ] Replay load initializes all layers consistently.
[ ] TimelineMode.REPLAY is used correctly.
[ ] Runtime state matches replay position.
[ ] State Cache matches replay position.
[ ] Timeline matches replay position.
[ ] Synchronization snapshot/status exists.
[ ] Drift detection exists.
[ ] Drift recovery exists where safe.
[ ] Unrecoverable drift produces structured error.
[ ] Event ordering is deterministic.
[ ] Events are emitted only after synchronization.
[ ] Replay switching does not leak state.
[ ] LIVE/HISTORICAL/REPLAY boundaries remain intact.
[ ] Controller remains above ReplayService.
[ ] No transport-specific logic is added unnecessarily.
[ ] No duplicate reconstruction logic exists.
[ ] No unnecessary persistence/infrastructure is added.
[ ] Deterministic synchronization tests pass.
[ ] Regression tests pass.
[ ] Documentation is updated.
[ ] Roadmap is updated.
[ ] Ruff/type checking/quality gates pass.

============================================================
STEP 37 — FINAL REPORT
============================================================

When complete, report:

1. Files created.
2. Files modified.
3. Synchronization architecture.
4. Authoritative position model.
5. Timeline synchronization.
6. Runtime synchronization.
7. State Cache synchronization.
8. Backward seek reconstruction.
9. Drift detection.
10. Drift recovery.
11. Event ordering.
12. Concurrency behavior.
13. Synchronization status model.
14. Tests added.
15. Test results.
16. Coverage result.
17. Documentation updated.
18. Roadmap status.
19. Known limitations.
20. Recommended Agent 10.10.

Do NOT claim completion if any required test fails.

============================================================
IMPORTANT
============================================================

This is an implementation task.

Do not merely describe the implementation.

Actually inspect and modify the repository.

Build directly on Agents 10.5, 10.6, 10.7 and 10.8.

Do not rewrite working replay architecture.

Do not create a second Runtime.

Do not create a second Timeline.

Do not create a second State Cache.

Do not bypass ReplayService.

Do not bypass ReplayApplicationController.

Do not add REST/WebSocket/Unity UI in this agent.

Do not add unnecessary infrastructure.

The repository is the source of truth.

============================================================
START
============================================================

First inspect the complete implementations and tests for Agents 10.5,
10.6, 10.7 and 10.8.

Then implement Agent 10.9 completely.

Run all relevant tests.

Fix failures.

Update specifications and roadmap.

Only then provide the final implementation report.
```

## User

**Agent 10.9 is complete.** One authoritative ReplayService position; Timeline and State Cache are mirrored projections with drift detection/recovery.

### Architecture

```text
RaceReplay (cursor + ReplayClock)
        ↓
ReplaySynchronizer.push / verify / recover
        ├── Timeline.seek(auth_ms)
        └── Cache reconstruct or runtime stamp
        ↓
ReplaySynchronized (only when aligned)
```

### Created

- `backend/runtime/replay/sync/` — synchronizer, settings, snapshot/status, detection, exceptions
- Protocol: `ReplaySynchronized`, `ReplayDriftDetected`, `ReplaySynchronizationDrift`
- Spec: `ReplaySynchronizationSpecification.md`
- Tests: `tests/runtime/replay_sync/`

### Wired

- `RaceReplay._synchronize` replaces bare timeline seeks (hook after load/apply/seek/step/tick)
- Settings: `synchronization_tolerance_ms=1.0`, `enable_synchronization`, `auto_recover_drift`
- `ReplayService.synchronization_status()`

### Invariants

- Timeline ≈ replay clock (integer ms, **1ms** tolerance)
- Cache `runtime_ms` ≈ **last-applied frame** (not mid-interval clock)
- Recovery never moves the authoritative cursor

### Tests

| Suite                                                                       | Result                                    |
| --------------------------------------------------------------------------- | ----------------------------------------- |
| Replay sync                                                                 | **14 passed**, **\~86%** package coverage |
| Sync + replay + controller + timeline/cache/sync-engine + FastF1 + eventbus | **237 passed**                            |
| Ruff                                                                        | clean                                     |

### Docs / roadmap

Roadmap **10.9 ✓**; specs README + `docs/Replay.md` updated

### Limitations / Agent 10.10

No transport layer yet. Sync stamp path updates session `runtime_ms` only (full vehicle reconstruction still via Agent 10.7 seek reconstruct).
**Recommended 10.10:** Replay transport / presentation (REST/WebSocket adapter over `ReplayCommandDispatcher`).

## Assistant

Excellent. **Agent 10.9 is accepted as complete.**

The important architectural decision here is correct: **ReplayService remains the single source of temporal truth**, while Timeline and State Cache are projections.

### Phase 10 status

| Agent | Component | Status |
|---|---|---|
| 10.0 | Race Session Domain | ✅ |
| 10.1 | Session Manager | ✅ |
| 10.2 | Race Event & Weekend Manager | ✅ |
| 10.3 | Track Session Manager | ✅ |
| 10.4 | Driver & Car Runtime Registry | ✅ |
| 10.5 | Race Timeline Engine | ✅ |
| 10.6 | Historical Telemetry Provider | ✅ |
| 10.7 | Replay Runtime Core | ✅ |
| 10.8 | Replay Controller | ✅ |
| **10.9** | **Replay Synchronization** | **✅** |

### Current replay architecture

```text
                 Historical Telemetry
                         │
                         ▼
                  FastF1 Provider
                         │
                         ▼
                  Canonical Frames
                         │
                         ▼
                 ┌───────────────┐
                 │ ReplayService │
                 │               │
                 │ Replay Clock  │
                 │ Replay Cursor │
                 │ Frame Buffer  │
                 └───────┬───────┘
                         │
                AUTHORITATIVE TIME
                         │
                         ▼
                ReplaySynchronizer
                  ┌──────┼──────┐
                  │      │      │
                  ▼      ▼      ▼
              Timeline Runtime Cache
                  │      │      │
                  └──────┼──────┘
                         ▼
                 ReplaySynchronized
```

The **1 ms synchronization tolerance** is also clearly defined rather than allowing arbitrary drift.

One particularly important detail is the distinction you've established:

```text
Replay Clock
     │
     └── authoritative playback position

Last Applied Frame
     │
     └── authoritative reconstructed state position
```

That prevents the State Cache from being incorrectly interpreted as having a fully reconstructed state at an arbitrary point between telemetry frames.

### The next architectural boundary

I agree with the proposed **Agent 10.10**.

At this point the backend has:

```text
10.6  Historical Telemetry
10.7  Replay Runtime
10.8  Replay Control
10.9  Replay Synchronization
```

So the next natural layer is:

```text
                 Replay Controller
                        │
                        ▼
              ReplayCommandDispatcher
                        │
                        ▼
              ┌─────────────────────┐
              │     Agent 10.10     │
              │  Replay Transport   │
              └──────────┬──────────┘
                         │
                  ┌──────┴──────┐
                  ▼             ▼
                HTTP        WebSocket
```

And critically:

```text
HTTP / WebSocket
       ↓
ReplayCommandDispatcher
       ↓
ReplayApplicationController
       ↓
ReplayService
```

**Not** directly into `ReplayService`.

That gives us a clean foundation for the later Unity/3D presentation layer without contaminating the replay domain with transport concerns.

**Agent 10.9 = accepted.** memcite

## User

Please give commands for Agent 10.10	Replay State Cache	Replay-specific state/snapshots/indexes ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. **Agent 10.10 should build the replay-specific state/snapshot/index layer on top of the existing State Cache**, without replacing it or creating a second general-purpose cache.

Copy/paste the entire block into Cursor:

```text
You are the Principal Distributed Systems Architect and Senior Python Engineer working on the RaceVision project.

============================================================
RACEVISION — AGENT 10.10
REPLAY STATE CACHE
============================================================

OBJECTIVE
---------

Implement Agent 10.10 — Replay State Cache.

The purpose of this agent is to provide replay-specific state management,
snapshots, checkpoints, and indexes that make historical replay seeking,
scrubbing, stepping, reconstruction, and synchronization efficient and
deterministic.

Agent 10.7 already provides:

- Replay Runtime Core
- Replay Clock
- Replay Cursor
- FrameBuffer
- Replay reconstruction
- seek
- step_forward
- step_backward

Agent 10.8 provides:

- Replay Controller
- ReplayApplicationController
- ReplayCommandDispatcher

Agent 10.9 provides:

- ReplaySynchronization
- Timeline synchronization
- State Cache synchronization
- drift detection
- drift recovery

Agent 10.10 must now introduce a dedicated REPLAY STATE CACHE layer.

IMPORTANT:

This is NOT a replacement for the existing State Cache.

The architecture must remain:

    ReplayService
         │
         ▼
    Replay State Cache
         │
         ├── Snapshots
         ├── Checkpoints
         ├── Frame indexes
         └── State reconstruction acceleration
         │
         ▼
    Existing Runtime State Cache
         │
         ▼
    Timeline / Runtime / Event Bus

The Replay State Cache is replay-specific infrastructure.

Do NOT create a second generic Runtime State Cache.

============================================================
STEP 0 — READ THE REPOSITORY FIRST
============================================================

Before modifying anything, inspect the actual repository.

Read:

- docs/Roadmap.md
- docs/Replay.md
- docs/specifications/README.md
- docs/specifications/SoftwareRequirementsSpecification.md
- docs/specifications/SystemArchitectureSpecification.md
- docs/specifications/DatabaseDesignSpecification.md
- docs/specifications/RaceTimelineEngineSpecification.md
- docs/specifications/HistoricalTelemetryProviderSpecification.md
- docs/specifications/ReplayRuntimeCoreSpecification.md
- docs/specifications/ReplayControllerSpecification.md
- docs/specifications/ReplaySynchronizationSpecification.md
- docs/specifications/LiveStateCacheSpecification.md
- docs/specifications/LiveSynchronizationEngineSpecification.md

Inspect:

- backend/runtime/replay/
- backend/runtime/replay/control/
- backend/runtime/replay/sync/
- ReplayService
- ReplayManager
- ReplayEngine
- ReplayClock
- FrameBuffer
- reconstruction
- existing State Cache
- Runtime State
- Timeline
- Event Bus
- telemetry models
- replay protocol
- repository/database abstractions
- existing snapshot/checkpoint/index implementations
- existing caching abstractions
- Phase 10.7 tests
- Phase 10.8 tests
- Phase 10.9 tests

Search the repository for:

- snapshot
- checkpoint
- cache
- index
- frame_index
- timestamp_index
- reconstruction
- seek
- replay
- state
- runtime_ms

Do not assume filenames.

The repository is the source of truth.

============================================================
STEP 1 — ARCHITECTURAL RESPONSIBILITY
============================================================

The Replay State Cache is responsible for:

- storing replay-specific reconstructed state snapshots
- locating the nearest snapshot for a target timestamp
- indexing telemetry frames by timestamp
- accelerating replay seeks
- supporting deterministic reconstruction
- providing snapshot metadata
- invalidating/rebuilding replay state when necessary
- preventing state leakage between replay sessions

It is NOT responsible for:

- owning the ReplayClock
- owning the authoritative replay cursor
- controlling play/pause/resume
- controlling the Replay lifecycle
- replacing ReplayService
- replacing Runtime State Cache
- replacing Timeline
- loading FastF1 data
- normalizing telemetry
- publishing transport responses

The authoritative replay position remains owned by ReplayService.

============================================================
STEP 2 — TARGET ARCHITECTURE
============================================================

Implement:

    ReplayService
         │
         ▼
    ReplayStateCache
         │
         ├── FrameIndex
         │
         ├── SnapshotIndex
         │
         ├── StateSnapshotStore
         │
         └── CheckpointManager
         │
         ▼
    Reconstruction Engine
         │
         ▼
    Existing Runtime State Cache
         │
         ▼
    ReplaySynchronizer
         │
         ├── Timeline
         └── Runtime State

Do not duplicate existing abstractions.

If equivalent components already exist, extend/reuse them.

============================================================
STEP 3 — REPLAY STATE CACHE CONTRACT
============================================================

Create a clean abstraction.

Use repository naming conventions.

Conceptually:

    ReplayStateCache

with operations equivalent to:

    initialize(...)
    clear(...)
    get(...)
    put(...)
    contains(...)
    nearest_snapshot(...)
    snapshot_at(...)
    create_snapshot(...)
    restore_snapshot(...)
    invalidate(...)
    rebuild(...)
    get_status(...)

Do NOT blindly implement every method if equivalent repository APIs exist.

Keep the public API small.

============================================================
STEP 4 — STATE SNAPSHOT
============================================================

Create an immutable replay state snapshot model.

Conceptually:

    ReplayStateSnapshot

Possible fields:

- replay_id
- session_id
- timestamp_ms
- frame_index
- sequence_number
- timeline_mode
- state_version
- created_at
- state payload/reference
- checksum/hash if appropriate

Use existing domain identifiers and timestamp types.

Do not store unnecessary duplicate telemetry.

The snapshot must represent a complete deterministic state required to
continue reconstruction from that point.

============================================================
STEP 5 — SNAPSHOT CONTENT
============================================================

Inspect the existing Runtime state model.

Determine exactly what state must be captured to reconstruct a replay.

Potential state includes:

- driver state
- car state
- vehicle position
- orientation
- velocity
- lap state
- sector state
- race position
- pit state
- tyre state where available
- session state
- race event state
- weather state if represented
- timing state
- other canonical runtime state

Do NOT invent fields that do not exist in the project.

A snapshot must contain the project's canonical reconstructed state or a
safe immutable representation/reference to it.

Do not serialize arbitrary Python objects.

============================================================
STEP 6 — IMMUTABILITY
============================================================

Snapshots must be immutable once published.

Avoid:

    snapshot.state["car"] = ...

after creation.

Use immutable models/value objects where consistent with the project.

If the existing architecture uses frozen Pydantic/dataclass models, reuse it.

The goal is:

    snapshot(T)
        ↓
    never changes

This is essential for deterministic replay.

============================================================
STEP 7 — FRAME INDEX
============================================================

Implement or reuse a frame index.

The frame index should efficiently answer:

    timestamp → frame index

and:

    target timestamp → nearest frame <= target

Support:

- first frame
- last frame
- exact timestamp
- nearest preceding frame
- nearest following frame if useful
- frame count
- timestamp bounds

Do not scan the entire frame buffer for every seek if an indexed structure
can be used.

Use binary search or the repository's equivalent efficient index.

============================================================
STEP 8 — SNAPSHOT INDEX
============================================================

Implement a snapshot index.

It must efficiently answer:

    target timestamp
        ↓
    nearest snapshot <= target

Example:

    snapshots:
        0s
        10s
        20s
        30s
        40s

Seek:

    27s

should locate:

    20s

then replay frames:

    20s → 27s

Do not reconstruct from the beginning unless no suitable snapshot exists.

============================================================
STEP 9 — CHECKPOINT POLICY
============================================================

Implement a deterministic checkpoint policy.

Inspect existing configuration before adding new settings.

Possible configuration:

    snapshot_interval_ms

or:

    snapshot_interval_frames

Choose the model that best matches the existing telemetry/replay design.

Do not hard-code arbitrary values without documenting them.

If the repository already has checkpoint configuration, reuse it.

The policy must be deterministic.

Given the same replay data and configuration, the same snapshot timestamps
must be generated.

============================================================
STEP 10 — INITIAL SNAPSHOT
============================================================

Every loaded replay should have a valid baseline state.

At minimum:

    snapshot at first valid replay state

This ensures reconstruction has a deterministic starting point.

The baseline must correspond to the initial replay frame/state.

============================================================
STEP 11 — SNAPSHOT CREATION
============================================================

During forward replay:

    frame applied
        ↓
    checkpoint policy
        ↓
    create snapshot if required

Snapshots must be created AFTER the state represented by that timestamp
has been successfully applied.

Never create a snapshot claiming:

    T = 30s

while the stored state is actually:

    T = 29s

============================================================
STEP 12 — SNAPSHOT RESTORATION
============================================================

When seeking:

    target = 75s

perform:

    locate nearest snapshot <= 75s
             ↓
    restore snapshot
             ↓
    replay frames after snapshot
             ↓
    target state

Reuse Agent 10.7 reconstruction mechanisms.

Do NOT create a second reconstruction algorithm.

The Replay State Cache should accelerate reconstruction, not replace the
existing reconstruction semantics.

============================================================
STEP 13 — BACKWARD SEEK
============================================================

Backward seek must use snapshots/checkpoints when available.

Example:

    current = 300s
    target = 120s

Do:

    snapshot <= 120s
         ↓
    restore
         ↓
    apply frames to 120s
         ↓
    synchronized Runtime State

Do NOT attempt to reverse state mutations.

Do NOT leave any state from 300s.

============================================================
STEP 14 — FORWARD SEEK
============================================================

Forward seeks should also use the nearest suitable checkpoint where this
improves performance.

Example:

    current = 100s
    target = 180s

The implementation may either:

- incrementally advance from the current state when safe
- restore an appropriate checkpoint

Use the strategy consistent with Agent 10.7.

Correctness comes before optimization.

============================================================
STEP 15 — STEP OPERATIONS
============================================================

Step operations must remain deterministic.

For:

    step_forward()

and:

    step_backward()

the Replay State Cache may be used to accelerate backward reconstruction.

Do not alter the semantics of Agent 10.7.

One step must remain exactly one logical replay frame.

============================================================
STEP 16 — CACHE KEY DESIGN
============================================================

Define stable cache identity.

At minimum, cache identity must prevent state from different replays
being mixed.

Conceptually:

    replay_id + frame_index

or:

    replay_id + timestamp + state_version

Use the repository's canonical identifiers.

Do NOT key snapshots only by timestamp.

Two different replays may both contain:

    timestamp = 10000ms

and they must never collide.

============================================================
STEP 17 — SESSION ISOLATION
============================================================

Replay A:

    replay_id = A

Replay B:

    replay_id = B

Snapshots and indexes from A MUST NEVER be used for B.

Test:

    load A
    create snapshots
    load B
    seek B

Verify B does not restore A state.

============================================================
STEP 18 — CACHE LIFECYCLE
============================================================

Implement clear lifecycle semantics.

Expected:

    create
       ↓
    initialize
       ↓
    populate
       ↓
    use
       ↓
    invalidate / clear
       ↓
    dispose

When replay changes:

- old snapshots must not leak
- old frame indexes must not leak
- old state references must not leak

Reuse existing lifecycle conventions.

============================================================
STEP 19 — MEMORY MANAGEMENT
============================================================

The Replay State Cache must be bounded.

Do not create an unbounded in-memory snapshot store.

Inspect existing configuration and cache patterns.

Possible controls:

- max snapshots
- max memory
- snapshot interval
- retention policy

Use the smallest appropriate mechanism.

If eviction is needed, use a deterministic policy such as LRU only if
consistent with the architecture.

Do not introduce unnecessary complexity.

============================================================
STEP 20 — SNAPSHOT EVICTION
============================================================

If snapshots are evicted:

- never evict the mandatory baseline snapshot unless another valid
  reconstruction baseline exists
- ensure nearest-snapshot lookup remains correct
- reconstruction must still work after eviction

Test cache pressure.

============================================================
STEP 21 — PERSISTENCE DECISION
============================================================

Inspect the project database architecture before deciding whether replay
snapshots should be persisted.

Do NOT automatically create PostgreSQL tables.

Agent 10.10 should remain primarily a runtime replay-state cache unless
the existing architecture explicitly requires persistence.

If persistence is required by existing specifications:

- use existing repository/UoW/database patterns
- do not create direct SQL inside Replay State Cache
- add proper migration
- preserve tenant/version/soft-delete conventions where applicable

If persistence is NOT required, keep the implementation in-memory and
document that decision.

============================================================
STEP 22 — HASH / CHECKSUM
============================================================

If the architecture already uses state hashes/checksums, integrate them.

A deterministic snapshot checksum can help detect corruption/drift.

Do not introduce cryptographic hashing merely for performance.

If implemented, the checksum must be deterministic.

Same state:

    same snapshot hash

============================================================
STEP 23 — VERSIONING
============================================================

Snapshots should have a state version or schema version if the project
already uses versioning.

This prevents incompatible state snapshots from being silently restored.

Example:

    state_version = 1

If a future schema changes, incompatible snapshots can be rejected.

Reuse existing versioning conventions.

============================================================
STEP 24 — REPLAY SYNCHRONIZATION INTEGRATION
============================================================

Agent 10.9 currently provides:

    ReplaySynchronizer

The new Replay State Cache must integrate with it.

Target:

    ReplayService
        ↓
    ReplayStateCache
        ↓
    reconstructed state
        ↓
    ReplaySynchronizer
        ├── Timeline
        ├── Runtime
        └── Existing State Cache

The synchronizer remains responsible for alignment verification.

Replay State Cache is responsible for efficient replay-state restoration.

Do not merge the two responsibilities.

============================================================
STEP 25 — STATE CACHE INTEGRATION
============================================================

There are now two distinct concepts:

    ReplayStateCache
        =
    replay-specific snapshots/checkpoints/indexes

and:

    Runtime State Cache
        =
    current authoritative application/runtime projection

Do not confuse them.

After restoring a ReplayStateSnapshot:

    ReplayStateCache.restore(...)
            ↓
    reconstructed runtime state
            ↓
    Runtime State Cache update
            ↓
    ReplaySynchronizer.verify()

============================================================
STEP 26 — TIMELINE INTEGRATION
============================================================

Timeline remains a projection.

After reconstruction:

    target timestamp
        ↓
    ReplayStateCache restore/replay
        ↓
    Runtime state
        ↓
    ReplaySynchronizer
        ↓
    Timeline.seek(target)

Do not let ReplayStateCache modify Timeline directly unless the existing
synchronization abstraction requires it.

============================================================
STEP 27 — EVENT BUS
============================================================

Do not create a second Event Bus.

Use existing events.

Potential events include:

- ReplaySnapshotCreated
- ReplaySnapshotRestored
- ReplayCacheInvalidated
- ReplayCacheRebuilt

Only add events where consumers genuinely need them.

Events must be emitted after the operation succeeds.

Do not emit:

    ReplaySnapshotRestored

before restoration has actually completed.

============================================================
STEP 28 — PROTOCOL BOUNDARY
============================================================

Replay State Cache is an internal runtime component.

Do not expose its internal structures through REST/WebSocket protocols.

Future transport layers should ask for replay status/position through the
Replay Controller.

Do not add transport endpoints in Agent 10.10.

============================================================
STEP 29 — THREAD SAFETY / CONCURRENCY
============================================================

Use the existing replay concurrency strategy.

Ensure that:

- snapshot creation
- snapshot restoration
- cache invalidation
- replay seek
- step backward
- replay switching

cannot produce inconsistent state.

Avoid holding locks during expensive operations if the existing architecture
supports safe snapshotting outside locks.

There must remain one authoritative replay cursor.

============================================================
STEP 30 — ATOMIC RESTORE
============================================================

Snapshot restoration should behave atomically from the perspective of
Replay Runtime consumers.

Avoid exposing:

    half-restored state

For example, consumers must not observe:

    Driver state = 20s
    Car state = 60s
    Timeline = 60s

during a restoration operation.

Use the existing synchronization/transaction abstractions where available.

============================================================
STEP 31 — RECONSTRUCTION PERFORMANCE
============================================================

Measure/verify the improvement.

Compare:

    seek without snapshot
        vs
    seek using nearest snapshot

The goal is to reduce the number of frames that must be replayed.

Expose useful diagnostics such as:

- snapshot used
- snapshot timestamp
- target timestamp
- frames replayed after snapshot
- reconstruction duration if appropriate

Do not add expensive instrumentation to every normal frame unless already
supported.

============================================================
STEP 32 — CACHE STATUS
============================================================

Expose a read-only status model.

Conceptually:

    ReplayStateCacheStatus

containing:

- replay_id
- snapshot_count
- frame_index_size
- earliest_snapshot_ms
- latest_snapshot_ms
- baseline_available
- cache_hits
- cache_misses
- snapshot_restores
- invalidations
- evictions if applicable
- current_state_version
- memory estimate if safely available

Do not expose mutable internal collections.

============================================================
STEP 33 — CACHE STATISTICS
============================================================

Provide useful statistics:

- snapshot hits
- snapshot misses
- restore count
- reconstruction count
- frames replayed from checkpoint
- cache invalidations
- eviction count
- average/last restore duration if already supported by project metrics

Do not introduce unnecessary monitoring infrastructure.

Use existing metrics/logging conventions.

============================================================
STEP 34 — ERROR HANDLING
============================================================

Handle:

- snapshot not found
- invalid snapshot
- incompatible snapshot version
- corrupt snapshot
- replay mismatch
- session mismatch
- cache unavailable
- reconstruction failure
- state restoration failure
- index failure

Use structured domain/application errors.

Do not expose raw implementation exceptions to callers.

Possible existing/new error concepts:

- ReplaySnapshotNotFound
- ReplaySnapshotInvalid
- ReplaySnapshotVersionMismatch
- ReplayCacheError
- ReplayStateRestoreError

Reuse existing Error Protocol conventions where applicable.

============================================================
STEP 35 — DETERMINISM
============================================================

The Replay State Cache must never change replay semantics.

Given identical:

- telemetry
- configuration
- snapshot policy
- replay commands

the resulting state MUST be identical.

Verify:

    replay without snapshots
        ==
    replay with snapshots

for the same target timestamps.

Snapshots are an optimization, not an alternate simulation.

============================================================
STEP 36 — TEST FIXTURES
============================================================

Create deterministic replay fixtures.

Example:

    frame 0:
        car A position = 0

    frame 1:
        car A position = 10

    frame 2:
        car A position = 20

    frame 3:
        car A position = 30

    frame 4:
        car A position = 40

Create snapshots at deterministic intervals.

Use these fixtures for:

- exact restore
- backward seek
- forward seek
- step backward
- reset
- cache invalidation
- replay switching

============================================================
STEP 37 — TESTING
============================================================

Create:

    tests/runtime/replay_state_cache/

or use the repository's existing test structure.

============================================================
TEST GROUP 1 — CACHE LIFECYCLE
============================================================

Test:

- initialize
- clear
- dispose
- reinitialize
- replay switching

============================================================
TEST GROUP 2 — SNAPSHOT CREATION
============================================================

Test:

- baseline snapshot
- periodic snapshots
- exact timestamp
- frame index association
- deterministic snapshot content
- immutable snapshots

============================================================
TEST GROUP 3 — SNAPSHOT INDEX
============================================================

Test:

- exact match
- nearest preceding snapshot
- beginning
- end
- target between checkpoints
- no snapshot available

============================================================
TEST GROUP 4 — FRAME INDEX
============================================================

Test:

- exact frame lookup
- preceding frame
- following frame
- boundaries
- empty index
- duplicate timestamp handling according to project semantics

============================================================
TEST GROUP 5 — RESTORATION
============================================================

Test:

    snapshot at 20s
    restore 20s

Verify exact state.

============================================================
TEST GROUP 6 — RECONSTRUCTION
============================================================

Test:

    snapshot at 20s
    target 27s

Verify:

    snapshot restored
    frames 21..27 applied
    resulting state == direct reconstruction

============================================================
TEST GROUP 7 — BACKWARD SEEK
============================================================

Test:

    replay to 60s
    seek to 20s

Verify:

- correct state
- no 60s state leakage
- correct timeline
- correct Runtime State Cache
- synchronization remains valid

============================================================
TEST GROUP 8 — FORWARD SEEK
============================================================

Test:

    current 20s
    seek 80s

Verify correct state and synchronization.

============================================================
TEST GROUP 9 — STEP BACKWARD
============================================================

Test repeated backward steps.

Verify every resulting state exactly matches direct reconstruction.

============================================================
TEST GROUP 10 — RESET
============================================================

Verify:

    reset
        ↓
    baseline snapshot
        ↓
    initial state

============================================================
TEST GROUP 11 — REPLAY ISOLATION
============================================================

Create:

    Replay A
    Replay B

Populate A snapshots.

Load B.

Verify A snapshots cannot be returned for B.

============================================================
TEST GROUP 12 — INVALIDATION
============================================================

Test:

- explicit invalidation
- replay replacement
- session replacement
- state version change

Verify stale snapshots cannot be restored.

============================================================
TEST GROUP 13 — MEMORY / EVICTION
============================================================

If bounded eviction is implemented:

- exceed configured limit
- verify deterministic eviction
- verify baseline remains available
- verify reconstruction still works

============================================================
TEST GROUP 14 — DETERMINISM
============================================================

Perform identical replay sequences:

Sequence A:

    load
    play
    seek
    step
    seek backward
    reset

Sequence B:

    same operations

Verify identical state.

============================================================
TEST GROUP 15 — SNAPSHOT VS FULL RECONSTRUCTION
============================================================

For a range of timestamps:

    direct reconstruction
        ==
    checkpoint reconstruction

This is a critical acceptance test.

============================================================
TEST GROUP 16 — SYNCHRONIZATION
============================================================

After every restore verify:

    replay position
        ≈
    Runtime State Cache position
        ≈
    Timeline position

using Agent 10.9's synchronization tolerance.

============================================================
TEST GROUP 17 — CONCURRENCY
============================================================

Test:

- seek + seek
- seek + step backward
- reset + seek
- replay switching + seek

No corrupted snapshots or partially restored state.

============================================================
TEST GROUP 18 — REGRESSION
============================================================

Run:

- Agent 10.6 tests
- Agent 10.7 tests
- Agent 10.8 tests
- Agent 10.9 tests
- Timeline tests
- State Cache tests
- Synchronization tests
- Event Bus tests
- Provider tests
- full relevant Phase 10 tests

============================================================
STEP 38 — PERFORMANCE ACCEPTANCE
============================================================

Measure a representative seek.

The snapshot implementation should demonstrate that checkpoint-based
seeking reduces reconstruction work for sufficiently distant seeks.

Do not require an arbitrary performance percentage.

Report:

- number of frames reconstructed without checkpoint
- number with checkpoint
- snapshot lookup time
- restore time if measurable

Correctness remains the primary requirement.

============================================================
STEP 39 — DOCUMENTATION
============================================================

Create:

    docs/specifications/ReplayStateCacheSpecification.md

unless an equivalent specification already exists.

Document:

- purpose
- architecture
- snapshot model
- checkpoint policy
- frame index
- snapshot index
- restoration
- reconstruction
- cache lifecycle
- session isolation
- memory limits
- persistence decision
- invalidation
- determinism
- synchronization integration
- error handling
- performance characteristics

Update:

    docs/specifications/README.md

Update:

    docs/Replay.md

Update:

    docs/Roadmap.md

Mark Agent 10.10 complete ONLY after all acceptance criteria pass.

============================================================
STEP 40 — DATABASE / PERSISTENCE RULE
============================================================

Do NOT add PostgreSQL persistence simply because the project has PostgreSQL.

First inspect existing architecture.

If replay snapshots are intended to be runtime-only:

    keep them runtime/in-memory

and explicitly document:

    Replay State Cache is an acceleration layer;
    canonical telemetry remains the source for deterministic reconstruction.

If persistent replay snapshots are already required by the specifications,
implement them through:

    Repository
        ↓
    UnitOfWork
        ↓
    existing PostgreSQL infrastructure

Never:

- create raw database connections
- create raw SQL in runtime cache
- bypass repositories
- introduce a parallel persistence layer

============================================================
STEP 41 — CODE QUALITY
============================================================

Follow RaceVision standards:

- Python 3.11
- PEP 8
- type hints
- dependency inversion
- immutable value objects where appropriate
- deterministic behavior
- no global mutable state
- no circular imports
- no duplicate reconstruction logic
- no dead code

Use the repository's actual:

- formatter
- linter
- type checker
- test runner
- coverage tooling

Discover commands from:

- pyproject.toml
- Makefile
- scripts
- CI configuration

============================================================
STEP 42 — ARCHITECTURAL GUARDRAILS
============================================================

DO NOT:

- create a second ReplayService
- create a second ReplayClock
- create a second ReplayCursor
- create a second Runtime State Cache
- create a second Timeline
- create a second Event Bus
- bypass ReplayService
- bypass ReplaySynchronizer
- bypass ReplayApplicationController
- call FastF1 directly
- duplicate telemetry normalization
- duplicate replay reconstruction algorithms
- create REST endpoints
- create WebSocket endpoints
- create Unity UI
- create OBS integration
- add Redis
- add unnecessary external infrastructure

The Replay State Cache is an INTERNAL replay acceleration component.

============================================================
STEP 43 — ACCEPTANCE CRITERIA
============================================================

Agent 10.10 is COMPLETE only when all are true:

[ ] ReplayStateCache exists.
[ ] It is distinct from Runtime State Cache by responsibility.
[ ] ReplayService remains authoritative for replay time.
[ ] No second replay clock exists.
[ ] No second replay cursor exists.
[ ] Immutable ReplayStateSnapshot exists.
[ ] Baseline snapshot exists.
[ ] Snapshot index exists.
[ ] Frame index exists or existing index is reused.
[ ] Nearest checkpoint lookup works.
[ ] Backward seek uses checkpoint reconstruction.
[ ] Forward seek works correctly.
[ ] Step backward works correctly.
[ ] Reset works correctly.
[ ] Replay/session isolation exists.
[ ] Snapshot invalidation exists.
[ ] State versioning is handled where appropriate.
[ ] Memory is bounded or explicitly justified.
[ ] Snapshot creation is deterministic.
[ ] Snapshot restoration is deterministic.
[ ] Snapshot reconstruction matches full reconstruction.
[ ] Runtime State Cache remains the current application projection.
[ ] Timeline remains a synchronized projection.
[ ] ReplaySynchronizer remains responsible for alignment.
[ ] No stale replay state leaks between sessions.
[ ] Structured errors exist.
[ ] Cache status exists.
[ ] Cache statistics exist where appropriate.
[ ] Event Bus integration follows existing conventions.
[ ] No transport layer is introduced.
[ ] No unnecessary database persistence is introduced.
[ ] Agent 10.7 semantics remain unchanged.
[ ] Agent 10.8 controller remains unchanged in responsibility.
[ ] Agent 10.9 synchronization remains valid.
[ ] Determinism tests pass.
[ ] Regression tests pass.
[ ] Documentation is updated.
[ ] Roadmap is updated.
[ ] Ruff/type checking/quality gates pass.

============================================================
STEP 44 — FINAL REPORT
============================================================

When complete, report:

1. Files created.
2. Files modified.
3. Replay State Cache architecture.
4. Snapshot model.
5. Frame index.
6. Snapshot index.
7. Checkpoint policy.
8. Restoration/reconstruction strategy.
9. Cache lifecycle.
10. Session isolation.
11. Memory/eviction strategy.
12. Persistence decision.
13. Synchronization integration.
14. Cache status/statistics.
15. Error handling.
16. Performance comparison.
17. Tests added.
18. Test results.
19. Coverage result.
20. Documentation updated.
21. Roadmap status.
22. Known limitations.
23. Recommended Agent 10.11.

Do NOT claim completion if any required test fails.

============================================================
IMPORTANT
============================================================

This is an implementation task.

Do not merely describe the implementation.

Actually inspect and modify the repository.

Build directly on Agents 10.6, 10.7, 10.8 and 10.9.

The existing implementation is the source of truth.

Preserve working architecture.

Replay State Cache is an optimization and deterministic state restoration
layer — NOT a new runtime.

============================================================
START
============================================================

First inspect the complete implementations and tests for:

- Agent 10.6 Historical Telemetry Provider
- Agent 10.7 Replay Runtime Core
- Agent 10.8 Replay Controller
- Agent 10.9 Replay Synchronization
- existing Runtime State Cache
- existing Timeline
- existing reconstruction system

Then implement Agent 10.10 completely.

Run all relevant tests.

Fix all failures caused by your changes.

Update specifications and roadmap.

Only then provide the final implementation report.
```

## User

**Agent 10.10 Replay State Cache is complete.** All 62 Phase 10.7–10.10 regression tests passed; state\_cache coverage \~84%; ruff clean.

### 1. Files created

- `backend/runtime/replay/state_cache/` — `__init__.py`, `replay_state_cache.py`, `snapshot.py`, `snapshot_index.py`, `frame_index.py`, `policy.py`, `status.py`, `exceptions.py`
- `docs/specifications/ReplayStateCacheSpecification.md`
- `tests/runtime/replay_state_cache/` — `conftest.py`, `test_replay_state_cache.py`

### 2. Files modified

- `replay_engine.py`, `replay_service.py`, `replay_manager.py`, `configuration.py`, `replay/__init__.py`
- Protocol: `shared/protocols/events/replay/messages.py`, `__init__.py`, `catalogue.py`
- Docs: `Replay.md`, `Roadmap.md`, `specifications/README.md`, `ReplayRuntimeCoreSpecification.md`

### 3–8. Architecture / model / indexes / policy / restore

```text
ReplayService → RaceReplay → ReplayStateCache
  ├── FrameIndex (FrameBuffer binary search)
  ├── SnapshotIndex (baseline + checkpoints)
  ├── CheckpointPolicy (every_n_frames, max_snapshots)
  └── ReplayStateSnapshot → reconstruct_to_index → Live Cache → ReplaySynchronizer
```

Immutable `ReplayStateSnapshot` wraps Live `CacheSnapshot` payload with `replay_id` + `frame_index`. Checkpoint after apply when `(index+1) % N == 0`. Seek/step still use Agent 10.7 `reconstruct_to_index` — cache only materials/ingests snapshots.

### 9–12. Lifecycle / isolation / memory / persistence

Initialize on load → baseline → checkpoints → clear on replay switch. Keys include `replay_id` (no cross-session restore). Bounded by `max_replay_snapshots` (default 256); baseline never evicted. **In-memory only** — no PostgreSQL.

### 13–15. Sync / status / errors

Synchronizer still owns alignment. Status via `state_cache_status()`. Errors: `ReplayStateCacheError`, snapshot not found/invalid/mismatch, restore failure. Events: `ReplaySnapshotCreated|Restored`, `ReplayCacheInvalidated`.

### 16. Performance

With `snapshot_every=2`, seek to frame 19 plans fewer frames than full reconstruct (`frames_to_replay < frames_without_checkpoint`). Correctness first.

### 17–19. Tests / results / coverage

- Suite: lifecycle, indexes, restore==full reconstruct, backward/forward seek, step, reset, isolation, eviction, sync, determinism, concurrency under manager lock, catalogue
- **62 passed** (10.7–10.10)
- **\~84%** package coverage

### 20–21. Docs / roadmap

Spec + README + Replay.md updated. Roadmap: **10.10 checked**; **10.11+** transport/presentation.

### 22. Limitations

Cooperative single-threaded replay; concurrent seeks need manager lock. No snapshot checksum crypto. Persistence deferred by design.

### 23. Recommended Agent 10.11

Replay **transport** (REST/WebSocket status/commands) over `ReplayApplicationController` — do not expose internal Replay State Cache structures.

## Assistant

Excellent. **Agent 10.10 is accepted as complete.**

The implementation preserves the important separation we established:

```text
Historical Telemetry
        ↓
ReplayService
        ↓
RaceReplay
        ↓
ReplayStateCache
   ├── FrameIndex
   ├── SnapshotIndex
   ├── CheckpointPolicy
   └── ReplayStateSnapshot
        ↓
Agent 10.7 Reconstruction
        ↓
Live/Runtime State Cache
        ↓
ReplaySynchronizer
        ↓
Timeline
```

### Phase 10 status

| Agent | Component | Status |
|---|---|---|
| 10.0 | Race Session Domain | ✅ |
| 10.1 | Session Manager | ✅ |
| 10.2 | Race Event & Weekend Manager | ✅ |
| 10.3 | Track Session Manager | ✅ |
| 10.4 | Driver & Car Runtime Registry | ✅ |
| 10.5 | Race Timeline Engine | ✅ |
| 10.6 | Historical Telemetry Provider | ✅ |
| 10.7 | Replay Runtime Core | ✅ |
| 10.8 | Replay Controller | ✅ |
| 10.9 | Replay Synchronization | ✅ |
| **10.10** | **Replay State Cache** | **✅** |

### Particularly good architectural decisions

**1. Cache does not become authoritative**

`ReplayService` remains the source of replay position. The cache is strictly an acceleration/state-restoration layer.

**2. Reconstruction semantics were not duplicated**

This is important:

```text
ReplayStateCache
      ↓
materials/ingests snapshots
      ↓
Agent 10.7 reconstruct_to_index()
```

Rather than creating a competing reconstruction engine.

**3. Session isolation**

Including `replay_id` in the snapshot identity prevents replay A's state from accidentally being restored into replay B.

**4. Baseline protection**

The baseline snapshot being non-evictable is the right choice for a bounded in-memory cache.

**5. Persistence deferred**

Keeping this in-memory is appropriate at this stage. PostgreSQL remains the canonical persistence layer for durable telemetry/recordings rather than turning the replay acceleration cache into another persistence subsystem.

**6. Synchronization boundary remains clean**

```text
ReplayStateCache
      ↓
state reconstruction
      ↓
ReplaySynchronizer
      ↓
Timeline / Runtime / Cache
```

So 10.10 hasn't polluted the synchronization responsibility from 10.9.

### Current replay stack

You now have a very solid chain:

```text
10.6  Historical Telemetry Provider
          ↓
10.7  Replay Runtime Core
          ↓
10.8  Replay Controller
          ↓
10.9  Replay Synchronization
          ↓
10.10 Replay State Cache
```

And the test result is strong:

**62 regression tests passed across 10.7–10.10, ~84% state-cache coverage, Ruff clean.**

### Agent 10.11

I agree with the proposed next step:

> **10.11 — Replay Transport**

The boundary should be:

```text
                    REST
                     │
                     ▼
              ┌───────────────┐
              │ Replay        │
              │ Transport     │
              └───────┬───────┘
                      │
                   WebSocket
                      │
                      ▼
          ReplayCommandDispatcher
                      │
                      ▼
       ReplayApplicationController
                      │
                      ▼
                ReplayService
                      │
             ┌────────┴────────┐
             ▼                 ▼
       State Cache         Synchronizer
```

The transport should expose **commands, status, lifecycle and replay events**, but **not expose `ReplayStateCache` internals**.

That keeps 10.10 reusable later by Unity, the web frontend, OBS overlays, chat control, and other presentation clients.

**Agent 10.10 = accepted.** memcite

## User

Please give commands for Agent 10.11	Replay Bookmark & Event System	Bookmarks, overtakes, incidents, laps, sectors ( 1 click copy and paste cursor friendly)

## Assistant

Yes. **Agent 10.11 should build the replay annotation/event layer on top of the existing replay stack**, while keeping telemetry, Runtime state, Timeline, and Replay State Cache separate.

Copy/paste this entire block into Cursor:

```text
You are the Principal Distributed Systems Architect and Senior Python Engineer working on the RaceVision project.

============================================================
RACEVISION — AGENT 10.11
REPLAY BOOKMARK & EVENT SYSTEM
============================================================

OBJECTIVE
---------

Implement Agent 10.11 — Replay Bookmark & Event System.

The purpose of this agent is to add a deterministic replay annotation
and event layer supporting:

- user bookmarks
- lap events
- sector events
- overtakes
- incidents
- pit events where supported
- race/session events relevant to replay
- event indexing
- timestamp/frame lookup
- replay event querying
- bookmark management
- event navigation

This layer must work with the existing replay architecture created by
Agents 10.6–10.10.

============================================================
EXISTING ARCHITECTURE — DO NOT BREAK
============================================================

The current replay architecture is:

    Historical Telemetry Provider
              │
              ▼
       Replay Runtime Core
              │
              ▼
       Replay Controller
              │
              ▼
       Replay Synchronization
              │
              ▼
       Replay State Cache
              │
              ▼
       Runtime State / Timeline / Event Bus

Agent 10.11 adds:

              Replay Runtime
                    │
                    ▼
          Replay Event System
             ┌──────┼──────┐
             │      │      │
             ▼      ▼      ▼
        Bookmarks  Events  Indexes
             │      │      │
             └──────┼──────┘
                    ▼
              Replay Queries
                    │
                    ▼
          Future Transport/UI

IMPORTANT:

Do NOT create:

- a second ReplayService
- a second ReplayClock
- a second ReplayCursor
- a second Timeline
- a second Runtime
- a second State Cache
- a second Event Bus
- a second telemetry pipeline
- a second normalization pipeline
- a second reconstruction engine

Replay events are metadata/annotations associated with the canonical
replay timeline.

============================================================
STEP 0 — READ THE REPOSITORY FIRST
============================================================

Before making changes, inspect the actual repository.

Read:

- docs/Roadmap.md
- docs/Replay.md
- docs/specifications/README.md
- docs/specifications/SoftwareRequirementsSpecification.md
- docs/specifications/SystemArchitectureSpecification.md
- docs/specifications/DatabaseDesignSpecification.md
- docs/specifications/RaceTimelineEngineSpecification.md
- docs/specifications/HistoricalTelemetryProviderSpecification.md
- docs/specifications/ReplayRuntimeCoreSpecification.md
- docs/specifications/ReplayControllerSpecification.md
- docs/specifications/ReplaySynchronizationSpecification.md
- docs/specifications/ReplayStateCacheSpecification.md
- docs/specifications/LiveStateCacheSpecification.md
- docs/specifications/LiveSynchronizationEngineSpecification.md

Inspect:

- backend/runtime/replay/
- backend/runtime/replay/control/
- backend/runtime/replay/sync/
- backend/runtime/replay/state_cache/
- backend/runtime/
- existing RaceEvent models
- existing Lap models
- existing Sector models
- existing ReplayBookmark models
- existing CameraEvent models
- existing Event Bus
- shared protocol events
- event catalogue
- database models/repositories
- telemetry models
- runtime state models
- Timeline implementation
- existing statistics/event detection code
- Agent 10.7–10.10 tests

Search the repository for:

- Bookmark
- ReplayBookmark
- RaceEvent
- RaceEventType
- overtaking
- overtake
- incident
- lap
- sector
- pit
- event
- annotation
- marker
- timestamp
- frame_index
- replay_event

Do NOT assume that any model is missing until the repository has been
inspected.

The repository is the source of truth.

============================================================
STEP 1 — DEFINE RESPONSIBILITIES
============================================================

Agent 10.11 is responsible for replay-specific event and annotation
management.

It must support:

1. Bookmark creation.
2. Bookmark update.
3. Bookmark deletion.
4. Bookmark lookup.
5. Bookmark navigation.
6. Automatic replay event registration.
7. Event indexing.
8. Event lookup by timestamp.
9. Event lookup by frame.
10. Event filtering.
11. Lap markers.
12. Sector markers.
13. Overtake markers.
14. Incident markers.
15. Pit/event markers where existing data supports them.
16. Event ordering.
17. Replay/session isolation.
18. Deterministic event identity.
19. Event lifecycle.
20. Event publication through the existing Event Bus where appropriate.

It must NOT become responsible for replay playback.

============================================================
STEP 2 — IMPORTANT DISTINCTION
============================================================

There are three different concepts:

    TELEMETRY
        ↓
    Raw/canonical measurements

    RUNTIME STATE
        ↓
    Current reconstructed application state

    REPLAY EVENTS / BOOKMARKS
        ↓
    Metadata and annotations attached to the replay timeline

Do not mix these.

Example:

Telemetry:

    car A position = X

Runtime state:

    car A currently at X

Replay event:

    car A overtook car B at T

Bookmark:

    user marked T as "Amazing overtake"

These are different concepts.

============================================================
STEP 3 — REUSE EXISTING DOMAIN MODELS
============================================================

Inspect existing models first.

The repository already contains or may contain:

- ReplayBookmark
- RaceEvent
- Lap
- Sector
- CameraEvent

If suitable existing models exist, extend/reuse them.

Do NOT create duplicate models such as:

    ReplayLap
    ReplaySector
    ReplayRaceEvent

unless the architecture clearly requires a replay-specific projection.

Prefer:

    existing domain event
          +
    replay reference/metadata

rather than duplicate domain concepts.

============================================================
STEP 4 — REPLAY EVENT MODEL
============================================================

Create or extend a canonical replay event representation.

Conceptually:

    ReplayEvent

Possible fields:

- event_id
- replay_id
- session_id
- event_type
- timestamp_ms
- frame_index
- sequence_number
- driver_id
- secondary_driver_id
- team_id where appropriate
- lap_number
- sector_number
- severity
- source
- title
- description
- metadata
- created_at
- updated_at

Use existing identifiers and enums.

Do NOT invent identifiers if the project already has canonical ones.

============================================================
STEP 5 — EVENT TYPES
============================================================

Inspect existing event enums first.

Support the following concepts where the repository supports them:

    LAP_COMPLETED
    SECTOR_COMPLETED
    OVERTAKE
    INCIDENT
    PIT_ENTRY
    PIT_EXIT
    SAFETY_CAR
    RED_FLAG
    YELLOW_FLAG
    VIRTUAL_SAFETY_CAR
    PENALTY
    RETIREMENT
    SESSION_START
    SESSION_END

Do not add every event blindly.

Only add event types that fit the existing domain/specification.

User bookmarks are separate:

    BOOKMARK

A bookmark is an annotation, not necessarily a race event.

============================================================
STEP 6 — EVENT SOURCE
============================================================

Every event should identify its source where appropriate.

Possible sources:

    TELEMETRY
    DERIVED
    USER
    SYSTEM
    HISTORICAL
    REPLAY

Use existing project terminology if available.

Examples:

    OVERTAKE
        source = DERIVED

    USER BOOKMARK
        source = USER

    LAP_COMPLETED
        source = TELEMETRY or DERIVED

Do not hard-code a new source taxonomy if an existing one exists.

============================================================
STEP 7 — EVENT CONFIDENCE
============================================================

If an event is derived rather than directly supplied by the source,
support confidence/provenance where appropriate.

For example:

    confidence
    detection_method
    source_provider

Do not invent AI-based confidence.

A deterministic derived event should remain deterministic.

============================================================
STEP 8 — EVENT IDENTITY
============================================================

Event identity must be deterministic where possible.

Avoid generating random duplicate events every time a replay is loaded.

For automatically derived events, consider identity based on:

    replay_id
    event_type
    frame_index/timestamp
    primary entity
    secondary entity
    sequence

Use the project's UUID conventions where required.

User-created bookmarks may use normal UUID identity.

============================================================
STEP 9 — EVENT STORE
============================================================

Create a replay event store/service using existing architecture.

Possible structure:

    backend/runtime/replay/events/

with:

    replay_event.py
    event_store.py
    event_index.py
    event_detector.py
    bookmark_service.py
    status.py
    exceptions.py

Use equivalent existing structures if they already exist.

Keep the implementation modular.

============================================================
STEP 10 — EVENT INDEX
============================================================

Create an efficient event index.

Support:

    timestamp → events

    frame_index → events

    event_type → events

    driver_id → events

    lap_number → events

The primary navigation operation must be efficient:

    next_event(after_timestamp)
    previous_event(before_timestamp)

Do not scan every event for every replay navigation operation.

Use sorted indexes/binary search where appropriate.

============================================================
STEP 11 — BOOKMARK MODEL
============================================================

Create or extend ReplayBookmark.

A bookmark should support at minimum:

- bookmark_id
- replay_id
- session_id
- timestamp_ms
- frame_index
- title
- description
- category/tag
- driver_id optional
- created_by
- created_at
- updated_at
- metadata

Use existing audit fields where available.

Bookmarks must be immutable in identity but editable in annotation content.

============================================================
STEP 12 — BOOKMARK OPERATIONS
============================================================

Provide operations equivalent to:

    create_bookmark(...)
    get_bookmark(...)
    list_bookmarks(...)
    update_bookmark(...)
    delete_bookmark(...)
    next_bookmark(...)
    previous_bookmark(...)
    clear_bookmarks(...)

Do not expose mutable internal collections.

Return immutable/read-only result objects where appropriate.

============================================================
STEP 13 — BOOKMARK AT CURRENT POSITION
============================================================

Support creating a bookmark at the current replay position.

Conceptually:

    bookmark_current_position()

The service should obtain the authoritative position from ReplayService.

Do NOT create another replay cursor.

Example:

    ReplayService position = 125430ms

    create bookmark

    bookmark.timestamp_ms = 125430

If a current frame exists, associate its frame index.

============================================================
STEP 14 — BOOKMARK NAVIGATION
============================================================

Support:

    next bookmark
    previous bookmark

The navigation result should identify:

- timestamp
- frame index
- bookmark ID
- title
- description

Do NOT automatically seek ReplayService unless the existing controller
semantics explicitly require navigation commands to seek.

Keep lookup separate from playback control unless the architecture
already defines combined navigation.

============================================================
STEP 15 — LAP EVENTS
============================================================

Inspect existing Lap model/runtime logic.

Do NOT create duplicate lap state.

Expose replay events representing lap boundaries:

    LAP_COMPLETED

with:

- driver
- lap number
- timestamp
- frame
- relevant timing metadata

If lap completion events already exist, reuse them.

============================================================
STEP 16 — SECTOR EVENTS
============================================================

Support:

    SECTOR_COMPLETED

with:

- driver
- lap
- sector
- timestamp
- frame
- sector time where available

Do not calculate sector timing independently if canonical timing already
exists.

Use existing telemetry/domain calculations.

============================================================
STEP 17 — OVERTAKE EVENTS
============================================================

Implement deterministic overtake detection only if sufficient telemetry
exists.

An overtake event should conceptually contain:

    attacker
    defender
    timestamp
    frame
    position_before
    position_after
    lap
    source/detection_method

Do NOT claim a physical on-track overtake merely because numeric positions
change.

Inspect the existing position/ranking data.

Use the safest deterministic rule supported by available data.

Example concept:

    previous ordering:
        A ahead of B

    new ordering:
        B ahead of A

    sustained ordering / validation
        ↓
    OVERTAKE

Avoid emitting duplicate events on every frame while the order remains
changed.

============================================================
STEP 18 — OVERTAKE DEDUPLICATION
============================================================

Overtake detection must be edge-triggered.

Bad:

    frame 100 → overtake
    frame 101 → overtake
    frame 102 → overtake

Good:

    frame 100 → overtake
    frame 101 → no event
    frame 102 → no event

until another valid position transition occurs.

Use deterministic event identity.

============================================================
STEP 19 — INCIDENT EVENTS
============================================================

Inspect available telemetry and event signals.

Only detect incidents that can be justified from available data.

Potential signals:

- collision indication
- sudden position change
- abnormal velocity change
- off-track state
- damage flag
- retirement
- telemetry event

Do NOT infer a collision purely from:

    speed changed

unless the project already defines such a detector.

If reliable incident telemetry is unavailable, create the event model and
detector interface but do not fabricate incident events.

============================================================
STEP 20 — INCIDENT SEVERITY
============================================================

If incidents are supported, use a clear severity model such as the
existing project enum.

Potential levels:

    INFO
    WARNING
    CRITICAL

Do not invent severity semantics if existing domain models already define
them.

============================================================
STEP 21 — PIT EVENTS
============================================================

If pit entry/exit information exists, expose:

    PIT_ENTRY
    PIT_EXIT

Use canonical telemetry/session data.

Do not create a second pit-state machine.

============================================================
STEP 22 — EVENT DETECTOR ARCHITECTURE
============================================================

Create a detector abstraction.

Conceptually:

    BaseReplayEventDetector

Implement separate detectors where appropriate:

    LapEventDetector
    SectorEventDetector
    OvertakeEventDetector
    IncidentEventDetector
    PitEventDetector

Do not implement one giant conditional function.

Only implement detectors supported by available project data.

============================================================
STEP 23 — DETECTOR INPUT
============================================================

Detectors should consume canonical/runtime state or canonical frames.

Do NOT call FastF1 directly from event detectors.

Architecture:

    FastF1
       ↓
    Provider
       ↓
    Canonical Telemetry
       ↓
    Replay Runtime
       ↓
    Event Detector

Not:

    Event Detector → FastF1

============================================================
STEP 24 — EVENT GENERATION TIMING
============================================================

Determine whether events are:

    PRECOMPUTED
    LAZY
    INCREMENTAL

Prefer a design compatible with the existing replay lifecycle.

For replay playback:

    frame applied
       ↓
    event detection
       ↓
    event registration
       ↓
    event publication

For seeking:

    reconstructed state
       ↓
    event index/query

Do not duplicate events simply because a replay was seeked backward.

============================================================
STEP 25 — SEEK BEHAVIOR
============================================================

When seeking backward:

    60s → 20s

the event system must not create duplicate events.

Events are timeline metadata.

They should be queryable independently of the current replay cursor.

If events are lazily generated, use deterministic deduplication.

============================================================
STEP 26 — EVENT REPLAYING
============================================================

If the existing Event Bus supports replay event publication, distinguish:

    event exists at timestamp T

from:

    event is being emitted because playback crossed T

This distinction is critical.

An event may exist in the Replay Event Store without being emitted every
time a seek crosses it.

If playback moves:

    10s → 20s

emit events crossed by the playback interval if the existing architecture
requires playback event emission.

If seeking:

    60s → 20s

do NOT automatically re-emit every historical event unless explicitly
defined.

============================================================
STEP 27 — EVENT CROSSING
============================================================

Provide a query such as:

    events_between(start_ms, end_ms)

This allows the replay engine/controller to determine:

    which events occurred while playback advanced

Support:

- inclusive/exclusive boundaries
- forward direction
- deterministic ordering

Document boundary semantics.

============================================================
STEP 28 — EVENT ORDERING
============================================================

Events at the same timestamp must have deterministic ordering.

Use a stable ordering such as:

    timestamp
    frame_index
    event_type
    sequence_number
    event_id

Do not rely on dictionary insertion order.

============================================================
STEP 29 — REPLAY SESSION ISOLATION
============================================================

Events and bookmarks MUST be isolated by:

    replay_id

and, where appropriate:

    session_id

Test:

    Replay A
       events/bookmarks

    Replay B
       events/bookmarks

No cross-replay leakage.

============================================================
STEP 30 — LIFECYCLE
============================================================

On replay load:

    initialize event store/index

On replay switch:

    clear old replay event state

On replay reset:

    events/bookmarks remain timeline metadata unless existing semantics
    explicitly require clearing runtime-generated annotations

Important distinction:

    RESET PLAYBACK POSITION

must NOT automatically mean:

    DELETE USER BOOKMARKS

unless explicitly commanded.

============================================================
STEP 31 — USER VS DERIVED EVENTS
============================================================

Clearly distinguish:

    USER BOOKMARK

from:

    DERIVED EVENT

User bookmarks:

- editable
- deletable
- user-owned

Derived events:

- generated from telemetry/runtime
- deterministic
- normally read-only

Do not allow accidental mutation of derived event definitions through
bookmark APIs.

============================================================
STEP 32 — TAGS / CATEGORIES
============================================================

Support bookmark categorization if compatible with the existing domain.

Examples:

    overtaking
    incident
    strategy
    camera
    interesting
    replay_review

Do not hard-code a restrictive list unless requirements already define it.

A simple string/category enum is acceptable according to existing patterns.

============================================================
STEP 33 — CAMERA INTEGRATION PREPARATION
============================================================

Do not implement camera control in Agent 10.11.

However, event/bookmark metadata should be usable later by the camera
system.

For example:

    bookmark.metadata["camera_hint"]

may be supported only if the existing metadata conventions allow it.

Do not import Unity/OBS code.

============================================================
STEP 34 — DATABASE / PERSISTENCE
============================================================

Inspect existing database models.

The repository already contains:

    ReplayBookmark
    RaceEvent
    Lap
    Sector
    CameraEvent

Determine which should be persisted and which should remain runtime-only.

IMPORTANT:

Do NOT create duplicate tables if equivalent models already exist.

If ReplayBookmark persistence already exists:

- reuse the model
- reuse Repository
- reuse UnitOfWork

If RaceEvent/Lap/Sector already persist canonical data:

- reference them
- do not duplicate them into replay-specific tables unless required

If runtime-derived replay events need persistence and the architecture
requires it, use the existing PostgreSQL architecture.

Never:

- use raw SQL from replay runtime
- create direct DB connections
- bypass Repository/UoW
- create a second persistence framework

If persistence is not currently required, keep derived indexes runtime-only
and document that decision.

============================================================
STEP 35 — EVENT STORE VS DATABASE
============================================================

Keep the distinction:

    Canonical persisted events
        ↓
    Database/domain layer

    Replay Event Index
        ↓
    Runtime acceleration/query layer

Do not treat the in-memory event index as the source of truth if the
canonical event exists in the database/domain model.

============================================================
STEP 36 — STATUS
============================================================

Expose read-only status.

Conceptually:

    ReplayEventSystemStatus

containing:

- replay_id
- event_count
- bookmark_count
- event_types
- earliest_event_ms
- latest_event_ms
- detector_count
- indexed
- generated
- generation_status

Do not expose internal mutable collections.

============================================================
STEP 37 — STATISTICS
============================================================

Provide useful statistics:

- events by type
- bookmarks by category
- overtake count
- incident count
- lap event count
- sector event count
- pit event count

Use existing statistics abstractions where possible.

============================================================
STEP 38 — ERROR HANDLING
============================================================

Handle:

- replay not loaded
- event not found
- bookmark not found
- invalid bookmark
- invalid event
- replay mismatch
- duplicate event
- unsupported detector
- detector failure
- event indexing failure

Use structured project errors.

Potential concepts:

    ReplayEventError
    ReplayBookmarkError
    ReplayEventNotFound
    ReplayBookmarkNotFound
    ReplayEventDuplicate
    ReplayEventDetectionError

Reuse existing error hierarchy where possible.

============================================================
STEP 39 — PROTOCOL EVENTS
============================================================

Inspect:

    shared/protocols/events/replay/

Add protocol messages only when required.

Potential events:

    ReplayBookmarkCreated
    ReplayBookmarkUpdated
    ReplayBookmarkDeleted
    ReplayEventDetected
    ReplayEventPublished

Do not duplicate existing protocol events.

Update:

    catalogue.py
    __init__.py

if required.

Protocol events must contain serializable payloads.

Do not expose internal detector/cache objects.

============================================================
STEP 40 — CONTROLLER INTEGRATION
============================================================

Agent 10.8 provides:

    ReplayApplicationController
    ReplayCommandDispatcher

Do not bypass them.

If bookmark/event commands are appropriate at this layer, expose thin
controller operations such as:

    create_bookmark
    update_bookmark
    delete_bookmark
    list_bookmarks
    get_events
    next_event
    previous_event

The Controller should delegate to the Replay Event System.

Do not move event detection logic into the Controller.

============================================================
STEP 41 — REPLAY STATE CACHE INTEGRATION
============================================================

Agent 10.10 provides:

    ReplayStateCache

Do not store bookmarks/events inside ReplayStateSnapshot.

Snapshots represent runtime state.

Events/bookmarks represent replay timeline metadata.

They must remain separate.

============================================================
STEP 42 — TIMELINE INTEGRATION
============================================================

The Timeline remains authoritative only as the timeline projection.

Replay events should be indexed by canonical replay timestamps/frame indexes.

When querying:

    events_at_current_position()

use ReplayService's authoritative position.

Do not create another timeline cursor.

============================================================
STEP 43 — SYNCHRONIZATION INTEGRATION
============================================================

Agent 10.9 owns:

    ReplaySynchronizer

Do not move synchronization responsibility into the event system.

The event system may observe:

    replay position
    current frame

but does not own them.

============================================================
STEP 44 — EVENT BUS INTEGRATION
============================================================

Use the existing Event Bus.

Potential flow:

    Replay frame applied
          ↓
    detector
          ↓
    Replay Event Store
          ↓
    Event Bus

Only publish after successful registration.

Do not publish duplicate events on repeated reconstruction.

============================================================
STEP 45 — DETERMINISM
============================================================

Event generation must be deterministic.

Given identical:

- canonical telemetry
- replay configuration
- detector configuration

the event set must be identical.

Run the same replay twice.

Verify identical:

- event IDs where deterministic IDs are used
- timestamps
- event types
- participants
- ordering

============================================================
STEP 46 — TESTING
============================================================

Create:

    tests/runtime/replay_events/

or use the repository's existing test structure.

============================================================
TEST GROUP 1 — BOOKMARK CRUD
============================================================

Test:

- create
- read
- update
- delete
- list
- clear

============================================================
TEST GROUP 2 — BOOKMARK POSITION
============================================================

Test:

    bookmark_current_position()

Verify:

- authoritative replay timestamp
- frame index
- replay ID
- session ID

============================================================
TEST GROUP 3 — BOOKMARK NAVIGATION
============================================================

Test:

- next bookmark
- previous bookmark
- first bookmark
- last bookmark
- no bookmark

============================================================
TEST GROUP 4 — EVENT INDEX
============================================================

Test:

- timestamp lookup
- frame lookup
- event type filtering
- driver filtering
- events_between
- next event
- previous event

============================================================
TEST GROUP 5 — LAP EVENTS
============================================================

Verify deterministic lap completion events.

============================================================
TEST GROUP 6 — SECTOR EVENTS
============================================================

Verify deterministic sector events.

============================================================
TEST GROUP 7 — OVERTAKE DETECTION
============================================================

Create deterministic position/order fixtures.

Verify:

    A ahead of B
       ↓
    B ahead of A
       ↓
    exactly one OVERTAKE

Then verify no duplicate events across subsequent frames.

============================================================
TEST GROUP 8 — INCIDENT DETECTION
============================================================

Only test signals actually supported by the repository.

Verify:

- valid incident generated
- unsupported ambiguous telemetry does not generate false incident

============================================================
TEST GROUP 9 — PIT EVENTS
============================================================

If supported, verify:

- pit entry
- pit exit
- no duplicate events

============================================================
TEST GROUP 10 — EVENT ORDERING
============================================================

Create multiple events at the same timestamp.

Verify deterministic ordering.

============================================================
TEST GROUP 11 — SEEK
============================================================

Test:

    play → 60s
    seek → 20s

Verify:

- event index remains unchanged
- no duplicate event creation
- queries still return correct events

============================================================
TEST GROUP 12 — REPLAY SWITCHING
============================================================

Create:

    Replay A
    Replay B

Verify no event/bookmark leakage.

============================================================
TEST GROUP 13 — RESET
============================================================

Verify:

    reset()

does NOT delete user bookmarks unless explicitly specified.

Derived event metadata must remain deterministic.

============================================================
TEST GROUP 14 — EVENT CROSSING
============================================================

Test:

    events_between(10s, 20s)

Verify exact boundary semantics.

Test forward playback crossing:

    10s → 20s

Verify events are emitted exactly once if playback-event emission is
enabled.

============================================================
TEST GROUP 15 — BACKWARD SEEK
============================================================

Test:

    60s → 20s

Verify no historical events are incorrectly duplicated.

============================================================
TEST GROUP 16 — CONTROLLER
============================================================

Test Controller delegation:

    Controller
       ↓
    Event System

Verify the Controller does not contain event detection logic.

============================================================
TEST GROUP 17 — EVENT BUS
============================================================

Verify:

- successful event publication
- bookmark event publication
- no publication on failed operation
- no duplicate publication

============================================================
TEST GROUP 18 — STATE CACHE SEPARATION
============================================================

Verify ReplayStateSnapshot does NOT contain bookmark/event metadata.

Verify event system does NOT mutate ReplayStateCache snapshots.

============================================================
TEST GROUP 19 — DETERMINISM
============================================================

Run event generation twice over the same canonical frames.

Verify identical results.

============================================================
TEST GROUP 20 — REGRESSION
============================================================

Run:

- Agent 10.6 tests
- Agent 10.7 tests
- Agent 10.8 tests
- Agent 10.9 tests
- Agent 10.10 tests
- Timeline tests
- State Cache tests
- Synchronization tests
- Event Bus tests
- Provider tests
- database/repository tests affected by changes
- full relevant Phase 10 suite

============================================================
STEP 47 — PERFORMANCE
============================================================

Event queries must not require scanning every telemetry frame.

Indexes should make:

    next event
    previous event
    events_between
    events by type

efficient.

Do not over-optimize event detection prematurely.

Correctness first.

============================================================
STEP 48 — DOCUMENTATION
============================================================

Create:

    docs/specifications/ReplayBookmarkEventSystemSpecification.md

unless an equivalent specification already exists.

Document:

- architecture
- event model
- bookmark model
- event types
- event sources
- event detectors
- overtake detection
- incident detection
- lap/sector events
- event indexing
- bookmark navigation
- event crossing
- deduplication
- persistence decisions
- Event Bus behavior
- replay/session isolation
- determinism
- error handling

Update:

    docs/specifications/README.md

Update:

    docs/Replay.md

Update:

    docs/Roadmap.md

Mark Agent 10.11 complete ONLY after all acceptance criteria pass.

============================================================
STEP 49 — CODE QUALITY
============================================================

Follow RaceVision standards:

- Python 3.11
- PEP 8
- type hints
- dependency inversion
- deterministic behavior
- immutable event/snapshot value objects
- no global mutable state
- no circular dependencies
- no duplicated domain logic
- no dead code

Use repository-standard:

- formatter
- Ruff
- type checker
- test runner
- coverage

Discover exact commands from:

- pyproject.toml
- Makefile
- scripts
- CI configuration

============================================================
STEP 50 — ARCHITECTURAL GUARDRAILS
============================================================

DO NOT:

- create a second ReplayService
- create a second ReplayClock
- create a second ReplayCursor
- create a second Timeline
- create a second Runtime State Cache
- create a second Event Bus
- create a second telemetry pipeline
- create a second normalization pipeline
- create a second reconstruction engine
- call FastF1 directly
- bypass ReplayApplicationController
- bypass ReplaySynchronizer
- store events in ReplayStateSnapshot
- store bookmarks in ReplayStateSnapshot
- create REST endpoints
- create WebSocket endpoints
- create Unity UI
- create OBS integration
- create camera-control logic
- add Redis
- add unnecessary infrastructure

============================================================
STEP 51 — ACCEPTANCE CRITERIA
============================================================

Agent 10.11 is COMPLETE only when all applicable requirements are true:

[ ] Replay Event System exists.
[ ] Replay Bookmark system exists.
[ ] Existing ReplayBookmark model is reused/extended where appropriate.
[ ] Existing RaceEvent/Lap/Sector models are reused where appropriate.
[ ] Event model has deterministic replay/session identity.
[ ] Event indexing exists.
[ ] Timestamp lookup works.
[ ] Frame lookup works.
[ ] events_between works.
[ ] next_event works.
[ ] previous_event works.
[ ] Bookmark CRUD works.
[ ] Bookmark-at-current-position works.
[ ] Bookmark navigation works.
[ ] Lap events are supported where canonical data exists.
[ ] Sector events are supported where canonical data exists.
[ ] Overtake detection is deterministic where data permits.
[ ] Overtake events are deduplicated.
[ ] Incident detection is only used where data supports it.
[ ] Pit events are supported where canonical data exists.
[ ] Event ordering is deterministic.
[ ] Event identity prevents duplicate derived events.
[ ] Replay/session isolation exists.
[ ] Reset does not unexpectedly delete bookmarks.
[ ] Backward seek does not duplicate events.
[ ] Event crossing semantics are documented.
[ ] Event Bus integration is correct.
[ ] Controller integration is thin.
[ ] Replay State Cache remains separate.
[ ] Replay Synchronizer remains responsible for synchronization.
[ ] Timeline remains a projection.
[ ] ReplayService remains authoritative for position.
[ ] Derived event generation is deterministic.
[ ] User and derived events are clearly separated.
[ ] Structured errors exist.
[ ] Status exists.
[ ] Relevant statistics exist.
[ ] Persistence follows existing database architecture.
[ ] No duplicate database models/tables are created unnecessarily.
[ ] No transport layer is added.
[ ] No Unity/OBS/camera logic is added.
[ ] Agent 10.7 semantics remain unchanged.
[ ] Agent 10.8 semantics remain unchanged.
[ ] Agent 10.9 synchronization remains valid.
[ ] Agent 10.10 cache remains valid.
[ ] New tests pass.
[ ] Regression tests pass.
[ ] Documentation is updated.
[ ] Roadmap is updated.
[ ] Ruff/type checking/quality gates pass.

============================================================
STEP 52 — FINAL REPORT
============================================================

When complete, report:

1. Files created.
2. Files modified.
3. Replay Event System architecture.
4. Bookmark architecture.
5. Event model.
6. Event types implemented.
7. Event source/provenance.
8. Event indexes.
9. Bookmark navigation.
10. Lap/sector handling.
11. Overtake detection.
12. Incident detection.
13. Pit event handling.
14. Event deduplication.
15. Event crossing behavior.
16. Event Bus integration.
17. Controller integration.
18. Database/persistence decision.
19. Replay/session isolation.
20. Determinism guarantees.
21. Tests added.
22. Test results.
23. Coverage result.
24. Ruff/type-check results.
25. Documentation updated.
26. Roadmap status.
27. Known limitations.
28. Recommended Agent 10.12.

Do NOT claim completion if required tests fail.

============================================================
IMPORTANT
============================================================

This is an implementation task.

Do not merely describe the implementation.

Actually inspect and modify the repository.

Build directly on Agents 10.6, 10.7, 10.8, 10.9 and 10.10.

Preserve the existing architecture.

Do not rewrite working replay functionality.

The repository is the source of truth.

============================================================
START
============================================================

First inspect the complete implementations and tests for:

- Agent 10.6 Historical Telemetry Provider
- Agent 10.7 Replay Runtime Core
- Agent 10.8 Replay Controller
- Agent 10.9 Replay Synchronization
- Agent 10.10 Replay State Cache
- existing ReplayBookmark
- existing RaceEvent
- existing Lap
- existing Sector
- existing CameraEvent
- existing Event Bus
- existing database/repository layer

Then implement Agent 10.11 completely.

Run all relevant tests.

Fix failures caused by your changes.

Update specifications and roadmap.

Only then provide the final implementation report.
```

## User

**Agent 10.11 complete.** 77 Phase 10.7–10.11 tests passed; event\_system coverage \~83%; ruff clean.

### 1–2. Files

**Created:** `backend/runtime/replay/event_system/` (models, enums, store, index, bookmark store, detectors, façade, status, exceptions), `docs/specifications/ReplayBookmarkEventSystemSpecification.md`, `tests/runtime/replay_events/`

**Modified:** `replay_engine.py`, `configuration.py`, `replay_service/manager`, `control/*`, protocol events/commands/catalogue, `docs/Replay.md`, `Roadmap.md`, specs README

### 3–9. Architecture

Package is `event_system/` (avoids clash with emit helper `events.py`).

```text
RaceReplay → ReplayEventSystem
  ├── BookmarkStore (USER CRUD + navigation)
  ├── EventStore + EventIndex (timestamp/frame/type/driver)
  └── Detectors → precompute on load
```

Immutable `ReplayEvent` / `ReplayBookmark`. Types: BOOKMARK, LAP/SECTOR\_COMPLETED, OVERTAKE, INCIDENT, PIT\_ENTRY/EXIT. Sources: USER / TELEMETRY / DERIVED / …. Indexes support `events_between`, `next/previous_event`. Bookmark-at-current-position uses authoritative cursor.

### 10–15. Detectors / crossing

Lap/sector: edge on number change. Overtake: edge-triggered `race_order` swap (deduped). Incident: explicit flags only. Pit: `in_pit` edges. Precompute + skip re-detect when indexed ⇒ seeks don’t duplicate. Playback emits `(last, current]`; seek/reset only resync.

### 16–20. Integration

Protocol: enriched `ReplayBookmarkCreated`, + Updated/Deleted, `ReplayEventDetected`. Controller thin CRUD/jump; `CreateBookmark` / `JumpToBookmark` dispatched. **In-memory only** (your choice). Isolation by `replay_id`. Reset keeps user bookmarks. Deterministic derived IDs.

### 21–26. Quality / docs

Tests cover CRUD, nav, lap/sector/overtake/pit/incident, seek, isolation, controller, separation, determinism. **77 passed**. Roadmap: **10.11 checked**; **10.12+** transport.

### 27–28. Limitations / next

ORM `ReplayBookmark` / `RaceEvent` not yet wired. Multi-car order needs `race_order` (or per-frame positions). Recommend **Agent 10.12 — Replay transport** (REST/WS over controller; optional bookmark persistence via existing repos).

## Assistant

Excellent. **Agent 10.11 is accepted as complete.**

The implementation is consistent with the architecture we've built through 10.10, and the important boundary decisions are correct.

### Phase 10 replay stack

| Agent | Component | Status |
|---|---|---|
| 10.6 | Historical Telemetry Provider | ✅ |
| 10.7 | Replay Runtime Core | ✅ |
| 10.8 | Replay Controller | ✅ |
| 10.9 | Replay Synchronization | ✅ |
| 10.10 | Replay State Cache | ✅ |
| **10.11** | **Replay Bookmark & Event System** | **✅** |

### Current architecture

```text
Historical Telemetry
        │
        ▼
   ReplayService
        │
        ▼
    RaceReplay
        │
   ┌────┼──────────────────┐
   │    │                  │
   ▼    ▼                  ▼
Replay  Replay          Replay Event
Clock   State Cache     System
   │                       │
   │              ┌────────┼────────┐
   │              ▼        ▼        ▼
   │          Bookmarks  Events  Detectors
   │                         │
   │               ┌─────────┼─────────┐
   │               ▼         ▼         ▼
   │             Lap/      Overtake  Incident
   │             Sector
   │
   ▼
Replay Synchronizer
   │
   ▼
Timeline / Runtime State
```

### What 10.11 now gives us

The replay system can now answer things such as:

```text
What happened at 01:23:456?
        ↓
events_at(timestamp)

What happened between 10:00 and 12:00?
        ↓
events_between()

What is the next event?
        ↓
next_event()

Where was the previous overtake?
        ↓
previous_event(OVERTAKE)

Take me to the next bookmark
        ↓
next_bookmark()

Bookmark the current replay position
        ↓
bookmark_current_position()
```

And importantly, the **event system is not another playback engine**.

### The precomputation decision is particularly good

```text
Replay loaded
     ↓
Detect events once
     ↓
EventStore
     ↓
EventIndex
```

Then:

```text
seek backward
     ↓
NO re-detection
     ↓
NO duplicate events
```

That is exactly what we want for deterministic replay.

The `(last, current]` playback crossing semantics are also a good foundation for future live replay overlays, commentary, camera triggers and event notifications.

### One important limitation to keep visible

You correctly identified:

> ORM `ReplayBookmark` / `RaceEvent` not yet wired.

That's **not a reason to reopen 10.11**. Keeping the runtime event system in-memory at this stage is acceptable, provided 10.12 does not accidentally turn transport into persistence logic.

The eventual architecture should be:

```text
                 REST / WebSocket
                        │
                        ▼
              Replay Transport
                        │
                        ▼
             ReplayApplicationController
                        │
                        ▼
                ReplayEventSystem
                   │           │
             Runtime        Persistence
               Index       Repository/UoW
```

rather than:

```text
REST → database
REST → ReplayEventSystem
REST → ReplayService
```

### 10.12 recommendation

I agree with the proposed next step:

**Agent 10.12 — Replay Transport**

It should expose the existing controller through:

- REST commands/status
- WebSocket commands/events
- replay status
- playback controls
- seek/step
- bookmark CRUD/navigation
- event queries
- event notifications

while **not exposing internal `ReplayStateCache`, `EventStore`, `EventIndex`, detector, or replay-engine structures**.

Persistence can be integrated through the existing Repository/UoW architecture where appropriate, but should remain a separate concern.

**Agent 10.11 = accepted. 77 tests passed, ~83% event-system coverage, Ruff clean.** memcite

## User

Please give commands for Agent 10.12	Replay Seeking & Time Navigation	Fast-forward, rewind, jump-to-lap/event ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. **Agent 10.12 should extend the existing replay navigation architecture rather than create another seeking engine.** It should build directly on 10.7 Replay Runtime Core, 10.8 Controller, 10.9 Synchronization, 10.10 State Cache, and 10.11 Event System.

Copy/paste this entire block into Cursor:

```text
You are the Principal Distributed Systems Architect and Senior Python Engineer working on the RaceVision project.

============================================================
RACEVISION — AGENT 10.12
REPLAY SEEKING & TIME NAVIGATION
============================================================

OBJECTIVE
---------

Implement Agent 10.12 — Replay Seeking & Time Navigation.

The purpose of this agent is to provide fast, deterministic, user-facing
time navigation over the existing Replay Runtime.

Required capabilities:

- fast-forward
- rewind
- jump to timestamp
- jump to lap
- jump to event
- jump to bookmark
- jump to next/previous event
- jump to next/previous bookmark
- configurable seek increments
- configurable playback navigation rate
- boundary-safe navigation
- deterministic navigation
- synchronization with Timeline and Runtime
- integration with Replay State Cache
- integration with Replay Event System

This agent MUST NOT create another replay engine.

============================================================
EXISTING ARCHITECTURE — DO NOT BREAK
============================================================

The existing architecture is:

    Agent 10.6
    Historical Telemetry Provider
             │
             ▼
    Agent 10.7
    Replay Runtime Core
             │
             ▼
    Agent 10.8
    Replay Controller
             │
             ▼
    Agent 10.9
    Replay Synchronization
             │
             ▼
    Agent 10.10
    Replay State Cache
             │
             ▼
    Agent 10.11
    Replay Bookmark & Event System

Agent 10.12 adds a navigation layer:

             Replay Navigation
                    │
       ┌────────────┼─────────────┐
       ▼            ▼             ▼
   Time Seek     Event Jump    Lap Jump
       │            │             │
       └────────────┼─────────────┘
                    ▼
             Replay Controller
                    │
                    ▼
              ReplayService
                    │
             ┌──────┴──────┐
             ▼             ▼
        State Cache    Synchronizer
             │             │
             └──────┬──────┘
                    ▼
                 Timeline

IMPORTANT:

ReplayService remains authoritative for replay position.

Replay Runtime Core remains responsible for actual replay state movement.

Replay State Cache remains an acceleration/reconstruction layer.

Replay Synchronizer remains responsible for alignment.

Replay Event System remains responsible for event/bookmark metadata.

Agent 10.12 coordinates navigation.

============================================================
ABSOLUTE ARCHITECTURAL RULE
============================================================

DO NOT CREATE:

- another ReplayService
- another ReplayClock
- another ReplayCursor
- another ReplayEngine
- another Timeline
- another State Cache
- another Synchronizer
- another Event Bus
- another telemetry pipeline
- another normalization pipeline
- another reconstruction engine

Do not duplicate Agent 10.7 seek logic.

Navigation must ultimately delegate to:

    ReplayApplicationController
          ↓
    ReplayService
          ↓
    RaceReplay
          ↓
    existing seek/reconstruct implementation

============================================================
STEP 0 — READ THE REPOSITORY
============================================================

Before changing anything inspect:

- docs/Roadmap.md
- docs/Replay.md
- docs/specifications/ReplayRuntimeCoreSpecification.md
- docs/specifications/ReplayControllerSpecification.md
- docs/specifications/ReplaySynchronizationSpecification.md
- docs/specifications/ReplayStateCacheSpecification.md
- docs/specifications/ReplayBookmarkEventSystemSpecification.md

Inspect:

- backend/runtime/replay/
- backend/runtime/replay/control/
- backend/runtime/replay/sync/
- backend/runtime/replay/state_cache/
- backend/runtime/replay/event_system/
- replay_engine.py
- replay_service.py
- replay_manager.py
- ReplayApplicationController
- ReplayCommandDispatcher
- Timeline implementation
- ReplayClock
- FrameBuffer
- reconstruction logic
- EventIndex
- BookmarkStore
- existing commands/events
- existing protocol catalogue
- configuration
- existing tests for Agents 10.7–10.11

Search for:

    seek
    jump
    timestamp
    frame_index
    replay position
    ReplayClock
    ReplayStateCache
    events_between
    next_event
    previous_event
    next_bookmark
    previous_bookmark
    lap_number
    sector_number
    ReplayCommand
    ReplayEvent

The repository is the source of truth.

============================================================
STEP 1 — DEFINE RESPONSIBILITY
============================================================

Agent 10.12 owns navigation semantics.

It should answer:

    "Where should the replay cursor go?"

Agent 10.7 owns:

    "How does the replay state move there?"

Agent 10.9 owns:

    "Are Runtime/Timeline/Cache synchronized?"

Agent 10.10 owns:

    "Can reconstruction be accelerated?"

Agent 10.11 owns:

    "What events/bookmarks exist at that point?"

Therefore:

    Navigation
         ↓
    Controller
         ↓
    ReplayService
         ↓
    existing seek/reconstruct
         ↓
    Synchronizer
         ↓
    Timeline/Runtime

============================================================
STEP 2 — NAVIGATION PACKAGE
============================================================

Create an appropriate package, preferably:

    backend/runtime/replay/navigation/

unless an equivalent structure already exists.

Possible modules:

    navigation_service.py
    navigation_policy.py
    navigation_result.py
    navigation_target.py
    navigation_status.py
    navigation_settings.py
    exceptions.py

Use existing project conventions.

Do not blindly create every file.

============================================================
STEP 3 — NAVIGATION TARGETS
============================================================

Create a strongly typed navigation target abstraction.

Supported targets:

    TIMESTAMP
    FRAME
    LAP
    EVENT
    BOOKMARK
    NEXT_EVENT
    PREVIOUS_EVENT
    NEXT_BOOKMARK
    PREVIOUS_BOOKMARK
    START
    END

If the repository already defines an equivalent enum/model, reuse it.

============================================================
STEP 4 — TIMESTAMP SEEK
============================================================

Provide:

    jump_to_timestamp(timestamp_ms)

Requirements:

- exact timestamp if a matching frame exists
- otherwise deterministic nearest-frame behavior
- documented rounding policy
- reject negative timestamp
- clamp or reject beyond replay end according to project policy
- return actual resulting position
- return target position
- return frame index
- return whether clamping occurred

Do not silently use floating-point seconds if the runtime uses integer ms.

Canonical unit:

    integer milliseconds

============================================================
STEP 5 — FRAME SEEK
============================================================

Provide:

    jump_to_frame(frame_index)

Requirements:

- validate frame index
- reject invalid negative values
- handle end boundary
- return resulting timestamp
- use existing ReplayService seek/reconstruction
- do not directly manipulate FrameBuffer cursor

The navigation layer must not own the cursor.

============================================================
STEP 6 — FAST-FORWARD
============================================================

Provide:

    fast_forward()

and optionally:

    fast_forward(delta_ms)

Default increment should come from configuration.

Example:

    default_fast_forward_ms = 10_000

Meaning:

    current = 100000
    fast_forward()
    target = 110000

The actual configured value must be discovered from existing project
configuration conventions.

Do not hard-code the value if configuration already exists.

============================================================
STEP 7 — REWIND
============================================================

Provide:

    rewind()

and optionally:

    rewind(delta_ms)

Example:

    current = 100000
    rewind()
    target = 90000

Never allow:

    timestamp < replay_start

Result should indicate:

    requested_position
    actual_position
    clamped

============================================================
STEP 8 — CUSTOM SEEK DELTA
============================================================

Support:

    seek_relative(delta_ms)

Positive:

    fast-forward

Negative:

    rewind

Example:

    seek_relative(+5000)
    seek_relative(-15000)

This should be the fundamental primitive for relative navigation.

Then:

    fast_forward()
        → seek_relative(+configured_delta)

    rewind()
        → seek_relative(-configured_delta)

============================================================
STEP 9 — FAST-FORWARD RATE
============================================================

Do NOT confuse:

    seek relative

with:

    playback speed.

Agent 10.7 ReplayClock already controls playback rate.

Agent 10.12 may provide navigation commands such as:

    fast_forward

but must not replace ReplayClock.

If rate controls are already supported, integrate with them rather than
creating a second clock.

============================================================
STEP 10 — JUMP TO START
============================================================

Provide:

    jump_to_start()

Semantics:

    replay_start_timestamp

Use ReplayService.

Do not directly modify:

    ReplayClock
    FrameBuffer
    Timeline

============================================================
STEP 11 — JUMP TO END
============================================================

Provide:

    jump_to_end()

Semantics:

    final available replay frame

Return:

- timestamp
- frame index
- replay state
- whether replay is finished

Do not assume timestamp 0 or a configured race duration.

Derive the end from actual loaded replay data.

============================================================
STEP 12 — JUMP TO LAP
============================================================

Provide:

    jump_to_lap(lap_number)

Potential overload:

    jump_to_lap(driver_id, lap_number)

Inspect existing Lap/Event models before choosing the signature.

The target should use existing canonical lap events/data.

Example:

    lap 15

should resolve to a deterministic timestamp/frame.

Define semantics clearly:

    jump to beginning of lap

or:

    jump to completion of lap

Preferred default:

    jump to beginning of requested lap

If the system already defines another convention, reuse it.

============================================================
STEP 13 — LAP NAVIGATION
============================================================

Provide:

    next_lap()
    previous_lap()

Use existing lap/event information.

Do NOT create a second lap detector.

Agent 10.11 already exposes lap events.

Navigation should query the event system.

============================================================
STEP 14 — JUMP TO EVENT
============================================================

Provide:

    jump_to_event(event_id)

Use Agent 10.11 EventStore/EventIndex.

Flow:

    event_id
       ↓
    EventSystem
       ↓
    event.timestamp_ms
       ↓
    ReplayApplicationController
       ↓
    ReplayService.seek()

Do not duplicate event lookup logic.

============================================================
STEP 15 — NEXT/PREVIOUS EVENT
============================================================

Provide:

    next_event()
    previous_event()

Optional:

    next_event(event_type)
    previous_event(event_type)

Use existing EventIndex.

The result must identify:

- event_id
- event_type
- timestamp_ms
- frame_index
- driver/entity information where available
- target position

============================================================
STEP 16 — JUMP TO BOOKMARK
============================================================

Provide:

    jump_to_bookmark(bookmark_id)

Flow:

    BookmarkStore
       ↓
    timestamp/frame
       ↓
    ReplayService.seek()

Do not create a second bookmark store.

============================================================
STEP 17 — NEXT/PREVIOUS BOOKMARK
============================================================

Provide:

    next_bookmark()
    previous_bookmark()

Use Agent 10.11 navigation.

Example:

    current = 60s

    bookmarks:
        20s
        80s
        120s

    next_bookmark()
        → 80s

    previous_bookmark()
        → 20s

Boundary behavior must be deterministic.

============================================================
STEP 18 — EVENT TYPE NAVIGATION
============================================================

Where supported:

    next_overtake()
    previous_overtake()

    next_incident()
    previous_incident()

    next_pit_event()
    previous_pit_event()

Do NOT create separate navigation engines.

These should be thin wrappers around:

    next_event(event_type=...)

============================================================
STEP 19 — DRIVER-SPECIFIC EVENT NAVIGATION
============================================================

If supported by Agent 10.11:

    next_event(driver_id=...)
    previous_event(driver_id=...)

Use EventIndex filtering.

Do not scan the complete telemetry stream.

============================================================
STEP 20 — NAVIGATION RESULT
============================================================

Create an immutable result object.

Conceptually:

    ReplayNavigationResult

Possible fields:

- success
- replay_id
- previous_timestamp_ms
- target_timestamp_ms
- actual_timestamp_ms
- previous_frame_index
- target_frame_index
- actual_frame_index
- target_type
- event_id optional
- bookmark_id optional
- lap_number optional
- clamped
- direction
- reason
- replay_state

Use project-standard result patterns if they already exist.

============================================================
STEP 21 — BOUNDARY BEHAVIOR
============================================================

Define exact semantics for:

    before start
    after end
    empty replay
    one-frame replay
    exact timestamp
    between-frame timestamp

Example:

    replay = 0ms ... 100000ms

    rewind from 5000 by 10000

    result = 0ms
    clamped = true

Example:

    fast-forward from 98000 by 10000

    result = 100000ms
    clamped = true

Do not produce negative positions.

============================================================
STEP 22 — EMPTY REPLAY
============================================================

If no replay is loaded:

return the project's structured:

    ReplayNotLoaded

or equivalent error.

Do not create a navigation state without a loaded replay.

============================================================
STEP 23 — FINISHED REPLAY
============================================================

Respect Agent 10.7 semantics.

Do not change:

    FINISHED
    STOPPED
    PAUSED
    PLAYING

state machine semantics.

If seeking from FINISHED is supported by ReplayService, delegate to it.

If reset is required before play, preserve the existing rule:

    play after FINISHED requires reset()

Navigation must not silently alter that behavior.

============================================================
STEP 24 — PAUSED VS PLAYING
============================================================

Seeking must not accidentally start playback.

Example:

    PLAYING
       ↓
    seek
       ↓
    PLAYING

or according to existing ReplayService semantics.

Example:

    PAUSED
       ↓
    seek
       ↓
    PAUSED

Preserve existing state unless the architecture explicitly defines
otherwise.

============================================================
STEP 25 — FAST-FORWARD WHILE PLAYING
============================================================

If:

    PLAYING
    fast_forward()

the operation must be deterministic.

Do not create a second background playback loop.

Do not spawn threads.

Do not alter wall-clock scheduling.

Use the existing ReplayService cooperative runtime.

============================================================
STEP 26 — SEEK PERFORMANCE
============================================================

Agent 10.10 already provides:

    snapshots
    FrameIndex
    SnapshotIndex
    reconstruct_to_index

Agent 10.12 must use those facilities indirectly through ReplayService.

Do NOT bypass ReplayService and manually reconstruct.

Navigation should therefore benefit automatically from checkpoints.

============================================================
STEP 27 — EVENT JUMP PERFORMANCE
============================================================

Jumping to an event must NOT scan telemetry.

Use:

    EventIndex

Example:

    next OVERTAKE

should be approximately:

    EventIndex lookup
       ↓
    timestamp
       ↓
    ReplayService.seek

============================================================
STEP 28 — LAP JUMP PERFORMANCE
============================================================

Jumping to lap must use indexed lap/event information.

Do not iterate through every telemetry frame to find lap 50.

============================================================
STEP 29 — NAVIGATION HISTORY
============================================================

Do not add browser-like navigation history unless the existing
requirements explicitly require it.

A seek operation should not automatically create a stack of previous
positions.

Keep Agent 10.12 focused.

============================================================
STEP 30 — SEEK COALESCING
============================================================

Do not add asynchronous seek coalescing unless existing architecture
requires it.

Navigation is deterministic and cooperative.

Multiple commands:

    seek 10s
    seek 20s
    seek 30s

should execute in order.

============================================================
STEP 31 — THREAD SAFETY
============================================================

Agent 10.7 already uses manager locking.

Do not introduce another locking strategy.

Navigation should use the existing ReplayManager/ReplayService concurrency
boundary.

============================================================
STEP 32 — SYNCHRONIZATION
============================================================

After navigation:

    ReplayService.seek(...)
            ↓
    RaceReplay
            ↓
    ReplaySynchronizer
            ↓
    Timeline / Runtime / Cache

Do not call Timeline.seek directly from NavigationService.

Do not call StateCache.restore directly.

Do not call Synchronizer internals directly unless existing public APIs
require it.

============================================================
STEP 33 — STATE CACHE
============================================================

Navigation must benefit from Agent 10.10 checkpoints.

Do not modify checkpoint policy in Agent 10.12 unless required.

Do not add another navigation cache.

============================================================
STEP 34 — EVENT SYSTEM
============================================================

Navigation must use Agent 10.11 for:

- event lookup
- bookmark lookup
- lap lookup
- next/previous navigation

Do not duplicate:

    EventIndex
    BookmarkStore
    event detector

============================================================
STEP 35 — TIMELINE
============================================================

Timeline remains a synchronized projection.

Never:

    NavigationService → Timeline.seek()

Instead:

    NavigationService
         ↓
    ReplayController
         ↓
    ReplayService
         ↓
    ReplaySynchronizer
         ↓
    Timeline

============================================================
STEP 36 — PROTOCOL COMMANDS
============================================================

Inspect existing replay protocol commands first.

Add commands only where required.

Potential commands:

    SeekReplay
    SeekRelative
    FastForwardReplay
    RewindReplay
    JumpToLap
    JumpToEvent
    JumpToBookmark
    NextReplayEvent
    PreviousReplayEvent
    NextReplayBookmark
    PreviousReplayBookmark
    JumpToStart
    JumpToEnd

Do NOT duplicate commands that already exist.

Use existing command naming conventions.

Update:

    shared/protocols/commands/replay/
    shared/protocols/events/replay/
    catalogue.py
    __init__.py

where appropriate.

============================================================
STEP 37 — CONTROLLER INTEGRATION
============================================================

Agent 10.8 provides:

    ReplayApplicationController
    ReplayCommandDispatcher

Agent 10.12 should integrate with those.

Preferred architecture:

    Command
       ↓
    ReplayCommandDispatcher
       ↓
    ReplayApplicationController
       ↓
    ReplayNavigationService
       ↓
    ReplayService

or:

    Controller
       ↓
    NavigationService
       ↓
    ReplayService

depending on existing conventions.

The Controller remains a façade.

Navigation logic must not be embedded into protocol dispatch code.

============================================================
STEP 38 — REST/WEBSOCKET
============================================================

DO NOT implement REST or WebSocket transport in Agent 10.12.

That belongs to the planned transport phase.

Commands/protocols may be defined so the future transport can consume them.

============================================================
STEP 39 — CONFIGURATION
============================================================

Inspect existing configuration.

Potential settings:

    default_seek_step_ms
    fast_forward_step_ms
    rewind_step_ms
    navigation_boundary_policy
    timestamp_seek_policy

Do not duplicate existing replay settings.

No hard-coded absolute filesystem paths.

No credentials.

============================================================
STEP 40 — TIME SEMANTICS
============================================================

Canonical internal time:

    integer milliseconds

Do not mix:

    seconds
    milliseconds
    nanoseconds

without explicit conversion.

Public APIs should document units.

If human-readable duration objects already exist, reuse them.

============================================================
STEP 41 — FRAME/TIME RESOLUTION
============================================================

For timestamp seeks between frames:

Example:

    frames:
       1000ms
       1020ms
       1040ms

requested:

    1030ms

Choose and document one policy:

    FLOOR
    CEIL
    NEAREST

Prefer existing ReplayService behavior if already defined.

Do not create conflicting seek semantics.

============================================================
STEP 42 — JUMP TO EVENT EXACTNESS
============================================================

For an event at:

    timestamp_ms = 52340

jump target should be:

    52340ms

subject to the existing frame-resolution policy.

Return both:

    requested event timestamp

and:

    actual replay position.

============================================================
STEP 43 — JUMP TO LAP SEMANTICS
============================================================

Define:

    lap start
    lap completion

using existing event timestamps.

Preferred:

    jump_to_lap(N)
        → first frame/event belonging to lap N

If the existing domain model defines another convention, follow it.

Document it.

============================================================
STEP 44 — JUMP TO SECTOR
============================================================

If useful and supported by existing Agent 10.11 data, also provide:

    jump_to_sector(lap_number, sector_number)

and:

    next_sector()
    previous_sector()

Do not make sector navigation mandatory if canonical sector events are
not available.

============================================================
STEP 45 — NAVIGATION STATUS
============================================================

Provide:

    ReplayNavigationStatus

Possible fields:

- replay_id
- current_timestamp_ms
- current_frame_index
- start_timestamp_ms
- end_timestamp_ms
- current_lap
- current_sector
- next_event_available
- previous_event_available
- next_bookmark_available
- previous_bookmark_available
- can_fast_forward
- can_rewind
- can_jump_start
- can_jump_end

This should be read-only.

============================================================
STEP 46 — NAVIGATION CAPABILITIES
============================================================

Expose capability checks:

    can_fast_forward()
    can_rewind()
    can_jump_to_event()
    can_jump_to_bookmark()
    can_jump_to_lap()
    can_next_event()
    can_previous_event()
    can_next_bookmark()
    can_previous_bookmark()

These should not duplicate Controller capability logic unnecessarily.

Integrate with existing status/capability patterns.

============================================================
STEP 47 — ERROR HANDLING
============================================================

Use structured project errors.

Handle:

- replay not loaded
- invalid timestamp
- invalid frame
- invalid lap
- invalid sector
- event not found
- bookmark not found
- no next event
- no previous event
- no next bookmark
- no previous bookmark
- empty replay
- navigation failure
- replay mismatch

Potential names:

    ReplayNavigationError
    InvalidNavigationTarget
    NavigationTargetNotFound
    NavigationBoundaryError

Reuse existing exception hierarchy where appropriate.

============================================================
STEP 48 — TESTS
============================================================

Create:

    tests/runtime/replay_navigation/

or follow existing repository conventions.

============================================================
TEST GROUP 1 — TIMESTAMP SEEK
============================================================

Test:

- exact timestamp
- between frames
- before start
- after end
- zero
- final timestamp

Verify documented resolution policy.

============================================================
TEST GROUP 2 — FRAME SEEK
============================================================

Test:

- first frame
- middle frame
- final frame
- invalid negative frame
- beyond end

============================================================
TEST GROUP 3 — RELATIVE SEEK
============================================================

Test:

    +delta

and:

    -delta

Verify exact resulting timestamp.

============================================================
TEST GROUP 4 — FAST-FORWARD
============================================================

Test configured increment.

Verify:

    current + increment

and end clamping.

============================================================
TEST GROUP 5 — REWIND
============================================================

Test configured increment.

Verify:

    current - increment

and start clamping.

============================================================
TEST GROUP 6 — START/END
============================================================

Test:

    jump_to_start()
    jump_to_end()

============================================================
TEST GROUP 7 — LAP
============================================================

Test:

    jump_to_lap(1)
    jump_to_lap(N)
    next_lap()
    previous_lap()

Verify event system is used.

============================================================
TEST GROUP 8 — EVENT
============================================================

Test:

    jump_to_event(event_id)
    next_event()
    previous_event()

Verify EventIndex is used rather than telemetry scanning.

============================================================
TEST GROUP 9 — BOOKMARK
============================================================

Test:

    jump_to_bookmark(bookmark_id)
    next_bookmark()
    previous_bookmark()

============================================================
TEST GROUP 10 — EVENT TYPE
============================================================

Test:

    next OVERTAKE
    previous OVERTAKE
    next INCIDENT
    previous INCIDENT

where those events exist.

============================================================
TEST GROUP 11 — DRIVER FILTER
============================================================

If supported:

    next event for driver X
    previous event for driver X

============================================================
TEST GROUP 12 — STATE PRESERVATION
============================================================

Verify navigation does not create a second replay state machine.

Test:

    PAUSED → seek → PAUSED

    PLAYING → seek → existing expected state

    FINISHED → seek

according to Agent 10.7 semantics.

============================================================
TEST GROUP 13 — SYNCHRONIZATION
============================================================

After every navigation operation verify:

    ReplayService position
          ≈
    Timeline
          ≈
    Synchronization status

within existing 1ms tolerance.

============================================================
TEST GROUP 14 — STATE CACHE
============================================================

Verify large seeks use the existing reconstruction/checkpoint mechanism.

Do not duplicate reconstruction.

============================================================
TEST GROUP 15 — EVENT DEDUPLICATION
============================================================

Repeated:

    jump_to_event()

must not create duplicate events.

============================================================
TEST GROUP 16 — BACKWARD/FORWARD
============================================================

Test:

    60s → 20s → 80s → 10s → 100s

Verify deterministic state.

============================================================
TEST GROUP 17 — BOUNDARIES
============================================================

Test:

    rewind beyond start
    fast-forward beyond end

Verify:

- clamped
- no negative time
- no timestamp beyond replay end

============================================================
TEST GROUP 18 — EMPTY REPLAY
============================================================

Verify structured ReplayNotLoaded/empty replay errors.

============================================================
TEST GROUP 19 — ISOLATION
============================================================

Load:

    Replay A
    Replay B

Verify navigation never resolves events/bookmarks from the wrong replay.

============================================================
TEST GROUP 20 — CONTROLLER
============================================================

Verify:

    Command
      ↓
    Dispatcher
      ↓
    Controller
      ↓
    Navigation
      ↓
    ReplayService

No navigation logic should exist inside command parsing.

============================================================
TEST GROUP 21 — PROTOCOL
============================================================

Test command serialization/deserialization.

Verify protocol catalogue registration.

============================================================
TEST GROUP 22 — DETERMINISM
============================================================

Run identical navigation sequence twice:

    start
    +10s
    +10s
    jump event
    -5s
    next bookmark
    end
    rewind

Verify identical final:

- timestamp
- frame
- replay state
- synchronization status

============================================================
TEST GROUP 23 — REGRESSION
============================================================

Run all relevant tests for:

- Agent 10.6
- Agent 10.7
- Agent 10.8
- Agent 10.9
- Agent 10.10
- Agent 10.11
- Event Bus
- Timeline
- State Cache
- Replay
- providers
- normalization
- database where affected

Fix all regressions caused by Agent 10.12.

============================================================
STEP 49 — PERFORMANCE
============================================================

Navigation must remain fast for large historical sessions.

Avoid:

    O(number_of_telemetry_frames)

for:

    next_event
    previous_event
    next_bookmark
    previous_bookmark
    jump_to_event
    jump_to_bookmark
    jump_to_lap

Use:

    EventIndex
    BookmarkStore/index
    FrameIndex
    SnapshotIndex

through existing abstractions.

============================================================
STEP 50 — DOCUMENTATION
============================================================

Create:

    docs/specifications/ReplaySeekingTimeNavigationSpecification.md

unless an equivalent specification already exists.

Document:

- architecture
- navigation targets
- timestamp semantics
- frame semantics
- fast-forward
- rewind
- relative seeking
- start/end
- lap navigation
- sector navigation
- event navigation
- bookmark navigation
- boundary behavior
- frame resolution
- state-machine behavior
- synchronization
- State Cache interaction
- Event System interaction
- performance
- errors
- determinism

Update:

    docs/specifications/README.md

Update:

    docs/Replay.md

Update:

    docs/Roadmap.md

Mark Agent 10.12 complete only after all acceptance criteria pass.

============================================================
STEP 51 — CODE QUALITY
============================================================

Follow RaceVision standards:

- Python 3.11
- PEP 8
- complete type hints
- dependency inversion
- immutable result/status models where appropriate
- deterministic behavior
- no global mutable state
- no circular imports
- no duplicate domain logic

Run repository-standard:

- formatter
- Ruff
- type checking
- tests
- coverage

Discover exact commands from:

- pyproject.toml
- Makefile
- CI configuration
- scripts

============================================================
STEP 52 — ARCHITECTURAL GUARDRAILS
============================================================

DO NOT:

- rewrite ReplayService
- rewrite ReplayEngine
- rewrite ReplayClock
- rewrite ReplayStateCache
- rewrite ReplaySynchronizer
- rewrite EventSystem
- create a second EventIndex
- create a second BookmarkStore
- directly manipulate Timeline
- directly manipulate State Cache
- directly manipulate FrameBuffer cursor
- directly call FastF1
- bypass Controller architecture
- create REST
- create WebSocket transport
- create Unity UI
- create OBS integration
- create camera logic
- add Redis
- add unnecessary infrastructure
- add browser-style navigation history

============================================================
STEP 53 — ACCEPTANCE CRITERIA
============================================================

Agent 10.12 is COMPLETE only when:

[ ] Navigation package exists.
[ ] Timestamp seek works.
[ ] Frame seek works.
[ ] Relative seek works.
[ ] Fast-forward works.
[ ] Rewind works.
[ ] Start navigation works.
[ ] End navigation works.
[ ] Jump-to-lap works where canonical lap data exists.
[ ] Next/previous lap works where supported.
[ ] Jump-to-event works.
[ ] Next/previous event works.
[ ] Event-type navigation works where supported.
[ ] Jump-to-bookmark works.
[ ] Next/previous bookmark works.
[ ] Sector navigation works where supported.
[ ] Driver-filtered navigation works where supported.
[ ] Navigation uses existing ReplayService.
[ ] Navigation does not create another replay cursor.
[ ] Navigation does not create another clock.
[ ] Navigation does not create another reconstruction engine.
[ ] Navigation benefits from Agent 10.10 checkpoints.
[ ] Navigation uses Agent 10.11 EventIndex.
[ ] Navigation uses Agent 10.11 BookmarkStore.
[ ] Timeline remains synchronized through Agent 10.9.
[ ] Runtime state remains synchronized.
[ ] Boundary behavior is deterministic.
[ ] Timestamp/frame resolution is documented.
[ ] Playback state semantics remain unchanged.
[ ] Seeking does not unexpectedly start playback.
[ ] Backward seeking does not duplicate events.
[ ] Replay/session isolation works.
[ ] Structured errors exist.
[ ] Navigation status exists.
[ ] Navigation capabilities exist.
[ ] Protocol commands are added only where needed.
[ ] Controller integration remains thin.
[ ] No REST/WS transport is implemented.
[ ] Tests added.
[ ] Regression tests pass.
[ ] Ruff passes.
[ ] Type checking passes where configured.
[ ] Coverage meets repository gate.
[ ] Documentation updated.
[ ] Roadmap updated.

============================================================
STEP 54 — FINAL REPORT
============================================================

When complete, report:

1. Files created.
2. Files modified.
3. Navigation architecture.
4. Navigation targets.
5. Timestamp seek semantics.
6. Frame seek semantics.
7. Fast-forward behavior.
8. Rewind behavior.
9. Start/end behavior.
10. Lap navigation.
11. Sector navigation.
12. Event navigation.
13. Bookmark navigation.
14. Boundary behavior.
15. Frame resolution policy.
16. Controller integration.
17. Protocol changes.
18. State Cache integration.
19. Synchronization behavior.
20. Event System integration.
21. Performance characteristics.
22. Error handling.
23. Determinism guarantees.
24. Tests added.
25. Full test results.
26. Coverage.
27. Ruff/type-check results.
28. Documentation updated.
29. Roadmap status.
30. Known limitations.
31. Recommended Agent 10.13.

Do NOT claim completion if required tests fail.

============================================================
START IMPLEMENTATION
============================================================

First inspect the complete implementations and tests for:

- Agent 10.6 Historical Telemetry Provider
- Agent 10.7 Replay Runtime Core
- Agent 10.8 Replay Controller
- Agent 10.9 Replay Synchronization
- Agent 10.10 Replay State Cache
- Agent 10.11 Replay Bookmark & Event System

Then inspect the current repository implementation.

Implement Agent 10.12 completely.

Build on the existing architecture.

Do not rewrite working functionality.

Run tests after implementation.

Fix failures caused by the implementation.

Update specifications, Replay documentation and Roadmap.

Only then provide the final implementation report.
```

## User

**Agent 10.12 complete.** 87 Phase 10.7–10.12 tests passed; navigation coverage **91%**; ruff clean.

### 1–2. Files

**Created:** `backend/runtime/replay/navigation/` (`navigation_service.py`, `enums.py`, `result.py`, `exceptions.py`, `__init__.py`), `docs/specifications/ReplaySeekingTimeNavigationSpecification.md`, `tests/runtime/replay_navigation/`

**Modified:** `configuration.py`, `control/application_controller.py`, `control/command_dispatcher.py`, `control/errors.py`, `event_system` next/previous driver filter, `replay/__init__.py`, protocol commands, `docs/Replay.md`, `Roadmap.md`, specs README

### 3–9. Architecture / seeking

```text
Command → Dispatcher → Controller → ReplayNavigationService → ReplayService.seek
                                                              → RaceReplay (+ State Cache + Sync)
```

Targets: TIMESTAMP, FRAME, RELATIVE, FF/RW, START/END, LAP/SECTOR, EVENT, BOOKMARK, next/prev variants. **FLOOR** ms resolution (matches `index_at_or_before`). FF/RW via `default_seek_step_ms` / `fast_forward_step_ms` / `rewind_step_ms` (default **10000**). Start/end from loaded buffer bounds; clamp with `clamped=true`.

### 10–15. Lap / sector / event / bookmark / boundaries

`jump_to_lap(N)`: N=1 → start; N>1 → `LAP_COMPLETED` of N−1. Sector S of lap L via prior sector completion. Events/bookmarks via Agent 10.11 indexes (no telemetry scan). Typed helpers: overtake/incident/pit. Boundaries never go negative or past end.

### 16–23. Integration / quality

Controller wraps nav in `ReplayControlResult`; commands: `SeekRelative`, `FastForwardReplay`, `RewindReplay`, `JumpToStart/End/Event/Lap`, `Next/PreviousReplayEvent/Bookmark`. Seek still drives 10.9 sync + 10.10 checkpoints. Deterministic; PAUSED stays paused. **No REST/WS.**

### 24–31. Tests / docs / next

Regression **87 passed**. Roadmap: **10.12 checked**; **10.13+** transport/presentation.
**Limitation:** Lap/sector need Agent 10.11 markers in frames.
**Recommend Agent 10.13:** Replay transport (REST/WebSocket) over the control plane.

## Assistant

**Agent 10.12 is accepted as complete.** The implementation fits the existing RaceVision replay architecture and the reported results are good.

### Phase 10 replay progression

| Agent | Component | Status |
|---|---|---|
| 10.6 | Historical Telemetry Provider | ✅ |
| 10.7 | Replay Runtime Core | ✅ |
| 10.8 | Replay Controller | ✅ |
| 10.9 | Replay Synchronization | ✅ |
| 10.10 | Replay State Cache | ✅ |
| 10.11 | Replay Bookmark & Event System | ✅ |
| **10.12** | **Replay Seeking & Time Navigation** | **✅** |

### Current replay architecture

```text
Historical Telemetry
        │
        ▼
   ReplayService
        │
        ▼
     RaceReplay
        │
 ┌──────┼───────────────┐
 │      │               │
 ▼      ▼               ▼
Clock  State Cache   Event System
 │      │               │
 │      │          ┌────┴─────┐
 │      │          ▼          ▼
 │      │       Events     Bookmarks
 │      │
 └──────┼──────────────────────┐
        ▼                      │
 Replay Navigation             │
        │                      │
        ▼                      │
 Replay Controller              │
        │                      │
        └──────────┬───────────┘
                   ▼
             Synchronizer
                   │
             ┌─────┴─────┐
             ▼           ▼
          Timeline    Runtime
```

### Particularly important decisions

**1. No second seek engine**

```text
NavigationService
       ↓
ReplayService.seek()
       ↓
RaceReplay
```

This preserves Agent 10.7 as the authoritative runtime.

**2. Fast-forward/rewind use relative seeking**

```text
fast_forward()
    ↓
+10,000 ms

rewind()
    ↓
-10,000 ms
```

with configuration rather than hard-coded navigation behavior.

**3. Event/bookmark navigation uses existing indexes**

This is important for scalability:

```text
next_event()
    ↓
EventIndex
    ↓
timestamp
    ↓
ReplayService.seek()
```

rather than scanning telemetry.

**4. State Cache and Synchronization remain behind ReplayService**

That means 10.12 doesn't undermine the work from 10.9/10.10.

**5. FLOOR timestamp resolution**

Using the existing `index_at_or_before` semantics avoids introducing conflicting timestamp behavior.

**6. Deterministic boundaries**

```text
rewind past start
        ↓
start

fast-forward past end
        ↓
end
```

with `clamped=true`.

### One thing I'd keep an eye on

The lap semantics:

```text
jump_to_lap(1) → replay start
jump_to_lap(N) → LAP_COMPLETED(N-1)
```

are reasonable, but should remain explicitly documented because they represent **"jump to beginning of lap"**, not "jump to lap completion."

The limitation that lap/sector navigation requires the Agent 10.11 markers is also acceptable. **Don't weaken the architecture by adding another lap detector just to remove that limitation.**

### Quality

Reported:

- **87 Phase 10.7–10.12 tests passed** ✅
- Navigation coverage **91%** ✅
- Ruff clean ✅
- Regression suite passing ✅
- Roadmap 10.12 checked ✅
- No REST/WS prematurely implemented ✅

So I would mark:

> **Agent 10.12 — COMPLETE / ACCEPTED**

The natural next architectural boundary is indeed **Agent 10.13 — Replay Transport**, exposing the already-built control plane through REST/WebSocket rather than adding more replay internals. memcite

## User

Please give commands for Agent 10.13	Replay Recording/Playback Validation	Verify historical replay integrity ( 1 click copy and paste cursor friendly)

## Assistant

Yes. **Agent 10.13 should be a validation/integrity layer**, not another replay engine. It should validate that historical recordings can be loaded, traversed, reconstructed, synchronized, and replayed deterministically using the existing 10.6–10.12 stack.

Copy/paste this entire block into Cursor:

```text
You are the Principal Distributed Systems Architect and Senior Python Engineer working on the RaceVision project.

============================================================
RACEVISION — AGENT 10.13
REPLAY RECORDING / PLAYBACK VALIDATION
============================================================

OBJECTIVE
---------

Implement Agent 10.13 — Replay Recording/Playback Validation.

The purpose of this agent is to verify the integrity, consistency,
determinism, completeness, and replayability of historical telemetry
recordings before and during replay.

This is a VALIDATION layer.

It must NOT become:

- another replay engine
- another telemetry provider
- another normalization pipeline
- another state cache
- another synchronization engine
- another event detector
- another persistence layer
- another playback controller

The existing Replay Runtime remains authoritative.

============================================================
EXISTING ARCHITECTURE — DO NOT BREAK
============================================================

Current completed replay architecture:

    Agent 10.6
    Historical Telemetry Provider
             │
             ▼
    Agent 10.7
    Replay Runtime Core
             │
             ▼
    Agent 10.8
    Replay Controller
             │
             ▼
    Agent 10.9
    Replay Synchronization
             │
             ▼
    Agent 10.10
    Replay State Cache
             │
             ▼
    Agent 10.11
    Replay Bookmark & Event System
             │
             ▼
    Agent 10.12
    Replay Seeking & Time Navigation

Agent 10.13 adds:

             Historical Replay
                    │
                    ▼
             Replay Validator
                    │
       ┌────────────┼─────────────┐
       ▼            ▼             ▼
   Recording     Playback      Determinism
   Integrity     Integrity       Checks
       │            │             │
       └────────────┼─────────────┘
                    ▼
              ValidationReport

The validator consumes existing replay abstractions.

============================================================
ABSOLUTE ARCHITECTURAL RULE
============================================================

DO NOT CREATE:

- another ReplayService
- another ReplayEngine
- another ReplayClock
- another ReplayCursor
- another FrameBuffer
- another State Cache
- another SnapshotIndex
- another EventIndex
- another Event Detector
- another Timeline
- another Synchronizer
- another FastF1 client
- another telemetry normalizer
- another database persistence system

Do not duplicate Agent 10.7–10.12 logic.

The validator OBSERVES and VALIDATES existing behavior.

============================================================
STEP 0 — READ THE REPOSITORY
============================================================

Before changing anything inspect:

- docs/Roadmap.md
- docs/Replay.md
- docs/specifications/HistoricalTelemetryProviderSpecification.md
- docs/specifications/ReplayRuntimeCoreSpecification.md
- docs/specifications/ReplayControllerSpecification.md
- docs/specifications/ReplaySynchronizationSpecification.md
- docs/specifications/ReplayStateCacheSpecification.md
- docs/specifications/ReplayBookmarkEventSystemSpecification.md
- docs/specifications/ReplaySeekingTimeNavigationSpecification.md

Inspect:

- backend/providers/fastf1/
- backend/runtime/replay/
- backend/runtime/replay/control/
- backend/runtime/replay/sync/
- backend/runtime/replay/state_cache/
- backend/runtime/replay/event_system/
- backend/runtime/replay/navigation/
- ReplayService
- RaceReplay
- ReplayClock
- FrameBuffer
- reconstruction logic
- Timeline
- State Cache
- Synchronizer
- Event System
- Navigation Service
- protocol commands/events
- configuration
- all replay tests

Search for:

    replay
    recording
    historical
    frame
    timestamp
    checksum
    hash
    validation
    integrity
    deterministic
    reconstruct
    snapshot
    telemetry
    source_provider
    session
    lap
    sector
    event

The repository is the source of truth.

============================================================
STEP 1 — DEFINE RESPONSIBILITY
============================================================

Agent 10.13 owns validation.

It should answer:

    "Is this historical replay valid and replayable?"

It should NOT answer:

    "How should replay work?"

That remains Agent 10.7.

Validation must inspect:

    recording structure
    frame ordering
    timestamps
    frame continuity
    canonical telemetry validity
    session identity
    replay boundaries
    state reconstruction
    synchronization
    event/index consistency
    deterministic playback

============================================================
STEP 2 — VALIDATION PACKAGE
============================================================

Create an appropriate package:

    backend/runtime/replay/validation/

unless an equivalent package already exists.

Suggested modules:

    __init__.py
    replay_validator.py
    recording_validator.py
    playback_validator.py
    determinism_validator.py
    integrity_validator.py
    checks.py
    models.py
    enums.py
    result.py
    status.py
    exceptions.py

Use repository conventions.

Do not blindly create all files if existing abstractions already provide
the required functionality.

============================================================
STEP 3 — VALIDATION MODEL
============================================================

Create strongly typed validation models.

Possible models:

    ValidationSeverity

Values:

    INFO
    WARNING
    ERROR
    FATAL

    ValidationStatus

Values:

    NOT_RUN
    PASSED
    PASSED_WITH_WARNINGS
    FAILED

    ValidationCheck

Fields may include:

    check_id
    category
    severity
    status
    message
    timestamp_ms
    frame_index
    details

Create:

    ReplayValidationReport

Possible fields:

    replay_id
    status
    started_at
    completed_at
    duration_ms
    total_checks
    passed_checks
    warning_checks
    failed_checks
    errors
    warnings
    checks

Use immutable models where appropriate.

============================================================
STEP 4 — VALIDATION CATEGORIES
============================================================

Support at least:

    RECORDING_STRUCTURE
    TIMESTAMP_INTEGRITY
    FRAME_INTEGRITY
    TELEMETRY_INTEGRITY
    SESSION_INTEGRITY
    BOUNDARY_INTEGRITY
    RECONSTRUCTION_INTEGRITY
    SYNCHRONIZATION_INTEGRITY
    EVENT_INTEGRITY
    BOOKMARK_INTEGRITY
    PLAYBACK_INTEGRITY
    DETERMINISM
    NAVIGATION_INTEGRITY

Reuse existing enums if present.

============================================================
STEP 5 — RECORDING EXISTENCE
============================================================

Validate that a historical replay actually contains usable data.

Check:

- replay is loaded
- replay ID exists
- frames exist
- frame count > 0
- start timestamp exists
- end timestamp exists
- start <= end

Empty replay should produce a structured validation failure.

Do not crash.

============================================================
STEP 6 — FRAME COUNT VALIDATION
============================================================

Validate:

    frame_count > 0

If metadata exposes expected frame count, compare:

    expected_frame_count
    actual_frame_count

If expected count is unavailable, do not invent one.

============================================================
STEP 7 — TIMESTAMP VALIDATION
============================================================

Validate all loaded canonical frames for:

- timestamp exists
- timestamp is integer milliseconds
- timestamp is not negative unless domain explicitly permits it
- timestamps are monotonic
- no impossible backwards timestamp jumps

Expected:

    t[n+1] >= t[n]

If strict increasing timestamps are NOT guaranteed by the provider,
allow equal timestamps.

Do not impose an unsupported strict-increase requirement.

============================================================
STEP 8 — TIMESTAMP GAP ANALYSIS
============================================================

Calculate:

- minimum frame delta
- maximum frame delta
- average frame delta
- frame delta distribution where practical
- suspicious gaps

Do not automatically declare a large gap invalid.

A gap may be legitimate depending on source/session.

Use:

    WARNING

unless project specifications define a hard maximum.

Report:

    gap_start
    gap_end
    delta_ms
    frame indexes

============================================================
STEP 9 — FRAME ORDER VALIDATION
============================================================

Verify frame indexes are logically ordered.

Expected:

    0
    1
    2
    ...

If frame indexes are not explicitly stored, validate buffer ordering.

Do not mutate the recording while validating.

============================================================
STEP 10 — CANONICAL FRAME VALIDATION
============================================================

Inspect canonical telemetry fields already defined by the project.

Validate:

- required identifiers
- timestamp
- session identity
- driver/car identity where required
- position fields where present
- speed where present
- race order where present
- lap/sector fields where present

Do NOT invent new telemetry requirements.

Use the canonical frame model as the source of truth.

============================================================
STEP 11 — NUMERIC VALIDATION
============================================================

Where canonical models define numeric ranges, validate them.

Examples:

- finite floating-point values
- no NaN
- no infinity
- valid latitude/longitude only if applicable
- speed >= 0 where domain defines speed as non-negative
- valid lap/sector values
- valid race order values

Do not invent arbitrary physics limits.

For fields where limits are unknown:

    check finite/value presence only.

============================================================
STEP 12 — SOURCE PROVIDER VALIDATION
============================================================

Validate:

    source_provider

is populated according to the canonical telemetry contract.

Historical replay should identify its provider appropriately.

Do not require a specific provider string unless the specification already
defines it.

============================================================
STEP 13 — SESSION IDENTITY
============================================================

Validate consistency of:

- replay_id
- session_id
- season
- event
- session type

where these fields exist.

A replay must not silently contain frames from multiple unrelated sessions.

If mixed session identity is detected:

    ERROR

unless the domain explicitly permits it.

============================================================
STEP 14 — DRIVER/CAR IDENTITY
============================================================

Validate that driver/car identifiers remain consistent with the loaded
session.

If the project has canonical participant metadata, verify references.

Do not require every frame to contain every driver.

Historical telemetry may legitimately have sparse channels.

============================================================
STEP 15 — RECORDING BOUNDARIES
============================================================

Validate:

    first_frame_timestamp
    last_frame_timestamp

against:

    ReplayService
    FrameBuffer

Verify:

    replay_start == buffer_start
    replay_end == buffer_end

according to existing timestamp resolution.

Do not use a separately calculated replay duration as authoritative.

============================================================
STEP 16 — FRAME BUFFER INTEGRITY
============================================================

Use the existing FrameBuffer APIs.

Validate:

- first frame accessible
- middle frame accessible
- final frame accessible
- frame count consistent
- timestamp lookup works
- index lookup works

Do not access private FrameBuffer internals if public APIs exist.

============================================================
STEP 17 — FRAME INDEX INTEGRITY
============================================================

Agent 10.10 already provides FrameIndex.

Validate representative and boundary lookups:

    first timestamp
    middle timestamp
    final timestamp
    before start
    after end

Verify:

    timestamp → frame index

is deterministic.

Do not build another index.

============================================================
STEP 18 — SNAPSHOT INDEX INTEGRITY
============================================================

Agent 10.10 already provides SnapshotIndex.

Validate:

- baseline exists
- baseline belongs to correct replay
- checkpoints reference valid frame indexes
- checkpoints belong to current replay
- no invalid checkpoint indexes
- baseline cannot be incorrectly evicted

Do not modify snapshot policy.

============================================================
STEP 19 — STATE CACHE VALIDATION
============================================================

Use existing ReplayStateCache.

Perform representative reconstruction checks.

Example:

    frame 0
    frame middle
    frame final

Verify:

    reconstruct_to_index(i)

returns valid state.

Do not implement a second reconstruction algorithm.

============================================================
STEP 20 — RECONSTRUCTION INTEGRITY
============================================================

For selected frames:

    direct/normal reconstruction
           vs
    checkpoint-assisted reconstruction

must produce equivalent state.

Use existing APIs.

The validator may perform:

    full reconstruction

for a small deterministic test sample.

Do NOT perform full O(N²) reconstruction on large recordings.

============================================================
STEP 21 — RECONSTRUCTION SAMPLE POLICY
============================================================

For large recordings use bounded sampling.

At minimum test:

    first frame
    25%
    50%
    75%
    final frame

If recording has fewer than five frames, test all frames.

Allow configuration:

    validation_sample_count

Do not hard-code expensive full-session validation.

============================================================
STEP 22 — REPLAY STATE VALIDATION
============================================================

Verify replay state transitions remain valid.

Test through existing ReplayService:

    load
    play
    pause
    resume
    stop
    reset

where appropriate.

Do not duplicate the state machine.

============================================================
STEP 23 — PLAYBACK VALIDATION
============================================================

Validate that playback can advance through representative frames.

Use existing:

    tick(delta)

Do not use wall-clock sleep.

Do not create background threads.

Example:

    load
    play
    tick(...)
    pause

Verify:

- position advances
- position remains within boundaries
- resulting state is valid
- synchronization remains valid

============================================================
STEP 24 — PLAYBACK BOUNDARY VALIDATION
============================================================

Validate:

    start
    middle
    end

during playback.

Verify playback cannot move:

    below start
    above end

============================================================
STEP 25 — PLAYBACK STATE PRESERVATION
============================================================

Verify:

    PAUSED → validation → PAUSED

Validation must NOT alter replay state.

If validation requires temporary replay movement:

    preserve original state and position

and restore it safely.

Prefer validation methods that do not mutate runtime state.

If mutation is unavoidable, restore:

- cursor
- state
- timeline
- synchronization
- cache state

before returning.

============================================================
STEP 26 — SEEK VALIDATION
============================================================

Use Agent 10.12 NavigationService.

Validate:

    jump_to_start
    jump_to_end
    relative seek
    timestamp seek

Verify actual positions remain valid.

Do not call Timeline directly.

============================================================
STEP 27 — EVENT SYSTEM VALIDATION
============================================================

Agent 10.11 already provides EventStore/EventIndex.

Validate:

- event indexes reference valid replay
- event timestamps fall within replay bounds
- event frame indexes are valid where provided
- event ordering is deterministic
- no duplicate deterministic derived event IDs
- bookmark timestamps are valid

Do not re-run event detectors unless the existing API explicitly supports
validation without mutation.

============================================================
STEP 28 — EVENT TIMESTAMP VALIDATION
============================================================

For every indexed event or bounded sample:

    replay_start <= event.timestamp <= replay_end

If not:

    ERROR

Events from another replay ID:

    ERROR

============================================================
STEP 29 — BOOKMARK VALIDATION
============================================================

Validate:

- bookmark replay_id
- bookmark timestamp
- bookmark frame index where present
- bookmark timestamp within replay bounds
- referenced frame exists if frame-index based

User bookmarks must not be silently deleted or changed by validation.

============================================================
STEP 30 — LAP/SECTOR VALIDATION
============================================================

Where lap/sector markers exist:

Validate:

- lap numbers are sensible
- sector numbers are valid
- timestamps are ordered
- markers fall inside replay bounds
- markers reference correct replay
- frame indexes are valid

Do not create new lap/sector detectors.

If markers are absent:

    WARNING or NOT_APPLICABLE

not necessarily failure.

============================================================
STEP 31 — DETERMINISM VALIDATION
============================================================

This is a core requirement.

Run the same replay reconstruction sequence twice.

Example:

    frame 0
    frame 25%
    frame 50%
    frame 75%
    frame end

Capture deterministic state fingerprints.

Compare:

    run A
    run B

Expected:

    identical

If deterministic state cannot be safely hashed using existing canonical
serialization, use a stable serialization representation.

Do not use Python's built-in hash() because it is not stable across processes.

============================================================
STEP 32 — STATE FINGERPRINT
============================================================

Create a stable fingerprint mechanism only if one does not already exist.

Preferred:

    canonical serialization
          ↓
    SHA-256

The fingerprint must be:

- deterministic
- independent of object memory address
- independent of dictionary insertion order
- independent of process hash randomization

Do NOT claim cryptographic authenticity.

This is an integrity/determinism fingerprint, not a security signature.

============================================================
STEP 33 — CROSS-RUN VALIDATION
============================================================

Validate:

    same recording
    same replay
    same navigation sequence

produces:

    same positions
    same frame indexes
    same reconstructed state fingerprints
    same event ordering
    same synchronization results

============================================================
STEP 34 — PLAYBACK REPRODUCIBILITY
============================================================

Execute a deterministic sequence such as:

    load
    jump_to_start
    play
    tick(...)
    tick(...)
    pause
    seek(...)
    step_forward
    step_backward
    jump_to_event
    jump_to_bookmark
    jump_to_end
    rewind

Run it twice.

Compare final state.

Use existing Controller/Navigation APIs.

Do not bypass architecture.

============================================================
STEP 35 — SYNCHRONIZATION VALIDATION
============================================================

After representative operations verify:

    ReplayService position
          ≈
    Timeline position
          ≈
    synchronization status

Use existing tolerance:

    1ms

unless configuration defines another value.

Do not create another synchronization tolerance.

============================================================
STEP 36 — SYNCHRONIZATION DRIFT
============================================================

Validation should detect:

- timeline drift
- runtime timestamp mismatch
- cache runtime mismatch
- invalid replay ID

Use existing Synchronizer status.

Do not implement another drift detector.

============================================================
STEP 37 — RECORDING MUTATION PROTECTION
============================================================

Validation must be read-only wherever possible.

It must NOT:

- alter telemetry frames
- alter EventStore
- alter BookmarkStore
- alter FrameBuffer
- alter snapshots
- alter replay recording
- alter database records
- delete invalid data

If a validation test needs temporary state, isolate it.

============================================================
STEP 38 — VALIDATION MODE
============================================================

Provide:

    validate(replay_id)

or equivalent based on existing architecture.

Possible modes:

    QUICK
    STANDARD
    FULL

Preferred semantics:

QUICK:
    structural checks + boundaries

STANDARD:
    structural + sampled reconstruction + playback + synchronization

FULL:
    comprehensive validation, potentially all frames where safe

Do not make FULL prohibitively expensive without clear documentation.

If the project does not need modes, use configuration-driven sampling instead.

============================================================
STEP 39 — VALIDATION OPTIONS
============================================================

Potential settings:

    validation_sample_count
    validation_max_frames
    validate_events
    validate_bookmarks
    validate_determinism
    validate_playback
    validate_synchronization

Reuse project configuration conventions.

No hard-coded absolute paths.

============================================================
STEP 40 — PERFORMANCE
============================================================

Validation must be bounded.

Do not accidentally implement:

    O(N²)

for a large historical recording.

Avoid:

    reconstruct every frame from frame zero

unless FULL mode explicitly requests it and the recording is within safe
configured limits.

Use:

- FrameIndex
- SnapshotIndex
- EventIndex
- existing reconstruction
- bounded sampling

============================================================
STEP 41 — VALIDATION REPORT
============================================================

The final report must clearly distinguish:

    PASS
    WARNING
    FAIL

Example:

    Recording structure        PASS
    Timestamp integrity       PASS
    Frame integrity            PASS
    Telemetry integrity        WARNING
    Reconstruction             PASS
    Synchronization            PASS
    Events                     PASS
    Bookmarks                  PASS
    Determinism                PASS
    Playback                   PASS

Overall:

    PASSED_WITH_WARNINGS

if warnings exist but no errors.

============================================================
STEP 42 — ERROR HANDLING
============================================================

Create structured exceptions only where existing hierarchy does not cover
the requirement.

Potential:

    ReplayValidationError
    RecordingIntegrityError
    PlaybackValidationError
    DeterminismValidationError

Do not throw raw exceptions for normal validation failures.

Validation failures should normally become report entries.

============================================================
STEP 43 — VALIDATION STATUS
============================================================

Expose read-only status:

    validation_status()

Possible fields:

- replay_id
- status
- last_validation_time
- last_result
- last_error_count
- last_warning_count
- validation_duration_ms

Do not persist validation status unless the existing architecture requires it.

In-memory status is acceptable for this agent.

============================================================
STEP 44 — CONTROLLER INTEGRATION
============================================================

Do NOT overload ReplayApplicationController with validation logic.

Preferred:

    ReplayApplicationController
             │
             └── ReplayValidationService

or:

    ReplayValidationService
             ↓
       existing public APIs

The controller should expose a thin façade if protocol-level validation
commands are required.

============================================================
STEP 45 — PROTOCOL
============================================================

Inspect existing protocol conventions.

Only add commands if the architecture needs them.

Possible:

    ValidateReplay

Possible events:

    ReplayValidationStarted
    ReplayValidationCompleted
    ReplayValidationFailed

Possible response:

    ReplayValidationResult

Do not add transport.

============================================================
STEP 46 — REST/WEBSOCKET
============================================================

DO NOT implement:

- REST
- WebSocket
- HTTP endpoints
- Unity UI

Those belong to the transport/presentation phase.

============================================================
STEP 47 — DATABASE
============================================================

Do NOT introduce new database tables for validation.

Do not create migrations.

Do not add validation persistence unless the existing specification explicitly
requires it.

The validation layer should work against loaded replay data.

============================================================
STEP 48 — TESTS
============================================================

Create:

    tests/runtime/replay_validation/

or follow existing conventions.

============================================================
TEST GROUP 1 — VALID RECORDING
============================================================

Build a valid historical replay.

Expected:

    PASSED

============================================================
TEST GROUP 2 — EMPTY RECORDING
============================================================

Expected:

    FAILED

with structured error.

============================================================
TEST GROUP 3 — TIMESTAMP ORDER
============================================================

Inject:

    1000
    2000
    1500

Expected:

    FAILED

============================================================
TEST GROUP 4 — EQUAL TIMESTAMPS
============================================================

Where equal timestamps are legal:

    1000
    1000
    1020

Expected:

    PASS

Do not reject equal timestamps unless the canonical model explicitly
requires strict ordering.

============================================================
TEST GROUP 5 — NEGATIVE TIMESTAMP
============================================================

If canonical domain disallows it:

    FAILED

============================================================
TEST GROUP 6 — INVALID NUMERIC VALUES
============================================================

Test:

- NaN
- infinity

Expected structured validation failures.

============================================================
TEST GROUP 7 — FRAME INDEX
============================================================

Test invalid frame references.

============================================================
TEST GROUP 8 — REPLAY BOUNDARIES
============================================================

Test:

- valid first frame
- valid final frame
- invalid event before start
- invalid event after end

============================================================
TEST GROUP 9 — SESSION IDENTITY
============================================================

Inject mixed session IDs.

Expected:

    FAILED

============================================================
TEST GROUP 10 — SOURCE PROVIDER
============================================================

Test valid/invalid canonical source provider values according to existing
contract.

============================================================
TEST GROUP 11 — FRAME INDEX LOOKUPS
============================================================

Test:

    first
    middle
    final
    before start
    after end

============================================================
TEST GROUP 12 — SNAPSHOT INDEX
============================================================

Test:

- baseline
- checkpoints
- invalid checkpoint
- wrong replay ID

============================================================
TEST GROUP 13 — RECONSTRUCTION
============================================================

Compare checkpoint-assisted reconstruction with normal reconstruction.

Expected:

    equivalent state

============================================================
TEST GROUP 14 — PLAYBACK
============================================================

Test:

    load
    play
    tick
    pause

Verify:

- position advances
- state valid
- boundaries respected

============================================================
TEST GROUP 15 — SEEK
============================================================

Test:

- start
- middle
- end
- relative seek
- timestamp seek

============================================================
TEST GROUP 16 — DETERMINISM
============================================================

Run the same reconstruction twice.

Expected identical fingerprints.

============================================================
TEST GROUP 17 — PLAYBACK REPRODUCIBILITY
============================================================

Run the same command/navigation sequence twice.

Expected:

    identical final state

============================================================
TEST GROUP 18 — SYNCHRONIZATION
============================================================

Verify:

    replay position
    timeline position
    synchronization status

remain aligned within configured tolerance.

============================================================
TEST GROUP 19 — EVENTS
============================================================

Validate event indexes.

Check:

- timestamps
- frame references
- replay ID
- ordering
- deterministic IDs

============================================================
TEST GROUP 20 — BOOKMARKS
============================================================

Validate:

- replay ID
- timestamp
- frame
- bounds

============================================================
TEST GROUP 21 — LAP/SECTOR
============================================================

Where markers exist:

- ordering
- bounds
- frame references

Where markers do not exist:

    NOT_APPLICABLE or WARNING

============================================================
TEST GROUP 22 — NAVIGATION
============================================================

Use Agent 10.12:

    jump_to_start
    jump_to_end
    fast_forward
    rewind
    jump_to_event
    jump_to_bookmark
    jump_to_lap

Verify valid positions.

============================================================
TEST GROUP 23 — READ-ONLY
============================================================

Capture replay state before validation.

Run validation.

Verify:

- position unchanged
- replay state unchanged
- event store unchanged
- bookmark store unchanged
- telemetry unchanged

============================================================
TEST GROUP 24 — ISOLATION
============================================================

Validate:

    Replay A

while Replay B exists.

Verify no cross-replay references.

============================================================
TEST GROUP 25 — REPORT
============================================================

Verify:

- pass count
- warning count
- failure count
- status
- check details
- duration
- replay ID

============================================================
TEST GROUP 26 — VALIDATION MODES
============================================================

If QUICK/STANDARD/FULL are implemented:

verify each mode.

Ensure FULL does not accidentally run unbounded work beyond configured
limits.

============================================================
TEST GROUP 27 — CONTROLLER
============================================================

If controller integration is implemented:

    command
      ↓
    dispatcher
      ↓
    controller
      ↓
    validator

Verify no validation logic is embedded in protocol parsing.

============================================================
TEST GROUP 28 — PROTOCOL
============================================================

If protocol additions exist:

test serialization/deserialization/catalogue registration.

============================================================
TEST GROUP 29 — REGRESSION
============================================================

Run all relevant tests from:

- Agent 10.6
- Agent 10.7
- Agent 10.8
- Agent 10.9
- Agent 10.10
- Agent 10.11
- Agent 10.12
- providers
- normalization
- event bus
- timeline
- replay

Fix regressions caused by Agent 10.13.

============================================================
STEP 49 — COVERAGE
============================================================

Target:

    >= 80%

for the new validation package.

Prefer:

    >= 85%

if practical.

Do not sacrifice architecture solely to increase coverage.

============================================================
STEP 50 — CODE QUALITY
============================================================

Follow RaceVision standards:

- Python 3.11
- PEP 8
- complete type hints
- dependency inversion
- deterministic behavior
- no global mutable state
- no circular imports
- immutable result models where appropriate
- structured logging
- structured errors

Run repository-standard:

- formatter
- Ruff
- type checking
- tests
- coverage

Discover exact commands from:

- pyproject.toml
- Makefile
- CI configuration
- scripts

============================================================
STEP 51 — DOCUMENTATION
============================================================

Create:

    docs/specifications/ReplayRecordingPlaybackValidationSpecification.md

unless an equivalent specification already exists.

Document:

- purpose
- architecture
- validation categories
- recording integrity
- timestamp validation
- frame validation
- telemetry validation
- session validation
- reconstruction validation
- playback validation
- synchronization validation
- event validation
- bookmark validation
- determinism
- fingerprints
- validation modes
- sampling
- performance
- errors
- read-only guarantees
- report format

Update:

    docs/specifications/README.md

Update:

    docs/Replay.md

Update:

    docs/Roadmap.md

============================================================
STEP 52 — ROADMAP
============================================================

Mark:

    Agent 10.13 ✓

ONLY after:

- implementation complete
- tests pass
- coverage passes
- Ruff passes
- documentation updated
- regression suite passes

============================================================
STEP 53 — SECURITY / INTEGRITY BOUNDARY
============================================================

The SHA-256 fingerprint is for:

    deterministic comparison
    replay integrity diagnostics

It is NOT:

    a cryptographic signature
    proof of authenticity
    proof that data came from Formula 1
    proof of untampered source data

Do not make unsupported security claims.

============================================================
STEP 54 — PERFORMANCE GUARDRAILS
============================================================

Never accidentally perform:

    every frame × full reconstruction

for normal validation.

Use bounded sampling.

For example:

    first
    quarter
    middle
    three-quarter
    final

and configurable samples.

FULL mode may perform more extensive checks only under explicit limits.

============================================================
STEP 55 — ARCHITECTURAL GUARDRAILS
============================================================

DO NOT:

- rewrite ReplayService
- rewrite ReplayEngine
- rewrite ReplayClock
- rewrite State Cache
- rewrite Synchronizer
- rewrite Event System
- rewrite Navigation
- create another telemetry provider
- create another normalizer
- create another FrameIndex
- create another SnapshotIndex
- create another EventIndex
- mutate historical telemetry during validation
- create database migrations
- create REST
- create WebSocket
- create Unity UI
- create OBS integration
- add Redis
- add unnecessary infrastructure

============================================================
STEP 56 — ACCEPTANCE CRITERIA
============================================================

Agent 10.13 is COMPLETE only when:

[ ] Validation package exists.
[ ] Recording existence is validated.
[ ] Frame count is validated.
[ ] Timestamp integrity is validated.
[ ] Frame ordering is validated.
[ ] Timestamp gaps are reported.
[ ] Canonical telemetry integrity is validated.
[ ] Numeric validity is checked.
[ ] Session identity is validated.
[ ] Participant references are validated where applicable.
[ ] Recording boundaries are validated.
[ ] FrameBuffer integrity is validated.
[ ] FrameIndex integrity is validated.
[ ] SnapshotIndex integrity is validated.
[ ] State Cache reconstruction is validated.
[ ] Checkpoint reconstruction matches normal reconstruction.
[ ] Playback can be validated.
[ ] Playback boundaries are validated.
[ ] Seek/navigation can be validated.
[ ] Event indexes are validated.
[ ] Bookmark indexes are validated.
[ ] Lap/sector markers are validated where available.
[ ] Replay synchronization is validated.
[ ] Deterministic state fingerprints are implemented where needed.
[ ] Repeated reconstruction is deterministic.
[ ] Repeated playback/navigation is deterministic.
[ ] Validation is read-only.
[ ] Validation report exists.
[ ] PASS/WARNING/FAIL semantics exist.
[ ] Structured validation errors exist.
[ ] Validation status exists.
[ ] Configuration is implemented where required.
[ ] No second replay engine exists.
[ ] No second reconstruction engine exists.
[ ] No second EventIndex exists.
[ ] No second State Cache exists.
[ ] No transport layer is implemented.
[ ] No new database schema is required.
[ ] Tests added.
[ ] Validation tests pass.
[ ] Phase 10.6–10.12 regression tests pass.
[ ] Coverage meets project gate.
[ ] Ruff passes.
[ ] Type checking passes where configured.
[ ] Documentation updated.
[ ] Roadmap updated.

============================================================
STEP 57 — FINAL REPORT
============================================================

When complete, report:

1. Files created.
2. Files modified.
3. Validation architecture.
4. Validation categories.
5. Recording integrity checks.
6. Timestamp checks.
7. Frame checks.
8. Telemetry checks.
9. Session checks.
10. Boundary checks.
11. FrameIndex validation.
12. SnapshotIndex validation.
13. State Cache validation.
14. Reconstruction validation.
15. Playback validation.
16. Seek/navigation validation.
17. Synchronization validation.
18. Event validation.
19. Bookmark validation.
20. Lap/sector validation.
21. Determinism validation.
22. Fingerprint implementation.
23. Read-only guarantees.
24. Validation modes/sampling.
25. Performance characteristics.
26. Error handling.
27. Report/status model.
28. Protocol changes, if any.
29. Controller integration, if any.
30. Tests added.
31. Full test results.
32. Coverage.
33. Ruff/type-check results.
34. Documentation updated.
35. Roadmap status.
36. Known limitations.
37. Recommended Agent 10.14.

Do NOT claim completion if required tests fail.

============================================================
START IMPLEMENTATION
============================================================

First inspect the complete implementations and tests for:

- Agent 10.6 Historical Telemetry Provider
- Agent 10.7 Replay Runtime Core
- Agent 10.8 Replay Controller
- Agent 10.9 Replay Synchronization
- Agent 10.10 Replay State Cache
- Agent 10.11 Replay Bookmark & Event System
- Agent 10.12 Replay Seeking & Time Navigation

Then inspect the current repository implementation.

Implement Agent 10.13 completely.

Build on the existing architecture.

Do not rewrite working functionality.

Keep validation read-only.

Run tests after implementation.

Fix failures caused by the implementation.

Update specifications, Replay documentation and Roadmap.

Only then provide the final implementation report.
```

## User

**Agent 10.13 is complete.** Historical replay validation is a read-only observer over Agents 10.7–10.12; no second replay engine.

### Architecture

`ReplayValidationService` → recording / timestamp / telemetry / indexes / reconstruction / playback / nav / sync / events / bookmarks → `ReplayValidationReport`
Controller/protocol: `ValidateReplay` → thin `validate_replay()` façade.

### Created

- `backend/runtime/replay/validation/` (`replay_validator`, enums, result, fingerprint, sampling, exceptions)
- `docs/specifications/ReplayRecordingPlaybackValidationSpecification.md`
- `tests/runtime/replay_validation/`

### Modified

- Settings toggles + sampling on `ReplayRuntimeSettings`
- Controller / dispatcher / protocol `ValidateReplay`
- `docs/Replay.md`, `docs/Roadmap.md` (10.13 ✓), specs README, replay `__init__` exports

### Key behavior

- Source timestamps (not only clamped `position_ms`) for regression detection; equals allowed; large gaps → WARNING
- Semantic SHA-256 fingerprints for determinism / checkpoint vs full reconstruction
- Config-driven sampling (no QUICK/STANDARD/FULL); state restored after mutating checks
- In-memory `validation_status()` only — no DB/transport

### Quality

| Gate                         | Result         |
| ---------------------------- | -------------- |
| Validation tests             | **22 passed**  |
| Replay 10.7–10.13 regression | **109 passed** |
| FastF1                       | **20 passed**  |
| Coverage (validation pkg)    | **82.84%**     |
| Ruff                         | clean          |
| mypy (`validation/`)         | clean          |

### Known limits

Live Cache raw snapshots aren’t bit-identical after checkpoint restore; equivalence uses durable session fields. Validation is best-effort restore if seek fails.

### Recommended Agent 10.14

Replay **transport / presentation** (REST/WebSocket façades) — your choice.

## Assistant

**Agent 10.13 is accepted as complete.** The implementation matches the intended architecture, and the reported quality gates are sufficient.

### Phase 10 replay status

| Agent | Component | Status |
|---|---|---|
| 10.6 | Historical Telemetry Provider | ✅ |
| 10.7 | Replay Runtime Core | ✅ |
| 10.8 | Replay Controller | ✅ |
| 10.9 | Replay Synchronization | ✅ |
| 10.10 | Replay State Cache | ✅ |
| 10.11 | Replay Bookmark & Event System | ✅ |
| 10.12 | Replay Seeking & Time Navigation | ✅ |
| **10.13** | **Replay Recording/Playback Validation** | **✅** |

### Why 10.13 is architecturally correct

The important part is:

```text
              Replay Runtime
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
   Normal Operation      Validation Observer
        │                     │
        │              ┌──────┴──────┐
        │              │             │
        │          Recording      Playback
        │          Integrity     Integrity
        │              │             │
        │              └──────┬──────┘
        │                     ▼
        └──────────────► ValidationReport
```

There is **one authoritative replay runtime**.

The validator observes it rather than creating a competing implementation.

### The strongest parts

**Source timestamp validation**

Using the actual source timestamps rather than only the replay's clamped `position_ms` is the right decision. It means corrupted/backwards historical timestamps can actually be detected.

**Deterministic fingerprints**

Using semantic SHA-256 fingerprints gives you a reproducible comparison mechanism without falsely claiming cryptographic authenticity.

**Checkpoint validation**

The validator is checking the existing Agent 10.10 checkpoint/reconstruction mechanism rather than implementing another reconstruction algorithm.

**Read-only design**

This is particularly important:

> `validation_status()` is in-memory and there is no new DB persistence.

That keeps 10.13 from becoming an unnecessary persistence subsystem.

**State restoration**

Because some validation operations temporarily move replay state, restoring the original position/state afterward is essential. The reported implementation addresses that.

### Quality gates

- **22 validation tests** ✅
- **109 replay 10.7–10.13 regression tests** ✅
- **20 FastF1 tests** ✅
- **82.84% validation coverage** ✅
- **Ruff clean** ✅
- **mypy clean** ✅

That is a solid completion point.

### Known limitation

The raw Live Cache snapshots aren't guaranteed to be byte-identical after checkpoint restoration.

That's **not necessarily a defect**. If the cache contains transient/runtime fields, comparing durable semantic state is the more appropriate validation strategy.

The important invariant is:

```text
same replay
    +
same frame
    +
same deterministic reconstruction
        ↓
equivalent canonical runtime state
```

rather than:

```text
byte-for-byte identical Python/cache object
```

### Phase 10 is now moving toward presentation

The current architecture is effectively:

```text
Historical Data
      │
      ▼
 Historical Provider
      │
      ▼
 Canonical Telemetry
      │
      ▼
 ┌─────────────────────────────┐
 │       Replay Runtime        │
 │                             │
 │ Clock                       │
 │ Frames                      │
 │ State Cache                 │
 │ Synchronization             │
 │ Events / Bookmarks           │
 │ Navigation                  │
 │ Validation                  │
 └──────────────┬──────────────┘
                │
                ▼
        Controller / Protocol
                │
                ▼
          [Next: Transport]
                │
       ┌────────┴────────┐
       ▼                 ▼
     REST            WebSocket
       │                 │
       └────────┬────────┘
                ▼
       Unity / Web UI / OBS
```

So **10.14 should not add more replay internals unless a concrete gap is discovered**.

The natural next boundary is indeed **Agent 10.14 — Replay Transport / Presentation**, exposing the existing `ReplayApplicationController`, navigation, validation, events and status through thin REST/WebSocket adapters. memcite

## User

Please give commands for Agent 10.14	Live Session Adapter	Connect live sessions into the unified Session Runtime ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. **Agent 10.14 should bridge live sessions into the existing unified Session Runtime**, not create a separate live runtime. It should complement Agent 10.6's historical provider and make live + historical sessions share the same canonical runtime path.

Copy/paste this entire block into Cursor:

```text
You are the Principal Distributed Systems Architect and Senior Python Engineer working on the RaceVision project.

============================================================
RACEVISION — AGENT 10.14
LIVE SESSION ADAPTER
============================================================

OBJECTIVE
---------

Implement Agent 10.14 — Live Session Adapter.

The purpose of this agent is to connect LIVE telemetry sessions into the
existing unified Session Runtime.

The architectural goal is:

    LIVE SESSION
         │
         ▼
    Live Session Adapter
         │
         ▼
    Canonical Telemetry
         │
         ▼
    Unified Session Runtime
         │
    ┌────┼───────────────┐
    ▼    ▼               ▼
 Timeline Cache      Event Bus
    │
    ▼
 Streaming / API / Replay / Presentation

Historical replay and live telemetry MUST converge on the same runtime
abstractions wherever the existing architecture allows.

This agent must NOT create a second runtime.

============================================================
CRITICAL ARCHITECTURAL PRINCIPLE
============================================================

RaceVision must have ONE unified Session Runtime.

Historical:

    Historical Provider
          ↓
    Canonical Frames
          ↓
    Unified Session Runtime

Live:

    Live Session Adapter
          ↓
    Canonical Frames
          ↓
    Unified Session Runtime

Both paths must converge as early as practical.

Do NOT implement:

    LiveRuntime

    LiveReplayRuntime

    LiveSessionRuntime

    LiveTelemetryEngine

or any other parallel runtime.

The adapter is a boundary adapter.

============================================================
EXISTING ARCHITECTURE — READ FIRST
============================================================

Before writing code, inspect the complete repository implementation.

Read:

- docs/Roadmap.md
- docs/Replay.md
- docs/Telemetry.md
- docs/Architecture.md
- docs/specifications/SoftwareRequirementsSpecification.md
- docs/specifications/SystemArchitectureSpecification.md
- docs/specifications/HistoricalTelemetryProviderSpecification.md
- docs/specifications/ReplayRuntimeCoreSpecification.md
- docs/specifications/ReplayControllerSpecification.md
- docs/specifications/ReplaySynchronizationSpecification.md
- docs/specifications/ReplayStateCacheSpecification.md
- docs/specifications/ReplayBookmarkEventSystemSpecification.md
- docs/specifications/ReplaySeekingTimeNavigationSpecification.md
- docs/specifications/ReplayRecordingPlaybackValidationSpecification.md

Inspect:

    backend/runtime/
    backend/providers/
    backend/normalization/
    backend/protocol/
    backend/telemetry/
    backend/services/
    backend/models/
    backend/database/
    shared/protocols/
    configuration

Especially inspect the actual implementations of:

    Session Runtime
    Session Manager
    Session lifecycle
    Runtime state
    Timeline
    State Cache
    Event Bus
    ProviderManager
    BaseProvider
    FastF1 provider
    canonical telemetry models
    ingestion
    normalization
    repositories
    Unit of Work
    configuration
    health checks

Search repository-wide for:

    SessionRuntime
    SessionManager
    SessionService
    session
    live
    realtime
    provider
    telemetry
    ingestion
    normalize
    canonical
    event_bus
    timeline
    cache
    lifecycle
    RuntimeMode
    SessionState
    RaceSession
    SessionParticipant

The repository is the source of truth.

============================================================
STEP 1 — DETERMINE EXISTING UNIFIED SESSION RUNTIME
============================================================

Before implementation identify the existing authoritative runtime abstraction.

Do NOT assume its name.

It may be:

    SessionRuntime
    RuntimeSession
    SessionManager
    RuntimeManager
    another existing abstraction

Use the existing implementation.

If the repository already has a unified runtime:

    adapt into it.

If there is a partially implemented runtime:

    complete only the minimum integration required.

Do NOT redesign the entire runtime during this agent.

============================================================
STEP 2 — DEFINE RESPONSIBILITY
============================================================

Agent 10.14 owns:

    LIVE PROVIDER → SESSION RUNTIME ADAPTER

It is responsible for:

- live session lifecycle
- connecting a live provider
- receiving live telemetry
- translating provider data into canonical frames
- forwarding canonical data into the existing runtime
- disconnect/reconnect lifecycle
- health/status
- backpressure handling
- sequence/timestamp validation
- duplicate handling
- graceful shutdown
- provider failure handling

It is NOT responsible for:

- rendering
- Unity
- OBS
- Twitch
- Kick
- YouTube
- replay
- historical reconstruction
- replay snapshots
- replay navigation
- database schema redesign
- AI commentary
- race strategy analysis
- physics simulation

============================================================
STEP 3 — LIVE VS HISTORICAL
============================================================

The existing historical path is approximately:

    HistoricalTelemetryRequest
             ↓
       FastF1Provider
             ↓
       Canonical Frames
             ↓
        Runtime / Replay

The new live path should be:

    LiveSessionRequest
             ↓
       LiveSessionAdapter
             ↓
       Live Provider
             ↓
       Canonical Frames
             ↓
       Unified Session Runtime

Do not bypass canonical normalization.

============================================================
STEP 4 — PROVIDER ABSTRACTION
============================================================

Inspect the existing provider interfaces.

If a common provider interface exists, reuse it.

Preferred conceptual model:

    BaseProvider
         │
    ┌────┴─────────────┐
    ▼                  ▼
Historical Provider  Live Provider
    │                  │
    └────────┬─────────┘
             ▼
       Canonical Data
             │
             ▼
      Unified Runtime

Do not make the Runtime know provider-specific packet formats.

============================================================
STEP 5 — LIVE SESSION PACKAGE
============================================================

Create an appropriate package based on repository conventions.

Preferred:

    backend/runtime/live/

or:

    backend/runtime/session/live/

or another existing live-session package if already present.

Potential structure:

    __init__.py
    adapter.py
    session.py
    request.py
    state.py
    lifecycle.py
    health.py
    sequence.py
    backpressure.py
    exceptions.py
    status.py

Do NOT blindly create every file.

Use the smallest clean architecture consistent with the repository.

============================================================
STEP 6 — LIVE SESSION REQUEST
============================================================

Create a strongly typed request model if one does not already exist.

Possible fields:

    session_id
    season
    event
    session_type
    provider
    mode
    auto_start
    reconnect
    reconnect_attempts
    timeout
    buffer_size

Only include fields supported by existing configuration/provider architecture.

No credentials in request objects.

No secrets in logs.

============================================================
STEP 7 — LIVE SESSION STATES
============================================================

Use the existing session lifecycle if one exists.

Do NOT create a conflicting state machine.

If necessary, support states conceptually equivalent to:

    DISCONNECTED
    CONNECTING
    CONNECTED
    RUNNING
    RECONNECTING
    STOPPING
    STOPPED
    FAILED

Reuse existing enums where available.

============================================================
STEP 8 — LIFECYCLE
============================================================

Implement:

    start()
    connect()
    stop()
    disconnect()
    shutdown()

where these responsibilities do not already exist.

Lifecycle must be idempotent.

Examples:

    stop()
    stop()

must not crash.

Likewise:

    disconnect()
    disconnect()

must be safe.

============================================================
STEP 9 — LIVE DATA FLOW
============================================================

The intended flow is:

    provider
       ↓
    raw live packet
       ↓
    adapter
       ↓
    canonical telemetry
       ↓
    existing normalization/validation
       ↓
    unified Session Runtime
       ↓
    event bus
       ↓
    cache/timeline/subscribers

Do not send raw provider packets into the Runtime.

============================================================
STEP 10 — CANONICAL TELEMETRY
============================================================

Identify the project's canonical telemetry model.

Do not create a competing canonical model.

Live frames must conform to the same canonical representation used by:

- historical telemetry
- runtime ingestion
- replay
- normalization
- state cache
- event processing

Where possible:

    same model
    same identifiers
    same timestamps
    same source metadata

============================================================
STEP 11 — LIVE NORMALIZATION
============================================================

Use the existing normalization pipeline.

Do not create:

    LiveNormalizer

unless the repository architecture explicitly requires a provider-specific
translator.

Preferred:

    raw live packet
         ↓
    provider translator
         ↓
    canonical frame
         ↓
    existing normalization/validation
         ↓
    runtime

============================================================
STEP 12 — PROVIDER TRANSLATION
============================================================

Provider-specific logic must remain at the provider boundary.

If a live provider supplies:

    provider-specific packet

translate it into the existing canonical model.

Do not leak:

    provider_packet
    provider_field_name
    provider-specific enums

into the Session Runtime.

============================================================
STEP 13 — LIVE PROVIDER IMPLEMENTATION
============================================================

Inspect the repository for an existing live provider.

If one exists:

    adapt it.

If a live provider interface exists but concrete implementation is intentionally
not available:

    implement an adapter boundary and deterministic in-memory test provider.

Do NOT invent credentials or pretend an external live feed is available.

Do NOT hard-code a proprietary F1 feed.

If the current repository already defines the licensed/live source boundary,
use it.

============================================================
STEP 14 — IN-MEMORY LIVE PROVIDER
============================================================

For offline tests, provide or reuse an in-memory provider.

It should support:

    connect()
    disconnect()
    publish(frame)
    publish_many(frames)
    stream()

or equivalent repository conventions.

This is a TEST DOUBLE.

It must never be treated as the production F1 feed.

============================================================
STEP 15 — SEQUENCE NUMBERS
============================================================

If live packets provide sequence numbers:

validate:

    monotonic sequence

Detect:

    duplicate sequence
    backwards sequence
    missing sequence

Do NOT automatically treat every missing sequence as fatal.

A dropped packet may be expected in a live stream.

Use:

    WARNING

for recoverable gaps unless the existing contract defines them as fatal.

============================================================
STEP 16 — DUPLICATE HANDLING
============================================================

Live systems can produce duplicate packets.

Implement deterministic duplicate detection using existing identifiers where
available:

    sequence
    packet ID
    timestamp + source identity

Do NOT deduplicate using arbitrary object equality.

Duplicate packets should not create duplicate runtime state/events.

============================================================
STEP 17 — TIMESTAMP VALIDATION
============================================================

Validate live frame timestamps against existing canonical rules.

Expected:

    non-decreasing source timestamps

Equal timestamps may be legal.

Backwards timestamps should produce a structured error/warning according to
existing telemetry policy.

Do NOT silently rewrite source timestamps.

============================================================
STEP 18 — RUNTIME TIMESTAMP
============================================================

Do not confuse:

    source timestamp

with:

    wall-clock receive time

or:

    runtime timestamp

Preserve source timestamp.

If receive timestamp is needed:

    store separately.

Do not overwrite canonical event time with local machine time.

============================================================
STEP 19 — RECEIVE TIME
============================================================

If required by existing telemetry models, capture:

    received_at

separately from:

    telemetry_timestamp

This enables latency diagnostics without corrupting telemetry chronology.

============================================================
STEP 20 — LATENCY
============================================================

If both source and receive timestamps can be compared meaningfully:

calculate:

    ingestion latency

Expose it in health/status.

Do not make latency an invalidity condition unless existing requirements define
a hard threshold.

============================================================
STEP 21 — BACKPRESSURE
============================================================

Live data may arrive faster than the Runtime can process.

Inspect existing ingestion/backpressure infrastructure first.

Reuse it.

If none exists, implement a minimal bounded mechanism.

Possible policy:

    bounded queue
        ↓
    consumer
        ↓
    runtime

Never allow an unbounded queue.

============================================================
STEP 22 — BACKPRESSURE POLICY
============================================================

Define explicit behavior when queue capacity is reached.

Possible policies:

    DROP_OLDEST
    DROP_NEWEST
    BLOCK
    FAIL

Use the safest policy supported by existing architecture.

For telemetry streaming, document the chosen policy.

Do not silently lose data without exposing a metric/status indicator.

============================================================
STEP 23 — LIVE INGESTION LOOP
============================================================

If an asynchronous stream is required:

use existing async conventions.

Avoid:

- unmanaged background threads
- daemon threads with hidden lifecycle
- infinite loops without cancellation
- blocking the event loop
- global worker state

Support clean cancellation.

============================================================
STEP 24 — CANCELLATION
============================================================

Stopping a live session must:

1. stop accepting new packets
2. cancel/close provider stream
3. drain or explicitly discard bounded pending work according to policy
4. stop runtime ingestion
5. publish final lifecycle state
6. release resources

No hanging tasks.

============================================================
STEP 25 — RECONNECT
============================================================

Implement reconnect only if existing architecture supports it.

Required conceptual states:

    CONNECTED
        ↓
    provider failure
        ↓
    RECONNECTING
        ↓
    CONNECTED

Use bounded retries.

Configuration:

    reconnect_enabled
    max_reconnect_attempts
    reconnect_delay

Do not use infinite retry loops.

============================================================
STEP 26 — RECONNECT SEMANTICS
============================================================

During reconnect:

- preserve session identity
- preserve runtime identity
- do not create a second Session Runtime
- do not duplicate historical frames
- do not reset session state unless explicitly required
- continue sequence validation

After reconnect:

    duplicate detection remains active.

============================================================
STEP 27 — PROVIDER HEALTH
============================================================

Expose:

    provider_connected
    session_state
    last_packet_at
    last_source_timestamp
    packets_received
    packets_processed
    packets_dropped
    duplicates
    sequence_gaps
    reconnect_count
    queue_depth
    ingestion_latency

Use existing health/status conventions.

============================================================
STEP 28 — SESSION HEALTH
============================================================

Create or extend the existing session health model.

Health should distinguish:

    HEALTHY
    DEGRADED
    DISCONNECTED
    FAILED

Do not treat temporary packet loss as immediate session failure.

============================================================
STEP 29 — RUNTIME INTEGRATION
============================================================

The critical integration is:

    LiveSessionAdapter
             ↓
       Unified Session Runtime

Use existing runtime ingestion interfaces.

Do NOT call internal private methods.

Prefer:

    runtime.ingest(...)
    runtime.publish(...)
    runtime.process(...)
    runtime.accept_frame(...)

depending on actual repository APIs.

============================================================
STEP 30 — EVENT BUS
============================================================

Live frames should enter the existing Event Bus path where appropriate.

Do not create:

    LiveEventBus

Use existing Event Bus.

Potential lifecycle events:

    LiveSessionConnected
    LiveSessionDisconnected
    LiveSessionReconnecting
    LiveSessionDegraded
    LiveSessionFailed

Only add events if they fit existing protocol conventions.

============================================================
STEP 31 — TIMELINE
============================================================

Live data should update the existing Timeline if the unified Runtime already
owns Timeline updates.

Do NOT call Timeline directly from the adapter if Runtime owns that concern.

Preferred:

    Live Adapter
         ↓
    Session Runtime
         ↓
    Timeline

============================================================
STEP 32 — STATE CACHE
============================================================

Live data should flow through the existing Runtime/Cache path.

Do NOT create:

    LiveStateCache

If the existing Session Runtime owns a State Cache, feed it through that path.

============================================================
STEP 33 — LIVE SESSION IDENTITY
============================================================

A live session must have a stable:

    session_id

and, where applicable:

    race_session_id

Do not create a new session ID for every reconnect.

============================================================
STEP 34 — PARTICIPANTS
============================================================

Where the existing runtime requires:

    drivers
    cars
    teams
    session participants

resolve them through existing models/services.

Do not duplicate database entities.

============================================================
STEP 35 — DATABASE
============================================================

Use existing session repositories where the architecture requires session
metadata persistence.

Do NOT introduce new tables unless absolutely required by an existing
specification.

Do not create a separate live-session database.

Telemetry persistence must use existing telemetry persistence architecture if
already implemented.

============================================================
STEP 36 — UNIT OF WORK
============================================================

If live session metadata is persisted:

use existing:

    Repository
    UnitOfWork
    transaction

architecture.

Do not bypass the persistence layer.

============================================================
STEP 37 — LIVE VS REPLAY MODE
============================================================

The unified runtime must be able to distinguish:

    LIVE
    HISTORICAL
    REPLAY

without duplicating runtime implementations.

Reuse existing TimelineMode/RuntimeMode concepts where present.

If a mode enum already exists:

    extend it.

Do not create several competing mode enums.

============================================================
STEP 38 — TRANSITION SAFETY
============================================================

Handle:

    LIVE → STOP
    LIVE → DISCONNECTED
    LIVE → HISTORICAL
    HISTORICAL → LIVE
    LIVE → REPLAY

according to existing session lifecycle architecture.

Do not allow two active providers to feed the same session simultaneously.

============================================================
STEP 39 — SINGLE ACTIVE LIVE SOURCE
============================================================

Enforce:

    one active live provider per live session

If a second connection attempts to attach:

return a structured conflict/error.

Do not silently create duplicate ingestion paths.

============================================================
STEP 40 — LIVE SESSION ADAPTER API
============================================================

Provide a thin API such as:

    start_session()
    stop_session()
    reconnect()
    get_status()
    get_health()

Use actual project naming conventions.

Avoid exposing provider-specific details.

============================================================
STEP 41 — ADAPTER RESULT
============================================================

If the existing project uses structured results, follow that convention.

Possible result:

    LiveSessionResult

Fields:

    session_id
    state
    accepted
    message
    provider
    runtime_mode

Do not expose raw provider objects.

============================================================
STEP 42 — CONFIGURATION
============================================================

Extend existing configuration.

Possible settings:

    live_enabled
    provider
    reconnect_enabled
    max_reconnect_attempts
    reconnect_delay_seconds
    queue_size
    backpressure_policy
    packet_timeout_seconds
    health_interval_seconds

Use:

    Pydantic Settings

and existing environment configuration.

No hard-coded:

- credentials
- API keys
- URLs
- filesystem paths

============================================================
STEP 43 — SECRETS
============================================================

Never log:

- API keys
- bearer tokens
- passwords
- credentials
- provider secrets

Configuration should reference secrets through existing environment/secret
mechanisms.

============================================================
STEP 44 — PROTOCOL
============================================================

Inspect existing protocol architecture.

If appropriate, add:

    StartLiveSession
    StopLiveSession
    ReconnectLiveSession
    GetLiveSessionStatus

and corresponding events.

Only add what is needed.

Do not build REST/WebSocket transport in this agent.

============================================================
STEP 45 — CONTROLLER INTEGRATION
============================================================

If a Session Application Controller exists:

integrate through it.

Preferred:

    command
       ↓
    dispatcher
       ↓
    Session Controller
       ↓
    LiveSessionAdapter
       ↓
    Unified Session Runtime

Do not expose provider internals.

============================================================
STEP 46 — TRANSPORT
============================================================

DO NOT implement:

- REST
- WebSocket
- HTTP endpoints
- Unity UI
- OBS integration
- streaming platform integrations

Those belong to transport/presentation agents.

============================================================
STEP 47 — TEST DOUBLE
============================================================

Create/reuse an in-memory live provider for deterministic tests.

It should allow tests to:

    connect
    send frame
    send multiple frames
    duplicate frame
    skip sequence
    disconnect
    reconnect
    close

============================================================
STEP 48 — TEST: START
============================================================

Test:

    start live session

Expected:

    CONNECTED/RUNNING
    correct session ID
    runtime mode LIVE

============================================================
STEP 49 — TEST: FRAME INGESTION
============================================================

Send canonical live frames.

Verify:

    provider
      ↓
    adapter
      ↓
    runtime

and verify the Runtime receives canonical data.

============================================================
STEP 50 — TEST: NORMALIZATION
============================================================

If raw provider frames are used:

verify:

    raw
      ↓
    translator
      ↓
    canonical
      ↓
    runtime

No provider-specific object reaches the Runtime.

============================================================
STEP 51 — TEST: TIMESTAMPS
============================================================

Send:

    1000
    1010
    1020

Expected:

    all accepted

Send:

    1000
    900

Expected:

    structured warning/error according to existing policy.

============================================================
STEP 52 — TEST: DUPLICATES
============================================================

Send:

    sequence 1
    sequence 2
    sequence 2

Expected:

    sequence 2 duplicate handled deterministically.

No duplicate runtime state/event.

============================================================
STEP 53 — TEST: SEQUENCE GAP
============================================================

Send:

    1
    2
    4

Expected:

    gap detected.

Normally:

    WARNING / metric

unless existing contract says otherwise.

============================================================
STEP 54 — TEST: RECONNECT
============================================================

Test:

    connect
    frames
    disconnect
    reconnect
    frames

Expected:

- same session identity
- no second runtime
- continued operation
- sequence validation continues

============================================================
STEP 55 — TEST: PROVIDER FAILURE
============================================================

Provider throws failure.

Expected:

    RUNNING
       ↓
    RECONNECTING / FAILED

according to configured policy.

No unhandled background exception.

============================================================
STEP 56 — TEST: STOP
============================================================

Test:

    start
    frames
    stop

Verify:

- provider closed
- runtime lifecycle correct
- no new frames accepted
- resources released

============================================================
STEP 57 — TEST: IDEMPOTENT STOP
============================================================

Call:

    stop()
    stop()

Expected:

    no crash
    deterministic state

============================================================
STEP 58 — TEST: CANCELLATION
============================================================

Start stream.

Cancel/stop while waiting for packet.

Verify:

- task terminates
- provider closes
- no leaked worker
- no hanging coroutine

============================================================
STEP 59 — TEST: BACKPRESSURE
============================================================

Configure small queue.

Send more frames than capacity.

Verify selected policy:

    DROP / BLOCK / FAIL

is deterministic.

Verify metrics reflect dropped frames if applicable.

============================================================
STEP 60 — TEST: SINGLE ACTIVE SOURCE
============================================================

Attempt two live providers for same session.

Expected:

    structured conflict.

============================================================
STEP 61 — TEST: SESSION ISOLATION
============================================================

Create:

    Session A
    Session B

Send frames independently.

Verify:

    no cross-session telemetry
    no cross-session events
    no cross-session runtime state

============================================================
STEP 62 — TEST: RUNTIME MODE
============================================================

Verify live session reports:

    LIVE

while historical/replay remain:

    HISTORICAL
    REPLAY

using the project's existing mode abstraction.

============================================================
STEP 63 — TEST: TIMELINE
============================================================

If Runtime owns Timeline:

send live frames and verify Timeline updates through Runtime.

Do not directly manipulate Timeline from adapter.

============================================================
STEP 64 — TEST: EVENT BUS
============================================================

Verify live telemetry reaches existing Event Bus where expected.

Verify lifecycle events if implemented.

No second Event Bus.

============================================================
STEP 65 — TEST: CACHE
============================================================

Verify live data reaches the existing state/cache architecture.

No LiveStateCache should be created.

============================================================
STEP 66 — TEST: HEALTH
============================================================

Verify:

    packets_received
    packets_processed
    packets_dropped
    duplicates
    sequence_gaps
    last_packet_at
    last_source_timestamp
    queue_depth
    reconnect_count

are correctly reported.

============================================================
STEP 67 — TEST: LATENCY
============================================================

Where timestamps are comparable:

verify receive latency calculation.

Do not make tests dependent on exact wall-clock values.

Use controlled clocks where repository conventions allow.

============================================================
STEP 68 — TEST: PROVIDER ABSTRACTION
============================================================

Verify the adapter depends on the provider interface, not a concrete external
implementation where possible.

Use dependency injection.

============================================================
STEP 69 — TEST: NO DUPLICATE RUNTIME
============================================================

Start/reconnect repeatedly.

Verify exactly one runtime/session context is used.

============================================================
STEP 70 — TEST: DATABASE
============================================================

If session persistence is integrated:

verify existing repository/UoW behavior.

Do not add unrelated schema.

============================================================
STEP 71 — REGRESSION TESTS
============================================================

Run all relevant tests from:

- Phase 10
- Agent 10.6
- Agent 10.7
- Agent 10.8
- Agent 10.9
- Agent 10.10
- Agent 10.11
- Agent 10.12
- Agent 10.13
- providers
- normalization
- runtime
- event bus
- database
- configuration

Fix regressions caused by Agent 10.14.

============================================================
STEP 72 — COVERAGE
============================================================

Target:

    >= 80%

for the new Agent 10.14 package.

Prefer:

    >= 85%

where practical.

============================================================
STEP 73 — CODE QUALITY
============================================================

Follow RaceVision standards:

- Python 3.11
- PEP 8
- complete type hints
- dependency injection
- async-safe lifecycle
- no global mutable state
- no circular imports
- structured logging
- structured errors
- deterministic tests
- bounded queues
- explicit cancellation

Run repository-standard:

- Ruff
- mypy/type checker if configured
- tests
- coverage

Discover exact commands from:

- pyproject.toml
- Makefile
- CI
- scripts

============================================================
STEP 74 — DOCUMENTATION
============================================================

Create:

    docs/specifications/LiveSessionAdapterSpecification.md

Document:

- purpose
- architecture
- unified runtime integration
- provider abstraction
- lifecycle
- live session states
- canonical telemetry
- normalization
- sequence handling
- duplicate handling
- timestamps
- receive time
- latency
- backpressure
- reconnect
- health
- runtime integration
- Event Bus
- Timeline
- State Cache
- configuration
- error handling
- shutdown
- isolation
- testing
- limitations

Update:

    docs/specifications/README.md

Update:

    docs/Telemetry.md

Update:

    docs/Architecture.md

Update:

    docs/Roadmap.md

============================================================
STEP 75 — ROADMAP
============================================================

Mark:

    Agent 10.14 ✓

ONLY after:

- implementation complete
- tests pass
- regression suite passes
- coverage passes
- Ruff passes
- type checking passes where configured
- documentation updated

============================================================
STEP 76 — ARCHITECTURAL ACCEPTANCE CRITERIA
============================================================

Agent 10.14 is COMPLETE only when:

[ ] Live Session Adapter exists.
[ ] It connects to the existing provider abstraction.
[ ] It does not create a second Runtime.
[ ] Live telemetry enters the unified Session Runtime.
[ ] Canonical telemetry is used.
[ ] Provider-specific packets do not leak into Runtime.
[ ] Existing normalization is reused.
[ ] Live session lifecycle is implemented.
[ ] Lifecycle is idempotent.
[ ] Clean shutdown exists.
[ ] Cancellation is safe.
[ ] Sequence numbers are handled.
[ ] Duplicate packets are handled.
[ ] Timestamp validation exists.
[ ] Source timestamp is preserved.
[ ] Receive timestamp is separate where required.
[ ] Latency metrics exist where meaningful.
[ ] Backpressure is bounded.
[ ] Backpressure policy is explicit.
[ ] Reconnect is bounded where implemented.
[ ] Reconnect preserves session identity.
[ ] No duplicate runtime is created during reconnect.
[ ] Provider health exists.
[ ] Session health exists.
[ ] Event Bus integration uses existing Event Bus.
[ ] Timeline integration uses existing Runtime.
[ ] Cache integration uses existing Runtime/cache.
[ ] Session isolation exists.
[ ] Single active live source is enforced.
[ ] Configuration uses existing settings architecture.
[ ] No secrets are hard-coded.
[ ] No REST is implemented.
[ ] No WebSocket is implemented.
[ ] No Unity UI is implemented.
[ ] No OBS integration is implemented.
[ ] No duplicate database model is created.
[ ] In-memory provider/test double exists if needed.
[ ] Unit tests exist.
[ ] Integration tests exist.
[ ] Failure/reconnect tests exist.
[ ] Backpressure tests exist.
[ ] Isolation tests exist.
[ ] Phase 10.6–10.13 regression passes.
[ ] Coverage >= project gate.
[ ] Ruff passes.
[ ] Type checking passes where configured.
[ ] Documentation updated.
[ ] Roadmap updated.

============================================================
STEP 77 — IMPORTANT: DO NOT FAKE A LIVE F1 FEED
============================================================

The project must not claim to have a working official live F1 telemetry feed
unless an actual configured/licensed provider exists.

If the repository does not currently contain a production live feed:

implement:

    provider interface
    adapter
    in-memory deterministic provider
    integration boundary
    configuration

and clearly document:

    production live provider integration remains dependent on the configured
    telemetry source.

Do not invent:

- credentials
- API endpoints
- packet formats
- official F1 access
- licensing
- undocumented provider capabilities

============================================================
STEP 78 — IMPORTANT: HISTORICAL COMPATIBILITY
============================================================

The most important architectural invariant is:

    LIVE
      ↓
    Canonical Telemetry
      ↓
    Unified Runtime

and:

    HISTORICAL
      ↓
    Canonical Telemetry
      ↓
    Unified Runtime / Replay

The Runtime must not need separate logic for every provider.

Provider-specific behavior belongs at the adapter/provider boundary.

============================================================
STEP 79 — FINAL REPORT
============================================================

When complete, report:

1. Files created.
2. Files modified.
3. Existing unified Session Runtime identified.
4. Live adapter architecture.
5. Provider abstraction used.
6. Canonical telemetry path.
7. Normalization path.
8. Lifecycle/state machine.
9. Sequence handling.
10. Duplicate handling.
11. Timestamp handling.
12. Latency handling.
13. Backpressure implementation.
14. Reconnect implementation.
15. Health/status implementation.
16. Event Bus integration.
17. Timeline integration.
18. Cache integration.
19. Session isolation.
20. Runtime mode handling.
21. Controller/protocol changes.
22. Configuration changes.
23. Database changes, if any.
24. Tests added.
25. Full test results.
26. Coverage.
27. Ruff result.
28. mypy/type-check result.
29. Documentation updated.
30. Roadmap status.
31. Production live-provider limitations.
32. Known limitations.
33. Recommended Agent 10.15.

Do NOT claim completion if required tests fail.

============================================================
START IMPLEMENTATION
============================================================

First inspect the actual RaceVision repository and identify the existing
Unified Session Runtime and provider architecture.

Then implement Agent 10.14 as a thin LIVE adapter into that runtime.

Reuse existing infrastructure.

Do not create a second runtime.

Do not implement REST/WebSocket/UI.

Do not invent a production F1 feed.

Implement the complete agent.

Run focused tests.

Run the full relevant regression suite.

Fix all regressions caused by this implementation.

Update specifications, architecture/telemetry/replay documentation and
Roadmap.

Only then provide the final implementation report.
```

## User

**Agent 10.14 is complete.** Live telemetry enters the same Cache / Timeline / Event Bus / `LiveRuntime` sinks as historical/replay — no second runtime, no invented F1 feed.

### Unified runtime identified

| Sink           | Component                               |
| -------------- | --------------------------------------- |
| Race state     | `CacheManager.apply`                    |
| Time           | `TimelineService` + `TimelineMode.LIVE` |
| Fan-out        | `EventBusManager` / Live Event Bus      |
| Orchestration  | `LiveRuntime.receive_event` (optional)  |
| Domain session | `SessionManager`                        |
| Provider port  | `TelemetryProvider` / `BaseProvider`    |

### Architecture

```text
TelemetryProvider → LiveSessionAdapter → canonical frames
    → Cache + Bus + Timeline(LIVE) [+ LiveRuntime]
```

### Created

- `backend/runtime/live/` — adapter, sequence, backpressure, memory provider, control, settings, models
- `shared/protocols/commands/live/` — Start/Stop/Reconnect/GetStatus
- `tests/runtime/live/`
- `docs/specifications/LiveSessionAdapterSpecification.md`

### Modified

- Runtime package exports, command catalogue
- `docs/Roadmap.md` (10.14 ✓; transport → **10.15+**)
- `docs/Telemetry.md`, `docs/Architecture.md`, `docs/Replay.md`, specs README

### Behavior highlights

- Lifecycle: connect/run/stop/reconnect/shutdown (idempotent stop)
- Sequence duplicates rejected; gaps → DEGRADED metrics
- Source timestamp preserved; `received_at` separate; latency metric
- Bounded queue: `DROP_OLDEST` / `DROP_NEWEST` / `FAIL`
- Single active live source per adapter; session isolation via separate adapters
- `InMemoryLiveProvider` test double only — not production F1

### Quality

| Gate                              | Result         |
| --------------------------------- | -------------- |
| Live tests                        | **23 passed**  |
| Phase 10 / FastF1 regression      | **152 passed** |
| Coverage (`backend.runtime.live`) | **82.60%**     |
| Ruff                              | clean          |
| mypy (`live/`)                    | clean          |

### Limitations

No production live F1 feed claimed. Persistence / REST / WebSocket / Unity / OBS out of scope.

### Recommended Agent 10.15

**Replay/live transport façades (REST/WebSocket)** — your choice.

## Assistant

**Agent 10.14 is accepted as complete.** The implementation is consistent with the RaceVision architecture and the reported gates are good.

One important architectural note: your existing system has a `LiveRuntime` sink/orchestrator. That's fine **provided it remains the existing runtime component rather than becoming a second parallel runtime**. The key invariant remains that live telemetry converges into the same canonical Cache/Timeline/Event Bus path.

### Phase 10 status

| Agent | Component | Status |
|---|---|---|
| 10.6 | Historical Telemetry Provider | ✅ |
| 10.7 | Replay Runtime Core | ✅ |
| 10.8 | Replay Controller | ✅ |
| 10.9 | Replay Synchronization | ✅ |
| 10.10 | Replay State Cache | ✅ |
| 10.11 | Replay Bookmark & Event System | ✅ |
| 10.12 | Replay Seeking & Time Navigation | ✅ |
| 10.13 | Replay Recording/Playback Validation | ✅ |
| **10.14** | **Live Session Adapter** | **✅** |

### Acceptance highlights

The important path is now:

```text
                    ┌── Historical Provider
                    │
                    ├── FastF1 / Replay
                    │
                    ▼
              Canonical Telemetry
                    ▲
                    │
                    └── Live Session Adapter
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Unified Runtime    │
                 └──────────┬───────────┘
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
          Cache         Timeline        Event Bus
                            │
                      LIVE / HISTORICAL /
                          REPLAY
```

That's the architectural direction we want.

### Particularly good decisions

- **No invented production F1 feed** — correct.
- `InMemoryLiveProvider` is explicitly a test double.
- Source timestamp remains authoritative.
- `received_at` is separate.
- Duplicate packets are rejected.
- Sequence gaps produce degraded telemetry rather than unnecessarily killing the session.
- Bounded backpressure is implemented.
- Stop/shutdown are idempotent.
- Session isolation exists.
- No unnecessary database redesign.
- REST/WebSocket/UI remain outside this agent.
- **82.60% coverage**, Ruff clean, mypy clean.

### One thing to keep an eye on

The phrase:

```text
LiveSessionAdapter
    → Cache + Bus + Timeline
    [+ LiveRuntime]
```

should not gradually evolve into:

```text
HistoricalRuntime
LiveRuntime
ReplayRuntime
```

with three independent state machines.

The long-term target should remain:

```text
                    Session Runtime
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
         LIVE        HISTORICAL       REPLAY
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                Canonical Runtime State
```

That distinction will become increasingly important when transport and presentation are added.

### Current capability

RaceVision now has the foundation for both:

**Live:**

```text
Live Provider
    ↓
LiveSessionAdapter
    ↓
Canonical Telemetry
    ↓
Runtime
    ↓
Cache / Timeline / EventBus
```

**Historical/replay:**

```text
Historical Provider
    ↓
Canonical Telemetry
    ↓
Replay Runtime
    ↓
State Cache / Timeline / Event System
    ↓
Validation
```

So **10.14 is a meaningful milestone**: the project now has both historical and live ingestion boundaries feeding the runtime architecture.

The natural next step is **Agent 10.15**, where we expose these capabilities through transport rather than adding another runtime subsystem.

## User

Please give commands for Agent 10.15	Live/Replay Mode Controller	Switch between Live and Replay modes safely ( 1 click copy and paste cursor friendly)

## Assistant

Below is a **single Cursor-friendly copy/paste block** for Agent 10.15. It is designed around the existing 10.14 Live Session Adapter and 10.7–10.13 Replay stack, with **one authoritative Session Runtime** and safe Live ↔ Replay transitions.

```text
You are the Principal Distributed Systems Architect and Senior Python Engineer
working on the RaceVision project.

============================================================
RACEVISION — AGENT 10.15
LIVE / REPLAY MODE CONTROLLER
============================================================

OBJECTIVE
---------

Implement Agent 10.15 — Live/Replay Mode Controller.

The purpose of this agent is to safely control transitions between:

    LIVE
    REPLAY

using the existing unified Session Runtime, Live Session Adapter, Replay
Controller, Replay Runtime, Timeline, State Cache, Event Bus and Session
Manager.

The controller must NOT create another runtime.

The architectural goal is:

    LIVE SESSION
         │
         ▼
    Unified Session Runtime
         │
         │ safe mode transition
         ▼
    REPLAY SESSION

and:

    REPLAY SESSION
         │
         │ safe mode transition
         ▼
    LIVE SESSION

The controller is an orchestration/control layer.

It does not replace:

    LiveSessionAdapter
    ReplayService
    ReplayApplicationController
    ReplayNavigationService
    ReplaySynchronizer
    ReplayStateCache
    SessionManager
    TimelineService
    CacheManager
    EventBusManager

============================================================
CRITICAL ARCHITECTURAL RULE
============================================================

There must remain ONE authoritative Session Runtime.

Do NOT create:

    LiveRuntime2
    ReplayRuntime2
    ModeRuntime
    HybridRuntime
    LiveReplayRuntime

The Mode Controller coordinates existing components.

Preferred architecture:

    Mode Command
         │
         ▼
    Mode Controller
         │
     ┌───┴──────────────────────┐
     ▼                          ▼
 LiveSessionAdapter       ReplayController
     │                          │
     └──────────┬───────────────┘
                ▼
       Unified Session Runtime
                │
       ┌────────┼────────┐
       ▼        ▼        ▼
     Cache   Timeline  EventBus

============================================================
STEP 1 — READ THE REPOSITORY FIRST
============================================================

Before modifying anything, inspect the actual repository.

Read:

    docs/Roadmap.md
    docs/Architecture.md
    docs/Telemetry.md
    docs/Replay.md

Read:

    docs/specifications/SoftwareRequirementsSpecification.md
    docs/specifications/SystemArchitectureSpecification.md
    docs/specifications/HistoricalTelemetryProviderSpecification.md
    docs/specifications/ReplayRuntimeCoreSpecification.md
    docs/specifications/ReplayControllerSpecification.md
    docs/specifications/ReplaySynchronizationSpecification.md
    docs/specifications/ReplayStateCacheSpecification.md
    docs/specifications/ReplayBookmarkEventSystemSpecification.md
    docs/specifications/ReplaySeekingTimeNavigationSpecification.md
    docs/specifications/ReplayRecordingPlaybackValidationSpecification.md
    docs/specifications/LiveSessionAdapterSpecification.md

Inspect:

    backend/runtime/
    backend/runtime/live/
    backend/runtime/replay/
    backend/providers/
    backend/normalization/
    backend/telemetry/
    backend/services/
    backend/models/
    backend/database/
    shared/protocols/
    configuration/

Search for:

    SessionRuntime
    LiveRuntime
    ReplayService
    ReplayController
    ReplayApplicationController
    ReplayCommandDispatcher
    LiveSessionAdapter
    SessionManager
    TimelineService
    TimelineMode
    CacheManager
    EventBusManager
    SessionState
    RuntimeMode
    replay
    live
    transition
    lifecycle
    shutdown

The repository implementation is the source of truth.

============================================================
STEP 2 — IDENTIFY THE AUTHORITATIVE MODE
============================================================

Find the existing mode abstraction.

If the repository already has:

    RuntimeMode
    TimelineMode
    SessionMode
    SessionRuntimeMode

reuse it.

Do NOT introduce a competing mode enum.

The final architecture should have a single authoritative mode.

Expected conceptual modes:

    LIVE
    REPLAY

Historical loading may remain:

    HISTORICAL

if already defined.

Do not remove existing HISTORICAL semantics.

============================================================
STEP 3 — DEFINE MODE OWNERSHIP
============================================================

The Mode Controller owns:

    requested mode transition
    transition validation
    transition lifecycle
    transition locking
    transition result
    transition errors
    safe handoff

The Mode Controller does NOT own:

    telemetry parsing
    replay reconstruction
    live packet ingestion
    timeline internals
    cache internals
    provider internals

============================================================
STEP 4 — CREATE MODE CONTROLLER PACKAGE
============================================================

Follow repository naming conventions.

Preferred:

    backend/runtime/mode/

or:

    backend/runtime/session/mode/

Possible files:

    __init__.py
    controller.py
    enums.py
    state.py
    transition.py
    result.py
    exceptions.py
    status.py
    policy.py

Do NOT create unnecessary files.

Reuse existing types where possible.

============================================================
STEP 5 — MODE STATES
============================================================

If an existing lifecycle state machine exists, extend it.

Otherwise define a minimal transition state such as:

    STABLE
    TRANSITIONING
    FAILED

The active operating modes remain:

    LIVE
    REPLAY

Do NOT make:

    TRANSITIONING

an operating mode.

============================================================
STEP 6 — TRANSITION MODEL
============================================================

Create a structured transition model.

Conceptually:

    ModeTransition

containing:

    transition_id
    session_id
    from_mode
    to_mode
    state
    requested_at
    completed_at
    reason
    error

Use existing project ID/time conventions.

============================================================
STEP 7 — CONTROLLER API
============================================================

Provide a thin public API.

At minimum:

    get_mode()
    get_status()

    switch_to_live(...)
    switch_to_replay(...)

    can_switch_to_live(...)
    can_switch_to_replay(...)

Use existing result/error conventions.

Do not expose internal Runtime structures.

============================================================
STEP 8 — TRANSITION LOCK
============================================================

Mode changes must be serialized.

Two simultaneous commands such as:

    switch_to_live()
    switch_to_replay()

must NOT execute concurrently.

Reuse the existing Replay Manager/session lock where appropriate.

Otherwise use an appropriate async/thread-safe lock consistent with the project.

The invariant is:

    ONE MODE TRANSITION AT A TIME.

============================================================
STEP 9 — LIVE → REPLAY
============================================================

Implement the transition:

    LIVE
      ↓
    stop accepting live data
      ↓
    stop/disconnect LiveSessionAdapter safely
      ↓
    finalize live ingestion
      ↓
    ensure Runtime state is consistent
      ↓
    load/select replay
      ↓
    synchronize Replay Runtime
      ↓
    switch authoritative mode
      ↓
    REPLAY

Do not create another Session Runtime.

============================================================
STEP 10 — LIVE DATA SAFETY
============================================================

During LIVE → REPLAY:

No new live frame may be allowed to mutate the runtime after the live
handoff boundary.

Prevent:

    live frame
        ↓
    replay state
        ↓
    corruption

The transition must establish a clear ingestion boundary.

============================================================
STEP 11 — REPLAY → LIVE
============================================================

Implement:

    REPLAY
      ↓
    pause/stop replay
      ↓
    ensure no replay tick continues
      ↓
    clear/finalize replay-owned transient state
      ↓
    connect LiveSessionAdapter
      ↓
    establish LIVE session
      ↓
    synchronize runtime
      ↓
    switch authoritative mode
      ↓
    LIVE

Do not allow replay ticks to continue after LIVE becomes authoritative.

============================================================
STEP 12 — REPLAY MUST STOP BEFORE LIVE
============================================================

This is a hard invariant.

Before entering LIVE:

    ReplayService must not continue ticking.

There must never be:

    replay tick
        +
    live telemetry
        ↓
    same runtime

at the same time unless the existing architecture explicitly defines a
deterministic merge model.

For Agent 10.15, do NOT invent such a merge model.

============================================================
STEP 13 — LIVE MUST STOP BEFORE REPLAY
============================================================

This is also a hard invariant.

Before entering REPLAY:

    LiveSessionAdapter must stop feeding the runtime.

No live provider may continue publishing into the replay state.

============================================================
STEP 14 — SESSION IDENTITY
============================================================

Determine how existing SessionManager identifies sessions.

Do NOT create arbitrary new session IDs during every mode switch.

Define clearly:

    same session
    new session
    replay session

according to existing architecture.

A replay loaded from historical data must not accidentally overwrite an
unrelated live session.

============================================================
STEP 15 — LIVE SESSION CONTINUITY
============================================================

If switching:

    LIVE → REPLAY → LIVE

the controller must decide according to existing session semantics whether:

    reconnect existing live session

or:

    start a new live session.

Do not silently invent behavior.

Use explicit policy/configuration.

Preferred configuration:

    resume_live_session_on_return

if the architecture supports it.

Otherwise:

    return to LIVE requires an explicit LiveSessionRequest.

============================================================
STEP 16 — REPLAY SELECTION
============================================================

Replay transition should use existing:

    ReplayApplicationController
    ReplayService
    ReplayNavigationService

Do not directly manipulate:

    ReplayEngine internals

unless no public API exists.

============================================================
STEP 17 — REPLAY LOADING
============================================================

The controller may accept:

    replay_id
    historical request
    recording identifier

depending on existing APIs.

Do not create a new replay loading implementation.

Use Agent 10.6 and Agent 10.7–10.13 infrastructure.

============================================================
STEP 18 — REPLAY START POLICY
============================================================

When entering REPLAY, explicitly define whether the replay starts:

    LOADED / PAUSED

or:

    PLAYING

Prefer:

    LOADED / PAUSED

unless an existing product requirement explicitly requests automatic play.

The caller can then invoke:

    play()

through the existing Replay Controller.

============================================================
STEP 19 — LIVE START POLICY
============================================================

When entering LIVE, explicitly define:

    CONNECTING
       ↓
    CONNECTED
       ↓
    RUNNING

according to Agent 10.14.

Do not report LIVE before the live provider/runtime handoff has actually
completed.

============================================================
STEP 20 — ATOMIC MODE COMMIT
============================================================

Do not switch:

    mode = REPLAY

before replay is ready.

Do not switch:

    mode = LIVE

before live session is ready.

Preferred:

    current_mode
         │
         ▼
    transition
         │
    prepare target
         │
    validate target
         │
    commit target
         │
         ▼
    new current_mode

If preparation fails:

    remain in previous safe mode

where possible.

============================================================
STEP 21 — FAILURE SEMANTICS
============================================================

Example:

    LIVE → REPLAY

Replay fails to load.

Expected:

    do not report REPLAY.

Remain:

    LIVE

if the live session can safely remain active.

If live was already stopped and rollback is impossible:

    report structured TRANSITION_FAILED state.

Do not falsely report a successful transition.

============================================================
STEP 22 — ROLLBACK
============================================================

Implement best-effort rollback.

For:

    LIVE → REPLAY

if replay preparation fails:

    restore LIVE

if safe.

For:

    REPLAY → LIVE

if live connection fails:

    restore REPLAY paused state

if safe.

Do not perform unsafe automatic rollback if existing components cannot
guarantee it.

Return a structured result describing:

    transition failed
    rollback succeeded/failed

============================================================
STEP 23 — ROLLBACK MUST NOT DUPLICATE DATA
============================================================

Rollback must not cause:

    duplicate live frames
    duplicate replay events
    duplicate lifecycle events
    duplicate subscriptions

Test this explicitly.

============================================================
STEP 24 — TIMELINE MODE
============================================================

Use the existing TimelineService.

When LIVE becomes authoritative:

    TimelineMode.LIVE

When REPLAY becomes authoritative:

    TimelineMode.REPLAY

Do not create a second Timeline.

Timeline transitions must occur as part of the mode transition.

============================================================
STEP 25 — CACHE
============================================================

Use the existing CacheManager.

Before REPLAY:

ensure live state does not leak into replay state.

Before LIVE:

ensure replay state does not leak into live state.

Use existing cache reset/reconstruction mechanisms.

Do NOT create:

    LiveCache
    ReplayCache2
    ModeCache

============================================================
STEP 26 — EVENT BUS
============================================================

Use the existing EventBusManager.

Add structured mode lifecycle events only if consistent with existing protocol
architecture.

Possible events:

    ModeTransitionStarted
    ModeChanged
    ModeTransitionFailed
    ModeTransitionRolledBack

Do not create:

    LiveEventBus
    ReplayEventBus

============================================================
STEP 27 — EVENT ORDER
============================================================

Document and test event ordering.

Preferred conceptual ordering:

    TransitionStarted
          ↓
    source shutdown/preparation
          ↓
    target preparation
          ↓
    timeline/cache synchronization
          ↓
    authoritative mode commit
          ↓
    ModeChanged

Failure:

    TransitionStarted
          ↓
    failure
          ↓
    rollback
          ↓
    TransitionFailed

Do not emit ModeChanged before the target is actually ready.

============================================================
STEP 28 — REPLAY EVENT SYSTEM
============================================================

Do not destroy user bookmarks merely because the mode changes.

If replay state is switched away from and back:

    bookmark ownership must remain consistent with replay_id.

Reuse Agent 10.11.

============================================================
STEP 29 — REPLAY STATE CACHE
============================================================

Do not bypass Agent 10.10.

Replay transitions should use:

    ReplayStateCache

through ReplayService.

Do not directly manipulate snapshots from the Mode Controller.

============================================================
STEP 30 — REPLAY SYNCHRONIZATION
============================================================

When entering REPLAY:

use Agent 10.9 synchronization.

Expected invariant:

    Timeline ≈ Replay Clock

within existing configured tolerance.

Do not duplicate synchronization logic.

============================================================
STEP 31 — LIVE SYNCHRONIZATION
============================================================

When entering LIVE:

use existing Timeline/Cache synchronization paths.

Do not invent a separate LiveSynchronizer unless the repository explicitly
requires one.

============================================================
STEP 32 — VALIDATION
============================================================

Before completing a transition, validate:

    target runtime exists
    target session identity is valid
    target mode is correct
    timeline mode is correct
    cache state is compatible
    no conflicting source is active
    no replay tick is active when LIVE
    no live provider is active when REPLAY

============================================================
STEP 33 — SAFE MODE
============================================================

If a transition cannot safely complete, expose:

    TRANSITION_FAILED

rather than silently selecting an ambiguous mode.

Never allow:

    LIVE + REPLAY

as an undocumented state.

============================================================
STEP 34 — STATUS
============================================================

Expose structured status.

At minimum:

    current_mode
    transition_state
    transition_id
    session_id
    target_mode
    can_switch_to_live
    can_switch_to_replay
    live_connected
    replay_loaded
    replay_playing
    timeline_mode
    last_transition
    last_error

Reuse existing status models where possible.

============================================================
STEP 35 — CAPABILITIES
============================================================

Implement capability checks.

Examples:

    can_switch_to_live
    can_switch_to_replay
    can_stop_live
    can_start_replay

These must reflect actual runtime state.

Do not simply return TRUE because a method exists.

============================================================
STEP 36 — COMMANDS
============================================================

Inspect existing command protocol.

If appropriate, add:

    SwitchToLive
    SwitchToReplay
    GetModeStatus

Only add commands if no equivalent already exists.

Do not implement REST/WebSocket in this agent.

============================================================
STEP 37 — CONTROLLER INTEGRATION
============================================================

Preferred:

    Command
       ↓
    Dispatcher
       ↓
    ModeController
       ├── LiveSessionAdapter
       └── ReplayApplicationController
                    │
                    ▼
             existing runtimes

The Mode Controller must remain a thin orchestrator.

============================================================
STEP 38 — CONCURRENCY
============================================================

Protect transitions with the appropriate existing lock.

Test:

    switch_to_live()
    switch_to_replay()

called concurrently.

Expected:

    deterministic serialization

No double start.

No double stop.

No corrupted state.

============================================================
STEP 39 — IDEMPOTENCY
============================================================

Calling:

    switch_to_live()

while already LIVE

should return a deterministic no-op/result.

Likewise:

    switch_to_replay()

while already REPLAY.

Do not reload/reconnect unnecessarily.

============================================================
STEP 40 — LIVE → LIVE
============================================================

Expected:

    no provider restart
    no timeline reset
    no cache reset
    no mode change event

unless explicitly requested.

============================================================
STEP 41 — REPLAY → REPLAY
============================================================

Expected:

    no replay reload
    no cursor reset
    no snapshot invalidation
    no mode change event

unless explicitly requested.

============================================================
STEP 42 — RAPID SWITCHING
============================================================

Test:

    LIVE
      ↓
    REPLAY
      ↓
    LIVE
      ↓
    REPLAY

Verify:

- no leaked tasks
- no duplicate providers
- no duplicate subscriptions
- no stale mode
- no stale timeline mode
- no cache contamination
- no duplicate events

============================================================
STEP 43 — LIVE → REPLAY WHILE PLAYING
============================================================

If LIVE is active:

stop live safely.

Then load replay.

Do not allow live ingestion during replay.

============================================================
STEP 44 — REPLAY → LIVE WHILE PLAYING
============================================================

If replay is PLAYING:

pause/stop replay before connecting LIVE.

Verify:

    no replay tick after LIVE commit.

============================================================
STEP 45 — REPLAY → LIVE WHILE PAUSED
============================================================

Verify transition works without unnecessary replay work.

============================================================
STEP 46 — LIVE PROVIDER FAILURE DURING TRANSITION
============================================================

Test provider failure during:

    LIVE → REPLAY

and:

    REPLAY → LIVE

Return structured transition result.

Do not leave stale provider state.

============================================================
STEP 47 — REPLAY FAILURE DURING TRANSITION
============================================================

Test replay load failure.

Expected:

    no false REPLAY state.

Rollback if safe.

============================================================
STEP 48 — TIMELINE FAILURE
============================================================

Test Timeline synchronization failure.

Expected:

    transition does not falsely commit.

Return structured failure.

============================================================
STEP 49 — CACHE FAILURE
============================================================

Test cache preparation failure.

Expected:

    transition failure.

No partial mode commit.

============================================================
STEP 50 — EVENT BUS FAILURE
============================================================

Follow existing EventBus failure policy.

Do not leave the mode falsely committed if EventBus participation is required
for a valid transition.

============================================================
STEP 51 — SESSION ISOLATION
============================================================

Create:

    Session A LIVE
    Session B REPLAY

Verify their state remains isolated according to the existing multi-session
architecture.

Do not globally switch every session unless the existing architecture defines
a global runtime.

============================================================
STEP 52 — SINGLE ACTIVE SOURCE
============================================================

The same session must never simultaneously receive:

    live telemetry

and:

    replay telemetry.

Enforce this at the controller boundary.

============================================================
STEP 53 — DATA BOUNDARY
============================================================

Document exactly where the source handoff occurs.

Example:

    LIVE source accepted
         ↓
    transition barrier
         ↓
    LIVE source closed
         ↓
    REPLAY source accepted

and reverse.

============================================================
STEP 54 — WALL CLOCK
============================================================

Do not use wall-clock time to drive replay.

Replay continues to use:

    ReplayClock

from Agent 10.7.

LIVE uses incoming telemetry timestamps and existing runtime timing.

============================================================
STEP 55 — CONFIGURATION
============================================================

Use existing Pydantic Settings architecture.

Possible settings only if justified:

    mode_transition_timeout
    auto_rollback
    require_live_stop_before_replay
    require_replay_stop_before_live

Do not hard-code operational policy.

============================================================
STEP 56 — ERROR MODEL
============================================================

Create structured errors only if existing errors cannot represent:

    InvalidModeTransition
    ModeTransitionInProgress
    TargetModeUnavailable
    LiveSessionRequired
    ReplayRequired
    TransitionTimeout
    TransitionRollbackFailed
    ConcurrentModeChange

Reuse existing errors where possible.

============================================================
STEP 57 — TIMEOUT
============================================================

Mode transitions must not hang forever.

If the existing async architecture supports timeouts:

apply a configurable timeout.

On timeout:

    structured failure
    cleanup
    rollback if safe

No orphaned background tasks.

============================================================
STEP 58 — SHUTDOWN
============================================================

During application shutdown:

the Mode Controller must not start a new mode transition.

If a transition is active:

    cancel/finish according to existing shutdown policy.

Then:

    stop live provider
    stop replay
    release locks/resources

Use existing lifecycle architecture.

============================================================
STEP 59 — TEST: INITIAL STATE
============================================================

Verify initial mode is deterministic.

Do not assume LIVE.

Do not assume REPLAY.

Use existing Session Runtime semantics.

============================================================
STEP 60 — TEST: LIVE → REPLAY
============================================================

Start LIVE.

Feed telemetry.

Switch to REPLAY.

Verify:

- live provider stopped
- no new live frames accepted
- replay loaded
- TimelineMode.REPLAY
- replay state synchronized
- current mode REPLAY

============================================================
STEP 61 — TEST: REPLAY → LIVE
============================================================

Start REPLAY.

Play/pause as appropriate.

Switch to LIVE.

Verify:

- replay stopped
- replay tick loop inactive
- TimelineMode.LIVE
- live adapter connected
- current mode LIVE

============================================================
STEP 62 — TEST: IDEMPOTENCY
============================================================

Test:

    LIVE → LIVE
    REPLAY → REPLAY

Expected:

    deterministic no-op.

============================================================
STEP 63 — TEST: CONCURRENT TRANSITIONS
============================================================

Run simultaneous:

    LIVE
    REPLAY

requests.

Expected:

    serialized transition.

============================================================
STEP 64 — TEST: ROLLBACK
============================================================

Force replay load failure.

Verify:

    LIVE remains authoritative

or:

    structured transition failure

according to safe rollback capability.

============================================================
STEP 65 — TEST: REPLAY FAILURE
============================================================

Force replay initialization failure.

Verify:

    no false REPLAY state.

============================================================
STEP 66 — TEST: LIVE FAILURE
============================================================

Force live connection failure.

Verify:

    no false LIVE state.

============================================================
STEP 67 — TEST: NO DUAL INGESTION
============================================================

Instrument Runtime ingestion.

During every stable mode:

    LIVE → only live source
    REPLAY → only replay source

Verify no simultaneous ingestion.

============================================================
STEP 68 — TEST: TIMELINE
============================================================

Verify:

    LIVE → TimelineMode.LIVE

and:

    REPLAY → TimelineMode.REPLAY

============================================================
STEP 69 — TEST: CACHE ISOLATION
============================================================

Verify replay state cannot leak into live state.

Verify live state cannot leak into replay state.

============================================================
STEP 70 — TEST: EVENT ORDER
============================================================

Verify:

    TransitionStarted
        ↓
    preparation
        ↓
    synchronization
        ↓
    ModeChanged

and failure ordering.

============================================================
STEP 71 — TEST: RAPID SWITCH
============================================================

Execute multiple sequential transitions.

Verify:

- no leaked tasks
- no duplicate subscriptions
- no duplicate provider
- no stale locks
- no stale transition state

============================================================
STEP 72 — TEST: SHUTDOWN
============================================================

Start transition.

Trigger shutdown.

Verify:

- no deadlock
- no orphaned task
- provider/replay resources released
- controller reaches terminal shutdown state

============================================================
STEP 73 — TEST: SESSION ISOLATION
============================================================

Verify independent sessions do not contaminate one another.

============================================================
STEP 74 — TEST: COMMAND DISPATCH
============================================================

If protocol commands are added:

verify:

    command
       ↓
    dispatcher
       ↓
    ModeController

No direct provider/runtime access from command handlers.

============================================================
STEP 75 — TEST: STATUS
============================================================

Verify status accurately reports:

    mode
    transition state
    target
    capabilities
    live state
    replay state
    timeline mode
    errors

============================================================
STEP 76 — REGRESSION
============================================================

Run all relevant tests:

- Phase 10
- Agent 10.6
- Agent 10.7
- Agent 10.8
- Agent 10.9
- Agent 10.10
- Agent 10.11
- Agent 10.12
- Agent 10.13
- Agent 10.14
- providers
- normalization
- runtime
- cache
- timeline
- Event Bus
- configuration
- database

Fix all regressions caused by Agent 10.15.

============================================================
STEP 77 — COVERAGE
============================================================

Target:

    >= 80%

for the new Agent 10.15 package.

Prefer:

    >= 85%

where practical.

============================================================
STEP 78 — CODE QUALITY
============================================================

Follow RaceVision standards:

- Python 3.11
- PEP 8
- complete type hints
- dependency injection
- deterministic state transitions
- no global mutable state
- no circular imports
- structured logging
- structured errors
- async-safe lifecycle
- cancellation safety
- bounded operations
- deterministic tests

Run:

    Ruff
    mypy/type checker if configured
    tests
    coverage

Discover exact project commands from:

    pyproject.toml
    Makefile
    CI
    scripts

============================================================
STEP 79 — DOCUMENTATION
============================================================

Create:

    docs/specifications/LiveReplayModeControllerSpecification.md

Document:

- purpose
- architecture
- mode ownership
- state machine
- transition model
- LIVE → REPLAY
- REPLAY → LIVE
- transition barrier
- source handoff
- session identity
- rollback
- failure handling
- concurrency
- idempotency
- Timeline
- Cache
- Event Bus
- LiveSessionAdapter
- ReplayController
- Replay synchronization
- configuration
- shutdown
- testing
- limitations

Update:

    docs/specifications/README.md
    docs/Architecture.md
    docs/Replay.md
    docs/Telemetry.md
    docs/Roadmap.md

============================================================
STEP 80 — ROADMAP
============================================================

Mark:

    Agent 10.15 ✓

ONLY after:

- implementation complete
- focused tests pass
- full regression passes
- coverage passes
- Ruff passes
- type checking passes where configured
- documentation updated

============================================================
STEP 81 — ARCHITECTURAL ACCEPTANCE CRITERIA
============================================================

Agent 10.15 is COMPLETE only when:

[ ] Mode Controller exists.
[ ] Existing unified runtime remains authoritative.
[ ] No second runtime is created.
[ ] Existing LiveSessionAdapter is reused.
[ ] Existing ReplayController is reused.
[ ] Existing ReplayService is reused.
[ ] Existing Timeline is reused.
[ ] Existing Cache is reused.
[ ] Existing Event Bus is reused.
[ ] LIVE mode is supported.
[ ] REPLAY mode is supported.
[ ] Existing HISTORICAL semantics remain intact.
[ ] LIVE → REPLAY is safe.
[ ] REPLAY → LIVE is safe.
[ ] Live ingestion stops before REPLAY becomes authoritative.
[ ] Replay ticking stops before LIVE becomes authoritative.
[ ] No dual ingestion occurs.
[ ] Mode transitions are serialized.
[ ] Mode transitions are idempotent.
[ ] Atomic/validated mode commit exists.
[ ] Transition failure is explicit.
[ ] Rollback is implemented where safe.
[ ] Rollback does not duplicate data.
[ ] Timeline mode follows authoritative mode.
[ ] Cache state is isolated.
[ ] Event ordering is deterministic.
[ ] Session identity is preserved correctly.
[ ] Session isolation is preserved.
[ ] Single active source is enforced.
[ ] Replay synchronization is reused.
[ ] Live synchronization uses existing runtime path.
[ ] Status/capabilities exist.
[ ] Structured errors exist.
[ ] Timeout/cancellation is safe.
[ ] Shutdown is safe.
[ ] Commands are added only where necessary.
[ ] No REST implementation.
[ ] No WebSocket implementation.
[ ] No Unity implementation.
[ ] No OBS implementation.
[ ] No new telemetry provider is invented.
[ ] No duplicate database subsystem is created.
[ ] Unit tests exist.
[ ] Integration tests exist.
[ ] Failure tests exist.
[ ] Rollback tests exist.
[ ] Concurrency tests exist.
[ ] Rapid-switch tests exist.
[ ] Dual-ingestion prevention is tested.
[ ] Session isolation is tested.
[ ] Timeline/cache/event integration is tested.
[ ] Phase 10.6–10.14 regression passes.
[ ] Coverage meets project gate.
[ ] Ruff passes.
[ ] mypy/type checking passes where configured.
[ ] Documentation updated.
[ ] Roadmap updated.

============================================================
STEP 82 — IMPORTANT: DO NOT BUILD TRANSPORT
============================================================

Agent 10.15 is the MODE CONTROL layer.

Do NOT implement:

    REST
    WebSocket
    HTTP
    Unity UI
    OBS
    Twitch
    Kick
    YouTube

Those belong to later transport/presentation work.

============================================================
STEP 83 — IMPORTANT: NO UNSAFE MODE SWITCH
============================================================

Never allow:

    current_mode = REPLAY

while LIVE is still actively feeding Runtime.

Never allow:

    current_mode = LIVE

while ReplayService is still ticking.

Never silently swallow transition failures.

Never claim a mode switch succeeded until the target is ready.

============================================================
STEP 84 — IMPORTANT: DO NOT REWRITE EXISTING REPLAY/LIVE CODE
============================================================

Agents 10.6–10.14 are already complete.

Treat them as established infrastructure.

Only modify them where the Mode Controller requires a clean integration point.

Prefer adapters/facades over invasive rewrites.

If an architectural conflict is discovered, document it and make the smallest
safe correction.

============================================================
START IMPLEMENTATION
============================================================

First inspect the actual RaceVision repository.

Identify:

1. authoritative Session Runtime
2. existing Runtime/Timeline mode abstraction
3. LiveSessionAdapter from Agent 10.14
4. ReplayController from Agent 10.8
5. ReplayService from Agent 10.7
6. Replay synchronization from Agent 10.9
7. Replay State Cache from Agent 10.10
8. Event System from Agent 10.11
9. Navigation from Agent 10.12
10. Validation from Agent 10.13

Then implement Agent 10.15 as a thin orchestration layer.

Do not create a second runtime.

Do not create a parallel Timeline.

Do not create a parallel Cache.

Do not create a parallel Event Bus.

Do not build transport.

Implement the complete agent.

Run focused tests.

Run the complete relevant regression suite.

Fix all regressions.

Update documentation and Roadmap.

Only then provide the final implementation report.

============================================================
FINAL REPORT FORMAT
============================================================

When complete, report:

1. Files created.
2. Files modified.
3. Authoritative runtime identified.
4. Mode abstraction reused.
5. Mode Controller architecture.
6. LIVE → REPLAY transition sequence.
7. REPLAY → LIVE transition sequence.
8. Transition locking.
9. Atomic mode commit.
10. Rollback behavior.
11. Failure behavior.
12. Timeline integration.
13. Cache integration.
14. Event Bus integration.
15. LiveSessionAdapter integration.
16. ReplayController integration.
17. Session identity behavior.
18. Session isolation behavior.
19. Dual-ingestion prevention.
20. Status/capabilities.
21. Protocol changes.
22. Configuration changes.
23. Tests added.
24. Focused test results.
25. Full regression results.
26. Coverage.
27. Ruff result.
28. mypy/type-check result.
29. Documentation updated.
30. Roadmap status.
31. Known limitations.
32. Recommended Agent 10.16.
```

## User

**Agent 10.15 is complete.** `ModeController` safely hands off LIVE ↔ REPLAY over the existing unified runtime — no second runtime, no dual ingestion, no transport.

### Identity

| Item                  | Value                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------- |
| Authoritative runtime | `CacheManager` + `TimelineService` + Event Bus + `LiveRuntime`                               |
| Mode abstraction      | `SessionOperatingMode` aligned with `TimelineMode` (`live`/`replay`); `HISTORICAL` untouched |
| Live return policy    | **Explicit** `LiveSessionRequest` + provider (no silent reconnect)                           |

### Architecture

```text
Command → ModeCommandDispatcher → ModeController
              ├── LiveSessionAdapter
              └── ReplayApplicationController
                         ↓
              Cache · Timeline · Event Bus
```

### Transitions

- **LIVE→REPLAY:** stop live → clear cache → load replay (paused) → `TimelineMode.REPLAY` → commit
- **REPLAY→LIVE:** pause/stop replay → clear cache → start live → `TimelineMode.LIVE` → commit
- Serialized via `asyncio.Lock`; idempotent same-mode no-ops; commit only after target ready
- Failure → structured result + best-effort rollback (`auto_rollback`)

### Created / modified

- **Created:** `backend/runtime/mode/`, `shared/protocols/commands/mode/`, `tests/runtime/mode/`, `LiveReplayModeControllerSpecification.md`
- **Modified:** command catalogue, runtime exports, Roadmap (10.15 ✓ → transport **10.16+**), Architecture/Replay/Telemetry/specs README

### Quality

| Gate                        | Result         |
| --------------------------- | -------------- |
| Mode tests                  | **18 passed**  |
| Phase 10.6–10.15 regression | **170 passed** |
| Coverage                    | **85.37%**     |
| Ruff                        | clean          |
| mypy (`mode/`)              | clean          |

### Limitations

No REST/WS/UI. Multi-session isolation is via separate controller instances. Live resume never invented silently.

### Recommended Agent 10.16

**REST/WebSocket transport façades for live + replay** — your choice.

## Assistant

Excellent. **Agent 10.15 is accepted as complete.**

The implementation matches the intended architecture: the Mode Controller is an orchestration layer, not another runtime, and the source handoff is explicit and serialized.

### Phase 10.6–10.15

| Agent | Component | Status |
|---|---|---|
| 10.6 | Historical Telemetry Provider | ✅ |
| 10.7 | Replay Runtime Core | ✅ |
| 10.8 | Replay Controller | ✅ |
| 10.9 | Replay Synchronization | ✅ |
| 10.10 | Replay State Cache | ✅ |
| 10.11 | Replay Bookmark & Event System | ✅ |
| 10.12 | Replay Seeking & Time Navigation | ✅ |
| 10.13 | Replay Recording/Playback Validation | ✅ |
| 10.14 | Live Session Adapter | ✅ |
| **10.15** | **Live/Replay Mode Controller** | **✅** |

### Key architectural invariant now established

```text
                    Unified Session Runtime
                             │
                 ┌───────────┴───────────┐
                 │                       │
              LIVE                     REPLAY
                 │                       │
        LiveSessionAdapter       ReplayController
                 │                       │
                 └───────────┬───────────┘
                             ▼
                    CacheManager
                             │
                    TimelineService
                             │
                       Event Bus
```

The important part is that **LIVE and REPLAY are modes of the same runtime**, rather than two competing runtimes.

### 10.15 acceptance

The reported results are strong:

- **18** focused mode tests
- **170** Phase 10.6–10.15 regression tests
- **85.37%** coverage
- Ruff clean
- mypy clean
- Serialized transitions
- Idempotent same-mode operations
- Atomic target-mode commit
- Best-effort rollback
- No dual ingestion
- Explicit live-session return
- Historical mode preserved
- No transport/UI leakage into this agent

I especially agree with the decision to require an explicit `LiveSessionRequest` when returning to LIVE. **Do not silently reconnect a production telemetry source.**

### Current architectural position

RaceVision has now crossed an important boundary:

```text
          TELEMETRY SOURCES
                 │
       ┌─────────┴─────────┐
       │                   │
      LIVE             HISTORICAL
       │                   │
       ▼                   ▼
 LiveSessionAdapter    FastF1Provider
       │                   │
       │              Replay Runtime
       │                   │
       └─────────┬─────────┘
                 ▼
          Mode Controller
                 │
                 ▼
       Unified Session Runtime
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
     Cache    Timeline   EventBus
```

And the replay side now has:

```text
Replay
 ├── Runtime Core
 ├── Controller
 ├── Synchronization
 ├── State Cache
 ├── Events / Bookmarks
 ├── Navigation
 └── Validation
```

while the live side has:

```text
Live
 └── Live Session Adapter
```

with 10.15 providing the controlled handoff between them.

**Agent 10.16 is therefore the logical next boundary: transport/presentation access to these already-existing capabilities, without putting business logic into REST/WebSocket handlers.**

## User

Please give commands for Agent 10.16	Race Timeline Delay Buffer	Foundation for the planned live delay	10.5 + Live Session ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. Agent 10.16 should build the **delay-buffer foundation**, not the final broadcaster/UI delay system. It must work with the existing unified runtime and remain compatible with 10.14 Live Session and 10.15 Mode Controller.

```text id="58321"
You are the Principal Distributed Systems Architect and Senior Python Engineer
working on the RaceVision project.

============================================================
RACEVISION — AGENT 10.16
RACE TIMELINE DELAY BUFFER
============================================================

OBJECTIVE
---------

Implement Agent 10.16 — Race Timeline Delay Buffer.

Purpose:

Create the foundation for RaceVision's planned LIVE race delay capability.

The system must be able to receive live canonical telemetry, retain it in a
bounded time-based buffer, and expose a delayed timeline/telemetry view without
creating a second runtime.

This is infrastructure for the planned live-delay feature.

It is NOT yet:

    - broadcaster-specific delay
    - OBS delay control
    - Twitch/Kick/YouTube implementation
    - REST transport
    - WebSocket transport
    - Unity UI
    - camera delay UI
    - audio delay system
    - artificial network latency
    - database persistence product
    - a second runtime

============================================================
CURRENT ARCHITECTURE
============================================================

Agents 10.6–10.15 are COMPLETE.

Existing architecture:

    HistoricalTelemetryProvider
            │
            ▼
    Canonical Telemetry
            │
            ├───────────────┐
            ▼               ▼
    Replay Runtime       LiveSessionAdapter
                            │
                            ▼
                    ModeController
                            │
                            ▼
                  Unified Session Runtime
                            │
                ┌───────────┼───────────┐
                ▼           ▼           ▼
              Cache      Timeline     EventBus

Agent 10.16 must fit INTO this architecture.

DO NOT create:

    DelayRuntime
    LiveDelayRuntime
    DelayedRuntime
    SecondTimeline
    SecondCache
    SecondEventBus

The delay buffer is a temporal data structure/service used by the existing
runtime.

============================================================
STEP 1 — READ THE REPOSITORY FIRST
============================================================

Before changing code, inspect the actual repository.

Read:

    docs/Roadmap.md
    docs/Architecture.md
    docs/Telemetry.md
    docs/Replay.md
    docs/Streaming.md

Read:

    docs/specifications/SoftwareRequirementsSpecification.md
    docs/specifications/SystemArchitectureSpecification.md

Read the specifications from Agents 10.6–10.15:

    HistoricalTelemetryProviderSpecification.md
    ReplayRuntimeCoreSpecification.md
    ReplayControllerSpecification.md
    ReplaySynchronizationSpecification.md
    ReplayStateCacheSpecification.md
    ReplayBookmarkEventSystemSpecification.md
    ReplaySeekingTimeNavigationSpecification.md
    ReplayRecordingPlaybackValidationSpecification.md
    LiveSessionAdapterSpecification.md
    LiveReplayModeControllerSpecification.md

Inspect:

    backend/runtime/
    backend/runtime/live/
    backend/runtime/replay/
    backend/runtime/mode/
    backend/providers/
    backend/normalization/
    backend/telemetry/
    backend/services/
    shared/protocols/
    configuration/

Search for:

    TimelineService
    TimelineMode
    CacheManager
    TelemetryProvider
    BaseProvider
    LiveSessionAdapter
    LiveRuntime
    SessionRuntime
    EventBusManager
    source_timestamp
    received_at
    sequence
    canonical frame
    telemetry frame
    RuntimeMode
    SessionOperatingMode

The repository is the source of truth.

============================================================
STEP 2 — UNDERSTAND AGENT 10.5
============================================================

Agent 10.16 explicitly builds on the existing Timeline foundation from 10.5.

Locate the exact implementation created by Agent 10.5.

Determine:

    - timeline model
    - timeline clock
    - timeline position
    - timeline mode
    - timeline event semantics
    - timestamp precision
    - synchronization behavior
    - locking/concurrency model
    - public APIs
    - existing tests

DO NOT replace the existing TimelineService.

DO NOT duplicate timeline state.

Extend the existing timeline architecture where appropriate.

============================================================
STEP 3 — FUNDAMENTAL DESIGN
============================================================

The delay buffer should conceptually operate like:

    Live Telemetry
          │
          ▼
    Canonical Frame
          │
          ▼
    Delay Buffer
          │
          ├── newest source timestamp
          ├── oldest retained timestamp
          ├── target delayed timestamp
          └── buffered frames
                    │
                    ▼
              Delayed View
                    │
                    ▼
             Existing Runtime
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
        Cache    Timeline   EventBus

The buffer itself does NOT become the runtime.

============================================================
STEP 4 — SOURCE TIME IS AUTHORITATIVE
============================================================

The buffer must use the canonical telemetry source timestamp.

Do NOT base delay on:

    received_at

unless explicitly required for diagnostics.

Use:

    source_timestamp

as the authoritative race timeline.

Keep:

    received_at

for latency/observability.

Example:

    source_timestamp = 14:32:10.250
    received_at      = 14:32:10.430

A 5-second delay means the target is:

    14:32:05.250

not:

    14:32:05.430

============================================================
STEP 5 — CREATE DELAY BUFFER PACKAGE
============================================================

Follow repository naming conventions.

Preferred:

    backend/runtime/delay/

or:

    backend/runtime/live_delay/

Prefer the simpler:

    backend/runtime/delay/

Potential files:

    __init__.py
    buffer.py
    frame.py
    clock.py
    policy.py
    settings.py
    status.py
    result.py
    exceptions.py

Only create files that are actually necessary.

============================================================
STEP 6 — CORE BUFFER RESPONSIBILITY
============================================================

Implement a time-indexed bounded buffer.

At minimum support:

    append(frame)
    oldest_timestamp()
    newest_timestamp()
    target_timestamp(delay_ms)
    get_frame_at(timestamp)
    get_frames_between(start, end)
    evict_before(timestamp)
    clear()
    size()
    status()

Use efficient timestamp indexing.

Do NOT scan the entire buffer for every lookup.

A deque plus monotonic timestamp index or equivalent structure is acceptable.

Use the project's existing data structures where possible.

============================================================
STEP 7 — TIMESTAMP ORDER
============================================================

Canonical source timestamps should normally be monotonic.

However, telemetry may arrive:

    duplicated
    late
    out of order

The buffer must define explicit policy.

Do NOT silently assume perfect ordering.

Provide policy for:

    duplicate
    older-than-latest
    equal timestamp
    timestamp regression

Possible policies:

    REJECT
    ACCEPT
    REORDER

Choose based on existing telemetry ingestion semantics.

Prefer the smallest deterministic implementation consistent with 10.14.

============================================================
STEP 8 — SEQUENCE HANDLING
============================================================

Agent 10.14 already handles telemetry sequence behavior.

Do NOT duplicate sequence validation.

The delay buffer should consume canonical frames after provider/adapter
validation.

If sequence metadata is present, preserve it.

Do not become the authoritative sequence validator.

============================================================
STEP 9 — DELAY CONFIGURATION
============================================================

Create configuration using the existing Pydantic Settings architecture.

Possible settings:

    enabled
    delay_ms
    min_delay_ms
    max_delay_ms
    buffer_capacity_ms
    late_frame_policy
    duplicate_policy
    overflow_policy
    interpolation_enabled

Do NOT hard-code these values.

Use sensible defaults.

Suggested initial defaults:

    enabled = false
    delay_ms = 0
    min_delay_ms = 0
    max_delay_ms = 120000
    buffer_capacity_ms = 180000

These are implementation defaults, not final product requirements.

Document them.

============================================================
STEP 10 — CONFIGURATION SAFETY
============================================================

Validate:

    delay_ms >= 0

    max_delay_ms >= min_delay_ms

    buffer_capacity_ms >= max_delay_ms

if the architecture requires that relationship.

Reject impossible configuration.

Do not silently clamp invalid configuration unless existing project configuration
semantics require clamping.

============================================================
STEP 11 — BUFFER CAPACITY
============================================================

The buffer must be bounded.

Never create an unbounded list of live telemetry.

Bound by time and/or maximum frame count.

Preferred:

    time-based retention

with an optional hard frame limit.

Example:

    retain 180 seconds

and:

    never exceed max_frames

============================================================
STEP 12 — EVICTION
============================================================

Evict data that can no longer be required by the configured delay window.

For example:

    newest = 14:35:00
    delay = 10s
    retention = 180s

Frames older than:

    14:32:00

may be eligible for eviction.

Do not evict frames still required for:

    delayed target
    interpolation
    configured lookback

============================================================
STEP 13 — NO WALL-CLOCK REPLAY
============================================================

Do not turn this into ReplayClock.

Live delay is based on:

    latest source timestamp
    minus configured delay

The existing ReplayClock remains exclusively responsible for replay playback.

============================================================
STEP 14 — DELAYED TARGET
============================================================

Given:

    newest_source_timestamp = T

and:

    delay_ms = D

the desired delayed timeline position is:

    target = T - D

The buffer must expose this calculation deterministically.

Do not use:

    current wall-clock - D

as the authoritative race timeline.

============================================================
STEP 15 — BUFFERING STATE
============================================================

Define buffering state.

At minimum:

    DISABLED
    BUFFERING
    READY
    DEGRADED
    STARVED

Suggested semantics:

DISABLED:
    delay feature disabled.

BUFFERING:
    insufficient telemetry history to safely satisfy configured delay.

READY:
    enough history exists to provide the configured delay.

DEGRADED:
    buffer exists but telemetry quality/continuity is impaired.

STARVED:
    delayed target cannot currently be produced.

Use existing project state conventions if equivalent states already exist.

============================================================
STEP 16 — BUFFER READINESS
============================================================

Example:

    delay = 10 seconds

At the beginning of a live session:

    newest = T
    oldest = T

The buffer is:

    BUFFERING

until:

    newest - oldest >= 10 seconds

Then:

    READY

Do not falsely report READY before enough history exists.

============================================================
STEP 17 — STARVATION
============================================================

If live telemetry stops arriving and the delayed target moves beyond the
available data:

transition to:

    STARVED

or existing equivalent.

Do not invent telemetry.

Do not repeat the newest frame indefinitely unless explicitly configured.

============================================================
STEP 18 — LIVE TELEMETRY INTEGRATION
============================================================

Integrate with Agent 10.14.

Preferred flow:

    LiveSessionAdapter
          │
          ▼
    canonical frame
          │
          ▼
    DelayBuffer
          │
          ▼
    delayed runtime application

Do not make LiveSessionAdapter itself responsible for all delay logic.

Keep the adapter responsible for ingestion.

============================================================
STEP 19 — DISABLED MODE
============================================================

When:

    enabled = false

the existing LIVE behavior must remain unchanged.

Expected:

    LiveSessionAdapter
        ↓
    existing runtime path

No unnecessary buffering overhead.

============================================================
STEP 20 — ZERO DELAY
============================================================

When:

    delay_ms = 0

the delayed target equals the newest available source timestamp.

Do not introduce an artificial delay.

The buffer may still exist for diagnostics if configured, but the runtime must
not become delayed.

============================================================
STEP 21 — LIVE MODE ONLY
============================================================

Agent 10.16 is primarily a LIVE delay foundation.

Do not apply the live delay buffer to:

    REPLAY

unless existing architecture explicitly requires it.

Replay already has:

    ReplayClock
    ReplayService
    ReplayNavigationService

Do not stack another temporal mechanism on top of replay.

============================================================
STEP 22 — MODE CONTROLLER INTEGRATION
============================================================

Integrate carefully with Agent 10.15.

When entering:

    LIVE

the delay buffer may initialize/reset according to policy.

When leaving:

    LIVE → REPLAY

the live delay buffer must stop receiving live frames.

When entering:

    REPLAY

the live delay buffer must not mutate replay state.

When returning:

    REPLAY → LIVE

initialize the live delay state according to explicit configuration.

Do not silently reconnect the live provider.

============================================================
STEP 23 — BUFFER RESET
============================================================

Define explicit reset conditions.

Reset when:

    live session changes
    source changes
    track/session identity changes
    provider reconnect requires a new timeline
    explicit reset requested

Do not accidentally carry:

    Monaco data

into:

    Silverstone

or one race session into another.

============================================================
STEP 24 — SESSION ISOLATION
============================================================

Buffer identity must include the relevant session identity.

Do not allow:

    Session A telemetry

to populate:

    Session B delay buffer.

If the architecture uses one buffer per controller/session, document that.

============================================================
STEP 25 — TRACK / EVENT ISOLATION
============================================================

If session identity alone does not guarantee event isolation, include the
existing race/session identifier.

Do not invent a new identity system.

Reuse existing:

    session_id
    race_session_id
    replay_id

where applicable.

============================================================
STEP 26 — FRAME RETENTION
============================================================

Frames should be immutable from the delay buffer's perspective.

Do not mutate the canonical telemetry object after insertion.

Prefer immutable references/models consistent with existing telemetry types.

============================================================
STEP 27 — INTERPOLATION
============================================================

Do NOT implement sophisticated telemetry interpolation unless required by the
existing architecture.

For Agent 10.16:

    exact frame lookup
    nearest frame
    bracketing frames

are sufficient.

If interpolation is implemented, keep it optional and deterministic.

Never fabricate vehicle physics.

============================================================
STEP 28 — FRAME LOOKUP
============================================================

Provide deterministic lookup semantics.

For:

    get_frame_at(timestamp)

define whether the result is:

    exact
    floor
    nearest
    ceiling

Prefer:

    floor + optional next frame

because this matches the existing timeline/replay semantics.

Document this.

============================================================
STEP 29 — BRACKET LOOKUP
============================================================

Provide:

    get_bracketing_frames(timestamp)

returning:

    previous
    next

where available.

This will support future interpolation.

============================================================
STEP 30 — DELAYED FRAME PULL
============================================================

Provide a method conceptually equivalent to:

    get_delayed_frame()

which:

    newest source timestamp
        ↓
    subtract delay
        ↓
    locate target
        ↓
    return frame/result

Do not hide failure.

Return a structured result if the target is unavailable.

============================================================
STEP 31 — NO DUPLICATE EVENT SYSTEM
============================================================

The delay buffer must not create a second event bus.

If delayed frames are eventually emitted:

use the existing EventBusManager.

Agent 10.16 may provide the delayed frame stream/handoff point, but should not
invent another event system.

============================================================
STEP 32 — EVENT SEMANTICS
============================================================

If protocol events are required, consider:

    DelayBufferReady
    DelayBufferStarved
    DelayBufferDegraded
    DelayConfigurationChanged

Only add events that provide real operational value.

Do not emit an event for every internal buffer operation.

============================================================
STEP 33 — METRICS
============================================================

Expose operational metrics/status.

At minimum:

    enabled
    configured_delay_ms
    actual_delay_ms
    oldest_timestamp
    newest_timestamp
    buffered_duration_ms
    frame_count
    capacity_ms
    state
    dropped_frames
    duplicate_frames
    late_frames
    gaps_detected
    last_frame_received_at
    last_source_timestamp

Reuse existing telemetry metrics conventions.

============================================================
STEP 34 — ACTUAL DELAY
============================================================

Distinguish:

    configured delay

from:

    actual available delay

Example:

    configured = 10s
    buffered = 6s

Then:

    actual_delay = 6s

and state:

    BUFFERING

Do not report 10 seconds of actual delay when only 6 seconds exists.

============================================================
STEP 35 — LATENCY
============================================================

Do not confuse:

    network/provider latency

with:

    intentional race delay

Expose them separately.

Example:

    source_to_receive_latency_ms
    configured_delay_ms
    actual_delay_ms

============================================================
STEP 36 — BACKPRESSURE
============================================================

Agent 10.14 already has bounded queue/backpressure.

Do not duplicate queue semantics unnecessarily.

The delay buffer's capacity policy is separate:

    ingestion queue capacity
    delay retention capacity

Keep those responsibilities clear.

============================================================
STEP 37 — OVERFLOW POLICY
============================================================

If frame-count capacity is reached, use deterministic behavior.

Preferred:

    evict oldest eligible frames

rather than:

    randomly discard frames.

Never silently violate the configured retention window.

============================================================
STEP 38 — OUT-OF-ORDER FRAMES
============================================================

Define behavior.

Recommended:

    accept only frames that do not violate the buffer's indexing invariant

or:

    insert into a bounded reorder window

Do NOT build a complicated distributed reorder system for this agent.

If an incoming frame is too old to safely insert:

    count as late
    reject deterministically

============================================================
STEP 39 — DUPLICATES
============================================================

Duplicate source timestamps/sequence frames must not cause duplicate delayed
frames.

Use existing sequence metadata where available.

Track:

    duplicate_frames

for diagnostics.

============================================================
STEP 40 — GAP DETECTION
============================================================

Do not replace Agent 10.14 gap detection.

The delay buffer may observe gap information for state/metrics.

Reuse existing gap semantics where possible.

============================================================
STEP 41 — PAUSE / RESUME
============================================================

Do not introduce replay-style play/pause semantics.

Live telemetry is driven by incoming source frames.

A future broadcaster may pause the delayed presentation, but that is outside
Agent 10.16.

============================================================
STEP 42 — DELAY CHANGE AT RUNTIME
============================================================

Determine whether changing:

    delay_ms

while LIVE is active is supported.

Prefer supporting it safely.

Example:

    10s → 20s

If enough buffered history exists:

    remain READY

Otherwise:

    BUFFERING

Example:

    20s → 5s

should immediately permit a smaller delayed target if available.

Do not discard data unnecessarily.

============================================================
STEP 43 — DELAY CHANGE SAFETY
============================================================

A delay change must never cause:

    negative timestamp
    future frame selection
    duplicate frame emission
    session contamination

============================================================
STEP 44 — TIMELINE INTEGRATION
============================================================

Agent 10.5 Timeline remains authoritative for the runtime's current temporal
position.

When live delay is active:

    TimelineMode = LIVE

The timeline position represents the delayed live presentation point, not a
new Timeline instance.

Do NOT introduce:

    TimelineMode.DELAYED

unless the existing architecture explicitly requires it.

LIVE remains LIVE.

============================================================
STEP 45 — TIMELINE SOURCE
============================================================

The delay buffer should provide the desired live presentation timestamp to the
existing TimelineService.

Conceptually:

    source latest = T
    delay = D
    delayed position = T-D

then:

    TimelineService.seek/update(delayed position)

using the existing public API.

Do not directly mutate private Timeline fields.

============================================================
STEP 46 — CACHE INTEGRATION
============================================================

When delayed presentation is active, Runtime Cache should reflect the delayed
frame, not the newest source frame.

However:

    do not modify CacheManager internals unnecessarily.

Use its existing apply/update APIs.

============================================================
STEP 47 — EVENT BUS INTEGRATION
============================================================

Do not let both:

    newest live frame

and:

    delayed frame

become authoritative runtime events.

There must be a clear source boundary.

If Agent 10.16 introduces delayed runtime emission:

    live source
        ↓
    buffer
        ↓
    delayed frame
        ↓
    existing EventBus

The raw live frame should not simultaneously drive the same delayed runtime.

============================================================
STEP 48 — RAW LIVE OBSERVABILITY
============================================================

It is acceptable to retain raw live telemetry metrics/logging.

Do not suppress provider diagnostics merely because runtime presentation is
delayed.

Distinguish:

    ingestion stream

from:

    delayed presentation stream.

============================================================
STEP 49 — CONTROL API
============================================================

Provide a thin API such as:

    enable()
    disable()
    configure(delay_ms)
    reset()
    get_status()
    get_delayed_frame()
    get_delayed_timestamp()

Use existing controller conventions.

Do not expose internal buffer structures.

============================================================
STEP 50 — APPLICATION CONTROLLER
============================================================

If the repository has a runtime application controller pattern, integrate the
delay buffer through a thin controller/facade.

Do not put business logic into protocol handlers.

Preferred:

    Command
       ↓
    Dispatcher
       ↓
    DelayController
       ↓
    DelayBuffer
       ↓
    Timeline / Cache / EventBus

============================================================
STEP 51 — COMMANDS
============================================================

Inspect the existing protocol catalogue first.

Only add commands if useful and consistent.

Potential commands:

    EnableLiveDelay
    DisableLiveDelay
    SetLiveDelay
    GetLiveDelayStatus

Do NOT implement REST/WebSocket.

============================================================
STEP 52 — SAFETY DEFAULT
============================================================

The default must preserve existing behavior.

Therefore:

    enabled = false

unless project configuration explicitly enables live delay.

An upgrade to RaceVision must not unexpectedly introduce a live race delay.

============================================================
STEP 53 — STARTUP
============================================================

On application startup:

    delay buffer exists/configures

but must not consume live telemetry until:

    LIVE session exists

and:

    delay feature is enabled.

============================================================
STEP 54 — LIVE SESSION START
============================================================

When LIVE starts:

    initialize buffer
    associate session identity
    begin retention

If delay is enabled:

    BUFFERING
       ↓
    READY

once enough telemetry history exists.

============================================================
STEP 55 — LIVE SESSION STOP
============================================================

When LIVE stops:

    stop accepting frames
    preserve metrics if appropriate
    release session resources
    clear/reset according to policy

Do not leak telemetry into a future session.

============================================================
STEP 56 — RECONNECT
============================================================

When Agent 10.14 reconnects:

determine whether the timeline remains continuous.

If not guaranteed:

    reset the delay buffer

Do not fabricate continuity.

Document behavior.

============================================================
STEP 57 — RECONNECT DELAY
============================================================

If reconnect produces:

    source timestamp discontinuity

the buffer must detect/reset/degrade according to policy.

Do not blindly concatenate unrelated telemetry streams.

============================================================
STEP 58 — THREAD / ASYNC SAFETY
============================================================

Use the existing runtime concurrency model.

The buffer must be safe under:

    frame append
    delayed lookup
    eviction
    reset
    configuration change

Do not introduce unnecessary locks if the runtime is already single-owner.

If locking is required, keep critical sections small.

============================================================
STEP 59 — PERFORMANCE
============================================================

The buffer is a high-frequency telemetry structure.

Avoid:

    O(n) lookup for every frame
    copying the entire buffer
    rebuilding indexes on every append
    unbounded memory

Prefer:

    O(1) append
    O(log n) timestamp lookup

where practical.

============================================================
STEP 60 — MEMORY
============================================================

Calculate/estimate memory usage.

Tests should verify:

    retention bounded
    max frame count bounded
    eviction works

Do not allow a long race to grow memory without bound.

============================================================
STEP 61 — TEST: BASIC APPEND
============================================================

Append canonical frames.

Verify:

    size
    oldest timestamp
    newest timestamp
    buffered duration

============================================================
STEP 62 — TEST: DELAY CALCULATION
============================================================

Example:

    frames:
        1000
        2000
        3000
        ...
        10000

delay:

    3000ms

Expected target:

    7000ms

Verify exact semantics.

============================================================
STEP 63 — TEST: BUFFERING
============================================================

Configure:

    delay = 10s

Provide only:

    5s

of history.

Expected:

    BUFFERING

not:

    READY.

============================================================
STEP 64 — TEST: READY
============================================================

Provide >= configured delay.

Expected:

    READY

and delayed frame is available.

============================================================
STEP 65 — TEST: ZERO DELAY
============================================================

Configure:

    delay = 0

Verify target equals newest available source timestamp.

============================================================
STEP 66 — TEST: EVICTION
============================================================

Configure finite retention.

Append enough frames.

Verify:

    oldest frames are evicted.

Verify:

    required delay history remains available.

============================================================
STEP 67 — TEST: DUPLICATES
============================================================

Insert duplicate frame.

Verify:

    deterministic behavior
    no duplicate delayed output
    metric increments

============================================================
STEP 68 — TEST: OUT-OF-ORDER
============================================================

Insert late frame.

Verify configured policy.

============================================================
STEP 69 — TEST: GAP
============================================================

Create timestamp gap.

Verify:

    existing gap semantics preserved
    buffer status/metrics reflect degradation if configured

============================================================
STEP 70 — TEST: STARVATION
============================================================

Stop source updates or advance beyond available buffer.

Verify:

    STARVED

or equivalent state.

Do not fabricate frames.

============================================================
STEP 71 — TEST: SESSION RESET
============================================================

Populate Session A.

Reset/start Session B.

Verify:

    no Session A frame is returned for Session B.

============================================================
STEP 72 — TEST: LIVE DISABLED
============================================================

With:

    enabled = false

verify existing LIVE behavior remains unchanged.

============================================================
STEP 73 — TEST: MODE TRANSITION
============================================================

Test:

    LIVE
      ↓
    REPLAY

Verify:

    buffer stops receiving frames
    replay remains authoritative
    TimelineMode remains REPLAY
    no live frame mutates replay state

============================================================
STEP 74 — TEST: RETURN TO LIVE
============================================================

Test:

    REPLAY
      ↓
    LIVE

Verify:

    delay buffer starts fresh according to policy
    no replay frame enters live delay buffer
    TimelineMode.LIVE

============================================================
STEP 75 — TEST: DELAY CHANGE
============================================================

Test:

    10s → 20s
    20s → 5s
    5s → 0

Verify correct readiness/target behavior.

============================================================
STEP 76 — TEST: CONCURRENCY
============================================================

Concurrent operations:

    append
    get_delayed_frame
    configure
    reset

must not corrupt buffer state.

============================================================
STEP 77 — TEST: LONG RUN
============================================================

Simulate a long live session.

Verify:

    memory remains bounded
    retention remains bounded
    indexes remain valid
    eviction remains correct

============================================================
STEP 78 — TEST: HIGH FREQUENCY
============================================================

Simulate high-frequency telemetry.

Verify:

    no pathological O(n) lookup
    no uncontrolled allocations
    acceptable runtime performance

============================================================
STEP 79 — TEST: TIMELINE
============================================================

Verify delayed target integrates through the existing TimelineService.

Expected:

    TimelineMode.LIVE

not a new mode.

============================================================
STEP 80 — TEST: CACHE
============================================================

Verify delayed runtime state reflects the delayed frame when delay is active.

Verify newest raw frame does not overwrite delayed presentation state.

============================================================
STEP 81 — TEST: EVENT BUS
============================================================

If delayed frame events are emitted:

verify:

    delayed frame → existing EventBus

and:

    raw live frame does not simultaneously become the delayed runtime frame.

============================================================
STEP 82 — TEST: RECONNECT
============================================================

Simulate LiveSessionAdapter reconnect.

Verify continuity policy.

If continuity cannot be guaranteed:

    reset/degrade buffer.

============================================================
STEP 83 — TEST: FAILURE
============================================================

Test:

    invalid configuration
    buffer overflow
    timestamp regression
    reset during append
    source disconnect
    mode transition during buffering

No corrupted state.

============================================================
STEP 84 — METRICS / STATUS TESTS
============================================================

Verify status fields accurately report:

    enabled
    state
    configured delay
    actual delay
    buffered duration
    oldest
    newest
    frame count
    capacity
    late frames
    duplicate frames
    gaps
    session identity

============================================================
STEP 85 — REGRESSION
============================================================

Run:

    Agent 10.6 tests
    Agent 10.7 tests
    Agent 10.8 tests
    Agent 10.9 tests
    Agent 10.10 tests
    Agent 10.11 tests
    Agent 10.12 tests
    Agent 10.13 tests
    Agent 10.14 tests
    Agent 10.15 tests

Also run:

    providers
    normalization
    timeline
    cache
    event bus
    runtime
    configuration
    database

Fix all regressions.

============================================================
STEP 86 — COVERAGE
============================================================

Target:

    >= 80%

for the Agent 10.16 package.

Prefer:

    >= 85%

where practical.

============================================================
STEP 87 — CODE QUALITY
============================================================

Follow RaceVision standards:

    Python 3.11
    PEP 8
    type hints
    dependency injection
    structured logging
    structured errors
    deterministic behavior
    bounded memory
    concurrency safety
    no global mutable state
    no circular imports

Run:

    Ruff
    mypy/type checking if configured
    pytest
    coverage

Use the project's actual commands from:

    pyproject.toml
    Makefile
    CI
    scripts

============================================================
STEP 88 — DOCUMENTATION
============================================================

Create:

    docs/specifications/RaceTimelineDelayBufferSpecification.md

Document:

    purpose
    architecture
    source timestamp semantics
    buffer model
    retention
    eviction
    delay calculation
    buffering state
    readiness
    starvation
    late frames
    duplicates
    gaps
    session isolation
    reconnect
    mode transitions
    Timeline integration
    Cache integration
    EventBus integration
    configuration
    metrics
    concurrency
    memory
    performance
    failure handling
    limitations
    future broadcaster integration

Update:

    docs/specifications/README.md
    docs/Architecture.md
    docs/Telemetry.md
    docs/Replay.md
    docs/Streaming.md
    docs/Roadmap.md

============================================================
STEP 89 — ROADMAP
============================================================

Mark:

    Agent 10.16 ✓

ONLY after implementation, tests, regression, coverage, linting, type checking,
and documentation are complete.

============================================================
STEP 90 — IMPORTANT SCOPE BOUNDARY
============================================================

Agent 10.16 is the FOUNDATION for live delay.

Do NOT implement:

    OBS delay
    Twitch delay
    Kick delay
    YouTube delay
    broadcaster synchronization
    camera delay controls
    audio delay controls
    REST
    WebSocket
    Unity UI
    Blender changes
    database persistence
    user authentication
    CDN buffering
    network packet shaping

Those belong to later agents.

============================================================
STEP 91 — ARCHITECTURAL INVARIANTS
============================================================

The following must remain true:

1. One unified Session Runtime.
2. One authoritative Timeline.
3. One authoritative Cache.
4. One Event Bus.
5. LIVE remains TimelineMode.LIVE.
6. REPLAY remains TimelineMode.REPLAY.
7. ReplayClock is not reused for live delay.
8. Source timestamp is authoritative for race time.
9. received_at is diagnostic, not race time.
10. Delay buffer is bounded.
11. Delay buffer is session isolated.
12. Raw live ingestion and delayed presentation are distinct stages.
13. Only delayed frames may mutate delayed runtime presentation.
14. Replay must never consume live delayed frames.
15. Live delay must never mutate replay state.
16. ModeController remains authoritative for LIVE/REPLAY transitions.
17. LiveSessionAdapter remains authoritative for live provider lifecycle.
18. ReplayController remains authoritative for replay lifecycle.
19. No second runtime.
20. No unbounded telemetry memory.
21. No invented telemetry.
22. No artificial vehicle physics.
23. No silent reconnect.
24. No transport implementation in 10.16.

============================================================
STEP 92 — FINAL ACCEPTANCE CRITERIA
============================================================

Agent 10.16 is COMPLETE only when:

[ ] Agent 10.5 Timeline is understood and reused.
[ ] DelayBuffer exists.
[ ] DelayBuffer is bounded.
[ ] Delay is source-time based.
[ ] received_at remains diagnostic.
[ ] Configurable delay exists.
[ ] Zero-delay mode works.
[ ] Buffering state exists.
[ ] Ready state exists.
[ ] Starvation/degradation behavior exists.
[ ] Timestamp lookup is deterministic.
[ ] Bracketing frames are supported.
[ ] Eviction works.
[ ] Duplicate policy exists.
[ ] Late-frame policy exists.
[ ] Gap behavior is defined.
[ ] Session isolation exists.
[ ] Reconnect behavior is defined.
[ ] LiveSessionAdapter integration exists.
[ ] ModeController integration exists.
[ ] Timeline integration exists.
[ ] Cache integration exists where required.
[ ] EventBus integration exists where required.
[ ] Delay can be configured safely.
[ ] Runtime delay changes are safe.
[ ] Memory is bounded.
[ ] High-frequency operation is tested.
[ ] Concurrency is tested.
[ ] LIVE → REPLAY isolation is tested.
[ ] REPLAY → LIVE isolation is tested.
[ ] No second runtime exists.
[ ] No second Timeline exists.
[ ] No second Cache exists.
[ ] No second EventBus exists.
[ ] No REST/WS/UI exists.
[ ] Tests pass.
[ ] Regression passes.
[ ] Coverage passes.
[ ] Ruff passes.
[ ] mypy/type checking passes where configured.
[ ] Documentation exists.
[ ] Roadmap updated.

============================================================
START IMPLEMENTATION
============================================================

First inspect the actual repository and Agent 10.5 Timeline implementation.

Then inspect Agent 10.14 LiveSessionAdapter and Agent 10.15 ModeController.

Implement the smallest clean delay-buffer foundation that integrates with those
existing components.

Do not rewrite completed agents.

Do not create a parallel runtime.

Do not implement transport/presentation.

Run focused tests.

Run the complete relevant regression suite.

Fix regressions.

Update documentation.

Mark Agent 10.16 complete only after all acceptance criteria pass.

============================================================
FINAL REPORT
============================================================

When complete, report:

1. Files created.
2. Files modified.
3. Agent 10.5 Timeline integration.
4. DelayBuffer architecture.
5. Timestamp semantics.
6. Delay calculation.
7. Buffer capacity.
8. Eviction policy.
9. Duplicate policy.
10. Late-frame policy.
11. Gap handling.
12. Buffer states.
13. LiveSessionAdapter integration.
14. ModeController integration.
15. Timeline integration.
16. Cache integration.
17. EventBus integration.
18. Session isolation.
19. Reconnect behavior.
20. Runtime delay configuration.
21. Metrics/status.
22. Memory/performance characteristics.
23. Tests added.
24. Focused test result.
25. Full regression result.
26. Coverage.
27. Ruff result.
28. mypy/type-check result.
29. Documentation updated.
30. Roadmap status.
31. Known limitations.
32. Recommended Agent 10.17.
```

## User

**Agent 10.16 is complete.** Bounded LIVE source-time delay buffer; default **off**; no second runtime/Timeline/Cache/EventBus; not OBS/transport.

### Architecture

```text
LiveSessionAdapter → (if delay enabled) RaceDelayBuffer → delayed floor frame
                         → Timeline(LIVE) / Cache / EventBus
```

When disabled: existing undelayed LIVE path.

### Key design

| Topic              | Choice                                            |
| ------------------ | ------------------------------------------------- |
| Authoritative time | Source `timestamp` (`T − delay_ms`)               |
| `received_at`      | Latency diagnostic only                           |
| Lookup             | Floor + bracketing                                |
| Late frames        | **REJECT**                                        |
| Duplicates         | Reject `(source_ms, sequence)`                    |
| States             | DISABLED / BUFFERING / READY / DEGRADED / STARVED |
| Timeline mode      | Remains **LIVE** (no DELAYED mode)                |
| Capacity           | `buffer_capacity_ms` + `max_frames` eviction      |

### Created / modified

- **Created:** `backend/runtime/delay/`, `shared/protocols/commands/delay/`, `tests/runtime/delay/`, `RaceTimelineDelayBufferSpecification.md`
- **Modified:** LiveSessionAdapter (`delay=` hook), ModeController (enter/leave LIVE), runtime exports, catalogue, Roadmap (10.16 ✓ → transport **10.17+**), Architecture/Telemetry/Replay/Streaming/specs README

### Integration

- **10.5 Timeline:** `seek` to delayed position; mode stays LIVE
- **10.14:** optional delay controller on accept path
- **10.15:** clear/unbind on LIVE→REPLAY; fresh bind on REPLAY→LIVE

### Quality

| Gate                        | Result         |
| --------------------------- | -------------- |
| Delay tests                 | **17 passed**  |
| Phase 10.6–10.16 regression | **187 passed** |
| Coverage                    | **84.65%**     |
| Ruff                        | clean          |
| mypy (`delay/`)             | clean          |

### Limitations

No OBS/platform delay, audio, REST/WS, UI, persistence, or replay delay stacking. Reconnect continuity → reset via live session lifecycle.

### Recommended Agent 10.17

**REST/WebSocket transport façades** — your choice.

## Assistant

**Agent 10.16 is accepted as complete.** The implementation is consistent with the RaceVision architecture and, importantly, keeps LIVE delay as a temporal buffer rather than creating another runtime.

### Phase 10.6 → 10.16

| Agent | Component | Status |
|---|---|---|
| 10.6 | Historical Telemetry Provider | ✅ |
| 10.7 | Replay Runtime Core | ✅ |
| 10.8 | Replay Controller | ✅ |
| 10.9 | Replay Synchronization | ✅ |
| 10.10 | Replay State Cache | ✅ |
| 10.11 | Replay Bookmark & Event System | ✅ |
| 10.12 | Replay Seeking & Time Navigation | ✅ |
| 10.13 | Replay Recording/Playback Validation | ✅ |
| 10.14 | Live Session Adapter | ✅ |
| 10.15 | Live/Replay Mode Controller | ✅ |
| **10.16** | **Race Timeline Delay Buffer** | **✅** |

### The important result

The temporal architecture is now:

```text
                    ┌─────────────────────┐
                    │   Live Telemetry    │
                    └──────────┬──────────┘
                               │
                               ▼
                    LiveSessionAdapter
                               │
                         delay enabled?
                         /           \
                       NO             YES
                       │               │
                       │        RaceDelayBuffer
                       │               │
                       │          T - delay
                       │               │
                       └───────┬───────┘
                               ▼
                       Unified Runtime
                               │
                 ┌─────────────┼─────────────┐
                 ▼             ▼             ▼
             Timeline        Cache        EventBus
               LIVE
```

That is the correct direction for RaceVision.

### 10.16 quality gate

The reported results are solid:

- **17** delay-specific tests
- **187** Phase 10.6–10.16 regression tests
- **84.65%** coverage
- Ruff clean
- mypy clean
- bounded retention
- source-time based delay
- deterministic floor lookup
- duplicate rejection
- late-frame rejection
- buffering/readiness/starvation states
- LIVE/REPLAY isolation
- session lifecycle reset
- no second runtime
- no second Timeline
- no second Cache
- no second EventBus

The particularly important invariant is:

> **LIVE delay remains `TimelineMode.LIVE`.**

That prevents the architecture from becoming unnecessarily fragmented.

### Current LIVE pipeline

You now effectively have:

```text
Provider
   │
   ▼
LiveSessionAdapter
   │
   ├── delay OFF ───────────────► Runtime
   │
   └── delay ON
          │
          ▼
     RaceDelayBuffer
          │
          ▼
     delayed source-time
          │
          ▼
     Timeline / Cache / EventBus
```

And switching remains:

```text
LIVE
 │
 │ 10.15
 ▼
REPLAY
 │
 │ 10.15
 ▼
LIVE
 │
 ▼
fresh delay-buffer binding
```

So replay cannot accidentally inherit the previous live buffer.

### One thing I would preserve going forward

**Do not turn 10.17 into a place where business logic gets moved into REST/WebSocket handlers.**

The transport layer should remain thin:

```text
REST / WebSocket
       │
       ▼
 Command Dispatcher
       │
       ▼
 Existing Controllers
       │
       ├── ReplayController
       ├── NavigationService
       ├── ModeController
       ├── LiveSessionAdapter
       └── DelayController
```

The existing runtime remains authoritative.

So **10.16 is a clean stopping point**, and RaceVision now has a proper foundation for a future configurable live race delay without prematurely coupling it to OBS, Twitch, Kick, YouTube, or Unity.

## User

Please give commands for Agent 10.17	Telemetry Interpolation & Gap Handling	Smooth missing/out-of-order historical/live frames ( 1 click copy and paste cursor friendly)

## Assistant

Yes. **Agent 10.17 should build on 10.14 + 10.16 and the existing normalization/timeline pipeline.** The critical architectural rule is: interpolation may create a *presentation-quality derived frame*, but it must never pretend fabricated data is authoritative telemetry.

Copy/paste the following directly into Cursor Agent:

```text
You are the Principal Distributed Systems Architect and Senior Python Engineer
working on the RaceVision project.

============================================================
RACEVISION — AGENT 10.17
TELEMETRY INTERPOLATION & GAP HANDLING
============================================================

OBJECTIVE
---------

Implement Agent 10.17 — Telemetry Interpolation & Gap Handling.

Purpose:

Provide deterministic handling of missing, sparse, delayed, duplicated, and
out-of-order telemetry frames for BOTH:

    LIVE telemetry
    HISTORICAL / REPLAY telemetry

The system must improve temporal continuity where safe by:

    - detecting gaps
    - detecting out-of-order frames
    - identifying interpolatable channels
    - generating bounded derived/interpolated frames
    - exposing gap quality/state
    - preserving authoritative source telemetry
    - preventing unsafe interpolation

This is a telemetry-quality layer.

It is NOT:

    - a physics simulator
    - a vehicle dynamics engine
    - a racing-line generator
    - a prediction model
    - an AI model
    - a Kalman filter
    - a machine-learning model
    - a second runtime
    - a second Timeline
    - a second Cache
    - a second Event Bus
    - a broadcaster transport
    - an OBS feature
    - a Unity presentation feature

============================================================
COMPLETED ARCHITECTURE
============================================================

Agents 10.6–10.16 are COMPLETE.

Current relevant architecture:

    HistoricalTelemetryProvider
            │
            ▼
    canonical telemetry
            │
            ▼
       Normalization
            │
            ▼
       Unified Runtime

LIVE:

    LiveSessionAdapter
            │
            ▼
    RaceDelayBuffer (optional)
            │
            ▼
       Unified Runtime

REPLAY:

    FastF1Provider
            │
            ▼
       Replay Runtime
            │
            ▼
       State Cache
            │
            ▼
       Unified Runtime

Existing temporal components:

    TimelineService
    ReplayClock
    RaceDelayBuffer
    ReplaySynchronizer

Agent 10.17 must integrate with these components.

DO NOT create:

    InterpolationRuntime
    GapRuntime
    PredictionRuntime
    InterpolatedTimeline
    InterpolatedCache
    InterpolatedEventBus

============================================================
STEP 1 — READ THE REPOSITORY FIRST
============================================================

Before modifying code, inspect the actual repository.

Read:

    docs/Roadmap.md
    docs/Architecture.md
    docs/Telemetry.md
    docs/Replay.md
    docs/Streaming.md

Read:

    docs/specifications/SoftwareRequirementsSpecification.md
    docs/specifications/SystemArchitectureSpecification.md

Read Agent 10.6:

    HistoricalTelemetryProviderSpecification.md

Read Agent 10.14:

    LiveSessionAdapterSpecification.md

Read Agent 10.16:

    RaceTimelineDelayBufferSpecification.md

Also inspect the existing:

    backend/normalization/
    backend/telemetry/
    backend/providers/
    backend/runtime/
    backend/runtime/live/
    backend/runtime/replay/
    backend/runtime/delay/
    backend/cache/
    backend/timeline/
    shared/protocols/

Search for:

    TelemetrySample
    TelemetryFrame
    CanonicalFrame
    NormalizedFrame
    source_timestamp
    received_at
    sequence
    gap
    interpolate
    normalize
    TimelineService
    RaceDelayBuffer
    LiveSessionAdapter
    ReplayService
    ReplayClock
    CacheManager
    EventBusManager

The repository is the source of truth.

Do not assume names above exist exactly.

============================================================
STEP 2 — UNDERSTAND EXISTING TELEMETRY MODEL
============================================================

Determine exactly how RaceVision represents a telemetry frame.

Identify:

    timestamp
    source_timestamp
    received_at
    sequence
    session_id
    driver_id
    car_id
    position
    speed
    heading
    orientation
    throttle
    brake
    gear
    RPM
    lap
    sector
    race position
    tyre data
    weather
    flags
    pit state
    damage
    any other channels

Do not create duplicate telemetry models.

Reuse the canonical telemetry model.

============================================================
STEP 3 — AUTHORITATIVE VS DERIVED DATA
============================================================

This is the most important rule for Agent 10.17.

Every frame must remain distinguishable as:

    AUTHORITATIVE
    DERIVED / INTERPOLATED

Never overwrite authoritative source telemetry with interpolated data.

Preferred conceptual model:

    source frame
        │
        ├── authoritative
        │
        └── derived interpolation

A derived frame must carry metadata such as:

    is_interpolated = true

or the repository's equivalent.

Also preserve:

    source_timestamp
    source_sequence where available
    interpolation source frames
    interpolation quality

Do not invent source sequence numbers that could be mistaken for provider
sequence numbers.

============================================================
STEP 4 — INTERPOLATION PACKAGE
============================================================

Create a package following repository conventions.

Preferred:

    backend/telemetry/interpolation/

Potential files:

    __init__.py
    interpolator.py
    gap_detector.py
    policies.py
    channel_policy.py
    frame_result.py
    quality.py
    settings.py
    status.py
    exceptions.py

Only create files that are actually needed.

Keep responsibilities separated.

============================================================
STEP 5 — GAP DETECTION
============================================================

Implement deterministic gap detection.

Given:

    frame A timestamp = T1
    frame B timestamp = T2

calculate:

    gap = T2 - T1

A gap exists when:

    gap > expected_interval + tolerance

Do NOT hard-code one universal telemetry frequency.

Telemetry providers may have different sample rates.

Use existing configured/sample-rate metadata where available.

============================================================
STEP 6 — EXPECTED SAMPLE INTERVAL
============================================================

Determine expected interval from the existing provider/session configuration.

Possible sources:

    provider sample_hz
    FastF1 settings
    LiveSession configuration
    telemetry metadata
    configured default

Prefer existing configuration.

Do not create a new independent global sample-rate authority.

============================================================
STEP 7 — GAP THRESHOLDS
============================================================

Support configurable thresholds.

At minimum:

    expected_interval_ms
    gap_tolerance_ms
    max_interpolation_gap_ms

Example:

    expected = 100ms
    tolerance = 20ms
    max interpolation = 500ms

Then:

    110ms → acceptable
    140ms → gap detected
    400ms → gap detected but interpolatable
    900ms → gap detected and NOT interpolatable

These are examples only.

Use project configuration conventions.

============================================================
STEP 8 — NEVER INTERPOLATE UNBOUNDED GAPS
============================================================

Interpolation must be bounded.

Never interpolate across:

    seconds
    minutes
    session boundaries
    race restarts
    unknown telemetry discontinuities

unless explicitly configured and proven safe.

Large gaps must produce:

    GAP_UNSAFE
    GAP_UNINTERPOLATED
    or existing equivalent.

============================================================
STEP 9 — BRACKETING FRAMES
============================================================

Interpolation requires:

    previous authoritative frame
    target timestamp
    next authoritative frame

Conceptually:

    A -------------------- B
    T1                     T2
              ↑
           target T

If:

    T1 <= T <= T2

then interpolation is possible subject to policy.

If there is no frame after T:

    DO NOT extrapolate by default.

If there is no frame before T:

    DO NOT interpolate.

============================================================
STEP 10 — NO EXTRAPOLATION BY DEFAULT
============================================================

Do NOT predict beyond the newest authoritative frame.

Therefore:

    target > newest source timestamp

must return:

    unavailable / not interpolatable

unless an explicit future agent introduces extrapolation.

Agent 10.17 is interpolation only.

============================================================
STEP 11 — INTERPOLATION MATHEMATICS
============================================================

For continuous scalar channels:

    alpha = (T - T1) / (T2 - T1)

    value = A + alpha * (B - A)

Examples:

    speed
    throttle
    brake
    RPM

Only interpolate channels for which linear interpolation is meaningful.

============================================================
STEP 12 — POSITION INTERPOLATION
============================================================

For position:

    x
    y
    z

linear interpolation may be used if the coordinate system and existing
telemetry model make this valid.

Do NOT automatically interpolate latitude/longitude if the project uses a
different coordinate model without checking existing implementation.

Respect the actual repository coordinate representation.

============================================================
STEP 13 — ANGLE INTERPOLATION
============================================================

Do NOT naïvely interpolate angles.

For example:

    359° → 1°

must produce approximately:

    0°

not:

    180°

Implement shortest-path angular interpolation where orientation/yaw requires
it.

Inspect the existing orientation model first.

============================================================
STEP 14 — QUATERNION INTERPOLATION
============================================================

If orientation uses quaternions:

use appropriate spherical interpolation semantics.

Do NOT component-wise linear interpolate normalized quaternions unless the
existing representation explicitly permits it.

If the repository does not currently use quaternions, do not introduce them.

============================================================
STEP 15 — DISCRETE CHANNELS
============================================================

Do NOT linearly interpolate discrete channels.

Examples:

    gear
    lap number
    sector number
    race position
    pit state
    flag state
    DRS state
    tyre compound
    driver identity
    car identity

Use deterministic policies such as:

    HOLD_PREVIOUS
    USE_NEXT
    NEAREST
    UNKNOWN

Choose appropriate policies per channel.

============================================================
STEP 16 — EVENT CHANNELS
============================================================

Do NOT interpolate events.

Examples:

    overtake
    collision
    pit entry
    pit exit
    incident
    lap completed
    sector completed

Events are edge-triggered/semantic data.

A missing event must not be invented by interpolation.

Existing Agent 10.11 event detection remains authoritative.

============================================================
STEP 17 — BOOLEAN CHANNELS
============================================================

Do not mathematically interpolate booleans.

Use policy.

Examples:

    brake_active
    pit_active
    DRS_active
    in_pit
    damage_flag

Prefer:

    previous value

unless the channel's semantics require another policy.

Document the decision.

============================================================
STEP 18 — ENUM CHANNELS
============================================================

Enums must not be numerically interpolated.

Examples:

    tyre_compound
    session_state
    flag
    pit_state

Use:

    previous
    next
    nearest
    unknown

according to channel semantics.

============================================================
STEP 19 — NULL CHANNELS
============================================================

If either bracketing frame lacks a channel:

do not invent the value.

Possible policies:

    use available value
    return unknown
    do not interpolate channel

Prefer conservative behavior.

============================================================
STEP 20 — CHANNEL POLICY
============================================================

Create an explicit channel policy registry.

Conceptually:

    speed       → LINEAR
    throttle    → LINEAR
    brake       → LINEAR
    RPM         → LINEAR
    position    → LINEAR
    heading     → ANGULAR
    gear        → HOLD
    lap         → HOLD/EDGE
    sector      → HOLD/EDGE
    race_order  → HOLD
    pit_state   → HOLD
    flags       → HOLD
    events      → NEVER

Do not blindly interpolate every field.

============================================================
STEP 21 — DERIVED FRAME METADATA
============================================================

A derived frame should identify:

    interpolation state
    source frame before
    source frame after
    interpolation alpha
    quality
    gap duration
    session identity

Do not alter original frame identity.

If the telemetry model cannot safely contain these fields, create a lightweight
wrapper/result rather than changing the canonical model unnecessarily.

============================================================
STEP 22 — QUALITY MODEL
============================================================

Create deterministic quality classification.

Suggested:

    AUTHORITATIVE
    INTERPOLATED_HIGH
    INTERPOLATED_MEDIUM
    INTERPOLATED_LOW
    UNAVAILABLE

Quality should depend on:

    gap duration
    channel completeness
    timestamp distance
    source integrity

Do not use subjective/random quality.

============================================================
STEP 23 — GAP STATES
============================================================

Provide explicit gap classification.

Suggested:

    NO_GAP
    GAP_ACCEPTABLE
    GAP_INTERPOLATABLE
    GAP_UNSAFE
    GAP_UNAVAILABLE

Reuse existing terminology if the repository already has equivalent states.

============================================================
STEP 24 — OUT-OF-ORDER HANDLING
============================================================

Agent 10.17 must handle historical and live out-of-order frames.

Do NOT duplicate Agent 10.14's ingestion sequence validation.

The interpolation layer observes ordered canonical frames.

For historical data:

    bounded reordering may be performed if safe.

For LIVE:

    late frames must not retroactively corrupt already-presented runtime state.

============================================================
STEP 25 — LIVE LATE FRAME POLICY
============================================================

When a late frame arrives:

    determine whether it belongs inside the interpolation window.

If it arrives before presentation has consumed that interval:

    it may be incorporated.

If the interval has already been emitted:

    do not rewrite runtime history by default.

Record:

    late frame
    dropped correction
    affected interval

according to existing metrics conventions.

============================================================
STEP 26 — HISTORICAL OUT-OF-ORDER POLICY
============================================================

Historical telemetry can be processed more deterministically.

If safe:

    reorder within a bounded window.

Then:

    gap detection
    interpolation

operate on ordered timestamps.

Do not reorder across:

    session boundary
    lap reset
    provider reset
    timestamp discontinuity

============================================================
STEP 27 — DUPLICATES
============================================================

Duplicates must not create artificial zero-length intervals.

Detect duplicates using existing:

    sequence
    source timestamp
    frame identity

where available.

Do not create duplicate interpolated frames.

============================================================
STEP 28 — TIMESTAMP REGRESSION
============================================================

If:

    T2 < T1

after ordering policy:

classify as:

    OUT_OF_ORDER
    TIMESTAMP_REGRESSION

Do not interpolate across an unresolved regression.

============================================================
STEP 29 — SESSION BOUNDARIES
============================================================

Never interpolate across:

    different session_id
    different race session
    different replay
    different event
    different driver/car identity where the frame model requires identity

A boundary must reset interpolation context.

============================================================
STEP 30 — LAP BOUNDARIES
============================================================

Do not automatically assume lap transitions are continuous for every channel.

At minimum:

    lap number = discrete

and:

    lap-completed event = semantic event

Do not interpolate lap number.

For vehicle position/speed, interpolation across a lap boundary may be allowed
ONLY if timestamps and session continuity prove the frames are adjacent.

============================================================
STEP 31 — PIT ENTRY / EXIT
============================================================

Do not interpolate pit-state transitions.

If:

    in_pit = false
    next = true

the interpolated frames may use the selected discrete policy, but must not
generate a synthetic PIT_ENTRY event.

Agent 10.11 remains authoritative for event detection.

============================================================
STEP 32 — COLLISIONS / INCIDENTS
============================================================

Never infer a collision merely because:

    position changes rapidly
    speed drops
    telemetry gap exists

Only existing authoritative incident flags/events may identify incidents.

============================================================
STEP 33 — OVERTAKES
============================================================

Do not generate synthetic overtakes from interpolation.

Race order remains discrete.

Agent 10.11 detector remains responsible for derived overtake events.

============================================================
STEP 34 — INTEGRATION WITH AGENT 10.16
============================================================

Agent 10.16:

    LiveSessionAdapter
        ↓
    RaceDelayBuffer
        ↓
    delayed frame

Agent 10.17 should integrate without replacing the delay buffer.

Preferred:

    LiveSessionAdapter
        ↓
    RaceDelayBuffer
        ↓
    ordered telemetry / gap handling
        ↓
    optional interpolation
        ↓
    existing Runtime

OR, if repository architecture indicates a better placement:

    LiveSessionAdapter
        ↓
    gap/interpolation
        ↓
    RaceDelayBuffer
        ↓
    Runtime

Choose based on the actual code.

Do not assume this ordering without inspecting the implementation.

The important invariant is:

    exactly one delay buffer
    exactly one interpolation layer
    exactly one runtime

============================================================
STEP 35 — REPLAY INTEGRATION
============================================================

Historical/replay telemetry must be able to use interpolation for presentation
where appropriate.

Do NOT alter:

    ReplayClock
    ReplayService
    ReplayNavigationService

Interpolation should supply missing temporal samples.

Replay authoritative frames remain authoritative.

============================================================
STEP 36 — REPLAY STATE CACHE
============================================================

Agent 10.10 checkpoints must remain deterministic.

A derived interpolated frame must not corrupt replay checkpoint semantics.

If validation or reconstruction requires authoritative frames:

    use authoritative frames.

If presentation requests an interpolated frame:

    use derived frame.

Do not store ephemeral interpolation as a permanent checkpoint unless explicitly
designed and documented.

============================================================
STEP 37 — REPLAY VALIDATION
============================================================

Agent 10.13 validation must continue to validate authoritative replay data.

Do not make validation fail simply because presentation interpolation exists.

If derived-frame fingerprints are added:

    keep them separate from authoritative fingerprints.

============================================================
STEP 38 — TIMELINE INTEGRATION
============================================================

Use the existing TimelineService.

Do not create another Timeline.

Timeline remains authoritative for:

    current runtime temporal position

Interpolation determines whether a frame can be produced at that position.

============================================================
STEP 39 — CACHE INTEGRATION
============================================================

Use existing CacheManager APIs.

Do not create:

    InterpolatedCache

When an interpolated frame is applied to presentation cache:

    preserve metadata indicating it is derived.

Do not overwrite authoritative provenance.

============================================================
STEP 40 — EVENT BUS
============================================================

Do not create a second EventBus.

Do NOT emit semantic events for every interpolated frame unless existing runtime
contracts explicitly require frame events.

If a frame event exists:

    mark derived/interpolated status.

Semantic events such as:

    OVERTAKE
    INCIDENT
    PIT
    LAP
    SECTOR

must not be synthesized merely because a frame was interpolated.

============================================================
STEP 41 — NORMALIZATION
============================================================

Interpolation should operate on canonical/normalized telemetry.

Do not interpolate raw provider-specific packet structures.

Preferred:

    Provider
       ↓
    Translation
       ↓
    Normalization
       ↓
    Canonical Frame
       ↓
    Gap/Interpolation

============================================================
STEP 42 — PROVIDER INDEPENDENCE
============================================================

The interpolation layer must not know FastF1-specific packet formats.

It should operate on canonical telemetry.

Do not add FastF1 logic to the interpolation package.

============================================================
STEP 43 — CONFIGURATION
============================================================

Use existing Pydantic configuration architecture.

Possible settings:

    enabled
    expected_interval_ms
    gap_tolerance_ms
    max_interpolation_gap_ms
    reorder_window_ms
    live_late_frame_policy
    historical_reorder_enabled
    interpolation_quality_threshold
    enable_position_interpolation
    enable_orientation_interpolation

Do not add unnecessary settings.

Defaults should preserve existing behavior.

Recommended:

    enabled = true for safe gap detection
    interpolation_enabled = false initially if required for backwards
    compatibility

If the project architecture supports safe interpolation by default, document
the choice.

============================================================
STEP 44 — BACKWARDS COMPATIBILITY
============================================================

When interpolation is disabled:

    existing telemetry behavior must remain unchanged.

Gap detection may still report diagnostics if enabled.

Do not alter authoritative frames.

============================================================
STEP 45 — INTERPOLATION ENABLE/DISABLE
============================================================

Provide a clear distinction:

    gap detection enabled
    interpolation enabled

These are not the same feature.

It must be possible to:

    detect gaps

without:

    generating derived frames.

============================================================
STEP 46 — CONTROLLER
============================================================

If appropriate, provide a thin controller/facade:

    get_status()
    configure()
    enable()
    disable()
    inspect_gap()
    interpolate()

Do not expose internal indexes.

Do not put interpolation logic into protocol handlers.

============================================================
STEP 47 — COMMANDS
============================================================

Inspect the existing protocol catalogue.

Only add commands if they have real runtime value.

Possible commands:

    GetTelemetryQuality
    ConfigureInterpolation
    EnableInterpolation
    DisableInterpolation

Do not implement REST/WebSocket.

============================================================
STEP 48 — STATUS
============================================================

Expose useful metrics.

At minimum:

    enabled
    interpolation_enabled
    frames_seen
    authoritative_frames
    interpolated_frames
    gaps_detected
    gaps_interpolated
    gaps_uninterpolated
    late_frames
    out_of_order_frames
    duplicate_frames
    largest_gap_ms
    average_gap_ms
    current_quality
    current_gap_state

Use existing metrics conventions.

============================================================
STEP 49 — OBSERVABILITY
============================================================

Log important transitions:

    gap detected
    gap interpolated
    unsafe gap
    late frame rejected
    out-of-order frame
    session boundary
    interpolation disabled

Do not log every frame at INFO.

Use DEBUG/TRACE for high-frequency details where supported.

============================================================
STEP 50 — PERFORMANCE
============================================================

Telemetry is high frequency.

Avoid:

    O(n) scan for every target
    rebuilding all indexes
    copying entire frame collections
    unbounded reorder windows

Preferred:

    timestamp-indexed lookup
    bounded reorder window
    efficient bracketing lookup

Target approximately:

    O(log n)

for frame lookup where practical.

============================================================
STEP 51 — MEMORY
============================================================

All reorder/interpolation buffers must be bounded.

Never retain an entire live session solely for interpolation.

Use:

    reorder_window_ms
    max_frames

or equivalent existing limits.

============================================================
STEP 52 — DETERMINISM
============================================================

Given identical:

    authoritative frames
    timestamps
    configuration

the interpolation result must be identical.

No:

    wall-clock dependence
    random values
    floating nondeterminism where avoidable
    provider-specific hidden state

============================================================
STEP 53 — FLOATING-POINT POLICY
============================================================

Use normal Python numeric behavior unless the project requires Decimal.

Document tolerances where equality is tested.

Do not introduce arbitrary rounding that changes telemetry.

============================================================
STEP 54 — FRAME IDENTITY
============================================================

Do not give an interpolated frame an identity that could be mistaken for an
authoritative provider frame.

If an ID is required:

    mark provenance clearly.

For example:

    frame_kind = AUTHORITATIVE / INTERPOLATED

or equivalent existing model semantics.

============================================================
STEP 55 — SOURCE PROVENANCE
============================================================

An interpolated frame should retain:

    source_frame_before
    source_frame_after
    target_timestamp
    alpha

or equivalent provenance.

This makes debugging and validation possible.

============================================================
STEP 56 — FUTURE PHYSICS BOUNDARY
============================================================

Do not calculate:

    acceleration-based physics
    tyre forces
    suspension
    aerodynamic effects
    steering dynamics
    collision response

Interpolation is mathematical temporal reconstruction only.

============================================================
STEP 57 — VEHICLE POSITION
============================================================

If vehicle position is interpolated:

verify the coordinate system first.

If the repository represents track position using:

    x/y/z

linear interpolation may be acceptable.

If it represents:

    distance along track

use that existing representation.

Do not invent track geometry logic.

============================================================
STEP 58 — ORIENTATION
============================================================

Use the existing orientation representation.

If:

    heading/yaw

use shortest angular interpolation.

If:

    quaternion

use appropriate quaternion interpolation.

If:

    orientation is unavailable

leave it unavailable rather than fabricate it.

============================================================
STEP 59 — SPEED
============================================================

Speed may use linear interpolation for small bounded gaps.

Do not extrapolate.

Do not derive speed from position unless the project explicitly requires that
as a fallback.

============================================================
STEP 60 — THROTTLE / BRAKE
============================================================

Only interpolate if these channels exist and their semantics permit it.

If values are percentages:

    0–100

or:

    0.0–1.0

respect the actual repository representation.

Clamp only if existing validation requires it.

============================================================
STEP 61 — RPM
============================================================

RPM may be linearly interpolated over short gaps.

For unsafe gaps:

    mark unavailable.

Do not create engine physics.

============================================================
STEP 62 — GEAR
============================================================

Gear is discrete.

Use:

    previous

or the repository's documented policy.

Never produce:

    5.5 gear.

============================================================
STEP 63 — LAP / SECTOR
============================================================

Lap and sector are discrete.

Never produce:

    lap = 12.4
    sector = 2.5

Use discrete policy.

Do not create lap/sector completion events.

============================================================
STEP 64 — RACE ORDER
============================================================

Race order is discrete.

Do not produce fractional race positions.

Do not create synthetic overtakes.

============================================================
STEP 65 — FLAGS
============================================================

Flags are discrete.

Do not interpolate:

    GREEN → YELLOW

as a numeric transition.

Use policy.

============================================================
STEP 66 — WEATHER
============================================================

If weather channels are included:

continuous values such as:

    temperature
    humidity
    wind speed

may be interpolated if appropriate.

Categorical conditions remain discrete.

Inspect the actual weather model before implementation.

============================================================
STEP 67 — TESTING STRATEGY
============================================================

Create:

    tests/telemetry/interpolation/

or the repository's equivalent.

Test the interpolation layer independently first.

Then integration tests.

============================================================
STEP 68 — BASIC GAP TEST
============================================================

Frames:

    0ms
    100ms
    200ms
    400ms

Expected:

    gap from 200 → 400 = 200ms

Verify detection.

============================================================
STEP 69 — NO GAP TEST
============================================================

Frames:

    0
    100
    200
    300

with expected interval:

    100ms

Verify:

    NO_GAP

============================================================
STEP 70 — SCALAR INTERPOLATION TEST
============================================================

Frame A:

    timestamp = 0
    speed = 100

Frame B:

    timestamp = 100
    speed = 200

Target:

    timestamp = 50

Expected:

    speed = 150

============================================================
STEP 71 — POSITION TEST
============================================================

A:

    x=0
    y=0
    z=0

B:

    x=10
    y=20
    z=30

target:

    50%

Expected:

    x=5
    y=10
    z=15

assuming repository coordinate semantics support this.

============================================================
STEP 72 — ANGLE WRAP TEST
============================================================

A:

    heading = 359°

B:

    heading = 1°

target:

    50%

Expected:

    approximately 0°

not:

    180°.

============================================================
STEP 73 — DISCRETE TEST
============================================================

A:

    gear = 5

B:

    gear = 6

target:

    50%

Expected:

    5 or documented discrete policy.

Never:

    5.5.

============================================================
STEP 74 — EVENT TEST
============================================================

A:

    no overtake event

B:

    overtake event

Interpolation must NOT produce:

    synthetic overtake event.

============================================================
STEP 75 — UNSAFE GAP TEST
============================================================

Configure:

    max_interpolation_gap_ms = 500

Gap:

    1000ms

Expected:

    GAP_UNSAFE

No interpolated frame.

============================================================
STEP 76 — NO EXTRAPOLATION TEST
============================================================

Newest frame:

    1000ms

request:

    1100ms

Expected:

    unavailable.

============================================================
STEP 77 — BEFORE-FIRST TEST
============================================================

First frame:

    1000ms

request:

    900ms

Expected:

    unavailable.

============================================================
STEP 78 — BRACKETING TEST
============================================================

Frames:

    100
    200

target:

    150

Expected:

    previous = 100
    next = 200

============================================================
STEP 79 — DUPLICATE TEST
============================================================

Provide duplicate source frames.

Verify:

    no zero-length interpolation
    no duplicate derived frames
    metric increments.

============================================================
STEP 80 — OUT-OF-ORDER TEST
============================================================

Provide:

    100
    300
    200

Verify configured bounded reorder behavior.

============================================================
STEP 81 — LATE LIVE FRAME TEST
============================================================

Simulate:

    100
    200
    300

then late:

    150

Verify it does not silently rewrite already-presented runtime state.

============================================================
STEP 82 — HISTORICAL REORDER TEST
============================================================

Historical input:

    100
    300
    200

If reorder enabled:

    ordered output = 100, 200, 300

Then gap detection operates correctly.

============================================================
STEP 83 — SESSION ISOLATION TEST
============================================================

Session A:

    100
    200

Session B:

    100
    200

Verify no interpolation uses:

    A frame + B frame.

============================================================
STEP 84 — REPLAY TEST
============================================================

Verify replay can request an interpolated presentation frame without modifying:

    ReplayClock
    authoritative ReplayService frames
    Replay State Cache checkpoints

============================================================
STEP 85 — LIVE TEST
============================================================

Verify:

    LiveSessionAdapter
       ↓
    gap/interpolation
       ↓
    existing runtime

works without creating a second runtime.

============================================================
STEP 86 — DELAY BUFFER TEST
============================================================

Verify Agent 10.16 interaction.

The delay buffer and interpolation layer must not:

    duplicate frames
    create competing timestamps
    cause infinite buffering
    create future frames

============================================================
STEP 87 — TIMELINE TEST
============================================================

Verify:

    TimelineMode.LIVE

remains unchanged for delayed LIVE telemetry.

For replay:

    TimelineMode.REPLAY

remains unchanged.

============================================================
STEP 88 — CACHE TEST
============================================================

Verify an interpolated frame can be applied through the existing CacheManager
without losing its derived provenance.

============================================================
STEP 89 — EVENT BUS TEST
============================================================

Verify no synthetic:

    overtake
    incident
    pit
    lap
    sector

events are produced merely from interpolation.

============================================================
STEP 90 — QUALITY TESTS
============================================================

Verify quality classification for:

    authoritative
    small gap
    medium gap
    unsafe gap
    missing channel

============================================================
STEP 91 — MEMORY TEST
============================================================

Run a long simulated live session.

Verify:

    reorder buffer bounded
    interpolation context bounded
    no memory leak

============================================================
STEP 92 — PERFORMANCE TEST
============================================================

Simulate high-frequency telemetry.

Measure:

    append
    gap detection
    lookup
    interpolation

Ensure no pathological O(n) behavior.

============================================================
STEP 93 — RESET TEST
============================================================

Reset:

    session
    provider
    live connection
    replay

Verify interpolation context is cleared.

============================================================
STEP 94 — MODE TRANSITION TEST
============================================================

Test:

    LIVE → REPLAY
    REPLAY → LIVE

Verify:

    no interpolation state leaks
    no live frames enter replay
    no replay frames enter live
    session identity is respected

============================================================
STEP 95 — REGRESSION
============================================================

Run all relevant tests:

    Agent 10.6
    Agent 10.7
    Agent 10.8
    Agent 10.9
    Agent 10.10
    Agent 10.11
    Agent 10.12
    Agent 10.13
    Agent 10.14
    Agent 10.15
    Agent 10.16

Also run:

    normalization
    providers
    telemetry
    timeline
    cache
    event bus
    runtime
    configuration

Fix all regressions.

Do not modify completed agents unnecessarily.

============================================================
STEP 96 — COVERAGE
============================================================

Target:

    >= 80%

Prefer:

    >= 85%

for the new interpolation package.

============================================================
STEP 97 — CODE QUALITY
============================================================

Follow RaceVision standards:

    Python 3.11
    PEP 8
    type hints
    dependency injection
    structured logging
    deterministic behavior
    bounded memory
    no global mutable state
    no circular imports

Run the repository's actual:

    pytest
    ruff
    mypy/type checking
    coverage

commands.

============================================================
STEP 98 — DOCUMENTATION
============================================================

Create:

    docs/specifications/TelemetryInterpolationGapHandlingSpecification.md

Document:

    purpose
    architecture
    canonical frame requirement
    authoritative vs derived data
    gap detection
    expected sample interval
    tolerance
    interpolation limits
    channel policies
    scalar interpolation
    position interpolation
    angular interpolation
    discrete channels
    event handling
    out-of-order handling
    duplicate handling
    late live frames
    historical reordering
    session boundaries
    LIVE integration
    REPLAY integration
    delay-buffer integration
    Timeline integration
    Cache integration
    EventBus integration
    quality
    metrics
    memory
    performance
    configuration
    failure handling
    limitations
    future work

Update:

    docs/specifications/README.md
    docs/Architecture.md
    docs/Telemetry.md
    docs/Replay.md
    docs/Streaming.md
    docs/Roadmap.md

============================================================
STEP 99 — ROADMAP
============================================================

Mark:

    Agent 10.17 ✓

ONLY after:

    implementation
    tests
    regression
    coverage
    Ruff
    mypy/type checking
    documentation

are complete.

============================================================
STEP 100 — ARCHITECTURAL INVARIANTS
============================================================

The following MUST remain true:

1. Authoritative telemetry is never overwritten.
2. Interpolated frames are explicitly derived.
3. No interpolation across unrelated sessions.
4. No unbounded interpolation gaps.
5. No extrapolation by default.
6. No synthetic events.
7. No synthetic overtakes.
8. No synthetic incidents.
9. No synthetic pit events.
10. No synthetic lap/sector completion events.
11. Discrete channels are never mathematically interpolated.
12. Angular channels use appropriate wrap-aware interpolation.
13. Provider-specific formats do not leak into interpolation.
14. Source timestamp remains authoritative.
15. received_at remains diagnostic.
16. ReplayClock remains authoritative for replay playback.
17. TimelineService remains authoritative for runtime position.
18. RaceDelayBuffer remains the live delay component.
19. No second runtime.
20. No second Timeline.
21. No second Cache.
22. No second EventBus.
23. No REST/WebSocket implementation.
24. No Unity/UI implementation.
25. No physics simulation.
26. No ML prediction.
27. No future-frame extrapolation.
28. Live late frames cannot silently rewrite presented history.
29. Historical reordering is bounded.
30. Memory remains bounded.
31. Results are deterministic.

============================================================
FINAL ACCEPTANCE CRITERIA
============================================================

Agent 10.17 is COMPLETE only when:

[ ] Repository and existing telemetry model inspected.
[ ] Agent 10.14 LiveSessionAdapter understood.
[ ] Agent 10.16 RaceDelayBuffer understood.
[ ] Canonical telemetry remains the interpolation input.
[ ] Gap detector implemented.
[ ] Expected sample interval is configurable/reused.
[ ] Gap tolerance exists.
[ ] Maximum interpolation gap exists.
[ ] Interpolation is bounded.
[ ] No extrapolation by default.
[ ] Scalar interpolation implemented.
[ ] Position interpolation implemented where safe.
[ ] Angular interpolation is wrap-aware.
[ ] Discrete channels are protected.
[ ] Event channels are protected.
[ ] Authoritative frames remain unchanged.
[ ] Derived frames are clearly marked.
[ ] Provenance is preserved.
[ ] Duplicate handling exists.
[ ] Out-of-order handling exists.
[ ] Live late-frame policy exists.
[ ] Historical reorder policy exists.
[ ] Session isolation exists.
[ ] Replay integration exists.
[ ] Live integration exists.
[ ] Delay-buffer integration exists.
[ ] Timeline integration exists.
[ ] Cache integration exists where required.
[ ] EventBus integration exists where required.
[ ] Quality classification exists.
[ ] Metrics/status exists.
[ ] Configuration exists.
[ ] Reset behavior exists.
[ ] Memory is bounded.
[ ] Performance is acceptable.
[ ] No second runtime exists.
[ ] No second Timeline exists.
[ ] No second Cache exists.
[ ] No second EventBus exists.
[ ] No physics simulation exists.
[ ] No ML prediction exists.
[ ] No transport exists.
[ ] Tests pass.
[ ] Full regression passes.
[ ] Coverage >= 80%.
[ ] Ruff clean.
[ ] mypy/type checking clean where configured.
[ ] Documentation complete.
[ ] Roadmap updated.

============================================================
START IMPLEMENTATION
============================================================

First inspect the actual repository.

Do NOT begin by creating files.

First understand:

    1. canonical telemetry model
    2. normalization pipeline
    3. Agent 10.14 LiveSessionAdapter
    4. Agent 10.16 RaceDelayBuffer
    5. Replay telemetry path
    6. TimelineService
    7. CacheManager
    8. EventBusManager

Then determine the cleanest integration point.

Implement the smallest deterministic interpolation/gap-handling layer that
fits the existing architecture.

Do not rewrite completed agents.

Do not create a parallel runtime.

Do not create a parallel timeline/cache/event bus.

Do not implement transport or presentation.

Run focused tests first.

Then run the complete relevant regression suite.

Fix all regressions.

Update documentation.

Mark Agent 10.17 complete only when every acceptance criterion passes.

============================================================
FINAL REPORT
============================================================

When complete, report:

1. Files created.
2. Files modified.
3. Canonical telemetry model used.
4. Integration point selected.
5. Gap detection architecture.
6. Expected interval source.
7. Gap thresholds.
8. Interpolation policies.
9. Channel policy table.
10. Scalar interpolation.
11. Position interpolation.
12. Angular interpolation.
13. Discrete channel handling.
14. Event protection.
15. Duplicate handling.
16. Out-of-order handling.
17. Live late-frame behavior.
18. Historical reorder behavior.
19. Authoritative/derived provenance.
20. Quality model.
21. Metrics/status.
22. Agent 10.14 integration.
23. Agent 10.16 integration.
24. Replay integration.
25. Timeline integration.
26. Cache integration.
27. EventBus integration.
28. Session isolation.
29. Memory characteristics.
30. Performance characteristics.
31. Tests added.
32. Focused test result.
33. Full regression result.
34. Coverage.
35. Ruff result.
36. mypy/type-check result.
37. Documentation updated.
38. Roadmap status.
39. Known limitations.
40. Recommended Agent 10.18.
```

## User

**Agent 10.17 is complete.** Gap detection is on by default; interpolation is off. Authoritative frames are never overwritten.

### 1–2. Files

**Created:** `backend/telemetry/interpolation/` (`__init__`, `enums`, `settings`, `exceptions`, `channel_policy`, `gap_detector`, `math_ops`, `window`, `interpolator`, `result`, `status`, `service`, `controller`); `tests/telemetry/interpolation/` (5 modules + conftest); `docs/specifications/TelemetryInterpolationGapHandlingSpecification.md`

**Modified:** `DelayController`, `LiveSessionAdapter`, telemetry protocol commands; docs (`Roadmap`, `Architecture`, `Telemetry`, `Replay`, `Streaming`, specs README, Delay Buffer spec)

### 3–8. Core design

- **Canonical model:** dict mappings (`timestamp`, `session_id`, `driver_id`, channels…)
- **Integration:** after delay / undelayed live observe → `TelemetryInterpolationService` → existing Runtime
- **Gaps:** `expected + tolerance`; states `NO_GAP` → `GAP_UNSAFE`
- **Interval:** `expected_interval_ms` (default 100); tolerance 20; max interpolate 500
- **Policies:** LINEAR / ANGULAR / HOLD\_PREVIOUS / NEVER

### 9–14. Channels

| Kind    | Channels                                             |
| ------- | ---------------------------------------------------- |
| LINEAR  | speed, throttle, brake, rpm, x/y/z                   |
| ANGULAR | heading/yaw (shortest path)                          |
| HOLD    | gear, lap/sector, race order, pit/flag/DRS, booleans |
| NEVER   | ids, sequence, events                                |

Events never synthesized. No extrapolation.

### 15–21. Robustness

Duplicates counted; historical bisect reorder; LIVE late → reject vs watermark; derived marked `is_interpolated` + provenance; quality HIGH/MEDIUM/LOW; metrics on `InterpolationStatus`

### 22–28. Integration

Optional on **10.14** & **10.16**; replay via `observe(historical=True)` without touching ReplayClock/checkpoints; Timeline/Cache/EventBus unchanged; session/driver isolation

### 29–36. Quality gates

Bounded `max_frames`; O(log n) brackets; **37** focused tests; **768** runtime+interpolation regression; **89%** package coverage; **Ruff** clean; **mypy** clean on package

### 37–40

Docs + Roadmap **10.17 ✓**; transport deferred to **10.18+**. Limitations: linear-only, interpolation default off, no physics/ML. **Recommended Agent 10.18:** Replay/live transport / presentation façades.

## Assistant

**Agent 10.17 is accepted as complete.** The implementation matches the intended RaceVision architecture and preserves the key invariant that **authoritative telemetry is never overwritten**.

### Phase 10.6 → 10.17

| Agent | Component | Status |
|---|---|---|
| 10.6 | Historical Telemetry Provider | ✅ |
| 10.7 | Replay Runtime Core | ✅ |
| 10.8 | Replay Controller | ✅ |
| 10.9 | Replay Synchronization | ✅ |
| 10.10 | Replay State Cache | ✅ |
| 10.11 | Replay Bookmark & Event System | ✅ |
| 10.12 | Replay Seeking & Time Navigation | ✅ |
| 10.13 | Replay Recording/Playback Validation | ✅ |
| 10.14 | Live Session Adapter | ✅ |
| 10.15 | Live/Replay Mode Controller | ✅ |
| 10.16 | Race Timeline Delay Buffer | ✅ |
| **10.17** | **Telemetry Interpolation & Gap Handling** | **✅** |

### The important architecture now

```text
                    TELEMETRY PROVIDERS
                           │
              ┌────────────┴────────────┐
              │                         │
          HISTORICAL                   LIVE
              │                         │
        FastF1 Provider         LiveSessionAdapter
              │                         │
              │                    DelayBuffer
              │                    (optional)
              │                         │
              └────────────┬────────────┘
                           │
                           ▼
                Telemetry Interpolation
                     / Gap Handling
                           │
                  ┌────────┴────────┐
                  │                 │
          authoritative        derived
             frames            frames
                  │                 │
                  └────────┬────────┘
                           ▼
                    Unified Runtime
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
          Timeline       Cache       EventBus
```

That's the architecture we wanted: **one telemetry path feeding one runtime**.

### Particularly good decisions

**1. Interpolation OFF by default**

This is conservative and appropriate. RaceVision can detect telemetry quality immediately without presenting fabricated data.

**2. Gap detection ON**

That gives us observability even when interpolation isn't being used.

**3. Authoritative data remains authoritative**

The distinction between:

```text
AUTHORITATIVE
INTERPOLATED
```

is essential for replay validation, debugging, statistics and eventually AI commentary.

**4. No extrapolation**

Correct decision. RaceVision should not claim to know where an F1 car is beyond the latest available telemetry.

**5. Discrete telemetry protected**

Things such as:

```text
gear
lap
sector
race order
pit state
flags
DRS
```

must not become fractional or mathematically fabricated.

**6. Events protected**

This is particularly important because Agent 10.11 already owns semantic replay events.

Interpolation must never manufacture:

```text
OVERTAKE
INCIDENT
PIT_ENTRY
PIT_EXIT
LAP_COMPLETED
SECTOR_COMPLETED
```

### Current temporal capabilities

RaceVision now has a surprisingly complete temporal foundation:

```text
                    SOURCE TELEMETRY
                           │
                           ▼
                 Normalization Layer
                           │
                           ▼
              ┌────────────────────────┐
              │ Gap / Quality Handling  │
              │ Agent 10.17             │
              └───────────┬────────────┘
                          │
             ┌────────────┴────────────┐
             │                         │
           LIVE                      REPLAY
             │                         │
       Delay Buffer               Replay Clock
         10.16                      10.7
             │                         │
             └────────────┬────────────┘
                          ▼
                  Unified Runtime
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
          Timeline       Cache       EventBus
             │
             ▼
       Synchronization
           10.9
             │
             ▼
       Replay Controls
        10.8 / 10.12
             │
             ▼
      State / Bookmarks
        10.10 / 10.11
             │
             ▼
        Validation
           10.13
```

### Quality gates

The reported **37 focused tests**, **768 regression tests**, **89% package coverage**, Ruff clean and mypy clean are a strong result.

The **768-test regression suite** is particularly important because 10.17 touches the live telemetry path as well as historical/replay processing.

### One architectural note for 10.18

I agree with the recommendation, but I would make **10.18 transport/presentation deliberately thin**.

The next layer should look approximately like:

```text
REST / WebSocket
       │
       ▼
Protocol Dispatcher
       │
       ▼
Application Controllers
       │
 ┌─────┼─────────────────────┐
 ▼     ▼                     ▼
Live  Replay              Mode
      Navigation           Control
       │
       ▼
Existing Runtime
```

It should **not** put business logic into HTTP/WebSocket handlers.

At this point, RaceVision has completed a substantial chunk of the difficult backend temporal architecture. The next major concern is exposing that architecture safely to the outside world rather than adding another internal runtime.

## User

Please give commands for Agent 10.18	Race State Snapshot Engine	Consistent point-in-time race snapshots ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. **Agent 10.18 should build the authoritative point-in-time snapshot layer above the existing unified Runtime**, while keeping Replay State Cache (10.10) separate: 10.10 is replay reconstruction/checkpoint state; 10.18 is the **race-wide coherent snapshot contract** that Live, Replay, Timeline, Cache and EventBus consumers can safely read.

Copy/paste this entire block into Cursor Agent:

```text
You are the Principal Distributed Systems Architect and Senior Python Engineer
working on the RaceVision project.

============================================================
RACEVISION — AGENT 10.18
RACE STATE SNAPSHOT ENGINE
============================================================

OBJECTIVE
---------

Implement Agent 10.18 — Race State Snapshot Engine.

Purpose:

Provide a deterministic, internally consistent, point-in-time snapshot of the
entire race state for downstream consumers.

A snapshot must represent one coherent runtime observation point containing,
where available:

    race/session state
    runtime time
    timeline position
    operating mode
    all active cars
    driver state
    vehicle state
    positions
    speed
    orientation
    lap/sector
    race order
    pit state
    flags
    telemetry quality/provenance
    weather
    active race events
    replay state
    delay/interpolation status
    snapshot metadata

The snapshot is intended to become the authoritative read model for future:

    REST
    WebSocket
    Unity
    overlays
    OBS
    replay UI
    dashboards
    AI commentary
    streaming presentation

This agent creates the snapshot engine only.

It must NOT implement:

    REST
    WebSocket
    Unity UI
    OBS integration
    Twitch/Kick/YouTube transport
    AI commentary
    rendering
    physics
    prediction
    a second runtime
    a second cache
    a second timeline
    a second event bus

============================================================
COMPLETED ARCHITECTURE
============================================================

Agents 10.6–10.17 are COMPLETE.

Relevant architecture:

    HistoricalTelemetryProvider
            │
            ▼
       Normalization
            │
            ▼
    Unified Runtime

LIVE:

    LiveSessionAdapter
            │
            ▼
    RaceDelayBuffer (optional)
            │
            ▼
    Telemetry Interpolation / Gap Handling
            │
            ▼
    Unified Runtime

REPLAY:

    Historical Provider
            │
            ▼
       Replay Runtime
            │
            ▼
      Replay State Cache
            │
            ▼
    Telemetry Interpolation / Gap Handling
            │
            ▼
    Unified Runtime

Existing authoritative runtime components include:

    CacheManager
    TimelineService
    EventBusManager
    LiveRuntime
    ReplayService
    ReplayClock
    ReplaySynchronizer
    ReplayStateCache
    RaceDelayBuffer
    TelemetryInterpolationService
    SessionManager

Agent 10.18 must compose these existing authorities.

DO NOT create replacements.

============================================================
CORE ARCHITECTURAL PRINCIPLE
============================================================

The Race State Snapshot Engine is a READ MODEL.

It does not become the owner of race state.

Conceptually:

    Existing Runtime Authorities
              │
       ┌──────┼────────┐
       ▼      ▼        ▼
     Cache  Timeline  Events
       │      │        │
       └──────┼────────┘
              ▼
      RaceStateSnapshot
              │
              ▼
        Snapshot Engine
              │
       ┌──────┼───────────────┐
       ▼      ▼               ▼
      API   WebSocket       Unity
     future    future        future

The snapshot engine observes authoritative runtime state and creates a
consistent immutable read model.

============================================================
STEP 1 — READ THE REPOSITORY FIRST
============================================================

Before creating files, inspect the actual repository.

Read:

    docs/Roadmap.md
    docs/Architecture.md
    docs/Telemetry.md
    docs/Replay.md
    docs/Streaming.md

Read:

    docs/specifications/SoftwareRequirementsSpecification.md
    docs/specifications/SystemArchitectureSpecification.md

Read:

    HistoricalTelemetryProviderSpecification.md
    ReplayRuntimeCoreSpecification.md
    ReplaySynchronizationSpecification.md
    ReplayStateCacheSpecification.md
    ReplayBookmarkEventSystemSpecification.md
    ReplaySeekingTimeNavigationSpecification.md
    ReplayRecordingPlaybackValidationSpecification.md
    LiveSessionAdapterSpecification.md
    LiveReplayModeControllerSpecification.md
    RaceTimelineDelayBufferSpecification.md
    TelemetryInterpolationGapHandlingSpecification.md

Inspect actual implementations of:

    backend/cache/
    backend/timeline/
    backend/runtime/
    backend/runtime/live/
    backend/runtime/replay/
    backend/runtime/mode/
    backend/runtime/delay/
    backend/telemetry/
    backend/session/
    shared/protocols/

Search for:

    CacheManager
    CacheSnapshot
    TimelineService
    TimelineSnapshot
    SessionManager
    LiveRuntime
    ReplayService
    ReplayStateCache
    ReplaySynchronizer
    RaceDelayBuffer
    TelemetryInterpolationService
    ReplayEventSystem
    ReplayBookmark
    RaceEvent
    TelemetrySample
    canonical frame
    state snapshot

The repository is the source of truth.

Do not invent replacement models if suitable existing models already exist.

============================================================
STEP 2 — DEFINE SNAPSHOT RESPONSIBILITY
============================================================

The snapshot engine answers:

    "What is the complete race state at one coherent runtime point?"

It must NOT answer:

    "What should the race state be?"

It only captures what the runtime currently knows.

Unknown data must remain explicitly unknown.

Do not silently convert:

    missing → zero
    missing → false
    missing → empty string
    missing → fake position
    missing → interpolated value

unless the existing domain model explicitly defines such defaults.

============================================================
STEP 3 — POINT-IN-TIME CONSISTENCY
============================================================

The most important requirement is consistency.

A snapshot must have one authoritative:

    runtime timestamp

and all included state must correspond to that point as closely as the
existing runtime architecture allows.

Conceptually:

    snapshot.runtime_ms = T

Then:

    timeline position ≈ T
    session state at T
    vehicle states at T
    replay state at T
    relevant events at T
    quality/provenance at T

Do not combine:

    car A from T
    car B from T+100
    timeline from T-500

without recording that inconsistency.

============================================================
STEP 4 — SNAPSHOT CONSISTENCY STRATEGY
============================================================

Inspect how CacheManager and TimelineService expose state.

Prefer an atomic/coordinated read if the existing runtime provides one.

If no atomic API exists, implement a controlled snapshot capture mechanism using
the existing runtime manager/lock conventions.

Do NOT introduce a second global lock hierarchy that can deadlock.

Preferred approach:

    acquire existing runtime read/coordinator lock
        ↓
    capture timeline
    capture cache
    capture session
    capture mode
    capture replay/live status
    capture quality
        ↓
    release lock
        ↓
    construct immutable snapshot

If the architecture is asynchronous, follow the repository's existing async
concurrency model.

============================================================
STEP 5 — SNAPSHOT ID
============================================================

Every snapshot should have a unique snapshot identity.

Prefer:

    UUID

or the repository's existing identifier convention.

Snapshot identity is not the same as:

    race/session ID
    replay ID
    telemetry frame ID

Do not reuse telemetry frame IDs as snapshot IDs.

============================================================
STEP 6 — SNAPSHOT VERSION
============================================================

Introduce a schema/version field.

Example:

    schema_version = "1.0"

Use the repository's existing version conventions if available.

This allows future REST/WebSocket/Unity clients to evolve safely.

============================================================
STEP 7 — SNAPSHOT TIMESTAMP
============================================================

Include at least:

    runtime_ms

and, where available:

    source_timestamp
    captured_at
    received_at

Important:

    runtime_ms

is the runtime's authoritative presentation position.

Do not replace it with wall-clock time.

============================================================
STEP 8 — MODE
============================================================

Snapshot must expose operating mode.

Use existing:

    SessionOperatingMode
    TimelineMode

Do not create a new competing mode enum.

Expected modes include:

    LIVE
    REPLAY

Historical mode semantics must remain compatible with the existing architecture.

============================================================
STEP 9 — SESSION IDENTITY
============================================================

Snapshot should identify:

    session_id
    race/event identity
    replay_id where applicable
    provider/source identity where available

Do not leak provider-specific implementation objects.

============================================================
STEP 10 — RACE STATE
============================================================

Capture existing race/session state.

Depending on the repository model, include:

    session type
    session state
    event name
    circuit/track
    lap
    total laps
    race status
    start/finish state
    session timing

Only include fields actually represented by the existing domain model.

Do not invent race metadata.

============================================================
STEP 11 — VEHICLE COLLECTION
============================================================

Snapshot must contain the current state of all known vehicles/cars.

Conceptually:

    cars: Mapping[DriverId, VehicleSnapshot]

Each vehicle snapshot should contain only fields available from runtime state.

Potential fields:

    driver_id
    car_id
    team_id
    position
    x
    y
    z
    orientation
    heading
    speed
    throttle
    brake
    gear
    rpm
    lap
    sector
    race_position
    pit_state
    tyre state
    flags
    telemetry quality
    provenance

Do not duplicate the canonical telemetry model unnecessarily.

Use lightweight snapshot/read-model types.

============================================================
STEP 12 — IMMUTABILITY
============================================================

Snapshots MUST be immutable after publication.

Preferred:

    frozen dataclasses
    immutable mappings
    tuples instead of mutable lists where appropriate

Do not expose internal mutable CacheManager structures directly.

A caller must not be able to modify runtime state by modifying a snapshot.

============================================================
STEP 13 — DEEP COPY / STRUCTURAL ISOLATION
============================================================

If runtime state contains mutable dictionaries/lists:

do not return them directly.

Use:

    immutable copies
    defensive copies
    immutable wrappers

according to project conventions.

The snapshot is a read model, not a live view.

============================================================
STEP 14 — TELEMETRY PROVENANCE
============================================================

Each vehicle snapshot should preserve telemetry provenance where available.

At minimum distinguish:

    AUTHORITATIVE
    INTERPOLATED

If Agent 10.17 exposes:

    quality
    interpolation state
    source timestamps

preserve that information.

Do not hide that a position is interpolated.

============================================================
STEP 15 — TELEMETRY QUALITY
============================================================

Include aggregate snapshot quality.

Example:

    EXCELLENT
    GOOD
    DEGRADED
    STALE
    UNKNOWN

Use existing project terminology if available.

Quality must be deterministic.

Do not invent subjective scores.

============================================================
STEP 16 — PER-VEHICLE QUALITY
============================================================

Include per-car quality when available.

Example:

    vehicle.telemetry_quality

and:

    vehicle.is_interpolated

or the existing equivalent.

A single degraded car should not necessarily make the entire race snapshot
invalid.

Aggregate quality should be derived according to a documented policy.

============================================================
STEP 17 — STALENESS
============================================================

Snapshot should be able to identify stale data.

Where existing runtime metadata supports it, include:

    source_age_ms
    data_age_ms
    stale = true/false

Do not use wall-clock assumptions where source/runtime time is authoritative.

============================================================
STEP 18 — TIMELINE STATE
============================================================

Include existing timeline information.

Potential:

    mode
    runtime_ms
    start_ms
    end_ms
    paused
    playback_rate
    source_timestamp

Do not duplicate TimelineService logic.

Create a snapshot projection from TimelineService.

============================================================
STEP 19 — REPLAY STATE
============================================================

When in REPLAY mode, expose existing replay state.

Potential:

    replay_id
    replay_state
    position_ms
    duration_ms
    frame_index
    playback_rate
    can_play
    can_pause
    can_seek
    synchronization state

Do not expose internal ReplayStateCache structures.

Use existing ReplayApplicationController status if appropriate.

============================================================
STEP 20 — LIVE STATE
============================================================

When LIVE:

include existing live status where available.

Potential:

    connected
    running
    sequence
    source timestamp
    latency
    gap state
    dropped frames
    delay state
    interpolation state

Do not create a second live status engine.

============================================================
STEP 21 — DELAY BUFFER STATE
============================================================

If Agent 10.16 delay is enabled, snapshot may expose:

    delay_enabled
    configured_delay_ms
    buffered_duration_ms
    buffer_state
    delayed_runtime_ms

Use existing DelayController/status APIs.

Do not copy internal buffer contents into the snapshot.

============================================================
STEP 22 — INTERPOLATION STATE
============================================================

Use Agent 10.17 status.

Expose useful summary:

    interpolation_enabled
    gaps_detected
    gaps_interpolated
    late_frames
    out_of_order_frames
    current_quality
    current_gap_state

Do not expose internal interpolation window structures.

============================================================
STEP 23 — EVENTS
============================================================

Snapshot may contain events relevant to the current point-in-time.

Examples:

    current events
    recent events
    active incidents
    latest lap event
    latest sector event
    latest pit event
    latest overtake

BUT:

Do not scan the entire event store on every snapshot.

Use existing Agent 10.11 event indexes.

Define an explicit bounded event window.

For example:

    events from T - event_window_ms through T

Do not make event window unlimited.

============================================================
STEP 24 — BOOKMARKS
============================================================

Snapshot may include the current/relevant replay bookmark information.

Do not include all bookmarks by default.

Use existing bookmark indexes.

If bookmarks are included:

    bounded
    deterministic
    read-only

============================================================
STEP 25 — WEATHER
============================================================

If weather state is already present in CacheManager/session state:

include it.

Do not create a new weather subsystem.

If unavailable:

    weather = None

or existing domain representation.

============================================================
STEP 26 — RACE EVENTS
============================================================

Race events must remain distinct from telemetry frames.

Do not create event objects from interpolated telemetry.

Use existing Agent 10.11 event system.

============================================================
STEP 27 — SNAPSHOT BOUNDARY
============================================================

Define a precise capture boundary.

Conceptually:

    T0 = capture start
    T1 = capture end

A snapshot should record enough metadata to determine whether capture was
coherent.

Possible:

    capture_sequence
    runtime_revision
    state_version

Use existing version counters if available.

============================================================
STEP 28 — REVISION / GENERATION
============================================================

If CacheManager or runtime already has:

    version
    revision
    generation

include it.

If not, introduce a minimal snapshot generation mechanism.

Do not create an independent state version for every domain component.

The snapshot generation must represent:

    "this snapshot was captured as one read operation."

============================================================
STEP 29 — CONSISTENCY VALIDATION
============================================================

Implement validation before publishing a snapshot.

Check:

    session identity consistent
    mode consistent
    runtime timestamp valid
    car identities unique
    no impossible duplicate driver/car entries
    replay identity consistent when replaying
    timeline mode compatible with operating mode

Do not perform physics validation.

============================================================
STEP 30 — SNAPSHOT VALIDITY
============================================================

Create explicit snapshot validity.

Possible:

    VALID
    DEGRADED
    INCONSISTENT

If the runtime cannot produce a coherent snapshot:

do not silently return a misleading "VALID" snapshot.

Return a structured result/error according to repository conventions.

============================================================
STEP 31 — PARTIAL SNAPSHOTS
============================================================

Determine whether the existing application requires partial snapshots.

Preferred:

    snapshot completeness metadata

Example:

    vehicles_complete
    timeline_complete
    session_complete
    events_complete

If a subsystem is unavailable:

    mark it unavailable

rather than fabricating data.

============================================================
STEP 32 — ATOMICITY
============================================================

Where possible, snapshot should be generated from one synchronized runtime
read.

Avoid:

    read car 1
    await
    read car 2
    await
    read timeline

because state may advance between reads.

Use existing lock/coordinator patterns.

============================================================
STEP 33 — ASYNC SAFETY
============================================================

Inspect whether:

    CacheManager
    TimelineService
    LiveRuntime
    ReplayService

are synchronous or asynchronous.

Match existing architecture.

Do not introduce unnecessary async wrappers.

============================================================
STEP 34 — THREAD SAFETY
============================================================

Snapshot reads must be safe under concurrent runtime updates.

Do not hold locks while performing:

    expensive serialization
    network operations
    logging
    external calls

Capture internal state under lock, then construct/serialize outside the lock.

============================================================
STEP 35 — PERFORMANCE
============================================================

Snapshots may eventually be produced at:

    10 Hz
    20 Hz
    30 Hz
    60 Hz

Design accordingly.

Avoid:

    O(n²)
    full event scans
    deep-copying entire runtime unnecessarily
    repeated provider calls

Prefer:

    O(number_of_cars + bounded_events)

per snapshot.

============================================================
STEP 36 — SNAPSHOT ENGINE PACKAGE
============================================================

Create a package following repository conventions.

Preferred:

    backend/runtime/snapshot/

Potential files:

    __init__.py
    engine.py
    models.py
    vehicle.py
    race.py
    timeline.py
    replay.py
    live.py
    events.py
    quality.py
    consistency.py
    result.py
    status.py
    exceptions.py
    settings.py

Only create files that are actually necessary.

Avoid excessive fragmentation.

============================================================
STEP 37 — SNAPSHOT MODEL
============================================================

Create a top-level immutable:

    RaceStateSnapshot

Potential conceptual structure:

    RaceStateSnapshot(
        snapshot_id,
        schema_version,
        session,
        runtime,
        timeline,
        mode,
        vehicles,
        events,
        weather,
        live,
        replay,
        delay,
        interpolation,
        quality,
        consistency,
        captured_at,
    )

Use actual repository types/conventions.

Do not blindly copy this structure if existing models suggest a better design.

============================================================
STEP 38 — VEHICLE SNAPSHOT
============================================================

Create:

    VehicleStateSnapshot

or equivalent.

It must be immutable.

It should represent the car state at snapshot time.

Do not make it an ORM model.

Do not couple it to PostgreSQL.

============================================================
STEP 39 — SESSION SNAPSHOT
============================================================

Create a lightweight session/race read model.

Do not duplicate:

    RaceSession ORM

unless the existing architecture explicitly uses ORM objects as read models.

The snapshot layer should remain persistence-agnostic.

============================================================
STEP 40 — EVENT SNAPSHOT
============================================================

If event projection is required, create an immutable event read model.

Preserve:

    event_id
    type
    timestamp
    driver/car identity
    source
    severity if existing

Do not expose mutable event-store objects.

============================================================
STEP 41 — SNAPSHOT ENGINE API
============================================================

Provide a minimal API such as:

    capture()
    capture_at_current_position()
    get_latest()
    validate(snapshot)
    status()

Do not add seek/replay controls here.

Snapshot engine reads state.

============================================================
STEP 42 — LATEST SNAPSHOT
============================================================

Maintain an optional latest snapshot reference.

If implemented:

    get_latest()

must return an immutable snapshot.

Replacing the latest snapshot must be atomic.

Do not retain an unbounded snapshot history.

============================================================
STEP 43 — SNAPSHOT HISTORY
============================================================

Do NOT create a full snapshot history in Agent 10.18.

Optional:

    bounded ring buffer

only if useful for consistency/debugging.

Default should be:

    latest snapshot only

or a small configurable bound.

Persistence is out of scope.

============================================================
STEP 44 — SNAPSHOT RATE
============================================================

Do not create a background publisher unless the repository architecture already
requires one.

Agent 10.18 primarily provides:

    on-demand capture

A future transport/presentation agent can request snapshots at a chosen rate.

============================================================
STEP 45 — SERIALIZATION
============================================================

Provide a safe serialization representation if the project already has a
protocol/model convention.

Preferred:

    dict / protocol DTO

Do not expose internal dataclass objects directly to future network clients.

Do not implement HTTP or WebSocket.

============================================================
STEP 46 — JSON SAFETY
============================================================

Ensure snapshot values can eventually be serialized.

Handle:

    UUID
    datetime
    enums
    tuples
    immutable mappings

using existing project serialization conventions.

Do not introduce a second serialization framework unnecessarily.

============================================================
STEP 47 — FLOATING POINT
============================================================

Do not arbitrarily round telemetry.

If serialization requires stable precision, use existing protocol conventions.

Snapshot equality tests must use appropriate tolerances where needed.

============================================================
STEP 48 — SOURCE TIMESTAMPS
============================================================

Preserve source timestamps separately from runtime time.

Important distinction:

    runtime_ms
    source_timestamp
    received_at

Do not collapse them into one field.

============================================================
STEP 49 — INTERPOLATED DATA
============================================================

If a vehicle state is interpolated by Agent 10.17:

snapshot must preserve:

    is_interpolated
    source/provenance
    quality

Do not convert derived state into authoritative state.

============================================================
STEP 50 — DELAYED LIVE
============================================================

For delayed LIVE:

    snapshot.runtime_ms

must represent the delayed runtime presentation position.

Do not expose future source telemetry as the current runtime state.

Where useful include:

    source_timestamp
    delayed_timestamp
    configured_delay_ms

according to existing delay model.

============================================================
STEP 51 — REPLAY
============================================================

For REPLAY:

snapshot runtime state must correspond to the authoritative ReplayService
position.

Do not independently calculate replay time.

Do not read raw replay frames directly if ReplayService already provides the
current state.

============================================================
STEP 52 — REPLAY CHECKPOINTS
============================================================

Do not replace Agent 10.10.

The relationship is:

    ReplayStateCache
        ↓
    ReplayService current state
        ↓
    RaceStateSnapshot

Agent 10.10 remains responsible for efficient replay reconstruction.

Agent 10.18 creates the race-wide read model.

============================================================
STEP 53 — REPLAY SYNCHRONIZATION
============================================================

If ReplaySynchronizer reports:

    synchronized

snapshot may be:

    VALID

If drift exists:

    snapshot consistency/quality must reflect that.

Do not silently suppress drift.

============================================================
STEP 54 — MODE TRANSITIONS
============================================================

Agent 10.15 owns:

    LIVE ↔ REPLAY

Snapshot engine must correctly observe transitions.

During transition:

    either capture the old committed state
    or return a structured unavailable/in-transition result

Do not produce a mixed:

    LIVE + REPLAY

snapshot.

============================================================
STEP 55 — SESSION TRANSITIONS
============================================================

Similarly:

    session A → session B

must never produce:

    car state from A
    race metadata from B

Use session identity checks.

============================================================
STEP 56 — EMPTY STATE
============================================================

Define behavior when no session is active.

For example:

    NoActiveSession

or an explicit empty snapshot state.

Do not invent:

    race = ""
    car positions = 0
    runtime = 0

unless repository conventions require it.

============================================================
STEP 57 — ERROR MODEL
============================================================

Create structured exceptions/results if needed.

Possible:

    SnapshotError
    SnapshotUnavailable
    SnapshotInconsistent
    SnapshotCaptureError
    SnapshotValidationError

Use existing error conventions.

Do not leak internal exceptions through the future transport layer.

============================================================
STEP 58 — CONFIGURATION
============================================================

Use existing Pydantic configuration.

Potential settings:

    enabled
    max_recent_events
    event_window_ms
    retain_latest
    max_history
    strict_consistency

Only implement settings that are genuinely required.

Recommended defaults:

    enabled = true
    retain_latest = true
    max_history = 1
    strict_consistency = true

But inspect existing configuration patterns before finalizing.

============================================================
STEP 59 — STATUS
============================================================

Expose snapshot engine status.

Potential:

    enabled
    snapshots_captured
    last_snapshot_id
    last_runtime_ms
    last_capture_duration_ms
    last_quality
    last_consistency
    active_session_id
    active_mode

Do not expose mutable internals.

============================================================
STEP 60 — METRICS
============================================================

Track:

    snapshots_captured
    snapshots_failed
    inconsistent_snapshots
    degraded_snapshots
    average_capture_ms
    max_capture_ms
    vehicles_captured
    events_captured

Use repository metrics conventions.

============================================================
STEP 61 — NO PERSISTENCE
============================================================

Agent 10.18 is in-memory.

Do not add:

    PostgreSQL tables
    Alembic migrations
    ORM models
    snapshot persistence

unless the repository already requires a specific persistence mechanism.

Future persistence can be added separately.

============================================================
STEP 62 — NO TRANSPORT
============================================================

Do not implement:

    REST
    WebSocket
    SSE
    GraphQL

The snapshot engine must be transport-independent.

============================================================
STEP 63 — NO UI
============================================================

Do not modify:

    Unity scenes
    Blender assets
    OBS scenes
    overlays

Only expose a clean backend read model for future consumers.

============================================================
STEP 64 — TESTING
============================================================

Create:

    tests/runtime/snapshot/

or the repository's equivalent.

Tests must cover:

    models
    immutability
    capture
    consistency
    session identity
    mode identity
    vehicle state
    timeline state
    replay state
    live state
    delay state
    interpolation state
    event projection
    quality
    status
    concurrency
    reset
    no-session behavior

============================================================
STEP 65 — BASIC SNAPSHOT TEST
============================================================

Create runtime state:

    session_id = A
    runtime_ms = 1000
    driver 1 position = known
    driver 2 position = known

Capture.

Verify:

    snapshot.session_id == A
    snapshot.runtime_ms == 1000
    both cars exist
    snapshot is immutable.

============================================================
STEP 66 — POINT-IN-TIME TEST
============================================================

Set:

    T = 1000

Capture.

Advance runtime to:

    T = 1100

Verify existing snapshot remains:

    T = 1000

Snapshots must be value objects, not live views.

============================================================
STEP 67 — SESSION ISOLATION TEST
============================================================

Capture session A.

Switch to session B.

Verify old snapshot remains A.

New snapshot is B.

No cross-session state.

============================================================
STEP 68 — MODE TEST
============================================================

Capture in:

    LIVE

Switch to:

    REPLAY

Capture again.

Verify:

    first.mode = LIVE
    second.mode = REPLAY

No mixed state.

============================================================
STEP 69 — REPLAY TEST
============================================================

Load replay.

Set replay position.

Capture.

Verify snapshot position matches ReplayService.

Do not modify replay position merely by capturing.

============================================================
STEP 70 — LIVE TEST
============================================================

Run live session.

Capture.

Verify snapshot contains current live state.

Do not create a second live runtime.

============================================================
STEP 71 — DELAY TEST
============================================================

Enable Agent 10.16 delay.

Capture.

Verify:

    delayed runtime position
    delay state
    source timestamp where available

are coherent.

============================================================
STEP 72 — INTERPOLATION TEST
============================================================

Provide an interpolated vehicle state from Agent 10.17.

Capture.

Verify:

    is_interpolated = true
    provenance retained
    quality retained

============================================================
STEP 73 — AUTHORITATIVE TEST
============================================================

Provide an authoritative frame.

Verify:

    is_interpolated = false
    provenance authoritative

============================================================
STEP 74 — EVENT TEST
============================================================

Create Agent 10.11 events.

Capture.

Verify relevant bounded events are included.

Verify:

    no duplicate events
    deterministic ordering

============================================================
STEP 75 — EVENT WINDOW TEST
============================================================

Events:

    T-10000
    T-1000
    T-100
    T+1000

with configured window:

    2000ms

Verify only appropriate events are included.

============================================================
STEP 76 — EVENT BOUNDARY TEST
============================================================

Verify events after the current runtime position are not presented as past
events unless the existing event semantics explicitly require them.

============================================================
STEP 77 — CONSISTENCY TEST
============================================================

Create deliberately inconsistent runtime state.

Verify:

    strict consistency detects it.

Do not return:

    VALID

for an inconsistent snapshot.

============================================================
STEP 78 — DUPLICATE DRIVER TEST
============================================================

Attempt to construct state containing duplicate driver identity.

Verify validation catches it.

============================================================
STEP 79 — DUPLICATE CAR TEST
============================================================

Attempt duplicate car identity.

Verify validation catches it.

============================================================
STEP 80 — REPLAY DRIFT TEST
============================================================

Force/reproduce ReplaySynchronizer drift.

Capture.

Verify snapshot reports degraded/inconsistent state according to policy.

============================================================
STEP 81 — EMPTY SESSION TEST
============================================================

No active session.

Capture.

Verify structured empty/unavailable result.

No fabricated cars.

============================================================
STEP 82 — IMMUTABILITY TEST
============================================================

Attempt:

    snapshot.vehicles[...] = ...

and mutation of nested values.

Verify mutation is prevented.

============================================================
STEP 83 — DEFENSIVE COPY TEST
============================================================

Mutate source CacheManager data after capture.

Verify snapshot remains unchanged.

============================================================
STEP 84 — LATEST SNAPSHOT TEST
============================================================

Capture snapshot A.

Capture snapshot B.

Verify:

    get_latest() == B

and A remains immutable.

============================================================
STEP 85 — BOUNDED HISTORY TEST
============================================================

If history is implemented:

verify configured bound.

Never allow unbounded snapshot growth.

============================================================
STEP 86 — CONCURRENCY TEST
============================================================

Run concurrent:

    telemetry updates
    snapshot capture

Verify:

    no corrupted snapshots
    no deadlocks
    no mixed session identity

Follow existing manager locks.

============================================================
STEP 87 — MODE TRANSITION CONCURRENCY
============================================================

Run:

    LIVE → REPLAY

while snapshot capture is requested.

Verify result is either:

    old coherent state

or:

    new coherent state

or:

    structured transition/unavailable result

Never:

    mixed LIVE/REPLAY snapshot.

============================================================
STEP 88 — SESSION TRANSITION CONCURRENCY
============================================================

Run session transition during snapshot capture.

Verify no cross-session snapshot.

============================================================
STEP 89 — SERIALIZATION TEST
============================================================

Serialize snapshot through existing project conventions.

Verify:

    UUID
    datetime
    enum
    immutable mapping
    tuple

are safely representable.

============================================================
STEP 90 — PERFORMANCE TEST
============================================================

Simulate:

    20 cars

and a realistic event window.

Measure capture time.

Avoid unnecessary full runtime copies.

Target:

    O(cars + bounded events)

per capture.

============================================================
STEP 91 — MEMORY TEST
============================================================

Run many captures.

Verify memory does not grow unbounded.

If retaining latest only:

    old snapshots become collectible.

============================================================
STEP 92 — RESET TEST
============================================================

Reset runtime/session.

Verify:

    latest snapshot cleared or explicitly invalidated

according to configured lifecycle.

No state leakage into next session.

============================================================
STEP 93 — DETERMINISM
============================================================

Given identical runtime state:

    snapshot projection must be deterministic

except for intentionally unique:

    snapshot_id
    capture wall-clock metadata

Snapshot content must otherwise be equivalent.

============================================================
STEP 94 — REGRESSION
============================================================

Run all relevant tests:

    Agent 10.6
    Agent 10.7
    Agent 10.8
    Agent 10.9
    Agent 10.10
    Agent 10.11
    Agent 10.12
    Agent 10.13
    Agent 10.14
    Agent 10.15
    Agent 10.16
    Agent 10.17

Also run:

    database
    repositories
    normalization
    providers
    telemetry
    timeline
    cache
    event bus
    runtime
    configuration

Do not break completed agents.

============================================================
STEP 95 — COVERAGE
============================================================

Target:

    >= 80%

Prefer:

    >= 85%

for the new snapshot package.

============================================================
STEP 96 — CODE QUALITY
============================================================

Follow RaceVision standards:

    Python 3.11
    PEP 8
    type hints
    SQLAlchemy conventions where applicable
    Pydantic configuration
    dependency injection
    structured logging
    deterministic behavior
    bounded memory
    immutable read models
    no global mutable state

Run:

    pytest
    ruff
    mypy/type checking
    coverage

using the repository's actual commands.

============================================================
STEP 97 — DOCUMENTATION
============================================================

Create:

    docs/specifications/RaceStateSnapshotEngineSpecification.md

Document:

    purpose
    architecture
    read-model responsibility
    point-in-time consistency
    snapshot identity
    schema version
    runtime timestamp
    session identity
    operating mode
    vehicle snapshots
    timeline projection
    replay projection
    live projection
    delay projection
    interpolation projection
    event projection
    weather
    quality
    consistency
    immutability
    concurrency
    lifecycle
    configuration
    metrics
    performance
    memory
    limitations
    future transport usage

Update:

    docs/specifications/README.md
    docs/Architecture.md
    docs/Telemetry.md
    docs/Replay.md
    docs/Streaming.md
    docs/Roadmap.md

============================================================
STEP 98 — ARCHITECTURAL INVARIANTS
============================================================

The following MUST remain true:

1. Snapshot Engine is a read model.
2. Existing Runtime remains authoritative.
3. CacheManager remains authoritative for cached race state.
4. TimelineService remains authoritative for runtime time.
5. ReplayService remains authoritative for replay position.
6. ReplayStateCache remains authoritative for replay checkpoints.
7. LiveSessionAdapter remains authoritative for live ingestion lifecycle.
8. RaceDelayBuffer remains authoritative for live temporal delay.
9. TelemetryInterpolationService remains authoritative for interpolation
   provenance.
10. EventSystem remains authoritative for replay events.
11. No second runtime exists.
12. No second Cache exists.
13. No second Timeline exists.
14. No second EventBus exists.
15. Snapshot objects are immutable.
16. Snapshot objects are isolated from runtime mutable state.
17. Snapshot identity is separate from telemetry frame identity.
18. Runtime time is separate from source timestamp.
19. received_at remains diagnostic.
20. Session identity is preserved.
21. LIVE and REPLAY state cannot be mixed.
22. Historical and live state cannot be mixed.
23. Interpolated data remains marked derived.
24. Authoritative data remains authoritative.
25. Synthetic events are never created.
26. No physics simulation occurs.
27. No prediction occurs.
28. No ML occurs.
29. No REST occurs.
30. No WebSocket occurs.
31. No Unity/UI implementation occurs.
32. No OBS implementation occurs.
33. Snapshot history remains bounded.
34. Event projection remains bounded.
35. Snapshot capture does not move runtime state.
36. Snapshot capture does not seek replay.
37. Snapshot capture does not advance live telemetry.
38. Snapshot capture is deterministic apart from identity/capture metadata.
39. Snapshot consistency is explicitly validated.
40. Inconsistent state is never silently presented as VALID.

============================================================
FINAL ACCEPTANCE CRITERIA
============================================================

Agent 10.18 is COMPLETE only when:

[ ] Repository inspected first.
[ ] Existing CacheManager inspected and reused.
[ ] Existing TimelineService inspected and reused.
[ ] Existing SessionManager inspected and reused.
[ ] Existing LiveRuntime inspected and reused.
[ ] Existing ReplayService inspected and reused.
[ ] Existing ReplaySynchronizer inspected and reused.
[ ] Existing ReplayStateCache inspected and reused.
[ ] Existing DelayBuffer inspected and reused.
[ ] Existing InterpolationService inspected and reused.
[ ] Existing EventSystem inspected and reused.
[ ] Immutable RaceStateSnapshot implemented.
[ ] Immutable VehicleStateSnapshot implemented.
[ ] Session identity included.
[ ] Runtime timestamp included.
[ ] Source timestamp preserved.
[ ] Operating mode included.
[ ] Timeline projection included.
[ ] Live projection included.
[ ] Replay projection included.
[ ] Delay state included where available.
[ ] Interpolation state/provenance included where available.
[ ] Vehicle collection implemented.
[ ] Event projection implemented if supported.
[ ] Weather projection implemented if supported.
[ ] Quality model implemented.
[ ] Consistency validation implemented.
[ ] LIVE/REPLAY mixing prevented.
[ ] Session mixing prevented.
[ ] Snapshot immutability verified.
[ ] Defensive copying verified.
[ ] Latest snapshot implemented.
[ ] Snapshot history bounded.
[ ] Status implemented.
[ ] Metrics implemented.
[ ] Empty-session behavior implemented.
[ ] Concurrency tested.
[ ] Mode transition tested.
[ ] Session transition tested.
[ ] Replay tested.
[ ] Live tested.
[ ] Delay tested.
[ ] Interpolation tested.
[ ] Event system tested.
[ ] Serialization tested.
[ ] Performance tested.
[ ] Memory tested.
[ ] Reset tested.
[ ] Determinism tested.
[ ] Full regression passes.
[ ] Coverage >= 80%.
[ ] Ruff clean.
[ ] mypy/type checking clean where configured.
[ ] Documentation complete.
[ ] Roadmap updated.
[ ] No transport implemented.
[ ] No UI implemented.
[ ] No second runtime created.

============================================================
START IMPLEMENTATION
============================================================

FIRST:

Inspect the repository and existing implementations.

Do NOT immediately create the snapshot package.

Determine:

    1. Where authoritative race state currently lives.
    2. How CacheManager exposes consistent state.
    3. How TimelineService exposes current time.
    4. How LiveRuntime exposes live state.
    5. How ReplayService exposes replay state.
    6. How ReplaySynchronizer exposes synchronization state.
    7. How Agent 10.16 exposes delay status.
    8. How Agent 10.17 exposes telemetry quality.
    9. How Agent 10.11 exposes events.
    10. What locking/versioning mechanisms already exist.

Then implement the smallest clean read-model layer that composes these existing
authorities.

Do not rewrite completed agents.

Do not create a parallel state system.

Do not create persistence.

Do not create transport.

Run focused tests first.

Then run the complete relevant regression suite.

Fix regressions.

Update documentation.

Mark Agent 10.18 complete only when every acceptance criterion passes.

============================================================
FINAL REPORT
============================================================

When complete, report:

1. Files created.
2. Files modified.
3. Authoritative state sources identified.
4. Snapshot architecture.
5. Snapshot schema.
6. Snapshot identity.
7. Schema version.
8. Runtime timestamp semantics.
9. Session identity semantics.
10. LIVE/REPLAY mode handling.
11. Vehicle snapshot design.
12. Timeline projection.
13. Live projection.
14. Replay projection.
15. Delay projection.
16. Interpolation projection.
17. Event projection.
18. Weather projection.
19. Quality model.
20. Consistency model.
21. Immutability strategy.
22. Defensive-copy strategy.
23. Concurrency strategy.
24. Snapshot lifecycle.
25. Latest snapshot behavior.
26. History/memory policy.
27. Status/metrics.
28. Serialization behavior.
29. Agent 10.10 integration.
30. Agent 10.11 integration.
31. Agent 10.14 integration.
32. Agent 10.15 integration.
33. Agent 10.16 integration.
34. Agent 10.17 integration.
35. Tests added.
36. Focused test result.
37. Full regression result.
38. Coverage.
39. Ruff result.
40. mypy/type-check result.
41. Documentation updated.
42. Roadmap status.
43. Known limitations.
44. Recommended Agent 10.19.
```

## User

**Agent 10.18 complete.** Immutable race read model over existing authorities — no second runtime/cache/timeline, no transport/UI.

### Final report

1. **Created:** `backend/runtime/snapshot/` (engine, models, consistency, quality, controller, settings, enums, result/status, exceptions); `tests/runtime/snapshot/`; `shared/protocols/commands/snapshot/`; `docs/specifications/RaceStateSnapshotEngineSpecification.md`

2. **Modified:** command catalogue; Roadmap, Architecture, Telemetry, Replay, Streaming, specs README

3. **Authorities:** CacheManager export/snapshot, TimelineService, SessionManager, ModeController, LiveSessionAdapter, Replay status/sync, DelayController, InterpolationService, Agent 10.11 `events_between`

4–8. **Architecture:** compose → validate → freeze → optional `get_latest()`; schema `1.0`; UUID `snapshot_id`; `runtime_ms` = presentation position (delayed LIVE uses delayed timestamp)

9–10. **Session/mode:** `SessionOperatingMode`; transitioning → unavailable; no LIVE+REPLAY mix

11–18. **Projections:** frozen `VehicleStateSnapshot`; timeline/live/replay/delay/interpolation summaries; bounded events; weather from cache if present

19–23. **Quality/consistency:** EXCELLENT→UNKNOWN, VALID/DEGRADED/INCONSISTENT; engine `RLock`; defensive copies from cache dicts

24–28. **Lifecycle:** on-demand capture; latest-only; metrics/status; `to_serializable()` JSON-safe

29–34. **Integrations:** 10.10 status-only (no payload); 10.11 windowed events; 10.14–10.17 via optional DI hooks

35–42. **Tests:** 31 focused; **779** runtime+interpolation regression; **89%** coverage; **Ruff** clean; **mypy** clean; docs + Roadmap **10.18 ✓**

43. **Limits:** not full MVCC; no persistence/history publisher; weather only if already in cache

44. **Recommended Agent 10.19:** REST/WebSocket (or presentation) façades consuming `RaceStateSnapshot`

## Assistant

Understood. **Agent 10.18 is now treated as complete and part of the RaceVision baseline.**

The important architectural point is that we now have a clean progression:

```text
Telemetry Providers
      │
      ▼
Normalization / Validation
      │
      ▼
Unified Runtime
 ┌────┼─────────────────────────────┐
 │    │                             │
 ▼    ▼                             ▼
LIVE  REPLAY                    Historical
 │      │                           │
 │      └─ Replay State Cache       │
 │                                  │
 └──────┬───────────────────────────┘
        ▼
Delay / Interpolation
        │
        ▼
Cache + Timeline + Event Bus
        │
        ▼
Mode / Synchronization
        │
        ▼
Race State Snapshot Engine  ← Agent 10.18
        │
        ▼
   Future presentation
 REST / WebSocket / Unity / OBS
```

### Current Phase 10 position

| Agent | Component | Status |
|---|---|---|
| 10.6 | Historical Telemetry Provider | ✅ |
| 10.7 | Replay Runtime Core | ✅ |
| 10.8 | Replay Controller | ✅ |
| 10.9 | Replay Synchronization | ✅ |
| 10.10 | Replay State Cache | ✅ |
| 10.11 | Replay Bookmark & Event System | ✅ |
| 10.12 | Replay Seeking & Time Navigation | ✅ |
| 10.13 | Replay Recording/Playback Validation | ✅ |
| 10.14 | Live Session Adapter | ✅ |
| 10.15 | Live/Replay Mode Controller | ✅ |
| 10.16 | Race Timeline Delay Buffer | ✅ |
| 10.17 | Telemetry Interpolation & Gap Handling | ✅ |
| **10.18** | **Race State Snapshot Engine** | **✅** |

So the next logical architectural layer is indeed **10.19**, but importantly it should **consume `RaceStateSnapshot` rather than reach into CacheManager, ReplayService, LiveSessionAdapter, etc. directly**.

That gives us a very clean boundary:

```text
                    ┌───────────────────┐
                    │ Unified Runtime   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ RaceStateSnapshot │
                    │     Agent 10.18   │
                    └─────────┬─────────┘
                              │
                 ┌────────────┴────────────┐
                 ▼                         ▼
          REST / HTTP                 WebSocket
                 │                         │
                 └────────────┬────────────┘
                              ▼
                    Future Unity / OBS /
                    Overlay / Streaming
```

**That separation is important for RaceVision:** the presentation/transport layer should never become another source of truth.

memcite

## User

Please give commands for Agent 10.19	Phase 10 Integration	End-to-end Session → Timeline → Replay/Live validation ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. **Agent 10.19 should be the Phase 10 integration gate**: prove that the components from 10.1–10.18 work together through the **unified Session Runtime**, without introducing another runtime or changing individual agent responsibilities.

Copy/paste the entire block below into Cursor Agent:

```text
You are the Principal Distributed Systems Architect and Senior Python Engineer
working on the RaceVision project.

============================================================
RACEVISION — AGENT 10.19
PHASE 10 INTEGRATION
============================================================

OBJECTIVE
---------

Implement Agent 10.19 — Phase 10 Integration.

This is the END-TO-END INTEGRATION AND VALIDATION AGENT for Phase 10.

The purpose is to prove that the completed Phase 10 architecture works as one
coherent system across:

    Session
      ↓
    Timeline
      ↓
    Historical Telemetry
      ↓
    Replay
      ↓
    Live Session
      ↓
    Delay
      ↓
    Interpolation / Gap Handling
      ↓
    Mode Switching
      ↓
    Replay Synchronization
      ↓
    Replay State Cache
      ↓
    Replay Events / Bookmarks
      ↓
    Replay Navigation
      ↓
    Replay Validation
      ↓
    Race State Snapshot
      ↓
    End-to-End Runtime State

Agent 10.19 is primarily an integration and validation layer.

Do NOT create a second runtime.

Do NOT rewrite completed agents.

Do NOT duplicate CacheManager, TimelineService, EventBus, ReplayService,
LiveSessionAdapter, DelayBuffer, InterpolationService, or SnapshotEngine.

============================================================
CRITICAL ARCHITECTURAL RULE
============================================================

RaceVision has ONE unified Session Runtime.

The integration architecture must remain:

    Session
       │
       ▼
    Timeline
       │
       ├───────────────┐
       ▼               ▼
    Historical       Live
       │               │
       ▼               ▼
    Replay         LiveSessionAdapter
       │               │
       ▼               ▼
    Replay State     Delay
    Cache              │
       │               ▼
       └──────────→ Interpolation
                        │
                        ▼
                 Cache / EventBus
                        │
                        ▼
                 RaceStateSnapshot

Replay and Live are operating modes of the same runtime architecture.

There must never be:

    LiveRuntime #1
    ReplayRuntime #2
    IntegrationRuntime #3

============================================================
COMPLETED PHASE 10 BASELINE
============================================================

Agents already complete:

    10.6  Historical Telemetry Provider
    10.7  Replay Runtime Core
    10.8  Replay Controller
    10.9  Replay Synchronization
    10.10 Replay State Cache
    10.11 Replay Bookmark & Event System
    10.12 Replay Seeking & Time Navigation
    10.13 Replay Recording/Playback Validation
    10.14 Live Session Adapter
    10.15 Live/Replay Mode Controller
    10.16 Race Timeline Delay Buffer
    10.17 Telemetry Interpolation & Gap Handling
    10.18 Race State Snapshot Engine

Treat the actual repository implementation as authoritative.

============================================================
STEP 1 — INSPECT THE REPOSITORY
============================================================

Before writing code, inspect:

    docs/Roadmap.md
    docs/Architecture.md
    docs/Telemetry.md
    docs/Replay.md
    docs/Streaming.md

Read all Phase 10 specifications:

    docs/specifications/

Specifically locate:

    HistoricalTelemetryProviderSpecification.md
    ReplayRuntimeCoreSpecification.md
    ReplayControllerSpecification.md
    ReplaySynchronizationSpecification.md
    ReplayStateCacheSpecification.md
    ReplayBookmarkEventSystemSpecification.md
    ReplaySeekingTimeNavigationSpecification.md
    ReplayRecordingPlaybackValidationSpecification.md
    LiveSessionAdapterSpecification.md
    LiveReplayModeControllerSpecification.md
    RaceTimelineDelayBufferSpecification.md
    TelemetryInterpolationGapHandlingSpecification.md
    RaceStateSnapshotEngineSpecification.md

Inspect actual implementations.

Do not assume the filenames/classes from earlier specifications are unchanged.

============================================================
STEP 2 — IDENTIFY ACTUAL AUTHORITIES
============================================================

Determine the actual authoritative components in the repository.

At minimum inspect:

    SessionManager
    TimelineService
    CacheManager
    EventBusManager
    LiveRuntime
    LiveSessionAdapter
    ReplayService
    ReplayApplicationController
    ReplayNavigationService
    ReplaySynchronizer
    ReplayStateCache
    ReplayEventSystem
    ReplayValidationService
    RaceDelayBuffer / DelayController
    TelemetryInterpolationService
    ModeController
    RaceStateSnapshotEngine

Document the actual dependency flow.

Do not introduce replacements.

============================================================
STEP 3 — DEFINE INTEGRATION SCOPE
============================================================

Agent 10.19 must validate the complete lifecycle:

    SESSION START
         ↓
    TIMELINE INITIALIZATION
         ↓
    HISTORICAL LOAD
         ↓
    REPLAY
         ↓
    REPLAY CONTROL
         ↓
    REPLAY SEEK
         ↓
    REPLAY EVENT NAVIGATION
         ↓
    SNAPSHOT
         ↓
    LIVE TRANSITION
         ↓
    LIVE INGESTION
         ↓
    OPTIONAL DELAY
         ↓
    OPTIONAL INTERPOLATION
         ↓
    SNAPSHOT
         ↓
    LIVE → REPLAY
         ↓
    REPLAY VALIDATION
         ↓
    SESSION RESET / SHUTDOWN

Every transition must preserve runtime invariants.

============================================================
STEP 4 — DO NOT IMPLEMENT TRANSPORT
============================================================

Agent 10.19 must NOT implement:

    REST
    WebSocket
    HTTP
    SSE
    Unity
    OBS
    Twitch
    Kick
    YouTube
    AI commentary
    rendering

Transport is a separate architectural concern.

If transport already exists in the repository, integration tests may test it
only if appropriate, but do not expand its implementation in this agent.

============================================================
STEP 5 — CREATE PHASE 10 INTEGRATION PACKAGE
============================================================

Create a minimal package following repository conventions.

Preferred:

    backend/runtime/integration/

Potential:

    __init__.py
    phase10.py
    scenarios.py
    result.py
    status.py
    exceptions.py

Only create files that are genuinely needed.

The integration package must orchestrate existing components.

It must NOT become a new runtime.

============================================================
STEP 6 — INTEGRATION RESULT
============================================================

Create an immutable result model representing an integration run.

Conceptually:

    Phase10IntegrationResult

Include:

    integration_id
    started_at
    completed_at
    passed
    scenarios
    failures
    warnings
    final_mode
    final_session_id
    final_runtime_ms
    snapshot_id
    metrics

Use existing project conventions where appropriate.

============================================================
STEP 7 — SCENARIO MODEL
============================================================

Create a structured scenario result.

Conceptually:

    IntegrationScenarioResult

Fields may include:

    name
    status
    duration_ms
    assertions
    failures
    warnings
    metadata

Statuses should be explicit.

For example:

    PASS
    FAIL
    SKIPPED
    DEGRADED

Do not use arbitrary strings if the repository uses enums.

============================================================
STEP 8 — END-TO-END TEST FIXTURE
============================================================

Build deterministic integration fixtures.

The fixture must use:

    InMemoryFastF1Client
    InMemoryLiveProvider

or the actual repository test doubles.

Do NOT contact:

    real F1 servers
    external telemetry APIs
    F1 official systems
    internet services

Integration tests must be deterministic and offline.

============================================================
STEP 9 — TEST SESSION INITIALIZATION
============================================================

Create a deterministic test session.

Example conceptual identity:

    session_id = known UUID

Use existing SessionManager APIs.

Verify:

    session created
    session identity stable
    session state initialized
    Timeline initialized
    Cache initialized
    EventBus available

Do not bypass SessionManager by directly mutating internals.

============================================================
STEP 10 — TIMELINE INITIALIZATION
============================================================

Verify the session starts with the correct Timeline state.

Validate:

    timeline mode
    runtime position
    start boundary
    end boundary
    session association

No negative time.

No stale previous-session timeline.

============================================================
STEP 11 — HISTORICAL TELEMETRY LOAD
============================================================

Load deterministic historical telemetry using Agent 10.6.

Verify:

    provider request accepted
    canonical frames produced
    source timestamps preserved
    session identity preserved
    driver identity preserved
    frame ordering is valid
    normalization succeeds
    validation succeeds

No production network calls.

============================================================
STEP 12 — HISTORICAL → REPLAY
============================================================

Load historical frames into ReplayService.

Verify:

    ReplayState = LOADED
    replay_id exists
    frame count correct
    start position correct
    end position correct
    Timeline mode = REPLAY
    session identity preserved

Replay must use the existing ReplayService.

============================================================
STEP 13 — REPLAY PLAYBACK
============================================================

Run:

    play
    tick
    pause
    resume
    tick
    stop

Verify:

    state transitions are correct
    runtime position advances correctly
    paused replay does not advance
    stopped replay does not unexpectedly advance
    playback rate is respected

Do not use wall-clock sleeps.

Use deterministic ReplayClock/tick behavior.

============================================================
STEP 14 — REPLAY STEP
============================================================

Test:

    step_forward
    step_backward

Verify:

    exactly one frame movement
    no negative position
    no movement beyond replay bounds
    Timeline remains synchronized
    Cache remains consistent

============================================================
STEP 15 — REPLAY SEEK
============================================================

Test:

    seek(start)
    seek(midpoint)
    seek(end)
    seek(before_start)
    seek(after_end)

Verify:

    correct clamping
    deterministic reconstruction
    Timeline synchronization
    Cache reconstruction
    ReplayStateCache checkpoint use
    no state leakage

============================================================
STEP 16 — REPLAY STATE CACHE
============================================================

Verify Agent 10.10 integration.

Capture/check:

    baseline
    checkpoints
    frame index
    snapshot index
    restore

Compare checkpoint reconstruction with full reconstruction.

They must produce equivalent durable race state.

Do not require raw internal snapshot object identity.

============================================================
STEP 17 — REPLAY SYNCHRONIZATION
============================================================

After:

    load
    seek
    step
    tick
    reset

verify:

    ReplaySynchronizer status

is synchronized within the configured tolerance.

Default expected tolerance:

    1 ms

or the actual repository configuration.

============================================================
STEP 18 — REPLAY EVENTS
============================================================

Load telemetry containing deterministic events.

Verify Agent 10.11 produces:

    laps
    sectors
    overtakes
    incidents
    pit entry
    pit exit

only when the input data supports them.

Do not invent events.

Verify deterministic event IDs.

Verify repeated seek does not duplicate derived events.

============================================================
STEP 19 — REPLAY BOOKMARKS
============================================================

Create bookmarks through the public controller API.

Verify:

    create
    read
    update
    delete
    jump-to-bookmark

Bookmark identity must remain associated with the replay.

Verify bookmarks do not leak across replay IDs.

============================================================
STEP 20 — REPLAY NAVIGATION
============================================================

Exercise Agent 10.12:

    fast-forward
    rewind
    jump-to-start
    jump-to-end
    jump-to-lap
    jump-to-sector
    jump-to-event
    next-event
    previous-event
    next-bookmark
    previous-bookmark

Verify every operation:

    uses ReplayService
    updates Timeline
    updates Cache
    updates synchronization
    does not change operating mode unexpectedly
    preserves PAUSED state where appropriate

============================================================
STEP 21 — REPLAY VALIDATION
============================================================

Run Agent 10.13 validation against the deterministic replay.

Verify:

    timestamps valid
    telemetry valid
    indexes valid
    reconstruction valid
    playback valid
    navigation valid
    synchronization valid
    events valid
    bookmarks valid
    deterministic fingerprints valid

No mutation of replay state should remain after validation.

============================================================
STEP 22 — SNAPSHOT IN REPLAY
============================================================

Use Agent 10.18.

Capture RaceStateSnapshot while replay is:

    LOADED
    PAUSED
    PLAYING
    after seek

Verify:

    mode = REPLAY
    session identity correct
    runtime_ms equals authoritative replay position
    vehicle states correspond to runtime position
    events are bounded
    snapshot is immutable
    snapshot does not alter replay state

============================================================
STEP 23 — LIVE SESSION INITIALIZATION
============================================================

Create a deterministic live session using:

    InMemoryLiveProvider

Do not use a real F1 feed.

Verify:

    LiveSessionAdapter lifecycle
    session identity
    Timeline mode = LIVE
    Cache reset/initialization
    EventBus integration
    live status

============================================================
STEP 24 — LIVE INGESTION
============================================================

Inject deterministic live frames.

Verify:

    frame accepted
    source timestamp preserved
    sequence accepted
    Cache updated
    Timeline updated
    EventBus receives the appropriate event
    Session identity preserved

============================================================
STEP 25 — LIVE SEQUENCE VALIDATION
============================================================

Inject:

    valid sequence
    duplicate sequence
    sequence gap
    out-of-order frame

Verify existing Agent 10.14 behavior.

Expected:

    duplicate rejected
    gap detected/degraded
    invalid ordering handled according to policy

Do not rewrite LiveSessionAdapter.

============================================================
STEP 26 — LIVE DELAY
============================================================

Enable Agent 10.16 delay.

Inject enough frames to satisfy the delay buffer.

Verify:

    BUFFERING
    READY
    delayed output
    source timestamp
    delayed runtime position
    Timeline remains LIVE
    Cache receives delayed state

Do not create DELAYED Timeline mode.

============================================================
STEP 27 — LIVE INTERPOLATION
============================================================

Enable Agent 10.17 interpolation.

Create deterministic telemetry gap.

Verify:

    gap detected
    interpolation occurs only when configured
    authoritative frames remain unchanged
    interpolated frame has provenance
    no extrapolation occurs
    events are not synthesized

Verify integration after:

    delay → interpolation → runtime

when both are enabled.

============================================================
STEP 28 — LIVE SNAPSHOT
============================================================

Capture Agent 10.18 snapshot while LIVE.

Verify:

    mode = LIVE
    session identity correct
    runtime_ms corresponds to live presentation time
    delayed state is represented if delay enabled
    interpolation metadata preserved
    vehicle states immutable
    quality is correct

============================================================
STEP 29 — LIVE → REPLAY TRANSITION
============================================================

Use Agent 10.15 ModeController.

Transition:

    LIVE → REPLAY

Verify exact sequence:

    live stops
    delay is unbound/reset
    live state is cleared appropriately
    cache is cleared
    replay loads
    Timeline becomes REPLAY
    replay starts in the expected state
    no live ingestion continues
    no mixed LIVE/REPLAY snapshot exists

This is a critical integration test.

============================================================
STEP 30 — REPLAY → LIVE TRANSITION
============================================================

Transition:

    REPLAY → LIVE

Verify:

    replay stops/pauses according to policy
    replay state no longer drives Timeline
    cache cleared
    explicit LiveSessionRequest used
    live provider starts
    Timeline becomes LIVE
    fresh live state accepted
    no stale replay state leaks into live snapshot

============================================================
STEP 31 — FAILED MODE TRANSITION
============================================================

Create a deterministic target-mode startup failure.

For example:

    live provider fails to connect

Attempt:

    REPLAY → LIVE

Verify:

    structured failure
    rollback according to configured policy
    authoritative mode remains coherent
    no half-committed state
    no mixed snapshot

Do not silently reconnect.

============================================================
STEP 32 — SESSION RESET
============================================================

Reset/close the session.

Verify:

    Cache cleared
    Timeline reset
    EventBus state isolated
    Replay state cleared where appropriate
    Delay state reset
    interpolation state reset
    snapshot latest state cleared/invalidated
    no old session data leaks

============================================================
STEP 33 — SESSION ISOLATION
============================================================

Create:

    Session A
    Session B

Run replay/live operations independently.

Verify:

    no telemetry crossover
    no replay bookmarks crossover
    no events crossover
    no snapshot crossover
    no cache crossover
    no timeline crossover

============================================================
STEP 34 — DRIVER ISOLATION
============================================================

Use multiple drivers.

Verify:

    telemetry remains associated with correct driver
    vehicle state remains correct
    events are associated with correct driver
    snapshot vehicles have unique driver identity

============================================================
STEP 35 — SOURCE TIMESTAMP INTEGRITY
============================================================

Across historical, replay, and live flows verify:

    source timestamp

is never replaced by:

    received_at
    wall-clock time
    delayed presentation time

Delayed presentation time must remain separately represented.

============================================================
STEP 36 — AUTHORITATIVE VS DERIVED DATA
============================================================

Verify:

    authoritative telemetry remains authoritative
    interpolated telemetry is marked derived
    replay reconstruction does not convert derived data into authoritative data
    events remain event objects
    snapshots preserve provenance

============================================================
STEP 37 — SNAPSHOT CONSISTENCY
============================================================

For every major phase:

    historical
    replay
    live
    delayed live
    interpolated live
    mode transition

capture RaceStateSnapshot.

Verify:

    session identity
    mode
    runtime_ms
    vehicle states
    timeline
    quality
    event projection

are internally consistent.

============================================================
STEP 38 — NO SECOND RUNTIME ASSERTION
============================================================

Add architectural tests/assertions where practical.

Verify the integration layer references the existing:

    CacheManager
    TimelineService
    EventBusManager
    LiveSessionAdapter
    ReplayService

rather than creating replacement instances that act as authorities.

Dependency injection should be explicit.

============================================================
STEP 39 — NO STATE LEAKAGE
============================================================

After every scenario verify:

    no stale replay state
    no stale live state
    no stale cache
    no stale delay
    no stale interpolation window
    no stale event index
    no stale snapshot

remains in the next scenario.

============================================================
STEP 40 — FAILURE INJECTION
============================================================

Add deterministic failure tests for:

    historical provider failure
    invalid telemetry
    replay load failure
    replay seek failure
    synchronization drift
    live provider failure
    live sequence gap
    delay starvation
    interpolation unsafe gap
    snapshot inconsistency
    mode transition failure

Every failure must produce:

    structured error/result
    coherent runtime state
    no partially committed mode

where the existing architecture promises rollback.

============================================================
STEP 41 — DETERMINISM
============================================================

Run identical integration scenario twice.

Verify equivalent:

    final runtime state
    timeline state
    replay position
    vehicle state
    event set
    snapshot content

Except intentionally unique:

    UUIDs
    wall-clock capture metadata

Fingerprints should remain deterministic where Agent 10.13 expects them to.

============================================================
STEP 42 — END-TO-END GOLDEN SCENARIO
============================================================

Create one complete golden integration scenario:

    1. Create session
    2. Initialize timeline
    3. Load historical telemetry
    4. Enter REPLAY
    5. Play
    6. Tick
    7. Pause
    8. Seek
    9. Step
   10. Jump to event
   11. Create bookmark
   12. Jump to bookmark
   13. Validate replay
   14. Capture snapshot
   15. Transition REPLAY → LIVE
   16. Inject live telemetry
   17. Enable delay
   18. Inject delayed frames
   19. Enable interpolation
   20. Inject deterministic gap
   21. Capture snapshot
   22. Transition LIVE → REPLAY
   23. Seek replay
   24. Capture snapshot
   25. Reset session
   26. Verify clean state

This scenario must pass deterministically.

============================================================
STEP 43 — INTEGRATION STATUS
============================================================

Provide an integration status API/report.

Conceptually:

    Phase10IntegrationStatus

Include:

    phase
    passed
    scenarios_total
    scenarios_passed
    scenarios_failed
    warnings
    active_session
    active_mode
    runtime_ms
    replay_state
    live_state
    synchronization_state
    snapshot_state
    last_failure

Do not expose internal objects.

============================================================
STEP 44 — INTEGRATION COMMAND
============================================================

If the project already has a command/controller convention, add a thin:

    ValidatePhase10

command.

It must invoke the integration orchestrator.

It must NOT become a transport endpoint.

Potential flow:

    ValidatePhase10
          ↓
    Phase10IntegrationService
          ↓
    existing runtime components
          ↓
    Phase10IntegrationResult

Do not expose internal implementation details.

============================================================
STEP 45 — TEST ORGANIZATION
============================================================

Create:

    tests/runtime/integration/

or the repository's established integration test location.

Organize tests around behavior:

    test_session_timeline_integration.py
    test_historical_replay_integration.py
    test_replay_navigation_integration.py
    test_replay_validation_integration.py
    test_live_integration.py
    test_delay_interpolation_integration.py
    test_mode_transition_integration.py
    test_snapshot_integration.py
    test_failure_recovery.py
    test_phase10_golden_path.py

Use fewer files if repository conventions favor it.

============================================================
STEP 46 — TEST LEVELS
============================================================

Provide:

    unit-level orchestration tests
    integration tests
    full golden-path test

Do not duplicate the detailed unit tests already belonging to Agents 10.6–10.18.

Integration tests should verify contracts between components.

============================================================
STEP 47 — REGRESSION
============================================================

Run the complete relevant suite.

At minimum:

    database
    configuration
    providers
    normalization
    telemetry
    cache
    timeline
    event bus
    session
    replay
    live
    delay
    interpolation
    snapshot
    Phase 10 integration

Do not assume previous reported test counts are still current.

Report the ACTUAL results from the repository.

============================================================
STEP 48 — QUALITY GATES
============================================================

Run:

    pytest
    ruff
    mypy

using the repository's actual commands/configuration.

Integration package target:

    >= 85% coverage

Overall regression must pass.

No new warnings should be introduced.

============================================================
STEP 49 — PERFORMANCE
============================================================

Measure the golden-path integration.

Look for:

    unnecessary frame copies
    duplicate normalization
    duplicate cache writes
    duplicate event detection
    repeated reconstruction
    unnecessary snapshot generation
    blocking operations

Do not prematurely optimize correct behavior.

Document any meaningful bottlenecks.

============================================================
STEP 50 — MEMORY
============================================================

Verify bounded memory during:

    replay
    seek
    event navigation
    live ingestion
    delay
    interpolation
    snapshots

No unbounded integration-level collections.

============================================================
STEP 51 — DOCUMENTATION
============================================================

Create:

    docs/specifications/Phase10IntegrationSpecification.md

Document:

    scope
    architecture
    component responsibilities
    lifecycle
    historical path
    replay path
    live path
    delay path
    interpolation path
    mode switching
    synchronization
    snapshot integration
    failure handling
    rollback
    session isolation
    determinism
    testing strategy
    performance
    limitations

Update:

    docs/specifications/README.md
    docs/Architecture.md
    docs/Replay.md
    docs/Telemetry.md
    docs/Streaming.md
    docs/Roadmap.md

============================================================
STEP 52 — ROADMAP
============================================================

Mark:

    Agent 10.19 — Phase 10 Integration

complete ONLY after:

    all integration scenarios pass
    golden path passes
    failure tests pass
    full regression passes
    quality gates pass
    documentation is updated

Do not mark complete based only on focused tests.

============================================================
ARCHITECTURAL INVARIANTS
============================================================

The following MUST remain true:

1. One unified runtime.
2. One authoritative CacheManager.
3. One authoritative TimelineService.
4. One authoritative EventBus.
5. One ReplayService.
6. One LiveSessionAdapter per active live session.
7. Replay and Live are operating modes, not separate products.
8. ModeController owns LIVE ↔ REPLAY transitions.
9. ReplaySynchronizer owns replay/timeline/cache alignment.
10. ReplayStateCache owns replay checkpoint acceleration.
11. ReplayEventSystem owns replay event/bookmark indexing.
12. ReplayNavigationService owns replay navigation.
13. ReplayValidationService remains read-only.
14. DelayController owns live temporal delay.
15. InterpolationService owns interpolation/provenance.
16. RaceStateSnapshotEngine owns immutable race read models.
17. Integration layer does not become a new source of truth.
18. Historical telemetry remains distinct from live telemetry.
19. Source timestamps remain distinct from received_at.
20. Delayed runtime time remains distinct from source time.
21. Interpolated state remains marked derived.
22. Events are never fabricated by integration.
23. Snapshot capture never advances runtime.
24. Snapshot capture never seeks replay.
25. Snapshot capture never injects telemetry.
26. Integration tests use deterministic offline providers.
27. No real F1 feed is required.
28. No external network dependency is allowed in tests.
29. No REST implementation.
30. No WebSocket implementation.
31. No Unity implementation.
32. No OBS implementation.
33. No AI implementation.
34. No physics implementation.
35. No persistence implementation.
36. No cross-session state leakage.
37. No LIVE/REPLAY mixed state.
38. Failed transitions cannot silently commit partial state.
39. Re-running the golden scenario is deterministic.
40. Completed agents must not be rewritten merely to make integration easier.

============================================================
ACCEPTANCE CRITERIA
============================================================

Agent 10.19 is COMPLETE only when:

[ ] Repository inspected.
[ ] Existing Phase 10 authorities identified.
[ ] Integration package created only if necessary.
[ ] No second runtime created.
[ ] Session initialization validated.
[ ] Timeline initialization validated.
[ ] Historical provider validated.
[ ] Historical → Replay validated.
[ ] Replay load validated.
[ ] Replay play validated.
[ ] Replay pause validated.
[ ] Replay resume validated.
[ ] Replay stop validated.
[ ] Replay tick validated.
[ ] Replay step validated.
[ ] Replay seek validated.
[ ] Replay state cache validated.
[ ] Replay synchronization validated.
[ ] Replay events validated.
[ ] Replay bookmarks validated.
[ ] Replay navigation validated.
[ ] Replay validation validated.
[ ] Replay snapshot validated.
[ ] Live session initialization validated.
[ ] Live ingestion validated.
[ ] Live sequence handling validated.
[ ] Live delay validated.
[ ] Live interpolation validated.
[ ] Live snapshot validated.
[ ] REPLAY → LIVE validated.
[ ] LIVE → REPLAY validated.
[ ] Failed mode transition validated.
[ ] Session reset validated.
[ ] Session isolation validated.
[ ] Driver isolation validated.
[ ] Source timestamp integrity validated.
[ ] Authoritative/derived provenance validated.
[ ] Snapshot consistency validated.
[ ] No-state-leakage tests pass.
[ ] Failure injection tests pass.
[ ] Determinism test passes.
[ ] Golden end-to-end scenario passes.
[ ] Integration status implemented if appropriate.
[ ] Validation command implemented if appropriate.
[ ] Documentation complete.
[ ] Roadmap updated.
[ ] Focused integration tests pass.
[ ] Full Phase 10 regression passes.
[ ] Full relevant project regression passes.
[ ] Coverage >= 85% for new integration package.
[ ] Ruff clean.
[ ] mypy/type checking clean.
[ ] No transport/UI implementation added.

============================================================
IMPORTANT IMPLEMENTATION RULE
============================================================

Do NOT assume the architecture described above exactly matches the current
source tree.

The CURRENT REPOSITORY is authoritative.

If an existing component already provides a required capability:

    USE IT.

If two completed agents expose slightly different interfaces:

    create a thin adapter at the integration boundary.

Do NOT modify a completed subsystem unless there is a genuine integration bug.

If a defect is discovered:

    1. reproduce it with an integration test
    2. identify the owning subsystem
    3. make the smallest backwards-compatible correction
    4. rerun that subsystem's tests
    5. rerun Phase 10 integration
    6. rerun full regression

Never solve an integration problem by duplicating a subsystem.

============================================================
START
============================================================

FIRST inspect the repository.

Then produce a concise internal implementation plan based on the ACTUAL code.

Then implement Agent 10.19.

Run focused integration tests.

Run the complete Phase 10 regression.

Run the full relevant project regression.

Fix all regressions.

Update documentation and Roadmap.

============================================================
FINAL REPORT
============================================================

When complete, report:

1. Files created.
2. Files modified.
3. Actual architecture discovered.
4. Integration architecture implemented.
5. Session → Timeline flow.
6. Historical → Replay flow.
7. Replay control flow.
8. Replay synchronization flow.
9. Replay cache integration.
10. Replay events/bookmarks integration.
11. Replay navigation integration.
12. Replay validation integration.
13. Replay → Live transition.
14. Live ingestion integration.
15. Delay integration.
16. Interpolation integration.
17. Live → Replay transition.
18. Snapshot integration.
19. Session reset behavior.
20. Failure/rollback behavior.
21. Session isolation.
22. Determinism.
23. Golden-path scenario.
24. Failure-injection scenarios.
25. Integration status/command.
26. Tests added.
27. Focused test count.
28. Full Phase 10 regression count.
29. Full project regression count.
30. Coverage.
31. Ruff result.
32. mypy result.
33. Performance observations.
34. Memory observations.
35. Documentation updated.
36. Roadmap status.
37. Known limitations.
38. Recommended Agent 10.20.
```

## User

**Agent 10.19 complete.** Phase 10 end-to-end integration lives in `backend/runtime/phase10/` (separate from the older `RuntimeIntegrationService`).

### Final report

1. **Created:** `backend/runtime/phase10/` (harness, service, controller, settings, result, enums, exceptions); `tests/runtime/phase10/` (22 tests); `shared/protocols/commands/phase10/`; `Phase10IntegrationSpecification.md`

2. **Modified:** command catalogue; snapshot engine (`ModeStatus.current_mode` fix); Roadmap/Architecture/Telemetry/Replay/Streaming/specs README

3. **Architecture:** Shared Session + Timeline + Cache + EventBus → Replay + Live(+Delay+Interp) → ModeController → SnapshotEngine

4–18. **Flows validated in golden path:** session/timeline → replay load/control/seek/sync/bookmarks/nav/validation → snapshot → REPLAY→LIVE → ingest/sequence/delay/interp → snapshot → LIVE→REPLAY → reset → failed transition coherence

19–22. Reset clears delay/interp/latest snapshot; failure paths stay non-LIVE; session isolation across harnesses; golden runs deterministic (scenario sequence/status)

23–25. Golden + failure-injection scenarios; `ValidatePhase10` + `Phase10IntegrationStatus`

26–36. **22** focused tests; **801** runtime+interpolation regression; **85%** coverage; **Ruff** clean; **mypy** clean; docs + Roadmap **10.19 ✓**

37. **Limits:** synthetic offline frames (not full FastF1 unpack); not a perf bench

38. **Recommended Agent 10.20:** REST/WebSocket (or presentation) façades consuming `RaceStateSnapshot`

## Assistant

Excellent. **Agent 10.19 is now accepted as complete** and the Phase 10 integration baseline is established.

The important result is that RaceVision now has an end-to-end validated runtime rather than a collection of independently tested subsystems.

### Phase 10 status

| Agent | Capability | Status |
|---|---|---:|
| 10.6 | Historical Telemetry Provider | ✅ |
| 10.7 | Replay Runtime Core | ✅ |
| 10.8 | Replay Controller | ✅ |
| 10.9 | Replay Synchronization | ✅ |
| 10.10 | Replay State Cache | ✅ |
| 10.11 | Replay Bookmark & Event System | ✅ |
| 10.12 | Replay Seeking & Time Navigation | ✅ |
| 10.13 | Replay Recording/Playback Validation | ✅ |
| 10.14 | Live Session Adapter | ✅ |
| 10.15 | Live/Replay Mode Controller | ✅ |
| 10.16 | Race Timeline Delay Buffer | ✅ |
| 10.17 | Telemetry Interpolation & Gap Handling | ✅ |
| 10.18 | Race State Snapshot Engine | ✅ |
| **10.19** | **Phase 10 Integration** | **✅** |

### The validated architecture

```text
                    ┌──────────────────────┐
                    │    Session Runtime   │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │      Timeline        │
                    └──────────┬───────────┘
                               │
              ┌────────────────┴────────────────┐
              │                                 │
       HISTORICAL / REPLAY                    LIVE
              │                                 │
              ▼                                 ▼
       ReplayService                    LiveSessionAdapter
              │                                 │
       Replay State Cache                      Delay
              │                                 │
       Events / Bookmarks                 Interpolation
              │                                 │
       Navigation / Validation                   │
              │                                 │
              └──────────────┬──────────────────┘
                             ▼
                    Cache + EventBus
                             │
                             ▼
                       ModeController
                             │
                             ▼
                    RaceStateSnapshot
                             │
                             ▼
                 Future Presentation Layer
```

The key architectural achievement is:

**Replay and Live are now demonstrated as two operating paths through the same runtime, not two separate runtimes.**

### Current quality baseline

The reported **801 runtime + interpolation regression tests**, **85% coverage**, clean **Ruff**, and clean **mypy** give us a strong foundation for moving upward into presentation/transport.

The synthetic-provider limitation is also correctly contained: **10.19 proves the runtime integration, not production F1 feed fidelity.**

### One important consequence for 10.20

The next layer should be deliberately thin:

```text
REST / WebSocket
       │
       ▼
Phase 10 / Runtime Controllers
       │
       ▼
RaceStateSnapshot
```

It should **not** become:

```text
REST → CacheManager
WebSocket → ReplayService
Unity → LiveSessionAdapter
OBS → TimelineService
```

That would bypass the architecture we've just validated.

So for **Agent 10.20**, the correct objective is a **transport/presentation boundary over the existing controllers and `RaceStateSnapshot`**, with no new source of truth.

I have the Phase 10.6–10.19 progression understood and can use this as the baseline for the next agent.

## User

Please give commands for Agent 10.20	Phase 10 Acceptance Testing	Final acceptance gate and performance testing ( 1 click copy and paste cursor friendly)

## Assistant

Yes. **Agent 10.20 should be the final Phase 10 acceptance gate**, not another feature layer. It should validate the complete 10.6–10.19 implementation under deterministic functional, failure, concurrency, performance, memory, and regression testing.

Copy/paste this entire block into Cursor Agent:

```text
You are the Principal Distributed Systems Architect, Principal QA Engineer,
and Performance Engineer for the RaceVision project.

============================================================
RACEVISION — AGENT 10.20
PHASE 10 ACCEPTANCE TESTING
FINAL ACCEPTANCE GATE + PERFORMANCE TESTING
============================================================

OBJECTIVE
---------

Implement Agent 10.20 — Phase 10 Acceptance Testing.

This is the FINAL ACCEPTANCE GATE for Phase 10.

Agents 10.6 through 10.19 are considered implemented.

Agent 10.20 must NOT introduce a new runtime architecture.

It must NOT become another feature layer.

Its responsibility is to independently verify that the complete Phase 10
system satisfies its functional, architectural, reliability, determinism,
performance, memory, concurrency, and regression requirements.

The final result must answer:

    "Is Phase 10 actually ready to be accepted?"

============================================================
CRITICAL RULE
============================================================

DO NOT redesign Phase 10.

DO NOT create:

    another Runtime
    another Cache
    another Timeline
    another Replay engine
    another Live engine
    another Snapshot engine
    another EventBus
    another Session manager

Use the actual completed implementation.

The acceptance layer observes and tests the existing architecture.

============================================================
PHASE 10 BASELINE
============================================================

Completed:

    10.6  Historical Telemetry Provider
    10.7  Replay Runtime Core
    10.8  Replay Controller
    10.9  Replay Synchronization
    10.10 Replay State Cache
    10.11 Replay Bookmark & Event System
    10.12 Replay Seeking & Time Navigation
    10.13 Replay Recording/Playback Validation
    10.14 Live Session Adapter
    10.15 Live/Replay Mode Controller
    10.16 Race Timeline Delay Buffer
    10.17 Telemetry Interpolation & Gap Handling
    10.18 Race State Snapshot Engine
    10.19 Phase 10 Integration

Reported current baseline:

    801 runtime + interpolation regression tests
    85% coverage
    Ruff clean
    mypy clean
    Phase 10 golden-path integration passing

Treat actual repository results as authoritative.

============================================================
STEP 1 — INSPECT THE REPOSITORY
============================================================

Before changing anything inspect:

    docs/Roadmap.md
    docs/Architecture.md
    docs/Telemetry.md
    docs/Replay.md
    docs/Streaming.md

Read all Phase 10 specifications.

Locate:

    backend/runtime/phase10/
    backend/runtime/replay/
    backend/runtime/live/
    backend/runtime/delay/
    backend/telemetry/interpolation/
    backend/runtime/snapshot/
    backend/runtime/mode/

Inspect:

    tests/runtime/
    tests/telemetry/
    tests/providers/

Do not assume previous reported numbers are still correct.

Run the repository's current tests before modifying anything.

============================================================
STEP 2 — DEFINE ACCEPTANCE GATES
============================================================

Create explicit acceptance gates.

Minimum gates:

    GATE-01 Functional correctness
    GATE-02 End-to-end integration
    GATE-03 Replay correctness
    GATE-04 Live correctness
    GATE-05 Mode transition safety
    GATE-06 Timeline synchronization
    GATE-07 Delay correctness
    GATE-08 Interpolation correctness
    GATE-09 Snapshot consistency
    GATE-10 Failure recovery
    GATE-11 Session isolation
    GATE-12 Determinism
    GATE-13 Concurrency safety
    GATE-14 Performance
    GATE-15 Memory boundedness
    GATE-16 Regression
    GATE-17 Code quality
    GATE-18 Documentation completeness

Every gate must produce:

    PASS
    FAIL
    SKIPPED

If a gate is skipped, provide a reason.

============================================================
STEP 3 — ACCEPTANCE PACKAGE
============================================================

Create a minimal acceptance package following repository conventions.

Preferred:

    backend/runtime/acceptance/

Possible files:

    __init__.py
    acceptance_runner.py
    acceptance_suite.py
    acceptance_result.py
    acceptance_gate.py
    acceptance_status.py
    acceptance_exceptions.py
    performance.py
    metrics.py

Only create files that are genuinely required.

This package must NOT become production runtime infrastructure.

It is test/validation infrastructure.

============================================================
STEP 4 — ACCEPTANCE RESULT
============================================================

Create an immutable result model.

Conceptually:

    Phase10AcceptanceResult

Include:

    acceptance_id
    started_at
    completed_at
    passed
    gates_total
    gates_passed
    gates_failed
    gates_skipped
    failures
    warnings
    functional_results
    performance_results
    memory_results
    regression_results
    quality_results
    environment
    metrics

Do not expose internal runtime objects.

============================================================
STEP 5 — ACCEPTANCE GATE MODEL
============================================================

Create:

    AcceptanceGateResult

Fields:

    gate_id
    name
    status
    duration_ms
    assertions
    failures
    warnings
    metrics

Use enums if the repository convention supports them.

============================================================
STEP 6 — TEST ENVIRONMENT
============================================================

Acceptance tests MUST be deterministic.

Do NOT require:

    internet
    F1 servers
    official F1 telemetry
    FastF1 network access
    REST endpoints
    WebSocket servers
    Unity
    OBS
    Twitch
    Kick
    YouTube

Use deterministic test doubles:

    InMemoryFastF1Client
    InMemoryLiveProvider

or the repository's actual equivalents.

The acceptance environment must clearly distinguish:

    functional runtime validation

from:

    production telemetry validation.

============================================================
STEP 7 — FUNCTIONAL ACCEPTANCE
============================================================

Validate the complete Session → Timeline → Replay/Live architecture.

The acceptance suite must execute:

    create session
    initialize timeline
    load historical telemetry
    enter replay
    play
    pause
    resume
    tick
    seek
    step
    navigate events
    create bookmark
    jump bookmark
    validate replay
    capture snapshot
    switch REPLAY → LIVE
    ingest live frames
    exercise sequence handling
    enable delay
    exercise delayed frames
    enable interpolation
    exercise gap
    capture live snapshot
    switch LIVE → REPLAY
    seek replay
    capture snapshot
    reset session
    shutdown

Use existing public APIs.

============================================================
STEP 8 — FUNCTIONAL ACCEPTANCE CRITERIA
============================================================

Verify:

    no invalid state transitions
    no negative replay time
    no position beyond replay end
    no duplicate replay events
    no duplicate bookmarks
    no stale session state
    no stale cache
    no stale delay state
    no stale interpolation state
    no mixed LIVE/REPLAY state
    no invalid snapshot
    no source timestamp corruption

============================================================
STEP 9 — REPLAY ACCEPTANCE
============================================================

Test:

    load
    play
    pause
    resume
    stop
    reset
    seek
    step_forward
    step_backward
    tick

Verify deterministic state transitions.

Test boundary conditions:

    frame 0
    first frame
    middle frame
    last frame
    before start
    after end

Verify configured clamping.

============================================================
STEP 10 — REPLAY SEEK PERFORMANCE
============================================================

Measure:

    seek to start
    seek to midpoint
    seek near end
    repeated seek
    backward seek
    forward seek

Compare:

    checkpoint-enabled reconstruction

against:

    full reconstruction

where the existing system exposes both paths.

Record:

    duration_ms
    frames_replayed
    checkpoint_used
    reconstruction_count

Do NOT require a specific optimization implementation.

Acceptance should verify that the configured checkpoint mechanism actually
reduces reconstruction work where expected.

============================================================
STEP 11 — REPLAY NAVIGATION ACCEPTANCE
============================================================

Test:

    fast-forward
    rewind
    start
    end
    jump-to-lap
    jump-to-sector
    jump-to-event
    next-event
    previous-event
    next-bookmark
    previous-bookmark

Measure latency.

Record:

    p50
    p95
    p99
    max

if sufficient samples exist.

For tiny deterministic suites, explicitly label percentile results as
microbenchmark measurements rather than production benchmarks.

============================================================
STEP 12 — REPLAY EVENT ACCEPTANCE
============================================================

Verify:

    lap completion
    sector completion
    overtake
    incident
    pit entry
    pit exit
    bookmark

Use deterministic telemetry.

Verify:

    events are deterministic
    event IDs are deterministic where designed
    repeated seek does not duplicate events
    unsupported events are not fabricated

============================================================
STEP 13 — REPLAY VALIDATION ACCEPTANCE
============================================================

Run Agent 10.13 validation.

Require:

    valid timestamps
    valid telemetry
    valid indexes
    valid reconstruction
    valid playback
    valid navigation
    valid synchronization
    valid events
    valid bookmarks
    deterministic fingerprints

Verify validation does not leave the replay mutated.

============================================================
STEP 14 — LIVE ACCEPTANCE
============================================================

Use InMemoryLiveProvider.

Test:

    connect
    run
    ingest
    stop
    reconnect
    shutdown

Verify:

    sequence handling
    duplicate rejection
    gap detection
    source timestamp preservation
    received_at separation
    latency measurement
    session isolation

============================================================
STEP 15 — LIVE THROUGHPUT TEST
============================================================

Create deterministic synthetic telemetry streams.

Measure ingestion rates such as:

    10 frames/sec
    50 frames/sec
    100 frames/sec
    500 frames/sec

Only test rates appropriate for the architecture.

Do not claim these represent real F1 feed rates.

Measure:

    accepted frames/sec
    rejected frames/sec
    queue depth
    processing latency
    dropped frames
    gap count
    error count

Record:

    mean
    p50
    p95
    p99
    max

============================================================
STEP 16 — LIVE BACKPRESSURE
============================================================

Test existing policies:

    DROP_OLDEST
    DROP_NEWEST
    FAIL

where supported.

Verify:

    queue remains bounded
    policy is deterministic
    metrics are correct
    runtime remains coherent
    no memory explosion occurs

Do not modify policy semantics merely to make tests pass.

============================================================
STEP 17 — DELAY BUFFER ACCEPTANCE
============================================================

Test:

    disabled
    buffering
    ready
    late frame
    duplicate frame
    starvation
    capacity pressure
    reset

Verify:

    delayed timestamp is correct
    source timestamp is preserved
    Timeline remains LIVE
    cache receives delayed presentation state
    no replay delay is accidentally introduced

============================================================
STEP 18 — DELAY PERFORMANCE
============================================================

Measure:

    insertion latency
    lookup latency
    eviction latency
    memory growth

Test increasing buffer sizes within reasonable deterministic limits.

Verify:

    bounded capacity
    predictable behavior
    no unbounded growth

============================================================
STEP 19 — INTERPOLATION ACCEPTANCE
============================================================

Test:

    no gap
    safe gap
    unsafe gap
    linear interpolation
    angular interpolation
    hold interpolation
    NEVER channels
    duplicate frames
    historical reorder
    live late frame
    no extrapolation

Verify:

    authoritative frames never overwritten
    derived frames marked interpolated
    provenance preserved
    no events synthesized
    driver/session isolation preserved

============================================================
STEP 20 — INTERPOLATION PERFORMANCE
============================================================

Measure interpolation processing against increasing frame counts.

Record:

    input frames
    output frames
    interpolated frames
    processing time
    frames/sec
    memory

Verify bounded windows.

============================================================
STEP 21 — MODE SWITCH ACCEPTANCE
============================================================

Test:

    LIVE → REPLAY
    REPLAY → LIVE
    LIVE → LIVE
    REPLAY → REPLAY

Verify same-mode transitions are idempotent.

Verify:

    no dual ingestion
    no mixed mode
    no stale cache
    no stale Timeline mode
    no stale replay cursor
    no stale live provider
    no stale delay
    no stale interpolation

============================================================
STEP 22 — MODE FAILURE TESTS
============================================================

Inject:

    replay load failure
    live connection failure
    live startup failure
    replay startup failure
    target-mode initialization failure

Verify:

    structured error
    no half-committed mode
    rollback behavior matches configuration
    authoritative state remains coherent
    no silent live reconnect

============================================================
STEP 23 — SNAPSHOT ACCEPTANCE
============================================================

Capture RaceStateSnapshot in:

    LIVE
    REPLAY
    delayed LIVE
    interpolated LIVE
    after replay seek
    after replay step
    after mode transition

Verify:

    immutable snapshot
    correct session
    correct mode
    correct runtime_ms
    correct vehicles
    correct timeline
    correct quality
    bounded events
    JSON-safe serialization

Snapshot capture MUST NOT:

    advance replay
    seek replay
    inject telemetry
    modify cache
    modify Timeline

============================================================
STEP 24 — SNAPSHOT PERFORMANCE
============================================================

Measure snapshot creation latency.

Test with:

    1 vehicle
    5 vehicles
    10 vehicles
    20 vehicles
    repository-supported maximum fixture

Record:

    p50
    p95
    p99
    max
    snapshot size
    memory allocation if measurable

Clearly label synthetic fixture sizes.

============================================================
STEP 25 — SYNCHRONIZATION ACCEPTANCE
============================================================

Verify replay synchronization after:

    load
    play
    tick
    seek
    step
    reset
    mode transition

Verify configured tolerance.

Default expected tolerance:

    1 ms

unless repository configuration differs.

Inject deterministic drift.

Verify:

    drift detected
    recovery behavior
    authoritative replay cursor never incorrectly moved

============================================================
STEP 26 — STATE CACHE ACCEPTANCE
============================================================

Verify:

    baseline creation
    checkpoint creation
    checkpoint lookup
    eviction
    replay isolation
    reset
    restore

Test:

    small snapshot limits
    larger snapshot limits
    multiple replay IDs

Verify no cross-replay restoration.

============================================================
STEP 27 — SESSION ISOLATION
============================================================

Create multiple sessions.

For example:

    Session A
    Session B
    Session C

Run simultaneous or interleaved operations.

Verify:

    telemetry isolation
    cache isolation
    Timeline isolation
    replay isolation
    event isolation
    bookmark isolation
    snapshot isolation
    delay isolation
    interpolation isolation

============================================================
STEP 28 — DRIVER ISOLATION
============================================================

Use multiple drivers.

Verify:

    telemetry identity
    vehicle state identity
    event identity
    snapshot identity

No driver state may leak between vehicles.

============================================================
STEP 29 — CONCURRENCY ACCEPTANCE
============================================================

Test supported concurrency.

At minimum:

    concurrent replay commands
    concurrent status requests
    concurrent snapshot requests
    live ingestion while status/snapshot requests occur
    mode transition contention

Use repository-supported locking semantics.

Do NOT invent unsupported thread-safety guarantees.

Verify:

    no race-induced corruption
    no deadlocks
    no inconsistent snapshots
    no duplicate transitions
    no data corruption

============================================================
STEP 30 — DEADLOCK / TIMEOUT DETECTION
============================================================

Every concurrency scenario must have a timeout.

A hanging test is a FAILURE.

Do not allow acceptance tests to wait indefinitely.

============================================================
STEP 31 — DETERMINISM ACCEPTANCE
============================================================

Run the exact golden scenario multiple times.

Minimum:

    3 complete runs

Compare normalized results.

Ignore intentionally variable:

    UUID
    wall-clock timestamps
    process IDs
    temporary paths

Require equivalent:

    scenario sequence
    runtime states
    replay positions
    event sets
    vehicle states
    snapshot semantic content
    fingerprints

============================================================
STEP 32 — RESTART / CLEAN STATE
============================================================

Run:

    initialize
    complete golden scenario
    shutdown
    initialize again

Verify:

    no stale runtime state
    no stale replay
    no stale live state
    no stale events
    no stale bookmarks
    no stale delay
    no stale interpolation
    no stale snapshot

unless persistence is explicitly intended.

============================================================
STEP 33 — FAILURE INJECTION MATRIX
============================================================

Test at least:

    invalid historical telemetry
    provider failure
    malformed frame
    duplicate frame
    sequence gap
    out-of-order frame
    replay load failure
    invalid seek
    synchronization drift
    checkpoint restore failure if injectable
    live provider failure
    delay starvation
    interpolation unsafe gap
    snapshot inconsistency
    mode transition failure

For each verify:

    detection
    structured result
    recovery or rollback
    no corrupted authoritative state

============================================================
STEP 34 — PERFORMANCE TEST HARNESS
============================================================

Create a performance test harness.

Preferred:

    tests/runtime/acceptance/performance/

or repository-equivalent.

The harness should collect:

    operation
    iterations
    total_duration_ms
    mean_ms
    p50_ms
    p95_ms
    p99_ms
    max_ms
    throughput
    errors
    memory_before
    memory_after
    peak_memory if available

Do not add external benchmark dependencies unless already present.

Prefer Python standard library timing:

    time.perf_counter()

and:

    tracemalloc

where appropriate.

============================================================
STEP 35 — PERFORMANCE WARMUP
============================================================

Avoid measuring imports and one-time initialization as normal operation.

Where appropriate:

    warm up
    then measure

Clearly distinguish:

    cold-start
    steady-state

if both are measured.

============================================================
STEP 36 — PERFORMANCE SAMPLE SIZE
============================================================

Use reasonable sample counts.

Do not make CI excessively slow.

Small deterministic microbenchmarks are acceptable.

For example:

    100
    500
    1000

iterations where appropriate.

Do not blindly run millions of iterations.

============================================================
STEP 37 — PERFORMANCE BASELINES
============================================================

Do NOT invent arbitrary production SLA numbers.

Instead establish repository-local baselines.

Report:

    measured value
    fixture size
    environment
    comparison to previous implementation if available

If a hard requirement already exists in project specifications, enforce it.

Otherwise label measurements:

    BASELINE
    NOT A PRODUCTION SLA

============================================================
STEP 38 — MEMORY TESTING
============================================================

Use tracemalloc or repository-supported profiling.

Test:

    replay loading
    repeated seeking
    event indexing
    live ingestion
    delay buffer
    interpolation window
    snapshots
    mode transitions

Look for:

    monotonically increasing memory
    stale references
    unbounded collections
    replay/session leakage

============================================================
STEP 39 — REPEATED-CYCLE MEMORY TEST
============================================================

Run repeated:

    replay load → seek → reset

and:

    live start → ingest → stop

and:

    LIVE → REPLAY → LIVE

cycles.

Measure memory before and after cycles.

The goal is to identify retained state.

Do not require exact allocator return-to-OS behavior.

Focus on retained Python object growth.

============================================================
STEP 40 — LARGE FIXTURE TEST
============================================================

Create deterministic larger synthetic datasets.

Test dimensions independently.

For example:

    more frames
    more drivers
    more events
    larger replay
    larger delay window

Do not create an unrealistic enormous dataset that makes CI unusable.

Document fixture sizes.

============================================================
STEP 41 — SOAK TEST
============================================================

Create a bounded deterministic soak test.

Example:

    repeated replay operations
    repeated live ingestion
    repeated mode transitions

for a fixed number of cycles.

Do not use time-based infinite tests.

Verify:

    no state drift
    no event duplication
    no memory leak indication
    no increasing latency caused by accumulated state

============================================================
STEP 42 — REGRESSION GATE
============================================================

Run:

    all Phase 10 tests
    all runtime tests
    all telemetry/interpolation tests
    provider tests
    database tests where applicable

Use the actual repository commands.

Record exact results.

Do not report historical test counts.

============================================================
STEP 43 — CODE QUALITY GATE
============================================================

Run repository-standard:

    Ruff
    mypy
    pytest

If formatting/lint commands exist, run them.

No new:

    lint errors
    type errors
    warnings
    skipped tests

unless explicitly documented and pre-existing.

============================================================
STEP 44 — COVERAGE GATE
============================================================

Measure coverage.

Do not artificially inflate coverage.

The acceptance layer itself should have meaningful coverage.

Target:

    >= 85%

for newly created acceptance infrastructure if practical.

More important:

    existing Phase 10 coverage must not regress.

Report:

    acceptance package coverage
    Phase 10 coverage
    overall project coverage

============================================================
STEP 45 — TEST REPORT
============================================================

Create a machine-readable result if project conventions support it.

Potential:

    phase10_acceptance_report.json

Do not commit generated reports unless repository conventions require it.

The report should include:

    timestamp
    git revision if available
    environment
    Python version
    test counts
    gate statuses
    performance measurements
    memory measurements
    failures
    warnings

============================================================
STEP 46 — ACCEPTANCE COMMAND
============================================================

If project conventions support an application-level validation command,
provide a thin:

    ValidatePhase10Acceptance

or equivalent.

It should invoke the acceptance suite.

It must not be required by production runtime.

If no command framework exists, do not invent an unnecessary CLI system.

A pytest entry point is sufficient.

============================================================
STEP 47 — DOCUMENTATION
============================================================

Create:

    docs/specifications/Phase10AcceptanceTestingSpecification.md

Document:

    acceptance scope
    gates
    functional tests
    integration tests
    replay tests
    live tests
    delay tests
    interpolation tests
    snapshot tests
    failure tests
    concurrency tests
    determinism
    performance methodology
    memory methodology
    regression methodology
    environment
    acceptance criteria
    known limitations

Update:

    docs/specifications/README.md
    docs/Roadmap.md
    docs/Architecture.md
    docs/Replay.md
    docs/Telemetry.md
    docs/Streaming.md

============================================================
STEP 48 — ROADMAP RULE
============================================================

Do NOT mark Agent 10.20 complete until every mandatory acceptance gate passes.

Roadmap should distinguish:

    PASS
    PASS WITH WARNINGS
    FAIL

Do not mark complete if a mandatory gate fails.

============================================================
STEP 49 — ACCEPTANCE DECISION
============================================================

Produce one final decision:

    ACCEPTED

or:

    ACCEPTED WITH WARNINGS

or:

    NOT ACCEPTED

Rules:

    ACCEPTED:
        all mandatory gates pass

    ACCEPTED WITH WARNINGS:
        all mandatory gates pass
        only non-blocking warnings remain

    NOT ACCEPTED:
        any mandatory gate fails

Do not hide failures behind warnings.

============================================================
MANDATORY ACCEPTANCE INVARIANTS
============================================================

The following MUST remain true:

1. One unified Session Runtime.
2. One authoritative CacheManager.
3. One authoritative TimelineService.
4. One EventBus authority.
5. One ReplayService.
6. Live and Replay remain operating modes.
7. ModeController owns mode transitions.
8. ReplaySynchronizer owns replay alignment.
9. ReplayStateCache remains acceleration state.
10. ReplayValidationService remains read-only.
11. Delay remains a live presentation-time mechanism.
12. Interpolation remains derived telemetry.
13. RaceStateSnapshot remains an immutable read model.
14. Acceptance infrastructure is not a runtime authority.
15. No transport layer is introduced.
16. No UI is introduced.
17. No external F1 feed is required.
18. No internet dependency exists in acceptance tests.
19. No source timestamp replacement.
20. No synthetic event fabrication.
21. No cross-session leakage.
22. No cross-driver leakage.
23. No LIVE/REPLAY mixed state.
24. No silent reconnect after failed mode transition.
25. Snapshot capture cannot mutate runtime.
26. Replay validation cannot leave state mutated.
27. Delay cannot create a DELAYED Timeline mode.
28. Interpolation cannot overwrite authoritative frames.
29. Replay checkpoints cannot change authoritative cursor semantics.
30. Repeated operations remain deterministic.
31. Memory remains bounded by configured structures.
32. Supported concurrency cannot corrupt state.
33. No deadlocks.
34. No unbounded queues.
35. No unbounded event/bookmark accumulation within configured limits.
36. No regression in completed Phase 10 components.

============================================================
MANDATORY ACCEPTANCE GATES
============================================================

GATE-01  Functional correctness
GATE-02  Golden end-to-end scenario
GATE-03  Replay correctness
GATE-04  Replay navigation
GATE-05  Replay validation
GATE-06  Live ingestion
GATE-07  Delay buffer
GATE-08  Interpolation
GATE-09  Timeline synchronization
GATE-10  Snapshot consistency
GATE-11  Mode transitions
GATE-12  Failure recovery
GATE-13  Session isolation
GATE-14  Driver isolation
GATE-15  Determinism
GATE-16  Concurrency
GATE-17  Memory boundedness
GATE-18  Performance baseline
GATE-19  Soak testing
GATE-20  Full regression
GATE-21  Ruff
GATE-22  mypy
GATE-23  Coverage
GATE-24  Documentation

Every mandatory gate must PASS.

============================================================
FINAL ACCEPTANCE CRITERIA
============================================================

Agent 10.20 is COMPLETE only when:

[ ] Repository inspected.
[ ] Existing Phase 10 tests executed before changes.
[ ] Acceptance harness created.
[ ] Acceptance result model created.
[ ] Acceptance gate model created.
[ ] Functional acceptance passes.
[ ] Golden-path acceptance passes.
[ ] Replay acceptance passes.
[ ] Replay navigation passes.
[ ] Replay validation passes.
[ ] Live acceptance passes.
[ ] Delay acceptance passes.
[ ] Interpolation acceptance passes.
[ ] Timeline synchronization passes.
[ ] Snapshot acceptance passes.
[ ] Mode transitions pass.
[ ] Failure injection passes.
[ ] Session isolation passes.
[ ] Driver isolation passes.
[ ] Determinism passes.
[ ] Concurrency tests pass.
[ ] No deadlocks detected.
[ ] Memory testing passes.
[ ] Repeated-cycle memory test passes.
[ ] Soak test passes.
[ ] Performance baseline established.
[ ] No unacceptable performance regression.
[ ] Full Phase 10 regression passes.
[ ] Full relevant project regression passes.
[ ] Ruff clean.
[ ] mypy clean.
[ ] Coverage measured.
[ ] Coverage does not regress.
[ ] Documentation complete.
[ ] Roadmap updated.
[ ] Final acceptance report generated.
[ ] Final decision is ACCEPTED or ACCEPTED WITH WARNINGS.
[ ] No new runtime architecture introduced.
[ ] No transport/UI implementation introduced.

============================================================
IMPORTANT IMPLEMENTATION RULE
============================================================

The current repository is authoritative.

If the actual implementation differs from this specification:

    inspect it
    understand it
    test it

Do not rewrite completed agents simply to match this document.

If a genuine defect is discovered:

    1. Reproduce it with an acceptance test.
    2. Identify the owning subsystem.
    3. Fix the smallest possible defect.
    4. Run the owning subsystem's tests.
    5. Run Phase 10 integration.
    6. Run Phase 10 acceptance again.
    7. Run the full regression.

Do not weaken acceptance criteria to make tests pass.

Do not mark a failing mandatory gate as a warning.

============================================================
START IMPLEMENTATION
============================================================

FIRST:

    inspect repository
    inspect Phase 10 specifications
    inspect existing tests
    run existing test suite

THEN:

    implement acceptance harness
    implement gates
    implement functional acceptance tests
    implement performance tests
    implement memory tests
    implement concurrency tests
    implement determinism tests
    implement soak tests

THEN:

    run focused acceptance tests
    fix genuine defects
    run Phase 10 regression
    run full relevant project regression
    run Ruff
    run mypy
    measure coverage

THEN:

    update documentation
    update Roadmap
    produce final acceptance report

============================================================
FINAL REPORT FORMAT
============================================================

When complete, report:

1. Acceptance decision:
       ACCEPTED
       ACCEPTED WITH WARNINGS
       NOT ACCEPTED

2. Files created.

3. Files modified.

4. Acceptance architecture.

5. Acceptance gates.

6. Functional results.

7. Golden-path results.

8. Replay results.

9. Live results.

10. Delay results.

11. Interpolation results.

12. Synchronization results.

13. Snapshot results.

14. Mode transition results.

15. Failure-injection results.

16. Session isolation results.

17. Driver isolation results.

18. Determinism results.

19. Concurrency results.

20. Memory results.

21. Soak results.

22. Performance results:
       throughput
       p50
       p95
       p99
       max
       fixture sizes

23. Performance comparison against previous baseline if available.

24. Full Phase 10 regression:
       actual test count
       passed
       failed
       skipped

25. Full relevant project regression:
       actual test count
       passed
       failed
       skipped

26. Coverage:
       acceptance
       Phase 10
       project

27. Ruff result.

28. mypy result.

29. Documentation updated.

30. Roadmap status.

31. Known limitations.

32. Any ACCEPTED WITH WARNINGS items.

33. Recommended Agent 10.21.

============================================================
FINAL PRINCIPLE
============================================================

Agent 10.20 is a GATE, not a feature.

Do not make the system look better by weakening tests.

Do not hide failures.

Do not invent production performance guarantees.

Measure the actual implementation.

The goal is to establish, with evidence:

    "Phase 10 is functionally correct,
     architecturally coherent,
     deterministic,
     bounded,
     performant within measured baselines,
     and ready for the next architectural phase."

START NOW.
```

## User

## 1. Acceptance decision: **ACCEPTED**

All 24 mandatory gates **PASS**. No warnings. No skipped gates.

### Evidence snapshot

| Item                                 | Result         |
| ------------------------------------ | -------------- |
| GATE-01…24                           | PASS           |
| Nested Phase 10 regression (GATE-20) | **257** passed |
| Full `tests/runtime` + interpolation | **805** passed |
| Acceptance package coverage          | **85%**        |
| Ruff / mypy                          | clean          |

### Delivered

- **Created:** `backend/runtime/phase10_acceptance/` (runner, gates, perf/memory helpers, controller); `tests/runtime/phase10_acceptance/`; `ValidatePhase10Acceptance`; `Phase10AcceptanceTestingSpecification.md`
- **Modified:** Roadmap/Architecture/Telemetry/Replay/Streaming/specs README; phase10 commands export

### Architecture

Acceptance is a **gate**, not a runtime. It composes `Phase10Harness` / `Phase10IntegrationService` + focused microbenches (`perf_counter`, `tracemalloc`) and quality subprocesses (pytest subset, ruff, mypy).

### Performance

Measurements are labeled **`BASELINE_NOT_PRODUCTION_SLA`**: snapshot capture (1–20 vehicles), live batch ingest (10/50/100 Hz batch), interpolate latency (p50/p95/p99). No invented production SLA.

### Limits

- Microbenchmarks ≠ production F1 rates
- GATE-20 excludes the acceptance suite itself (avoids nested recursion)
- Soak cycles bounded for CI

### Recommended Agent 10.21

REST/WebSocket (or presentation) façades consuming `RaceStateSnapshot`.

## Assistant

Excellent. **Agent 10.20 is accepted.**

This is a significant milestone: **Phase 10 has now passed its final acceptance gate.**

### Phase 10 final status

| Agent | Component | Status |
|---|---|---:|
| 10.6 | Historical Telemetry Provider | ✅ |
| 10.7 | Replay Runtime Core | ✅ |
| 10.8 | Replay Controller | ✅ |
| 10.9 | Replay Synchronization | ✅ |
| 10.10 | Replay State Cache | ✅ |
| 10.11 | Replay Bookmark & Event System | ✅ |
| 10.12 | Replay Seeking & Time Navigation | ✅ |
| 10.13 | Replay Recording/Playback Validation | ✅ |
| 10.14 | Live Session Adapter | ✅ |
| 10.15 | Live/Replay Mode Controller | ✅ |
| 10.16 | Race Timeline Delay Buffer | ✅ |
| 10.17 | Telemetry Interpolation & Gap Handling | ✅ |
| 10.18 | Race State Snapshot Engine | ✅ |
| 10.19 | Phase 10 Integration | ✅ |
| **10.20** | **Phase 10 Acceptance Testing** | **✅ ACCEPTED** |

### Acceptance evidence

The important figures are:

- **24/24 mandatory gates PASS**
- **0 warnings**
- **0 skipped gates**
- **257 Phase 10 acceptance regression tests passed**
- **805 runtime + interpolation tests passed**
- **85% acceptance-package coverage**
- **Ruff clean**
- **mypy clean**
- Performance baselines established without inventing production SLAs
- Deterministic synthetic testing
- Memory/performance/concurrency/failure-path validation completed

Most importantly, the acceptance suite itself remains **outside the runtime authority**. That's exactly what we wanted.

### Architectural position now

```text
                    ┌──────────────────────────┐
                    │      Session Runtime     │
                    │                          │
                    │ Session                  │
                    │ Timeline                 │
                    │ Cache                    │
                    │ Event Bus                │
                    └────────────┬─────────────┘
                                 │
                ┌────────────────┴────────────────┐
                │                                 │
             REPLAY                              LIVE
                │                                 │
        Replay Runtime                    Live Session
                │                                 │
        Replay Controller                 Delay Buffer
        Navigation                        Interpolation
        Events / Bookmarks                       │
        State Cache                              │
        Validation                               │
                │                                 │
                └────────────┬────────────────────┘
                             │
                      Mode Controller
                             │
                             ▼
                    RaceStateSnapshot
                             │
                             ▼
                  ┌─────────────────────┐
                  │  Future Presentation │
                  │  / Transport Layer  │
                  └─────────────────────┘
```

And separately:

```text
Phase 10 Acceptance
        │
        ├── Functional gates
        ├── Integration gates
        ├── Failure testing
        ├── Determinism
        ├── Concurrency
        ├── Memory
        ├── Performance
        ├── Regression
        └── Quality
```

That separation is architecturally important.

## What Phase 10 now proves

RaceVision can now demonstrate, using deterministic test data, a complete lifecycle:

**Session → Timeline → Historical Telemetry → Replay → Seek/Navigation → Events/Bookmarks → Validation → Snapshot → Live → Delay → Interpolation → Snapshot → Replay → Reset**

while maintaining the unified runtime model.

It also means we should **not go back and keep adding functionality to the core runtime simply because transport/UI isn't there yet**.

### Next logical boundary: Agent 10.21

The recommended next step remains:

**10.21 — REST/WebSocket Presentation & Transport**

But this should be a **thin adapter**, not another runtime.

```text
REST / WebSocket
       │
       ▼
Command / Query Adapter
       │
       ▼
Existing Controllers
       │
       ├── ReplayController
       ├── ModeController
       ├── LiveSessionAdapter
       ├── Navigation
       └── RaceStateSnapshot
```

For example:

```text
GET  /runtime/status
GET  /runtime/snapshot

GET  /replay/status
POST /replay/load
POST /replay/play
POST /replay/pause
POST /replay/seek
POST /replay/step
POST /replay/reset

POST /replay/bookmarks
GET  /replay/events

POST /mode/live
POST /mode/replay

GET  /live/status

WebSocket:
    runtime.snapshot
    replay.state
    replay.event
    live.telemetry
    mode.changed
```

The crucial rule for 10.21 will be:

> **Transport exposes the runtime; transport does not become the runtime.**

So I would treat **Phase 10 as closed and accepted** at this point. memcite

## User

Is this still the plan below still.

Based on the original RaceVision vision—supporting both live Formula 1 races and historical race replay, with Unity/Blender rendering and streaming to OBS and social platforms. Is the structure the next major phases roughly like this:


Phase 11: Live Streaming Runtime (WebSocket/API transport)
Phase 12: Unity Integration & 3D Scene Runtime
Phase 13: OBS & Broadcast Overlay Runtime
Phase 14: Camera & Director System
Phase 15: Prediction & Latency Compensation (including the 5-second delay prediction pipeline you previously planned)
Phase 16: AI Commentary & Analytics
Phase 17: Public APIs & External Integrations

That ordering builds outward from the runtime you've established, keeping rendering, streaming, and AI as independent consumers rather than tightly coupling them into the core.

## Assistant

Yes — **the overall plan is still correct**, and after the completion and acceptance of Phase 10, I would keep that outward-expansion strategy.

There is, however, **one important refinement**: Phase 11 should establish the transport/presentation boundary, and the later phases should consume that boundary rather than connecting directly into the internal runtime.

### Updated RaceVision roadmap

| Phase | Name | Purpose | Status |
|---|---|---|---|
| **10** | Unified Session Runtime | Live + historical + replay + timeline + snapshots | ✅ **ACCEPTED** |
| **11** | Live Streaming Runtime / Transport | REST/WebSocket transport + real-time state/event distribution | 🔜 Next |
| **12** | Unity Integration & 3D Scene Runtime | 3D cars, tracks, transforms, scene state | Planned |
| **13** | OBS & Broadcast Overlay Runtime | OBS integration, overlays, broadcast telemetry | Planned |
| **14** | Camera & Director System | Cameras, automated directing, chat-controlled cameras | Planned |
| **15** | Prediction & Latency Compensation | Prediction, smoothing, delayed-live compensation | Planned |
| **16** | AI Commentary & Analytics | Commentary, race intelligence, analytics | Planned |
| **17** | Public APIs & External Integrations | External consumers, integrations and public API surface | Planned |

### The architectural principle remains

```text
                    ┌─────────────────────────────┐
                    │       Phase 10 Runtime      │
                    │                             │
                    │ Session                     │
                    │ Timeline                    │
                    │ Replay                      │
                    │ Live                        │
                    │ Delay                       │
                    │ Interpolation               │
                    │ Events                      │
                    │ Snapshots                   │
                    └──────────────┬──────────────┘
                                   │
                         Phase 11 Transport
                                   │
                    ┌──────────────┴──────────────┐
                    │                             │
                 REST API                    WebSocket
                    │                             │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────┼───────────────┐
                    │              │               │
                  Unity           OBS           External
                 Phase 12       Phase 13          Phase 17
                    │              │
                    └──────┬───────┘
                           │
                    Phase 14 Director
                           │
                    Phase 15 Prediction
                           │
                    Phase 16 AI
```

## One refinement to Phase 15

Your original idea of a **5-second prediction pipeline** still fits, but I would **not make the 5-second prediction part of the core runtime**.

Instead:

```text
Actual Live Telemetry
        │
        ├──────────────► Authoritative State
        │
        ▼
Prediction Pipeline
        │
        ├── short-horizon prediction
        ├── latency compensation
        ├── trajectory estimation
        └── visual smoothing
                │
                ▼
          Presentation
```

The authoritative telemetry remains authoritative.

Prediction becomes a **derived presentation/analytics layer** that can be corrected when real telemetry arrives.

That is especially important for your eventual 3D visualization: the renderer can smoothly predict where a car should be while the underlying RaceVision state remains grounded in actual telemetry.

## And Phase 12/13 should stay separate

This is another part of the original plan I'd strongly preserve.

### Phase 12 — Unity

Unity should consume something like:

```text
WebSocket
    ↓
RaceVision Client
    ↓
RaceStateSnapshot / Events
    ↓
3D Scene State
    ↓
Cars / Track / Effects / Audio
```

It shouldn't know how FastF1 works, how PostgreSQL works, or how replay reconstruction works.

### Phase 13 — OBS

Likewise:

```text
RaceVision Runtime
       ↓
WebSocket/API
       ↓
Broadcast Overlay Runtime
       ↓
OBS
       ↓
Twitch / YouTube / Kick
```

This keeps your broadcast system replaceable.

## The big architectural picture

The project is now naturally dividing into four layers:

```text
┌─────────────────────────────────────────────────────┐
│                 CONSUMER / EXPERIENCE               │
│                                                     │
│ Unity │ OBS │ Cameras │ AI │ External Clients       │
├─────────────────────────────────────────────────────┤
│                PRESENTATION SERVICES                │
│                                                     │
│ Director │ Prediction │ Overlays │ Commentary       │
├─────────────────────────────────────────────────────┤
│                    TRANSPORT                        │
│                                                     │
│ REST │ WebSocket │ Event Streaming │ API            │
├─────────────────────────────────────────────────────┤
│                 UNIFIED RUNTIME                     │
│                                                     │
│ Session │ Timeline │ Live │ Replay │ Cache          │
│ Events │ Delay │ Interpolation │ Snapshots           │
├─────────────────────────────────────────────────────┤
│                    DATA SOURCES                     │
│                                                     │
│ FastF1 │ Live Provider │ Historical Data │ DB        │
└─────────────────────────────────────────────────────┘
```

**That's the architecture I would continue with.**

So yes: **Phase 10 is now the completed foundation, Phase 11 is the transport boundary, and Phases 12–17 build outward without contaminating the unified runtime.**

The only thing I would avoid is prematurely locking every future phase to the exact numbering/details. The **architecture is solid; individual agents within Phases 11–17 can be decomposed as we discover what the implementation actually needs.**

## User

So what are the list for the next Phase for the Agents?

## Assistant

Yes. Now that **Phase 10 is fully accepted**, I would structure the next work as **Phase 11 — Transport & Live Streaming Runtime**.

The important change from Phase 10 is that we should now expose the runtime safely rather than adding more internal runtime features.

## Phase 11 — Transport & Live Streaming Runtime

| Agent | Component | Purpose |
|---|---|---|
| **11.1** | Transport Architecture | Define REST/WebSocket boundary and transport contracts |
| **11.2** | REST Runtime API | Expose runtime status, sessions, snapshots and capabilities |
| **11.3** | WebSocket Runtime Gateway | Real-time telemetry/state/event streaming |
| **11.4** | Command Transport Layer | REST/WS → existing Controllers/Commands |
| **11.5** | Snapshot Streaming | Stream `RaceStateSnapshot` efficiently |
| **11.6** | Live Telemetry Streaming | Stream live canonical telemetry/events |
| **11.7** | Replay Streaming | Stream replay state/events through the same transport |
| **11.8** | Subscription System | Clients subscribe to telemetry, snapshots, events, replay, etc. |
| **11.9** | Connection & Session Management | Client lifecycle, reconnect, heartbeat, session isolation |
| **11.10** | Backpressure & Rate Control | Prevent slow clients from affecting Runtime |
| **11.11** | Transport Authentication & Authorization | Secure API/WS access boundary |
| **11.12** | Transport Observability | Metrics, health, connection statistics, errors |
| **11.13** | Transport Integration Testing | End-to-end REST/WS tests against Phase 10 |
| **11.14** | Live Streaming Acceptance | Performance, concurrency, disconnect/reconnect testing |
| **11.15** | Phase 11 Acceptance | Final acceptance gate |

### The resulting architecture

```text
                 PHASE 10
          ┌───────────────────┐
          │ Unified Runtime   │
          │                   │
          │ Session           │
          │ Timeline          │
          │ Live             │
          │ Replay            │
          │ Cache             │
          │ Events            │
          │ Delay             │
          │ Interpolation     │
          │ Snapshot          │
          └─────────┬─────────┘
                    │
                    ▼
              PHASE 11
          ┌───────────────────┐
          │ Transport Layer  │
          ├───────────────────┤
          │ REST API          │
          │ WebSocket         │
          │ Commands          │
          │ Subscriptions     │
          │ Snapshots         │
          │ Events            │
          │ Auth              │
          │ Rate Control      │
          └─────────┬─────────┘
                    │
          ┌─────────┼──────────┐
          ▼         ▼          ▼
       Unity      OBS       External
       Phase 12   Phase 13   Phase 17
```

## Then Phase 12 — Unity / 3D

After 11 is accepted:

| Agent | Component |
|---|---|
| **12.1** | Unity Client Architecture |
| **12.2** | RaceVision WebSocket Client |
| **12.3** | Runtime State Synchronization |
| **12.4** | Track/Coordinate System |
| **12.5** | F1 Car Entity Runtime |
| **12.6** | Multi-Car Rendering |
| **12.7** | Vehicle Transform / Orientation |
| **12.8** | Track & Circuit Scene |
| **12.9** | Telemetry Visualization |
| **12.10** | Vehicle Effects |
| **12.11** | Replay/Live Unity Modes |
| **12.12** | Unity Performance |
| **12.13** | Unity Integration Testing |
| **12.14** | Phase 12 Acceptance |

## Phase 13 — OBS / Broadcast

| Agent | Component |
|---|---|
| **13.1** | Broadcast Runtime Architecture |
| **13.2** | OBS Integration |
| **13.3** | Overlay State Engine |
| **13.4** | Race Leaderboard Overlay |
| **13.5** | Timing / Lap Overlay |
| **13.6** | Telemetry Overlay |
| **13.7** | Driver Battle Overlay |
| **13.8** | Incident / Event Overlay |
| **13.9** | Broadcast Scene Management |
| **13.10** | Stream Output Integration |
| **13.11** | Broadcast Performance |
| **13.12** | Phase 13 Acceptance |

## Phase 14 — Camera & Director

| Agent | Component |
|---|---|
| **14.1** | Camera Runtime Architecture |
| **14.2** | Camera Registry |
| **14.3** | Track Cameras |
| **14.4** | Driver Follow Cameras |
| **14.5** | Battle Detection |
| **14.6** | Overtake Camera |
| **14.7** | Incident Camera |
| **14.8** | Replay Camera |
| **14.9** | Automated Director |
| **14.10** | Chat Camera Commands |
| **14.11** | Camera Transitions |
| **14.12** | Director Acceptance |

## Phase 15 — Prediction & Latency Compensation

This is where your planned **5-second delayed-live prediction system** belongs.

| Agent | Component |
|---|---|
| **15.1** | Prediction Architecture |
| **15.2** | Prediction State Model |
| **15.3** | Short-Horizon Vehicle Prediction |
| **15.4** | 5-Second Prediction Pipeline |
| **15.5** | Trajectory Prediction |
| **15.6** | Position / Orientation Smoothing |
| **15.7** | Prediction Error Correction |
| **15.8** | Live-vs-Predicted State Comparison |
| **15.9** | Confidence / Prediction Quality |
| **15.10** | Prediction Performance |
| **15.11** | Prediction Failure Handling |
| **15.12** | Phase 15 Acceptance |

## Phase 16 — AI Commentary & Analytics

| Agent | Component |
|---|---|
| **16.1** | Race Analytics Runtime |
| **16.2** | Driver Performance Analytics |
| **16.3** | Battle Detection / Intelligence |
| **16.4** | Strategy Analytics |
| **16.5** | Incident Intelligence |
| **16.6** | Predictive Race Analytics |
| **16.7** | Commentary Event Generator |
| **16.8** | AI Commentary Engine |
| **16.9** | Commentary Context Manager |
| **16.10** | Voice/TTS Integration |
| **16.11** | Commentary Safety / Rate Control |
| **16.12** | Phase 16 Acceptance |

## Phase 17 — Public API & External Integrations

| Agent | Component |
|---|---|
| **17.1** | Public API Architecture |
| **17.2** | API Versioning |
| **17.3** | Public REST API |
| **17.4** | Public WebSocket API |
| **17.5** | API Authentication |
| **17.6** | API Rate Limiting |
| **17.7** | API Documentation / OpenAPI |
| **17.8** | External Webhooks |
| **17.9** | External Streaming Integrations |
| **17.10** | Developer API / SDK Foundations |
| **17.11** | API Monitoring |
| **17.12** | Public API Acceptance |

### The overall roadmap now becomes

```text
PHASE 10  Unified Runtime
          └── ✅ ACCEPTED

PHASE 11  Transport & Live Streaming
          └── REST / WebSocket / subscriptions

PHASE 12  Unity & 3D Runtime
          └── Cars / tracks / visualization

PHASE 13  OBS & Broadcast
          └── overlays / broadcast output

PHASE 14  Camera & Director
          └── automated cameras / chat control

PHASE 15  Prediction
          └── 5-second prediction / compensation

PHASE 16  AI
          └── analytics / commentary

PHASE 17  Public API
          └── external ecosystem
```

**I would start with Agent 11.1 next.** It should establish the transport contracts and boundaries *before* we implement REST or WebSocket, just as we did with the runtime architecture in Phase 10. This keeps the same disciplined agent-by-agent progression that got us to the Phase 10 acceptance gate.

## User

Please give commands for Agent 11.1	Transport Architecture	Define REST/WebSocket boundary and transport contracts ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. **Agent 11.1 should define the transport architecture and contracts only**. It should not implement the REST server, WebSocket server, Unity client, OBS integration, or bypass the Phase 10 controllers.

Copy/paste this entire block into Cursor Agent:

```text
You are the Principal Distributed Systems Architect for the RaceVision project.

============================================================
RACEVISION — AGENT 11.1
TRANSPORT ARCHITECTURE
DEFINE REST / WEBSOCKET BOUNDARY + TRANSPORT CONTRACTS
============================================================

OBJECTIVE
---------

Implement Agent 11.1 — Transport Architecture.

Phase 10 is COMPLETE and ACCEPTED.

Phase 10 acceptance:

    24/24 mandatory gates PASS
    257 Phase 10 acceptance regression tests PASS
    805 runtime + interpolation tests PASS
    85% acceptance-package coverage
    Ruff clean
    mypy clean

Phase 11 begins the outward-facing transport boundary.

Agent 11.1 must define the architecture and contracts required for:

    REST
    WebSocket
    runtime commands
    runtime queries
    snapshots
    events
    subscriptions
    connection/session identity
    errors
    capabilities
    transport health

DO NOT implement the actual REST server.

DO NOT implement the actual WebSocket server.

Those belong to later Phase 11 agents.

This agent establishes the contracts that those implementations will consume.

============================================================
ARCHITECTURAL PRINCIPLE
============================================================

The Phase 10 Runtime remains authoritative.

Transport is an adapter around the Runtime.

The architecture MUST remain:

    Client
       ↓
    REST / WebSocket Transport
       ↓
    Transport Contracts
       ↓
    Existing Commands / Controllers
       ↓
    Phase 10 Runtime
       ↓
    Cache / Timeline / Replay / Live / EventBus
       ↓
    RaceStateSnapshot

NEVER:

    REST → CacheManager directly

    WebSocket → CacheManager directly

    REST → ReplayService internals

    WebSocket → LiveSessionAdapter internals

    Unity → PostgreSQL

    OBS → ReplayService

    External client → internal Runtime objects

Transport must not become another runtime.

============================================================
PHASE 10 AUTHORITIES
============================================================

Treat these as existing authorities:

    Session Runtime
    SessionManager
    TimelineService
    CacheManager
    EventBus
    ReplayService
    ReplayApplicationController
    ReplayCommandDispatcher
    ReplayNavigationService
    LiveSessionAdapter
    ModeController
    DelayController
    TelemetryInterpolationService
    RaceStateSnapshotEngine
    Phase10IntegrationService

Do not replace them.

Do not duplicate their responsibilities.

============================================================
STEP 1 — INSPECT THE REPOSITORY
============================================================

Before writing code:

    inspect repository structure

Read:

    docs/Roadmap.md
    docs/Architecture.md
    docs/Replay.md
    docs/Telemetry.md
    docs/Streaming.md

Read all relevant Phase 10 specifications.

Inspect:

    shared/protocols/
    shared/protocols/commands/
    shared/protocols/events/
    backend/runtime/
    backend/runtime/phase10/
    backend/runtime/replay/
    backend/runtime/live/
    backend/runtime/mode/
    backend/runtime/snapshot/

Inspect:

    command catalogue
    event catalogue
    existing response/error models
    existing serialization utilities
    existing configuration system

Inspect existing tests before implementing anything.

Do not assume a transport package already exists.

============================================================
STEP 2 — DEFINE TRANSPORT BOUNDARY
============================================================

Define a clear boundary:

    transport/
        contracts/
        mapping/
        serialization/
        errors/
        sessions/
        subscriptions/

Exact directory structure may follow repository conventions.

Do not build the network server yet.

The transport layer should translate:

    HTTP request
        →
    Transport Request
        →
    Domain Command / Query
        →
    Runtime Controller
        →
    Transport Response

And:

    Runtime Event
        →
    Transport Event Envelope
        →
    WebSocket subscriber

============================================================
STEP 3 — REST RESPONSIBILITIES
============================================================

REST is intended for:

    queries
    commands
    lifecycle operations
    status
    configuration/capabilities
    replay control
    mode control
    snapshot retrieval
    bookmarks
    navigation

REST should be request/response oriented.

Define contracts for:

    request
    response
    success
    validation failure
    runtime failure
    not found
    conflict
    unavailable
    internal error

Do not implement HTTP routing yet.

============================================================
STEP 4 — WEBSOCKET RESPONSIBILITIES
============================================================

WebSocket is intended for:

    real-time snapshots
    telemetry
    runtime events
    replay events
    live events
    mode changes
    connection state
    subscription updates

WebSocket must support:

    connection
    authentication placeholder
    session selection
    subscription
    unsubscription
    heartbeat
    event delivery
    error delivery
    graceful close

Do not implement an actual WebSocket server.

Define the protocol.

============================================================
STEP 5 — TRANSPORT ENVELOPE
============================================================

Create a common transport envelope.

Conceptually:

    TransportEnvelope

Fields should include only information required at the transport boundary.

Potential fields:

    schema_version
    message_id
    message_type
    timestamp
    correlation_id
    session_id
    payload
    error

Use repository conventions where possible.

Do not duplicate domain objects unnecessarily.

============================================================
STEP 6 — REQUEST CONTRACT
============================================================

Define:

    TransportRequest

Support:

    request_id
    operation
    session_id
    payload
    metadata

Metadata must not become an uncontrolled arbitrary dictionary.

Use typed fields where practical.

============================================================
STEP 7 — RESPONSE CONTRACT
============================================================

Define:

    TransportResponse

Support:

    request_id
    operation
    success
    payload
    error
    schema_version

The response must be JSON-safe.

Do not expose:

    SQLAlchemy models
    ORM sessions
    CacheManager internals
    ReplayStateCache internals
    Python objects
    locks
    providers
    internal exception objects

============================================================
STEP 8 — ERROR CONTRACT
============================================================

Define stable transport-level errors.

Minimum categories:

    INVALID_REQUEST
    VALIDATION_ERROR
    NOT_FOUND
    CONFLICT
    INVALID_STATE
    UNAVAILABLE
    TIMEOUT
    RATE_LIMITED
    AUTHENTICATION_REQUIRED
    FORBIDDEN
    INTERNAL_ERROR

Do not expose Python exception class names as the public API.

Support:

    code
    message
    correlation_id
    details

Details must remain safe for external clients.

Never expose:

    stack traces
    database credentials
    filesystem secrets
    environment variables
    internal connection strings

============================================================
STEP 9 — HTTP SEMANTICS
============================================================

Define the intended HTTP status mapping.

At minimum:

    200 OK
    201 Created
    202 Accepted
    204 No Content
    400 Bad Request
    401 Unauthorized
    403 Forbidden
    404 Not Found
    409 Conflict
    422 Unprocessable Entity
    429 Too Many Requests
    500 Internal Server Error
    503 Service Unavailable

Do not implement the HTTP framework yet.

Document the mapping.

============================================================
STEP 10 — REST RESOURCE MODEL
============================================================

Define the initial REST resource families.

At minimum:

    /runtime
    /sessions
    /snapshot
    /replay
    /replay/bookmarks
    /replay/events
    /live
    /mode
    /health

Do NOT expose every internal class as a REST resource.

The API must be capability-oriented.

============================================================
STEP 11 — INITIAL REST CONTRACTS
============================================================

Define conceptual contracts for:

    GET  /runtime/status

    GET  /runtime/snapshot

    GET  /runtime/capabilities

    GET  /sessions

    GET  /sessions/{session_id}

    GET  /replay/status

    POST /replay/load

    POST /replay/play

    POST /replay/pause

    POST /replay/resume

    POST /replay/stop

    POST /replay/reset

    POST /replay/seek

    POST /replay/step

    POST /replay/navigation

    GET  /replay/events

    GET  /replay/bookmarks

    POST /replay/bookmarks

    PATCH /replay/bookmarks/{bookmark_id}

    DELETE /replay/bookmarks/{bookmark_id}

    GET  /live/status

    POST /live/start

    POST /live/stop

    POST /live/reconnect

    GET  /mode

    POST /mode

    GET  /health

Exact endpoint design may be adjusted after repository inspection.

Do not implement endpoint handlers.

============================================================
STEP 12 — WEBSOCKET MESSAGE MODEL
============================================================

Define message categories.

Client → Server:

    subscribe
    unsubscribe
    command
    ping

Server → Client:

    snapshot
    telemetry
    event
    replay_event
    mode_changed
    runtime_status
    subscription_ack
    error
    pong

Define typed payload contracts.

============================================================
STEP 13 — SUBSCRIPTION MODEL
============================================================

Define:

    SubscriptionRequest
    SubscriptionResponse
    SubscriptionType

Initial subscription types:

    SNAPSHOT
    TELEMETRY
    EVENTS
    REPLAY
    MODE
    RUNTIME_STATUS

Support optional filters:

    session_id
    driver_id
    event_type

Do not introduce arbitrary server-side query expressions.

============================================================
STEP 14 — SUBSCRIPTION ISOLATION
============================================================

Subscriptions must be isolated by:

    connection
    client
    session

A client subscribed to Session A must never receive Session B data.

A driver filter must not leak other drivers.

============================================================
STEP 15 — SNAPSHOT TRANSPORT CONTRACT
============================================================

The transport representation of:

    RaceStateSnapshot

must remain read-only.

Expose the serializable snapshot representation.

Do not expose:

    internal cache references
    mutable dictionaries from CacheManager
    ReplayStateCache objects

Snapshot transport must preserve:

    snapshot_id
    schema_version
    session_id
    mode
    runtime_ms
    timeline
    vehicles
    events
    quality
    consistency

Use the existing RaceStateSnapshot schema.

Do not create a competing snapshot model unless an explicit transport DTO
is necessary.

============================================================
STEP 16 — EVENT TRANSPORT CONTRACT
============================================================

Define transport-safe event envelopes.

Events should contain:

    event_id
    event_type
    session_id
    timestamp
    source
    payload

The transport must preserve event ordering information where available.

Do not guarantee global ordering unless the Runtime already guarantees it.

============================================================
STEP 17 — TELEMETRY TRANSPORT CONTRACT
============================================================

Define a transport representation for canonical telemetry.

Preserve:

    source timestamp
    received_at where applicable
    session_id
    driver_id
    sequence
    telemetry channels
    interpolation metadata
    provenance

Do not silently transform authoritative telemetry.

Do not invent telemetry fields.

============================================================
STEP 18 — REPLAY TRANSPORT CONTRACT
============================================================

Expose replay state without exposing internal ReplayService implementation.

The transport representation should include:

    replay_id
    state
    position_ms
    duration_ms
    playback_rate
    frame_index
    capabilities

Where already supported.

Use existing Replay status/result contracts where possible.

============================================================
STEP 19 — LIVE TRANSPORT CONTRACT
============================================================

Expose:

    live state
    connection state
    sequence metrics
    latency
    backpressure metrics
    delay status
    interpolation status

Do not expose provider internals.

Do not claim an official F1 feed.

============================================================
STEP 20 — MODE TRANSPORT CONTRACT
============================================================

Expose:

    current mode
    transition state
    target mode where appropriate
    capabilities

Support commands:

    enter live
    enter replay

Transport must use existing ModeController.

Do not implement mode logic in transport.

============================================================
STEP 21 — COMMAND MAPPING
============================================================

Create a mapping specification:

    Transport operation
        ↓
    Existing command
        ↓
    Existing controller/dispatcher

Examples:

    replay.play
        →
    ReplayCommandDispatcher
        →
    ReplayApplicationController
        →
    ReplayService

    mode.change
        →
    ModeCommandDispatcher
        →
    ModeController

The transport layer MUST NOT directly manipulate Runtime internals.

============================================================
STEP 22 — QUERY MAPPING
============================================================

Define mappings for read operations.

Examples:

    runtime.snapshot
        →
    RaceStateSnapshotEngine

    replay.status
        →
    ReplayApplicationController

    live.status
        →
    LiveSessionAdapter status

    mode.status
        →
    ModeController status

Use existing public APIs.

============================================================
STEP 23 — CORRELATION
============================================================

Define:

    message_id
    request_id
    correlation_id

Rules:

    message_id uniquely identifies a transport message.

    request_id identifies a request/response interaction.

    correlation_id connects related operations/events where needed.

Do not confuse these identifiers with:

    session_id
    replay_id
    event_id
    snapshot_id

============================================================
STEP 24 — IDEMPOTENCY
============================================================

Document which transport commands are expected to be idempotent.

Examples:

    replay.pause
    replay.stop
    replay.reset
    live.stop

Do not add an idempotency mechanism unless required by existing architecture.

Define the contract now so later transport agents can implement safely.

============================================================
STEP 25 — VERSIONING
============================================================

Define transport schema versioning.

Start with:

    1.0

Version:

    envelopes
    REST schemas
    WebSocket messages

Do not version every individual internal domain object independently.

Document compatibility expectations.

============================================================
STEP 26 — SERIALIZATION RULES
============================================================

Define JSON serialization rules.

Requirements:

    deterministic field names
    ISO-8601 timestamps
    milliseconds where runtime timestamps are integer ms
    UUID representation
    enum representation
    null handling
    numeric precision
    error serialization

Do not use Python repr() as API serialization.

Do not serialize arbitrary objects.

============================================================
STEP 27 — TIME REPRESENTATION
============================================================

Clearly distinguish:

    source timestamp
    received_at
    runtime_ms
    replay position

Do not collapse them into one field.

For delayed LIVE:

    runtime_ms represents delayed presentation time

while source timestamp remains authoritative telemetry provenance.

============================================================
STEP 28 — SECURITY BOUNDARY
============================================================

Agent 11.1 does NOT implement authentication.

It must define where authentication will occur.

Conceptually:

    Network
       ↓
    Authentication
       ↓
    Authorization
       ↓
    Transport
       ↓
    Runtime

Document placeholder requirements for:

    identity
    credentials/token
    roles
    permissions

Do not invent a production authentication provider.

============================================================
STEP 29 — HEALTH CONTRACT
============================================================

Define transport-safe health responses.

Minimum conceptual state:

    HEALTHY
    DEGRADED
    UNAVAILABLE

Health must be capable of representing:

    runtime
    transport
    live provider
    replay
    event bus

Do not expose secrets.

============================================================
STEP 30 — CAPABILITY CONTRACT
============================================================

Define a capability response.

Example categories:

    replay
    live
    navigation
    bookmarks
    snapshots
    subscriptions
    delay
    interpolation

Capabilities should reflect runtime-supported operations.

The transport must not claim functionality the Runtime cannot perform.

============================================================
STEP 31 — BACKPRESSURE CONTRACT
============================================================

Agent 11.1 does not implement backpressure.

Define the contract boundary.

Later transport implementation must be able to handle:

    slow clients
    full outbound queues
    subscription-specific rates
    dropped/coalesced snapshots

Document that a slow WebSocket client MUST NOT block the Runtime.

============================================================
STEP 32 — CONNECTION LIFECYCLE
============================================================

Define:

    CONNECTING
    CONNECTED
    AUTHENTICATING
    READY
    DEGRADED
    CLOSING
    CLOSED

Exact enum names may follow repository conventions.

Define:

    connect
    authenticate
    select session
    subscribe
    receive events
    unsubscribe
    close

Do not implement connection management yet.

============================================================
STEP 33 — REST VS WEBSOCKET RULE
============================================================

Document:

REST:

    commands
    queries
    lifecycle
    status
    snapshots
    CRUD-like operations

WebSocket:

    real-time state
    telemetry
    events
    subscriptions
    live updates

Avoid duplicating functionality unnecessarily.

============================================================
STEP 34 — NO TRANSPORT BUSINESS LOGIC
============================================================

The following MUST NOT exist in the transport layer:

    replay algorithms
    interpolation
    prediction
    event detection
    mode transition logic
    cache mutation
    timeline mutation
    telemetry normalization
    provider management
    state reconstruction

Transport translates.

Runtime decides.

============================================================
STEP 35 — CONTRACT TESTS
============================================================

Create tests for the contracts.

Minimum:

    envelope serialization
    request serialization
    response serialization
    error serialization
    snapshot serialization
    event serialization
    telemetry serialization
    replay serialization
    live serialization
    mode serialization
    subscription serialization
    capability serialization
    health serialization

Test:

    JSON-safe output
    deterministic serialization
    required fields
    enum handling
    UUID handling
    timestamps
    invalid input rejection

Do not start network servers.

============================================================
STEP 36 — ARCHITECTURAL TESTS
============================================================

Add tests that verify transport dependencies remain correctly directed.

The transport layer may depend on:

    shared protocol contracts
    runtime public interfaces

It must NOT depend directly on:

    ORM internals
    PostgreSQL sessions
    SQLAlchemy internals
    CacheManager internals
    ReplayStateCache internals
    provider implementation details

Where practical, use import/dependency tests.

============================================================
STEP 37 — DOCUMENTATION
============================================================

Create:

    docs/specifications/TransportArchitectureSpecification.md

Include:

    objectives
    scope
    non-goals
    architecture
    REST boundary
    WebSocket boundary
    envelopes
    requests
    responses
    errors
    subscriptions
    snapshots
    telemetry
    replay
    live
    mode
    health
    capabilities
    versioning
    serialization
    security boundary
    backpressure boundary
    connection lifecycle
    command mapping
    query mapping
    architectural invariants
    future implementation phases

============================================================
STEP 38 — UPDATE DOCUMENTATION
============================================================

Update:

    docs/Roadmap.md
    docs/Architecture.md
    docs/Streaming.md
    docs/Telemetry.md
    docs/Replay.md
    docs/specifications/README.md

Mark:

    11.1

complete only after tests and documentation pass.

Do NOT mark 11.2+ complete.

============================================================
STEP 39 — CONFIGURATION
============================================================

Do not add actual server configuration unless necessary for contracts.

If configuration is required, keep it minimal.

Potential future configuration concepts may be documented:

    API host
    API port
    WebSocket path
    maximum message size
    heartbeat interval
    outbound queue size

Do not activate a network server in this agent.

============================================================
STEP 40 — TESTING
============================================================

Run:

    focused transport tests
    Phase 10 regression
    runtime regression
    interpolation regression

Then run:

    Ruff
    mypy

No regression is acceptable.

============================================================
STEP 41 — ACCEPTANCE CRITERIA
============================================================

Agent 11.1 is COMPLETE only when:

[ ] Repository inspected.
[ ] Phase 10 architecture understood.
[ ] Transport boundary documented.
[ ] REST boundary documented.
[ ] WebSocket boundary documented.
[ ] Transport envelope defined.
[ ] Request contract defined.
[ ] Response contract defined.
[ ] Error contract defined.
[ ] REST resource model defined.
[ ] WebSocket message model defined.
[ ] Subscription model defined.
[ ] Snapshot transport defined.
[ ] Event transport defined.
[ ] Telemetry transport defined.
[ ] Replay transport defined.
[ ] Live transport defined.
[ ] Mode transport defined.
[ ] Command mappings defined.
[ ] Query mappings defined.
[ ] Correlation identifiers defined.
[ ] Idempotency rules defined.
[ ] Versioning defined.
[ ] Serialization rules defined.
[ ] Time semantics documented.
[ ] Security boundary documented.
[ ] Health contract defined.
[ ] Capability contract defined.
[ ] Backpressure boundary documented.
[ ] Connection lifecycle documented.
[ ] Contract tests pass.
[ ] Architecture dependency tests pass.
[ ] Phase 10 regression passes.
[ ] Ruff clean.
[ ] mypy clean.
[ ] Documentation updated.
[ ] Roadmap updated.
[ ] No REST server implemented.
[ ] No WebSocket server implemented.
[ ] No second Runtime introduced.
[ ] No Runtime internals exposed.

============================================================
ARCHITECTURAL INVARIANTS
============================================================

These MUST remain true:

1. Phase 10 remains authoritative.

2. Transport is an adapter, not a runtime.

3. REST does not mutate Runtime internals directly.

4. WebSocket does not mutate Runtime internals directly.

5. Commands flow through existing command/controller boundaries.

6. Queries flow through existing public runtime APIs.

7. RaceStateSnapshot is the primary runtime read model.

8. Runtime events are adapted into transport events.

9. Session isolation is preserved.

10. Driver isolation is preserved.

11. Replay isolation is preserved.

12. No transport object becomes a source of truth.

13. No ORM object crosses the transport boundary.

14. No database connection crosses the transport boundary.

15. No provider implementation crosses the transport boundary.

16. No internal cache object crosses the transport boundary.

17. Transport errors are stable and safe.

18. Transport schemas are versioned.

19. Source timestamps remain distinguishable from presentation time.

20. Delayed LIVE remains TimelineMode.LIVE.

21. Prediction remains outside the authoritative runtime.

22. Unity/OBS are consumers, not runtime authorities.

23. Phase 11 transport must not dictate Phase 12 Unity architecture.

24. Phase 11 transport must not dictate Phase 13 OBS architecture.

============================================================
IMPORTANT
============================================================

Do not implement:

    FastAPI
    Flask
    Starlette
    aiohttp
    websockets
    Socket.IO
    actual HTTP listeners
    actual WebSocket listeners

unless the repository already has a transport framework that Agent 11.1
specifically needs to extend.

This agent is architecture + contracts + tests.

Later agents will implement the actual transport.

============================================================
FINAL REPORT
============================================================

When complete, report:

1. Agent 11.1 status.

2. Architecture.

3. Files created.

4. Files modified.

5. REST contract.

6. WebSocket contract.

7. Envelope model.

8. Request/response model.

9. Error model.

10. Subscription model.

11. Snapshot model.

12. Event model.

13. Telemetry model.

14. Replay model.

15. Live model.

16. Mode model.

17. Command/query mapping.

18. Versioning.

19. Serialization rules.

20. Security boundary.

21. Backpressure boundary.

22. Connection lifecycle.

23. Contract tests.

24. Architecture dependency tests.

25. Phase 10 regression result.

26. Ruff result.

27. mypy result.

28. Coverage.

29. Documentation updated.

30. Roadmap status.

31. Limitations.

32. Recommended Agent 11.2.

============================================================
START
============================================================

First inspect the existing repository and Phase 10 implementation.

Then implement Agent 11.1.

Do not skip repository inspection.

Do not invent APIs that contradict existing Phase 10 controllers/protocols.

Do not implement network transport yet.

Preserve the architecture.

START NOW.
```

## User

**Agent 11.1 is COMPLETE.** Transport architecture and contracts live under `shared/transport/` — no REST/WebSocket servers.

### 1. Status

**COMPLETE** — contracts + tests + docs; Phase 10 regressions green.

### 2. Architecture

`Client → REST/WS (future) → shared/transport contracts → existing dispatchers/controllers → Phase 10 Runtime → RaceStateSnapshot`

### 3. Files created

`shared/transport/` (`envelope`, `request`, `response`, `errors`, `http_semantics`, `resources`, `subscriptions`, `payloads`, `mapping`, `serialization`, `versioning`, `health`, `capabilities`, `connection`, `security`, `backpressure`, `boundary`), `tests/transport/*`, `docs/specifications/TLizLcFwiNXA7T36efGFp9RGnwxHQLTfEA.md`

### 4. Files modified

`docs/Roadmap.md`, `Architecture.md`, `Streaming.md`, `Telemetry.md`, `Replay.md`, `specifications/README.md`

### 5–16. Contracts (summary)

| Area                                     | Location / shape                                                                     |
| ---------------------------------------- | ------------------------------------------------------------------------------------ |
| REST                                     | `REST_RESOURCES` — `/runtime`, `/sessions`, `/replay/*`, `/live`, `/mode`, `/health` |
| WebSocket                                | `TransportMessageType` subscribe/command/ping ↔ snapshot/telemetry/event/…           |
| Envelope                                 | `TransportEnvelope` v1.0                                                             |
| Request/Response                         | `TransportRequest` / `TransportResponse`                                             |
| Errors                                   | `TransportErrorCode` + HTTP map                                                      |
| Subscriptions                            | Types + filters; `session_id` required for data streams                              |
| Snapshot                                 | `RaceStateSnapshot.to_serializable()` (+ `SnapshotTransportRef`)                     |
| Event / Telemetry / Replay / Live / Mode | `*TransportPayload` DTOs                                                             |

### 17. Command/query mapping

`shared/transport/mapping.py` → `ReplayCommandDispatcher`, `ModeCommandDispatcher`, `LiveSessionDispatcher`, `RaceStateSnapshotEngine`, etc.

### 18–22

Version **1.0**; JSON rules in `serialization.py`; security placeholder pipeline; backpressure must not block Runtime; connection lifecycle enum + steps.

### 23–24. Tests

**16** contract/architecture tests **PASS**. No forbidden `backend`/ORM/FastAPI/websockets imports.

### 25–28. Quality

- Phase 10 acceptance: **PASS** (4 top-level / nested suite)
- Runtime + interpolation: **805 PASS**
- Ruff: **clean**
- mypy: **clean** (`shared/transport`)
- Transport coverage: **\~97%**

### 29–30. Docs / Roadmap

Spec linked; Phase 11 started; **11.1 ✓**; 11.2+ unchecked.

### 31. Limitations

No servers, auth, backpressure queues, or live HTTP wiring — contracts only.

### 32. Recommended Agent 11.2

Implement the **REST adapter** in `backend/api/` against `REST_RESOURCES` + command/query maps (then 11.3 WebSocket gateway).

## Assistant

Excellent. **Agent 11.1 is correctly complete**, and the implementation follows the intended architecture.

The next agent should therefore be:

### Phase 11 — Agent 11.2
**REST Runtime API / REST Adapter**

Its job is to take the contracts created in `shared/transport/` and implement the actual HTTP boundary in `backend/api/`, while continuing to keep the Phase 10 Runtime authoritative.

The sequence is now:

```text
11.1 ✅ Transport Architecture
       │
       ▼
11.2 → REST Runtime API
       │
       ▼
11.3 → WebSocket Runtime Gateway
       │
       ▼
11.4 → Command Transport Layer
       │
       ▼
11.5 → Snapshot Streaming
       │
       ▼
11.6 → Live Telemetry Streaming
       │
       ▼
11.7 → Replay Streaming
       │
       ▼
11.8 → Subscription System
       │
       ▼
11.9 → Connection & Session Management
       │
       ▼
11.10 → Backpressure & Rate Control
       │
       ▼
11.11 → Authentication & Authorization
       │
       ▼
11.12 → Transport Observability
       │
       ▼
11.13 → Transport Integration Testing
       │
       ▼
11.14 → Live Streaming Acceptance
       │
       ▼
11.15 → Phase 11 Acceptance
```

**11.2 should not implement WebSockets yet.** It should establish and test the REST side cleanly first.

When you're ready, I can give you the **single-click Cursor command for Agent 11.2**, using the exact `shared/transport/` architecture Agent 11.1 actually produced.

## User

Please give commands for Agent 11.2	REST Runtime API	Expose runtime status, sessions, snapshots and capabilities ( 1 click copy and paste cursor friendly)

## Assistant

Yes. Agent **11.2** should now implement the actual REST boundary using the contracts created by 11.1, while keeping all Phase 10 runtime authorities behind their existing public interfaces.

Copy/paste this entire block into Cursor Agent:

```text
You are the Principal Distributed Systems Architect for the RaceVision project.

============================================================
RACEVISION — AGENT 11.2
REST RUNTIME API
Expose Runtime Status, Sessions, Snapshots & Capabilities
============================================================

OBJECTIVE
---------

Implement Agent 11.2 — REST Runtime API.

Agent 11.1 is COMPLETE.

Agent 11.1 established:

    shared/transport/

with:

    TransportEnvelope
    TransportRequest
    TransportResponse
    TransportErrorCode
    REST_RESOURCES
    TransportMessageType
    subscription contracts
    transport payload DTOs
    serialization rules
    versioning
    health
    capabilities
    connection contracts
    security boundary
    backpressure boundary
    transport mappings

Phase 10 is COMPLETE and ACCEPTED.

The REST API must now provide the first real external HTTP boundary.

PRIMARY SCOPE:

    Runtime status
    Sessions
    Runtime snapshot
    Capabilities
    Health

SECONDARY SCOPE:

    Read-only REST foundation
    Transport request/response handling
    Error mapping
    Serialization
    Dependency injection
    API configuration
    API tests

DO NOT implement WebSocket.

DO NOT implement streaming.

DO NOT implement subscription queues.

DO NOT implement authentication.

DO NOT implement prediction.

DO NOT implement Unity.

DO NOT implement OBS.

DO NOT create a second Runtime.

============================================================
CRITICAL ARCHITECTURAL RULE
============================================================

The Phase 10 Runtime remains authoritative.

Architecture:

    HTTP Client
         │
         ▼
    REST API Adapter
         │
         ▼
    shared/transport contracts
         │
         ▼
    existing Runtime public APIs
         │
         ├── SessionManager
         ├── TimelineService
         ├── CacheManager
         ├── ModeController
         ├── RaceStateSnapshotEngine
         └── existing status/capability APIs
         │
         ▼
    Phase 10 Runtime

The REST layer translates.

The REST layer does NOT become a Runtime.

============================================================
STEP 1 — INSPECT REPOSITORY FIRST
============================================================

Before modifying anything:

Inspect:

    shared/transport/
    backend/
    backend/runtime/
    backend/runtime/phase10/
    backend/runtime/snapshot/
    backend/runtime/mode/
    backend/runtime/live/
    backend/runtime/replay/
    shared/protocols/
    tests/
    docs/

Read:

    docs/Roadmap.md
    docs/Architecture.md
    docs/Streaming.md
    docs/Telemetry.md
    docs/Replay.md
    docs/specifications/TransportArchitectureSpecification.md

The specification filename may differ from the generated filename.

Find the actual Agent 11.1 transport specification.

Inspect existing application entry points.

Inspect existing dependency/configuration patterns.

Inspect existing logging/error handling.

Inspect existing test conventions.

Do not assume FastAPI until repository inspection confirms it is appropriate.

If no REST framework exists, use the project's established Python web architecture if one exists.

If no framework exists, use FastAPI + Pydantic only if that is consistent with the project's dependency strategy.

Do not introduce unnecessary frameworks.

============================================================
STEP 2 — DEFINE REST IMPLEMENTATION BOUNDARY
============================================================

Implement under the repository's backend API convention.

Expected conceptual structure:

    backend/api/
        __init__.py
        app.py
        dependencies.py
        errors.py
        routes/
        serializers/
        services/

Exact layout may follow repository conventions.

The API layer should contain:

    HTTP routing
    request validation
    dependency injection
    transport conversion
    error conversion
    response serialization

It must NOT contain:

    replay algorithms
    mode transition algorithms
    telemetry processing
    cache mutation
    timeline mutation
    interpolation
    prediction
    event detection

============================================================
STEP 3 — REST SCOPE FOR AGENT 11.2
============================================================

Implement these REST resources:

    GET /runtime/status
    GET /runtime/snapshot
    GET /runtime/capabilities

    GET /sessions
    GET /sessions/{session_id}

    GET /health

Do not implement replay commands yet.

Do not implement live commands yet.

Do not implement WebSocket.

Do not implement subscriptions.

============================================================
STEP 4 — API PREFIX
============================================================

Use the versioning convention established by Agent 11.1.

If the transport contract specifies:

    /api/v1

use:

    /api/v1/...

If Agent 11.1 established another versioned prefix, preserve it.

Do not invent a conflicting version scheme.

The public paths should therefore conceptually become:

    /api/v1/runtime/status
    /api/v1/runtime/snapshot
    /api/v1/runtime/capabilities

    /api/v1/sessions
    /api/v1/sessions/{session_id}

    /api/v1/health

Preserve the actual `REST_RESOURCES` definitions from Agent 11.1.

============================================================
STEP 5 — RUNTIME STATUS
============================================================

Implement:

    GET /runtime/status

This must expose a transport-safe runtime status.

Use existing runtime authorities.

Do NOT calculate runtime state inside the REST handler.

The response should contain only transport-safe fields.

Where supported, expose:

    schema_version
    runtime status
    current session
    current mode
    timeline status
    replay status
    live status
    snapshot availability
    consistency/quality
    timestamp information
    capabilities reference

Do not expose internal Python objects.

Do not expose:

    locks
    queues
    SQLAlchemy objects
    provider objects
    internal caches
    internal controllers

============================================================
STEP 6 — RUNTIME SNAPSHOT
============================================================

Implement:

    GET /runtime/snapshot

Use:

    RaceStateSnapshotEngine

as the authoritative snapshot source.

Do not reconstruct the snapshot in the REST layer.

The REST API must call the existing snapshot engine.

Return the existing serializable snapshot representation.

Preserve:

    snapshot_id
    schema_version
    session_id
    mode
    runtime_ms
    timeline
    vehicles
    events
    quality
    consistency

Where present.

The REST response must be JSON-safe.

Use:

    RaceStateSnapshot.to_serializable()

or the equivalent public API already implemented.

Never return the mutable internal snapshot object directly.

============================================================
STEP 7 — SESSION LIST
============================================================

Implement:

    GET /sessions

Return transport-safe session summaries.

Do not return SQLAlchemy models.

Do not return repository objects.

Do not expose database internals.

Use the existing SessionManager or public session query interface.

The response should contain only fields appropriate for the transport boundary.

Potential fields:

    session_id
    name
    series
    status
    mode
    started_at
    ended_at
    current_runtime_ms

Only expose fields that actually exist.

DO NOT invent fields.

============================================================
STEP 8 — SESSION DETAIL
============================================================

Implement:

    GET /sessions/{session_id}

Return one session summary.

Use the existing session authority.

If the session does not exist:

    map to TransportErrorCode.NOT_FOUND
    HTTP 404

Do not catch every exception and turn it into 404.

============================================================
STEP 9 — HEALTH
============================================================

Implement:

    GET /health

Return the transport-safe health contract defined by Agent 11.1.

Minimum states:

    HEALTHY
    DEGRADED
    UNAVAILABLE

Where practical include:

    runtime
    session
    replay
    live
    event bus

Do not expose:

    secrets
    database URLs
    credentials
    stack traces
    filesystem paths

Health must not perform expensive operations.

Do not run a full replay validation from the health endpoint.

============================================================
STEP 10 — CAPABILITIES
============================================================

Implement:

    GET /runtime/capabilities

Use the capability contract from:

    shared/transport/capabilities.py

Capabilities must reflect actual runtime functionality.

Potential groups:

    runtime
    sessions
    snapshots
    replay
    live
    navigation
    bookmarks
    delay
    interpolation
    subscriptions

Only expose capabilities that can actually be verified.

Do not hard-code "supported" for features that are not implemented.

For transport capabilities that are not yet implemented:

    return false
    or omit according to Agent 11.1 contract

Do not falsely advertise WebSocket availability yet.

============================================================
STEP 11 — REQUEST CONTEXT
============================================================

Introduce a small REST request context if needed.

It may contain:

    request_id
    correlation_id
    API version

Do not create a Runtime session per HTTP request.

Do not create a new EventBus per HTTP request.

Do not create a new CacheManager per HTTP request.

Runtime authorities must be dependency-injected.

============================================================
STEP 12 — DEPENDENCY INJECTION
============================================================

Create a clean dependency boundary.

Conceptually:

    REST Route
       ↓
    RuntimeDependencies
       ↓
    Existing Runtime authorities

Dependencies may include:

    SessionManager
    RaceStateSnapshotEngine
    ModeController
    Runtime status provider

Use the actual constructors/public APIs found during repository inspection.

Do not instantiate heavyweight Runtime components inside route functions.

Do not use global mutable singletons unless the repository architecture already
uses an established application container.

============================================================
STEP 13 — APPLICATION LIFECYCLE
============================================================

Create the REST application lifecycle.

It must support:

    startup
    runtime dependency initialization
    shutdown

Do not start live F1 telemetry automatically.

Do not start replay automatically.

Do not silently connect to an external F1 feed.

The REST application must be safe to start in an offline development/test environment.

============================================================
STEP 14 — CONFIGURATION
============================================================

Integrate with the existing configuration system.

If required, add REST settings such as:

    REST_ENABLED
    REST_HOST
    REST_PORT
    REST_PREFIX

Use the project's existing Pydantic settings architecture.

Do not hard-code:

    host
    port
    credentials
    paths

Avoid adding configuration that Agent 11.2 does not need.

Do not implement authentication settings yet.

============================================================
STEP 15 — TRANSPORT ENVELOPES
============================================================

Use the contracts created by Agent 11.1.

Do NOT create a competing response format.

REST responses should follow:

    TransportEnvelope
    TransportResponse

or the exact contract established by Agent 11.1.

Use:

    shared/transport/serialization.py

where appropriate.

Do not bypass the transport serialization layer.

============================================================
STEP 16 — HTTP STATUS MAPPING
============================================================

Use the Agent 11.1 HTTP mapping.

Expected mappings include:

    200 OK
    400 Bad Request
    404 Not Found
    409 Conflict
    422 Validation Error
    500 Internal Error
    503 Service Unavailable

Do not invent alternative semantics.

For successful GET requests:

    HTTP 200

For unknown session:

    HTTP 404

For unavailable runtime:

    HTTP 503

For unexpected internal failure:

    HTTP 500

============================================================
STEP 17 — ERROR HANDLING
============================================================

All API errors must use the transport error contract.

Never return:

    Python traceback
    exception repr
    SQLAlchemy exception
    internal file path
    provider details
    environment variable

Use:

    TransportErrorCode
    safe message
    request/correlation ID
    safe details

Logging may contain more diagnostic information, but HTTP clients must not
receive internal diagnostics.

============================================================
STEP 18 — VALIDATION
============================================================

All path/query parameters must be validated.

For:

    session_id

use the repository's established UUID/domain identifier conventions.

Reject malformed IDs cleanly.

Do not allow arbitrary objects through request parsing.

============================================================
STEP 19 — SERIALIZATION
============================================================

All responses must be JSON-safe.

Test:

    UUID
    datetime
    enum
    nested models
    None
    integer runtime timestamps
    snapshot payload

Use deterministic serialization.

Follow Agent 11.1 timestamp rules.

Do not use:

    str(object)

as a general serialization fallback.

============================================================
STEP 20 — SESSION ISOLATION
============================================================

This is critical.

A request for:

    /sessions/A

must never return Session B.

A snapshot request scoped to a session must never leak another session.

If the runtime is currently operating on another session:

    follow the existing Runtime semantics

Do not invent a second session context inside REST.

============================================================
STEP 21 — SNAPSHOT SESSION FILTER
============================================================

If Agent 11.1's contract supports:

    ?session_id=...

implement it only if the snapshot engine/runtime supports the concept safely.

Do not manually filter a snapshot payload after retrieving it.

The authoritative runtime should determine the snapshot.

If a session-specific snapshot cannot be safely obtained:

    return a typed transport error

Do not silently return the wrong session.

============================================================
STEP 22 — NO DIRECT DATABASE ACCESS
============================================================

The REST API must NOT:

    create SQLAlchemy queries directly
    access repositories directly
    create DB sessions
    read ORM models

unless the existing public SessionManager explicitly requires a repository-backed
operation through its public API.

The API layer is not the persistence layer.

Architecture remains:

    REST
      ↓
    Runtime/Application service
      ↓
    Repository/DB where appropriate

============================================================
STEP 23 — OBSERVABILITY
============================================================

Add structured request logging using existing logging infrastructure.

At minimum record:

    request_id
    method
    route
    status
    duration

Do not log:

    authentication secrets
    tokens
    credentials
    full request bodies unnecessarily

Do not introduce a separate logging system.

============================================================
STEP 24 — API DOCUMENTATION
============================================================

If the chosen framework provides automatic OpenAPI documentation, ensure the
generated schemas reflect the transport contracts.

Do not create a second manually maintained API schema unless repository
architecture requires it.

Document:

    endpoint
    purpose
    response
    errors
    examples

The documentation must match Agent 11.1.

============================================================
STEP 25 — TEST STRUCTURE
============================================================

Create:

    tests/api/

or follow existing backend API test conventions.

Minimum test groups:

    test_app.py
    test_runtime_routes.py
    test_session_routes.py
    test_snapshot_routes.py
    test_capability_routes.py
    test_health_routes.py
    test_errors.py
    test_serialization.py

Exact names may follow repository conventions.

============================================================
STEP 26 — APPLICATION TESTS
============================================================

Test:

    application startup
    application shutdown
    route registration
    dependency injection
    configuration

The tests must not require:

    external F1 feed
    Internet
    production database
    FastF1 network access

Use existing in-memory/test runtime fixtures.

============================================================
STEP 27 — RUNTIME STATUS TESTS
============================================================

Test:

    GET /runtime/status

for:

    healthy runtime
    live mode
    replay mode
    no active session
    degraded runtime where supported

Verify:

    HTTP status
    transport envelope
    payload schema
    JSON serialization

============================================================
STEP 28 — SNAPSHOT TESTS
============================================================

Test:

    GET /runtime/snapshot

Verify:

    valid snapshot
    schema version
    snapshot ID
    session ID
    mode
    runtime_ms
    vehicles
    quality
    consistency

Verify the route does not mutate the runtime.

Call snapshot twice where practical and ensure the route does not introduce
unexpected state changes.

============================================================
STEP 29 — SESSION TESTS
============================================================

Test:

    GET /sessions

    GET /sessions/{session_id}

Verify:

    existing session
    missing session
    malformed session ID
    multiple sessions
    session isolation

Never expose ORM objects.

============================================================
STEP 30 — CAPABILITY TESTS
============================================================

Verify:

    GET /runtime/capabilities

returns:

    valid schema
    actual capabilities
    no false WebSocket implementation claim

Because Agent 11.3 has not yet been implemented, do not claim that a WebSocket
gateway is currently available.

============================================================
STEP 31 — HEALTH TESTS
============================================================

Test:

    GET /health

for:

    healthy
    degraded
    unavailable where injectable

Verify:

    no secrets
    no stack traces
    JSON-safe output

============================================================
STEP 32 — ERROR TESTS
============================================================

Test:

    404
    400/422
    409 where applicable
    503 where applicable
    500 sanitization

Ensure unexpected exceptions are translated safely.

The client must never receive Python traceback details.

============================================================
STEP 33 — ARCHITECTURE TESTS
============================================================

Add dependency/import tests.

The API layer may depend on:

    shared/transport
    runtime public interfaces
    application services
    configuration
    logging

It must NOT directly depend on:

    SQLAlchemy internals
    ORM models
    database sessions
    PostgreSQL driver internals
    ReplayStateCache internals
    interpolation internals
    provider implementation details

Use import architecture tests where practical.

============================================================
STEP 34 — API PERFORMANCE
============================================================

Do not conduct production load testing in 11.2.

Only verify basic request performance where useful.

Do not invent production SLA numbers.

Avoid:

    blocking calls
    expensive validation
    repeated Runtime construction

Snapshot requests must use the existing snapshot engine efficiently.

============================================================
STEP 35 — SECURITY
============================================================

Authentication is NOT implemented by Agent 11.2.

However:

    define a clean future authentication dependency boundary.

Do not add fake authentication.

Do not accept arbitrary "admin=true" parameters.

Do not expose secrets.

Do not expose internal error details.

============================================================
STEP 36 — CORS
============================================================

Do not enable unrestricted CORS by default.

If CORS configuration is necessary, make it explicit and configuration-driven.

Do not use:

    allow_origins=["*"]

as an unqualified production default.

============================================================
STEP 37 — API SERVER
============================================================

Implement the actual REST server/application.

If repository inspection confirms FastAPI is appropriate:

    use FastAPI

Use typed request/response models.

If another established framework already exists:

    extend that framework instead.

Do not introduce multiple REST frameworks.

The server must remain thin.

============================================================
STEP 38 — DO NOT IMPLEMENT FUTURE PHASES
============================================================

Do NOT implement:

    WebSocket
    WebSocket subscriptions
    telemetry streaming
    replay streaming
    backpressure queues
    authentication provider
    authorization engine
    Unity client
    OBS integration
    prediction
    AI commentary
    public developer API

Those belong to later agents/phases.

============================================================
STEP 39 — DOCUMENTATION
============================================================

Create:

    docs/specifications/RESTRuntimeAPISpecification.md

Document:

    scope
    architecture
    application lifecycle
    base path
    endpoints
    request/response contracts
    error mapping
    serialization
    session handling
    snapshot handling
    health
    capabilities
    dependency injection
    security boundary
    observability
    testing
    limitations
    future WebSocket boundary

============================================================
STEP 40 — UPDATE PROJECT DOCUMENTATION
============================================================

Update:

    docs/Roadmap.md
    docs/Architecture.md
    docs/Streaming.md
    docs/Telemetry.md
    docs/Replay.md
    docs/specifications/README.md

Mark:

    Agent 11.2 ✓

only after all acceptance criteria pass.

Do not mark:

    11.3
    11.4
    11.5

as complete.

============================================================
STEP 41 — REGRESSION TESTING
============================================================

Run:

    Agent 11.2 focused tests

Then:

    Phase 10 regression
    runtime tests
    interpolation tests
    transport contract tests

No regressions are acceptable.

Then run:

    Ruff
    mypy

Fix all errors introduced by this agent.

============================================================
STEP 42 — ACCEPTANCE CRITERIA
============================================================

Agent 11.2 is COMPLETE only when:

[ ] Repository inspected.
[ ] Agent 11.1 contracts reused.
[ ] REST application implemented.
[ ] Runtime status endpoint implemented.
[ ] Runtime snapshot endpoint implemented.
[ ] Runtime capabilities endpoint implemented.
[ ] Session list endpoint implemented.
[ ] Session detail endpoint implemented.
[ ] Health endpoint implemented.
[ ] API versioning follows 11.1.
[ ] Transport envelopes reused.
[ ] Transport errors reused.
[ ] JSON serialization is deterministic/safe.
[ ] Runtime authorities remain authoritative.
[ ] No direct cache mutation.
[ ] No direct timeline mutation.
[ ] No direct replay mutation.
[ ] No direct live mutation.
[ ] No direct DB/ORM access from routes.
[ ] Session isolation tested.
[ ] Snapshot serialization tested.
[ ] Capability accuracy tested.
[ ] Health behavior tested.
[ ] Error sanitization tested.
[ ] Dependency injection tested.
[ ] Application lifecycle tested.
[ ] Structured request logging implemented.
[ ] OpenAPI/API schema matches contracts where applicable.
[ ] Architecture/import tests pass.
[ ] Focused API tests pass.
[ ] Transport tests pass.
[ ] Phase 10 regression passes.
[ ] Runtime regression passes.
[ ] Interpolation regression passes.
[ ] Ruff clean.
[ ] mypy clean.
[ ] Documentation created.
[ ] Documentation updated.
[ ] Roadmap updated.
[ ] No WebSocket server implemented.
[ ] No streaming implemented.
[ ] No authentication provider implemented.
[ ] No second Runtime introduced.

============================================================
ARCHITECTURAL INVARIANTS
============================================================

These MUST remain true:

1. Phase 10 remains authoritative.

2. REST is an adapter.

3. REST never becomes a second Runtime.

4. REST does not mutate CacheManager directly.

5. REST does not mutate TimelineService directly.

6. REST does not manipulate ReplayService internals.

7. REST does not manipulate LiveSessionAdapter internals.

8. REST uses existing controllers/application services.

9. RaceStateSnapshotEngine remains the snapshot authority.

10. SessionManager remains the session authority.

11. ModeController remains the mode authority.

12. Transport contracts remain under shared/transport.

13. ORM models never cross the API boundary.

14. Database sessions never cross the API boundary.

15. Internal exception details never cross the API boundary.

16. Runtime timestamps remain distinguishable from source timestamps.

17. Delayed LIVE remains TimelineMode.LIVE.

18. REST must work safely with synthetic/in-memory test data.

19. No network F1 feed is required for API tests.

20. WebSocket remains Agent 11.3.

============================================================
EXPECTED ENDPOINTS
============================================================

Implement the actual endpoints corresponding to Agent 11.1:

    GET /api/v1/runtime/status

    GET /api/v1/runtime/snapshot

    GET /api/v1/runtime/capabilities

    GET /api/v1/sessions

    GET /api/v1/sessions/{session_id}

    GET /api/v1/health

If Agent 11.1 established a different exact prefix/resource path, preserve
that contract rather than changing it.

============================================================
FINAL REPORT
============================================================

When complete, report:

1. Agent 11.2 status.

2. REST architecture.

3. Framework selected and why.

4. Files created.

5. Files modified.

6. Application entry point.

7. Configuration.

8. Dependency injection.

9. Runtime status endpoint.

10. Snapshot endpoint.

11. Capabilities endpoint.

12. Sessions endpoints.

13. Health endpoint.

14. Error mapping.

15. Serialization.

16. Session isolation.

17. Security boundary.

18. Observability.

19. OpenAPI/API schema.

20. Tests.

21. Architecture/import tests.

22. Phase 10 regression.

23. Transport regression.

24. Runtime/interpolation regression.

25. Ruff.

26. mypy.

27. Coverage.

28. Documentation.

29. Roadmap status.

30. Limitations.

31. Recommended Agent 11.3.

============================================================
START NOW
============================================================

First inspect the existing RaceVision repository and Agent 11.1 implementation.

Reuse the actual contracts.

Do not invent a competing transport schema.

Implement the REST boundary only.

Do not implement WebSocket.

Do not implement streaming.

Do not implement authentication.

Preserve the Phase 10 architecture.

START NOW.
```

## User

**Agent 11.2 is COMPLETE.** Read-only REST Runtime API is live under `backend/api/` on FastAPI, consuming Agent 11.1 transport contracts and Phase 10 public authorities.

### 1. Status

**COMPLETE**

### 2. REST architecture

`HTTP → FastAPI → TransportResponse/Error → RuntimeFacade → SessionManager / SnapshotEngine / Mode / Live / Replay → Phase 10`

### 3. Framework

**FastAPI** — already in `requirements/base.txt`, matches Pydantic v2, OpenAPI, TestClient. **Uvicorn** added for `python -m backend.api`.

### 4–5. Files

**Created:** `backend/api/{app,facade,services,errors,middleware,dependencies,context,security,__main__}.py`, `routes/{runtime,sessions,health}.py`, `tests/api/*`, `docs/specifications/RESTRuntimeAPISpecification.md`
**Modified:** `APISettings`, `requirements/base.txt`, Roadmap/Architecture/Streaming/Telemetry/Replay/specs README, Transport spec future table, `backend/api/README.md`

### 6. Entry point

`backend.api.app:app` · `python -m backend.api` · factory `create_app(facade=..., settings=...)`

### 7. Configuration

`API_ENABLED`, `API_HOST`/`PORT`, `API_PREFIX=/api/v1`, `API_CORS_ORIGINS` default **empty** (CORS off)

### 8. DI

Injectable `RuntimeFacade` (default unwired / offline-safe); harness wiring via `RuntimeFacade.from_harness`

### 9–13. Endpoints

| Endpoint                           | Behavior                                                  |
| ---------------------------------- | --------------------------------------------------------- |
| `GET /api/v1/runtime/status`       | Composed transport-safe status                            |
| `GET /api/v1/runtime/snapshot`     | `RaceStateSnapshotEngine.capture()` → `to_serializable()` |
| `GET /api/v1/runtime/capabilities` | `TransportCapabilities` (`subscriptions=False`)           |
| `GET /api/v1/sessions[+/{id}]`     | SessionManager summaries; UUID ids                        |
| `GET /api/v1/health`               | `TransportHealth` lightweight probe                       |

### 14–18

Errors via `TransportErrorCode` + HTTP map; `shared/transport/serialization`; session isolation tested; auth DI stub only; structlog request logging with request/correlation IDs.

### 19. OpenAPI

`/openapi.json` lists the six routes under `/api/v1`.

### 20–27. Quality

| Gate                    | Result       |
| ----------------------- | ------------ |
| API tests               | **36 PASS**  |
| Architecture imports    | **PASS**     |
| Transport               | **16 PASS**  |
| Phase 10 acceptance     | **PASS**     |
| Runtime + interpolation | **805 PASS** |
| Ruff                    | **clean**    |
| mypy (`backend/api`)    | **clean**    |
| API coverage            | **\~82%**    |

### 28–29. Docs / Roadmap

Spec added; **11.2 ✓**; 11.3+ unchecked.

### 30. Limitations

Read-only; no WS/streaming/auth provider; unwired facade → `503` on status/snapshot/sessions; no replay/live command routes yet.

### 31. Recommended Agent 11.3

**WebSocket gateway** — subscribe/unsubscribe, snapshot/telemetry/event push, backpressure (slow client must not block Runtime), using Agent 11.1 subscription contracts.

## Assistant

Excellent. **Agent 11.2 is correctly complete.** The implementation is aligned with the architecture we established: REST is only an adapter, while Phase 10 remains authoritative.

The next agent is therefore:

### Phase 11 — Agent 11.3
**WebSocket Runtime Gateway**

The important architectural goal for 11.3 is:

```text
                    ┌── REST API ────────────────┐
                    │                            │
Client ─────────────┼── WebSocket Gateway ───────┼──> shared/transport
                    │                            │
                    └────────────────────────────┘
                                                 │
                                                 ▼
                              Phase 10 Runtime Authorities
                              ├── RaceStateSnapshotEngine
                              ├── CacheManager
                              ├── TimelineService
                              ├── Event Bus
                              ├── LiveRuntime
                              ├── ReplayService
                              └── ModeController
```

### Agent 11.3 should implement

1. **WebSocket connection lifecycle**
2. **Subscribe / unsubscribe**
3. **Session-scoped subscriptions**
4. **Snapshot push**
5. **Telemetry push**
6. **Event push**
7. **Replay state/event push**
8. **Live state/event push**
9. **Ping/pong / connection health**
10. **Per-client bounded queues**
11. **Backpressure**
12. **Slow-client isolation**
13. **Disconnect cleanup**
14. **Transport envelope serialization**
15. **Subscription filtering**
16. **Connection/error protocol**
17. **WebSocket integration tests**
18. **No blocking of the Runtime**

And importantly, **11.3 should not implement authentication yet**. That remains a later transport/security agent.

The critical invariant should be:

> **A slow WebSocket client must never be capable of slowing, blocking, or corrupting the Phase 10 Runtime.**

Given 11.1 and 11.2 are now complete, **11.3 is the correct next step** before we start building the actual live telemetry/Unity-facing streaming pipeline.

## User

Please give commands for Agent 11.3	WebSocket Runtime Gateway	Real-time telemetry/state/event streaming ( 1 click copy and paste cursor friendly)

## Assistant

Yes. Agent **11.3** should build the real-time WebSocket boundary on top of the transport contracts from 11.1 and the REST/runtime façade from 11.2.

Copy/paste this **entire block** into Cursor Agent:

```text
You are the Principal Distributed Systems Architect for the RaceVision project.

============================================================
RACEVISION — AGENT 11.3
WEBSOCKET RUNTIME GATEWAY
Real-Time Telemetry / State / Event Streaming
============================================================

OBJECTIVE
---------

Implement Agent 11.3 — WebSocket Runtime Gateway.

Agent 11.1 is COMPLETE:
    Transport Architecture + REST/WebSocket contracts

Agent 11.2 is COMPLETE:
    REST Runtime API

Phase 10 is COMPLETE and ACCEPTED.

The objective of this agent is to implement the actual WebSocket transport
boundary for real-time Runtime data.

PRIMARY RESPONSIBILITIES:

    WebSocket connection lifecycle
    Subscribe / unsubscribe
    Session-scoped subscriptions
    Snapshot streaming
    Telemetry streaming
    Event streaming
    Replay state/event streaming
    Live state/event streaming
    Ping/pong
    Connection health
    Client isolation
    Bounded per-client queues
    Backpressure
    Slow-client protection
    Transport serialization
    WebSocket error protocol
    Disconnect cleanup
    WebSocket integration tests

============================================================
CRITICAL ARCHITECTURAL RULE
============================================================

The Phase 10 Runtime remains authoritative.

Architecture:

    WebSocket Client
          │
          ▼
    WebSocket Gateway
          │
          ▼
    shared/transport contracts
          │
          ▼
    Subscription Manager
          │
          ▼
    Runtime Event / Snapshot Sources
          │
          ▼
    Phase 10 Runtime

The WebSocket gateway is an ADAPTER.

It is NOT a second Runtime.

It must never replace:

    CacheManager
    TimelineService
    EventBus
    LiveRuntime
    ReplayService
    ModeController
    RaceStateSnapshotEngine
    LiveSessionAdapter
    ReplayApplicationController

============================================================
STEP 1 — INSPECT REPOSITORY FIRST
============================================================

Before changing anything inspect:

    shared/transport/
    backend/api/
    backend/runtime/
    backend/runtime/phase10/
    backend/runtime/snapshot/
    backend/runtime/live/
    backend/runtime/replay/
    backend/runtime/mode/
    shared/protocols/
    tests/
    docs/

Read:

    docs/Roadmap.md
    docs/Architecture.md
    docs/Streaming.md
    docs/Telemetry.md
    docs/Replay.md

Read the Agent 11.1 transport specification.

Read:

    shared/transport/envelope.py
    shared/transport/request.py
    shared/transport/response.py
    shared/transport/errors.py
    shared/transport/resources.py
    shared/transport/subscriptions.py
    shared/transport/payloads.py
    shared/transport/mapping.py
    shared/transport/serialization.py
    shared/transport/versioning.py
    shared/transport/health.py
    shared/transport/capabilities.py
    shared/transport/connection.py
    shared/transport/backpressure.py
    shared/transport/boundary.py

Inspect the exact contracts created by Agent 11.1.

Do NOT invent competing WebSocket contracts.

Inspect Agent 11.2's FastAPI application and dependency injection.

Determine whether FastAPI WebSocket support is already available.

If FastAPI is already the repository REST framework, use its native WebSocket
support unless repository architecture provides a better established mechanism.

Do not introduce another web framework.

============================================================
STEP 2 — WEBSOCKET BOUNDARY
============================================================

Implement the WebSocket endpoint according to Agent 11.1's resource contract.

If Agent 11.1 specifies:

    /api/v1/ws

use that exact path.

If it specifies another path, preserve it.

Do not change the transport contract.

Conceptual architecture:

    Client
      │
      ▼
    WebSocket endpoint
      │
      ▼
    ConnectionManager
      │
      ├── SubscriptionManager
      ├── ClientQueue
      ├── BackpressureController
      └── TransportSerializer
             │
             ▼
       Runtime authorities

============================================================
STEP 3 — NO SECOND RUNTIME
============================================================

The WebSocket gateway MUST NOT create:

    CacheManager
    TimelineService
    EventBusManager
    ReplayService
    LiveRuntime
    ModeController
    SessionManager

per WebSocket connection.

Runtime dependencies must be injected.

One connected client must not create another Runtime.

============================================================
STEP 4 — CONNECTION LIFECYCLE
============================================================

Implement:

    CONNECTING
    CONNECTED
    CLOSING
    CLOSED
    ERROR

or the exact connection states defined by Agent 11.1.

Connection lifecycle:

    accept
      ↓
    initialize context
      ↓
    authenticate boundary placeholder
      ↓
    receive messages
      ↓
    process subscriptions/commands
      ↓
    publish matching runtime messages
      ↓
    disconnect
      ↓
    cleanup subscriptions
      ↓
    close queues/tasks

Connection cleanup MUST always happen.

No orphaned:

    tasks
    queues
    subscriptions
    callbacks
    event handlers

============================================================
STEP 5 — CONNECTION CONTEXT
============================================================

Each WebSocket connection should have a small context containing only transport
state.

Potential fields:

    connection_id
    request_id
    connected_at
    protocol_version
    session_id
    subscriptions
    queue
    connection_state

Do not put Runtime state inside the connection context.

Do not duplicate:

    vehicle state
    race state
    replay cursor
    timeline
    cache

============================================================
STEP 6 — SUBSCRIPTION SYSTEM
============================================================

Use:

    shared/transport/subscriptions.py

Implement the subscription model established by Agent 11.1.

Support the transport-defined subscription categories.

At minimum, where contracts permit:

    SNAPSHOT
    TELEMETRY
    EVENT
    RUNTIME
    LIVE
    REPLAY

Do not invent unsupported categories.

Subscriptions must be explicit.

A client should not automatically receive high-volume telemetry merely because
it connected.

============================================================
STEP 7 — SUBSCRIBE MESSAGE
============================================================

Implement the Agent 11.1 subscribe message.

Conceptually:

    {
        "type": "subscribe",
        ...
    }

Validate:

    protocol version
    subscription type
    session_id
    filters
    requested frequency/options where supported

Return the transport-defined subscription acknowledgement.

Do not return internal Python objects.

============================================================
STEP 8 — UNSUBSCRIBE
============================================================

Implement the Agent 11.1 unsubscribe message.

On unsubscribe:

    remove subscription
    stop producing messages for it
    release subscription-specific resources

Do not close the entire WebSocket connection unless the protocol explicitly
requires it.

Unsubscribing one stream must not affect unrelated subscriptions.

============================================================
STEP 9 — SESSION ISOLATION
============================================================

This is CRITICAL.

If a client subscribes to:

    session_id = A

it must NEVER receive:

    session B

telemetry
events
snapshots
replay state
live state

Session filtering must occur before queue insertion.

Do not enqueue another session and attempt to filter later.

============================================================
STEP 10 — SNAPSHOT STREAMING
============================================================

Implement snapshot push using:

    RaceStateSnapshotEngine

or its existing public snapshot API.

Do NOT reconstruct snapshots inside the WebSocket layer.

Use:

    RaceStateSnapshot.to_serializable()

or the transport representation defined by Agent 11.1.

Snapshot messages must contain transport-safe state.

Possible payload:

    snapshot_id
    schema_version
    session_id
    mode
    runtime_ms
    timeline
    vehicles
    events
    quality
    consistency

Only include fields that actually exist.

============================================================
STEP 11 — TELEMETRY STREAMING
============================================================

Implement telemetry delivery through existing runtime/event authorities.

Do NOT make the WebSocket layer poll the database.

Do NOT make the WebSocket layer poll FastF1.

Do NOT create a telemetry ingestion loop inside the WebSocket gateway.

Correct architecture:

    LiveSessionAdapter / Replay Runtime
             │
             ▼
        Runtime/Event Bus
             │
             ▼
       WebSocket Gateway
             │
             ▼
          client queue

Where an existing event source is not yet directly exposed, create a thin
adapter/subscription hook rather than duplicating ingestion.

============================================================
STEP 12 — EVENT STREAMING
============================================================

Expose existing runtime/replay events through the transport layer.

Potential events include:

    lap completed
    sector completed
    overtake
    incident
    pit entry
    pit exit
    replay state changes
    mode changes
    synchronization events
    snapshot events

Only expose events that already exist.

DO NOT synthesize race events in the WebSocket gateway.

============================================================
STEP 13 — LIVE STREAMING
============================================================

When Runtime is LIVE:

    LiveSessionAdapter
        ↓
    existing runtime event path
        ↓
    WebSocket subscription
        ↓
    client queue

Do not create a second live telemetry ingestion path.

Do not connect directly to an F1 provider.

Do not invent production F1 telemetry.

The gateway consumes the Runtime.

============================================================
STEP 14 — REPLAY STREAMING
============================================================

When Runtime is REPLAY:

    Replay Runtime
        ↓
    existing event/state path
        ↓
    WebSocket subscription
        ↓
    client queue

Do not create a second ReplayClock.

Do not create another replay cursor.

Do not mutate replay state from telemetry delivery.

============================================================
STEP 15 — MODE CHANGES
============================================================

WebSocket clients may be subscribed while Runtime changes:

    LIVE → REPLAY
    REPLAY → LIVE

The gateway must remain coherent.

It must never report:

    LIVE and REPLAY simultaneously

for the same session.

Use existing:

    ModeController
    TimelineService
    Runtime status

as authorities.

Do not implement mode transitions in the WebSocket gateway.

============================================================
STEP 16 — TRANSPORT ENVELOPES
============================================================

Every outgoing message must use Agent 11.1 transport envelopes.

Use:

    TransportEnvelope
    TransportResponse
    transport payload DTOs
    serialization rules
    protocol versioning

Do not create:

    ad-hoc JSON
    raw dict responses
    framework-specific response schemas

unless the Agent 11.1 contract explicitly permits them.

============================================================
STEP 17 — MESSAGE TYPES
============================================================

Use:

    TransportMessageType

from Agent 11.1.

Expected conceptual categories include:

    SUBSCRIBE
    UNSUBSCRIBE
    PING
    COMMAND

and:

    SNAPSHOT
    TELEMETRY
    EVENT
    RESPONSE
    ERROR
    PONG

Only use values that actually exist.

If Agent 11.1 uses different names, preserve them.

============================================================
STEP 18 — PING/PONG
============================================================

Implement protocol ping/pong if defined.

Support:

    client → ping
    server → pong

or the exact protocol defined by Agent 11.1.

Ping must not access the Runtime unnecessarily.

Use it for connection health.

============================================================
STEP 19 — BACKPRESSURE
============================================================

This is one of the most important requirements.

A slow client MUST NOT block:

    Runtime
    EventBus
    LiveSessionAdapter
    ReplayService
    TimelineService
    SnapshotEngine

Each client must have a bounded outbound queue.

Use:

    shared/transport/backpressure.py

where appropriate.

Never use an unbounded queue.

============================================================
STEP 20 — PER-CLIENT QUEUE
============================================================

Each connection should have:

    bounded outbound queue

Conceptually:

    Runtime event
          │
          ▼
    Subscription filtering
          │
          ▼
    Client queue
          │
          ▼
    WebSocket sender

The Runtime should not wait for the socket.

If the queue is full, apply the policy established by Agent 11.1.

Possible policies:

    DROP_OLDEST
    DROP_NEWEST
    DISCONNECT
    COALESCE

Use only policies defined by the transport contract.

============================================================
STEP 21 — STREAM PRIORITIES
============================================================

If Agent 11.1 supports priority:

    control messages > errors > state/snapshot > telemetry

Do not allow high-volume telemetry to starve control traffic.

A client must still be able to:

    unsubscribe
    receive errors
    receive pong

when telemetry is busy.

============================================================
STEP 22 — TELEMETRY COALESCING
============================================================

If the transport contract supports coalescing:

    telemetry may be coalesced

but:

    events must not be silently dropped if the contract marks them reliable.

Do not coalesce:

    commands
    errors
    mode transitions
    critical replay state

unless explicitly permitted.

============================================================
STEP 23 — SLOW CLIENT PROTECTION
============================================================

Track per-client metrics:

    queued_messages
    dropped_messages
    bytes_queued
    send_latency
    queue_full_count
    subscription_count

If a client exceeds the configured threshold:

    apply the configured backpressure policy.

Never allow one client to consume unbounded memory.

============================================================
STEP 24 — DISCONNECT CLEANUP
============================================================

When a client disconnects:

    unsubscribe all streams
    detach event listeners
    cancel sender task
    cancel receiver task
    clear queue
    remove connection context
    release resources

Cleanup must execute even when the socket closes unexpectedly.

Test:

    normal close
    client disconnect
    network failure
    send failure
    malformed message
    server shutdown

============================================================
STEP 25 — ERROR HANDLING
============================================================

Malformed WebSocket messages must produce transport errors.

Use:

    TransportErrorCode

and Agent 11.1 error mapping.

Do not expose:

    traceback
    internal exception details
    file paths
    SQL statements
    credentials

For invalid subscription:

    return protocol error

For malformed JSON:

    return protocol error

For unsupported protocol version:

    return version error

For unavailable Runtime:

    return service-unavailable transport error

============================================================
STEP 26 — AUTHENTICATION BOUNDARY
============================================================

Authentication is NOT implemented by Agent 11.3.

Create/use the authentication dependency boundary established by Agent 11.1/11.2.

It may be:

    allow-all development implementation

but it must be replaceable.

Do not implement fake authentication.

Do not trust client-supplied:

    user_id
    role
    admin
    authenticated=true

============================================================
STEP 27 — CONNECTION LIMITS
============================================================

Add configuration for reasonable limits:

    max_connections
    max_subscriptions_per_connection
    outbound_queue_size
    max_message_size
    ping interval/timeout

Use the existing configuration system.

Do not invent production SLA values.

Defaults must be safe and bounded.

============================================================
STEP 28 — MESSAGE SIZE
============================================================

Reject oversized inbound messages.

Do not allocate arbitrary memory based on client input.

Use the WebSocket framework's maximum message size where available plus an
application-level validation boundary if appropriate.

============================================================
STEP 29 — SERIALIZATION PERFORMANCE
============================================================

Use the established transport serializer.

Avoid:

    repeated deep-copy operations
    unnecessary JSON encode/decode cycles
    ORM serialization
    repeated snapshot reconstruction

A snapshot should be generated once per required publication cycle and then
serialized for clients.

Do not mutate the shared snapshot payload after serialization.

============================================================
STEP 30 — SNAPSHOT FANOUT
============================================================

If multiple clients subscribe to the same snapshot stream:

    produce one authoritative snapshot payload

then fan it out through independent client queues.

Do not invoke:

    RaceStateSnapshotEngine.capture()

once per client unless the architecture explicitly requires it.

============================================================
STEP 31 — EVENT FANOUT
============================================================

Runtime event:

    one event
       ↓
    subscription matching
       ↓
    independent client queues

Never let a client callback directly block the EventBus.

The EventBus must not await slow socket writes.

============================================================
STEP 32 — EVENT BUS INTEGRATION
============================================================

Inspect the existing EventBus implementation.

Integrate using its established subscription mechanism.

Do not modify the EventBus architecture unnecessarily.

If the EventBus is synchronous:

    bridge events into non-blocking transport queues.

If it is asynchronous:

    register lightweight subscribers.

The WebSocket sender remains responsible for actual socket I/O.

============================================================
STEP 33 — RUNTIME THREAD/ASYNC SAFETY
============================================================

The REST/WebSocket layer must respect existing runtime concurrency rules.

Do not:

    mutate runtime from sender tasks
    call blocking runtime operations from the event loop
    hold runtime locks while performing socket writes

Especially:

    NEVER hold a Runtime lock while awaiting WebSocket.send_*()

============================================================
STEP 34 — COMMANDS
============================================================

Agent 11.3 is primarily streaming.

Do not implement the complete command API here.

If Agent 11.1 requires command messages for protocol operation, implement only
transport-level commands necessary for:

    subscribe
    unsubscribe
    ping

Do not expose replay control commands yet unless the existing contract
explicitly requires them.

Replay commands remain behind:

    ReplayCommandDispatcher

and later transport agents.

============================================================
STEP 35 — REST COMPATIBILITY
============================================================

Agent 11.2 must continue to work.

Do not break:

    /api/v1/runtime/status
    /api/v1/runtime/snapshot
    /api/v1/runtime/capabilities
    /api/v1/sessions
    /api/v1/sessions/{session_id}
    /api/v1/health

Run the Agent 11.2 API tests after implementation.

============================================================
STEP 36 — CONFIGURATION
============================================================

Use existing API settings or create a dedicated WebSocket settings object
only if architecturally justified.

Potential configuration:

    WS_ENABLED
    WS_PATH
    WS_MAX_CONNECTIONS
    WS_MAX_MESSAGE_SIZE
    WS_OUTBOUND_QUEUE_SIZE
    WS_MAX_SUBSCRIPTIONS
    WS_PING_INTERVAL
    WS_PING_TIMEOUT
    WS_BACKPRESSURE_POLICY

Do not hard-code operational settings.

Do not add unnecessary configuration.

============================================================
STEP 37 — FILE STRUCTURE
============================================================

Follow repository conventions.

A reasonable structure is:

    backend/api/
        websocket/
            __init__.py
            gateway.py
            connection.py
            manager.py
            subscriptions.py
            queue.py
            sender.py
            receiver.py
            errors.py
            dependencies.py
            settings.py
            metrics.py

Use a simpler or different structure if repository conventions dictate.

Do not duplicate transport models already under:

    shared/transport/

============================================================
STEP 38 — TEST STRUCTURE
============================================================

Create:

    tests/api/websocket/

or follow existing conventions.

Minimum tests:

    test_connection.py
    test_subscription.py
    test_unsubscription.py
    test_snapshot_stream.py
    test_telemetry_stream.py
    test_event_stream.py
    test_session_isolation.py
    test_backpressure.py
    test_disconnect.py
    test_errors.py
    test_ping_pong.py
    test_lifecycle.py
    test_serialization.py

Add architecture tests where useful.

============================================================
STEP 39 — CONNECTION TESTS
============================================================

Verify:

    connection accepted
    valid protocol established
    malformed handshake/message rejected
    ping/pong works
    clean close
    abnormal close
    cleanup executes

============================================================
STEP 40 — SUBSCRIPTION TESTS
============================================================

Verify:

    subscribe
    duplicate subscribe
    unsubscribe
    invalid subscription
    missing session_id
    session isolation
    multiple subscriptions
    subscription cleanup

A subscription must not receive another session's data.

============================================================
STEP 41 — SNAPSHOT TESTS
============================================================

Verify:

    snapshot subscription
    snapshot delivery
    correct session_id
    correct mode
    JSON serialization
    multiple clients
    one snapshot source fanout

Verify slow client does not block another client.

============================================================
STEP 42 — TELEMETRY TESTS
============================================================

Use synthetic/in-memory runtime telemetry.

Do NOT require:

    Internet
    production F1 feed
    FastF1 network access

Verify:

    telemetry received
    correct session
    correct driver
    source timestamp preserved
    transport serialization
    filtering
    backpressure behavior

============================================================
STEP 43 — EVENT TESTS
============================================================

Verify existing events can reach subscribed clients.

Test at minimum, where available:

    lap
    sector
    overtake
    incident
    pit
    replay event
    mode event

Do not invent events solely for testing.

============================================================
STEP 44 — BACKPRESSURE TESTS
============================================================

This is mandatory.

Create a deliberately slow client.

Generate enough outbound messages to fill its queue.

Verify:

    queue remains bounded
    configured policy activates
    Runtime continues
    other clients continue
    memory does not grow without bound

Specifically test:

    slow Client A
    healthy Client B

Client B must continue receiving data while Client A is congested.

============================================================
STEP 45 — NON-BLOCKING RUNTIME TEST
============================================================

Prove that the WebSocket sender does not hold a Runtime lock.

Test or inspect the architecture to guarantee:

    Runtime operation
        !=
    socket write

No runtime lock may remain held across:

    await websocket.send_text()
    await websocket.send_bytes()

or equivalent.

============================================================
STEP 46 — DISCONNECT TESTS
============================================================

Verify all resources are released after:

    client close
    server close
    send exception
    receive exception
    cancellation

Ensure no:

    orphan task
    listener
    queue
    subscription

remains.

============================================================
STEP 47 — MULTI-CLIENT TEST
============================================================

Create:

    Client A
    Client B
    Client C

with different subscriptions.

Verify:

    correct fanout
    session isolation
    filter isolation
    backpressure isolation
    disconnect isolation

One client's failure must not disconnect healthy clients.

============================================================
STEP 48 — MODE TRANSITION TEST
============================================================

Use existing ModeController.

Test:

    LIVE
      ↓
    REPLAY
      ↓
    LIVE

while clients remain connected.

Verify transport state follows the authoritative Runtime.

No client should see a fabricated mixed mode.

============================================================
STEP 49 — REPLAY TEST
============================================================

Use existing replay test fixtures.

Verify subscribed clients can receive appropriate:

    replay state
    replay events
    snapshots

during:

    play
    pause
    seek
    step

Only where the existing event/state contracts provide those messages.

Do not create another ReplayClock.

============================================================
STEP 50 — PERFORMANCE TESTING
============================================================

Do lightweight microbenchmarks only.

Measure where useful:

    message serialization
    queue insertion
    subscription matching
    fanout

Do not invent production SLAs.

Do not claim production F1 throughput.

Label any benchmarks:

    BASELINE_NOT_PRODUCTION_SLA

============================================================
STEP 51 — SECURITY
============================================================

No production authentication in this agent.

Still enforce:

    message size limit
    bounded queues
    bounded subscriptions
    session isolation
    safe errors
    no secrets in logs

Do not expose Runtime internals.

============================================================
STEP 52 — OBSERVABILITY
============================================================

Use existing structured logging.

Track:

    connection_count
    active_connections
    subscriptions
    messages_sent
    messages_dropped
    queue_full_events
    send_failures
    disconnects
    subscription_errors

Use existing metrics/logging conventions.

Do not create a separate observability framework.

============================================================
STEP 53 — DOCUMENTATION
============================================================

Create:

    docs/specifications/WebSocketRuntimeGatewaySpecification.md

Document:

    architecture
    endpoint
    protocol
    connection lifecycle
    message lifecycle
    subscribe
    unsubscribe
    snapshot
    telemetry
    events
    filtering
    session isolation
    backpressure
    queue policy
    slow clients
    errors
    ping/pong
    lifecycle
    observability
    security boundary
    configuration
    testing
    limitations

============================================================
STEP 54 — UPDATE DOCUMENTATION
============================================================

Update:

    docs/Roadmap.md
    docs/Architecture.md
    docs/Streaming.md
    docs/Telemetry.md
    docs/Replay.md
    docs/specifications/README.md
    backend/api/README.md

Mark:

    Agent 11.3 ✓

ONLY after all acceptance criteria pass.

Do not mark 11.4+ complete.

============================================================
STEP 55 — REGRESSION TESTING
============================================================

Run:

    Agent 11.3 tests

Then:

    Agent 11.2 API tests
    Agent 11.1 transport tests
    Phase 10 acceptance
    runtime tests
    interpolation tests

No regressions are acceptable.

Then run:

    Ruff
    mypy

Fix all introduced issues.

============================================================
STEP 56 — ACCEPTANCE CRITERIA
============================================================

Agent 11.3 is COMPLETE only when:

[ ] Repository inspected.
[ ] Agent 11.1 transport contracts reused.
[ ] Agent 11.2 FastAPI application remains functional.
[ ] WebSocket endpoint implemented.
[ ] Connection lifecycle implemented.
[ ] Subscribe implemented.
[ ] Unsubscribe implemented.
[ ] Session-scoped subscriptions implemented.
[ ] Snapshot streaming implemented.
[ ] Telemetry streaming implemented.
[ ] Event streaming implemented.
[ ] Live streaming consumes existing Runtime.
[ ] Replay streaming consumes existing Runtime.
[ ] Ping/pong implemented.
[ ] Transport envelopes reused.
[ ] Transport serialization reused.
[ ] Transport errors reused.
[ ] Per-client bounded queue implemented.
[ ] Backpressure policy implemented.
[ ] Slow clients cannot block Runtime.
[ ] Slow Client A cannot block Client B.
[ ] Session isolation tested.
[ ] Subscription isolation tested.
[ ] Disconnect cleanup implemented.
[ ] Orphan tasks prevented.
[ ] Message size bounded.
[ ] Subscription count bounded.
[ ] Connection count bounded.
[ ] Runtime locks never held during socket writes.
[ ] No direct database access.
[ ] No direct F1 provider access.
[ ] No second Runtime.
[ ] No second ReplayClock.
[ ] No second CacheManager.
[ ] No second TimelineService.
[ ] No authentication provider implemented.
[ ] Structured observability implemented.
[ ] Documentation created.
[ ] Documentation updated.
[ ] Roadmap updated.
[ ] WebSocket tests pass.
[ ] REST tests pass.
[ ] Transport tests pass.
[ ] Phase 10 acceptance passes.
[ ] Runtime regression passes.
[ ] Interpolation regression passes.
[ ] Ruff clean.
[ ] mypy clean.

============================================================
ARCHITECTURAL INVARIANTS
============================================================

These MUST remain true:

1. Phase 10 remains authoritative.

2. WebSocket is an adapter.

3. REST and WebSocket share transport contracts.

4. REST and WebSocket do not create separate Runtimes.

5. Runtime never waits for a WebSocket client.

6. EventBus never waits for socket I/O.

7. Socket writes never occur while holding Runtime locks.

8. Every client has bounded resources.

9. Session isolation is enforced before queue insertion.

10. Slow clients cannot affect healthy clients.

11. Telemetry ingestion remains outside the WebSocket gateway.

12. Replay control remains outside the WebSocket gateway.

13. Mode transitions remain owned by ModeController.

14. Snapshots remain owned by RaceStateSnapshotEngine.

15. Transport models remain under shared/transport.

16. ORM/database objects never cross the WebSocket boundary.

17. Internal exceptions never cross the WebSocket boundary.

18. No production F1 feed is invented.

19. No authentication is falsely claimed.

20. No WebSocket capability is advertised by REST until the gateway is actually
    wired and verified.

============================================================
EXPECTED RESULT
============================================================

After completion:

    REST
       │
       ├──────────────────────────────┐
       │                              │
       ▼                              ▼
    HTTP Clients                 WebSocket Clients
                                      │
                                      ▼
                              WebSocket Gateway
                                      │
                                      ▼
                              shared/transport
                                      │
                                      ▼
                             Phase 10 Runtime
                                      │
                    ┌─────────────────┼─────────────────┐
                    ▼                 ▼                 ▼
                  LIVE             REPLAY            SNAPSHOT
                    │                 │                 │
                    └─────────────────┴─────────────────┘
                                      │
                                      ▼
                               Client Queues

The Runtime remains the single source of truth.

============================================================
FINAL REPORT
============================================================

When complete, report:

1. Agent 11.3 status.
2. WebSocket framework.
3. Endpoint.
4. Connection architecture.
5. Subscription architecture.
6. Snapshot streaming.
7. Telemetry streaming.
8. Event streaming.
9. Live integration.
10. Replay integration.
11. Ping/pong.
12. Session isolation.
13. Backpressure strategy.
14. Queue configuration.
15. Slow-client behavior.
16. Disconnect cleanup.
17. Error handling.
18. Serialization.
19. Observability.
20. Security boundary.
21. Files created.
22. Files modified.
23. Tests.
24. Multi-client tests.
25. Backpressure tests.
26. Phase 10 regression.
27. Runtime/interpolation regression.
28. Ruff.
29. mypy.
30. Coverage.
31. Documentation.
32. Roadmap status.
33. Limitations.
34. Recommended Agent 11.4.

============================================================
START NOW
============================================================

First inspect the actual Agent 11.1 transport contracts and Agent 11.2 API.

Then implement Agent 11.3.

Do not invent competing contracts.

Do not implement authentication.

Do not implement Unity.

Do not implement OBS.

Do not implement prediction.

Do not implement AI.

Do not implement future phases.

Implement the WebSocket Runtime Gateway only.

Preserve the Phase 10 architecture.

START NOW.
```

## User

**Agent 11.3 is COMPLETE.** WebSocket Runtime Gateway is mounted at `WS /api/v1/ws` with bounded per-client queues and EventBus/snapshot fanout — Runtime stays authoritative.

### 1. Status

**COMPLETE**

### 2–3. Framework / endpoint

**FastAPI native WebSocket** on the Agent 11.2 app → **`/api/v1/ws`**

### 4–5. Connection / subscriptions

`WebSocketConnectionManager` + `ClientConnection` (transport state only). Subscribe/unsubscribe via Agent 11.1 `SubscriptionRequest` types; no auto-telemetry on connect.

### 6–10. Streaming

- **Snapshot:** shared `RaceStateSnapshotEngine` capture/latest → fanout
- **Telemetry/events:** EventBus → `GatewayBusBridge` → `offer_bus_event` (non-blocking)
- **Live/replay:** consume Runtime/EventBus paths only
- **Ping/pong:** implemented

### 11–16. Isolation / backpressure

Session filter **before** enqueue. Default `COALESCE_SNAPSHOT`; priorities control > event > snapshot > telemetry. Slow Client A cannot block Client B or Runtime. Disconnect clears tasks/subs/queues.

### 17–20

Transport envelopes/errors; structlog + `GatewayMetrics`; auth stub only (`auth_required` default false; true → reject).

### 21–22. Files

**Created:** `backend/api/websocket/*`, `tests/api/websocket/*`, `WebSocketRuntimeGatewaySpecification.md`
**Modified:** `create_app`, capabilities, `WebSocketSettings.auth_required`, docs/roadmap/README

### 23–30. Quality

| Gate                    | Result       |
| ----------------------- | ------------ |
| WS tests                | **36 PASS**  |
| API + transport         | **88 PASS**  |
| Phase 10 acceptance     | **PASS**     |
| Runtime + interpolation | **805 PASS** |
| Ruff                    | **clean**    |
| mypy (`backend/api`)    | **clean**    |
| WS coverage             | **\~80.5%**  |

### 31–32. Docs / Roadmap

Spec + docs updated; **11.3 ✓**; 11.4+ open.

### 33. Limitations

No WS command channel for replay/live; no production auth; replay may need EventBus rebinding for richer replay lifecycle events; telemetry may coalesce under pressure.

### 34. Recommended Agent 11.4

**Auth wiring + replay/live command REST** (and optional WS command passthrough through existing dispatchers), without claiming false security before a real provider exists.

## Assistant

Excellent. **Agent 11.3 is now locked as COMPLETE.**

The Phase 11 transport stack is now:

```text
                    RaceVision Runtime
                           │
              ┌────────────┴────────────┐
              │                         │
          REST API                  WebSocket
          Agent 11.2                Agent 11.3
              │                         │
              └────────────┬────────────┘
                           │
                   shared/transport
                    Agent 11.1
                           │
                           ▼
                  Phase 10 Runtime
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
       LIVE              REPLAY            SNAPSHOT
        │                  │                  │
        └──────────────────┴──────────────────┘
```

### Current Phase 11 status

| Agent | Component | Status |
|---|---|---|
| **11.1** | Transport Architecture | ✅ COMPLETE |
| **11.2** | REST Runtime API | ✅ COMPLETE |
| **11.3** | WebSocket Runtime Gateway | ✅ COMPLETE |
| **11.4** | Runtime Command/API Control | ⬜ NEXT |
| **11.5+** | Remaining transport/security work | ⬜ |

And importantly:

- **Phase 10:** ✅ ACCEPTED
- **805 runtime + interpolation tests:** ✅ PASS
- **REST + transport:** ✅ PASS
- **WebSocket:** 36 tests ✅
- **Ruff:** ✅
- **mypy:** ✅
- Runtime remains the **single source of truth**
- WebSocket does **not** create a second runtime
- Backpressure is isolated per client
- Session filtering happens **before enqueue**

### Recommended next step

I would make **Agent 11.4** the command/control layer:

**Agent 11.4 — Runtime Command Gateway**

Expose the already-existing controllers through transport:

```text
REST / WebSocket
       │
       ▼
Transport Command
       │
       ▼
Command Mapping
       │
 ┌─────┼──────────────────────┐
 ▼     ▼                      ▼
Replay ModeController      Live
Controller                 Controller
       │
       ▼
Existing Phase 10 Runtime
```

This would give RaceVision actual remote control over:

- Replay play/pause/resume/stop/reset
- Seek
- Step forward/backward
- Fast-forward / rewind
- Jump to lap/event/bookmark
- LIVE start/stop/reconnect
- LIVE ↔ REPLAY mode switching
- Runtime status/capabilities
- Snapshot requests

**without putting any business logic into REST or WebSocket.**

After that, we can continue building the transport layer before moving into **Phase 12 Unity Integration & 3D Scene Runtime**.

## User

Please give commands for Agent 11.4	Command Transport Layer	REST/WS → existing Controllers/Commands ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. Agent **11.4** should be the thin command-control layer that connects the already-established REST/WebSocket transport to the existing Phase 10 controllers. It should **not** introduce new runtime logic.

Copy/paste this entire block into Cursor Agent:

```text
You are the Principal Distributed Systems Architect for the RaceVision project.

============================================================
RACEVISION — AGENT 11.4
COMMAND TRANSPORT LAYER
REST / WebSocket → EXISTING CONTROLLERS / COMMANDS
============================================================

OBJECTIVE
---------

Implement Agent 11.4 — Command Transport Layer.

The purpose of this agent is to expose the existing Runtime command/control
capabilities through the transport layer created by Agents 11.1–11.3.

This agent MUST be a THIN TRANSPORT ADAPTER.

It must translate:

    REST / WebSocket transport commands
                    ↓
              existing commands
                    ↓
              existing dispatchers
                    ↓
              existing controllers
                    ↓
              Phase 10 Runtime

DO NOT create a second command system.

DO NOT put business logic in REST.

DO NOT put business logic in WebSocket.

DO NOT modify Runtime ownership.

============================================================
CURRENT ARCHITECTURE
============================================================

Phase 10 is COMPLETE and ACCEPTED.

Agent 11.1:
    Transport Architecture
    shared/transport/

Agent 11.2:
    REST Runtime API
    backend/api/

Agent 11.3:
    WebSocket Runtime Gateway
    backend/api/websocket/

Agent 11.4:
    Command Transport Layer
    REST/WS → existing Controllers/Commands

Current authoritative Runtime:

    CacheManager
    TimelineService
    EventBus
    LiveRuntime
    ReplayService
    ReplayApplicationController
    LiveSessionAdapter
    ModeController
    RaceStateSnapshotEngine

The transport layer must remain outside this authority boundary.

============================================================
CRITICAL ARCHITECTURAL RULE
============================================================

The correct architecture is:

    REST Client
         │
         ▼
    REST Command Route
         │
         ├───────────────┐
         │               │
         ▼               ▼
    Transport       Command Mapping
    Validation            │
                         ▼
                  Existing Dispatcher
                         │
              ┌──────────┼───────────┐
              ▼          ▼           ▼
          Replay       Live        Mode
        Controller   Controller   Controller
              │          │           │
              └──────────┴───────────┘
                         │
                         ▼
                    Phase 10
                     Runtime

and:

    WebSocket Client
         │
         ▼
    WebSocket Gateway
         │
         ▼
    Command Transport
         │
         ▼
    Existing Dispatchers / Controllers

The Command Transport Layer MUST NOT become a new Runtime authority.

============================================================
STEP 1 — INSPECT THE REPOSITORY
============================================================

Before making changes inspect the actual implementation.

Read:

    docs/Roadmap.md
    docs/Architecture.md
    docs/Streaming.md
    docs/Telemetry.md
    docs/Replay.md

Inspect:

    shared/transport/
    backend/api/
    backend/api/websocket/
    backend/runtime/
    backend/runtime/replay/
    backend/runtime/live/
    backend/runtime/mode/
    shared/protocols/commands/
    shared/protocols/events/
    tests/

Inspect Agent 11.1:

    shared/transport/mapping.py
    shared/transport/request.py
    shared/transport/response.py
    shared/transport/errors.py
    shared/transport/payloads.py
    shared/transport/serialization.py
    shared/transport/resources.py
    shared/transport/capabilities.py

Inspect Agent 11.2:

    backend/api/app.py
    backend/api/facade.py
    backend/api/services/
    backend/api/routes/

Inspect Agent 11.3:

    backend/api/websocket/

Inspect existing command/control implementations created during Phase 10:

    ReplayCommandDispatcher
    ReplayApplicationController
    ReplayNavigationService
    LiveSessionDispatcher / controller
    ModeCommandDispatcher
    ModeController
    RaceStateSnapshotEngine
    Phase10 command/controller infrastructure

DO NOT assume names if the repository uses different exact names.

Use the actual existing implementations.

============================================================
STEP 2 — INVENTORY EXISTING COMMANDS
============================================================

Before implementing transport, produce an internal inventory of existing
commands and dispatchers.

At minimum inspect commands relating to:

REPLAY:

    load
    load historical
    play
    pause
    resume
    stop
    reset
    seek
    step forward
    step backward
    fast-forward
    rewind
    jump to start
    jump to end
    jump to lap
    jump to sector
    jump to event
    jump to bookmark
    next event
    previous event
    next bookmark
    previous bookmark

LIVE:

    start
    stop
    reconnect
    status

MODE:

    switch LIVE
    switch REPLAY

SNAPSHOT:

    capture/get snapshot

VALIDATION:

    validate replay

BOOKMARK:

    create
    update
    delete
    jump

Use ONLY commands/controllers that actually exist.

Do not create duplicate command implementations.

============================================================
STEP 3 — COMMAND TRANSPORT CONTRACT
============================================================

Use Agent 11.1 transport contracts.

Do not create an unrelated command envelope.

If Agent 11.1 already defines:

    TransportRequest
    TransportResponse
    TransportEnvelope
    TransportErrorCode
    TransportMessageType
    command payload DTOs

reuse them.

If a small missing command payload is genuinely required, extend the existing
transport contract consistently.

Do not create:

    RawCommand
    GenericCommand2
    RestCommand
    WebSocketCommand

when an existing transport contract can represent the operation.

============================================================
STEP 4 — COMMAND MAPPING
============================================================

The primary responsibility of Agent 11.4 is:

    transport command
          ↓
    command mapping
          ↓
    existing dispatcher/controller

Example:

    {
        "type": "command",
        "command": "replay.play",
        "payload": {...}
    }

must become the existing Replay command expected by:

    ReplayCommandDispatcher

or the exact existing dispatcher.

Do not duplicate:

    validation
    replay state machine
    seek logic
    mode transition logic
    synchronization
    cache management

Those already belong to Phase 10.

============================================================
STEP 5 — REST COMMAND API
============================================================

Expose commands through REST.

Follow the REST boundary defined by Agent 11.1.

Use:

    /api/v1/...

according to existing REST_RESOURCES.

Do NOT invent a completely different URL hierarchy.

If Agent 11.1 specifies resource-oriented command endpoints, follow that.

Possible conceptual routes include:

    POST /api/v1/replay/commands
    POST /api/v1/live/commands
    POST /api/v1/mode/commands

or the exact contract already defined.

If a command-resource structure already exists, use it.

Do not create one REST route per internal method unless the transport contract
requires it.

============================================================
STEP 6 — REST COMMAND VALIDATION
============================================================

REST must validate:

    request schema
    protocol version
    command type
    required fields
    session_id
    payload structure

Then forward to the existing dispatcher.

REST must NOT validate Runtime business rules such as:

    "can replay seek while playing"

That belongs to:

    ReplayApplicationController
    ReplayService
    existing Runtime logic

Transport validation answers:

    "Is this a valid command message?"

Runtime validation answers:

    "Can the command execute now?"

Keep those responsibilities separate.

============================================================
STEP 7 — WEBSOCKET COMMAND CHANNEL
============================================================

Extend Agent 11.3 WebSocket gateway to support command messages.

The WebSocket command path must be:

    WebSocket
       ↓
    transport envelope
       ↓
    CommandTransportService
       ↓
    existing dispatcher/controller

Do NOT put controller calls directly into:

    websocket.py
    gateway.py
    sender.py
    receiver.py

Use a dedicated command transport service/adapter.

============================================================
STEP 8 — WEBSOCKET COMMAND RESPONSE
============================================================

Every command should produce a transport-safe response.

Conceptually:

    command request
          ↓
    dispatcher
          ↓
    controller
          ↓
    command result
          ↓
    TransportResponse
          ↓
    WebSocket client

Use existing response/result mapping.

Do not return internal controller objects.

Do not serialize:

    Runtime objects
    SQLAlchemy models
    internal exceptions
    Python dataclasses without transport mapping

============================================================
STEP 9 — REQUEST CORRELATION
============================================================

Every command should preserve:

    request_id

and, where applicable:

    correlation_id

The response must allow the client to match:

    request → response

Do not generate a new unrelated ID after the command reaches the dispatcher
unless the transport contract explicitly requires it.

============================================================
STEP 10 — SESSION ID
============================================================

Commands operating on a session MUST respect:

    session_id

where required by Agent 11.1.

Session isolation is mandatory.

A client must not be able to issue:

    session A command

and accidentally operate on:

    session B

Do not rely solely on a client-provided arbitrary object reference.

Use the existing session/controller architecture.

============================================================
STEP 11 — REPLAY COMMANDS
============================================================

Expose existing replay control through transport.

Where implemented, support:

    load
    load_historical
    play
    pause
    resume
    stop
    reset
    seek
    step_forward
    step_backward
    fast_forward
    rewind
    jump_to_start
    jump_to_end
    jump_to_lap
    jump_to_sector
    jump_to_event
    jump_to_bookmark
    next_event
    previous_event
    next_bookmark
    previous_bookmark

Only expose commands actually supported by the current controller.

Every operation MUST route through:

    ReplayCommandDispatcher
    ReplayApplicationController
    ReplayNavigationService

as appropriate.

Do not call:

    ReplayService

directly from the REST route unless the existing architecture explicitly uses
it as the public controller boundary.

============================================================
STEP 12 — LIVE COMMANDS
============================================================

Expose existing Live commands:

    start
    stop
    reconnect
    status

Use:

    LiveSessionDispatcher
    LiveSessionAdapter
    existing Live controller

or the actual repository equivalents.

Do not create another Live ingestion path.

Do not connect directly to an F1 provider.

============================================================
STEP 13 — MODE COMMANDS
============================================================

Expose existing mode operations.

At minimum, where supported:

    switch to LIVE
    switch to REPLAY

Route through:

    ModeCommandDispatcher
    ModeController

Do not implement transition logic in the transport layer.

Do not silently reconnect LIVE.

Do not bypass rollback/coherence logic.

============================================================
STEP 14 — SNAPSHOT COMMAND
============================================================

If transport contract supports an explicit snapshot command:

    GET / POST according to contract

must call:

    RaceStateSnapshotEngine

or its existing public façade.

Do not build snapshots manually.

Return:

    RaceStateSnapshot
        ↓
    transport-safe serialization

============================================================
STEP 15 — VALIDATION COMMAND
============================================================

If Agent 11.1 transport contract includes replay validation:

    ValidateReplay

must route through the existing validation controller.

Do not duplicate validation.

Do not mutate replay state in the transport layer.

============================================================
STEP 16 — BOOKMARK COMMANDS
============================================================

If Agent 10.11 exposes bookmark control through its controller, expose:

    CreateBookmark
    UpdateBookmark
    DeleteBookmark
    JumpToBookmark

through the existing controller/dispatcher.

Do not manipulate BookmarkStore directly from REST/WebSocket.

============================================================
STEP 17 — COMMAND RESULT MAPPING
============================================================

Create a dedicated result mapper if needed:

    command result
          ↓
    transport response

Map:

    success
    validation failure
    invalid state
    not loaded
    invalid seek
    session unavailable
    service unavailable
    conflict
    internal error

into:

    TransportErrorCode

Use the existing error mapping.

Never expose raw exceptions.

============================================================
STEP 18 — HTTP STATUS MAPPING
============================================================

Use Agent 11.1 HTTP semantics.

Conceptually:

    successful command → 200/202 according to contract

    invalid request → 400
    unauthorized → 401
    forbidden → 403
    not found → 404
    invalid state/conflict → 409
    unavailable → 503
    internal failure → 500

Do NOT blindly use these values if Agent 11.1 specifies different mappings.

Use the established transport contract.

============================================================
STEP 19 — ASYNCHRONOUS COMMANDS
============================================================

Determine whether existing controllers are:

    synchronous
    asynchronous

Preserve their semantics.

Do not introduce background jobs merely because the transport is async.

If an operation is already cooperative/synchronous, await only as required.

If an operation is asynchronous, preserve it.

Never block the WebSocket event loop with a long-running synchronous operation
without following the repository's established async strategy.

============================================================
STEP 20 — COMMAND TIMEOUTS
============================================================

Do not invent arbitrary Runtime timeouts.

If Agent 11.1 defines transport timeout configuration, use it.

A transport timeout MUST NOT leave the Runtime command in an unknown or
incorrect state.

If the underlying command continues after the transport response times out,
the response must not falsely claim failure if the contract cannot establish
that.

Prefer the existing command lifecycle semantics.

============================================================
STEP 21 — IDEMPOTENCY
============================================================

Inspect existing command semantics.

Do not add fake idempotency.

Where commands are explicitly idempotent:

    stop
    reset
    same-mode transitions

preserve existing semantics.

For non-idempotent operations such as:

    step
    seek
    bookmark creation

do not silently retry.

============================================================
STEP 22 — CONCURRENCY
============================================================

The transport layer must respect existing controller concurrency.

Especially:

    ReplayCommandDispatcher
    ModeCommandDispatcher
    LiveSessionDispatcher

Do not create additional locks around the Runtime unless required.

Do not bypass existing:

    RLock
    asyncio.Lock
    lifecycle synchronization

Do not allow REST and WebSocket to mutate the same Runtime through parallel
unsafe paths.

The existing controllers remain responsible for command serialization.

============================================================
STEP 23 — COMMAND CAPABILITIES
============================================================

Update transport capabilities only for commands that are actually wired.

For example:

    replay_commands = true
    live_commands = true
    mode_commands = true

ONLY if implementation and tests prove them.

Do not advertise commands that are merely defined but unwired.

============================================================
STEP 24 — WEBSOCKET COMMAND RESPONSE VS EVENT
============================================================

Keep these separate:

    CommandResponse
        = response to the client request

    RuntimeEvent
        = asynchronous state/event publication

Example:

    Client → replay.pause
    Gateway → CommandResponse(success)
    Runtime → ReplayPaused event
    Gateway → Event(subscription)

Do not use an event as a substitute for the command response.

Do not use a command response as a substitute for a Runtime event.

============================================================
STEP 25 — COMMAND ACKNOWLEDGEMENT
============================================================

Where the protocol supports acknowledgement:

    command accepted
    command completed

must remain semantically distinct if the existing controller is asynchronous.

Do not report:

    "completed"

when the command has only been accepted.

Use existing command result semantics.

============================================================
STEP 26 — SECURITY BOUNDARY
============================================================

Agent 11.3 currently has:

    auth stub
    auth_required default false

Do NOT claim production authentication.

Agent 11.4 must preserve the authentication boundary.

If:

    auth_required = true

and no real provider exists:

    reject commands safely.

Do not implement fake roles.

Do not trust:

    admin=true
    authenticated=true
    user_role=admin

from clients.

============================================================
STEP 27 — COMMAND AUTHORIZATION BOUNDARY
============================================================

If Agent 11.1 defines authorization hooks, wire them.

Otherwise:

    create an injectable authorization dependency

but keep development mode explicitly permissive only when configured.

Do not hard-code:

    "all users can control everything"

as production policy.

============================================================
STEP 28 — COMMAND PAYLOAD LIMITS
============================================================

Reuse WebSocket/REST transport limits.

Validate:

    maximum request size
    maximum payload depth if configured
    maximum command parameters
    allowed enum values

Do not allow arbitrary nested JSON to reach Runtime controllers.

============================================================
STEP 29 — OBSERVABILITY
============================================================

Record structured command metrics:

    commands_received
    commands_succeeded
    commands_failed
    commands_rejected
    command_duration
    command_errors
    command_timeouts

Include:

    request_id
    correlation_id
    command
    session_id where safe
    transport = rest/ws

Do not log:

    credentials
    secrets
    raw authentication tokens
    huge telemetry payloads

============================================================
STEP 30 — NO BUSINESS LOGIC
============================================================

The following are forbidden inside the Command Transport Layer:

    replay state transitions
    replay seek calculations
    replay synchronization
    mode transition algorithms
    live ingestion
    telemetry interpolation
    snapshot construction
    cache mutation
    event detection
    bookmark indexing
    database queries

All of these already belong to existing runtime components.

============================================================
STEP 31 — RECOMMENDED STRUCTURE
============================================================

Follow repository conventions.

A reasonable structure:

    backend/api/commands/
        __init__.py
        service.py
        mapper.py
        dispatcher.py
        result_mapper.py
        errors.py
        dependencies.py
        settings.py

Potential routes:

    backend/api/routes/commands.py

WebSocket integration:

    backend/api/websocket/command_handler.py

Do NOT duplicate models already under:

    shared/transport/

============================================================
STEP 32 — REST ROUTES
============================================================

Add command routes consistent with Agent 11.1.

Potential conceptual resource:

    POST /api/v1/commands

or resource-specific routes already defined.

Use the existing REST_RESOURCES.

If Agent 11.1 has already specified:

    replay commands
    live commands
    mode commands

follow that exact design.

Do NOT introduce a competing API.

============================================================
STEP 33 — WEBSOCKET HANDLER
============================================================

Modify Agent 11.3 minimally.

The gateway should delegate command messages:

    command message
          ↓
    CommandTransportService
          ↓
    existing dispatcher

Do not make the gateway aware of:

    ReplayService internals
    LiveSessionAdapter internals
    ModeController internals

============================================================
STEP 34 — TESTS
============================================================

Create:

    tests/api/commands/

or follow repository convention.

At minimum:

    test_command_mapping.py
    test_command_validation.py
    test_replay_commands.py
    test_live_commands.py
    test_mode_commands.py
    test_snapshot_commands.py
    test_bookmark_commands.py
    test_validation_commands.py
    test_rest_commands.py
    test_websocket_commands.py
    test_errors.py
    test_session_isolation.py
    test_capabilities.py
    test_auth_boundary.py

Only create tests for commands that actually exist.

============================================================
STEP 35 — REPLAY TESTS
============================================================

Test transport → existing controller.

Examples:

    POST replay.pause
        ↓
    ReplayCommandDispatcher
        ↓
    ReplayApplicationController
        ↓
    ReplayService

Verify the transport did NOT mutate ReplayService directly.

Test:

    play
    pause
    resume
    stop
    reset
    seek
    step
    fast-forward
    rewind
    jump-to-lap
    jump-to-event
    jump-to-bookmark

where implemented.

============================================================
STEP 36 — LIVE TESTS
============================================================

Test:

    start
    stop
    reconnect

through the existing Live controller.

Use:

    InMemoryLiveProvider

or existing test doubles.

Do not use a production F1 feed.

============================================================
STEP 37 — MODE TESTS
============================================================

Test:

    LIVE → REPLAY
    REPLAY → LIVE

through:

    ModeCommandDispatcher
    ModeController

Verify rollback/coherence remains controlled by the existing ModeController.

============================================================
STEP 38 — SESSION ISOLATION TEST
============================================================

Create multiple sessions.

Issue:

    session A command

Verify:

    session B remains unchanged.

This test is mandatory.

============================================================
STEP 39 — REST/WS PARITY
============================================================

For representative commands verify:

    REST command
    WebSocket command

reach the same existing dispatcher/controller behavior.

Do not duplicate business logic between transports.

============================================================
STEP 40 — ERROR TESTS
============================================================

Test:

    malformed command
    unknown command
    missing payload
    invalid payload
    invalid session
    invalid replay state
    invalid seek
    replay not loaded
    unavailable Runtime
    auth required
    authorization failure

Verify transport-safe errors.

No traceback leakage.

============================================================
STEP 41 — CONCURRENCY TEST
============================================================

Test:

    REST command
    WebSocket command

arriving concurrently for the same Runtime/session.

Verify existing controller serialization prevents inconsistent state.

Do not add a second Runtime lock.

============================================================
STEP 42 — COMMAND CORRELATION TEST
============================================================

Verify:

    request_id

is preserved from:

    REST/WS request

through:

    command response

and logs/metrics where applicable.

============================================================
STEP 43 — COMMAND EVENT TEST
============================================================

Where existing Runtime events exist:

    command
       ↓
    controller
       ↓
    Runtime state change
       ↓
    EventBus
       ↓
    WebSocket event subscription

Verify both:

    command response

and:

    asynchronous Runtime event

remain separate.

============================================================
STEP 44 — BACKPRESSURE INTERACTION
============================================================

Agent 11.3 already protects outbound streaming.

Ensure command responses cannot be silently lost behind a telemetry flood.

Control responses must have appropriate priority according to the existing
transport backpressure policy.

A slow telemetry subscriber must not prevent:

    command response
    error
    pong

from being delivered.

============================================================
STEP 45 — REST REGRESSION
============================================================

Run Agent 11.2 tests.

Verify:

    GET /api/v1/runtime/status
    GET /api/v1/runtime/snapshot
    GET /api/v1/runtime/capabilities
    GET /api/v1/sessions
    GET /api/v1/sessions/{id}
    GET /api/v1/health

continue to work.

============================================================
STEP 46 — WEBSOCKET REGRESSION
============================================================

Run all Agent 11.3 tests.

Verify:

    connection
    subscribe
    unsubscribe
    snapshot
    telemetry
    events
    ping/pong
    backpressure
    disconnect

remain green.

============================================================
STEP 47 — PHASE 10 REGRESSION
============================================================

Run:

    Phase 10 acceptance
    runtime tests
    interpolation tests
    replay tests
    live tests
    mode tests
    snapshot tests

No Phase 10 regression is acceptable.

============================================================
STEP 48 — QUALITY
============================================================

Run:

    Ruff
    mypy

Fix all introduced errors.

Do not suppress warnings with broad:

    # noqa
    type: ignore

unless there is a documented architectural reason.

============================================================
STEP 49 — DOCUMENTATION
============================================================

Create:

    docs/specifications/CommandTransportLayerSpecification.md

Document:

    architecture
    REST commands
    WebSocket commands
    command envelope
    mapping
    dispatchers
    response lifecycle
    errors
    session isolation
    authentication boundary
    authorization boundary
    idempotency
    concurrency
    observability
    capabilities
    security
    limitations

Update:

    docs/Roadmap.md
    docs/Architecture.md
    docs/Streaming.md
    docs/Telemetry.md
    docs/Replay.md
    docs/specifications/README.md
    backend/api/README.md

Mark:

    Agent 11.4 ✓

ONLY after all acceptance criteria pass.

============================================================
STEP 50 — ARCHITECTURAL INVARIANTS
============================================================

These MUST remain true:

1. Phase 10 remains authoritative.

2. Agent 11.4 contains no Runtime business logic.

3. REST and WebSocket use the same command mapping.

4. REST and WebSocket use the same existing dispatchers/controllers.

5. No duplicate ReplayService.

6. No duplicate ReplayClock.

7. No duplicate LiveRuntime.

8. No duplicate LiveSessionAdapter.

9. No duplicate ModeController.

10. No duplicate CacheManager.

11. No duplicate TimelineService.

12. Snapshot creation remains owned by RaceStateSnapshotEngine.

13. Replay navigation remains owned by ReplayNavigationService.

14. Replay synchronization remains owned by ReplaySynchronizer.

15. Mode transitions remain owned by ModeController.

16. Live lifecycle remains owned by LiveSessionAdapter/controller.

17. Command responses are separate from Runtime events.

18. Transport errors never expose internal exceptions.

19. Session isolation is enforced.

20. Authentication is not falsely claimed.

21. WebSocket backpressure remains intact.

22. Runtime locks are never held during socket I/O.

23. No database access from command routes.

24. No direct F1 provider access from command routes.

25. No production F1 feed is invented.

26. Existing Phase 10 behavior remains unchanged.

============================================================
STEP 51 — ACCEPTANCE CRITERIA
============================================================

Agent 11.4 is COMPLETE only when:

[ ] Repository inspected.
[ ] Agent 11.1 contracts reused.
[ ] Agent 11.2 REST remains functional.
[ ] Agent 11.3 WebSocket remains functional.
[ ] Command transport service implemented.
[ ] REST command transport implemented.
[ ] WebSocket command transport implemented.
[ ] Existing Replay dispatcher reused.
[ ] Existing Live dispatcher reused.
[ ] Existing Mode dispatcher reused.
[ ] Existing Snapshot authority reused.
[ ] Existing Bookmark controller reused where available.
[ ] Existing Validation controller reused where available.
[ ] No duplicate Runtime created.
[ ] No business logic added to transport.
[ ] Request correlation implemented.
[ ] Session isolation tested.
[ ] Command result mapping implemented.
[ ] Transport error mapping implemented.
[ ] HTTP status mapping correct.
[ ] WebSocket response mapping correct.
[ ] Command/event separation implemented.
[ ] Capabilities updated only for actually wired commands.
[ ] Authentication boundary preserved.
[ ] Authorization boundary preserved.
[ ] Backpressure does not starve command responses.
[ ] REST/WS parity tested.
[ ] Replay command tests pass.
[ ] Live command tests pass.
[ ] Mode command tests pass.
[ ] Session isolation tests pass.
[ ] Error tests pass.
[ ] Concurrency tests pass.
[ ] REST regression passes.
[ ] WebSocket regression passes.
[ ] Transport regression passes.
[ ] Phase 10 acceptance passes.
[ ] Runtime/interpolation regression passes.
[ ] Ruff clean.
[ ] mypy clean.
[ ] Documentation complete.
[ ] Roadmap updated.

============================================================
EXPECTED FINAL ARCHITECTURE
============================================================

                         CLIENTS
                    ┌───────────────┐
                    │               │
                 REST              WS
                    │               │
                    └───────┬───────┘
                            │
                            ▼
                  shared/transport
                            │
                            ▼
                 CommandTransportService
                            │
                            ▼
                    Command Mapping
                            │
             ┌──────────────┼───────────────┐
             ▼              ▼               ▼
       ReplayDispatcher  LiveDispatcher  ModeDispatcher
             │              │               │
             ▼              ▼               ▼
       ReplayController LiveController ModeController
             │              │               │
             └──────────────┼───────────────┘
                            ▼
                     PHASE 10 RUNTIME
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
            Replay         Live        Snapshot
              │             │             │
              └─────────────┼─────────────┘
                            ▼
                         EventBus
                            │
                            ▼
                      WebSocket fanout

There must be ONE authoritative Runtime.

============================================================
FINAL REPORT FORMAT
============================================================

When complete, report:

1. Agent 11.4 status.
2. Command transport architecture.
3. REST command endpoint(s).
4. WebSocket command protocol.
5. Commands exposed.
6. Existing dispatchers reused.
7. Existing controllers reused.
8. Request/correlation handling.
9. Session isolation.
10. Result mapping.
11. Error mapping.
12. HTTP status mapping.
13. WebSocket response behavior.
14. Command/event separation.
15. Capabilities changes.
16. Authentication boundary.
17. Authorization boundary.
18. Files created.
19. Files modified.
20. Tests created.
21. Test results.
22. REST regression.
23. WebSocket regression.
24. Transport regression.
25. Phase 10 acceptance.
26. Runtime/interpolation regression.
27. Ruff.
28. mypy.
29. Coverage.
30. Documentation.
31. Roadmap status.
32. Limitations.
33. Recommended Agent 11.5.

============================================================
START NOW
============================================================

First inspect the actual existing command contracts, dispatchers and
controllers.

Then implement Agent 11.4.

Do not invent competing controllers.

Do not create a second Runtime.

Do not put business logic in REST or WebSocket.

Do not implement Unity.

Do not implement OBS.

Do not implement prediction.

Do not implement AI.

Implement the Command Transport Layer only.

Preserve the Phase 10 architecture.

START NOW.
```

## User

## Agent 11.4 — COMPLETE ✓

Thin command transport only: REST/WS → existing Phase 10 dispatchers/controllers. No second Runtime.

---

### 1. Status

**COMPLETE and ACCEPTED** against the listed gates.

### 2. Architecture

`Client → REST|WS → shared/transport → CommandTransportService → builders → Replay|Live|Mode dispatchers → controllers → Phase 10 Runtime`. One mapping shared by both transports.

### 3. REST endpoints

Agent 11.1 `REST_RESOURCES` under `/api/v1`: replay load/play/pause/resume/stop/reset/seek/step/navigation/status/events/bookmarks; live start/stop/reconnect/status; mode GET/POST.

### 4. WebSocket protocol

`message_type: "command"` with `operation` (+ optional `request_id` / `session_id` / payload) → `CommandTransportService` → `response` envelope at **CONTROL** priority.

### 5. Commands exposed

Replay control/navigation/bookmarks/validate; live start/stop/reconnect/status; mode switch LIVE|REPLAY + status; snapshot via service when engine is wired.

### 6. Dispatchers reused

`ReplayCommandDispatcher`, `LiveSessionDispatcher`, `ModeCommandDispatcher`.

### 7. Controllers reused

`ReplayApplicationController`, `LiveSessionController`/`LiveSessionAdapter`, `ModeController`, `RaceStateSnapshotEngine`.

### 8. Correlation

`request_id` / `correlation_id` preserved from middleware or WS payload into `TransportResponse`.

### 9. Session isolation

Scoped commands carry `session_id`; replay status returns `CONFLICT` on mismatch (tested).

### 10–12. Result / error / HTTP mapping

`result_mapper.py` → `TransportErrorCode`; HTTP via `ERROR_TO_HTTP_STATUS` (e.g. validation **422**, unavailable **503**, conflict **409**).

### 13–14. WS responses & events

Command replies are CONTROL responses; Runtime events stay subscription fanout — not substitutes.

### 15. Capabilities

Notes include Agent 11.4; operations advertised only when dispatchers are wired.

### 16–17. Authz boundary

`auth_required` stub preserved; unauthenticated + required → `AUTHENTICATION_REQUIRED`. No fake roles. Real auth = **11.5**.

### 18. Files created

`backend/api/commands/{__init__,service,builders,result_mapper,metrics}.py`, `routes/commands.py`, `websocket/command_handler.py`, `docs/specifications/CommandTransportLayerSpecification.md`, `tests/api/commands/*`.

### 19. Files modified

`facade.py`, `app.py`, `services.py`, `websocket/manager.py`, `routes/__init__.py`, WS coverage test, docs (Roadmap, Architecture, Streaming, Telemetry, Replay, specs README, REST/WS specs, `backend/api/README.md`).

### 20–21. Tests / results

`tests/api/commands/` — **35 passed**. Isolation, parity, auth, architecture included.

### 22–26. Regressions

API + transport + Phase 10 acceptance: green. Broader suite (phase10 + replay/live/mode + interpolation): **229 passed**. Ruff/mypy clean.

### 27–28. Ruff / mypy

All checks passed; mypy clean (`--follow-imports=skip`).

### 29. Coverage

Command transport package **\~87.6%** (≥80% gate).

### 30–31. Docs / roadmap

Spec written; docs updated; Roadmap marks **11.4 ✓**, next **11.5 Auth**.

### 32. Limitations

No production auth; `replay.validate` not in `REST_RESOURCES` (WS/service); live needs injected provider factory; no Unity/OBS/AI.

### 33. Recommended Agent 11.5

**Real authentication provider + authorization hooks** for command/control (replace the stub; keep development-permissive mode explicit).

## Assistant

Confirmed. **Agent 11.4 is complete and accepted.** The Phase 11 transport layer now has the full path:

```text
REST / WebSocket
       ↓
Transport Contracts
       ↓
CommandTransportService
       ↓
Existing Dispatchers
       ↓
Existing Controllers
       ↓
Unified Phase 10 Runtime
```

### Phase 11 progress

| Agent | Component | Status |
|---|---|---|
| 11.1 | Transport Architecture | ✅ |
| 11.2 | REST Runtime API | ✅ |
| 11.3 | WebSocket Runtime Gateway | ✅ |
| 11.4 | Command Transport Layer | ✅ |
| **11.5** | **Authentication & Authorization** | ⬜ Next |
| 11.6 | Transport Security / Rate Limiting | ⬜ |
| 11.7 | Production Runtime Wiring | ⬜ |
| 11.8 | Transport Integration Testing | ⬜ |
| 11.9 | Phase 11 Integration | ⬜ |
| 11.10 | Phase 11 Acceptance Testing | ⬜ |

**Next logical agent: 11.5 — Authentication & Authorization.**

It should replace the current auth stub **without putting authentication logic inside the Runtime**, and keep REST/WS using the same authorization boundary.

## User

Please give commands for Agent 11.5	Snapshot Streaming	Stream RaceStateSnapshot efficiently ( 1 click copy and paste cursor friendly)

## Assistant

Yes. Since you have deliberately named **11.5 Snapshot Streaming** rather than the previously suggested auth work, I’d treat **snapshot streaming as the next implementation step** and keep authentication separate.

Paste this entire prompt into Cursor Agent:

```text
You are Agent 11.5 — Snapshot Streaming for the RaceVision project.

========================================================
MISSION
========================================================

Implement efficient RaceStateSnapshot streaming over the existing
Phase 11 REST/WebSocket transport architecture.

The goal is to stream immutable RaceStateSnapshot updates efficiently
to subscribed WebSocket clients without creating a second runtime,
second cache, second timeline, or independent state authority.

RaceStateSnapshotEngine remains the authoritative snapshot producer.

This agent MUST build on Agents 10.18, 10.19, 10.20, 11.1, 11.2,
11.3, and 11.4.

DO NOT redesign the Runtime.

DO NOT create another snapshot engine.

DO NOT bypass EventBus / Runtime authorities.

DO NOT introduce Unity, OBS, Twitch, Kick, YouTube, AI, prediction,
database persistence, or production authentication in this agent.

========================================================
CURRENT ARCHITECTURE
========================================================

Authoritative Runtime:

CacheManager
TimelineService
EventBus
LiveRuntime
SessionManager
ModeController
ReplayService
RaceStateSnapshotEngine

Transport:

shared/transport/
backend/api/
backend/api/websocket/
backend/api/commands/

Existing flow:

Client
  ↓
WebSocket Gateway
  ↓
Subscription / Transport contracts
  ↓
Runtime authorities
  ↓
RaceStateSnapshotEngine
  ↓
Transport serialization
  ↓
bounded per-client WebSocket queue
  ↓
Client

The snapshot engine is the ONLY authority for RaceStateSnapshot.

========================================================
PRIMARY OBJECTIVES
========================================================

Implement:

1. Snapshot subscription lifecycle.
2. Efficient snapshot generation.
3. Snapshot change detection.
4. Snapshot coalescing.
5. Per-client snapshot delivery.
6. Configurable snapshot frequency.
7. Session filtering.
8. Backpressure-safe snapshot streaming.
9. Snapshot sequence/version metadata.
10. Snapshot delivery metrics.
11. Clean disconnect/unsubscribe behavior.
12. Deterministic tests.
13. Documentation.
14. Roadmap update.

========================================================
DESIGN REQUIREMENTS
========================================================

A. EXISTING SNAPSHOT ENGINE

Use:

RaceStateSnapshotEngine.capture()
RaceStateSnapshotEngine.get_latest()

where appropriate.

Do NOT duplicate snapshot composition logic.

The streaming layer is a consumer of the snapshot engine.

--------------------------------------------------------

B. SNAPSHOT STREAM SERVICE

Create a dedicated transport/presentation component, for example:

backend/api/snapshot/

Suggested structure:

backend/api/snapshot/
    __init__.py
    service.py
    publisher.py
    comparator.py
    policy.py
    status.py
    metrics.py
    exceptions.py

Names may be adjusted to match the existing repository conventions.

Responsibilities:

- obtain snapshots
- determine whether a snapshot changed
- publish snapshots to subscribed clients
- apply frequency policy
- coalesce redundant snapshots
- expose metrics/status
- never become a state authority

--------------------------------------------------------

C. SNAPSHOT SUBSCRIPTION

Use the existing Agent 11.1 subscription contracts.

Do NOT invent a competing subscription protocol.

Support:

subscribe to snapshot stream
unsubscribe from snapshot stream

Subscription should support:

session_id
optional frequency
optional change-only mode

If the existing contract already has suitable fields,
reuse them instead of creating duplicates.

--------------------------------------------------------

D. FREQUENCY CONTROL

Implement configurable snapshot delivery frequency.

Examples:

1 Hz
5 Hz
10 Hz
20 Hz
30 Hz
custom configured maximum

Do not assume that higher frequency automatically means
higher-quality runtime data.

The Runtime remains independent of transport frequency.

A client requesting 30 Hz must NOT force the Runtime to operate
at 30 Hz.

The transport layer controls publication frequency only.

--------------------------------------------------------

E. CHANGE DETECTION

Avoid serializing and sending identical snapshots unnecessarily.

Implement deterministic snapshot change detection.

Preferred approach:

1. obtain authoritative snapshot
2. derive deterministic semantic representation
3. compare with previously delivered snapshot for that client
4. suppress unchanged snapshots when change-only mode is enabled
5. otherwise publish according to configured frequency

Do NOT use unstable Python object identity.

Do NOT depend on dictionary insertion order unless the existing
serialization contract guarantees deterministic ordering.

Reuse:

RaceStateSnapshot.to_serializable()

and/or the existing transport serialization utilities.

Do not modify the semantic meaning of RaceStateSnapshot.

--------------------------------------------------------

F. COALESCING

The existing WebSocket gateway already supports bounded queues
and COALESCE_SNAPSHOT behavior.

Integrate with that design.

When a client cannot consume snapshots fast enough:

- newer snapshot supersedes older queued snapshot
- stale snapshots may be discarded
- control messages must not be discarded
- Runtime must never block waiting for a client
- Client A must not affect Client B

Never allow unbounded per-client snapshot queues.

--------------------------------------------------------

G. SESSION ISOLATION

A snapshot containing:

session_id = X

must never be delivered to a subscriber explicitly scoped to:

session_id = Y

unless the existing contract explicitly defines an equivalent
broadcast/global subscription.

Apply filtering before queue insertion.

Test this thoroughly.

--------------------------------------------------------

H. SEQUENCE METADATA

Every streamed snapshot should have transport-level sequencing
metadata where appropriate.

Example:

snapshot_sequence
published_at
session_id
runtime_ms
snapshot_id

Do NOT modify the authoritative snapshot identity unnecessarily.

If transport envelope metadata already supports sequence/correlation,
reuse it.

The sequence must represent transport publication order, not
telemetry sequence.

Document this distinction clearly.

--------------------------------------------------------

I. SNAPSHOT VERSIONING

Respect the existing snapshot schema version:

schema_version = 1.0

Do not silently change the snapshot schema.

If additional transport metadata is required, keep it outside
the snapshot payload where possible.

========================================================
J. EVENTBUS / PUBLICATION MODEL
========================================================

Prefer integration with the existing EventBus / Runtime publication
architecture.

Do not create a polling loop that constantly reconstructs snapshots
at maximum frequency if the Runtime already provides an appropriate
notification mechanism.

If a polling mechanism is necessary, make it:

- bounded
- cancellable
- configurable
- non-blocking
- isolated from Runtime execution
- deterministic in tests

Do not introduce busy-wait loops.

========================================================
K. LIVE / REPLAY SUPPORT
========================================================

Snapshot streaming must work for:

LIVE
REPLAY

using the existing RaceStateSnapshotEngine.

The transport must not care how the snapshot was produced.

Do not create separate:

LiveSnapshotEngine
ReplaySnapshotEngine

There must remain one authoritative snapshot model.

========================================================
L. DELAYED LIVE SUPPORT
========================================================

If Phase 10.16 delay mode is active:

use the snapshot produced by the existing RaceStateSnapshotEngine.

Do not apply another delay in the transport layer.

Transport delay must never stack on top of Runtime delay.

========================================================
M. INTERPOLATION SUPPORT
========================================================

If Phase 10.17 interpolation is enabled:

stream the resulting authoritative snapshot.

Do not perform interpolation in the WebSocket layer.

Transport is presentation only.

========================================================
N. BACKPRESSURE
========================================================

Integrate with Agent 11.3 backpressure.

Required behavior:

FAST CLIENT
→ receives snapshots normally.

SLOW CLIENT
→ snapshots coalesce/drop according to existing policy.

VERY SLOW CLIENT
→ queue remains bounded.

CONTROL MESSAGE
→ higher priority than snapshot data.

RUNTIME
→ never waits for network client.

One slow client must never reduce Runtime throughput.

========================================================
O. ERROR HANDLING
========================================================

Use existing TransportErrorCode / TransportResponse mechanisms.

Do not invent unrelated error formats.

Possible conditions:

SNAPSHOT_UNAVAILABLE
INVALID_SESSION
INVALID_FREQUENCY
SUBSCRIPTION_REQUIRED
STREAM_NOT_AVAILABLE

Map errors consistently with existing transport contracts.

========================================================
P. CONFIGURATION
========================================================

Add configuration only where necessary.

Suggested settings:

SNAPSHOT_STREAM_ENABLED
SNAPSHOT_DEFAULT_HZ
SNAPSHOT_MAX_HZ
SNAPSHOT_CHANGE_ONLY
SNAPSHOT_COALESCE_ENABLED
SNAPSHOT_MAX_CLIENT_QUEUE

Reuse existing WebSocket/backpressure configuration where possible.

Do not duplicate configuration that already exists.

All settings must have safe defaults.

Do not hard-code production assumptions.

========================================================
Q. METRICS
========================================================

Provide useful metrics/status.

At minimum:

snapshots_captured
snapshots_published
snapshots_suppressed
snapshots_coalesced
snapshots_dropped
active_snapshot_subscribers
per-session subscriber counts
publication_errors
serialization_errors
last_publication_time
publication_rate

Do not expose sensitive information.

Use existing metrics conventions.

========================================================
R. CLIENT LIFECYCLE
========================================================

On subscribe:

- validate subscription
- validate session scope
- register subscriber
- initialize delivery state
- optionally send latest snapshot according to existing contract

On unsubscribe:

- remove subscription
- release delivery state
- do not affect Runtime

On WebSocket disconnect:

- remove snapshot subscription
- release queues/state
- no memory leak

On session change:

- old session subscription must not leak into new session.

========================================================
S. INITIAL SNAPSHOT
========================================================

Define deterministic behavior for a new subscriber.

Preferred behavior:

1. subscribe
2. validate
3. obtain latest authoritative snapshot
4. send initial snapshot if available
5. begin incremental streaming

If no snapshot exists:

return/emit the existing appropriate transport state rather
than inventing an empty race state.

Document the behavior.

========================================================
T. REST
========================================================

Do not turn REST into a continuous streaming mechanism.

REST may expose snapshot streaming configuration/status if useful.

Existing:

GET /api/v1/runtime/snapshot

must continue to work.

Do not break Agent 11.2.

========================================================
U. WEBSOCKET
========================================================

Integrate with:

WS /api/v1/ws

Use existing:

subscribe
unsubscribe
snapshot message types
TransportEnvelope
SubscriptionRequest
TransportResponse

Do not create a second WebSocket endpoint.

========================================================
V. TRANSPORT PAYLOAD
========================================================

Use the existing snapshot transport payload contracts.

If changes are required:

- keep backward compatibility
- update versioning
- update tests
- update documentation

Do not leak internal ORM models.

Do not expose SQLAlchemy objects.

Do not expose internal CacheManager structures.

========================================================
W. PERFORMANCE
========================================================

The purpose is efficient streaming.

Avoid:

- JSON serialization multiple times per client
- rebuilding identical snapshots per client
- repeated expensive snapshot capture for every client
- unbounded queues
- blocking EventBus handlers
- per-client Runtime calls

Preferred model:

Runtime snapshot
      ↓
single serialized representation
      ↓
fanout
      ↓
client-specific filtering / envelope
      ↓
bounded queue

Where session-specific serialization prevents safe sharing,
document and implement the minimal correct approach.

Correctness takes priority over premature optimization.

========================================================
TEST REQUIREMENTS
========================================================

Create:

tests/api/snapshot/

Test at minimum:

1. subscribe snapshot stream
2. unsubscribe snapshot stream
3. initial snapshot delivery
4. no snapshot available
5. changed snapshot publication
6. unchanged snapshot suppression
7. frequency enforcement
8. max frequency enforcement
9. invalid frequency
10. session filtering
11. session isolation
12. LIVE snapshot
13. REPLAY snapshot
14. delayed LIVE snapshot
15. interpolated snapshot
16. coalescing
17. slow client
18. bounded queue
19. control message priority
20. disconnect cleanup
21. multiple clients
22. one slow client does not block another
23. deterministic sequence numbers
24. serialization failure
25. publication failure
26. metrics
27. configuration
28. concurrent subscribers
29. no duplicate snapshot engine
30. architecture/import boundary

Tests must use deterministic fake/in-memory authorities where
appropriate.

Do NOT require a real F1 feed.

========================================================
REGRESSION REQUIREMENTS
========================================================

Run:

- snapshot tests
- WebSocket tests
- REST/API tests
- transport tests
- Phase 10 acceptance
- runtime + interpolation regression
- relevant replay/live/mode tests

Required:

Ruff clean.

Mypy clean for new/modified packages.

Do not weaken existing tests or coverage gates.

========================================================
ARCHITECTURE TESTS
========================================================

Explicitly verify that snapshot streaming does NOT import or create:

- a second CacheManager
- a second TimelineService
- a second EventBus authority
- a second ReplayService
- a second LiveRuntime
- ORM persistence logic
- Unity
- OBS
- streaming platform SDKs

The streaming layer must remain a consumer.

========================================================
DOCUMENTATION
========================================================

Create:

docs/specifications/SnapshotStreamingSpecification.md

Update:

docs/Roadmap.md
docs/Architecture.md
docs/Streaming.md
docs/Telemetry.md
docs/Replay.md
docs/specifications/README.md
backend/api/README.md

Document:

- architecture
- subscription protocol
- frequency behavior
- change detection
- coalescing
- backpressure
- session isolation
- initial snapshot behavior
- metrics
- configuration
- LIVE/REPLAY behavior
- delayed LIVE behavior
- limitations

========================================================
ROADMAP
========================================================

Mark:

Phase 11
Agent 11.5 — Snapshot Streaming
COMPLETE ✓

Do not mark later agents complete.

========================================================
ACCEPTANCE GATES
========================================================

Agent 11.5 is COMPLETE only if:

GATE-01 Snapshot subscription works
GATE-02 Unsubscription works
GATE-03 Initial snapshot behavior is deterministic
GATE-04 Snapshot changes stream correctly
GATE-05 Unchanged snapshots can be suppressed
GATE-06 Frequency limits are enforced
GATE-07 Maximum frequency is enforced
GATE-08 Session isolation is enforced
GATE-09 LIVE works
GATE-10 REPLAY works
GATE-11 Delayed LIVE works
GATE-12 Interpolated state works
GATE-13 Backpressure is bounded
GATE-14 Snapshot coalescing works
GATE-15 Control messages remain higher priority
GATE-16 Slow client cannot block Runtime
GATE-17 Slow client cannot block other clients
GATE-18 Disconnect cleanup works
GATE-19 Sequence metadata is deterministic
GATE-20 Serialization failures are handled
GATE-21 Metrics are available
GATE-22 REST API remains compatible
GATE-23 WS API remains compatible
GATE-24 No second Runtime/state authority exists
GATE-25 Architecture boundaries pass
GATE-26 Ruff clean
GATE-27 Mypy clean
GATE-28 Snapshot tests pass
GATE-29 API/WS/transport regressions pass
GATE-30 Phase 10 acceptance remains PASS

========================================================
IMPORTANT ENGINEERING RULES
========================================================

1. Inspect the existing repository before modifying anything.

2. Reuse existing contracts.

3. Reuse existing WebSocket gateway.

4. Reuse RaceStateSnapshotEngine.

5. Reuse existing EventBus and transport serialization.

6. Do not create parallel runtime authorities.

7. Do not fake production F1 telemetry.

8. Do not introduce authentication in this agent.

9. Do not implement Unity/OBS/social streaming.

10. Do not change Phase 10 semantics.

11. Do not silently change public transport contracts.

12. Preserve backward compatibility.

13. Prefer small, composable components.

14. Keep transport concerns outside the core Runtime.

15. Do not stop after creating scaffolding — implement the complete
working feature and tests.

========================================================
FINAL REPORT
========================================================

When complete, report:

1. ACCEPTED / NOT ACCEPTED
2. Architecture implemented
3. Files created
4. Files modified
5. Snapshot subscription behavior
6. Frequency/change-detection behavior
7. Backpressure/coalescing behavior
8. LIVE/REPLAY behavior
9. Session isolation
10. Metrics
11. Configuration
12. REST/WS integration
13. Test count
14. Regression test count
15. Coverage
16. Ruff result
17. Mypy result
18. Acceptance gates GATE-01…30
19. Documentation changes
20. Roadmap status
21. Limitations
22. Recommended Agent 11.6

Do not claim COMPLETE unless all mandatory gates actually pass.
```

## User

## Agent 11.5 — ACCEPTED ✓

Efficient RaceStateSnapshot streaming as a transport consumer of `RaceStateSnapshotEngine` — no second Runtime.

---

### 1. Status

**ACCEPTED**

### 2. Architecture

`Engine → SnapshotStreamService (obtain once) → frequency/change-only gate → TransportEnvelope.sequence → COALESCE queue → WS client`

### 3. Files created

`backend/api/snapshot/{__init__,service,publisher,comparator,policy,status,metrics,exceptions}.py`
`docs/specifications/SnapshotStreamingSpecification.md`
`tests/api/snapshot/*`

### 4. Files modified

WS manager/queue/protocol/settings usage, `app.py`, `routes/runtime.py`, `services.py`, `shared/transport/{subscriptions,envelope}.py`, docs (Roadmap, Architecture, Streaming, Telemetry, Replay, specs README, REST/WS specs, `backend/api/README.md`)

### 5. Subscription

`SNAPSHOT` + required `session_id`; optional `frequency_hz` / `change_only`. Unsubscribe + disconnect clear delivery state.

### 6. Frequency / change detection

Per-sub Hz capped by `SNAPSHOT_MAX_HZ` (default 30). Semantic fingerprint ignores `snapshot_id` / `captured_at` / `capture_sequence`.

### 7. Backpressure / coalesce

Existing bounded queues + `COALESCE_SNAPSHOT`; control > snapshot; Runtime never waits.

### 8. LIVE / REPLAY

Mode-agnostic engine projections streamed as-is (including delay + interpolation fields). No transport delay stacking.

### 9. Session isolation

Mismatch → no delivery (tested).

### 10. Metrics

Published/suppressed/coalesced/dropped/subscribers/rate/errors via service + `GET /runtime/snapshot/stream`.

### 11. Configuration

`SNAPSHOT_STREAM_*` + existing `WS_*` backpressure/interval (default Hz derived from interval).

### 12. REST / WS

REST snapshot unchanged; stream status endpoint added. Same `WS /api/v1/ws`.

### 13–15. Tests / coverage

**30** snapshot tests; package coverage **\~83%**. Regressions: WS+API+transport green; Phase 10 + interpolation **98** in focused run.

### 16–17. Ruff / mypy

Clean for new/modified packages.

### 18. Gates GATE-01…30

All mandatory gates satisfied (subscribe/unsub/initial/change/freq/isolation/LIVE·REPLAY·delay·interp/backpressure/coalesce/control priority/cleanup/sequence/errors/metrics/REST·WS compat/architecture/ruff/mypy/Phase 10).

### 19–20. Docs / roadmap

Spec complete; **11.5 Snapshot Streaming ✓**; **11.6 = Auth**.

### 21. Limitations

No deltas; poll-based fanout (bounded); no production auth; multi-session `conn.session_id` last-wins.

### 22. Recommended Agent 11.6

**Auth provider / authorization hooks / hardening**

## Assistant

Confirmed. **Agent 11.5 is accepted and complete.** ✓

The important architectural point is that snapshot streaming remains a **transport consumer**, exactly as intended:

```text
Phase 10 Runtime
      │
      ▼
RaceStateSnapshotEngine
      │
      ▼
SnapshotStreamService
      │
      ├── frequency gate
      ├── change detection
      ├── transport envelope
      └── bounded/coalescing queue
               │
               ▼
        WebSocket Gateway
               │
          ┌────┴────┐
          ▼         ▼
       Client A   Client B
```

### Phase 11 status

| Agent | Component | Status |
|---|---|---:|
| 11.1 | Transport Architecture | ✅ |
| 11.2 | REST Runtime API | ✅ |
| 11.3 | WebSocket Runtime Gateway | ✅ |
| 11.4 | Command Transport Layer | ✅ |
| 11.5 | Snapshot Streaming | ✅ |
| **11.6** | **Authentication & Authorization** | ⬜ **NEXT** |
| 11.7 | Transport Hardening / Rate Limiting | ⬜ |
| 11.8 | Production Runtime Wiring | ⬜ |
| 11.9 | Phase 11 Integration | ⬜ |
| 11.10 | Phase 11 Acceptance Testing | ⬜ |

One thing worth preserving for 11.6: **do not put authentication/authorization into the Runtime.** It belongs at the API/transport boundary and should apply consistently to REST commands, WebSocket commands, subscriptions, and snapshot access.

The current **11.5 limitation — “no production auth” — is exactly the reason 11.6 should address the auth boundary next.**

## User

Please give commands for Agent 11.6	Authentication & Authorization ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. Agent 11.6 should replace the current authentication stub while keeping **all security concerns at the transport/API boundary**, with no changes to the Phase 10 Runtime authority model.

Paste this entire block into Cursor Agent:

```text
You are Agent 11.6 — Authentication & Authorization for the RaceVision project.

========================================================
MISSION
========================================================

Implement the production-ready Authentication & Authorization
boundary for the existing RaceVision REST + WebSocket transport.

This agent replaces the existing development authentication stub
introduced by Agents 11.1–11.5.

Authentication and authorization MUST remain outside the core Runtime.

The Runtime remains completely unaware of:

- users
- passwords
- tokens
- JWT
- API keys
- roles
- permissions
- OAuth/OIDC
- sessions at the identity layer

This agent MUST build on:

Agent 11.1 — Transport Architecture
Agent 11.2 — REST Runtime API
Agent 11.3 — WebSocket Runtime Gateway
Agent 11.4 — Command Transport Layer
Agent 11.5 — Snapshot Streaming

Do not redesign the Runtime.

Do not create another Runtime.

Do not modify CacheManager authority.

Do not modify TimelineService authority.

Do not modify RaceStateSnapshotEngine authority.

Do not bypass existing Controllers or Dispatchers.

========================================================
SECURITY ARCHITECTURE
========================================================

Required architecture:

Client
  ↓
Authentication Middleware / Dependency
  ↓
Identity
  ↓
Authorization Policy
  ↓
Transport Endpoint
  ↓
Existing Controllers / Dispatchers
  ↓
Phase 10 Runtime

For WebSocket:

Client
  ↓
WebSocket Authentication
  ↓
Identity
  ↓
Authorization
  ↓
Subscription / Command
  ↓
Existing Gateway
  ↓
Runtime

Authentication MUST happen before protected operations.

Authorization MUST happen before:

- runtime commands
- replay commands
- live commands
- mode changes
- snapshot subscriptions
- protected snapshot access

========================================================
IMPORTANT SECURITY RULE
========================================================

DO NOT invent a fake production authentication provider.

Implement a provider abstraction and a safe development provider,
but production configuration MUST require an explicitly configured
real authentication backend.

Do not claim OAuth/OIDC/JWT verification is production-secure
unless the implementation actually performs cryptographic
verification and key validation.

========================================================
PROVIDER ARCHITECTURE
========================================================

Create a provider abstraction similar to:

backend/api/security/
    __init__.py
    models.py
    provider.py
    policy.py
    permissions.py
    roles.py
    middleware.py
    dependencies.py
    websocket.py
    configuration.py
    exceptions.py
    audit.py
    metrics.py

Reuse existing security files if Agent 11.2/11.3 already created
them.

Do NOT duplicate security modules.

========================================================
IDENTITY MODEL
========================================================

Define an immutable authenticated principal.

Example conceptual fields:

principal_id
subject
issuer
roles
permissions
session_ids
metadata
authenticated_at
authentication_method

Keep the public model minimal.

Do not store passwords.

Do not store access tokens in logs.

Do not expose secrets through transport responses.

========================================================
AUTHENTICATION PROVIDER
========================================================

Define an interface such as:

AuthenticationProvider

with responsibilities such as:

authenticate_http(...)
authenticate_websocket(...)
validate_credentials(...)
validate_token(...)

The exact method names should follow repository conventions.

The provider must return an authenticated Principal.

Provider failures must map to existing transport errors.

========================================================
SUPPORTED AUTHENTICATION
========================================================

The architecture must support a pluggable provider.

Implement at minimum:

1. Development provider
2. Token-based provider boundary

The token provider must be structured so a real JWT/OIDC provider
can be plugged in without modifying Runtime or Controllers.

If the repository already contains an authentication dependency
or provider abstraction, extend it rather than duplicating it.

========================================================
DEVELOPMENT AUTH
========================================================

Development authentication MUST be explicitly configurable.

Example:

AUTH_ENABLED=false
AUTH_PROVIDER=development

or equivalent existing configuration.

Development bypass must NEVER silently activate in production.

Production startup/configuration must reject insecure combinations
such as:

ENVIRONMENT=production
AUTH_ENABLED=false

unless an explicit emergency override is documented and strongly
guarded.

Do not use a hard-coded development secret.

========================================================
TOKEN AUTHENTICATION
========================================================

If implementing JWT verification:

Support proper validation of:

- signature
- algorithm
- issuer
- audience
- expiration
- not-before
- subject

Do not accept:

- alg=none
- unsigned tokens
- arbitrary algorithms
- expired tokens

Use a maintained cryptographic library already present in the
project where possible.

Do not write custom cryptography.

If a real external OIDC/JWKS provider cannot be fully implemented
without introducing an unsupported dependency, create the provider
interface and a secure integration boundary rather than pretending
verification exists.

========================================================
AUTHORIZATION MODEL
========================================================

Implement explicit permissions.

Suggested permissions:

runtime:read
runtime:snapshot:read

session:read

replay:read
replay:control
replay:bookmark

live:read
live:control

mode:read
mode:switch

transport:subscribe

admin:configuration

Use repository naming conventions if equivalent permissions already
exist.

Do not grant permissions implicitly based only on endpoint names.

========================================================
ROLES
========================================================

Provide a small default role model.

Suggested:

viewer
operator
admin

Example:

viewer:
    runtime:read
    runtime:snapshot:read
    session:read
    replay:read
    live:read
    mode:read
    transport:subscribe

operator:
    viewer permissions
    replay:control
    replay:bookmark
    live:control
    mode:switch

admin:
    operator permissions
    admin:configuration

Do not over-engineer RBAC.

The permission system must remain extensible.

========================================================
RESOURCE AUTHORIZATION
========================================================

Authorization must support resource/session scope.

For example:

A principal authorized for session A must not automatically
control session B.

Required checks:

principal
+
permission
+
resource/session scope

before execution.

This is particularly important for:

- replay commands
- live commands
- mode switching
- snapshot subscriptions

========================================================
REST PROTECTION
========================================================

Protect existing API routes without changing their business logic.

Examples:

GET /api/v1/runtime/status
GET /api/v1/runtime/snapshot
GET /api/v1/runtime/capabilities
GET /api/v1/sessions

require appropriate read permissions when authentication is enabled.

Protect command endpoints according to their permissions.

Examples:

Replay read
Replay control
Live control
Mode switch

Do not move authorization logic into:

ReplayService
LiveSessionAdapter
ModeController
RaceStateSnapshotEngine

Authorization belongs in the API boundary.

========================================================
WEBSOCKET AUTHENTICATION
========================================================

Protect:

WS /api/v1/ws

Authentication must occur before accepting protected operations.

Support authentication during WebSocket connection establishment.

Do not put access tokens into logs.

Do not echo credentials back to clients.

After authentication:

connection → principal

Every subscription and command must use that principal.

========================================================
WEBSOCKET AUTHORIZATION
========================================================

Authorization must be checked independently for:

subscribe
unsubscribe
snapshot subscription
telemetry subscription
event subscription
replay commands
live commands
mode commands

Do not assume that authentication automatically grants permission.

A user authenticated as viewer must not be able to:

- start live sessions
- stop live sessions
- switch modes
- control replay

unless explicitly authorized.

========================================================
COMMAND TRANSPORT INTEGRATION
========================================================

Integrate with Agent 11.4:

CommandTransportService

Do not create a parallel command dispatcher.

Required flow:

REST / WS
   ↓
Authentication
   ↓
Authorization
   ↓
CommandTransportService
   ↓
Existing Dispatcher
   ↓
Existing Controller
   ↓
Runtime

Authorization failures must prevent the command from reaching
the dispatcher.

========================================================
SNAPSHOT STREAMING INTEGRATION
========================================================

Integrate with Agent 11.5.

Snapshot subscriptions require:

transport:subscribe
+
runtime:snapshot:read

and appropriate session scope.

A viewer may subscribe to permitted sessions.

Unauthorized session subscriptions must fail cleanly.

Do not leak snapshot information through:

- error messages
- timing-sensitive metadata
- subscription status
- metrics

========================================================
ERROR MODEL
========================================================

Reuse:

TransportErrorCode
TransportResponse
existing HTTP mappings
existing WebSocket error envelopes

Provide clear but non-sensitive errors.

Examples:

AUTHENTICATION_REQUIRED
AUTHENTICATION_FAILED
TOKEN_EXPIRED
TOKEN_INVALID
AUTHORIZATION_DENIED
RESOURCE_FORBIDDEN
SESSION_FORBIDDEN

Do not reveal:

- whether a username exists
- token internals
- signing keys
- issuer secrets
- database credentials

HTTP examples:

401 → unauthenticated / invalid authentication

403 → authenticated but unauthorized

Do not confuse 401 and 403.

========================================================
SECURITY HEADERS
========================================================

For REST responses, implement appropriate security headers where
they belong at the HTTP boundary.

Examples may include:

X-Content-Type-Options
Cache-Control for sensitive responses
Content-Security-Policy where appropriate
Referrer-Policy

Do not blindly apply browser-only headers to WebSocket frames.

Follow existing API conventions.

========================================================
CORS
========================================================

Review existing:

API_CORS_ORIGINS

Do not default to wildcard CORS in production.

Configuration must distinguish:

development
testing
production

Credentialed CORS must never be combined with wildcard origins.

========================================================
SECRET HANDLING
========================================================

Never:

- hard-code secrets
- commit secrets
- log tokens
- log Authorization headers
- return secrets in errors
- expose provider credentials through /runtime/status
- include secrets in metrics

Configuration must use environment/settings mechanisms already used
by RaceVision.

========================================================
RATE LIMITING / BRUTE FORCE
========================================================

Do NOT implement a huge rate-limiting subsystem in this agent.

However, create the security hooks needed for Agent 11.7.

Expose security metrics such as:

authentication_attempts
authentication_failures
authorization_denials
active_authenticated_connections

Do not record raw credentials.

Document rate limiting as an Agent 11.7 concern.

========================================================
AUDIT LOGGING
========================================================

Implement structured security audit events.

Examples:

authentication_success
authentication_failure
authorization_denied
authorization_success for sensitive operations
websocket_authenticated
websocket_disconnect

Include safe metadata:

timestamp
principal_id
operation
resource
session_id where safe
correlation_id
result

Never include:

password
raw token
Authorization header
secret
private key

Use existing structlog/logging conventions.

========================================================
FAIL-CLOSED BEHAVIOR
========================================================

When authentication is enabled:

missing identity
→ reject

invalid identity
→ reject

missing permission
→ reject

invalid session scope
→ reject

unknown provider
→ startup/configuration failure

Do not silently fall back from production authentication to
development authentication.

========================================================
CONFIGURATION
========================================================

Reuse existing API/security settings where possible.

Suggested settings:

AUTH_ENABLED
AUTH_PROVIDER
AUTH_ISSUER
AUTH_AUDIENCE
AUTH_JWKS_URL
AUTH_ALLOWED_ALGORITHMS
AUTH_CLOCK_SKEW_SECONDS
AUTH_REQUIRE_HTTPS
AUTH_DEV_MODE

Only add settings that are actually required.

Production defaults must be secure.

Do not expose secrets through configuration introspection.

========================================================
HTTPS / SECURE TRANSPORT
========================================================

The application should be capable of enforcing secure transport
in production.

If TLS termination occurs at a reverse proxy, support the existing
deployment model rather than implementing a second TLS stack.

When:

AUTH_REQUIRE_HTTPS=true

reject insecure HTTP authentication attempts unless the existing
trusted-proxy configuration explicitly identifies the request as
secure.

Do not blindly trust arbitrary forwarded headers.

========================================================
WEBSOCKET SECURITY
========================================================

Do not put long-lived credentials in URLs.

Avoid:

ws://host/ws?token=SECRET

Prefer the existing authentication mechanism supported by the
transport architecture.

If browser constraints require a token transport mechanism,
document its security implications and ensure tokens do not appear
in ordinary access logs.

========================================================
SECURITY STATUS
========================================================

Do NOT expose:

- JWT secrets
- signing keys
- raw configuration
- provider credentials

through:

GET /runtime/status
GET /runtime/capabilities

It is acceptable to expose safe information such as:

authentication_enabled
provider_type
authorization_enabled
websocket_authentication_required

Do not expose secret values.

========================================================
TEST REQUIREMENTS
========================================================

Create or extend:

tests/api/security/

Required tests:

1. authentication disabled development mode
2. authentication enabled
3. missing credentials
4. invalid credentials
5. expired token
6. invalid token
7. invalid signature
8. invalid issuer
9. invalid audience
10. unsupported algorithm
11. authenticated principal creation
12. permission checking
13. role expansion
14. viewer permissions
15. operator permissions
16. admin permissions
17. denied command
18. allowed command
19. session scope allowed
20. session scope denied
21. REST authentication
22. REST authorization
23. WebSocket authentication
24. WebSocket authorization
25. snapshot subscription authorization
26. replay command authorization
27. live command authorization
28. mode switch authorization
29. unauthorized session isolation
30. correct 401 mapping
31. correct 403 mapping
32. no token leakage in logs
33. no secrets in status
34. development bypass cannot activate in production
35. unknown provider fails safely
36. secure configuration validation
37. CORS production behavior
38. security headers
39. audit events
40. correlation IDs
41. WebSocket disconnect cleanup
42. authenticated multiple clients
43. different principals isolated
44. authorization failure never reaches controller
45. architecture/import boundary

Use deterministic test providers/fixtures.

Do not require an external identity provider for unit tests.

========================================================
REGRESSION REQUIREMENTS
========================================================

Run:

- security tests
- API tests
- WebSocket tests
- command transport tests
- snapshot streaming tests
- transport tests
- Phase 10 acceptance
- runtime + interpolation tests
- replay/live/mode tests

Required:

Ruff clean.

Mypy clean for modified/new security packages.

Do not weaken existing tests.

========================================================
ARCHITECTURE TESTS
========================================================

Explicitly verify security packages do NOT import:

- CacheManager
- TimelineService
- ReplayService internals
- LiveRuntime internals
- RaceStateSnapshotEngine internals
- SQLAlchemy models
- Unity
- OBS
- streaming platforms

Security must depend on transport/API abstractions, not Runtime internals.

========================================================
DOCUMENTATION
========================================================

Create:

docs/specifications/AuthenticationAuthorizationSpecification.md

Update:

docs/Roadmap.md
docs/Architecture.md
docs/Streaming.md
docs/Telemetry.md
docs/Replay.md
docs/specifications/README.md
backend/api/README.md

Document:

- authentication architecture
- provider interface
- development mode
- production requirements
- authorization model
- roles
- permissions
- session/resource scope
- REST behavior
- WebSocket behavior
- command authorization
- snapshot authorization
- token handling
- secret handling
- audit logging
- CORS
- HTTPS
- security headers
- failure behavior
- limitations
- Agent 11.7 responsibilities

========================================================
ROADMAP
========================================================

Mark:

Phase 11
Agent 11.6 — Authentication & Authorization
COMPLETE ✓

Do not mark 11.7 or later complete.

========================================================
ACCEPTANCE GATES
========================================================

Agent 11.6 is COMPLETE only if:

GATE-01 Authentication provider abstraction exists
GATE-02 Development provider is explicitly configurable
GATE-03 Production cannot silently use development bypass
GATE-04 Missing authentication is rejected when enabled
GATE-05 Invalid authentication is rejected
GATE-06 Token validation boundary is implemented safely
GATE-07 No custom cryptography exists
GATE-08 401/403 mapping is correct
GATE-09 Permission model exists
GATE-10 Role model exists
GATE-11 Resource/session authorization exists
GATE-12 REST authentication works
GATE-13 REST authorization works
GATE-14 WebSocket authentication works
GATE-15 WebSocket authorization works
GATE-16 Snapshot subscription authorization works
GATE-17 Replay command authorization works
GATE-18 Live command authorization works
GATE-19 Mode command authorization works
GATE-20 Unauthorized session access is denied
GATE-21 Authorization happens before controller dispatch
GATE-22 No Runtime security coupling exists
GATE-23 Secrets are not logged
GATE-24 Tokens are not logged
GATE-25 Security status exposes no secrets
GATE-26 CORS production behavior is safe
GATE-27 HTTPS/security configuration is validated
GATE-28 Audit logging works
GATE-29 Security metrics work
GATE-30 WebSocket disconnect cleanup works
GATE-31 Architecture boundaries pass
GATE-32 Ruff clean
GATE-33 Mypy clean
GATE-34 Security tests pass
GATE-35 API/WS/command/snapshot regressions pass
GATE-36 Phase 10 acceptance remains PASS
GATE-37 Existing Phase 11 functionality remains compatible

========================================================
IMPORTANT ENGINEERING RULES
========================================================

1. Inspect the existing repository first.

2. Reuse Agent 11.1 transport contracts.

3. Reuse Agent 11.2 REST API.

4. Reuse Agent 11.3 WebSocket Gateway.

5. Reuse Agent 11.4 CommandTransportService.

6. Reuse Agent 11.5 Snapshot Streaming.

7. Do not create another Runtime.

8. Do not place authorization inside Runtime services.

9. Do not create fake production security.

10. Do not hard-code credentials.

11. Do not write custom cryptography.

12. Fail closed when authentication is enabled.

13. Preserve development usability through explicit configuration.

14. Never leak credentials through logs, metrics, errors, or status.

15. Preserve existing transport contracts.

16. Preserve existing Phase 10 behavior.

17. Keep authentication/authorization modular and replaceable.

18. Do not implement rate limiting fully — leave the appropriate
hooks for Agent 11.7.

19. Do not implement Unity, OBS, social streaming, AI, or prediction.

20. Do not stop at scaffolding. Implement the complete feature,
tests, integration, documentation, and acceptance validation.

========================================================
FINAL REPORT
========================================================

When complete, report:

1. ACCEPTED / NOT ACCEPTED
2. Authentication architecture
3. Authorization architecture
4. Provider implementation
5. Principal model
6. Roles
7. Permissions
8. Session/resource authorization
9. REST integration
10. WebSocket integration
11. Command transport integration
12. Snapshot streaming integration
13. Configuration
14. Security/audit logging
15. Metrics
16. Security headers/CORS/HTTPS handling
17. Files created
18. Files modified
19. Test count
20. Regression test count
21. Coverage
22. Ruff result
23. Mypy result
24. GATE-01…37 results
25. Documentation changes
26. Roadmap status
27. Limitations
28. Recommended Agent 11.7

Do not claim COMPLETE unless every mandatory gate actually passes.
```

## User

## Agent 11.6 — ACCEPTED ✓

Production-ready auth/authz at the transport boundary only. Runtime stays identity-unaware.

---

### 1. Status

**ACCEPTED**

### 2–3. Architecture

`Client → Provider → Principal → AuthorizationPolicy → REST/WS → existing services/dispatchers → Phase 10 Runtime`

### 4. Providers

- **Disabled** (`AUTH_ENABLED=false`)
- **Development** (`AUTH_PROVIDER=development` + `AUTH_DEV_MODE=true`; blocked in production)
- **JWT** (PyJWT: signature, alg allow-list excluding `none`, iss/aud/exp/nbf/sub; JWKS or HMAC secret)

### 5–7. Principal / roles / permissions

Immutable `Principal`. Roles: **viewer / operator / admin**. Permissions as specified (`runtime:read`, `replay:control`, `mode:switch`, `transport:subscribe`, …).

### 8. Session scope

Allow-list on principal; mismatch → **403** `AUTHORIZATION_DENIED` (`SESSION_FORBIDDEN`).

### 9–12. Integrations

REST routes + commands authorize before dispatch. WS authenticates before accept (`Authorization` or `racevision-bearer` subprotocol). Snapshot subscribe needs subscribe + snapshot\:read. Commands never reach dispatchers on deny.

### 13. Configuration

`AUTH_*` settings; production fail-closed for auth-off / development provider without `AUTH_ALLOW_INSECURE_OVERRIDE`.

### 14–16. Audit / metrics / headers

Structlog audit (no tokens). Security metrics for Agent 11.7. Security headers + safe CORS (no `*` with production credentials).

### 17–18. Files

Created `backend/api/security/*` (replaced stub file with package). Wired `app`, routes, WS manager/command handler, transport error codes. Spec + tests under `tests/api/security/`.

### 19–23. Quality

**34** security tests; Phase 11 API regressions green (**141**); Phase 10/transport/interpolation **79**. Coverage **\~76%**. Ruff/mypy clean.

### 24. Gates GATE-01…37

All mandatory gates pass.

### 25–26. Docs / roadmap

`AuthenticationAuthorizationSpecification.md` written; docs updated; **11.6 ✓**; next **11.7 Rate limiting**.

### 27. Limitations

No full OIDC UI flows; no revocation list; rate limiting deferred; `/health` stays open for probes.

### 28. Recommended Agent 11.7

**Rate limiting / brute-force protections** using the new security metrics hooks.

## Assistant

Excellent. **Agent 11.6 is correctly accepted.** The Phase 11 transport/security foundation is now substantially complete:

**11.1 ✓ Transport Architecture**  
**11.2 ✓ REST Runtime API**  
**11.3 ✓ WebSocket Runtime Gateway**  
**11.4 ✓ Command Transport Layer**  
**11.5 ✓ Snapshot Streaming**  
**11.6 ✓ Authentication & Authorization**

The logical next step is **Agent 11.7 — Rate Limiting & Abuse Protection**, using the security hooks Agent 11.6 deliberately left behind.

If you want to continue in the same format, I can give you the **single-click Cursor command for Agent 11.7** next.

## User

Please give commands for Agent 11.6.1	Live Telemetry Streaming	Stream live canonical telemetry/events ( 1 click copy and paste cursor friendly)

## Assistant

Yes. Since **11.6 is already accepted**, I would treat **11.6.1 as a transport streaming sub-phase**, not as another authentication/security phase. It should consume the existing authenticated WebSocket gateway and stream canonical live telemetry without creating a second ingestion/runtime path.

Paste this entire block into Cursor Agent:

```text
You are Agent 11.6.1 — Live Telemetry Streaming for the RaceVision project.

========================================================
MISSION
========================================================

Implement production-ready transport streaming for LIVE canonical
telemetry and runtime events.

This is an extension of the existing Phase 11 transport layer.

The implementation MUST use the existing:

- Agent 11.1 Transport Architecture
- Agent 11.2 REST Runtime API
- Agent 11.3 WebSocket Runtime Gateway
- Agent 11.4 Command Transport Layer
- Agent 11.5 Snapshot Streaming
- Agent 11.6 Authentication & Authorization
- Agent 10.14 Live Session Adapter
- Agent 10.16 Race Timeline Delay Buffer
- Agent 10.17 Telemetry Interpolation & Gap Handling
- Agent 10.18 Race State Snapshot Engine
- Agent 10.19 Phase 10 Integration
- Agent 10.20 Phase 10 Acceptance

Do NOT create another Runtime.

Do NOT create another telemetry ingestion pipeline.

Do NOT create another EventBus.

Do NOT create another CacheManager.

Do NOT bypass LiveSessionAdapter.

Do NOT invent an F1 telemetry feed.

Do NOT connect directly to a third-party F1 feed from the WebSocket
gateway.

The transport layer is a consumer of the existing canonical runtime.

========================================================
PRIMARY OBJECTIVE
========================================================

Enable authenticated WebSocket clients to subscribe to:

1. LIVE canonical telemetry
2. LIVE runtime events
3. LIVE session-scoped telemetry
4. LIVE session-scoped events

using the existing:

WS /api/v1/ws

and existing Agent 11.1 subscription contracts.

Required architecture:

Real Live Provider
      ↓
LiveSessionAdapter
      ↓
Delay Buffer (optional)
      ↓
Interpolation Service (optional)
      ↓
Canonical Runtime
      ↓
Cache / Timeline / EventBus
      ↓
Live Telemetry Stream Publisher
      ↓
WebSocket Gateway
      ↓
Authenticated Client

The WebSocket layer MUST NOT become the source of truth.

========================================================
AUTHORITATIVE DATA FLOW
========================================================

Canonical LIVE telemetry MUST originate from:

LiveSessionAdapter

or the existing canonical EventBus path produced by it.

Do not reconstruct telemetry from:

- snapshots
- REST responses
- replay frames
- database queries
- presentation objects
- Unity state
- OBS state

unless the existing architecture explicitly identifies that source
as the canonical runtime event.

========================================================
TELEMETRY STREAM CONTRACT
========================================================

Use the existing shared transport envelope.

Extend existing DTOs/contracts where required.

Do not create a parallel transport protocol.

A telemetry message should conceptually contain:

TransportEnvelope
    version
    message_type
    sequence
    timestamp
    session_id
    payload

Telemetry payload should contain only canonical transport-safe data.

Suggested conceptual fields:

session_id
driver_id
car_id
timestamp
source_timestamp
received_at
sequence
position
velocity
speed
heading
throttle
brake
rpm
gear
lap
sector
race_position
pit_state
flags
quality
is_interpolated
provenance

Only include fields that actually exist in the canonical telemetry
model.

Do NOT invent fields merely to satisfy this specification.

========================================================
EVENT STREAM CONTRACT
========================================================

Stream canonical runtime events through the existing EventBus.

Examples:

lap completed
sector completed
overtake
incident
pit entry
pit exit
flag/state changes
session lifecycle
telemetry quality/degradation
delay state changes
interpolation quality changes

Only forward events that actually exist in the Runtime/EventBus.

Do NOT synthesize events inside the WebSocket gateway.

========================================================
SUBSCRIPTION TYPES
========================================================

Extend the existing Agent 11.1 subscription model if necessary.

Required stream types:

TELEMETRY
EVENT

Existing:

SNAPSHOT

must remain unchanged.

A client may subscribe to:

TELEMETRY
EVENT
SNAPSHOT

independently.

Do not automatically subscribe clients to telemetry.

========================================================
SUBSCRIPTION REQUIREMENTS
========================================================

LIVE telemetry subscriptions MUST require:

transport:subscribe
+
live:read

LIVE event subscriptions MUST require:

transport:subscribe
+
live:read

Existing Agent 11.6 authorization must remain authoritative.

Do not bypass:

AuthenticationProvider
Principal
AuthorizationPolicy

Unauthorized subscriptions must be rejected before stream
registration.

========================================================
SESSION ISOLATION
========================================================

Every telemetry subscription MUST be session scoped.

session_id is REQUIRED.

Example conceptual request:

{
    "message_type": "subscribe",
    "subscription": {
        "type": "telemetry",
        "session_id": "<uuid>"
    }
}

A client subscribed to session A must never receive telemetry from
session B.

This must be enforced BEFORE enqueueing data.

Never rely only on client-side filtering.

========================================================
LIVE-ONLY SEMANTICS
========================================================

This stream is for LIVE telemetry.

Do not mix:

LIVE
REPLAY
HISTORICAL

into a single telemetry subscription unless the existing transport
contract explicitly supports a mode filter.

At minimum, telemetry subscriptions must carry enough metadata to
identify the originating session and operating mode.

Expected mode:

LIVE

If the Runtime is in REPLAY mode, live telemetry must not be emitted
to a LIVE subscription.

========================================================
DELAY BUFFER INTEGRATION
========================================================

Agent 10.16 already provides the optional Race Timeline Delay Buffer.

The transport MUST consume the telemetry after the configured delay
pipeline where the existing LiveSessionAdapter defines the canonical
delivery point.

Do NOT implement another WebSocket delay.

Do NOT add:

sleep()
asyncio.sleep()
queue delay timers
transport-side timestamp shifting

to simulate the race delay.

The transport simply publishes the canonical runtime result.

If delay is disabled:

source telemetry remains undelayed.

If delay is enabled:

the stream reflects the delayed runtime telemetry.

========================================================
INTERPOLATION INTEGRATION
========================================================

Agent 10.17 interpolation is optional and disabled by default.

The transport MUST preserve canonical metadata such as:

is_interpolated
provenance
quality

when these fields exist.

Do not interpolate in the WebSocket layer.

Do not reorder telemetry in the transport.

Do not generate missing frames in the transport.

========================================================
EVENT BUS INTEGRATION
========================================================

Use the existing EventBus.

Implement a thin bridge/publisher if necessary.

Required conceptual flow:

EventBus
   ↓
LiveTelemetryStreamPublisher
   ↓
GatewayBusBridge / WebSocket manager
   ↓
session filter
   ↓
authorization scope
   ↓
bounded client queue
   ↓
WebSocket

Do not create a second EventBus.

========================================================
BACKPRESSURE
========================================================

A slow WebSocket client MUST NEVER block:

- LiveSessionAdapter
- EventBus
- CacheManager
- TimelineService
- LiveRuntime
- interpolation
- delay buffer

Reuse Agent 11.3 bounded per-client queues.

Reuse:

COALESCE_SNAPSHOT

where applicable.

Telemetry requires an explicit policy.

Implement configuration for:

DROP_OLDEST
DROP_NEWEST
DISCONNECT_SLOW_CLIENT

Default should be conservative and bounded.

Do not allow unlimited telemetry queues.

========================================================
TELEMETRY COALESCING
========================================================

Do NOT blindly coalesce telemetry in the same manner as snapshots.

Telemetry is sequential data.

If telemetry coalescing is implemented, it must be explicit and
documented.

Preserve:

sequence
source timestamp
session_id

and never create misleading continuity.

Dropped/coalesced telemetry must be observable through metrics.

========================================================
SEQUENCE NUMBERS
========================================================

Preserve canonical source sequence where available.

Transport may also provide a transport sequence.

Do NOT overwrite canonical sequence.

If two sequence concepts exist, name them clearly.

For example:

source_sequence
transport_sequence

Do not pretend the transport sequence represents telemetry source
ordering.

========================================================
ORDERING
========================================================

Within a single client/session stream:

telemetry should be delivered in canonical runtime order.

The gateway MUST NOT:

- reorder old frames
- extrapolate
- invent timestamps
- replay old frames after reconnect
- silently merge sessions

Late/out-of-order handling remains the responsibility of the
canonical telemetry pipeline.

========================================================
DUPLICATES
========================================================

Do not silently duplicate frames.

If the EventBus can produce duplicate delivery notifications,
the stream publisher should use the existing canonical sequence
or event identity where appropriate.

Do not create a global deduplication system unless repository
architecture requires it.

========================================================
EVENT DELIVERY
========================================================

Events should be delivered separately from telemetry.

Do not convert every telemetry sample into a WebSocket event.

Do not create synthetic events for:

- speed changes
- throttle changes
- position changes

unless such events already exist in the Runtime.

========================================================
EVENT PRIORITY
========================================================

Reuse Agent 11.3 queue priority.

Recommended:

CONTROL
EVENT
SNAPSHOT
TELEMETRY

Do not allow high-rate telemetry to starve:

- commands
- errors
- lifecycle events
- critical runtime events

========================================================
AUTHENTICATION
========================================================

Reuse Agent 11.6.

Every WebSocket client must have an authenticated Principal when
authentication is enabled.

Do not implement authentication again.

Do not introduce a second token mechanism.

========================================================
AUTHORIZATION
========================================================

Before registering:

TELEMETRY subscription

verify:

transport:subscribe
live:read

Before registering:

EVENT subscription

verify:

transport:subscribe
live:read

Then enforce:

principal session scope
+
requested session_id

on every delivery.

Authorization must occur before queue insertion.

========================================================
REST
========================================================

This agent is primarily WebSocket streaming.

Do NOT build a polling REST telemetry endpoint.

REST remains appropriate for:

- runtime status
- snapshot
- sessions
- capabilities
- stream status

If useful, extend the existing stream-status endpoint to report:

telemetry_subscribers
event_subscribers
messages_published
messages_dropped
messages_coalesced
slow_clients
authorization_denials

Do not expose telemetry payloads through the status endpoint.

========================================================
WEBSOCKET MESSAGE EXAMPLES
========================================================

Use the repository's actual envelope/serialization conventions.

Conceptual subscription:

{
    "message_type": "subscribe",
    "request_id": "...",
    "subscription": {
        "type": "telemetry",
        "session_id": "..."
    }
}

Conceptual telemetry:

{
    "message_type": "telemetry",
    "sequence": 12345,
    "session_id": "...",
    "payload": {
        "...canonical telemetry..."
    }
}

Conceptual event:

{
    "message_type": "event",
    "sequence": 987,
    "session_id": "...",
    "payload": {
        "...canonical event..."
    }
}

Do not copy these examples literally if existing contracts differ.

========================================================
FILTERING
========================================================

Support session filtering as mandatory.

If existing transport contracts already support filters, preserve them.

Optional filters may include:

driver_id
car_id
event_type

Only implement filters that can be safely evaluated from canonical
runtime data.

Do not query PostgreSQL for every WebSocket frame.

Do not scan the entire telemetry history.

========================================================
RATE CONTROL
========================================================

Do not impose arbitrary low-frequency limits on canonical telemetry.

However, protect the gateway from pathological subscriptions.

Implement configuration such as:

LIVE_TELEMETRY_MAX_HZ

only if needed.

Default should be compatible with the expected canonical telemetry
rate.

Do not fabricate a production telemetry rate.

If the actual source is 100 Hz, the transport must be capable of
handling it in tests and benchmark scenarios.

========================================================
METRICS
========================================================

Add stream metrics.

At minimum:

telemetry_subscribers
event_subscribers
telemetry_published
events_published
telemetry_dropped
events_dropped
telemetry_coalesced
slow_clients
authorization_denials
serialization_errors
queue_overflows
active_sessions

Per-session metrics may be included if bounded and safe.

Do not use unbounded metric labels such as arbitrary user IDs.

========================================================
OBSERVABILITY
========================================================

Use existing structlog.

Log:

subscription_created
subscription_removed
stream_error
slow_client
client_disconnected

Do NOT log every telemetry frame.

Never log:

Authorization header
JWT
API key
credentials

========================================================
ERROR HANDLING
========================================================

Reuse existing TransportErrorCode.

Possible errors:

AUTHENTICATION_REQUIRED
AUTHORIZATION_DENIED
SESSION_FORBIDDEN
INVALID_SUBSCRIPTION
STREAM_UNAVAILABLE
BACKPRESSURE_LIMIT
INTERNAL_ERROR

Do not expose internal stack traces.

========================================================
CONNECTION LIFECYCLE
========================================================

On connect:

1. authenticate
2. create connection
3. attach Principal
4. wait for subscription

Do NOT automatically subscribe to telemetry.

On subscribe:

1. validate request
2. authenticate/authorize
3. validate session
4. register subscription
5. begin delivery

On unsubscribe:

remove only requested subscription.

On disconnect:

remove all subscriptions
clear queues
detach EventBus listeners
release metrics
cancel publisher tasks

No leaked subscriptions.

========================================================
RECONNECT SEMANTICS
========================================================

Do not replay missed telemetry automatically.

After reconnect:

client must resubscribe.

This avoids pretending that WebSocket transport is a durable telemetry
recording system.

If future replay/resume support is required, leave it for a later phase.

========================================================
SNAPSHOT COMPATIBILITY
========================================================

Agent 11.5 snapshot streaming MUST continue to work.

A client may subscribe to:

SNAPSHOT + TELEMETRY + EVENT

simultaneously.

The three streams must remain independently controllable.

Telemetry must not break snapshot coalescing.

Snapshot must not consume telemetry queue capacity.

========================================================
REPLAY COMPATIBILITY
========================================================

Do not break Replay.

Replay event streaming may continue through existing EventBus paths.

Do not label replay telemetry as LIVE.

Do not silently route replay frames into LIVE subscriptions.

If the existing gateway already supports replay events, preserve them.

========================================================
CAPABILITIES
========================================================

Update transport capabilities to advertise:

telemetry subscription support
event subscription support

only when actually wired.

Do not claim a capability that is unavailable.

========================================================
FILES
========================================================

Inspect the repository first.

Prefer existing modules.

Likely implementation areas:

backend/api/websocket/
backend/api/services/
backend/api/snapshot/
shared/transport/
shared/protocols/
tests/api/websocket/
tests/transport/

Possible new module:

backend/api/telemetry/

Potential files:

service.py
publisher.py
policy.py
status.py
metrics.py
exceptions.py
__init__.py

But DO NOT create unnecessary modules if existing architecture already
provides the correct location.

========================================================
ARCHITECTURE RULES
========================================================

The following imports are forbidden from the transport telemetry
publisher unless already explicitly allowed by repository architecture:

direct ORM access
SQLAlchemy session creation
FastF1 SDK
Unity
Blender
OBS
Twitch
Kick
YouTube
external F1 APIs

The transport layer must consume existing Runtime authorities.

========================================================
TESTS
========================================================

Create:

tests/api/telemetry/

or extend the existing WebSocket tests.

Required tests:

1. telemetry subscription
2. telemetry unsubscribe
3. event subscription
4. event unsubscribe
5. session_id required
6. authenticated subscription
7. unauthenticated rejection
8. missing permission rejection
9. session scope rejection
10. session isolation
11. canonical telemetry forwarding
12. canonical event forwarding
13. source timestamp preserved
14. source sequence preserved
15. transport sequence independent
16. no synthetic telemetry
17. no synthetic events
18. interpolation metadata preserved
19. delay metadata preserved
20. LIVE-only subscription
21. replay does not leak into LIVE stream
22. multiple sessions isolated
23. multiple clients isolated
24. slow client does not block Runtime
25. bounded queue
26. telemetry overflow policy
27. event priority over telemetry
28. control priority over telemetry
29. snapshot stream remains functional
30. snapshot + telemetry + event simultaneously
31. disconnect cleanup
32. unsubscribe cleanup
33. reconnect requires resubscription
34. no missed telemetry replay on reconnect
35. metrics
36. structured audit/logging
37. no token logging
38. no unbounded queue
39. serialization failure handling
40. capability advertisement
41. REST stream status
42. architecture boundaries
43. Ruff
44. mypy

Use deterministic fake/in-memory canonical providers already used by
the project.

Do NOT require a real F1 feed for tests.

========================================================
PERFORMANCE TESTS
========================================================

Add bounded microbenchmarks for:

- telemetry serialization
- telemetry enqueue
- telemetry fanout
- multi-client fanout
- event fanout

Test at representative synthetic rates.

Do not claim production SLA.

Label measurements:

BASELINE_NOT_PRODUCTION_SLA

Do not make up a guaranteed latency figure.

========================================================
BACKPRESSURE ACCEPTANCE
========================================================

Explicitly prove:

Client A is slow
Client B is healthy

Client B continues receiving telemetry.

Runtime ingestion continues.

EventBus is not blocked.

Snapshot delivery continues.

Control commands remain responsive.

========================================================
SECURITY ACCEPTANCE
========================================================

Explicitly prove:

unauthenticated client cannot subscribe when auth is enabled.

viewer can read live telemetry.

viewer cannot control live session.

operator can perform permitted live control.

unauthorized session is rejected.

No telemetry is delivered before authorization.

========================================================
DOCUMENTATION
========================================================

Create:

docs/specifications/LiveTelemetryStreamingSpecification.md

Update:

docs/Roadmap.md
docs/Architecture.md
docs/Streaming.md
docs/Telemetry.md
docs/Replay.md
docs/specifications/README.md
backend/api/README.md

Document:

- architecture
- canonical source
- subscription protocol
- session isolation
- authentication
- authorization
- event streaming
- telemetry streaming
- sequence semantics
- ordering
- delay integration
- interpolation metadata
- backpressure
- queue policies
- reconnect semantics
- metrics
- limitations

========================================================
ROADMAP
========================================================

Mark:

Phase 11
Agent 11.6.1 — Live Telemetry Streaming
COMPLETE ✓

Do not mark 11.7 or later complete.

Do not renumber existing agents.

========================================================
ACCEPTANCE GATES
========================================================

Agent 11.6.1 is COMPLETE only if all gates pass:

GATE-01 Existing WS gateway reused
GATE-02 No second Runtime created
GATE-03 Canonical LiveSessionAdapter path reused
GATE-04 EventBus reused
GATE-05 Telemetry subscription implemented
GATE-06 Event subscription implemented
GATE-07 session_id required
GATE-08 Authentication enforced
GATE-09 Authorization enforced
GATE-10 Session scope enforced
GATE-11 Session isolation verified
GATE-12 Canonical source timestamp preserved
GATE-13 Canonical source sequence preserved
GATE-14 No synthetic telemetry
GATE-15 No synthetic events
GATE-16 Delay pipeline remains authoritative
GATE-17 Interpolation remains authoritative
GATE-18 LIVE mode isolation works
GATE-19 Replay does not leak into LIVE subscriptions
GATE-20 Multiple clients supported
GATE-21 Slow client cannot block Runtime
GATE-22 Bounded queues enforced
GATE-23 Telemetry backpressure policy implemented
GATE-24 Event priority preserved
GATE-25 Control priority preserved
GATE-26 Snapshot streaming remains functional
GATE-27 Combined subscriptions work
GATE-28 Disconnect cleanup works
GATE-29 Unsubscribe cleanup works
GATE-30 Reconnect requires resubscription
GATE-31 No automatic missed-frame replay
GATE-32 Metrics implemented
GATE-33 Safe structured logging implemented
GATE-34 No credentials/tokens logged
GATE-35 Capabilities accurately advertised
GATE-36 REST stream status remains functional
GATE-37 Performance microbenchmarks exist
GATE-38 Performance measurements labelled correctly
GATE-39 Architecture boundaries pass
GATE-40 Security regression passes
GATE-41 API/WS/transport regression passes
GATE-42 Phase 10 acceptance remains PASS
GATE-43 Ruff clean
GATE-44 Mypy clean
GATE-45 All telemetry/event streaming tests pass

========================================================
REGRESSION REQUIREMENTS
========================================================

Run all relevant existing tests.

At minimum:

- tests/api/security
- tests/api/websocket
- tests/api/commands
- tests/api/snapshot
- tests/transport
- tests/runtime
- tests/runtime/live
- tests/runtime/delay
- tests/telemetry/interpolation
- Phase 10 integration
- Phase 10 acceptance

Do not weaken or delete existing tests.

========================================================
IMPORTANT ENGINEERING RULES
========================================================

1. Inspect the repository before modifying anything.

2. Reuse existing transport contracts.

3. Reuse existing WebSocket gateway.

4. Reuse Agent 11.6 authentication/authorization.

5. Reuse LiveSessionAdapter.

6. Reuse EventBus.

7. Reuse existing bounded queue implementation.

8. Do not create a second ingestion path.

9. Do not connect directly to F1 providers.

10. Do not query the database per telemetry frame.

11. Do not implement delay in WebSocket transport.

12. Do not implement interpolation in WebSocket transport.

13. Do not synthesize telemetry.

14. Do not synthesize events.

15. Do not leak sessions between clients.

16. Do not log telemetry payloads at frame rate.

17. Do not create unbounded queues.

18. Do not replay missed telemetry after reconnect.

19. Do not claim production performance SLAs from microbenchmarks.

20. Preserve all Phase 10 behavior.

21. Preserve Agents 11.1–11.6 behavior.

22. Keep the transport layer independent of Unity/Blender/OBS.

23. Do not implement social streaming.

24. Do not implement AI commentary.

25. Do not implement prediction/latency compensation.

26. Do not implement rate limiting beyond hooks required for
future Agent 11.7.

27. Do not stop at scaffolding. Implement, integrate, test, document,
and validate the complete feature.

========================================================
FINAL REPORT
========================================================

When complete, report:

1. ACCEPTED / NOT ACCEPTED
2. Architecture
3. Canonical telemetry source
4. Event source
5. Subscription model
6. Authentication integration
7. Authorization integration
8. Session isolation
9. Sequence semantics
10. Ordering behavior
11. Delay integration
12. Interpolation integration
13. Backpressure strategy
14. Queue policies
15. Event priority
16. Snapshot compatibility
17. Replay isolation
18. Reconnect semantics
19. Metrics
20. Files created
21. Files modified
22. Test count
23. Regression test count
24. Performance benchmark results
25. Coverage
26. Ruff result
27. Mypy result
28. GATE-01…45 results
29. Documentation changes
30. Roadmap status
31. Limitations
32. Recommended next Agent

Do not claim COMPLETE unless every mandatory gate actually passes.
```

**One architectural point to preserve:** 11.6.1 should make the WebSocket transport a **consumer of canonical live telemetry**, not another telemetry-processing system. That keeps the architecture:

`F1 Feed → LiveSessionAdapter → Delay/Interpolation → Runtime → EventBus/Cache/Timeline → WebSocket → Unity/OBS/other consumers`

which is exactly the separation we want before moving deeper into the rendering and broadcast phases.

---

If you want, I can:

- Generate detailed plan to implement telemetry subscription enforcement
- List comprehensive test cases for Agent 11.6.1 telemetry and event streaming
- Create a mapping of system components showing Agent 11.6.1 data flow
