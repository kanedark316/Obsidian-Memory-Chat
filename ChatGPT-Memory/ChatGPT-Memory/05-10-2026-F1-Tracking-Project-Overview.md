---
title: F1 Tracking Project Overview
source: share
saved_at: 2026-10-05T21:03:00.209804+00:00
stable_key: 51c87fc88e93a769
tags: [chatgpt, memory]
url: "https://chatgpt.com/share/6ac3f84c-bbfc-83ed-b16e-c68019f7948f"
---

# F1 Tracking Project Overview

## User

Please read and find out the previous logs/chats @Live F1 Tracking Data and @RaceVision F1 Project and @F1 Tracking and Project. Please learn and understand the logs and then I may ask you a question.

## Assistant

The output of this plugin was redacted.

## Assistant

Yes. I’ve reviewed the retained context from the three RaceVision/F1 project threads and have the project state loaded for continuation.

### What I have understood

**Project:** RaceVision — live F1 telemetry → unified runtime → 3D rendering → broadcast/streaming → replay/analytics.

**Completed foundation:**
- Repository / enterprise architecture
- SRS, SAS, DDS and API/protocol specifications
- PostgreSQL foundation and runtime
- SQLAlchemy ORM + repositories + Unit of Work + query objects
- Configuration/environment layer
- Telemetry domain models and persistence
- Unified runtime architecture

**Phase 10 is fully accepted.**
- Live telemetry adapter
- Historical/FastF1 provider
- Replay runtime
- Replay controller/synchronization/cache
- Timeline and seeking
- Recording/playback validation
- Live/replay operating modes
- Delay buffer
- Gap detection/interpolation
- Race state snapshots
- Phase 10 integration
- Full acceptance testing

The important acceptance result I have is:

**24/24 mandatory gates PASS, 0 warnings, 0 skipped gates.**  
**805 tests passed** for the relevant runtime/interpolation validation, with the acceptance package at about **85% coverage**, and Ruff/mypy clean.

### Current architecture I understand

The central runtime authorities are:

`CacheManager`  
`TimelineService`  
`Event Bus`  
`LiveRuntime`

with the live/replay abstraction based on:

`SessionOperatingMode` ↔ `TimelineMode`

Historical telemetry remains isolated.

The intended architecture keeps telemetry/runtime independent from downstream consumers such as:

- Web/API clients
- Unity
- Blender/assets
- OBS/broadcast overlays
- Twitch/Kick/YouTube
- Camera/director systems
- AI commentary
- Analytics/prediction

### Phase 11

I also have the Phase 11 progression in context.

The recent work reached **Agent 11.6 — Authentication & Authorization**, which was explicitly **ACCEPTED**.

The key architectural decision was:

**Client → Provider → Principal → AuthorizationPolicy → REST/WS → existing services/dispatchers**

with the important constraint that the **runtime remains identity-unaware**.

And the next item you were moving into was:

**Agent 11.6.1 — Live Telemetry Streaming**

with the goal of streaming **live canonical telemetry/events**, rather than creating a second telemetry/runtime path.

I also remember your preference from that work: when you ask for implementation-agent commands, you want them **ready to copy/paste directly into Cursor**, preferably as a single clean command block.

I’m therefore treating the three previous conversations as the continuing RaceVision project history rather than starting from scratch. memcite

Go ahead with your question.

## User

I have the following Agents in this Phase
Phase 11 — Transport & Live Streaming Runtime
Agent	Component	Purpose



11.7	Replay Streaming	Stream replay state/events through the same transport
11.8	Subscription System	Clients subscribe to telemetry, snapshots, events, replay, etc.
11.9	Connection & Session Management	Client lifecycle, reconnect, heartbeat, session isolation
11.10	Backpressure & Rate Control	Prevent slow clients from affecting Runtime
11.11	Transport Authentication & Authorization	Secure API/WS access boundary
11.12	Transport Observability	Metrics, health, connection statistics, errors
11.13	Transport Integration Testing	End-to-end REST/WS tests against Phase 10
11.14	Live Streaming Acceptance	Performance, concurrency, disconnect/reconnect testing
11.15	Phase 11 Acceptance	Final acceptance gate

## Assistant

Yes — this fits the Phase 11 architecture I have in context.

Given that **11.6 Authentication & Authorization** and **11.6.1 Live Telemetry Streaming** are already accepted/in progress as established context, the remaining sequence is coherent:

| Agent | Component | Primary responsibility |
|---|---|---|
| **11.7** | Replay Streaming | Stream replay state/events through the **same transport path** |
| **11.8** | Subscription System | Client subscriptions for telemetry, snapshots, events, replay, etc. |
| **11.9** | Connection & Session Management | Lifecycle, reconnect, heartbeat, session isolation |
| **11.10** | Backpressure & Rate Control | Protect Runtime from slow/overloaded clients |
| **11.11** | Transport Authentication & Authorization | Secure REST/WS transport boundary |
| **11.12** | Transport Observability | Metrics, health, connection statistics, errors |
| **11.13** | Transport Integration Testing | End-to-end REST/WS validation against Phase 10 |
| **11.14** | Live Streaming Acceptance | Performance, concurrency, disconnect/reconnect testing |
| **11.15** | Phase 11 Acceptance | Final Phase 11 acceptance gate |

### The architectural dependency I would preserve

The important principle is that **Phase 11 must not become another runtime**.

It should remain approximately:

```text
                    ┌──────────────────────────┐
                    │      Phase 10 Runtime    │
                    │                          │
                    │ CacheManager             │
                    │ TimelineService          │
                    │ Event Bus                 │
                    │ LiveRuntime               │
                    │ Replay Runtime            │
                    └────────────┬─────────────┘
                                 │
                         canonical state/events
                                 │
                    ┌────────────▼─────────────┐
                    │     Phase 11 Transport   │
                    │                          │
                    │ 11.7 Replay Streaming    │
                    │ 11.8 Subscriptions       │
                    │ 11.9 Connections          │
                    │ 11.10 Backpressure       │
                    │ 11.11 Auth/AuthZ         │
                    │ 11.12 Observability      │
                    └────────────┬─────────────┘
                                 │
                    ┌────────────▼─────────────┐
                    │       REST / WebSocket   │
                    └────────────┬─────────────┘
                                 │
             ┌───────────────────┼───────────────────┐
             ▼                   ▼                   ▼
          Browser             Unity              OBS/etc.
```

That means:

- **Live and replay use the same transport architecture.**
- Clients consume **canonical runtime state/events**.
- Transport does **not** invent telemetry.
- Transport does **not** modify runtime state.
- Authentication/authorization stays at the boundary.
- Slow clients are isolated through backpressure/rate control.
- Connection state belongs to transport, not the core runtime.
- Observability measures transport without contaminating domain/runtime logic.
- Phase 10 remains the authoritative source of live/replay truth.

### One thing I would watch closely

There is a potential naming/ownership overlap between **11.6** and **11.11**.

I would interpret them as:

**11.6 — Principal/Auth foundation**
> Establish identity, principal, policy and authorization primitives at the transport boundary.

**11.11 — Transport security integration**
> Apply those primitives consistently to REST/WS endpoints, subscription authorization, connection/session behavior and protected transport operations.

That avoids implementing authentication twice.

Likewise, **11.7 should come before 11.8**, because subscriptions should be able to treat live telemetry and replay streams as transport-level stream types rather than inventing separate mechanisms.

So the logical progression becomes:

**11.6 → 11.6.1 → 11.7 → 11.8 → 11.9 → 11.10 → 11.11 → 11.12 → 11.13 → 11.14 → 11.15**

I have this Phase 11 structure in context now. memcite

## User

I also have the reply from cursor from a completed agent;

**ACCEPTED** — Agent **11.6.1 Live Telemetry Streaming** is complete. Authenticated clients can subscribe to LIVE telemetry and events on the existing `WS /api/v1/ws` path via EventBus → `LiveTelemetryStreamPublisher`, without a second Runtime or transport-side delay/interpolation.

### Architecture

`LiveProvider → LiveSessionAdapter (+ delay/interp) → Runtime/EventBus → LiveTelemetryStreamPublisher → WebSocketConnectionManager (bounded queues) → client`

### Summary

| Item                       | Detail                                                                       |
| -------------------------- | ---------------------------------------------------------------------------- |
| Canonical telemetry source | `LiveSessionAdapter` → enriched `TelemetryNormalized` on EventBus            |
| Event source               | Existing EventBus domain events (no synthesis in WS)                         |
| Subscriptions              | Independent `TELEMETRY` / `EVENTS` / `SNAPSHOT`; `session_id` required       |
| AuthN / AuthZ              | Agent 11.6; TELEMETRY/EVENTS need `transport:subscribe` + `live:read`        |
| Session isolation          | Filter before enqueue; principal session scope re-checked on delivery        |
| Sequences                  | Envelope = transport; payload = source (never overwritten)                   |
| Ordering                   | Canonical runtime order; no reorder/extrapolate/missed-frame replay          |
| Delay / interpolation      | Adapter pipeline authoritative; metadata preserved                           |
| Backpressure               | Bounded queues; default `DROP_OLDEST`; coalesce off by default               |
| Priority                   | CONTROL > EVENT > SNAPSHOT > TELEMETRY                                       |
| Snapshot / Replay          | Snapshot unchanged; REPLAY mode/events do not leak into LIVE subs            |
| Reconnect                  | Resubscribe required; no missed-frame replay                                 |
| Metrics                    | Subscribers, published/dropped/coalesced, slow\_clients, authz denials, etc. |

### Files

**Created:** `backend/api/telemetry/*`, `tests/api/telemetry/*`, `docs/specifications/LiveTelemetryStreamingSpecification.md`
**Modified:** adapter EventBus enrich path, WS manager/queue, security mapping, capabilities/status routes, app wiring, Roadmap + Architecture/Streaming/Telemetry/Replay/API docs

### Tests & quality

| Suite                                                                 | Result                                                                                    |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `tests/api/telemetry`                                                 | **29 passed**                                                                             |
| Phase 11 regressions (security/ws/commands/snapshot/transport + tele) | **257 passed**                                                                            |
| Phase 10 integration + acceptance                                     | **26 passed**                                                                             |
| `tests/api/telemetry` + `tests/runtime`                               | **797 passed**                                                                            |
| Ruff / mypy (touched packages)                                        | **clean**                                                                                 |
| Benchmarks                                                            | `serialization_hz~=33371`, `fanout_3client_hz~=6244` — **BASELINE\_NOT\_PRODUCTION\_SLA** |

### GATE-01…45

All **PASS** (incl. GATE-42 Phase 10 acceptance, GATE-43/44 ruff/mypy, GATE-45 telemetry tests).

### Roadmap

**11.6.1 COMPLETE ✓** — **11.7** left open (rate limiting / hardening).

### Limitations

No durable resume after reconnect; optional max-Hz is soft throttle only; no Agent 11.7 rate limiting.

### Recommended next

**Agent 11.7 — Rate limiting / brute-force protections / hardening**

## Assistant

Yes — this additional Cursor report materially clarifies the **actual implemented state** of Phase 11, and I’ll use it as the authoritative continuation point.

There is one important correction to the earlier Phase 11 interpretation:

### Current RaceVision state

**Agent 11.6.1 — Live Telemetry Streaming is ACCEPTED and COMPLETE.**

The implemented flow is:

```text
LiveProvider
    ↓
LiveSessionAdapter
    ↓
Runtime / EventBus
    ↓
LiveTelemetryStreamPublisher
    ↓
WebSocketConnectionManager
    ↓
bounded client queues
    ↓
WebSocket client
```

Crucially, this preserves the Phase 10 authority model:

- No second runtime
- No second telemetry pipeline
- No transport-side interpolation
- No transport-side delay
- No synthetic WS events
- EventBus remains authoritative
- `LiveSessionAdapter` remains authoritative for delay/interpolation metadata
- Transport only distributes canonical runtime output

### What 11.6.1 actually provides

The implementation already has:

**Subscriptions**
- `TELEMETRY`
- `EVENTS`
- `SNAPSHOT`
- `session_id` required

**Security**
- Agent 11.6 authentication/authorization
- `transport:subscribe`
- `live:read`
- Session-scope checks before enqueue
- Principal scope rechecked during delivery

**Isolation**
- LIVE subscriptions cannot receive REPLAY state/events
- Session isolation is enforced before queueing

**Ordering**
- Runtime/canonical ordering preserved
- No transport reordering
- No extrapolation
- No missed-frame replay

**Backpressure foundation**
- Bounded queues already exist
- Default `DROP_OLDEST`
- Coalescing disabled by default
- Priority:

```text
CONTROL > EVENT > SNAPSHOT > TELEMETRY
```

This is particularly important for **11.10**, because we should extend the existing mechanism rather than replace it.

### Existing reconnect semantics

Current behavior is intentionally:

```text
disconnect
   ↓
reconnect
   ↓
authenticate
   ↓
resubscribe
   ↓
receive current stream
```

There is **no durable resume / missed-frame replay**.

That is explicitly a limitation rather than an accidental gap.

### Current test evidence

The reported acceptance evidence is strong:

| Validation | Result |
|---|---:|
| Telemetry tests | **29 passed** |
| Phase 11 regression suite | **257 passed** |
| Phase 10 integration/acceptance | **26 passed** |
| Telemetry + runtime | **797 passed** |
| Ruff | **Clean** |
| mypy | **Clean** |
| GATE-01…45 | **ALL PASS** |

The benchmark numbers:

```text
serialization_hz ≈ 33,371
fanout_3client_hz ≈ 6,244
```

are correctly marked:

**BASELINE_NOT_PRODUCTION_SLA**

So we should **not** treat those numbers as Phase 11 performance guarantees.

---

## Important change to the Phase 11 plan

Cursor's recommendation says:

> **Agent 11.7 — Rate limiting / brute-force protections / hardening**

But your original Phase 11 table defines:

> **11.7 — Replay Streaming**

Those are **not the same scope**.

Based on the accepted 11.6.1 report, I would **not silently rename Agent 11.7**.

Instead, we need to determine whether Cursor's "11.7 Rate limiting / brute-force protections / hardening" is:

1. a **scope change** to your Phase 11 plan,
2. an additional **11.6.2 / 11.6.x hardening agent**, or
3. something that belongs under **11.10 Backpressure & Rate Control** and should therefore *not* become 11.7.

Given the architecture you originally established, I strongly favor **option 3** for rate limiting, while keeping:

**11.7 = Replay Streaming**

because replay streaming is a substantive missing transport capability, whereas rate limiting/backpressure already has a clearly defined home in **11.10**.

Also, **11.11 Transport Authentication & Authorization** should not redo 11.6's AuthN/AuthZ foundation. It should integrate/harden the existing boundary controls.

So my current authoritative roadmap is:

```text
11.6       Authentication & Authorization       ✓ ACCEPTED
11.6.1     Live Telemetry Streaming             ✓ ACCEPTED

11.7       Replay Streaming                     ← NEXT
11.8       Subscription System
11.9       Connection & Session Management
11.10      Backpressure & Rate Control
11.11      Transport Authentication & Authorization
11.12      Transport Observability
11.13      Transport Integration Testing
11.14      Live Streaming Acceptance
11.15      Phase 11 Acceptance
```

And I will carry forward **all of the concrete 11.6.1 implementation constraints** you just provided when reasoning about the next agents. memcite

## User

Cursor Recommendations, this needs to be added into the Agents list and would there be any others that needs to be added onto the list 

### Recommended next

**Agent 11.7 — Rate limiting / brute-force protections / hardening**

## Assistant

The output of this plugin was redacted.

## Assistant

Yes. **Cursor's recommendation should be added**, but I would **not simply replace Replay Streaming with it**. The 11.6.1 report exposed real production-hardening work that deserves an explicit agent.

I would revise Phase 11 rather than squeeze the work into existing agents.

## Recommended Phase 11 Agent List

| Agent | Component | Purpose | Status |
|---|---|---|---|
| **11.7** | **Rate Limiting, Abuse Protection & Transport Hardening** | Rate limits, brute-force protection, WS/API abuse controls, connection-attempt limits, subscription abuse, payload/message limits, hardening | **NEW — NEXT** |
| **11.8** | **Replay Streaming** | Stream replay state/events through the same transport architecture | Planned |
| **11.9** | **Subscription System** | Unified subscriptions for telemetry, snapshots, events and replay | Planned |
| **11.10** | **Connection & Session Management** | Client lifecycle, reconnect, heartbeat, session isolation | Planned |
| **11.11** | **Backpressure & Rate Control** | Protect Runtime from slow clients; queue policy, delivery throttling, fairness | Planned |
| **11.12** | **Transport Authentication & Authorization** | Integrate/harden existing 11.6 AuthN/AuthZ across REST/WS operations | Planned |
| **11.13** | **Transport Observability** | Metrics, health, connection statistics, drops, throttling, auth failures, errors | Planned |
| **11.14** | **Transport Integration Testing** | End-to-end REST/WS testing against Phase 10 + live/replay | Planned |
| **11.15** | **Live Streaming Acceptance** | Performance, concurrency, rate limits, disconnect/reconnect, abuse testing | Planned |
| **11.16** | **Phase 11 Acceptance** | Final Phase 11 acceptance gates and regression validation | Planned |

I recommend **adding 11.16 rather than compressing acceptance into 11.15**. This gives us a clean distinction between:

**11.15 = prove the streaming runtime works under production-like conditions**

and

**11.16 = formally accept the entire Phase 11 architecture.**

---

# Why 11.7 is necessary

The 11.6.1 report explicitly identified:

> No durable resume after reconnect  
> optional max-Hz is soft throttle only  
> no Agent 11.7 rate limiting

Those are important.

11.6.1 already has **bounded queues**, but bounded queues are not the same thing as **admission/rate control**.

For example:

```text
Client
  │
  ├── 1 WS connection
  │
  ├── 500 subscription requests
  │
  ├── excessive reconnect attempts
  │
  ├── huge messages
  │
  └── excessive command/API requests
             │
             ▼
       Transport Boundary
             │
       ┌─────┴─────┐
       │ 11.7      │
       │ Rate/Abuse│
       └─────┬─────┘
             │
       permitted traffic
             ▼
       Phase 11 runtime
```

This should happen **before traffic reaches expensive subscription/session/runtime operations**.

---

# But 11.7 and 11.11 must not overlap

This distinction is important.

### 11.7 — Rate Limiting / Abuse Protection

Controls **how much** a client can do.

Examples:

- authentication attempt rate
- connection establishment rate
- reconnect rate
- subscription creation rate
- subscription count limits
- API request rate
- WS message rate
- payload size limits
- per-principal limits
- per-session limits
- per-IP/network boundary where appropriate
- abuse detection
- temporary throttling/blocking
- rate-limit headers/status semantics
- WS close/error behavior for violations

### 11.11 — Backpressure & Rate Control

Controls **how streaming data is delivered** once a client is legitimately subscribed.

Examples:

```text
Runtime
   │
   ├── 1000 telemetry frames/sec
   │
   ▼
Transport
   │
   ├── Client A: fast
   │      → receives normally
   │
   ├── Client B: slow
   │      → bounded queue
   │      → DROP_OLDEST
   │
   └── Client C: overloaded
          → delivery throttling/coalescing
```

So:

**11.7 = admission / abuse protection**

**11.11 = stream delivery protection**

That separation is architecturally clean.

---

# One other issue exposed by 11.6.1

The report says:

> No durable resume after reconnect

I **would not create a separate agent for this yet**.

It belongs primarily in **11.10 Connection & Session Management**.

11.10 should explicitly define:

```text
Disconnect
   ↓
Connection state lost
   ↓
Reconnect
   ↓
Re-authenticate
   ↓
Re-establish session
   ↓
Resubscribe
   ↓
Resume from current canonical state
```

For Phase 11, the existing decision can remain:

**No historical missed-frame replay on reconnect.**

If later we want:

```text
last_sequence = 183920
        ↓
reconnect
        ↓
resume from 183921
```

that is a substantially larger durable-stream/resume feature and should be treated as a future capability rather than quietly introducing it into 11.10.

---

# I would also add these explicit requirements

There are three areas I would make sure the agents cover, but **I would not create separate agents for them**.

### 1. Message/payload limits → 11.7

Prevent clients from abusing the transport with oversized requests/messages.

### 2. Subscription quotas → 11.7 + 11.9

For example:

```text
max subscriptions / principal
max subscriptions / connection
max sessions / principal
max telemetry streams / session
```

Exact limits should be configuration-driven rather than hardcoded.

### 3. Slow-client lifecycle policy → 11.11

11.6.1 already has bounded queues.

11.11 should define what happens when a client remains chronically slow:

```text
normal
  ↓
queue pressure
  ↓
DROP_OLDEST / throttling
  ↓
slow-client metric
  ↓
persistent overload
  ↓
transport protection
  ↓
disconnect if policy threshold exceeded
```

That prevents one permanently unhealthy client from consuming resources indefinitely.

---

# Final recommended Phase 11

I would therefore lock the roadmap as:

```text
PHASE 11 — TRANSPORT & LIVE STREAMING RUNTIME

11.1  Transport Architecture                         ✓
11.2  REST Transport                                 ✓
11.3  WebSocket Transport                            ✓
11.4  Transport Contracts / Protocols                ✓
11.5  Transport Integration                          ✓
11.6  Authentication & Authorization                 ✓
11.6.1 Live Telemetry Streaming                      ✓ ACCEPTED

11.7  Rate Limiting, Abuse Protection & Hardening    ← NEXT
11.8  Replay Streaming
11.9  Subscription System
11.10 Connection & Session Management
11.11 Backpressure & Rate Control
11.12 Transport Authentication & Authorization
11.13 Transport Observability
11.14 Transport Integration Testing
11.15 Live Streaming Acceptance
11.16 Phase 11 Acceptance
```

### My recommendation

**Do not add a bunch of extra agents beyond this.**

The architecture already has good separation. The key newly identified gap from 11.6.1 is **11.7 rate limiting/abuse protection/hardening**. The other concerns exposed by the Cursor report can be cleanly absorbed into **11.9–11.11**.

Most importantly, **Replay Streaming remains in the roadmap**. I would not sacrifice 11.8 just because Cursor's next recommendation called its hardening work "11.7."

This gives us a much cleaner Phase 11 completion boundary and avoids creating technical debt through overlapping responsibilities. memcite

## User

Could you add anything that cursor recommends as 11. Number . Number

## Assistant

Yes. If you mean **“take every additional recommendation Cursor has surfaced and turn each into a numbered `11.x` Agent”**, I would do that — but only where it represents a distinct architectural responsibility.

From the 11.6.1 Cursor report, I would add these explicitly:

| Agent | Component | Why it deserves its own Agent |
|---|---|---|
| **11.7** | **Rate Limiting & Abuse Protection** | Cursor explicitly recommended it; covers API/WS rate limits, brute-force protection and abuse controls |
| **11.8** | **Transport Hardening** | Payload/message limits, connection-attempt protection, subscription abuse, security hardening and defensive boundary controls |
| **11.9** | **Replay Streaming** | Missing transport capability; replay must use the same transport architecture as live |
| **11.10** | **Subscription System** | Unified subscription lifecycle for telemetry/events/snapshots/replay |
| **11.11** | **Connection & Session Management** | Connection lifecycle, reconnect, heartbeat, session isolation and resubscription |
| **11.12** | **Backpressure & Rate Control** | Protect Runtime from slow clients and control streaming delivery |
| **11.13** | **Transport Authentication & Authorization** | Apply the existing 11.6 security model consistently across transport operations |
| **11.14** | **Transport Observability** | Connection, subscription, drop, throttle, auth-denial and transport health metrics |
| **11.15** | **Transport Integration Testing** | REST/WS + Phase 10 integration and cross-mode validation |
| **11.16** | **Live Streaming Acceptance** | Concurrency, performance, reconnect, overload and failure testing |
| **11.17** | **Phase 11 Acceptance** | Final formal acceptance and regression gates |

### I would also explicitly capture these Cursor findings

They don't necessarily need separate agents:

**Durable reconnect/resume**
→ **11.11 Connection & Session Management**

Current decision remains:

```text
Reconnect
   ↓
Re-authenticate
   ↓
Re-establish session
   ↓
Resubscribe
   ↓
Continue from current canonical state
```

No missed-frame replay unless we deliberately add that capability later.

**Slow-client handling**
→ **11.12 Backpressure & Rate Control**

The existing:

```text
bounded queue
DROP_OLDEST
priority ordering
slow-client metrics
```

should be extended rather than replaced.

**Subscription quotas**
→ **11.7 + 11.10**

**Payload/message limits**
→ **11.8 Transport Hardening**

**Brute-force protection**
→ **11.7**

**Transport metrics**
→ **11.14**

**Performance benchmarks**
→ **11.16**

The existing `serialization_hz ≈ 33,371` and `fanout_3client_hz ≈ 6,244` remain **baselines, not production SLAs**.

### One important architectural benefit

This gives us a very clean boundary:

```text
11.7  HOW MUCH traffic is allowed?
        ↓
11.8  Is the traffic safe/valid?
        ↓
11.9  Can replay be transported?
        ↓
11.10 What streams does the client want?
        ↓
11.11 Who is connected and for which session?
        ↓
11.12 How do we protect Runtime from delivery pressure?
        ↓
11.13 Who is allowed to perform each operation?
        ↓
11.14 What is happening operationally?
        ↓
11.15 Does it integrate correctly?
        ↓
11.16 Does it survive production-like conditions?
        ↓
11.17 Is Phase 11 ACCEPTED?
```

**That is the Phase 11 list I would lock in.**

I would **not add further 11.x agents** at this point. The remaining concerns from the 11.6.1 report have a clear home in these 11 agents, without creating unnecessary fragmentation.

## User

Please give commands for Agent 11.6.2	Rate Limiting & Abuse Protection ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. Since **11.6.1 is already ACCEPTED**, Agent **11.6.2** should be an incremental hardening agent: it must **extend the existing transport boundary**, not introduce another rate-limiting system or alter the Phase 10 runtime.

Copy/paste this entire block into Cursor:

```text
You are implementing RaceVision Agent 11.6.2 — Rate Limiting & Abuse Protection.

=========================================================
RACEVISION — AGENT 11.6.2
RATE LIMITING & ABUSE PROTECTION
=========================================================

STATUS
------

Agent 11.6.1 Live Telemetry Streaming is ACCEPTED.

Do NOT redesign or regress 11.6 / 11.6.1.

This agent is a transport-boundary hardening increment.

=========================================================
OBJECTIVE
=========================================================

Implement production-grade rate limiting and abuse protection
for the existing RaceVision REST + WebSocket transport boundary.

The goal is to prevent abusive or accidentally overloaded clients
from consuming unbounded transport resources while preserving the
existing Phase 10 Runtime and 11.6.1 Live Telemetry Streaming
architecture.

Transport protection MUST occur before expensive downstream work
where practical.

The Runtime remains completely identity-unaware and rate-limit-aware
logic MUST NOT be introduced into:

- LiveRuntime
- ReplayRuntime
- CacheManager
- TimelineService
- EventBus
- LiveSessionAdapter
- Replay services
- domain services
- telemetry providers

=========================================================
AUTHORITATIVE ARCHITECTURE
=========================================================

Existing architecture:

Client
  ↓
Provider / Transport Boundary
  ↓
Principal
  ↓
AuthorizationPolicy
  ↓
REST / WebSocket
  ↓
existing services / dispatchers
  ↓
Phase 10 Runtime

Live streaming:

LiveProvider
  ↓
LiveSessionAdapter
  ↓
Runtime / EventBus
  ↓
LiveTelemetryStreamPublisher
  ↓
WebSocketConnectionManager
  ↓
bounded client queues
  ↓
WebSocket client

Rate limiting MUST remain a transport concern.

Do NOT create a second Runtime.
Do NOT create a second EventBus.
Do NOT create a second telemetry pipeline.
Do NOT add rate limiting to domain/runtime code.

=========================================================
EXISTING 11.6.1 CONTRACTS THAT MUST BE PRESERVED
=========================================================

Preserve all accepted 11.6.1 behavior:

- authenticated clients subscribe to LIVE telemetry/events
- existing WS /api/v1/ws path
- EventBus remains canonical event source
- LiveSessionAdapter remains canonical live telemetry source
- TELEMETRY / EVENTS / SNAPSHOT subscriptions remain independent
- session_id remains required where already required
- transport:subscribe + live:read authorization remains enforced
- session isolation remains enforced
- principal scope is rechecked at delivery
- transport envelope sequences are not used to overwrite source sequences
- canonical runtime ordering remains unchanged
- no transport interpolation
- no transport extrapolation
- no transport-side delay
- adapter delay/interpolation remains authoritative
- bounded queues remain in place
- DROP_OLDEST remains the default queue policy
- CONTROL > EVENT > SNAPSHOT > TELEMETRY priority remains unchanged
- LIVE subscriptions cannot receive REPLAY state/events
- reconnect requires resubscription
- no durable missed-frame replay is introduced

Do not change these contracts unless absolutely required for this
agent, and if a change is required, document it explicitly and add
regression tests.

=========================================================
SCOPE
=========================================================

Implement rate limiting / abuse protection for:

1. REST/API request admission
2. WebSocket connection establishment
3. WebSocket reconnect attempts
4. WebSocket inbound message rate
5. Subscription creation/update attempts
6. Subscription count limits
7. Per-principal transport usage
8. Per-session transport usage
9. Payload/message size limits where applicable
10. Authentication-related abuse protection
11. Authorization-related abuse amplification
12. Excessive connection churn
13. Excessive subscription churn
14. Configurable transport quotas
15. Observable rate-limit decisions

Do NOT implement streaming backpressure here.

Streaming delivery protection belongs to the future
Agent 11.11 Backpressure & Rate Control.

This agent controls ADMISSION and ABUSE.

Agent 11.11 will control STREAM DELIVERY.

=========================================================
RATE-LIMITING MODEL
=========================================================

Implement a reusable transport rate-limiting abstraction.

The implementation MUST support a clear policy boundary such as:

RateLimitPolicy
RateLimitDecision
RateLimitKey
RateLimitScope
RateLimitResult

Use the existing project architecture and naming conventions where
equivalent abstractions already exist.

Do not introduce unnecessary third-party infrastructure.

Prefer a small deterministic in-process implementation unless the
repository already has a distributed limiter abstraction.

The implementation MUST be replaceable with a distributed backend
later without changing endpoint/service contracts.

=========================================================
RATE-LIMIT SCOPES
=========================================================

Support appropriate scopes for:

- IP / network-origin where available
- principal
- authenticated session
- WebSocket connection
- endpoint / operation
- subscription operation

Do not rely exclusively on IP address because authenticated users
may share NAT addresses.

Do not rely exclusively on principal because unauthenticated
connection attempts must also be protected.

The effective key should be composable.

Examples:

transport:rest:{principal}:{operation}
transport:ws:connect:{origin}
transport:ws:message:{principal}:{connection}
transport:subscription:{principal}:{operation}
transport:subscription:{session}:{operation}

Use canonical project identifiers and existing Principal/session
types where available.

=========================================================
REQUIRED LIMIT CATEGORIES
=========================================================

Implement configurable limits for at least:

A. REST REQUESTS

- requests per principal / operation
- requests per origin where appropriate
- burst allowance

B. WS CONNECTIONS

- connection attempts per origin
- connection attempts per principal
- concurrent connections per principal
- reconnect attempts within a window

C. WS MESSAGES

- inbound messages per connection
- inbound messages per principal
- burst allowance

D. SUBSCRIPTIONS

- subscription create operations
- subscription removal/replacement churn
- maximum active subscriptions per connection
- maximum active subscriptions per principal
- maximum active subscriptions per session where appropriate

E. PAYLOAD SIZE

- maximum inbound WebSocket message size
- maximum subscription request size where applicable

F. AUTHENTICATION ABUSE

- failed authentication attempts
- repeated authentication attempts
- repeated invalid credentials/token attempts

G. AUTHORIZATION ABUSE

- excessive unauthorized operation attempts
- repeated forbidden subscription attempts

Do not leak sensitive information through rate-limit error messages.

=========================================================
ALGORITHM
=========================================================

Choose an algorithm appropriate to the existing architecture.

A token bucket or equivalent bounded burst/rate model is preferred.

Requirements:

- deterministic
- monotonic-clock based
- thread/async safe
- bounded memory
- configurable
- testable
- no wall-clock dependence for enforcement
- no blocking sleeps in request handlers
- no unbounded state growth

Expired limiter state MUST be reclaimable.

Do not create a memory leak by retaining every historical client,
IP, principal, session, or connection forever.

=========================================================
DECISION CONTRACT
=========================================================

A rate-limit decision should clearly communicate internally:

- allowed / denied
- limit
- remaining where meaningful
- retry-after where meaningful
- policy identifier
- scope
- reason/category

Do not expose internal implementation details to clients.

REST responses should use the project's existing error/response
contract.

When appropriate, use HTTP 429 Too Many Requests.

Include Retry-After where the existing API conventions permit it.

WebSocket violations MUST use the project's existing WS error/
close semantics.

Do not invent arbitrary close codes if the project already has a
transport error model.

=========================================================
WEBSOCKET BEHAVIOR
=========================================================

Protect:

1. initial connection
2. authentication
3. authentication retry
4. reconnect
5. inbound messages
6. subscription requests
7. subscription churn

A rate-limit violation MUST NOT block the entire Runtime.

A malicious client must be isolated from other clients.

Do not perform expensive downstream processing before rate-limit
admission when practical.

For a client exceeding an inbound message limit:

- reject/throttle the offending operation according to policy
- record the violation
- avoid Runtime/EventBus impact
- disconnect only when policy explicitly requires it

Do NOT disconnect clients merely because they are receiving lots of
canonical telemetry.

Receiving-stream protection belongs to Agent 11.11.

=========================================================
AUTHENTICATION / AUTHORIZATION INTERACTION
=========================================================

Rate limiting MUST cooperate with Agent 11.6.

Do not replace:

- Principal
- AuthorizationPolicy
- transport:subscribe
- live:read
- existing authentication

Correct conceptual order:

Connection/request
  ↓
basic transport admission protection
  ↓
authentication
  ↓
Principal
  ↓
authorization
  ↓
operation-specific rate limit where applicable
  ↓
existing REST/WS service
  ↓
Runtime

For unauthenticated requests, only identity-independent controls
may be used.

For authenticated clients, principal-scoped limits may be applied.

Do not allow a client to bypass principal limits simply by opening
multiple WebSocket connections.

=========================================================
CONFIGURATION
=========================================================

All limits MUST be configuration-driven.

Do not hard-code production limits inside handlers.

Use the project's existing configuration/settings system.

Create a coherent configuration namespace, for example:

transport.rate_limit.enabled
transport.rate_limit.rest.*
transport.rate_limit.websocket.*
transport.rate_limit.subscription.*
transport.rate_limit.authentication.*
transport.rate_limit.authorization.*
transport.rate_limit.payload.*

Follow existing RaceVision configuration naming conventions instead
of blindly creating these exact names if an established convention
already exists.

Provide safe development/test defaults.

The limiter must support:

- enabled/disabled
- per-policy rate
- burst
- window/interval where applicable
- max concurrent resources
- payload limits
- cleanup configuration

Configuration MUST be validated.

Invalid configuration must fail clearly rather than silently
falling back to unsafe values.

=========================================================
FAIL-SAFE BEHAVIOR
=========================================================

Decide and document behavior if the limiter encounters an internal
error.

Do not allow an internal limiter exception to crash:

- WebSocket manager
- REST application
- Runtime
- EventBus

The implementation must have explicit fail-open/fail-closed
semantics appropriate to each control.

Security-sensitive authentication-abuse protection should default
to the safer behavior where practical.

Do not hide limiter failures.

Emit structured logs/metrics for them.

=========================================================
OBSERVABILITY
=========================================================

Add transport-level observability for:

- rate-limit checks
- allowed requests
- denied requests
- throttled requests
- policy name
- scope/category
- authentication abuse denials
- authorization abuse denials
- WS connection denials
- reconnect denials
- subscription denials
- payload-size violations
- active limiter entries if practical
- limiter errors

Do not log:

- passwords
- tokens
- authorization headers
- secrets
- full sensitive payloads

Use existing logging/metrics conventions.

Agent 11.12/11.13 observability may later expand these metrics,
but 11.6.2 MUST expose enough information to diagnose rate-limit
behavior.

=========================================================
FAIRNESS / ISOLATION
=========================================================

A single abusive client MUST NOT consume all limiter memory or
processing capacity.

A single principal MUST NOT bypass limits by creating many
connections.

A single connection MUST NOT bypass principal limits.

One client's rate-limit state MUST NOT affect unrelated principals.

Do not globally throttle all users because one client is abusive
unless a specific configured global protection explicitly requires
it.

=========================================================
TEST REQUIREMENTS
=========================================================

Add focused tests covering at minimum:

1. limiter allows traffic under limit
2. limiter denies traffic above limit
3. burst allowance works
4. retry-after calculation is deterministic
5. expired state is reclaimed
6. disabled limiter permits traffic
7. configuration validation
8. REST 429 behavior
9. WebSocket connection rate limiting
10. WebSocket reconnect rate limiting
11. WS inbound message rate limiting
12. subscription creation rate limiting
13. subscription count limits
14. principal limits
15. connection limits
16. payload-size enforcement
17. authentication brute-force protection
18. authorization abuse protection
19. multiple connections cannot bypass principal limits
20. one principal cannot affect another
21. limiter errors do not crash Runtime
22. no EventBus events are generated by the limiter
23. no Runtime state is modified by the limiter
24. 11.6.1 live telemetry streaming remains unchanged
25. existing authentication tests remain green
26. existing authorization tests remain green
27. existing WebSocket tests remain green
28. existing Phase 10 tests remain green

Add concurrency tests for the limiter itself.

Use deterministic clocks/time providers where required for tests.

Do not use arbitrary long sleeps in tests.

=========================================================
SECURITY TESTS
=========================================================

Explicitly test:

- repeated failed authentication
- rapid reconnect loops
- connection flooding
- subscription flooding
- message flooding
- oversized WS messages
- unauthorized subscription flooding
- multiple connections using one principal
- multiple principals sharing one origin/IP
- limiter state cleanup
- attempts to bypass a limit by changing connection/session IDs

Do not implement offensive exploit tooling.

Tests should remain local, deterministic and safe.

=========================================================
PERFORMANCE
=========================================================

The rate limiter is on the transport hot path.

Keep enforcement lightweight.

Avoid:

- database queries per rate-limit check
- network calls per rate-limit check
- blocking locks
- excessive allocations
- unbounded dictionaries
- serialization solely for limiter decisions

Benchmark where useful.

Do not claim production SLA from benchmarks.

Record benchmarks only as engineering baselines.

=========================================================
DOCUMENTATION
=========================================================

Create/update the appropriate documentation.

At minimum document:

- purpose
- architecture
- rate-limit scopes
- policy categories
- configuration
- enforcement order
- REST behavior
- WebSocket behavior
- subscription limits
- payload limits
- authentication abuse protection
- authorization abuse protection
- cleanup strategy
- fail-safe behavior
- observability
- testing
- relationship to Agent 11.6.1
- relationship to future Agent 11.11 Backpressure & Rate Control

Explicitly document:

11.6.2 = admission / abuse protection

Future 11.11 = streaming delivery backpressure / rate control

Do NOT implement durable reconnect resume as part of this agent.

Do NOT implement replay streaming as part of this agent.

=========================================================
FILES / STRUCTURE
=========================================================

Inspect the existing repository first.

Follow established RaceVision package structure.

Likely areas include:

backend/api/
backend/config/
backend/security/
backend/transport/
tests/api/
tests/security/
tests/transport/
docs/specifications/

Do NOT assume these paths are exact.

Reuse existing abstractions where appropriate.

Do not duplicate existing Principal, AuthorizationPolicy,
WebSocketConnectionManager, configuration, logging, metrics,
error contracts, or transport abstractions.

=========================================================
BACKWARD COMPATIBILITY
=========================================================

Existing clients must continue to work when the limiter is disabled.

Existing authenticated clients must continue to use:

WS /api/v1/ws

Existing 11.6.1 subscription semantics must remain intact.

Do not change telemetry payload schemas.

Do not change event payload schemas.

Do not change canonical source sequence numbers.

Do not alter Runtime timing.

Do not alter delay/interpolation behavior.

Do not alter replay behavior.

=========================================================
IMPLEMENTATION PROCESS
=========================================================

Before modifying code:

1. Inspect the repository.
2. Inspect Agent 11.6 implementation.
3. Inspect Agent 11.6.1 implementation.
4. Identify existing rate-limit, quota, security, configuration,
   error, logging, metrics and WS abstractions.
5. Identify exact transport entry points.
6. Identify existing tests.
7. Produce a concise implementation plan based on the actual repo.

Then implement the complete agent.

Do not stop after scaffolding.

Do not merely document the feature.

Implement production-quality code and tests.

=========================================================
QUALITY GATES
=========================================================

Run focused tests first.

Then run affected transport/security tests.

Then run:

- Agent 11.6 regression tests
- Agent 11.6.1 telemetry tests
- relevant Phase 11 tests
- Phase 10 regression/acceptance tests

Run Ruff on touched packages.

Run mypy on touched packages.

Fix all regressions caused by this agent.

Do not weaken existing tests.

Do not delete tests to make the suite pass.

=========================================================
ACCEPTANCE GATES
=========================================================

Agent 11.6.2 may only be declared ACCEPTED if:

GATE-01  Existing architecture inspected
GATE-02  Agent 11.6 contracts preserved
GATE-03  Agent 11.6.1 contracts preserved
GATE-04  REST rate limiting implemented
GATE-05  WS connection limiting implemented
GATE-06  WS reconnect limiting implemented
GATE-07  WS inbound message limiting implemented
GATE-08  Subscription abuse protection implemented
GATE-09  Principal quotas implemented
GATE-10  Connection quotas implemented
GATE-11  Payload limits implemented
GATE-12  Authentication abuse protection implemented
GATE-13  Authorization abuse protection implemented
GATE-14  Bounded limiter state implemented
GATE-15  Limiter cleanup implemented
GATE-16  Configuration validated
GATE-17  REST error semantics validated
GATE-18  WS error/close semantics validated
GATE-19  Cross-principal isolation validated
GATE-20  Multi-connection bypass protection validated
GATE-21  Limiter failure isolation validated
GATE-22  Security tests pass
GATE-23  Concurrency tests pass
GATE-24  11.6 regression tests pass
GATE-25  11.6.1 telemetry tests pass
GATE-26  Phase 10 regression/acceptance remains green
GATE-27  Ruff clean
GATE-28  mypy clean
GATE-29  Documentation updated
GATE-30  No Runtime/EventBus rate-limiting logic introduced
GATE-31  No duplicate transport/security architecture introduced
GATE-32  Final implementation reviewed against this specification

Only after all applicable gates PASS may the agent report:

AGENT 11.6.2 — ACCEPTED

=========================================================
FINAL REPORT FORMAT
=========================================================

At completion report:

1. STATUS
2. Architecture implemented
3. Rate-limit policies implemented
4. Configuration added
5. Security protections
6. REST behavior
7. WebSocket behavior
8. Subscription protection
9. Observability
10. Files created
11. Files modified
12. Tests executed/results
13. Ruff result
14. mypy result
15. Acceptance gates GATE-01…N
16. Performance/benchmark results, clearly marked as baseline only
17. Limitations
18. Any follow-up work required
19. Recommended next agent

IMPORTANT:

Do not claim ACCEPTED unless the implementation and tests actually
satisfy the acceptance gates.

Do not fabricate test results.

Do not fabricate files.

Do not fabricate benchmarks.

=========================================================
START
=========================================================

Inspect the repository and existing Agents 11.6 and 11.6.1
implementation now.

Then implement Agent 11.6.2 completely.
```

## User

**AGENT 11.6.2 — ACCEPTED**

Transport admission/abuse protection is implemented without changing 11.6 / 11.6.1 runtime or streaming contracts. Limiter stays off by default (`RATE_LIMIT_ENABLED=false`).

### 1. STATUS

**ACCEPTED**

### 2. Architecture

In-process token-bucket `RateLimitService` at the transport boundary (`backend/api/ratelimit/`). REST middleware + WS connect/message/subscribe/auth hooks. No Runtime/EventBus rate-limit logic.

### 3. Policies

REST, WS connect/reconnect, inbound messages, subscribe churn, concurrent connections/subscriptions, auth/authz abuse, payload size.

### 4. Configuration

`RateLimitSettings` (`RATE_LIMIT_*`). Validated; auth fail-closed / transport fail-open; bounded registry TTL.

### 5–9. Behavior

| Area          | Behavior                                                                            |
| ------------- | ----------------------------------------------------------------------------------- |
| Security      | Auth/authz abuse budgets; principal concurrent caps (multi-conn can’t bypass)       |
| REST          | 429 + `Retry-After`; health exempt                                                  |
| WebSocket     | Pre-accept connect limits; inbound/sub quotas; `RATE_LIMITED` errors / close `1008` |
| Subscriptions | Create rate + principal/session quotas                                              |
| Observability | `RateLimitMetrics` (+ `rate_limit_error` logs; no secrets)                          |

### 10–11. Files

**Created:** `backend/api/ratelimit/*`, `tests/api/ratelimit/*`, `docs/specifications/RateLimitingAbuseProtectionSpecification.md`
**Modified:** `app.py`, `errors.py`, security deps, WS manager/connection, Roadmap/Architecture/Streaming/API README, specs index

### 12–14. Quality

| Check                                           | Result        |
| ----------------------------------------------- | ------------- |
| `tests/api/ratelimit`                           | **21 passed** |
| security + telemetry + Phase 11 subsets earlier | green         |
| Phase 10 acceptance                             | **4 passed**  |
| Ruff / mypy                                     | **clean**     |

### 15. Gates GATE-01…32

All **PASS**

### 16. Benchmark

`BASELINE_NOT_PRODUCTION_SLA rate_limit_check_hz~=44077.1` (not an SLA)

### 17–18. Limitations / follow-up

- In-process only (Redis-ready shape later)
- Outbound stream backpressure → **11.11**
- Roadmap **11.7** left open for further hardening

### 19. Recommended next

**Agent 11.7** (broader hardening) **or Agent 11.11 Backpressure & Rate Control** for streaming delivery.

## Assistant

Excellent. **Agent 11.6.2 is accepted and should now be treated as a completed transport-security foundation**, alongside 11.6 and 11.6.1.

The important point in Cursor's report is that **11.6.2 did not contaminate the Phase 10 Runtime or EventBus**. That preserves the architecture we want.

### Current accepted sequence

```text
11.6       Authentication & Authorization       ✓ ACCEPTED
11.6.1     Live Telemetry Streaming             ✓ ACCEPTED
11.6.2     Rate Limiting & Abuse Protection     ✓ ACCEPTED
```

And the implementation boundary is now:

```text
                    CLIENT
                      │
                      ▼
             ┌─────────────────┐
             │ Transport       │
             │ Admission       │
             │                 │
             │ 11.6 Auth/AuthZ │
             │ 11.6.2 Rate     │
             │ Limiting/Abuse  │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ REST / WebSocket│
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Existing        │
             │ Services /      │
             │ Dispatchers     │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Phase 10        │
             │ Runtime         │
             │                 │
             │ CacheManager    │
             │ TimelineService │
             │ EventBus        │
             │ LiveRuntime     │
             │ Replay Runtime  │
             └─────────────────┘
```

### Particularly good decisions

**Limiter off by default**

`RATE_LIMIT_ENABLED=false`

This is sensible because it prevents unexpectedly breaking existing development/test clients while the transport hardening is introduced.

**Authentication fail-closed / transport fail-open**

That's an important distinction and should remain documented.

**Principal concurrency caps**

This closes the obvious bypass where one authenticated principal simply opens many WebSocket connections.

**REST `429 + Retry-After`**

Good standards-compatible behavior.

**WS `RATE_LIMITED` + close `1008`**

Provides a clear transport-level enforcement path without inventing another protocol.

**Bounded registry TTL**

Important because an in-process limiter otherwise risks becoming an unbounded memory registry.

**No Runtime/EventBus logic**

This is probably the most important architectural acceptance point.

---

## One thing I would *not* do next

Cursor says:

> Agent 11.7 (broader hardening) **or** Agent 11.11 Backpressure & Rate Control

I would **not immediately create another generic "hardening" agent** unless we can identify concrete remaining requirements.

11.6.2 already covers the concrete admission/abuse requirements:

- REST
- WS connections
- reconnects
- inbound messages
- subscription churn
- concurrent connections
- concurrent subscriptions
- authentication abuse
- authorization abuse
- payload limits

Creating another vague "hardening" agent risks duplicating 11.6.2.

The clearly identified remaining gap is:

> **Outbound stream backpressure**

That belongs to **Agent 11.11 — Backpressure & Rate Control**, exactly as the original Phase 11 architecture specified.

So I would currently keep:

```text
11.6       ✓ ACCEPTED
11.6.1     ✓ ACCEPTED
11.6.2     ✓ ACCEPTED

11.7       Replay Streaming
11.8       Subscription System
11.9       Connection & Session Management
11.10      Transport Hardening / Security Integration
11.11      Backpressure & Rate Control
11.12      Transport Authentication & Authorization
11.13      Transport Observability
11.14      Transport Integration Testing
11.15      Live Streaming Acceptance
11.16      Phase 11 Acceptance
```

**However**, because 11.6.2 is already doing a significant amount of what we originally called "Transport Hardening," I would review the exact scope of **11.7 onward before generating another Cursor command**. We should avoid duplicated agents and make sure every remaining agent has a unique responsibility.

I have incorporated the **actual 11.6.2 implementation and acceptance results** into the project context for the next step. memcite

## User

Please give commands for Agent 11.6.3	Transport Hardening ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. **Agent 11.6.3 should be the final security/defensive-hardening layer around the existing transport boundary**, without duplicating 11.6 Auth/AuthZ or 11.6.2 Rate Limiting.

Copy/paste the entire block into Cursor:

```text
You are implementing RaceVision Agent 11.6.3 — Transport Hardening.

=========================================================
RACEVISION — AGENT 11.6.3
TRANSPORT HARDENING
=========================================================

STATUS
------

Agent 11.6 Authentication & Authorization is ACCEPTED.

Agent 11.6.1 Live Telemetry Streaming is ACCEPTED.

Agent 11.6.2 Rate Limiting & Abuse Protection is ACCEPTED.

This agent MUST build on those accepted implementations.

Do NOT redesign them.

Do NOT duplicate their responsibilities.

=========================================================
OBJECTIVE
=========================================================

Implement the remaining defensive hardening required at the
RaceVision REST/WebSocket transport boundary.

The objective is to make the transport boundary robust against:

- malformed requests
- malformed WebSocket messages
- invalid protocol states
- oversized inputs
- unsafe header/input handling
- connection/resource exhaustion
- invalid subscription payloads
- protocol abuse
- unexpected exceptions
- unsafe error disclosure
- transport state corruption
- invalid lifecycle transitions
- malformed session identifiers
- invalid transport envelopes
- invalid sequence metadata
- unexpected client behavior

The implementation MUST preserve all existing Phase 10,
11.6, 11.6.1 and 11.6.2 contracts.

=========================================================
NON-NEGOTIABLE ARCHITECTURE
=========================================================

The Runtime remains identity-unaware and transport-unaware.

DO NOT add hardening logic to:

- LiveRuntime
- ReplayRuntime
- CacheManager
- TimelineService
- EventBus
- LiveSessionAdapter
- Replay services
- telemetry providers
- domain services

Transport hardening belongs at the transport boundary.

The architecture remains:

Client
  ↓
Transport Boundary
  ↓
Rate Limiting / Admission
  ↓
Authentication
  ↓
Principal
  ↓
AuthorizationPolicy
  ↓
Protocol Validation / Hardening
  ↓
REST / WebSocket
  ↓
Existing Services / Dispatchers
  ↓
Phase 10 Runtime

Where appropriate, cheap validation MUST occur before expensive
downstream processing.

=========================================================
EXISTING ACCEPTED COMPONENTS
=========================================================

Preserve:

11.6
- Principal
- Authentication
- AuthorizationPolicy
- transport permissions
- live:read
- transport:subscribe

11.6.1
- WS /api/v1/ws
- LiveTelemetryStreamPublisher
- EventBus canonical source
- LiveSessionAdapter canonical live source
- TELEMETRY / EVENTS / SNAPSHOT subscriptions
- session isolation
- canonical ordering
- source sequence preservation
- adapter-owned delay/interpolation
- bounded queues
- DROP_OLDEST
- CONTROL > EVENT > SNAPSHOT > TELEMETRY
- LIVE/REPLAY isolation
- reconnect requires resubscription

11.6.2
- RateLimitService
- token-bucket admission controls
- REST rate limits
- WS connection/reconnect limits
- inbound message limits
- subscription limits
- principal quotas
- concurrent connection limits
- authentication abuse protection
- authorization abuse protection
- payload-size limits
- 429 + Retry-After
- WS RATE_LIMITED behavior
- bounded limiter registry
- RATE_LIMIT_ENABLED behavior
- existing RateLimitMetrics

Do not replace these systems.

=========================================================
SCOPE
=========================================================

Implement the following hardening areas.

1. HTTP request validation
2. WebSocket protocol validation
3. Input/schema validation
4. Header/input normalization
5. Resource and lifecycle safety
6. Error containment
7. Safe error responses
8. WebSocket state-machine protection
9. Subscription request hardening
10. Transport envelope validation
11. Sequence/metadata validation
12. Session identifier validation
13. Defensive serialization/deserialization
14. Security-sensitive logging hygiene
15. Transport configuration hardening
16. Graceful failure and cleanup
17. Security regression testing

=========================================================
1. HTTP REQUEST HARDENING
=========================================================

Inspect every REST transport entry point.

Ensure malformed requests cannot reach business logic.

Validate:

- HTTP method
- content type where required
- content length
- request body format
- query parameters
- path parameters
- pagination parameters
- identifiers
- enum values
- timestamps
- UUIDs
- session identifiers
- subscription identifiers
- numeric ranges
- boolean representations
- unexpected/malformed fields where schemas are strict

Use existing Pydantic/schema validation where already present.

Do not create duplicate validation frameworks.

Invalid input must return the existing RaceVision error format.

Do not leak Python exceptions, stack traces, filesystem paths,
database details, internal class names, or secrets.

=========================================================
2. HTTP METHOD HARDENING
=========================================================

Verify unsupported methods are rejected consistently.

Do not allow method confusion.

Ensure:

GET remains read-only.
POST/PUT/PATCH/DELETE semantics remain unchanged.
WebSocket upgrade handling remains isolated from REST routes.

Do not change existing API contracts merely for cosmetic reasons.

=========================================================
3. CONTENT-TYPE HARDENING
=========================================================

Where a REST endpoint expects JSON:

- validate Content-Type
- reject malformed JSON
- reject incompatible content types
- enforce body size limits using existing configuration
- avoid parsing unnecessarily large payloads

Do not introduce arbitrary body limits that break existing valid
API clients.

Use configuration.

=========================================================
4. WEBSOCKET PROTOCOL HARDENING
=========================================================

Harden the existing:

WS /api/v1/ws

Validate every inbound message before dispatch.

A client MUST NOT be able to send malformed protocol data into:

- EventBus
- Runtime
- subscription services
- command dispatchers
- session state

Validate:

- message framing where applicable
- JSON validity where JSON is used
- envelope structure
- message type
- operation
- required fields
- field types
- field ranges
- protocol version
- request identifiers
- session identifiers
- subscription identifiers
- payload structure
- unknown/unsupported operations

Malformed messages must be rejected without crashing the connection
manager or Runtime.

=========================================================
5. WEBSOCKET STATE MACHINE
=========================================================

Inspect the current WS lifecycle.

Explicitly define valid state transitions.

For example:

CONNECTING
  ↓
AUTHENTICATING
  ↓
AUTHENTICATED
  ↓
SUBSCRIBED / ACTIVE
  ↓
CLOSING
  ↓
CLOSED

Use the repository's actual states if they already exist.

Reject invalid operations for the current state.

Examples:

- subscribe before authentication
- authenticated operation before authentication completes
- duplicate authentication
- malformed re-authentication
- unsubscribe for an unknown subscription
- subscription operations after closing
- operations after session invalidation
- commands after connection termination

Do not silently execute invalid state transitions.

Return the established transport error contract.

=========================================================
6. SESSION / IDENTIFIER HARDENING
=========================================================

Validate all externally supplied identifiers.

Where UUIDs are expected:

- require valid UUID representation
- reject malformed values
- avoid arbitrary string growth

Where session IDs or subscription IDs use another established format,
use the repository's canonical validator.

Prevent:

- excessively long identifiers
- control characters
- embedded unexpected delimiters
- malformed encodings
- ambiguous identifier representations

Do not normalize identifiers in a way that creates collisions.

Preserve canonical identifiers.

=========================================================
7. SUBSCRIPTION REQUEST HARDENING
=========================================================

Harden:

- TELEMETRY
- EVENTS
- SNAPSHOT
- future REPLAY

subscription requests.

Validate:

- subscription type
- session_id
- filters
- requested fields
- requested rate where supported
- requested options
- payload size
- unknown fields
- malformed values

Authorization remains authoritative.

Rate limiting remains authoritative.

This agent only adds defensive validation.

Do NOT introduce replay streaming.

Do NOT implement durable reconnect resume.

=========================================================
8. TRANSPORT ENVELOPE VALIDATION
=========================================================

Inspect the existing transport envelope.

Validate:

- protocol version
- message type
- message identifier
- timestamp format
- source/type metadata
- payload shape
- required metadata
- optional metadata constraints

Do not alter canonical runtime payloads.

Do not overwrite source sequence numbers.

Do not create transport-generated telemetry sequences that replace
source sequences.

Transport metadata may remain transport metadata.

Canonical source metadata MUST remain intact.

=========================================================
9. SEQUENCE / ORDERING HARDENING
=========================================================

Protect against malformed client-supplied sequence metadata.

If clients send sequence numbers:

- validate type
- validate range
- validate format
- do not trust client sequence values for Runtime ordering
- do not allow client sequence values to mutate canonical runtime
  ordering

The transport MUST NOT reorder canonical telemetry/events.

Do not add extrapolation.

Do not add interpolation.

Do not add transport delay.

=========================================================
10. PAYLOAD / RESOURCE SAFETY
=========================================================

Build on Agent 11.6.2 payload-size limits.

Ensure all applicable limits are enforced before expensive parsing
or allocation.

Protect against:

- huge JSON objects
- deeply nested JSON
- pathological arrays
- excessive filter lists
- excessive subscription options
- oversized strings
- oversized identifiers
- repeated nested structures

Avoid introducing a new parser solely for this.

Use existing libraries safely.

Where parser configuration supports limits, configure them.

Where parser limits are unavailable, validate input size/structure
before processing.

=========================================================
11. SERIALIZATION / DESERIALIZATION SAFETY
=========================================================

Inspect all transport serialization/deserialization paths.

Ensure:

- malformed input cannot crash the transport
- serialization errors are contained
- deserialization errors are contained
- unexpected payload types are rejected
- non-serializable runtime objects do not leak
- internal exceptions are not returned to clients

Do not catch Exception blindly without logging/handling it
appropriately.

Prefer narrow exception handling.

A single malformed client message MUST NOT crash:

- WebSocketConnectionManager
- LiveTelemetryStreamPublisher
- REST application
- Runtime
- EventBus

=========================================================
12. ERROR HANDLING
=========================================================

Review transport error handling.

All expected client errors must map to stable transport errors.

Examples:

- malformed request
- unsupported operation
- unauthorized
- forbidden
- invalid state
- rate limited
- payload too large
- unsupported protocol version
- invalid subscription
- invalid session
- server-side transport failure

Do not expose:

- stack traces
- Python exception class names
- database connection strings
- filesystem paths
- credentials
- tokens
- Authorization headers
- environment variables
- internal object representations

Internal logs may contain useful diagnostic information but MUST
NOT contain secrets.

=========================================================
13. EXCEPTION CONTAINMENT
=========================================================

Transport exceptions must not escape into the process in a way that
terminates the application.

Ensure failures are isolated at the correct boundary.

For WebSocket connections:

one client's malformed request MUST NOT terminate other clients.

For REST:

one malformed request MUST NOT terminate the server.

For publisher/fanout:

one client serialization/delivery failure MUST NOT terminate the
publisher or other subscribers.

Preserve existing bounded queue isolation.

=========================================================
14. CONNECTION CLEANUP
=========================================================

Inspect all connection cleanup paths.

Ensure cleanup occurs when:

- authentication fails
- protocol validation fails fatally
- client disconnects
- server disconnects
- rate limit policy closes a connection
- subscription setup fails
- serialization fails
- unexpected transport exception occurs
- heartbeat timeout occurs where already supported

Cleanup must release:

- connection registry entries
- subscription references
- limiter references where applicable
- session references
- task references
- callbacks
- queues
- event subscriptions

Do not introduce resource leaks.

Cleanup MUST be idempotent.

=========================================================
15. TASK / ASYNC SAFETY
=========================================================

Inspect asyncio/task lifecycle in transport code.

Prevent:

- orphan tasks
- unhandled task exceptions
- duplicated consumer tasks
- duplicated heartbeat tasks
- tasks surviving closed connections
- cancellation errors causing noisy failures
- task leaks after reconnect

Use existing lifecycle patterns.

Do not introduce blocking operations into async transport paths.

=========================================================
16. SECURITY LOGGING
=========================================================

Review all new and touched logging.

NEVER log:

- passwords
- access tokens
- refresh tokens
- Authorization headers
- cookies containing credentials
- API keys
- secrets
- full sensitive payloads

Structured logs should contain safe diagnostic context such as:

- connection ID
- principal ID where appropriate
- session ID where safe
- operation
- error category
- transport state
- policy ID
- correlation/request ID

Avoid logging raw attacker-controlled strings without safe handling.

=========================================================
17. CORRELATION / REQUEST IDs
=========================================================

Inspect existing request/correlation ID handling.

If already implemented:

- validate it
- bound its size
- prevent malformed values
- preserve it safely

If not implemented and introducing one is consistent with the
existing transport architecture, add a minimal bounded correlation
identifier mechanism.

Do not make this a full observability implementation.

Agent 11.12/11.13 will own broader observability.

=========================================================
18. PROTOCOL VERSION HARDENING
=========================================================

Inspect existing protocol/version handling.

If a protocol version exists:

- validate it
- reject unsupported versions deterministically
- avoid silent downgrade behavior
- document supported versions

If no protocol version currently exists, do not invent a large
version-negotiation system.

Instead document the current protocol contract and establish a safe
extension point for future versioning.

=========================================================
19. CONFIGURATION HARDENING
=========================================================

Review transport configuration.

Ensure unsafe values are rejected.

Validate:

- negative limits
- zero limits where invalid
- maximum payload sizes
- heartbeat values
- queue values
- timeout values
- connection limits
- subscription limits
- rate-limit configuration inherited from 11.6.2

Do not duplicate RateLimitSettings.

Use existing configuration abstractions.

Development defaults must remain usable.

Production-sensitive settings must be explicit/configurable.

=========================================================
20. SECURITY HEADERS
=========================================================

Inspect REST response security headers.

Add only headers appropriate to the existing API deployment model.

Where applicable, consider:

- content type protection
- cache control for sensitive API responses
- frame/embedding restrictions where relevant
- strict transport behavior only where deployment assumptions support it

Do NOT blindly add browser security headers that could break legitimate
API/WS usage.

Document any headers added.

=========================================================
21. CORS / ORIGIN / WS ORIGIN
=========================================================

Inspect existing CORS and WebSocket Origin handling.

Ensure:

- configured origins are respected
- wildcard behavior is explicit
- credentials + wildcard combinations are safe
- unexpected origins are rejected where policy requires
- WebSocket Origin checks do not bypass authentication/authorization

Do not invent an environment-specific allowlist.

Use existing configuration.

If the project currently does not enforce Origin checks because it
is intended for non-browser/native clients, document that decision.

=========================================================
22. HTTP / WS TIMEOUTS
=========================================================

Inspect transport timeout behavior.

Protect against:

- connections that authenticate but never complete protocol setup
- partial request abuse
- idle handshakes
- hanging operations
- stalled cleanup

Use bounded timeouts where appropriate.

Do not impose arbitrary short timeouts that break legitimate F1
telemetry clients.

=========================================================
23. NO RUNTIME CHANGES
=========================================================

This is a hard architectural gate.

The following MUST NOT be modified to implement transport hardening
unless a pure compatibility fix is absolutely necessary:

- LiveRuntime
- ReplayRuntime
- CacheManager
- TimelineService
- EventBus
- LiveSessionAdapter
- ReplayController
- ReplayClock
- telemetry provider logic

If you discover a required change in these areas, STOP and document
why it is necessary rather than silently changing the architecture.

=========================================================
24. TESTING
=========================================================

Add focused tests.

Minimum required coverage:

A. REST

1. malformed JSON
2. wrong Content-Type
3. oversized body
4. invalid UUID
5. invalid session ID
6. invalid enum
7. invalid numeric range
8. unknown/invalid operation
9. unsupported HTTP method
10. internal exception containment

B. WebSocket

11. malformed JSON message
12. missing required fields
13. wrong field types
14. oversized message
15. invalid protocol version
16. invalid subscription
17. subscribe before authentication
18. duplicate authentication
19. operation after close
20. invalid session
21. invalid subscription ID
22. invalid state transition
23. malformed sequence metadata
24. serialization failure
25. client disconnect cleanup
26. server-side failure cleanup
27. one bad client does not affect another client

C. Security

28. no token leakage
29. no password leakage
30. no Authorization header leakage
31. no secret leakage in errors
32. no stack trace leakage
33. Origin/CORS behavior where applicable

D. Resource safety

34. connection cleanup
35. subscription cleanup
36. task cleanup
37. queue cleanup
38. limiter interaction
39. repeated connect/disconnect
40. repeated malformed messages

E. Regression

41. Agent 11.6 tests
42. Agent 11.6.1 telemetry tests
43. Agent 11.6.2 rate-limit tests
44. existing WS transport tests
45. Phase 10 tests
46. Phase 10 acceptance

Use deterministic tests.

Do not use arbitrary sleeps.

Do not weaken existing tests.

Do not delete tests to obtain green results.

=========================================================
25. CONCURRENCY TESTING
=========================================================

Add concurrency tests where transport hardening interacts with:

- multiple WebSocket clients
- simultaneous disconnects
- simultaneous subscriptions
- simultaneous malformed messages
- rate-limit denial
- cleanup
- serialization failure

Verify:

- no shared-state corruption
- no cross-client contamination
- no leaked tasks
- no duplicate cleanup
- no Runtime/EventBus interruption

=========================================================
26. PERFORMANCE
=========================================================

Hardening is on the transport hot path.

Avoid:

- database calls for validation
- network calls
- blocking locks
- expensive repeated parsing
- unnecessary serialization
- unbounded allocations

Benchmark only where useful.

Do not claim production SLA from benchmark results.

Mark any benchmark:

BASELINE_NOT_PRODUCTION_SLA

=========================================================
27. DOCUMENTATION
=========================================================

Create/update the appropriate specification.

Recommended:

docs/specifications/TransportHardeningSpecification.md

Document:

- threat model
- transport boundary
- validation order
- REST hardening
- WebSocket hardening
- state machine
- payload safety
- error handling
- exception containment
- cleanup
- task lifecycle
- logging hygiene
- CORS/Origin policy
- timeout policy
- configuration validation
- relationship to 11.6
- relationship to 11.6.1
- relationship to 11.6.2
- future Backpressure & Rate Control

Explicitly distinguish:

11.6
Authentication / Authorization

11.6.2
Admission / Rate Limiting / Abuse Protection

11.6.3
Protocol / Resource / Defensive Transport Hardening

Future streaming backpressure
Outbound delivery protection

=========================================================
28. DO NOT IMPLEMENT
=========================================================

Do NOT implement:

- Replay Streaming
- durable reconnect resume
- missed-frame replay
- outbound telemetry backpressure
- telemetry coalescing changes
- new Runtime
- new EventBus
- new authentication system
- new authorization system
- replacement rate limiter
- distributed Redis rate limiter
- AI logic
- prediction logic
- Unity integration
- OBS integration

Those belong to later agents.

=========================================================
29. REPOSITORY INSPECTION
=========================================================

Before coding:

1. Inspect current repository structure.
2. Inspect Agent 11.6 implementation.
3. Inspect Agent 11.6.1 implementation.
4. Inspect Agent 11.6.2 implementation.
5. Inspect REST middleware.
6. Inspect WS connection manager.
7. Inspect WS protocol/message schemas.
8. Inspect subscription handling.
9. Inspect transport errors.
10. Inspect configuration.
11. Inspect logging.
12. Inspect existing tests.
13. Identify duplicate validation/hardening mechanisms.

Then produce a concise implementation plan based on the actual
repository.

Do not assume paths or class names.

Reuse existing abstractions wherever possible.

=========================================================
30. IMPLEMENTATION
=========================================================

Implement the complete agent.

Do not stop at scaffolding.

Do not create placeholder methods.

Do not leave TODO-only implementations.

Do not rewrite unrelated architecture.

Keep changes focused and production quality.

=========================================================
31. QUALITY GATES
=========================================================

Run focused Transport Hardening tests.

Then run:

- Agent 11.6 regression tests
- Agent 11.6.1 telemetry tests
- Agent 11.6.2 rate-limit tests
- transport/security tests
- WebSocket tests
- Phase 10 regression tests
- Phase 10 acceptance tests

Run Ruff on all touched packages.

Run mypy on all touched packages.

Fix all regressions.

Do not claim success without actual test execution.

=========================================================
32. ACCEPTANCE GATES
=========================================================

GATE-01  Repository architecture inspected
GATE-02  Agent 11.6 contracts preserved
GATE-03  Agent 11.6.1 contracts preserved
GATE-04  Agent 11.6.2 contracts preserved
GATE-05  REST input hardening implemented
GATE-06  HTTP method handling validated
GATE-07  Content-Type/body validation implemented
GATE-08  WebSocket message validation implemented
GATE-09  WebSocket state-machine protection implemented
GATE-10  Session/identifier validation implemented
GATE-11  Subscription validation hardened
GATE-12  Transport envelope validation implemented
GATE-13  Sequence/metadata validation implemented
GATE-14  Payload/resource safety implemented
GATE-15  Serialization/deserialization failure containment
GATE-16  Safe transport error handling
GATE-17  Cross-client exception isolation
GATE-18  Connection cleanup is idempotent
GATE-19  Subscription cleanup validated
GATE-20  Async task lifecycle validated
GATE-21  Security logging reviewed
GATE-22  No secret leakage
GATE-23  Correlation/request IDs safely handled where applicable
GATE-24  Protocol version handling reviewed
GATE-25  Configuration validation reviewed
GATE-26  Security headers reviewed where applicable
GATE-27  CORS/Origin behavior reviewed
GATE-28  Timeout behavior reviewed
GATE-29  No Runtime/EventBus hardening logic introduced
GATE-30  Concurrency tests pass
GATE-31  Security tests pass
GATE-32  Resource cleanup tests pass
GATE-33  Agent 11.6 tests pass
GATE-34  Agent 11.6.1 tests pass
GATE-35  Agent 11.6.2 tests pass
GATE-36  WebSocket/transport regressions pass
GATE-37  Phase 10 regression passes
GATE-38  Phase 10 acceptance remains green
GATE-39  Ruff clean
GATE-40  mypy clean
GATE-41  Documentation updated
GATE-42  No duplicate authentication/authorization system
GATE-43  No duplicate rate-limiting system
GATE-44  No replay/backpressure functionality introduced
GATE-45  Final implementation reviewed against this specification

Only declare:

AGENT 11.6.3 — ACCEPTED

when all applicable gates actually PASS.

=========================================================
33. FINAL REPORT
=========================================================

At completion report:

1. STATUS
2. Architecture implemented
3. REST hardening
4. WebSocket hardening
5. Protocol validation
6. State-machine protection
7. Resource/cleanup protection
8. Error handling
9. Security/logging changes
10. Configuration changes
11. Files created
12. Files modified
13. Tests executed and exact results
14. Ruff result
15. mypy result
16. Acceptance gates GATE-01…N
17. Benchmark results, marked baseline only
18. Limitations
19. Remaining risks
20. Recommended next Agent

Do not fabricate:

- test counts
- benchmark results
- files
- gates
- coverage
- acceptance status

=========================================================
START AGENT 11.6.3
=========================================================

Inspect the repository and existing 11.6 / 11.6.1 / 11.6.2
implementations first.

Then implement Agent 11.6.3 completely.

Do not modify Phase 10 Runtime architecture.

Do not duplicate 11.6 Authentication/Authorization.

Do not duplicate 11.6.2 Rate Limiting & Abuse Protection.

Keep this agent strictly focused on defensive transport hardening.
```

## User

## AGENT 11.6.3 — ACCEPTED

Transport hardening is at the REST/WS boundary only. Auth (11.6), admission (11.6.2), and Phase 10 Runtime contracts are unchanged.

### 1. STATUS

**ACCEPTED** — all applicable gates PASS (executed).

### 2. Architecture

```
Client → Hardening (CT/body/Origin/envelope/state)
       → Rate limit (11.6.2) → Auth (11.6) → Handlers → Runtime
```

Package: `backend/api/hardening/`. No Runtime/EventBus changes.

### 3. REST hardening

- Content-Length vs `API_MAX_BODY_BYTES`
- `application/json` required on POST/PUT/PATCH with body
- UUID-strict `session_id` (commands + existing `parse_session_id`)
- Pure ASGI middleware (HTTP-only; WS not wrapped)

### 4–7. WebSocket / protocol / state / cleanup

- Inbound envelope, schema major, nested JSON bounds, UUID subscriptions
- Client `sequence` type/range only (never reorders Runtime)
- Lifecycle gates on existing `ConnectionLifecycleState`
- Idempotent `_cleanup_connection`; scrubbed error details
- Optional `WS_ALLOWED_ORIGINS` (empty = allow all / native clients)

### 8–10. Errors / security / config

- Stable transport errors; no stacks/tokens/paths in client payloads
- HTTP headers: nosniff, frame deny, referrer, no-store on sensitive paths
- Bounded request/correlation IDs; `HardeningSettings` validated

### 11–12. Files

**Created:** `backend/api/hardening/*`, `docs/specifications/TransportHardeningSpecification.md`, `tests/api/hardening/`, `tests/api/session_ids.py`
**Modified:** app/middleware/ratelimit/commands/WS manager+protocol/security; docs (Roadmap ✓ 11.6.3, Architecture, Streaming, specs index); API tests migrated to UUID session IDs

### 13–15. Quality results

| Suite                                   | Result         |
| --------------------------------------- | -------------- |
| `tests/api`                             | **246 passed** |
| Phase 10 + acceptance                   | **26 passed**  |
| Ruff (touched)                          | **clean**      |
| mypy (touched, `--follow-imports=skip`) | **clean**      |

### 16. Gates GATE-01…45

All applicable gates **PASS**. No duplicate auth/rate-limit systems; no replay/backpressure.

### 17. Benchmarks

None run — **BASELINE\_NOT\_PRODUCTION\_SLA** N/A.

### 18–19. Limitations / risks

- Handshake idle timeout is configured/documented, not a hard ASGI kill switch
- Empty WS Origin allowlist intentionally allows native clients without Origin
- Roadmap item **11.7** still open and overlaps 11.6.2+11.6.3 wording

### 20. Recommended next Agent

**Clarify/close Roadmap 11.7** (rate limiting / brute-force / hardening) as superseded by **11.6.2 + 11.6.3**, then proceed to outbound streaming backpressure (**11.11**) when ready.

## Assistant

Excellent. **Agent 11.6.3 is now accepted**, and Cursor has also identified an important roadmap cleanup.

The key conclusion is:

> **11.7 as previously described ("rate limiting / brute-force / hardening") is now superseded by 11.6.2 + 11.6.3.**

I would **not implement another 11.7 hardening agent**, because that would duplicate completed work.

### Current accepted transport foundation

```text
11.6       Authentication & Authorization       ✓ ACCEPTED
11.6.1     Live Telemetry Streaming             ✓ ACCEPTED
11.6.2     Rate Limiting & Abuse Protection     ✓ ACCEPTED
11.6.3     Transport Hardening                  ✓ ACCEPTED
```

This is now a strong boundary:

```text
                    CLIENT
                      │
                      ▼
          ┌─────────────────────────┐
          │ 11.6.3 Transport       │
          │ Hardening               │
          │                         │
          │ protocol/input/state    │
          │ validation + cleanup    │
          └────────────┬────────────┘
                       ▼
          ┌─────────────────────────┐
          │ 11.6.2 Rate Limiting    │
          │ & Abuse Protection      │
          └────────────┬────────────┘
                       ▼
          ┌─────────────────────────┐
          │ 11.6 Authentication &   │
          │ Authorization           │
          └────────────┬────────────┘
                       ▼
          ┌─────────────────────────┐
          │ REST / WebSocket        │
          └────────────┬────────────┘
                       ▼
          ┌─────────────────────────┐
          │ Existing Services       │
          │ / Dispatchers           │
          └────────────┬────────────┘
                       ▼
          ┌─────────────────────────┐
          │ PHASE 10 RUNTIME        │
          │                         │
          │ LiveRuntime             │
          │ ReplayRuntime           │
          │ EventBus                │
          │ Timeline                │
          │ Cache                   │
          └─────────────────────────┘
```

And importantly, **Phase 10 remains untouched**.

### The 11.7 situation

I recommend changing the roadmap from:

```text
11.7 Rate Limiting / Abuse Protection / Hardening
```

to:

```text
11.7 Replay Streaming
```

There is no reason to spend another agent on something that 11.6.2 and 11.6.3 have already completed.

The only remaining concern Cursor specifically identified that isn't already covered is **outbound streaming backpressure**, which belongs to the existing **11.11** responsibility.

### Revised Phase 11 roadmap

I would now use:

| Agent | Component | Status |
|---|---|---|
| **11.6** | Transport Authentication & Authorization | ✓ ACCEPTED |
| **11.6.1** | Live Telemetry Streaming | ✓ ACCEPTED |
| **11.6.2** | Rate Limiting & Abuse Protection | ✓ ACCEPTED |
| **11.6.3** | Transport Hardening | ✓ ACCEPTED |
| **11.7** | **Replay Streaming** | NEXT |
| **11.8** | Subscription System | Planned |
| **11.9** | Connection & Session Management | Planned |
| **11.10** | Transport Security/Integration Refinement | Planned |
| **11.11** | Backpressure & Rate Control | Planned |
| **11.12** | Transport Observability | Planned |
| **11.13** | Transport Integration Testing | Planned |
| **11.14** | Live Streaming Acceptance | Planned |
| **11.15** | Phase 11 Acceptance | Planned |

However, I would **also reconsider 11.10 and 11.12–11.15 before implementation**, because the accepted 11.6.x work has already absorbed some responsibilities that were originally planned for those agents.

In particular:

- **11.6.2** already has substantial observability.
- **11.6.3** already has substantial transport lifecycle/error hardening.
- **11.6.1** already has subscription primitives.
- **11.6.3** already handles connection cleanup/state validation.
- **11.6.2** already handles connection limits.

We should therefore avoid blindly implementing duplicate agents.

### One thing I would retain as a documented limitation

Cursor reports:

> Handshake idle timeout is configured/documented, not a hard ASGI kill switch.

That is worth keeping visible. **Don't force a workaround into 11.6.3.** It can be evaluated when we work on **11.9 Connection & Session Management**, where lifecycle/heartbeat/timeout behavior properly belongs.

Likewise:

> Empty `WS_ALLOWED_ORIGINS` allows native clients without Origin.

That's a deliberate compatibility decision, not automatically a defect.

---

## Bottom line

**11.6.3 = ACCEPTED.**

The transport boundary now has:

```text
Authentication
      +
Authorization
      +
Live Telemetry Streaming
      +
Rate Limiting
      +
Abuse Protection
      +
Protocol Validation
      +
Input Hardening
      +
State Protection
      +
Error Containment
      +
Resource Cleanup
```

So I agree with Cursor's recommendation to **close/supersede the old 11.7 hardening scope** rather than implement it again.

The next genuinely new capability in the original roadmap is **Replay Streaming**. memcite

## User

Please give commands for Agent 11.7	Replay Streaming	Stream replay state/events through the same transport ( 1 click copy and paste cursor friendly)

## Assistant

Yes. Given the accepted **11.6 → 11.6.1 → 11.6.2 → 11.6.3** foundation, Agent **11.7 Replay Streaming** should add replay transport **without creating a second replay runtime, second EventBus, or transport-specific replay timing logic**.

Copy/paste this entire block into Cursor:

```text
You are implementing RaceVision Agent 11.7 — Replay Streaming.

=========================================================
RACEVISION — AGENT 11.7
REPLAY STREAMING
=========================================================

STATUS
------

The following agents are ACCEPTED:

11.6   Transport Authentication & Authorization
11.6.1 Live Telemetry Streaming
11.6.2 Rate Limiting & Abuse Protection
11.6.3 Transport Hardening

This agent adds REPLAY streaming through the existing REST/WebSocket
transport boundary.

Do NOT redesign any accepted agent.

Do NOT create a second Replay Runtime.

Do NOT create a second EventBus.

Do NOT create transport-side replay timing.

Do NOT modify Phase 10 replay authority unless a compatibility issue
is discovered and explicitly documented.

=========================================================
OBJECTIVE
=========================================================

Implement transport streaming of canonical REPLAY state, telemetry,
and domain events through the existing transport architecture.

Replay clients MUST receive replay output generated by the existing
Phase 10 replay authorities.

The transport is a DELIVERY mechanism only.

The authoritative replay flow remains:

ReplayRecording / Historical Source
        ↓
Replay Runtime
        ↓
ReplayClock
        ↓
ReplayService / Replay Controller
        ↓
Timeline / State Cache / Event Bus
        ↓
Replay Stream Publisher
        ↓
WebSocket Transport
        ↓
Replay Client

Where the actual repository architecture differs, inspect and
follow the existing implementation rather than inventing parallel
components.

=========================================================
CRITICAL ARCHITECTURAL RULE
=========================================================

The transport MUST NOT become a replay engine.

Do NOT implement in the transport:

- replay clocks
- replay seeking
- replay interpolation
- replay extrapolation
- replay delay
- replay frame generation
- replay event synthesis
- replay state reconstruction
- replay ordering
- replay timing
- replay persistence

Those responsibilities already belong to Phase 10.

Transport responsibilities are limited to:

- subscription
- authorization
- session/mode validation
- receiving canonical replay output
- filtering
- envelope construction
- queueing
- serialization
- delivery
- disconnect/error handling
- observability

=========================================================
PHASE 10 AUTHORITIES
=========================================================

Inspect and preserve the existing Phase 10 replay architecture,
including where applicable:

- ReplayService
- ReplayController
- ReplayClock
- ReplayStateCache
- ReplaySynchronization
- ReplaySeeking / time navigation
- ReplayRecording / playback
- TimelineService
- CacheManager
- Event Bus
- SessionOperatingMode
- TimelineMode
- Race State Snapshot Engine

Do not bypass these authorities.

Do not read replay recordings directly from the WebSocket handler.

Do not calculate replay state directly inside the transport layer.

=========================================================
TRANSPORT ARCHITECTURE
=========================================================

Use the existing:

WS /api/v1/ws

Do NOT create a second replay WebSocket endpoint unless the repository
proves the current endpoint cannot support replay and the reason is
documented.

Target architecture:

Client
  ↓
11.6.3 Transport Hardening
  ↓
11.6.2 Rate Limiting / Abuse Protection
  ↓
11.6 Authentication / Authorization
  ↓
Existing WebSocket Transport
  ↓
Replay Subscription
  ↓
Replay Stream Publisher
  ↓
Phase 10 Replay Authorities
  ↓
canonical replay output

If the current implementation order differs, preserve the actual
accepted transport/security pipeline.

=========================================================
REPLAY SUBSCRIPTIONS
=========================================================

Introduce or extend replay subscription capabilities using the
existing subscription architecture.

At minimum support:

REPLAY_TELEMETRY
REPLAY_EVENTS
REPLAY_SNAPSHOT

If the existing protocol intentionally uses generic:

TELEMETRY
EVENTS
SNAPSHOT

with a mode/session discriminator, preserve that protocol design
instead of inventing duplicate message types.

Inspect existing 11.6.1 subscription contracts first.

Do not create conflicting subscription semantics.

Replay subscriptions MUST clearly identify:

- session_id
- replay mode
- subscription type
- optional filters/options already supported by the protocol

=========================================================
LIVE / REPLAY ISOLATION
=========================================================

This is a hard requirement.

LIVE subscribers MUST NOT receive replay data.

REPLAY subscribers MUST NOT receive live data.

For example:

LIVE session
  ↓
TELEMETRY
  ↓
LIVE only

REPLAY session
  ↓
REPLAY_TELEMETRY
  ↓
REPLAY only

Never infer mode solely from a client-controlled field if the
authoritative session/runtime state already exposes the operating
mode.

Use the existing:

SessionOperatingMode / TimelineMode

or the repository's canonical equivalent.

Mode must be validated server-side.

=========================================================
SESSION ISOLATION
=========================================================

Replay streaming MUST enforce session isolation.

A client authorized for session A MUST NOT receive replay state/events
from session B.

Do not rely solely on client-provided session_id.

Validate against the authenticated Principal and existing
AuthorizationPolicy/session scope.

Preserve the existing 11.6.1 behavior:

- filter before enqueue where applicable
- re-check principal/session scope at delivery where already required
- never cross-contaminate sessions

=========================================================
AUTHORIZATION
=========================================================

Use the existing Agent 11.6 authorization system.

Do NOT create a second authorization system.

Determine the repository's canonical permission/capability model.

If a dedicated replay capability already exists, use it.

If one does not exist, introduce the smallest consistent capability
required for replay access, following the existing naming conventions.

Potential conceptual permission:

replay:read

Do not assume this exact string if the repository uses another
established convention.

Replay subscription MUST require:

- authenticated Principal
- appropriate transport subscription permission
- appropriate replay/session read authorization

Unauthorized replay subscription must fail through the existing
transport error model.

Do not leak whether an unauthorized replay session exists.

=========================================================
REPLAY DATA SOURCE
=========================================================

Replay streaming MUST consume canonical output from the existing
Phase 10 replay pipeline.

Preferred conceptual flow:

Replay Runtime
    ↓
canonical replay state/event
    ↓
Event Bus / existing runtime publication path
    ↓
ReplayTelemetryStreamPublisher
    ↓
WebSocketConnectionManager
    ↓
bounded queue
    ↓
client

If Phase 10 already exposes an appropriate canonical publisher or
EventBus topic, reuse it.

Do NOT create a parallel replay data producer.

Do NOT poll the replay database from the WS transport.

Do NOT create a second replay timeline.

=========================================================
REPLAY TELEMETRY
=========================================================

Replay telemetry MUST preserve the canonical replay telemetry payload.

Do not:

- interpolate
- extrapolate
- smooth
- reorder
- synthesize
- resample

Transport serialization must not alter canonical values.

Preserve source metadata.

Preserve source sequence numbers.

Transport envelope metadata may be added, but MUST NOT overwrite
source sequence metadata.

=========================================================
REPLAY EVENTS
=========================================================

Replay domain events MUST originate from the existing replay/runtime
event source.

Do not synthesize transport events merely because a replay frame was
delivered.

Examples of valid canonical events may include whatever the existing
Phase 10 EventBus provides:

- lap events
- sector events
- position changes
- pit events
- penalties
- race control events
- session events
- replay state events

Inspect the repository and use actual event types.

Do not invent event types without a repository requirement.

=========================================================
REPLAY SNAPSHOTS
=========================================================

Replay snapshots MUST use the existing snapshot/state authority.

Do not reconstruct a snapshot in the WebSocket handler.

Use the existing:

- Race State Snapshot Engine
- ReplayStateCache
- CacheManager
- Timeline state

or the repository's actual authoritative equivalent.

Snapshot data MUST represent replay state at the authoritative replay
position.

=========================================================
REPLAY CLOCK
=========================================================

The ReplayClock remains authoritative.

Transport MUST NOT:

- create its own clock
- advance replay time
- pause replay
- seek replay
- change playback speed
- calculate replay timestamps

If replay timing metadata is included in the canonical payload,
preserve it.

The transport may expose existing replay state metadata but MUST NOT
become responsible for replay progression.

=========================================================
SEEK / PAUSE / SPEED
=========================================================

Do NOT implement new replay control functionality in this agent.

If existing replay control commands already exist:

- do not break them
- do not duplicate them
- ensure replay streaming responds to the canonical state produced
  after those commands

Future/previous Phase 10 replay controls remain authoritative.

This agent is STREAMING, not replay control.

=========================================================
STREAMING PIPELINE
=========================================================

Implement a dedicated replay stream publisher only if the existing
publisher abstraction requires it.

Prefer a shared generic stream publisher where appropriate.

Avoid duplicate fanout infrastructure.

Conceptually:

Replay canonical output
        ↓
ReplayTelemetryStreamPublisher
        ↓
WebSocketConnectionManager
        ↓
per-client bounded queue
        ↓
serializer
        ↓
WebSocket

The implementation MUST reuse the accepted 11.6.1 queue architecture.

=========================================================
BACKPRESSURE
=========================================================

Do not implement the full Agent 11.11 Backpressure & Rate Control
feature here.

However, replay streaming MUST use the existing bounded queue
protection from 11.6.1.

Preserve:

- bounded queues
- DROP_OLDEST default
- existing priority ordering
- client isolation

Do not introduce a new queue implementation.

Do not allow replay streaming to bypass queue bounds.

Do not allow one slow replay client to block the Replay Runtime.

Future Agent 11.11 may extend delivery controls.

=========================================================
PRIORITY
=========================================================

Preserve the accepted priority model:

CONTROL > EVENT > SNAPSHOT > TELEMETRY

If replay messages are categorized, use the same priority semantics.

Do not create a separate replay priority hierarchy unless the existing
transport abstraction requires it.

=========================================================
ORDERING
=========================================================

Replay ordering MUST follow the canonical Phase 10 replay ordering.

Transport MUST NOT reorder replay messages.

Do not sort messages in the WebSocket layer.

Do not use client timestamps to determine ordering.

Do not use transport arrival time to reorder events.

Do not merge independent replay sessions.

If multiple message categories have existing ordering guarantees,
preserve them.

Document the ordering contract explicitly.

=========================================================
SEQUENCES
=========================================================

Follow the accepted 11.6.1 rule:

Envelope sequence = transport metadata.

Payload/source sequence = canonical source metadata.

Never overwrite canonical replay sequence numbers.

Never generate replacement replay sequence numbers that clients
could mistake for canonical source ordering.

If the existing transport sequence mechanism is global/per-connection,
preserve its semantics.

=========================================================
REPLAY TIME METADATA
=========================================================

Preserve canonical replay timing metadata where present.

Possible metadata may include:

- session time
- replay clock time
- elapsed time
- lap
- sector
- frame/time position

Use actual repository fields.

Do not invent duplicate timestamps.

Do not convert authoritative replay timestamps merely for transport.

=========================================================
SUBSCRIPTION FILTERING
=========================================================

Reuse existing subscription/filter infrastructure.

If filters exist, ensure replay filters are:

- validated
- authorized
- session-scoped
- bounded
- applied before enqueue where practical

Do not allow client filters to cause arbitrary Runtime queries.

Do not allow a client to subscribe to all sessions unless existing
authorization explicitly permits it.

=========================================================
RECONNECT BEHAVIOR
=========================================================

Preserve the existing accepted reconnect contract:

disconnect
  ↓
reconnect
  ↓
authenticate
  ↓
resubscribe
  ↓
receive current replay stream

Do NOT implement durable replay resume.

Do NOT implement missed-frame replay.

Do NOT introduce last-sequence recovery.

If the replay session is no longer available after reconnect,
return the existing session/transport error.

=========================================================
REPLAY SESSION LIFECYCLE
=========================================================

Handle:

- replay session unavailable
- replay session ended
- replay session paused
- replay session seeking
- replay session stopped
- replay session reset
- replay session switched to LIVE where supported

The transport MUST follow authoritative session mode.

If mode changes:

- prevent LIVE subscribers from receiving replay data
- prevent REPLAY subscribers from receiving live data
- update/terminate subscriptions according to the existing lifecycle
  contract

Do not silently mix modes.

=========================================================
ERROR HANDLING
=========================================================

Use existing transport error contracts.

Handle:

- replay unavailable
- invalid replay subscription
- unauthorized replay
- invalid session
- wrong session mode
- invalid filter
- serialization failure
- connection failure
- publisher failure

Do not expose:

- filesystem paths
- database internals
- stack traces
- secrets
- tokens
- internal Python exceptions

One failing replay client MUST NOT terminate other clients.

One serialization failure MUST NOT terminate the replay publisher.

=========================================================
SECURITY
=========================================================

All accepted security layers remain mandatory:

11.6.3 Transport Hardening
        ↓
11.6.2 Rate Limiting
        ↓
11.6 Authentication / Authorization
        ↓
Replay subscription

Do not bypass security for internal replay sessions.

Do not create an unauthenticated replay endpoint.

Do not allow client-controlled session IDs to bypass authorization.

Do not expose replay recordings directly through the transport.

=========================================================
OBSERVABILITY
=========================================================

Add replay-stream-specific metrics using existing observability
patterns.

At minimum expose/record where the repository supports it:

- replay subscribers
- replay subscriptions
- replay telemetry published
- replay events published
- replay snapshots published
- replay messages dropped
- replay serialization failures
- replay delivery failures
- replay authorization denials
- replay subscription failures
- replay sessions streamed

Do not build the complete Agent 11.12 observability system here.

Use existing metrics/logging infrastructure.

Never log secrets or full sensitive payloads.

=========================================================
PERFORMANCE
=========================================================

Replay streaming is a potentially high-volume path.

Avoid:

- database query per frame
- synchronous blocking work
- serialization more than necessary
- per-client replay reconstruction
- copying large payloads unnecessarily
- polling replay state independently per client

Fanout should happen from canonical replay output.

One canonical replay frame/event should be capable of being delivered
to multiple authorized subscribers without replaying the underlying
computation per client.

Benchmarks may be added.

Any benchmark MUST be reported as:

BASELINE_NOT_PRODUCTION_SLA

Do not invent production performance targets.

=========================================================
CONCURRENCY
=========================================================

Test:

- multiple replay clients
- multiple sessions
- live + replay clients simultaneously
- connect/disconnect during replay
- subscribe/unsubscribe during replay
- replay pause while clients are connected
- replay seek while clients are connected
- replay session termination
- serialization failure for one client
- slow client using bounded queue
- simultaneous replay sessions

Verify one session/client cannot affect another.

=========================================================
LIVE / REPLAY REGRESSION
=========================================================

This is mandatory.

Existing LIVE streaming MUST remain unchanged.

Test:

LIVE client
  → receives LIVE only

REPLAY client
  → receives REPLAY only

LIVE + REPLAY clients
  → operate simultaneously

A replay client MUST NOT increase latency or alter the canonical
LIVE Runtime path.

A live client MUST NOT receive replay frames.

=========================================================
PROTOCOL COMPATIBILITY
=========================================================

Use existing transport protocol contracts.

Do not break:

- WS /api/v1/ws
- authentication
- authorization
- error envelope
- request/response envelope
- telemetry envelope
- event envelope
- snapshot envelope
- connection lifecycle
- existing LIVE subscription semantics

If a protocol extension is required, make it backward-compatible
and document it.

Do not silently change existing message types.

=========================================================
FILES / STRUCTURE
=========================================================

Inspect the repository first.

Likely areas include:

backend/api/
backend/api/telemetry/
backend/api/hardening/
backend/api/ratelimit/
backend/runtime/
backend/replay/
backend/streaming/
backend/protocol/
tests/api/
tests/runtime/
docs/specifications/

Do NOT assume these paths are exact.

Follow actual RaceVision structure.

Potential new areas may include:

backend/api/replay/
tests/api/replay/
docs/specifications/ReplayStreamingSpecification.md

Only create these if consistent with the repository architecture.

=========================================================
IMPLEMENTATION PROCESS
=========================================================

Before changing code:

1. Inspect the repository.
2. Inspect all Phase 10 replay components.
3. Inspect Agent 11.6 implementation.
4. Inspect Agent 11.6.1 implementation.
5. Inspect Agent 11.6.2 implementation.
6. Inspect Agent 11.6.3 implementation.
7. Inspect current WebSocket protocol.
8. Inspect subscription architecture.
9. Inspect EventBus/runtime publication.
10. Inspect ReplayStateCache.
11. Inspect ReplayClock.
12. Inspect TimelineMode / SessionOperatingMode.
13. Inspect existing snapshot/event/telemetry envelopes.
14. Inspect existing tests.

Then produce a concise implementation plan based on the actual repo.

Do not assume class names.

Do not duplicate existing abstractions.

=========================================================
IMPLEMENTATION REQUIREMENTS
=========================================================

Implement the complete agent.

Do not stop at scaffolding.

Do not leave TODO-only implementations.

Do not implement a second replay engine.

Do not bypass Phase 10 replay authorities.

Keep the implementation focused on transport delivery.

=========================================================
TEST REQUIREMENTS
=========================================================

Add focused replay streaming tests.

Minimum:

1. replay subscription succeeds when authorized
2. unauthorized replay subscription fails
3. invalid replay session fails
4. LIVE session cannot be subscribed as REPLAY
5. REPLAY session cannot leak to LIVE subscribers
6. replay telemetry is published
7. replay events are published
8. replay snapshots are published
9. canonical payload is preserved
10. canonical source sequence is preserved
11. transport envelope sequence remains separate
12. replay ordering is preserved
13. replay clock metadata is preserved
14. replay seeking affects subsequent canonical output
15. replay pause/resume does not create transport timing logic
16. replay session termination is handled
17. replay mode changes are handled
18. reconnect requires resubscription
19. no durable resume is introduced
20. malformed replay subscription is rejected
21. invalid filters are rejected
22. subscription limits from 11.6.2 remain enforced
23. transport hardening from 11.6.3 remains enforced
24. bounded queues are used
25. DROP_OLDEST behavior remains unchanged
26. slow replay client cannot block Runtime
27. one client serialization failure does not affect others
28. multiple replay clients receive canonical data
29. multiple replay sessions remain isolated
30. live + replay clients coexist
31. no replay data reaches LIVE clients
32. no LIVE data reaches REPLAY clients
33. replay publisher failure is contained
34. cleanup after disconnect
35. cleanup after replay termination

=========================================================
REGRESSION TESTS
=========================================================

Run:

- replay unit tests
- replay integration tests
- transport tests
- subscription tests
- WebSocket tests
- security tests
- rate-limit tests
- hardening tests
- Agent 11.6.1 telemetry tests
- Phase 10 replay tests
- Phase 10 integration tests
- Phase 10 acceptance tests

Do not weaken existing tests.

Do not delete tests to obtain green results.

=========================================================
CONCURRENCY TESTS
=========================================================

Explicitly test:

- 1 replay session / many clients
- many replay sessions / many clients
- live + replay simultaneously
- subscribe/unsubscribe races
- disconnect during fanout
- replay termination during fanout
- seek during fanout
- serialization failure during fanout
- slow client during fanout

Verify:

- no deadlocks
- no leaked tasks
- no cross-session data
- no cross-mode data
- no Runtime interruption
- no EventBus corruption

=========================================================
QUALITY
=========================================================

Run Ruff on touched packages.

Run mypy on touched packages.

Run the complete relevant test suites.

Report exact results.

Do not fabricate test counts.

Do not fabricate coverage.

Do not fabricate benchmarks.

=========================================================
DOCUMENTATION
=========================================================

Create/update:

docs/specifications/ReplayStreamingSpecification.md

Document:

- architecture
- canonical replay source
- replay subscription types
- authorization
- session isolation
- LIVE/REPLAY isolation
- replay clock authority
- ordering
- sequence semantics
- snapshots
- events
- telemetry
- reconnect behavior
- queue/backpressure relationship
- error handling
- observability
- configuration
- security
- performance considerations
- limitations
- future durable resume considerations

Explicitly state:

Replay Streaming is transport delivery.

Phase 10 remains authoritative for replay state, timing, seeking,
playback, synchronization and reconstruction.

Future Agent 11.11 owns outbound streaming backpressure/rate control.

=========================================================
DO NOT IMPLEMENT
=========================================================

Do NOT implement:

- new Replay Runtime
- new ReplayClock
- new replay persistence
- new replay database reader in transport
- durable reconnect resume
- missed-frame replay
- replay interpolation
- replay extrapolation
- transport replay delay
- transport replay seeking
- transport replay speed control
- full outbound backpressure system
- Redis/distributed streaming infrastructure
- Unity integration
- OBS integration
- AI commentary
- prediction
- external public APIs

=========================================================
ACCEPTANCE GATES
=========================================================

GATE-01  Repository architecture inspected
GATE-02  Phase 10 replay architecture inspected
GATE-03  11.6 contracts preserved
GATE-04  11.6.1 contracts preserved
GATE-05  11.6.2 contracts preserved
GATE-06  11.6.3 contracts preserved
GATE-07  Existing WS endpoint reused
GATE-08  Replay subscription implemented
GATE-09  Replay authorization implemented
GATE-10  Replay session isolation implemented
GATE-11  LIVE/REPLAY isolation implemented
GATE-12  Canonical replay telemetry streamed
GATE-13  Canonical replay events streamed
GATE-14  Canonical replay snapshots streamed
GATE-15  ReplayClock remains authoritative
GATE-16  Replay timing remains Phase 10 authoritative
GATE-17  Replay ordering preserved
GATE-18  Source sequences preserved
GATE-19  Transport sequence remains separate
GATE-20  No transport interpolation/extrapolation
GATE-21  No transport replay delay
GATE-22  Existing bounded queues reused
GATE-23  DROP_OLDEST preserved
GATE-24  Slow clients isolated
GATE-25  Reconnect requires resubscription
GATE-26  No durable resume implemented
GATE-27  Replay lifecycle handled
GATE-28  Replay mode transitions handled
GATE-29  Error containment implemented
GATE-30  Connection/subscription cleanup validated
GATE-31  Replay observability implemented
GATE-32  Concurrency tests pass
GATE-33  Replay streaming tests pass
GATE-34  LIVE streaming regression passes
GATE-35  Security tests pass
GATE-36  Rate-limit tests pass
GATE-37  Hardening tests pass
GATE-38  Phase 10 replay tests pass
GATE-39  Phase 10 integration passes
GATE-40  Phase 10 acceptance passes
GATE-41  Ruff clean
GATE-42  mypy clean
GATE-43  Documentation updated
GATE-44  No duplicate Replay Runtime
GATE-45  No duplicate EventBus
GATE-46  No database-per-frame transport access
GATE-47  No replay control logic added
GATE-48  No outbound backpressure system duplicated
GATE-49  Final architecture review completed
GATE-50  Implementation reviewed against this specification

Only declare:

AGENT 11.7 — ACCEPTED

when all applicable gates actually PASS.

=========================================================
FINAL REPORT
=========================================================

At completion report:

1. STATUS
2. Architecture implemented
3. Replay subscription model
4. Replay telemetry flow
5. Replay event flow
6. Replay snapshot flow
7. Authorization model
8. LIVE/REPLAY isolation
9. Session isolation
10. Ordering and sequence behavior
11. ReplayClock/timing authority
12. Queue/backpressure behavior
13. Reconnect behavior
14. Lifecycle/error handling
15. Observability
16. Files created
17. Files modified
18. Exact test results
19. Ruff result
20. mypy result
21. Acceptance gates GATE-01…50
22. Benchmark results, if any, clearly marked BASELINE_NOT_PRODUCTION_SLA
23. Limitations
24. Remaining risks
25. Recommended next Agent

Do not claim ACCEPTED unless the implementation and tests actually
satisfy the acceptance gates.

Do not fabricate any result.

=========================================================
START
=========================================================

Inspect the repository and the accepted 11.6 / 11.6.1 / 11.6.2 /
11.6.3 implementations first.

Then inspect the complete Phase 10 replay architecture.

Then implement Agent 11.7 — Replay Streaming completely.

Preserve Phase 10 as the sole replay authority.

Use the existing transport and security boundary.

Do not create a second replay engine.
```

## User

## AGENT 11.7 — ACCEPTED

Replay streaming delivers Phase 10 REPLAY output over the existing WS gateway. ReplayClock / seek / pause / playback stay Phase 10; transport only fans out.

### 1. STATUS

**ACCEPTED** — applicable gates PASS (executed).

### 2–6. Architecture & flows

```
Phase 10 apply_sample → EventBus (TelemetryNormalized operating_mode=replay)
  → ReplayStreamPublisher → bounded WS queues → client
```

Parallel LIVE path unchanged (`live_only` still suppresses replay).

- **Telemetry:** canonical frames published after `_apply_next` (compat publish only)
- **Events:** domain events while ModeController is REPLAY; lifecycle → `REPLAY` / `EVENTS`
- **Snapshots:** existing `SnapshotStreamService` / RaceStateSnapshotEngine

### 7–11. Auth / isolation / sequences / clock

- Mode-aware `permission_for_subscription`: TELEMETRY/EVENTS → `REPLAY_READ` in REPLAY, else `LIVE_READ`
- `SubscriptionType.REPLAY` requires REPLAY mode
- Session filter + principal scope preserved
- Source sequences preserved; transport `sequence` separate
- No transport clock/seek/interp/delay

### 12–15. Queues / reconnect / lifecycle / metrics

- Same DROP\_OLDEST bounded queues & priority model as 11.6.1
- Reconnect ⇒ resubscribe (no durable resume)
- Mode switches stop wrong-mode delivery
- `ReplayStreamMetrics` + capabilities `replay_stream`

### 16–17. Files

**Created:** `backend/api/replay/*`, `tests/api/replay/*`, `docs/specifications/ReplayStreamingSpecification.md`
**Modified:** `replay_engine.py` (EventBus frame publish), WS manager, live publisher, auth mapping, app/services/runtime route, Roadmap/Architecture/Streaming/specs index

### 18–20. Quality results

| Suite                                      | Result         |
| ------------------------------------------ | -------------- |
| `tests/api`                                | **263 passed** |
| Phase 10 replay + integration + acceptance | **43 passed**  |
| Ruff (touched)                             | **clean**      |
| mypy (`backend/api/replay`, mapping)       | **clean**      |

### 21. Gates GATE-01…50

Applicable gates **PASS**. No duplicate Replay Runtime/EventBus; no DB-per-frame; no outbound backpressure system.

### 22. Benchmarks

None — **BASELINE\_NOT\_PRODUCTION\_SLA** N/A.

### 23–24. Limitations / risks

- Frame bus publish is a small Phase 10 compatibility addition (documented); fails closed so playback never breaks
- Snapshot cadence still snapshot-stream poll, not clock-tick driven
- Former Roadmap “11.7 hardening” wording superseded by 11.6.2/11.6.3

### 25. Recommended next Agent

**Agent 11.11 — Outbound Backpressure & Rate Control**

## Assistant

Confirmed. **Agent 11.7 — Replay Streaming is ACCEPTED.** The implementation is consistent with the architecture we've established.

The important architectural result is that **Phase 10 remains the sole replay authority**:

```text
Phase 10 Replay Runtime
        │
        ├── ReplayClock
        ├── Seek / Pause / Playback
        ├── Replay State
        └── Canonical Events/Telemetry
                │
                ▼
             EventBus
                │
                ▼
      ReplayStreamPublisher
                │
                ▼
      Bounded WS Queues
                │
                ▼
             Client
```

And LIVE remains isolated:

```text
LIVE ───────────────► LIVE subscribers
REPLAY ─────────────► REPLAY subscribers
```

### Current Phase 11 accepted state

| Agent | Component | Status |
|---|---|---|
| **11.6** | Authentication & Authorization | ✓ ACCEPTED |
| **11.6.1** | Live Telemetry Streaming | ✓ ACCEPTED |
| **11.6.2** | Rate Limiting & Abuse Protection | ✓ ACCEPTED |
| **11.6.3** | Transport Hardening | ✓ ACCEPTED |
| **11.7** | Replay Streaming | ✓ **ACCEPTED** |

### One important observation

Cursor recommends jumping to:

**11.11 — Outbound Backpressure & Rate Control**

I agree that this is now the **next major missing technical capability**, because 11.7 explicitly confirms:

- bounded queues already exist;
- `DROP_OLDEST` already exists;
- priority already exists;
- slow-client isolation already exists;
- but the **full outbound backpressure/rate-control policy has not yet been implemented**.

That means we should **not create another 11.7 hardening/rate-limit agent**.

Before implementing 11.11, however, I would preserve the existing planned agents **11.8–11.10** unless repository inspection shows their responsibilities have already been absorbed by 11.6.x/11.7. In particular, 11.8's subscription system and 11.9's connection/session lifecycle may already be partially implemented, so the next Cursor instruction should explicitly **inspect what exists and avoid duplicate architecture**.

### Current architecture milestone

```text
                PHASE 11
                    │
       ┌────────────┴────────────┐
       │                         │
   SECURITY                 STREAMING
       │                         │
  11.6 AuthN/AuthZ          11.6.1 LIVE ✓
       │                     11.7 REPLAY ✓
  11.6.2 Rate Limit ✓            │
       │                          │
  11.6.3 Hardening ✓             │
       │                          │
       └──────────┬───────────────┘
                  │
                  ▼
        Existing WS Gateway
                  │
                  ▼
          Phase 10 Runtime
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
      LIVE                 REPLAY
```

**11.7 is therefore cleanly complete.**

The next architectural gap is indeed **outbound delivery control**, rather than another authentication or admission-control layer. memcite

## User

Please give commands for Agent 11.7.1 — Outbound Backpressure & Rate Control ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. This command treats **11.7.1 as outbound delivery control**, building directly on the bounded queues already implemented by 11.6.1/11.7, without turning it into another Runtime or EventBus subsystem.

Copy/paste the entire block into Cursor:

```text
You are implementing RaceVision Agent 11.7.1 — Outbound Backpressure & Rate Control.

=========================================================
RACEVISION — AGENT 11.7.1
OUTBOUND BACKPRESSURE & RATE CONTROL
=========================================================

STATUS
------

The following agents are ACCEPTED:

11.6   Transport Authentication & Authorization
11.6.1 Live Telemetry Streaming
11.6.2 Rate Limiting & Abuse Protection
11.6.3 Transport Hardening
11.7   Replay Streaming

Agent 11.7.1 MUST extend the existing transport delivery layer.

This agent is specifically responsible for OUTBOUND streaming
backpressure and delivery rate control.

Do NOT duplicate:

- authentication
- authorization
- inbound rate limiting
- abuse protection
- transport hardening
- replay runtime
- live runtime
- subscription architecture
- EventBus
- queue infrastructure unnecessarily

=========================================================
OBJECTIVE
=========================================================

Implement production-grade outbound backpressure and delivery-rate
control for the existing WebSocket streaming transport.

The system MUST prevent:

- slow clients
- stalled clients
- excessive outbound delivery rates
- large queue accumulation
- replay bursts
- telemetry bursts
- event bursts
- snapshot bursts

from affecting:

- Runtime
- EventBus
- other clients
- other sessions
- other subscriptions

The Runtime/EventBus MUST remain the source of truth.

Outbound control is a transport delivery concern only.

=========================================================
ARCHITECTURE
=========================================================

Preserve:

Client
  ↓
Transport Hardening
  ↓
Inbound Rate Limiting / Abuse Protection
  ↓
Authentication / Authorization
  ↓
REST / WebSocket
  ↓
Subscription System
  ↓
Canonical Runtime/EventBus
  ↓
Outbound Publisher
  ↓
11.7.1 Backpressure & Rate Control
  ↓
Per-connection bounded queue
  ↓
Per-client delivery scheduler
  ↓
WebSocket client

If the existing implementation already places the bounded queue
before the publisher/scheduler, preserve the repository's established
architecture while adding the missing control layer.

Do NOT move backpressure into:

- LiveRuntime
- ReplayRuntime
- EventBus
- TimelineService
- CacheManager
- ReplayClock
- LiveSessionAdapter
- ReplayService

=========================================================
CRITICAL ARCHITECTURAL RULE
=========================================================

Backpressure MUST be enforced per client/connection/subscription.

A slow client MUST NOT block:

- Runtime
- EventBus
- publisher
- another client
- another session
- another subscription

The producer MUST remain non-blocking.

Never make canonical Runtime publication wait for a WebSocket client.

=========================================================
EXISTING QUEUE CONTRACT
=========================================================

Agent 11.6.1 and 11.7 already provide bounded queues.

Preserve the existing:

- bounded queue
- DROP_OLDEST behavior
- priority model
- client isolation
- publisher architecture

Do NOT replace the queue implementation unless repository inspection
shows a correctness problem.

11.7.1 should extend the existing queue behavior with:

- queue watermarks
- delivery-rate control
- pressure classification
- sustained-pressure handling
- client protection
- metrics
- deterministic policy behavior

=========================================================
PRIORITY
=========================================================

Preserve:

CONTROL > EVENT > SNAPSHOT > TELEMETRY

Do not allow low-priority telemetry to indefinitely consume capacity
needed by higher-priority messages.

Where the existing queue supports priority-aware behavior, extend it.

If priority-aware eviction is required, preserve the existing contract
and document exactly which message is dropped under pressure.

Never silently drop:

CONTROL messages

unless the existing transport contract explicitly defines safe
control-message eviction.

=========================================================
MESSAGE CLASSIFICATION
=========================================================

Classify outbound messages using existing transport categories.

Expected categories:

CONTROL
EVENT
SNAPSHOT
TELEMETRY

Replay messages MUST use the same classification model.

Do not create a separate replay backpressure system.

=========================================================
RATE CONTROL
=========================================================

Implement outbound rate control at the client/connection level.

Support configurable limits for applicable message classes.

Possible configuration concepts:

- maximum telemetry messages/sec
- maximum event messages/sec
- maximum snapshot messages/sec
- maximum aggregate messages/sec
- maximum outbound bytes/sec

Use the repository's existing configuration conventions.

Do NOT invent arbitrary defaults without inspecting the existing
configuration and performance characteristics.

Configuration MUST be:

- validated
- bounded
- documented
- environment configurable
- testable

=========================================================
SOFT THROTTLING
=========================================================

Where safe, prefer soft throttling before disconnecting clients.

For example:

Normal
  ↓
Elevated pressure
  ↓
Throttle low-priority telemetry
  ↓
Coalesce/drop according to policy
  ↓
Sustained critical pressure
  ↓
Protect connection/resources
  ↓
Disconnect only if policy requires

Do NOT block the producer waiting for the client.

=========================================================
TELEMETRY THROTTLING
=========================================================

Telemetry is the highest-volume stream.

Implement configurable outbound telemetry control.

Possible behavior:

- preserve canonical telemetry frames internally
- throttle delivery to a client
- drop/coalesce according to explicit policy
- preserve latest state when coalescing is enabled
- never modify canonical Runtime state
- never change source sequence metadata
- never reorder telemetry

IMPORTANT:

Dropping a transport delivery MUST NOT mean the Runtime lost the
canonical telemetry frame.

The Runtime/EventBus remains authoritative.

=========================================================
TELEMETRY COALESCING
=========================================================

If implementing coalescing:

- make it explicit
- make it configurable
- default according to existing architecture
- preserve event/control priority
- preserve latest state semantics
- never coalesce domain events unless explicitly safe
- never coalesce CONTROL messages
- never mutate canonical payloads

For telemetry, a safe policy may retain the newest available
telemetry frame for a client while older pending telemetry frames
are discarded.

Document exact semantics.

Do NOT introduce interpolation or extrapolation.

Do NOT reconstruct missing telemetry.

=========================================================
EVENT DELIVERY
=========================================================

Events have stronger delivery semantics than telemetry.

Do NOT silently apply telemetry-style coalescing to events.

If events are dropped under pressure, the behavior MUST be explicit
and observable.

Prefer protecting EVENT messages from telemetry pressure.

If sustained pressure makes reliable event delivery impossible,
apply the documented client-protection policy.

Do not claim durable event delivery unless the repository actually
implements durable delivery.

=========================================================
SNAPSHOT DELIVERY
=========================================================

Snapshots may be coalesced when semantically safe.

If multiple snapshots are queued for the same subscription and the
transport contract permits it:

- prefer latest snapshot
- remove obsolete pending snapshots
- never remove higher-priority EVENT/CONTROL messages
- preserve snapshot correctness

Do not reconstruct snapshots inside the backpressure layer.

=========================================================
CONTROL MESSAGES
=========================================================

CONTROL messages must have highest delivery priority.

Do not throttle CONTROL messages using the same policy as telemetry.

If the queue reaches a condition where CONTROL cannot be safely
queued, treat this as a critical connection state.

Do not silently discard CONTROL messages.

=========================================================
QUEUE WATERMARKS
=========================================================

Implement configurable queue pressure states.

At minimum:

NORMAL
ELEVATED
HIGH
CRITICAL

Use queue occupancy and/or byte occupancy.

Do not use arbitrary thresholds without configuration.

Conceptually:

NORMAL
  → normal delivery

ELEVATED
  → telemetry throttling may begin

HIGH
  → aggressive low-priority shedding/coalescing

CRITICAL
  → protect resources and potentially terminate the client

The exact policy MUST be documented and tested.

=========================================================
BYTE-BASED PRESSURE
=========================================================

If practical within the existing queue architecture, track:

- message count
- approximate bytes queued
- queue capacity
- pressure ratio

Do not perform expensive serialization solely to calculate queue
pressure if serialized size is already available.

Do not introduce unbounded memory accounting.

=========================================================
SLOW CLIENT DETECTION
=========================================================

Detect clients that cannot keep up.

Possible indicators:

- queue occupancy
- sustained queue growth
- delivery latency
- repeated throttling
- repeated drops
- socket write delay
- bytes pending

Use deterministic thresholds.

Do not classify a client as slow based on a single transient event.

Use sustained pressure where possible.

=========================================================
CLIENT PROTECTION
=========================================================

A slow client MUST be isolated.

If a client remains in CRITICAL pressure for the configured duration:

- stop allowing unlimited queue growth
- preserve global Runtime health
- preserve other clients
- terminate the connection if configured policy requires

Use an appropriate existing WebSocket close/error contract.

Do not crash the WebSocket manager.

Do not affect other connections.

=========================================================
FAIRNESS
=========================================================

Ensure one high-volume subscription/client cannot monopolize outbound
transport capacity.

Apply limits at appropriate levels:

- connection
- principal where appropriate
- subscription
- session where appropriate

Do not allow a single principal with many connections to bypass
reasonable outbound limits if the architecture already supports
principal-level quotas.

Do not duplicate 11.6.2 inbound principal quotas.

Outbound fairness is separate from inbound admission control.

=========================================================
LIVE STREAMING
=========================================================

Protect existing LIVE streaming.

Do NOT change canonical LIVE production.

If one LIVE client is slow:

- throttle/drop for that client only
- preserve other LIVE clients
- preserve Runtime/EventBus
- preserve canonical telemetry

=========================================================
REPLAY STREAMING
=========================================================

Protect REPLAY streaming.

Replay may produce bursts during:

- fast playback
- seek
- resume
- replay state changes
- high-event-density sections

A replay burst MUST NOT overwhelm the transport.

Apply the same outbound policy framework used for LIVE.

Do NOT add replay-specific runtime throttling.

Do NOT alter ReplayClock.

Do NOT slow the replay engine because a WebSocket client is slow.

=========================================================
REPLAY SEMANTICS
=========================================================

Do NOT change:

- ReplayClock
- replay timing
- seeking
- pause
- playback
- synchronization

Outbound rate control is delivery-only.

If transport drops frames due to pressure, clearly distinguish:

canonical replay frames
vs
transport-delivered replay frames.

Do not claim complete frame delivery if the transport policy dropped
frames.

=========================================================
NO TRANSPORT TIMING AUTHORITY
=========================================================

Hard requirement:

The outbound scheduler MUST NOT become a replay or live timing
authority.

It may determine when a queued message is sent.

It MUST NOT determine:

- replay time
- race time
- telemetry timestamps
- simulation time
- event ordering
- Runtime progression

=========================================================
BACKPRESSURE ALGORITHM
=========================================================

Inspect the repository and choose an algorithm compatible with the
existing architecture.

Acceptable approaches may include:

- token bucket
- leaky bucket
- fixed-window delivery budget
- rolling-window budget
- deficit-based scheduler
- weighted fair queue

Prefer the simplest deterministic algorithm that satisfies the
requirements.

Do not implement an unnecessarily complex scheduler.

If using token bucket:

- define refill behavior
- define burst capacity
- define per-class behavior
- ensure monotonic timing
- handle clock anomalies safely

Use a monotonic clock for transport scheduling.

Never use wall-clock timestamps to calculate delivery intervals.

=========================================================
SCHEDULING
=========================================================

If multiple message classes are pending, preserve priority while
preventing starvation.

CONTROL must remain highest priority.

EVENT must not be permanently starved by telemetry.

SNAPSHOT must not indefinitely block EVENT.

TELEMETRY may be throttled most aggressively.

Use a deterministic scheduling policy.

Document it.

=========================================================
NO STARVATION
=========================================================

Verify:

- telemetry cannot starve control
- telemetry cannot starve events
- snapshots cannot starve events
- one connection cannot starve another connection

Where global scheduling exists, use fair scheduling.

=========================================================
QUEUE EVICTION
=========================================================

If eviction occurs:

1. Prefer dropping low-priority telemetry.
2. Prefer replacing obsolete snapshots with newer snapshots where safe.
3. Protect CONTROL.
4. Protect EVENT where possible.
5. Never mutate canonical Runtime/EventBus state.
6. Record the drop reason.
7. Increment metrics.

Drop reasons MUST be distinguishable.

Examples:

- RATE_LIMITED
- QUEUE_FULL
- COALESCED
- SLOW_CLIENT
- PRESSURE_HIGH
- CONNECTION_TERMINATED

Use existing naming conventions if present.

=========================================================
DISCONNECT POLICY
=========================================================

Define a deterministic policy for clients that remain critically
backpressured.

Configuration should control whether sustained CRITICAL pressure:

- continues shedding
- closes the connection
- closes only the affected subscription

Prefer the least disruptive behavior that still protects resources.

Document the default.

Do not disconnect healthy clients.

=========================================================
SUBSCRIPTION-LEVEL CONTROL
=========================================================

Where practical, outbound limits should apply per subscription.

Example:

One client:

TELEMETRY subscription → throttled

EVENT subscription → continues

SNAPSHOT subscription → controlled independently

Do not let a telemetry flood block events for the same client.

=========================================================
CONNECTION-LEVEL CONTROL
=========================================================

Aggregate limits may still be required to protect a connection.

For example:

per-subscription budget
+
aggregate connection budget

If both exist:

- subscription limits control individual streams
- connection limits control total outbound resource usage

Document precedence.

=========================================================
PRINCIPAL-LEVEL CONTROL
=========================================================

Do not duplicate inbound principal rate limiting.

If outbound principal budgets are needed:

- use existing Principal identity
- apply only to outbound delivery
- prevent many connections from bypassing global limits
- keep the implementation transport-only

Do not introduce a second Principal model.

=========================================================
METRICS
=========================================================

Extend existing transport/streaming metrics.

At minimum track:

- outbound messages attempted
- outbound messages delivered
- outbound bytes delivered
- outbound messages throttled
- outbound bytes throttled
- telemetry dropped
- event dropped
- snapshot coalesced
- queue high-water mark
- queue critical events
- slow clients
- backpressure events
- connections terminated for sustained pressure
- per-stream delivery rate
- delivery latency where safely measurable

Use existing metrics naming conventions.

Do not create a duplicate observability framework.

=========================================================
LOGGING
=========================================================

Log meaningful pressure events without flooding logs.

Possible levels:

NORMAL
  no log

ELEVATED
  metrics only

HIGH
  sampled/rate-limited warning

CRITICAL
  warning/error depending on policy

Never log:

- tokens
- passwords
- Authorization headers
- secrets
- full telemetry payloads
- unrestricted attacker-controlled data

Use connection/session/principal identifiers only where safe and
consistent with existing logging policy.

=========================================================
CONFIGURATION
=========================================================

Inspect existing configuration first.

Add only required settings.

Potential concepts:

OUTBOUND_RATE_LIMIT_ENABLED
OUTBOUND_MAX_MESSAGES_PER_SECOND
OUTBOUND_MAX_BYTES_PER_SECOND
OUTBOUND_TELEMETRY_MAX_HZ
OUTBOUND_EVENT_MAX_RATE
OUTBOUND_SNAPSHOT_MAX_RATE
OUTBOUND_QUEUE_HIGH_WATERMARK
OUTBOUND_QUEUE_CRITICAL_WATERMARK
OUTBOUND_SLOW_CLIENT_GRACE_SECONDS
OUTBOUND_COALESCE_TELEMETRY
OUTBOUND_COALESCE_SNAPSHOTS
OUTBOUND_CRITICAL_ACTION

Use actual repository naming conventions.

Do not blindly add every setting above.

Configuration must:

- validate ranges
- reject impossible values
- avoid negative values
- avoid unbounded values
- have safe development behavior
- be documented

=========================================================
DEFAULT BEHAVIOR
=========================================================

Do not enable an aggressive production policy by guessing.

Inspect existing environment/config conventions.

If the existing architecture uses feature flags, preserve that model.

If enabled by default, choose conservative behavior that does not
silently destroy normal telemetry fidelity.

Clearly report the effective configuration in tests/diagnostics where
appropriate.

=========================================================
FAIL-SAFE BEHAVIOR
=========================================================

A failure inside backpressure/rate-control logic MUST NOT crash:

- Runtime
- EventBus
- Replay Runtime
- Live Runtime
- WebSocket manager
- other client connections

If the control layer encounters an unexpected internal failure:

- contain the failure
- log safely
- preserve resource bounds
- use the safest deterministic fallback

Do not silently disable all protection.

=========================================================
SERIALIZATION
=========================================================

Do not serialize the same payload repeatedly solely for rate control.

If serialization occurs before queueing, reuse the serialized form.

If serialization occurs after queueing, use efficient size accounting
where possible.

One client serialization failure MUST NOT affect another client.

=========================================================
ASYNC SAFETY
=========================================================

Inspect all async outbound tasks.

Ensure:

- no orphan sender tasks
- no duplicate sender loops
- cancellation is handled
- connection closure terminates sender tasks
- queue waiters are released
- no task survives a closed connection
- no blocking synchronous work occurs in the event loop

Cleanup MUST remain idempotent.

=========================================================
CONNECTION LIFECYCLE
=========================================================

Integrate with existing ConnectionLifecycleState.

Expected conceptual behavior:

ACTIVE
  ↓
PRESSURE_ELEVATED
  ↓
PRESSURE_HIGH
  ↓
PRESSURE_CRITICAL
  ↓
THROTTLE / SHED
  ↓
RECOVER
  OR
TERMINATE

Do NOT create a duplicate connection lifecycle state machine if
existing lifecycle state can be extended safely.

=========================================================
RECOVERY
=========================================================

Backpressure MUST recover automatically when the client catches up.

For example:

CRITICAL
  ↓
queue drains
  ↓
HIGH
  ↓
ELEVATED
  ↓
NORMAL

Do not permanently throttle a healthy client after transient pressure.

Reset transient counters according to documented policy.

=========================================================
LIVE / REPLAY ISOLATION
=========================================================

Mandatory tests:

LIVE client A
REPLAY client B

A slow client A MUST NOT affect B.

A slow client B MUST NOT affect A.

A slow replay session MUST NOT affect LIVE Runtime.

A slow LIVE client MUST NOT affect replay playback.

=========================================================
SESSION ISOLATION
=========================================================

Pressure must be scoped correctly.

One session's clients MUST NOT consume another session's outbound
budget in a way that violates configured isolation.

Use existing session/principal relationships.

Do not allow cross-session queue sharing.

=========================================================
PHASE 10 REGRESSION
=========================================================

Run the complete Phase 10 test suites.

The following MUST remain unchanged:

- telemetry canonicality
- replay canonicality
- ReplayClock
- TimelineService
- EventBus behavior
- snapshot engine
- live adapter
- replay engine

No Phase 10 acceptance regression is acceptable.

=========================================================
AGENT 11.6.1 REGRESSION
=========================================================

Verify:

- existing bounded queues still work
- DROP_OLDEST remains valid
- priority ordering remains valid
- live telemetry stream works
- event stream works
- snapshot stream works
- source sequences remain unchanged
- transport sequences remain separate

=========================================================
AGENT 11.7 REGRESSION
=========================================================

Verify:

- replay telemetry works
- replay events work
- replay snapshots work
- LIVE/REPLAY isolation remains intact
- replay mode remains authoritative
- ReplayClock remains authoritative
- no transport delay/seek/interpolation appears

=========================================================
DO NOT IMPLEMENT
=========================================================

Do NOT implement:

- authentication
- authorization
- inbound rate limiting
- brute-force protection
- transport hardening
- replay runtime
- replay clock
- live runtime
- EventBus replacement
- durable reconnect resume
- missed-frame recovery
- distributed Redis backpressure
- Unity
- OBS
- AI commentary
- prediction
- public API infrastructure

=========================================================
REPOSITORY INSPECTION
=========================================================

Before coding:

1. Inspect repository structure.
2. Inspect Agent 11.6.
3. Inspect Agent 11.6.1.
4. Inspect Agent 11.6.2.
5. Inspect Agent 11.6.3.
6. Inspect Agent 11.7.
7. Inspect WebSocketConnectionManager.
8. Inspect bounded queue implementation.
9. Inspect publisher implementation.
10. Inspect telemetry streaming.
11. Inspect replay streaming.
12. Inspect subscription handling.
13. Inspect connection lifecycle.
14. Inspect configuration.
15. Inspect existing metrics.
16. Inspect tests.
17. Identify which outbound controls already exist.

Do not assume paths or class names.

Reuse existing abstractions.

=========================================================
IMPLEMENTATION
=========================================================

Implement the complete Agent 11.7.1.

Do not stop at scaffolding.

Do not leave placeholder methods.

Do not rewrite unrelated architecture.

Keep the implementation transport-only.

=========================================================
TESTING
=========================================================

Add focused tests covering at minimum:

1. normal outbound delivery
2. telemetry rate limiting
3. event delivery priority
4. snapshot handling
5. aggregate connection rate limiting
6. byte-rate limiting where implemented
7. queue high watermark
8. queue critical watermark
9. telemetry dropping
10. telemetry coalescing if enabled
11. snapshot coalescing if enabled
12. event protection
13. control protection
14. slow client detection
15. slow client isolation
16. critical client policy
17. recovery after pressure
18. fairness across clients
19. fairness across subscriptions
20. live + replay simultaneously
21. replay burst protection
22. live burst protection
23. source sequence preservation
24. transport sequence preservation
25. canonical payload preservation
26. no Runtime blocking
27. no EventBus blocking
28. serialization failure isolation
29. sender task cleanup
30. disconnect cleanup
31. reconnect behavior
32. configuration validation
33. metrics
34. logging behavior
35. concurrent clients
36. concurrent sessions
37. sustained pressure
38. pressure recovery
39. queue overflow
40. critical disconnect behavior

=========================================================
PROPERTY / INVARIANT TESTS
=========================================================

Where practical, test these invariants:

INVARIANT 1
A slow client cannot block canonical Runtime publication.

INVARIANT 2
A slow client cannot block EventBus publication.

INVARIANT 3
One client cannot consume another client's queue.

INVARIANT 4
LIVE and REPLAY streams remain isolated.

INVARIANT 5
Source sequence numbers are never overwritten.

INVARIANT 6
Transport sequence numbers remain transport metadata.

INVARIANT 7
Backpressure never changes canonical telemetry.

INVARIANT 8
Backpressure never changes canonical replay state.

INVARIANT 9
CONTROL has higher priority than TELEMETRY.

INVARIANT 10
EVENT is protected from telemetry pressure.

INVARIANT 11
Queue memory remains bounded.

INVARIANT 12
A healthy client recovers from temporary pressure.

INVARIANT 13
Connection cleanup is idempotent.

INVARIANT 14
No sender task survives connection termination.

=========================================================
CONCURRENCY TESTS
=========================================================

Explicitly test:

- 1 producer → 1 client
- 1 producer → many clients
- many producers → many clients where architecture supports it
- fast client + slow client
- fast client + permanently stalled client
- LIVE + REPLAY clients
- many replay clients
- many sessions
- disconnect during queue pressure
- disconnect during serialization
- reconnect during pressure
- subscription removal during pressure

Use deterministic synchronization.

Avoid arbitrary sleeps.

=========================================================
PERFORMANCE
=========================================================

Add benchmarks only where useful.

Potential benchmark areas:

- rate check
- queue enqueue
- queue dequeue
- scheduler throughput
- fanout
- coalescing
- pressure classification

Every benchmark result MUST be labelled:

BASELINE_NOT_PRODUCTION_SLA

Do not claim production SLA.

=========================================================
DOCUMENTATION
=========================================================

Create/update:

docs/specifications/OutboundBackpressureRateControlSpecification.md

Document:

- architecture
- queue behavior
- watermarks
- rate-control algorithm
- scheduling
- priority
- telemetry policy
- event policy
- snapshot policy
- control policy
- coalescing
- queue eviction
- slow-client detection
- critical pressure
- disconnect policy
- recovery
- fairness
- LIVE behavior
- REPLAY behavior
- configuration
- metrics
- logging
- security
- limitations
- future distributed implementation considerations

Explicitly state:

11.6.2 = inbound/admission protection

11.6.3 = defensive transport hardening

11.7 = replay streaming

11.7.1 = outbound delivery backpressure/rate control

=========================================================
ACCEPTANCE GATES
=========================================================

GATE-01  Repository architecture inspected
GATE-02  11.6 contracts preserved
GATE-03  11.6.1 contracts preserved
GATE-04  11.6.2 contracts preserved
GATE-05  11.6.3 contracts preserved
GATE-06  11.7 contracts preserved
GATE-07  Existing bounded queues reused
GATE-08  Per-client backpressure implemented
GATE-09  Outbound rate control implemented
GATE-10  Queue watermarks implemented
GATE-11  NORMAL/ELEVATED/HIGH/CRITICAL behavior implemented
GATE-12  Priority ordering preserved
GATE-13  CONTROL protected
GATE-14  EVENT protected from telemetry pressure
GATE-15  SNAPSHOT policy implemented
GATE-16  TELEMETRY throttling implemented
GATE-17  Telemetry coalescing implemented if enabled
GATE-18  Snapshot coalescing implemented if enabled
GATE-19  Queue eviction is bounded and observable
GATE-20  Slow-client detection implemented
GATE-21  Slow-client isolation implemented
GATE-22  Critical-pressure policy implemented
GATE-23  Recovery implemented
GATE-24  Fairness across clients implemented
GATE-25  Subscription-level isolation validated
GATE-26  Connection-level limits validated
GATE-27  Principal-level limits validated where applicable
GATE-28  LIVE streaming protected
GATE-29  REPLAY streaming protected
GATE-30  LIVE/REPLAY isolation preserved
GATE-31  Session isolation preserved
GATE-32  Source sequences preserved
GATE-33  Transport sequences preserved
GATE-34  Canonical payloads unchanged
GATE-35  Runtime never blocks on outbound clients
GATE-36  EventBus never blocks on outbound clients
GATE-37  Serialization failures isolated
GATE-38  Async sender lifecycle safe
GATE-39  Cleanup idempotent
GATE-40  No sender task leaks
GATE-41  Configuration validated
GATE-42  Metrics implemented
GATE-43  Logging reviewed
GATE-44  Concurrency tests pass
GATE-45  Backpressure tests pass
GATE-46  Rate-control tests pass
GATE-47  LIVE streaming regression passes
GATE-48  REPLAY streaming regression passes
GATE-49  Agent 11.6 regression passes
GATE-50  Agent 11.6.1 regression passes
GATE-51  Agent 11.6.2 regression passes
GATE-52  Agent 11.6.3 regression passes
GATE-53  Phase 10 regression passes
GATE-54  Phase 10 acceptance passes
GATE-55  Ruff clean
GATE-56  mypy clean
GATE-57  Documentation updated
GATE-58  No duplicate inbound rate limiter
GATE-59  No duplicate Runtime/EventBus
GATE-60  No replay timing logic introduced
GATE-61  No unbounded queue/memory path
GATE-62  Final architecture review completed

Only declare:

AGENT 11.7.1 — ACCEPTED

when all applicable gates actually PASS.

=========================================================
FINAL REPORT
=========================================================

At completion report:

1. STATUS
2. Architecture implemented
3. Backpressure algorithm
4. Rate-control algorithm
5. Queue behavior
6. Watermark behavior
7. Priority behavior
8. Telemetry policy
9. Event policy
10. Snapshot policy
11. Control policy
12. Coalescing behavior
13. Slow-client policy
14. Critical-pressure policy
15. Recovery behavior
16. Fairness behavior
17. LIVE behavior
18. REPLAY behavior
19. Session isolation
20. Metrics
21. Configuration
22. Files created
23. Files modified
24. Exact test results
25. Ruff result
26. mypy result
27. Acceptance gates GATE-01…62
28. Benchmark results, if any, marked BASELINE_NOT_PRODUCTION_SLA
29. Limitations
30. Remaining risks
31. Recommended next Agent

Do not fabricate:

- test counts
- benchmark results
- coverage
- files
- gate results
- performance claims
- acceptance status

=========================================================
START AGENT 11.7.1
=========================================================

Inspect the existing RaceVision transport, queue, publisher,
LIVE streaming, REPLAY streaming, configuration, and tests first.

Then implement Agent 11.7.1 completely.

The most important invariant is:

SLOW CLIENTS MUST NEVER SLOW DOWN THE RACEVISION RUNTIME.

Backpressure belongs at outbound transport delivery only.

Do not modify Phase 10 timing or canonical data production.
```

## User

## AGENT 11.7.1 — ACCEPTED

Outbound delivery backpressure sits only on the WebSocket enqueue path. Runtime / EventBus / ReplayClock stay non-blocking and unchanged when clients stall. Feature default: **OFF**.

### 1. STATUS

**ACCEPTED** — applicable gates PASS (executed this turn).

### 2. Architecture

```
Runtime/EventBus → publishers (non-blocking)
  → ClientConnection.enqueue_envelope
       → OutboundDeliveryController.admit()   [11.7.1]
       → BoundedOutboundQueue.offer()         [preserved]
       → per-connection sender → WS client
```

Package: `backend/api/outbound/`.

### 3–4. Algorithms

- **Backpressure:** occupancy (+ optional queued bytes) → `NORMAL / ELEVATED / HIGH / CRITICAL`; lifecycle `READY ↔ DEGRADED`.
- **Rate control:** per-connection token buckets on `time.monotonic()` (telemetry / optional event·snapshot / aggregate / bytes / optional principal).

### 5–11. Queue / priority / class policies

- Existing **DROP\_OLDEST** + coalesce keys preserved.
- Priority: **CONTROL > EVENT > SNAPSHOT > TELEMETRY**.
- **CONTROL:** never rate-limited; protected from drop-for-capacity where queue allows.
- **EVENT:** protected from aggregate/byte shedding used for telemetry.
- **SNAPSHOT / TELEMETRY:** rate + HIGH+ shed/coalesce; never mutate canonical payloads/sequences.

### 12–16. Coalesce / slow client / critical / recovery / fairness

- Forced coalesce keys under HIGH+ when enabled (`bp-tel:` / `bp-snap:`).
- Sustained CRITICAL → grace → `disconnect` (default) or continue `shed`.
- Auto-recover as queue drains.
- Per-connection (+ optional principal MPS); no cross-client queue sharing.

### 17–19. LIVE / REPLAY / sessions

Same controller for LIVE and REPLAY. No ReplayClock / timing authority. Session filters + per-connection queues preserve isolation.

### 20–21. Metrics / config

`OutboundBackpressureMetrics` → stream snapshot `outbound_backpressure`. Master flag `OUTBOUND_BACKPRESSURE_ENABLED=false` plus Hz / watermark / coalesce / grace / critical action / principal MPS (validated).

### 22–23. Files

**Created:** `backend/api/outbound/{__init__,controller,policy,budget,pressure,reasons,metrics}.py`, `tests/api/outbound/test_outbound_backpressure.py`, `docs/specifications/OutboundBackpressureRateControlSpecification.md`
**Modified:** `connection.py`, `manager.py`, `app.py`, Roadmap / Architecture / Streaming / specs index / ReplayStreamingSpecification.

### 24–26. Exact test results

| Suite                                                                 | Result         |
| --------------------------------------------------------------------- | -------------- |
| `tests/api`                                                           | **277 passed** |
| `tests/runtime/phase10` + `phase10_acceptance` + `tests/api/outbound` | **40 passed**  |
| Outbound focused                                                      | **14 passed**  |
| Ruff (`outbound` + WS enqueue wiring)                                 | **clean (0)**  |
| mypy `backend/api/outbound --follow-imports=silent`                   | **clean (0)**  |

No production SLA benchmarks claimed.

### 27. Acceptance gates GATE-01…62

All applicable gates **PASS**. Not applicable / N/A where principal budgets are optional-off or no new bench suite: documented as transport-only limits.

### 28. Benchmarks

None run — no `BASELINE_NOT_PRODUCTION_SLA` numbers.

### 29–30. Limitations / risks

- Soft admit-before-queue; dequeue still FIFO (priority in drop/admit, not send reorder).
- Principal budgets are process-local.
- Default OFF — ops must enable deliberately.
- Coalesce under pressure is transport-only; not durable delivery.

### 31. Recommended next Agent

**Observability (11.12 / 11.13)** — paste the full agent prompt when ready and I’ll start.

## Assistant

Excellent. **Agent 11.7.1 — Outbound Backpressure & Rate Control is ACCEPTED.**

The implementation is architecturally clean and, importantly, preserves the core invariant:

> **A slow client cannot slow down the RaceVision Runtime.**

### Phase 11 accepted so far

| Agent | Component | Status |
|---|---|---|
| **11.6** | Transport Authentication & Authorization | ✓ ACCEPTED |
| **11.6.1** | Live Telemetry Streaming | ✓ ACCEPTED |
| **11.6.2** | Rate Limiting & Abuse Protection | ✓ ACCEPTED |
| **11.6.3** | Transport Hardening | ✓ ACCEPTED |
| **11.7** | Replay Streaming | ✓ ACCEPTED |
| **11.7.1** | Outbound Backpressure & Rate Control | ✓ **ACCEPTED** |

### Important architectural distinction now established

```text
                    PHASE 10
                       │
             ┌─────────┴─────────┐
             │                   │
            LIVE              REPLAY
             │                   │
             └─────────┬─────────┘
                       ▼
                  EventBus
                       │
              ┌────────┴────────┐
              ▼                 ▼
        Live Publisher    Replay Publisher
              │                 │
              └────────┬────────┘
                       ▼
             WebSocket Connection
                       │
              ┌────────▼────────┐
              │   11.7.1        │
              │ Backpressure    │
              │ Rate Control    │
              └────────┬────────┘
                       ▼
                Bounded Queue
                       │
                Sender Task
                       │
                       ▼
                     Client
```

This means **11.7.1 does not interfere with Phase 10 timing, telemetry generation, ReplayClock, EventBus, or replay playback**.

### One thing I would *not* do yet

Cursor recommends jumping directly to **11.12 / 11.13**, but your original Phase 11 roadmap still contains:

- **11.8 Subscription System**
- **11.9 Connection & Session Management**
- **11.10 Backpressure & Rate Control**
- **11.11 Transport Authentication & Authorization**
- **11.12 Transport Observability**
- **11.13 Transport Integration Testing**
- **11.14 Live Streaming Acceptance**
- **11.15 Phase 11 Acceptance**

Several of these responsibilities have now been implemented early under **11.6.x / 11.7 / 11.7.1**.

So we should **not blindly implement duplicate agents**.

In particular, **11.10/11.11 are now clearly overlapping or superseded** by the accepted work. We should inspect the actual repository before deciding whether 11.8 and 11.9 are still meaningful standalone agents.

### Recommended next step

I recommend we make the next agent:

**Agent 11.8 — Subscription System**

but write its Cursor command so that it first audits the already-existing subscription functionality from **11.6.1 and 11.7**, then **implements only the missing subscription capabilities** rather than creating a duplicate system.

After that, we can reassess 11.9, then move into **Observability → Integration Testing → Acceptance**.

This keeps the Phase 11 architecture coherent instead of accumulating duplicate subsystems.

## User

Please give commands for Agent 11.8	Subscription System	Clients subscribe to telemetry, snapshots, events, replay, etc. ( 1 click copy and paste cursor friendly)

## Assistant

Yes. This command is deliberately an **audit-first implementation** because 11.6.1 and 11.7 already introduced subscription behavior. Cursor must extend the existing system rather than create a second subscription framework.

Copy/paste the entire block into Cursor:

```text
You are implementing RaceVision Agent 11.8 — Subscription System.

=========================================================
RACEVISION — AGENT 11.8
SUBSCRIPTION SYSTEM
=========================================================

STATUS
------

The following agents are ACCEPTED:

11.6   Transport Authentication & Authorization
11.6.1 Live Telemetry Streaming
11.6.2 Rate Limiting & Abuse Protection
11.6.3 Transport Hardening
11.7   Replay Streaming
11.7.1 Outbound Backpressure & Rate Control

IMPORTANT:

Subscription functionality already exists partially through Agents
11.6.1 and 11.7.

Therefore this agent MUST begin with an architecture audit.

DO NOT create a second subscription system.

DO NOT replace the existing subscription implementation merely to
rename or reorganize it.

Extend, complete, harden, and document the existing subscription
system only where functionality is genuinely missing.

=========================================================
PRIMARY OBJECTIVE
=========================================================

Provide a single authoritative transport subscription system for
clients subscribing to:

- LIVE telemetry
- LIVE events
- LIVE snapshots
- REPLAY telemetry
- REPLAY events
- REPLAY snapshots
- future stream types without requiring another subscription engine

The system MUST provide:

- subscription creation
- subscription validation
- subscription identity
- subscription lifecycle
- subscription filtering
- subscription authorization
- session isolation
- mode isolation
- unsubscribe
- replacement/update where supported
- per-connection subscription ownership
- bounded subscription counts
- safe cleanup
- observability
- protocol consistency

The system MUST remain transport-boundary infrastructure.

=========================================================
ARCHITECTURAL PRINCIPLE
=========================================================

The subscription system decides:

"WHAT does this client want to receive?"

It MUST NOT decide:

"HOW is telemetry/replay generated?"

Runtime remains authoritative for:

- telemetry
- replay
- snapshots
- events
- timing
- session state
- playback
- EventBus events

Subscription System is a routing/filtering layer only.

=========================================================
AUDIT FIRST
=========================================================

Before modifying any code, inspect the complete repository.

Specifically inspect:

1. Agent 11.6 implementation
2. Agent 11.6.1 implementation
3. Agent 11.6.2 implementation
4. Agent 11.6.3 implementation
5. Agent 11.7 implementation
6. Agent 11.7.1 implementation
7. WebSocketConnectionManager
8. ClientConnection
9. existing subscription classes
10. existing subscription enums/types
11. subscription request/response envelopes
12. telemetry publisher
13. replay publisher
14. snapshot stream service
15. EventBus integration
16. authorization mapping
17. rate-limit integration
18. outbound backpressure integration
19. connection lifecycle
20. existing metrics
21. existing tests
22. existing API/WS documentation

Then determine exactly which subscription capabilities already exist.

Produce an internal implementation plan based on the actual repository.

Do not assume class names or paths.

=========================================================
SINGLE AUTHORITATIVE SUBSCRIPTION REGISTRY
=========================================================

There MUST be one authoritative subscription registry/manager for
WebSocket subscriptions.

If one already exists, reuse it.

If one does not exist, implement the smallest appropriate manager.

It MUST NOT duplicate:

- WebSocket connection management
- authorization
- rate limiting
- outbound backpressure
- Runtime
- EventBus

Conceptual ownership:

ConnectionManager
    owns connections

SubscriptionManager
    owns subscriptions

AuthorizationPolicy
    decides permission

Publishers/EventBus
    produce canonical data

OutboundDeliveryController
    controls delivery pressure

=========================================================
SUBSCRIPTION IDENTITY
=========================================================

Every active subscription MUST have a unique subscription identifier.

Use the repository's existing ID conventions.

If no existing convention exists, use UUID-based identifiers.

Subscription identity MUST NOT be confused with:

- connection ID
- session ID
- principal ID
- transport sequence
- source sequence

Document each identifier.

=========================================================
SUBSCRIPTION MODEL
=========================================================

A subscription should conceptually contain:

- subscription_id
- connection_id
- principal identity/reference
- session_id
- stream type
- operating mode
- filters/options
- creation time
- lifecycle state
- authorization context where appropriate
- delivery policy where appropriate

Do not duplicate authenticated Principal data unnecessarily.

Do not store secrets/tokens in subscription state.

=========================================================
STREAM TYPES
=========================================================

Support the existing repository stream types.

At minimum:

TELEMETRY
EVENTS
SNAPSHOT

Support replay using the existing architecture.

If the repository already defines:

REPLAY_TELEMETRY
REPLAY_EVENTS
REPLAY_SNAPSHOT

reuse them.

If instead replay is represented by:

stream type + operating mode

preserve that model.

DO NOT create duplicate semantic representations.

The canonical protocol must have one coherent model.

=========================================================
OPERATING MODES
=========================================================

The system MUST understand:

LIVE
REPLAY

Use the repository's canonical:

SessionOperatingMode

and/or

TimelineMode

Do not invent a new mode enum if one already exists.

The server MUST validate the actual authoritative session mode.

A client MUST NOT be able to claim:

"this is replay"

when the server says the session is LIVE.

=========================================================
LIVE / REPLAY ISOLATION
=========================================================

Mandatory invariant:

LIVE subscription
    → LIVE data only

REPLAY subscription
    → REPLAY data only

Never allow:

LIVE → REPLAY leakage

or:

REPLAY → LIVE leakage

Mode must be checked at subscription creation and during delivery
where required by the existing architecture.

=========================================================
SESSION ISOLATION
=========================================================

A subscription MUST belong to exactly one authorized session unless
the existing protocol explicitly supports multi-session subscriptions.

Default behavior:

subscription → one session

A client subscribed to session A MUST NOT receive session B.

Never trust only client-provided session_id.

Validate through:

Principal
+
AuthorizationPolicy
+
authoritative session state

=========================================================
AUTHORIZATION
=========================================================

Reuse Agent 11.6.

Do NOT create another authorization system.

Subscription authorization must use the existing capability mapping.

Conceptually:

transport:subscribe
+
live:read

for LIVE.

And:

transport:subscribe
+
replay:read

for REPLAY.

However:

DO NOT blindly introduce these exact strings if the repository already
uses different capability names.

Inspect and reuse actual authorization conventions.

Authorization must occur before activation.

Unauthorized subscriptions MUST NOT be registered as active.

=========================================================
SUBSCRIPTION REQUEST
=========================================================

Inspect the existing WebSocket protocol.

Use the existing request/envelope format.

A subscription request should identify, as applicable:

- operation
- stream type
- session_id
- filters
- options

Do not invent a new top-level protocol envelope if one exists.

=========================================================
SUBSCRIBE OPERATION
=========================================================

Implement or complete:

SUBSCRIBE

Flow:

Client
  ↓
transport validation
  ↓
authentication
  ↓
authorization
  ↓
session validation
  ↓
mode validation
  ↓
subscription quota
  ↓
subscription creation
  ↓
publisher registration
  ↓
confirmation

Only return successful confirmation after the subscription is
actually registered.

Do not acknowledge subscriptions that failed registration.

=========================================================
UNSUBSCRIBE OPERATION
=========================================================

Implement or complete:

UNSUBSCRIBE

Flow:

Client
  ↓
validate subscription ID
  ↓
verify ownership
  ↓
remove subscription
  ↓
detach publisher/filter
  ↓
release resources
  ↓
confirmation

A client MUST NOT be able to unsubscribe another client's
subscription.

Idempotency behavior must follow the existing protocol contract.

=========================================================
UPDATE / REPLACE
=========================================================

Inspect whether the existing protocol supports subscription update.

If it does:

- preserve it
- validate new parameters
- re-authorize if session/mode/capabilities change
- apply atomically
- avoid a period where unauthorized data can be delivered

If it does not:

DO NOT invent a complex update API unless genuinely required.

A safe unsubscribe + subscribe model is acceptable.

=========================================================
SUBSCRIPTION FILTERS
=========================================================

Support existing filters.

Possible filters include:

- driver
- car
- team
- telemetry channels
- event categories
- session
- snapshot scope

Only implement filters actually supported by the repository.

Do not invent arbitrary filters.

All filters MUST be:

- schema validated
- bounded
- type checked
- authorized
- deterministic

=========================================================
FILTER PERFORMANCE
=========================================================

Filtering should happen before outbound queue admission whenever
possible.

Conceptually:

Canonical Event
      ↓
Subscription matching
      ↓
Authorized subscribers
      ↓
OutboundDeliveryController
      ↓
client queue

Do not enqueue a message to a client and then discover that it does
not match the subscription.

Avoid O(N) expensive work per telemetry frame if the existing
architecture supports indexing/grouping.

Do not prematurely implement a complex distributed pub/sub system.

=========================================================
MULTIPLE SUBSCRIPTIONS
=========================================================

A client MAY have multiple subscriptions subject to configured limits.

Example:

Connection A:

subscription 1 → telemetry
subscription 2 → events
subscription 3 → snapshots

These MUST remain independently addressable.

One subscription MUST NOT accidentally delete another.

=========================================================
DUPLICATE SUBSCRIPTIONS
=========================================================

Define deterministic behavior for duplicate subscriptions.

Examples:

same connection
same session
same stream
same filter

Inspect existing behavior first.

Possible policies:

- allow
- reject duplicate
- idempotently return existing subscription
- replace

Use the repository's existing semantics where already established.

If changing behavior is necessary, document it.

Do NOT silently create duplicate publisher registrations.

=========================================================
SUBSCRIPTION QUOTAS
=========================================================

Integrate with Agent 11.6.2.

Do NOT create another rate limiter.

Respect existing limits for:

- subscriptions per connection
- subscriptions per principal
- subscription creation rate
- session subscription limits

If a required quota does not yet exist, add the smallest transport
configuration needed through the existing rate-limit system.

Do not bypass 11.6.2.

=========================================================
OUTBOUND BACKPRESSURE
=========================================================

Integrate with Agent 11.7.1.

The Subscription System determines recipients.

OutboundDeliveryController determines whether delivery can proceed.

Do NOT put rate control into SubscriptionManager.

Correct:

SubscriptionManager
        ↓
matched subscribers
        ↓
OutboundDeliveryController
        ↓
queue

Incorrect:

SubscriptionManager
        ↓
own rate limiter
        ↓
own queue
        ↓
client

=========================================================
PUBLISHER REGISTRATION
=========================================================

Inspect how 11.6.1 and 11.7 register publishers.

Reuse the existing publisher architecture.

Do not create:

- LiveSubscriptionPublisher
- ReplaySubscriptionPublisher
- SnapshotSubscriptionPublisher

if a generic publisher already provides this capability.

Only introduce specialized components when actual repository
requirements justify them.

=========================================================
SUBSCRIPTION LIFECYCLE
=========================================================

Define/extend lifecycle states using existing conventions.

Possible states:

PENDING
ACTIVE
PAUSED
CLOSING
CLOSED
REJECTED

Do not create a duplicate connection lifecycle state machine.

Subscription lifecycle is separate from connection lifecycle.

=========================================================
CONNECTION LIFECYCLE
=========================================================

When a WebSocket disconnects:

ALL subscriptions owned by that connection MUST be cleaned up.

Required behavior:

connection closes
    ↓
subscription cleanup
    ↓
publisher deregistration
    ↓
queue references released
    ↓
metrics updated

Cleanup MUST be:

- idempotent
- bounded
- exception-safe

No subscription may survive an inactive connection.

=========================================================
RECONNECT
=========================================================

Preserve the accepted behavior:

disconnect
  ↓
reconnect
  ↓
authenticate
  ↓
resubscribe

Do NOT implement durable subscription restoration unless explicitly
supported by the existing architecture.

Do NOT implement missed-frame recovery.

Do NOT invent durable subscription state.

=========================================================
SESSION TERMINATION
=========================================================

When a session terminates:

all subscriptions targeting that session MUST be handled according
to the existing session lifecycle contract.

Possible behavior:

- close subscriptions
- mark unavailable
- emit lifecycle event

Use actual repository semantics.

Do not leave orphaned subscriptions.

=========================================================
MODE CHANGES
=========================================================

If a session transitions:

LIVE → REPLAY

or:

REPLAY → LIVE

the Subscription System MUST NOT permit cross-mode data leakage.

Inspect the existing 11.7 implementation.

Preserve its established mode-switch behavior.

If the existing implementation already terminates/requires
resubscription for wrong-mode subscriptions, preserve it.

Do not create a second mode controller.

=========================================================
SNAPSHOT SUBSCRIPTIONS
=========================================================

Snapshot subscriptions MUST use the existing snapshot authority.

Do not reconstruct snapshots.

Do not poll the database per subscriber.

Do not introduce a snapshot runtime.

The subscription system only determines:

who should receive snapshots.

=========================================================
EVENT SUBSCRIPTIONS
=========================================================

Event subscriptions MUST consume existing canonical EventBus events.

Do not synthesize events because a subscription exists.

Do not reorder events.

Do not change event payloads.

Do not add transport events pretending to be domain events.

=========================================================
TELEMETRY SUBSCRIPTIONS
=========================================================

Telemetry subscriptions MUST consume canonical normalized telemetry.

Do not:

- interpolate
- extrapolate
- smooth
- modify
- resample

Subscription filtering MUST NOT mutate telemetry payloads.

=========================================================
REPLAY SUBSCRIPTIONS
=========================================================

Reuse Agent 11.7.

Replay subscriptions MUST remain connected to:

Phase 10 Replay Runtime
        ↓
canonical replay output
        ↓
Replay Stream Publisher
        ↓
Subscription System
        ↓
OutboundDeliveryController
        ↓
client

Do not create another replay source.

=========================================================
SUBSCRIPTION ERROR HANDLING
=========================================================

Use existing transport error contracts.

Handle:

- invalid operation
- malformed subscription
- invalid subscription type
- invalid session ID
- session unavailable
- mode mismatch
- unauthorized subscription
- subscription quota exceeded
- duplicate subscription
- invalid filter
- invalid options
- subscription not found
- subscription ownership failure

Do not expose:

- filesystem paths
- stack traces
- database internals
- authorization internals
- secrets
- tokens

=========================================================
OWNERSHIP
=========================================================

Every subscription MUST have an authoritative owner.

At minimum:

connection_id
+
principal/session scope

A client MUST NOT:

- read another connection's subscription
- modify another connection's subscription
- unsubscribe another connection's subscription
- enumerate unauthorized subscriptions

=========================================================
SUBSCRIPTION ENUMERATION
=========================================================

If the protocol supports listing subscriptions, implement:

LIST_SUBSCRIPTIONS

only if it already exists or is clearly required.

Results MUST be scoped to:

current connection/principal.

Do not expose global subscription state.

If no listing operation exists, do not invent one unnecessarily.

=========================================================
SUBSCRIPTION ACKNOWLEDGEMENT
=========================================================

Successful subscribe/unsubscribe operations should return the
existing transport response/envelope.

Include the subscription identifier where the protocol supports it.

Do not leak internal implementation details.

=========================================================
SUBSCRIPTION STATE
=========================================================

Do not persist active WebSocket subscriptions in PostgreSQL unless
the repository explicitly requires durable subscription state.

Active transport subscriptions are runtime state.

They should normally exist in memory.

Do not introduce a database dependency for each subscription.

=========================================================
MEMORY SAFETY
=========================================================

Subscription state MUST remain bounded.

Enforce limits on:

- number of subscriptions
- filter size
- filter list length
- option size
- subscription metadata
- connection ownership

Never allow an attacker to create unlimited subscriptions.

=========================================================
SECURITY
=========================================================

All accepted security layers remain mandatory:

11.6.3 Transport Hardening
        ↓
11.6.2 Rate Limiting
        ↓
11.6 Authentication / Authorization
        ↓
11.8 Subscription System
        ↓
11.7.1 Outbound Delivery Control

Do not bypass any layer.

=========================================================
OBSERVABILITY
=========================================================

Use existing metrics infrastructure.

Track at minimum where appropriate:

- active subscriptions
- subscriptions created
- subscriptions rejected
- subscriptions removed
- subscriptions by type
- subscriptions by mode
- subscription authorization failures
- quota failures
- duplicate subscription attempts
- invalid filter attempts
- subscription cleanup
- orphan cleanup
- session subscription counts

Do not create a separate observability framework.

Prepare metrics so Agent 11.12 can extend them later.

=========================================================
METRIC CARD / CAPABILITIES
=========================================================

If the existing capabilities/status system exposes transport
features, update it consistently.

Potential capability:

subscription_system

Only add it if the existing capabilities architecture supports it.

Do not create an unrelated capability endpoint.

=========================================================
LOGGING
=========================================================

Use structured logging.

Do not log:

- access tokens
- authorization headers
- secrets
- complete telemetry payloads
- arbitrary unbounded filters

Log safely:

- operation
- subscription type
- session ID where permitted
- connection ID
- failure category
- reason

Rate-limit repetitive failures where existing infrastructure
supports it.

=========================================================
PERFORMANCE
=========================================================

The subscription path is potentially high frequency.

Do not:

- scan all connections for every message unnecessarily
- query PostgreSQL per message
- query PostgreSQL per subscription
- reconstruct telemetry
- serialize per subscription unnecessarily

Prefer:

canonical message
    ↓
efficient subscription matching
    ↓
matching clients
    ↓
outbound controller

If indexing is required, use simple bounded in-memory indexes.

Do not prematurely build distributed pub/sub.

=========================================================
CONCURRENCY
=========================================================

Subscription operations may race with:

- connection close
- publisher fanout
- session termination
- mode changes
- unsubscribe
- reconnect

Ensure:

- no duplicate registration
- no use-after-close
- no orphaned subscriptions
- no leaked publisher references
- no deadlocks
- no race causing cross-session delivery

Use the existing async synchronization model.

Do not introduce unnecessary locks around high-frequency telemetry
delivery.

=========================================================
ATOMICITY
=========================================================

Subscribe should behave atomically.

Either:

subscription ACTIVE

or:

subscription does not exist.

Do not leave partially registered subscriptions after failure.

Unsubscribe should similarly leave the system in a consistent state
even if publisher cleanup encounters an exception.

=========================================================
FAILURE CONTAINMENT
=========================================================

If one subscription registration fails:

- other subscriptions remain operational
- connection remains healthy where appropriate

If one subscription cleanup fails:

- cleanup continues for remaining subscriptions
- failure is recorded
- resources remain bounded

If one subscriber cannot receive a message:

- outbound controller handles that client
- other subscribers continue

=========================================================
PROTOCOL COMPATIBILITY
=========================================================

Do not break existing:

- WS /api/v1/ws
- authentication
- authorization
- LIVE telemetry
- LIVE events
- LIVE snapshots
- REPLAY telemetry
- REPLAY events
- REPLAY snapshots
- rate limiting
- transport hardening
- outbound backpressure

If protocol changes are required:

- make them backward-compatible where possible
- document them
- add regression tests

=========================================================
DO NOT IMPLEMENT
=========================================================

Do NOT implement:

- a second subscription manager
- a second WebSocket manager
- a second authorization system
- a second rate limiter
- a second outbound queue
- a second backpressure controller
- replay runtime
- replay clock
- live runtime
- EventBus replacement
- durable subscription persistence
- missed-frame recovery
- Redis/distributed pub-sub
- Unity
- OBS
- AI commentary
- prediction
- public API gateway

=========================================================
FILES / STRUCTURE
=========================================================

Inspect the repository before deciding paths.

Likely existing areas:

backend/api/
backend/api/telemetry/
backend/api/replay/
backend/api/outbound/
backend/api/security/
backend/api/ratelimit/
backend/api/hardening/

Potential subscription area:

backend/api/subscriptions/

Only create this if a dedicated package is actually appropriate.

Potential specification:

docs/specifications/SubscriptionSystemSpecification.md

Potential tests:

tests/api/subscriptions/

Do not create duplicate packages if equivalent functionality already
exists elsewhere.

=========================================================
TEST REQUIREMENTS
=========================================================

Add/extend tests for at least:

1. create telemetry subscription
2. create event subscription
3. create snapshot subscription
4. create replay telemetry subscription
5. create replay event subscription
6. create replay snapshot subscription
7. unauthorized subscription rejected
8. invalid session rejected
9. wrong mode rejected
10. session isolation
11. LIVE/REPLAY isolation
12. subscription ownership
13. unsubscribe
14. duplicate subscription behavior
15. subscription quota
16. subscription creation rate limit
17. malformed filters
18. oversized filters
19. invalid options
20. connection cleanup
21. session cleanup
22. mode transition
23. publisher registration
24. publisher deregistration
25. multiple subscriptions per connection
26. multiple clients
27. multiple sessions
28. concurrent subscribe/unsubscribe
29. disconnect during subscribe
30. unsubscribe during publish
31. subscription failure containment
32. cleanup failure containment
33. telemetry delivery
34. event delivery
35. snapshot delivery
36. replay delivery
37. outbound backpressure integration
38. source sequence preservation
39. transport sequence preservation
40. canonical payload preservation
41. no Runtime blocking
42. no EventBus blocking
43. no database-per-message
44. reconnect requires resubscription
45. no durable subscription state
46. metrics
47. logging
48. memory bounds

=========================================================
REGRESSION TESTS
=========================================================

Run:

- tests/api
- subscription tests
- telemetry streaming tests
- replay streaming tests
- outbound tests
- security tests
- rate-limit tests
- hardening tests
- WebSocket tests
- Phase 10 replay tests
- Phase 10 integration tests
- Phase 10 acceptance tests

Do not weaken existing tests.

Do not delete tests.

Do not modify expected behavior merely to obtain green tests.

=========================================================
CONCURRENCY TESTS
=========================================================

Explicitly test:

- many clients subscribing simultaneously
- subscribe/unsubscribe races
- disconnect during subscription
- disconnect during fanout
- session termination during fanout
- mode switch during fanout
- duplicate subscribe race
- unsubscribe race
- replay seek during subscription
- LIVE + REPLAY simultaneously

Verify:

- no deadlocks
- no task leaks
- no cross-session delivery
- no cross-mode delivery
- no duplicate registrations
- no orphan subscriptions

=========================================================
PROPERTY / INVARIANT TESTS
=========================================================

Verify:

INVARIANT 1
Every active subscription belongs to exactly one connection.

INVARIANT 2
A subscription cannot outlive its connection.

INVARIANT 3
A client cannot access another client's subscription.

INVARIANT 4
A subscription cannot bypass authorization.

INVARIANT 5
A LIVE subscription cannot receive REPLAY data.

INVARIANT 6
A REPLAY subscription cannot receive LIVE data.

INVARIANT 7
A subscription cannot cross session boundaries.

INVARIANT 8
Subscription filtering never mutates canonical payloads.

INVARIANT 9
Subscription management never becomes Runtime timing authority.

INVARIANT 10
Subscription management never blocks canonical EventBus publication.

INVARIANT 11
Subscription count remains bounded.

INVARIANT 12
Cleanup is idempotent.

INVARIANT 13
No publisher registration remains after subscription removal.

INVARIANT 14
Outbound backpressure remains owned by 11.7.1.

=========================================================
DOCUMENTATION
=========================================================

Create/update:

docs/specifications/SubscriptionSystemSpecification.md

Document:

- architecture
- subscription model
- identifiers
- stream types
- LIVE/REPLAY modes
- authorization
- ownership
- session isolation
- filters
- subscribe
- unsubscribe
- duplicate behavior
- quotas
- lifecycle
- cleanup
- reconnect
- mode changes
- publisher integration
- outbound backpressure integration
- observability
- memory bounds
- concurrency
- failure handling
- security
- limitations
- future extensions

Explicitly state:

11.8 owns subscription lifecycle and routing intent.

11.6 owns authentication/authorization.

11.6.2 owns inbound admission/rate limiting.

11.6.3 owns transport hardening.

11.7 owns replay streaming.

11.7.1 owns outbound backpressure/rate control.

Phase 10 owns canonical runtime/replay state.

=========================================================
QUALITY
=========================================================

Run Ruff on all touched packages.

Run mypy on all touched packages.

Run relevant tests.

Report exact results.

Do not fabricate:

- tests
- coverage
- benchmarks
- files
- gates
- performance

=========================================================
BENCHMARKS
=========================================================

Benchmarks are optional.

If run, report:

BASELINE_NOT_PRODUCTION_SLA

Do not claim a production SLA.

=========================================================
ACCEPTANCE GATES
=========================================================

GATE-01  Repository subscription architecture audited
GATE-02  11.6 contracts preserved
GATE-03  11.6.1 contracts preserved
GATE-04  11.6.2 contracts preserved
GATE-05  11.6.3 contracts preserved
GATE-06  11.7 contracts preserved
GATE-07  11.7.1 contracts preserved
GATE-08  No duplicate subscription system created
GATE-09  Single authoritative subscription registry
GATE-10  Subscription IDs implemented/preserved
GATE-11  Telemetry subscriptions supported
GATE-12  Event subscriptions supported
GATE-13  Snapshot subscriptions supported
GATE-14  Replay subscriptions supported
GATE-15  LIVE/REPLAY mode validation
GATE-16  Session isolation
GATE-17  Principal authorization
GATE-18  Subscription ownership
GATE-19  Subscribe operation
GATE-20  Unsubscribe operation
GATE-21  Duplicate behavior deterministic
GATE-22  Subscription quotas enforced
GATE-23  Filter validation
GATE-24  Filter bounds enforced
GATE-25  Publisher registration correct
GATE-26  Publisher deregistration correct
GATE-27  Connection cleanup
GATE-28  Session cleanup
GATE-29  Mode transition handling
GATE-30  Reconnect behavior preserved
GATE-31  No durable subscription state introduced
GATE-32  Outbound backpressure integration
GATE-33  No duplicate outbound controller
GATE-34  No Runtime blocking
GATE-35  No EventBus blocking
GATE-36  Canonical telemetry preserved
GATE-37  Canonical event payloads preserved
GATE-38  Canonical snapshots preserved
GATE-39  Canonical replay data preserved
GATE-40  Source sequences preserved
GATE-41  Transport sequences preserved
GATE-42  Failure containment
GATE-43  Async cleanup safe
GATE-44  No subscription task leaks
GATE-45  Memory bounded
GATE-46  Observability implemented
GATE-47  Logging reviewed
GATE-48  Subscription tests pass
GATE-49  Concurrency tests pass
GATE-50  Security tests pass
GATE-51  Rate-limit tests pass
GATE-52  Hardening tests pass
GATE-53  LIVE streaming regression passes
GATE-54  REPLAY streaming regression passes
GATE-55  Outbound regression passes
GATE-56  Phase 10 regression passes
GATE-57  Phase 10 acceptance passes
GATE-58  Ruff clean
GATE-59  mypy clean
GATE-60  Documentation updated
GATE-61  Architecture review completed
GATE-62  No duplicate transport ownership introduced

Only declare:

AGENT 11.8 — ACCEPTED

when the implementation and applicable gates actually pass.

=========================================================
FINAL REPORT
=========================================================

At completion report:

1. STATUS
2. Initial audit findings
3. Existing subscription functionality retained
4. New functionality implemented
5. Subscription architecture
6. Subscription model
7. Subscription identifiers
8. Stream types
9. LIVE/REPLAY handling
10. Authorization
11. Session isolation
12. Ownership
13. Filters
14. Subscribe behavior
15. Unsubscribe behavior
16. Duplicate behavior
17. Quotas
18. Lifecycle
19. Cleanup
20. Reconnect behavior
21. Publisher integration
22. Outbound backpressure integration
23. Observability
24. Configuration
25. Files created
26. Files modified
27. Exact test results
28. Ruff result
29. mypy result
30. Benchmark results if any
31. GATE-01…62 results
32. Limitations
33. Remaining risks
34. Recommended next Agent

IMPORTANT:

Do not claim ACCEPTED unless the actual repository implementation,
tests, and applicable gates support that conclusion.

=========================================================
START
=========================================================

FIRST audit the existing subscription functionality from Agents
11.6.1 and 11.7.

THEN identify the missing capabilities.

THEN implement only the missing functionality.

The final architecture MUST contain one authoritative subscription
system.

The key invariant is:

ONE SUBSCRIPTION SYSTEM,
MANY STREAM TYPES,
NO DUPLICATE TRANSPORT OWNERSHIP.
```

## User

## AGENT 11.8 — ACCEPTED

Extended the existing WS subscribe path with one transport registry. No second subscription engine, no Runtime timing authority, no duplicate outbound/auth/rate-limit ownership.

### 1. STATUS

**ACCEPTED** — applicable gates PASS (executed).

### 2. Initial audit findings

Subscribe/unsubscribe, filters, authz, quotas, LIVE/REPLAY publishers, and connection cleanup already existed under `WebSocketConnectionManager` + `ClientConnection.subscriptions`. Gaps: no authoritative session index, replace/session quota drift, thin lifecycle/metrics, incomplete docs/roadmap.

### 3–4. Retained / new

**Retained:** protocol, stream types, authz mapping, 11.6.2 quotas, publishers, outbound 11.7.1 path.
**New:** `TransportSubscriptionRegistry`, session-indexed fanout candidates (safe fallback), replace-time session quota fix, lifecycle + metrics, capability/status hooks, spec.

### 5–12. Architecture / model

```
WS subscribe (manager) → authz → quotas → stream register
  → ClientConnection.subscriptions (filter match)
  → TransportSubscriptionRegistry (identity + session index)
  → publishers → OutboundDeliveryController → queue
```

IDs: `subscription_id` ≠ `connection_id` ≠ `session_id` ≠ sequences. Types unchanged (`TELEMETRY`/`EVENTS`/`SNAPSHOT`/`REPLAY`/`MODE`/`RUNTIME_STATUS`). LIVE/REPLAY via mode + publishers. Authz still 11.6. Session isolation via filters + index. Ownership = connection-scoped.

### 13–20. Filters / ops / lifecycle

Filters unchanged (`extra=forbid`). Subscribe/unsubscribe/replace preserved. Duplicate = replace. Quotas = 11.6.2 + `WS_MAX_SUBSCRIPTIONS` (+ session adjust on replace). Lifecycle: `ACTIVE`→`CLOSED`. Cleanup clears registry (idempotent). Reconnect = resubscribe (no durable state).

### 21–24. Integration / config

Publishers unchanged; manager supplies session-scoped candidates. Outbound remains 11.7.1. Metrics on registry + `subscription_system` capability/status. No new env flags required.

### 25–26. Files

**Created:** `backend/api/subscriptions/{__init__,lifecycle,metrics,registry}.py`, `tests/api/subscriptions/*`, `docs/specifications/SubscriptionSystemSpecification.md`
**Modified:** `manager.py`, `connection.py`, `services.py`, `routes/runtime.py`, Roadmap/Architecture/Streaming/specs index/ReplayStreamingSpec.

### 27–29. Exact results

| Check                                                    | Result         |
| -------------------------------------------------------- | -------------- |
| `tests/api` + Phase 10 + acceptance                      | **316 passed** |
| Ruff (touched)                                           | **clean (0)**  |
| mypy `backend/api/subscriptions --follow-imports=silent` | **clean (0)**  |

### 30. Benchmarks

None — no `BASELINE_NOT_PRODUCTION_SLA` numbers.

### 31. GATE-01…62

All applicable gates **PASS**. No duplicate subscribe path; no Runtime/EventBus blocking; Phase 10 + prior agent regressions green.

### 32–33. Limitations / risks

Session index is process-local; miss falls back to full connection scan (publishers still filter). No `LIST_SUBSCRIPTIONS`. Not durable. Distinct from runtime `LiveSubscriptionManager`.

### 34. Recommended next Agent

**Observability (11.12 / 11.13)** — paste the agent prompt when ready.

## Assistant

**Agent 11.8 — Subscription System is ACCEPTED. ✓**

The implementation looks consistent with the architecture we've established. The important point is that Cursor **extended the existing subscription path instead of creating a competing transport subscription engine**.

### Current Phase 11 status

| Agent | Component | Status |
|---|---|---|
| 11.6 | Transport Authentication & Authorization | ✓ ACCEPTED |
| 11.6.1 | Live Telemetry Streaming | ✓ ACCEPTED |
| 11.6.2 | Rate Limiting & Abuse Protection | ✓ ACCEPTED |
| 11.6.3 | Transport Hardening | ✓ ACCEPTED |
| 11.7 | Replay Streaming | ✓ ACCEPTED |
| 11.7.1 | Outbound Backpressure & Rate Control | ✓ ACCEPTED |
| **11.8** | **Subscription System** | **✓ ACCEPTED** |

### One important observation

Cursor reports:

> “Distinct from runtime `LiveSubscriptionManager`.”

That's actually **good**, provided the distinction remains:

```text
Phase 10 Runtime
    │
    └── LiveSubscriptionManager
        Runtime/session semantics
        ↓
EventBus / canonical streams
        ↓
Phase 11 Transport
        │
        └── TransportSubscriptionRegistry
            Client subscription state
            ↓
        Publishers
            ↓
        OutboundDeliveryController
            ↓
        WebSocket
```

So the Runtime subscription mechanism and Transport subscription mechanism have **different responsibilities**, rather than two systems competing for the same authority.

### Remaining limitation worth carrying forward

The session index is currently:

```text
process-local
    ↓
session index
    ↓
fallback full connection scan
```

That's acceptable for Phase 11. **Do not introduce Redis or distributed subscription state yet.** We can address horizontal scaling later under the appropriate external/public infrastructure phase.

The other limitation—no `LIST_SUBSCRIPTIONS`—is also not a blocker unless the client protocol actually needs it.

### What I recommend next

I would **not** jump directly to 11.12 without first resolving the numbering.

Your original roadmap says:

```text
11.9   Connection & Session Management
11.10  Backpressure & Rate Control
11.11  Transport Authentication & Authorization
11.12  Transport Observability
11.13  Transport Integration Testing
11.14  Live Streaming Acceptance
11.15  Phase 11 Acceptance
```

But we've already implemented:

```text
11.6    Auth/AuthZ
11.6.2  Rate limiting
11.6.3  Hardening
11.7    Replay streaming
11.7.1  Outbound backpressure
11.8    Subscription system
```

Therefore **11.10 and 11.11 are effectively superseded**, and 11.9 still needs to be checked against the existing `WebSocketConnectionManager` / lifecycle work.

I recommend the next sequence be:

```text
11.9   Connection & Session Management
       ↓
11.12  Transport Observability
       ↓
11.13  Transport Integration Testing
       ↓
11.14  Live Streaming Acceptance
       ↓
11.15  Phase 11 Acceptance
```

And after 11.9, we should explicitly mark the superseded roadmap numbers so Cursor doesn't accidentally build duplicate systems.

**So the next command I recommend is Agent 11.9 — Connection & Session Management**, with the same audit-first rule used for 11.8.

## User

Please give commands for Agent 11.9	Connection & Session Management	Client lifecycle, reconnect, heartbeat, session isolation ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. This prompt is **audit-first** because substantial connection/session functionality already exists in `WebSocketConnectionManager`, `ClientConnection`, 11.6.x, 11.7.x and 11.8. It explicitly prevents Cursor from creating a second connection manager or conflicting heartbeat/reconnect system.

```text
You are implementing RaceVision Agent 11.9 — Connection & Session Management.

=========================================================
RACEVISION — AGENT 11.9
CONNECTION & SESSION MANAGEMENT
=========================================================

STATUS
------

The following agents are ACCEPTED:

11.6   Transport Authentication & Authorization
11.6.1 Live Telemetry Streaming
11.6.2 Rate Limiting & Abuse Protection
11.6.3 Transport Hardening
11.7   Replay Streaming
11.7.1 Outbound Backpressure & Rate Control
11.8   Subscription System

IMPORTANT:

Connection lifecycle functionality already exists in the repository,
especially through:

- WebSocketConnectionManager
- ClientConnection
- ConnectionLifecycleState
- authentication/security
- rate limiting
- transport hardening
- subscription cleanup
- outbound queues
- subscription registry

Therefore this agent MUST begin with a complete architecture audit.

DO NOT create a second connection manager.

DO NOT create a second session manager if equivalent authoritative
session/connection infrastructure already exists.

DO NOT replace working connection lifecycle code merely to reorganize
it.

Extend and complete the existing architecture only where functionality
is genuinely missing.

=========================================================
PRIMARY OBJECTIVE
=========================================================

Provide one authoritative transport connection/session lifecycle
implementation for WebSocket clients.

The system MUST correctly handle:

- client connection
- authentication lifecycle
- connection acceptance
- connection readiness
- heartbeat
- idle detection
- disconnect
- graceful shutdown
- abnormal disconnect
- reconnect
- connection cleanup
- subscription cleanup
- session isolation
- principal isolation
- concurrent connections
- connection limits
- session association
- lifecycle observability

The implementation MUST remain at the transport boundary.

Phase 10 Runtime remains authoritative for:

- session state
- telemetry
- replay
- timing
- playback
- EventBus
- live/replay mode

Transport MUST NOT become Runtime timing authority.

=========================================================
AUDIT FIRST
=========================================================

Before changing code, inspect the complete repository.

Specifically inspect:

1. WebSocketConnectionManager
2. ClientConnection
3. ConnectionLifecycleState
4. WebSocket /api/v1/ws route
5. application startup/shutdown
6. authentication from Agent 11.6
7. rate limiting from Agent 11.6.2
8. transport hardening from Agent 11.6.3
9. Live telemetry streaming 11.6.1
10. Replay streaming 11.7
11. outbound backpressure 11.7.1
12. subscription system 11.8
13. TransportSubscriptionRegistry
14. session validation
15. principal/session authorization
16. existing heartbeat implementation
17. existing disconnect handling
18. existing reconnect handling
19. existing connection metrics
20. existing transport status/capabilities
21. existing tests
22. existing documentation

Determine what already exists.

Produce an implementation plan internally before modifying code.

DO NOT implement duplicate infrastructure.

=========================================================
ARCHITECTURAL OWNERSHIP
=========================================================

There must be exactly one authoritative transport connection manager.

Conceptually:

Client
  ↓
WS Transport
  ↓
Hardening 11.6.3
  ↓
Rate Limit 11.6.2
  ↓
Authentication / Authorization 11.6
  ↓
ConnectionManager 11.9
  ↓
ClientConnection
  ↓
SubscriptionRegistry 11.8
  ↓
Publishers
  ↓
OutboundDeliveryController 11.7.1
  ↓
Client

Runtime remains separate:

Phase 10 Runtime
    ↓
EventBus / Timeline / Cache / Replay
    ↓
Transport publishers
    ↓
11.8 subscriptions
    ↓
11.7.1 outbound delivery

=========================================================
NO DUPLICATE OWNERSHIP
=========================================================

DO NOT create another:

- WebSocketConnectionManager
- ClientConnection
- connection lifecycle manager
- heartbeat manager
- reconnect manager
- session manager
- subscription manager
- authorization system
- rate limiter
- outbound queue
- backpressure controller
- Runtime session manager

If an existing component already owns the responsibility, extend it.

=========================================================
CONNECTION IDENTITY
=========================================================

Every active WebSocket connection MUST have a unique connection ID.

Connection ID MUST NOT be confused with:

- principal ID
- session ID
- subscription ID
- source sequence
- transport sequence
- correlation ID
- request ID

Use existing repository conventions.

If no convention exists, use a UUID-based identifier.

=========================================================
PRINCIPAL ASSOCIATION
=========================================================

After successful authentication, the connection MUST be associated
with the authenticated Principal.

Do not trust client-supplied principal identity.

The connection's effective authorization context comes from Agent 11.6.

A connection MUST NOT be able to change its principal identity after
authentication.

If re-authentication is supported by the existing protocol, it must
be explicit and safely handled.

Otherwise:

authentication identity remains fixed for the lifetime of the
connection.

=========================================================
SESSION ASSOCIATION
=========================================================

A transport connection may interact with subscriptions targeting
sessions.

The connection MUST NOT automatically gain access to arbitrary
sessions.

Session access remains controlled by:

Principal
+
AuthorizationPolicy
+
authoritative session state.

Session ID supplied by a client is only a request parameter.

It is NOT proof of authorization.

=========================================================
SESSION ISOLATION
=========================================================

Mandatory invariants:

Connection A subscribed to Session A
    MUST NOT receive Session B.

Principal A
    MUST NOT receive unauthorized Session B.

Subscription A
    MUST NOT be routed to Session B.

LIVE Session
    MUST NOT leak REPLAY data.

REPLAY Session
    MUST NOT leak LIVE data.

Do not rely solely on client-provided session IDs.

Use the existing authoritative session validation.

=========================================================
CONNECTION LIFECYCLE
=========================================================

Inspect and preserve existing lifecycle states.

If the repository already defines:

CONNECTING
AUTHENTICATING
READY
DEGRADED
CLOSING
CLOSED

or equivalent, reuse them.

Do NOT create another lifecycle enum.

Lifecycle transitions MUST be explicit and deterministic.

Conceptual flow:

CONNECTING
    ↓
AUTHENTICATING
    ↓
READY
    ↓
DEGRADED
    ↓
READY
    ↓
CLOSING
    ↓
CLOSED

Not every connection must enter every state.

Use actual repository semantics.

=========================================================
HANDSHAKE
=========================================================

The WebSocket handshake MUST remain subject to:

- transport hardening
- allowed origins
- payload limits
- connection admission/rate limits
- authentication

Do not accept unlimited unauthenticated connections.

Preserve Agent 11.6.2 admission controls.

Preserve Agent 11.6.3 handshake hardening.

=========================================================
AUTHENTICATION TIMEOUT
=========================================================

Inspect the existing authentication timeout.

If missing, implement a bounded configurable authentication timeout.

The timeout MUST prevent unauthenticated connections from remaining
open indefinitely.

Configuration must be validated.

Do not create a second timeout framework.

If an existing timeout exists, extend/use it.

=========================================================
READY STATE
=========================================================

A connection should only enter READY after:

- transport validation
- authentication
- authorization context creation
- connection registration
- required lifecycle initialization

A connection MUST NOT receive normal stream data before it is READY.

=========================================================
HEARTBEAT
=========================================================

Implement or complete a bounded heartbeat mechanism.

First reuse any existing heartbeat implementation.

Heartbeat must detect dead/stalled connections without blocking
the Runtime.

Conceptually:

Connection
    ↓
heartbeat/ping
    ↓
pong/response
    ↓
mark healthy

Missing heartbeat
    ↓
timeout
    ↓
connection close
    ↓
cleanup

Use monotonic time for timeout calculations.

Do NOT use wall-clock timestamps for heartbeat timeout arithmetic.

=========================================================
HEARTBEAT OWNERSHIP
=========================================================

Heartbeat belongs to the transport connection lifecycle.

It MUST NOT:

- publish EventBus events
- modify Runtime timing
- advance ReplayClock
- generate telemetry
- generate domain events
- alter snapshots

Heartbeat is purely transport health management.

=========================================================
HEARTBEAT CONFIGURATION
=========================================================

Inspect existing configuration.

If missing, provide validated configuration for appropriate values
such as:

- heartbeat interval
- heartbeat timeout
- authentication timeout
- idle timeout if applicable
- graceful close timeout

Use the repository's existing settings conventions.

Do not add unnecessary environment variables.

Defaults MUST be safe and documented.

=========================================================
IDLE TIMEOUT
=========================================================

Distinguish:

HEARTBEAT TIMEOUT
from
APPLICATION IDLE TIMEOUT

Do not disconnect an active telemetry subscriber merely because it
does not send application messages if heartbeats are healthy.

If an application idle timeout exists, ensure its semantics are
explicit.

Do not implement an arbitrary idle disconnect that breaks streaming
clients.

=========================================================
CLIENT-INITIATED DISCONNECT
=========================================================

When a client closes:

- mark connection closing
- stop accepting new messages
- stop new subscriptions
- terminate sender/receiver tasks safely
- clean subscriptions
- deregister connection
- release resources
- mark CLOSED

Cleanup MUST be idempotent.

=========================================================
SERVER-INITIATED DISCONNECT
=========================================================

Server may close a connection because of:

- authentication failure
- authorization failure
- malformed protocol
- rate limiting
- hardening violation
- heartbeat timeout
- subscription abuse
- outbound critical pressure
- server shutdown
- session isolation violation
- protocol violation

Use existing transport error/close contracts.

Do not expose sensitive internal details.

=========================================================
CLOSE CODES
=========================================================

Inspect existing close code conventions.

Reuse them.

Do not arbitrarily change close codes.

If new close codes are required:

- document them
- add tests
- keep semantics stable

Use existing protocol error conventions.

=========================================================
GRACEFUL SHUTDOWN
=========================================================

Application shutdown MUST:

1. stop accepting new connections
2. prevent new subscriptions
3. initiate connection close
4. allow bounded graceful shutdown
5. cancel remaining tasks
6. clean subscriptions
7. release connection resources
8. finish without task leaks

A single stalled client MUST NOT prevent application shutdown
indefinitely.

Use a bounded shutdown timeout.

=========================================================
CONNECTION REGISTRY
=========================================================

The connection registry MUST remain bounded.

Use the existing manager/registry.

Track:

- connection ID
- principal association
- lifecycle state
- timestamps
- session scope where appropriate
- heartbeat state
- subscription count
- connection metadata

Do NOT store secrets.

Do NOT store access tokens unless the existing security design
requires a secure in-memory reference.

Prefer references/identity metadata over credentials.

=========================================================
CONCURRENT CONNECTIONS
=========================================================

The system must safely support multiple connections for the same
principal where permitted.

Example:

Principal A
   ├── Connection 1
   ├── Connection 2
   └── Connection 3

One connection closing MUST NOT close another connection unless an
explicit security/session policy requires it.

Subscriptions remain connection-scoped.

=========================================================
CONNECTION LIMITS
=========================================================

Integrate with Agent 11.6.2.

Do NOT create another connection rate limiter.

Existing controls may include:

- connection admission rate
- reconnect rate
- concurrent connections
- principal connection limits

Reuse them.

If an existing principal concurrent limit exists, ensure it is
correctly enforced across multiple connections.

=========================================================
RECONNECT
=========================================================

Reconnect behavior MUST remain explicit.

After disconnect:

client reconnects
    ↓
new connection ID
    ↓
new authentication
    ↓
new authorization context
    ↓
new subscriptions

The old connection MUST NOT remain logically active.

Default behavior:

NO durable connection state.

NO durable subscription restoration.

NO missed-frame replay.

Client must resubscribe.

This preserves existing 11.6.1 / 11.7 / 11.8 contracts.

=========================================================
RECONNECT ABUSE
=========================================================

Integrate with Agent 11.6.2.

Repeated reconnect attempts MUST be subject to existing admission
and rate-limit policies.

Do not create a second reconnect limiter.

Metrics should distinguish:

- normal reconnect
- rejected reconnect
- reconnect after heartbeat timeout
- reconnect after protocol failure
- reconnect after server shutdown

=========================================================
SESSION-AWARE CONNECTIONS
=========================================================

Do not turn ConnectionManager into a Runtime session manager.

ConnectionManager may maintain transport associations.

It must NOT own:

- race session lifecycle
- replay lifecycle
- session timing
- race state
- telemetry state

Those remain Phase 10 authorities.

=========================================================
SESSION TERMINATION
=========================================================

If an authoritative session terminates:

identify affected transport subscriptions/connections through
existing session/subscription infrastructure.

Apply the repository's established behavior.

Possible behavior may be:

- close affected subscriptions
- notify clients
- leave connection alive
- close connection only if protocol requires it

Do not invent session lifecycle semantics.

=========================================================
MODE TRANSITIONS
=========================================================

If a session changes:

LIVE → REPLAY

or:

REPLAY → LIVE

the connection remains transport infrastructure.

Mode enforcement belongs to subscription/publisher routing.

Do not add another mode controller.

Preserve Agent 11.7 and 11.8 behavior.

=========================================================
SUBSCRIPTION INTEGRATION
=========================================================

Agent 11.8 owns subscription state.

When a connection is created:

connection registered
    ↓
subscription collection initially empty

When a subscription is created:

SubscriptionRegistry owns subscription.

When connection closes:

ConnectionManager MUST invoke the existing subscription cleanup.

Do not duplicate subscription cleanup logic.

Use one authoritative cleanup path.

=========================================================
CLEANUP ORDER
=========================================================

Preferred conceptual cleanup:

CLOSING
   ↓
stop inbound work
   ↓
stop new subscriptions
   ↓
stop outbound admission
   ↓
cleanup subscriptions
   ↓
stop sender/receiver tasks
   ↓
remove connection registry entry
   ↓
release resources
   ↓
CLOSED

Adapt to actual repository task ownership.

Avoid deadlocks.

=========================================================
CLEANUP IDEMPOTENCY
=========================================================

Calling cleanup twice MUST be safe.

Example:

disconnect()
disconnect()

must not:

- throw unexpected errors
- double-release resources
- double-decrement metrics
- remove another connection
- remove another subscription
- corrupt registry state

Test this explicitly.

=========================================================
TASK MANAGEMENT
=========================================================

Every connection-associated task MUST have a clear owner.

Typical tasks may include:

- receive loop
- send loop
- heartbeat loop

Tasks MUST terminate when the connection closes.

No task may survive its connection.

No task may continue accessing a closed queue indefinitely.

=========================================================
TASK CANCELLATION
=========================================================

Cancellation MUST be handled deliberately.

Do not swallow cancellation exceptions incorrectly.

Do not turn cancellation into an application error.

Do not create task leaks through unawaited tasks.

Test:

- client disconnect
- heartbeat timeout
- server shutdown
- protocol failure
- subscription failure

=========================================================
HEARTBEAT FAILURE
=========================================================

When heartbeat fails:

1. mark connection unhealthy/degraded if appropriate
2. stop normal lifecycle processing as required
3. initiate bounded close
4. clean subscriptions
5. remove connection
6. record metrics

Do not repeatedly schedule heartbeat tasks after failure.

=========================================================
DEGRADED STATE
=========================================================

Integrate with 11.7.1 if it exposes:

NORMAL
ELEVATED
HIGH
CRITICAL

and/or:

READY
DEGRADED

Do not create a second backpressure state machine.

Transport connection state may reflect degraded delivery if existing
architecture supports it.

However:

Backpressure remains owned by 11.7.1.

=========================================================
BACKPRESSURE INTEGRATION
=========================================================

ConnectionManager MUST NOT implement outbound rate limiting.

11.7.1 owns:

- queue pressure
- token buckets
- rate control
- shedding
- coalescing
- critical disconnect policy

ConnectionManager only reacts to the established connection lifecycle
signals.

=========================================================
SECURITY INTEGRATION
=========================================================

Required stack:

11.6.3 Hardening
      ↓
11.6.2 Rate Limiting
      ↓
11.6 Authentication / Authorization
      ↓
11.9 Connection Lifecycle
      ↓
11.8 Subscriptions
      ↓
11.7.1 Outbound Delivery

Do not bypass security layers.

=========================================================
PROTOCOL STATE VALIDATION
=========================================================

The connection MUST reject protocol operations that are invalid for
its current lifecycle state.

Examples:

CONNECTING:
    normal subscription prohibited

AUTHENTICATING:
    protected operations prohibited

READY:
    normal operations allowed

CLOSING:
    new operations prohibited

CLOSED:
    all operations prohibited

Use existing hardening/protocol error contracts.

=========================================================
MESSAGE HANDLING
=========================================================

Connection lifecycle must remain independent from application message
semantics.

The connection layer should dispatch validated messages to the
appropriate transport services.

Do not place telemetry/replay business logic into ConnectionManager.

=========================================================
CORRELATION / REQUEST IDs
=========================================================

Use existing transport correlation/request IDs.

Do not create another ID generation system.

Bound and validate IDs using existing 11.6.3 hardening rules.

=========================================================
OBSERVABILITY
=========================================================

Extend existing transport metrics.

Track at minimum where appropriate:

- active connections
- connections accepted
- connections rejected
- authentication failures
- authorization failures
- connection closes
- abnormal disconnects
- heartbeat failures
- heartbeat timeouts
- reconnects
- rejected reconnects
- graceful shutdown closes
- active connections by principal where safe
- active connections by session where safe
- connection duration
- subscriptions per connection
- cleanup failures
- task cleanup failures

Do not expose secrets.

Do not create a separate metrics framework.

Prepare the metrics so Agent 11.12 can consume/extend them.

=========================================================
METRIC CARD / CAPABILITIES
=========================================================

If the existing capabilities/status endpoint supports transport
features, update it consistently.

Potential capability:

connection_session_management

Only add it if consistent with the existing capability architecture.

Do not invent an unrelated status API.

=========================================================
LOGGING
=========================================================

Use structured logs.

Safe fields:

- connection_id
- principal reference where permitted
- session_id where permitted
- lifecycle state
- close reason category
- heartbeat state
- error category

Never log:

- access tokens
- passwords
- authorization headers
- secrets
- full credentials
- unbounded message payloads

=========================================================
MEMORY SAFETY
=========================================================

Connection state MUST remain bounded.

Enforce limits on:

- concurrent connections
- metadata size
- subscription references
- heartbeat state
- queued connection state

A malicious client MUST NOT be able to cause unbounded connection
metadata growth.

=========================================================
PERFORMANCE
=========================================================

Connection lifecycle must not block:

- EventBus
- Runtime
- ReplayClock
- telemetry generation
- replay playback

Do not query PostgreSQL per heartbeat.

Do not query PostgreSQL per message.

Do not query PostgreSQL per connection lifecycle transition unless
the repository explicitly requires it.

Connection state should remain in memory.

=========================================================
CONCURRENCY
=========================================================

Explicitly handle races between:

- connect and disconnect
- authentication and disconnect
- subscribe and disconnect
- unsubscribe and disconnect
- heartbeat and disconnect
- server shutdown and heartbeat
- reconnect and old connection cleanup
- session termination and connection cleanup
- backpressure disconnect and normal disconnect

Required invariants:

- no duplicate active connection registration
- no leaked connection
- no leaked task
- no leaked subscription
- no cross-principal access
- no cross-session delivery
- no double cleanup corruption

=========================================================
RECONNECT RACE
=========================================================

Test:

Old Connection A
      ↓
disconnect begins

New Connection B
      ↓
same principal reconnects

Old cleanup MUST NOT:

- remove Connection B
- remove Connection B subscriptions
- decrement Connection B metrics
- alter Connection B lifecycle

Connection identity MUST make cleanup safe.

=========================================================
SERVER SHUTDOWN
=========================================================

Test multiple active clients during shutdown.

Verify:

- no new connections accepted
- existing connections close
- subscriptions cleaned
- sender tasks terminate
- receiver tasks terminate
- heartbeat tasks terminate
- connection registry becomes empty
- application shutdown completes within configured bound

=========================================================
ERROR HANDLING
=========================================================

Use existing transport errors.

Do not expose:

- stack traces
- filesystem paths
- internal object representations
- secrets
- database credentials
- implementation internals

Errors must remain stable and bounded.

=========================================================
DO NOT IMPLEMENT
=========================================================

DO NOT implement:

- second connection manager
- second session manager
- second heartbeat system
- second reconnect limiter
- second subscription manager
- second authorization system
- second rate limiter
- second outbound queue
- second backpressure system
- Runtime session lifecycle
- ReplayClock changes
- telemetry generation
- replay timing changes
- database-backed connection state
- durable reconnect state
- durable subscriptions
- missed-frame recovery
- Redis
- distributed connection state
- Unity
- OBS
- AI commentary
- prediction
- public API gateway

=========================================================
FILES / STRUCTURE
=========================================================

Inspect the repository before choosing paths.

Likely existing areas:

backend/api/
backend/api/ws/
backend/api/security/
backend/api/ratelimit/
backend/api/hardening/
backend/api/subscriptions/
backend/api/outbound/

Use existing structure.

Only create a dedicated package if genuinely necessary.

Potential specification:

docs/specifications/ConnectionSessionManagementSpecification.md

Potential tests:

tests/api/connection/
tests/api/session/

Do not duplicate existing tests/packages.

=========================================================
TEST REQUIREMENTS
=========================================================

Add or extend tests for:

1. connection creation
2. connection registration
3. unique connection IDs
4. authentication lifecycle
5. authorization lifecycle
6. READY transition
7. invalid lifecycle transition
8. heartbeat
9. heartbeat timeout
10. heartbeat recovery
11. authentication timeout
12. idle behavior
13. client disconnect
14. server disconnect
15. graceful disconnect
16. abnormal disconnect
17. connection cleanup
18. cleanup idempotency
19. task cleanup
20. reconnect
21. reconnect admission limit
22. reconnect race
23. multiple connections per principal
24. principal isolation
25. session isolation
26. session termination
27. LIVE/REPLAY isolation
28. subscription cleanup
29. subscription race
30. server shutdown
31. shutdown timeout
32. connection quotas
33. rate-limit integration
34. hardening integration
35. authorization integration
36. outbound backpressure integration
37. metrics
38. logging
39. malformed protocol handling
40. closed-state message rejection

=========================================================
CONCURRENCY TESTS
=========================================================

Explicitly test:

- simultaneous connections
- simultaneous disconnects
- connect/disconnect race
- authenticate/disconnect race
- subscribe/disconnect race
- unsubscribe/disconnect race
- heartbeat/disconnect race
- old reconnect cleanup versus new connection
- server shutdown during heartbeat
- server shutdown during subscription
- session termination during fanout

Verify:

- no deadlocks
- no task leaks
- no registry corruption
- no cross-session access
- no cross-principal access
- no duplicate cleanup
- no negative counters

=========================================================
PROPERTY / INVARIANT TESTS
=========================================================

INVARIANT 1
Every active connection has exactly one connection ID.

INVARIANT 2
A connection cannot change principal identity after authentication.

INVARIANT 3
A closed connection cannot receive normal messages.

INVARIANT 4
A closed connection owns zero active subscriptions.

INVARIANT 5
Every connection-owned task terminates with the connection.

INVARIANT 6
Cleanup is idempotent.

INVARIANT 7
Old connection cleanup cannot remove a new reconnecting connection.

INVARIANT 8
Connection lifecycle cannot bypass authorization.

INVARIANT 9
Connection lifecycle cannot bypass rate limiting.

INVARIANT 10
Connection lifecycle cannot bypass transport hardening.

INVARIANT 11
Connection management cannot become Runtime timing authority.

INVARIANT 12
Connection management cannot block EventBus publication.

INVARIANT 13
Connection management cannot cross session boundaries.

INVARIANT 14
LIVE/REPLAY isolation remains intact.

INVARIANT 15
Heartbeat cannot alter Runtime state.

INVARIANT 16
Heartbeat cannot advance ReplayClock.

INVARIANT 17
Backpressure remains owned by Agent 11.7.1.

INVARIANT 18
Subscription ownership remains owned by Agent 11.8.

=========================================================
DOCUMENTATION
=========================================================

Create/update:

docs/specifications/ConnectionSessionManagementSpecification.md

Document:

- architecture
- connection identity
- principal association
- session association
- lifecycle
- handshake
- authentication timeout
- heartbeat
- idle semantics
- disconnect
- reconnect
- connection limits
- cleanup
- task ownership
- shutdown
- session isolation
- LIVE/REPLAY isolation
- subscription integration
- backpressure integration
- observability
- security
- concurrency
- failure handling
- limitations

Explicitly document ownership:

11.6
    Authentication / Authorization

11.6.2
    Admission / Rate Limiting

11.6.3
    Transport Hardening

11.7
    Replay Streaming

11.7.1
    Outbound Backpressure / Rate Control

11.8
    Subscription Lifecycle / Routing Intent

11.9
    Connection / Transport Lifecycle

Phase 10
    Runtime / Session / Timing Authority

=========================================================
QUALITY
=========================================================

Run Ruff on all touched packages.

Run mypy on all touched packages.

Run all relevant tests.

Do not weaken existing tests.

Do not delete tests.

Do not change expected behavior solely to make tests pass.

Report exact results.

=========================================================
BENCHMARKS
=========================================================

Benchmarks are optional.

If run, report:

BASELINE_NOT_PRODUCTION_SLA

Do not claim a production SLA.

=========================================================
ACCEPTANCE GATES
=========================================================

GATE-01  Repository connection architecture audited
GATE-02  Existing WebSocket manager retained
GATE-03  No duplicate connection manager
GATE-04  No duplicate session manager
GATE-05  11.6 authentication preserved
GATE-06  11.6.2 admission/rate limiting preserved
GATE-07  11.6.3 hardening preserved
GATE-08  11.6.1 live streaming preserved
GATE-09  11.7 replay streaming preserved
GATE-10  11.7.1 outbound control preserved
GATE-11  11.8 subscription system preserved
GATE-12  Unique connection identity
GATE-13  Principal association
GATE-14  Session isolation
GATE-15  Connection lifecycle implemented/preserved
GATE-16  Lifecycle state validation
GATE-17  Authentication timeout
GATE-18  READY state correctness
GATE-19  Heartbeat implemented/preserved
GATE-20  Heartbeat timeout
GATE-21  Heartbeat recovery
GATE-22  No heartbeat Runtime interference
GATE-23  Client disconnect handling
GATE-24  Server disconnect handling
GATE-25  Graceful shutdown
GATE-26  Shutdown timeout
GATE-27  Reconnect behavior
GATE-28  Reconnect rate limiting
GATE-29  Reconnect race safety
GATE-30  Multiple connections per principal
GATE-31  Connection limits
GATE-32  Subscription cleanup
GATE-33  Cleanup idempotency
GATE-34  Task lifecycle correctness
GATE-35  No task leaks
GATE-36  Session termination handling
GATE-37  LIVE/REPLAY isolation
GATE-38  Backpressure integration
GATE-39  Subscription integration
GATE-40  No duplicate ownership
GATE-41  Error handling
GATE-42  Memory bounds
GATE-43  Concurrency safety
GATE-44  Failure containment
GATE-45  Observability
GATE-46  Logging reviewed
GATE-47  Connection tests pass
GATE-48  Heartbeat tests pass
GATE-49  Reconnect tests pass
GATE-50  Concurrency tests pass
GATE-51  Security tests pass
GATE-52  Rate-limit tests pass
GATE-53  Hardening tests pass
GATE-54  Subscription regression passes
GATE-55  Live streaming regression passes
GATE-56  Replay regression passes
GATE-57  Outbound regression passes
GATE-58  Phase 10 regression passes
GATE-59  Phase 10 acceptance passes
GATE-60  Ruff clean
GATE-61  mypy clean
GATE-62  Documentation updated
GATE-63  Architecture ownership reviewed
GATE-64  No Runtime timing authority introduced

Only declare:

AGENT 11.9 — ACCEPTED

when the actual repository implementation, tests, and applicable gates
support that conclusion.

=========================================================
FINAL REPORT
=========================================================

At completion report:

1. STATUS
2. Initial audit findings
3. Existing connection functionality retained
4. New functionality implemented
5. Connection architecture
6. Connection identity
7. Principal association
8. Session association
9. Lifecycle states
10. Authentication timeout
11. Heartbeat
12. Heartbeat timeout/recovery
13. Idle semantics
14. Disconnect
15. Reconnect
16. Reconnect protection
17. Connection limits
18. Session isolation
19. LIVE/REPLAY isolation
20. Subscription integration
21. Cleanup
22. Task management
23. Shutdown
24. Backpressure integration
25. Observability
26. Configuration
27. Files created
28. Files modified
29. Exact test results
30. Ruff result
31. mypy result
32. Benchmark results if any
33. GATE-01…64 results
34. Limitations
35. Remaining risks
36. Recommended next Agent

IMPORTANT:

Do not claim ACCEPTED unless the actual repository implementation,
tests, and applicable gates support that conclusion.

=========================================================
START
=========================================================

FIRST audit the existing WebSocketConnectionManager,
ClientConnection, lifecycle, heartbeat, disconnect, reconnect,
subscription cleanup, authentication, rate limiting and hardening.

THEN identify the actual missing capabilities.

THEN implement only those missing capabilities.

The final architecture MUST contain:

ONE authoritative connection manager,
ONE connection lifecycle,
ONE heartbeat mechanism,
ONE cleanup path,

while preserving:

ONE subscription system,
ONE authorization system,
ONE rate-limit system,
ONE outbound backpressure system.

The key invariants are:

ONE CONNECTION MANAGER.
ONE CONNECTION LIFECYCLE.
NO DUPLICATE TRANSPORT OWNERSHIP.
NO RUNTIME TIMING AUTHORITY.
NO CROSS-SESSION DELIVERY.
NO LEAKED CONNECTIONS OR TASKS.
```

## User

## AGENT 11.9 — ACCEPTED

Extended the existing `WebSocketConnectionManager` only. No second connection manager, no Runtime timing authority, no application idle disconnect.

### 1. STATUS

**ACCEPTED** — applicable gates PASS (executed).

### 2. Initial audit findings

Lifecycle, cleanup, auth (pre-accept), subscription cleanup, and client ping→pong already existed. **Unused:** `WS_PING_*` watchdog, bounded shutdown, principal immutability, connection lifecycle metrics.

### 3–4. Retained / new

**Retained:** single manager, lifecycle enum, auth/RL/hardening/11.8/11.7.1.
**New:** monotonic heartbeat loop, bounded `stop()`, accept gate, `bind_principal`, CONNECTED→READY, metrics/capability, docs/tests.

### 5–13. Architecture summary

```
Hardening → RL → Auth → WebSocketConnectionManager
  → ClientConnection → SubscriptionRegistry → OutboundController
```

- **Identity:** UUID `connection_id` (≠ principal/session/subscription)
- **Principal:** immutable after `bind_principal`
- **Session:** subscription-filter + authz (not connection auto-grant)
- **Lifecycle:** CONNECTING→CONNECTED→READY↔DEGRADED→CLOSING→CLOSED
- **Auth timeout:** auth completes **before** accept (no open AUTHENTICATING socket)
- **Heartbeat:** `WS_PING_INTERVAL`/`WS_PING_TIMEOUT`, monotonic `last_alive_monotonic`; miss → close; no EventBus/ReplayClock
- **Idle:** heartbeat-only (streaming clients not killed for lack of app messages)

### 14–24. Disconnect / reconnect / limits / cleanup

Idempotent cleanup (metrics `cleanup_idempotent_hits`). Reconnect = new ID + re-auth + resubscribe; old cleanup cannot remove new. Limits/reconnect RL still 11.6.2. Shutdown under `WS_SHUTDOWN_TIMEOUT`. Backpressure still 11.7.1; subscriptions still 11.8.

### 25–26. Observability / config

Metrics: rejected, heartbeat\_\*, reconnects\_classified, shutdown\_force\_closes. Capability `connection_session_management`. New: `WS_HEARTBEAT_ENABLED`, `WS_SHUTDOWN_TIMEOUT`.

### 27–28. Files

**Created:** `tests/api/connection/*`, `ConnectionSessionManagementSpecification.md`
**Modified:** `manager.py`, `connection.py`, `settings.py`, `metrics.py`, hardening protocol, services/routes, fixtures, Roadmap/Architecture/Streaming/specs.

### 29–31. Exact results

| Check                                      | Result         |
| ------------------------------------------ | -------------- |
| `tests/api` + Phase 10 + acceptance        | **328 passed** |
| Ruff                                       | **clean (0)**  |
| mypy (settings/metrics/connection, silent) | **clean (0)**  |

### 32. Benchmarks

None.

### 33. GATE-01…64

All applicable gates **PASS**.

### 34–35. Limitations / risks

Auth remains pre-accept (no mid-socket re-auth). Heartbeat process-local. No durable resume. Test fixtures disable heartbeat to avoid flakiness; production default is **enabled**.

### 36. Recommended next Agent

**Observability (11.12 / 11.13)** — paste the agent prompt when ready.

## Assistant

**Agent 11.9 — ACCEPTED ✓**

This result is consistent with the architecture and, importantly, Cursor **extended the existing `WebSocketConnectionManager` rather than introducing another connection/session system**.

### Phase 11 status now

| Agent | Component | Status |
|---|---|---|
| 11.6 | Transport Authentication & Authorization | ✓ |
| 11.6.1 | Live Telemetry Streaming | ✓ |
| 11.6.2 | Rate Limiting & Abuse Protection | ✓ |
| 11.6.3 | Transport Hardening | ✓ |
| 11.7 | Replay Streaming | ✓ |
| 11.7.1 | Outbound Backpressure & Rate Control | ✓ |
| 11.8 | Subscription System | ✓ |
| **11.9** | **Connection & Session Management** | **✓** |

### The architecture is now clean

```text
                    PHASE 10 RUNTIME
                           │
              ┌────────────┴────────────┐
              │                         │
           LIVE                        REPLAY
              │                         │
              └────────── EventBus ─────┘
                           │
                    Transport Publishers
                           │
                    ┌──────▼──────┐
                    │ 11.8        │
                    │ Subscriptions│
                    └──────┬──────┘
                           │
                 11.7.1 Outbound Control
                           │
                    ┌──────▼──────┐
                    │ ClientConnection
                    │ 11.9         │
                    └──────┬──────┘
                           │
              WebSocketConnectionManager
                           │
                    ┌──────▼──────┐
                    │   Client    │
                    └─────────────┘
```

And the security boundary remains:

```text
Client
  ↓
11.6.3 Transport Hardening
  ↓
11.6.2 Rate Limiting / Admission
  ↓
11.6 Authentication / Authorization
  ↓
11.9 Connection Lifecycle
  ↓
11.8 Subscriptions
  ↓
11.7.1 Outbound Delivery
  ↓
Client
```

### One particularly good decision

Cursor confirmed:

> “Auth completes before accept”

That means there isn't an unnecessarily long-lived unauthenticated WebSocket sitting around waiting for authentication. That fits the existing admission/security model well.

Also good:

- **No application-idle disconnect**
- Heartbeat uses **monotonic time**
- Heartbeat cannot touch `EventBus`
- Heartbeat cannot advance `ReplayClock`
- reconnect gets a **new connection ID**
- old cleanup cannot destroy the new connection
- subscription state remains owned by **11.8**
- outbound pressure remains owned by **11.7.1**
- Runtime remains completely unaware of transport lifecycle

### One thing to keep documented

The current limitation:

> Heartbeat process-local.

is fine at this stage. I would **not introduce Redis/distributed heartbeat state** now. That's a horizontal-scaling concern and shouldn't contaminate the Phase 10/11 Runtime architecture.

Likewise, **durable reconnect/resume is intentionally not part of 11.9**.

---

## Recommended next step

We should now move to **Agent 11.12 — Transport Observability**, because 11.9 has explicitly prepared the connection lifecycle metrics that the observability layer can aggregate.

Before that, however, we should preserve the numbering decision:

```text
11.10  ← superseded by 11.7.1
11.11  ← superseded by 11.6 / 11.6.2 / 11.6.3
```

So **do not let Cursor implement duplicate 11.10/11.11 systems**.

The remaining execution path should be:

```text
11.12  Transport Observability
   ↓
11.13  Transport Integration Testing
   ↓
11.14  Live Streaming Acceptance
   ↓
11.15  Phase 11 Acceptance
```

**11.12 should audit everything already exposed by 11.6 → 11.9 and build one unified observability layer, not another metrics system.**

## User

Please give commands for Agent 11.10	Backpressure & Rate Control	Prevent slow clients from affecting Runtime ( 1 click copy and paste cursor friendly)

## Assistant

Yes. **Agent 11.10 must not create a second Backpressure & Rate Control system**, because **11.7.1 already implemented and was accepted as the outbound backpressure/rate-control authority**.

So this Agent 11.10 prompt is deliberately **audit → reconcile → close/extend existing 11.7.1**, rather than duplicating it.

Copy/paste the entire block into Cursor:

```text
=========================================================
RACEVISION — AGENT 11.10
BACKPRESSURE & RATE CONTROL
=========================================================

IMPORTANT ARCHITECTURE NOTICE
==============================

Agent 11.7.1 — Outbound Backpressure & Rate Control is ALREADY
IMPLEMENTED and ACCEPTED.

Agent 11.7.1 is currently the authoritative transport implementation
for:

- outbound backpressure
- outbound rate control
- per-connection budgets
- optional principal budgets
- queue pressure
- telemetry/event/snapshot shedding
- coalescing
- slow-client handling
- critical-client handling
- outbound disconnect policy
- outbound backpressure metrics

Therefore:

DO NOT create another backpressure system.

DO NOT create another rate limiter.

DO NOT create another outbound queue.

DO NOT create another slow-client manager.

DO NOT create another token-bucket implementation.

DO NOT move backpressure into Phase 10 Runtime.

DO NOT modify EventBus to perform client rate limiting.

DO NOT modify ReplayClock for transport backpressure.

Agent 11.7.1 remains the single authoritative outbound
backpressure/rate-control implementation.

=========================================================
AGENT OBJECTIVE
=========================================================

Perform a full architecture and implementation audit of the original
Roadmap Agent 11.10 requirement:

"Backpressure & Rate Control — Prevent slow clients from affecting
Runtime."

Determine whether the accepted Agent 11.7.1 implementation fully
satisfies the original Agent 11.10 requirement.

If it does:

    formally mark Agent 11.10 as SUPERSEDED / SATISFIED BY 11.7.1

and make the minimum required roadmap/documentation corrections.

If genuine gaps remain:

    extend Agent 11.7.1 only.

Do NOT create a new implementation.

=========================================================
CURRENT ACCEPTED ARCHITECTURE
=========================================================

The current transport architecture is:

Phase 10 Runtime
    ↓
EventBus
    ↓
Live / Replay Publishers
    ↓
11.8 Subscription System
    ↓
11.7.1 OutboundDeliveryController
    ↓
BoundedOutboundQueue
    ↓
ClientConnection
    ↓
WebSocket

Security/admission boundary:

Client
    ↓
11.6.3 Transport Hardening
    ↓
11.6.2 Rate Limiting & Abuse Protection
    ↓
11.6 Authentication / Authorization
    ↓
11.9 Connection & Session Management
    ↓
11.8 Subscription System
    ↓
11.7.1 Outbound Backpressure & Rate Control
    ↓
WebSocket Client

IMPORTANT:

11.6.2 protects transport admission/inbound abuse.

11.7.1 protects outbound delivery and slow clients.

These are separate responsibilities.

Do not merge them.

=========================================================
AGENT 11.7.1 ACCEPTED BASELINE
=========================================================

The accepted 11.7.1 implementation currently provides:

Package:

backend/api/outbound/

Components include:

- controller
- policy
- budget
- pressure
- reasons
- metrics

Architecture:

Runtime/EventBus
    ↓
publishers
    ↓
ClientConnection.enqueue_envelope
    ↓
OutboundDeliveryController.admit()
    ↓
BoundedOutboundQueue.offer()
    ↓
per-connection sender
    ↓
WebSocket client

Existing behavior:

- bounded outbound queues
- DROP_OLDEST preserved
- queue occupancy pressure states
- NORMAL
- ELEVATED
- HIGH
- CRITICAL
- optional queued-byte pressure
- per-connection token buckets
- telemetry rate control
- optional event/snapshot rate control
- aggregate rate control
- byte budgets
- optional principal budgets
- CONTROL > EVENT > SNAPSHOT > TELEMETRY priority
- CONTROL protected from normal rate limiting
- EVENT protected from telemetry shedding
- HIGH/CRITICAL telemetry/snapshot shedding
- optional forced coalescing
- slow-client detection
- critical grace period
- critical disconnect or shed policy
- automatic recovery
- per-connection isolation
- LIVE/REPLAY compatibility
- session isolation
- outbound metrics
- configuration validation

Master feature flag:

OUTBOUND_BACKPRESSURE_ENABLED=false

Existing tests and acceptance:

tests/api + Phase 10 + outbound:
277 passed

Focused outbound:
14 passed

Ruff:
clean

mypy:
clean

GATE-01…62:
applicable gates PASS

No production SLA was claimed.

=========================================================
AUDIT REQUIREMENTS
=========================================================

FIRST inspect the actual repository.

Do not assume the above summary is still exact.

Inspect:

1. backend/api/outbound/
2. ClientConnection
3. WebSocketConnectionManager
4. 11.8 TransportSubscriptionRegistry
5. LiveTelemetryStreamPublisher
6. ReplayStreamPublisher
7. Snapshot streaming
8. EventBus integration
9. 11.6.2 RateLimitService
10. 11.6.3 TransportHardening
11. 11.9 Connection & Session Management
12. bounded outbound queue
13. sender loop
14. connection cleanup
15. disconnect handling
16. configuration/settings
17. metrics
18. transport status/capabilities
19. tests/api/outbound
20. all relevant transport tests
21. Phase 10 tests
22. Phase 10 acceptance tests
23. architecture specifications
24. roadmap
25. streaming specification
26. replay specification
27. API documentation

Then compare the actual implementation against the original Agent
11.10 objective.

=========================================================
PRIMARY INVARIANT
=========================================================

The most important invariant is:

A slow WebSocket client MUST NEVER block or materially stall:

- Phase 10 Runtime
- EventBus
- LiveSessionAdapter
- Replay runtime
- ReplayClock
- TimelineService
- CacheManager
- telemetry production
- replay playback
- other clients

The Runtime MUST NOT wait for a client.

The EventBus MUST NOT wait for a client.

The ReplayClock MUST NOT wait for a client.

Client delivery is asynchronous and bounded.

=========================================================
NON-BLOCKING REQUIREMENT
=========================================================

Verify that:

Runtime/EventBus
    ↓
publisher
    ↓
enqueue/admit
    ↓
bounded queue

does not synchronously wait for:

- network transmission
- socket send completion
- slow client
- client acknowledgement
- client processing speed

If enqueue can block Runtime/EventBus, fix it through the existing
11.7.1 architecture.

Do not introduce Runtime-side throttling.

=========================================================
QUEUE REQUIREMENTS
=========================================================

Verify:

- every connection has bounded outbound state
- queue capacity is finite
- queued bytes can be bounded where configured
- one client cannot consume unbounded memory
- one client cannot consume another client's queue
- queue overflow cannot block Runtime
- queue overflow cannot block EventBus

Preserve existing:

DROP_OLDEST

unless actual repository evidence proves another policy is required.

Do not silently change queue semantics.

=========================================================
PRIORITY REQUIREMENTS
=========================================================

Verify the established priority:

CONTROL
    >
EVENT
    >
SNAPSHOT
    >
TELEMETRY

Preserve this behavior.

Do not implement transport-wide global FIFO that allows telemetry
flooding to starve control messages.

Do not reorder canonical Runtime sequences.

Do not modify source sequences.

=========================================================
TELEMETRY REQUIREMENTS
=========================================================

Telemetry is the highest-volume stream.

Verify telemetry can be shed/throttled under pressure without:

- modifying canonical telemetry payloads
- rewriting source sequence numbers
- changing Runtime timestamps
- changing telemetry ordering semantics
- modifying ReplayClock
- modifying LiveSessionAdapter timing
- modifying EventBus semantics

Transport may decide whether a frame is admitted to a particular
client queue.

Transport MUST NOT modify the canonical frame itself.

=========================================================
EVENT REQUIREMENTS
=========================================================

Events generally have higher delivery importance than telemetry.

Verify EVENT traffic is protected from telemetry shedding.

Do not silently drop critical/control events unless the existing
policy explicitly permits it.

If event loss behavior is configurable, document it.

=========================================================
SNAPSHOT REQUIREMENTS
=========================================================

Verify snapshots remain transport consumers.

Under pressure they may be:

- rate controlled
- coalesced
- shed

according to existing policy.

Do not modify RaceStateSnapshotEngine.

Do not make transport responsible for snapshot generation.

=========================================================
CONTROL REQUIREMENTS
=========================================================

CONTROL messages must remain protected.

Verify they are not accidentally subjected to telemetry rate limits.

Do not allow a telemetry flood to prevent control messages from
reaching a client where queue capacity permits.

=========================================================
RATE CONTROL
=========================================================

Verify the existing 11.7.1 token bucket implementation.

Check:

- monotonic clock
- refill behavior
- bounded state
- per-connection isolation
- optional principal budget
- telemetry budget
- event/snapshot budget
- aggregate budget
- byte budget
- disabled/default behavior

Do not create another rate limiter.

=========================================================
IMPORTANT DISTINCTION
=========================================================

11.6.2:

INBOUND / ADMISSION / ABUSE PROTECTION

Examples:

- connection rate
- reconnect rate
- authentication abuse
- subscription churn
- inbound message quotas
- concurrent connections
- payload admission

11.7.1:

OUTBOUND DELIVERY PROTECTION

Examples:

- slow client
- outbound queue pressure
- telemetry rate
- outbound bytes
- queue shedding
- coalescing
- critical slow-client handling

Do not collapse these systems.

=========================================================
SLOW CLIENT
=========================================================

A slow client is any client whose outbound queue cannot drain at the
rate required by its subscribed streams.

Verify the progression:

NORMAL
    ↓
ELEVATED
    ↓
HIGH
    ↓
CRITICAL

Verify recovery when the queue drains.

Verify a slow client cannot affect another client.

=========================================================
CRITICAL CLIENT
=========================================================

Verify existing behavior for sustained CRITICAL pressure.

Existing policy supports:

- grace period
- disconnect
or
- continue shedding

Do not invent a second policy.

If existing configuration is ambiguous, document the behavior.

=========================================================
COALESCING
=========================================================

Verify coalescing remains transport-only.

Allowed examples:

latest telemetry/snapshot representation for a connection

NOT allowed:

- modifying Runtime state
- changing canonical EventBus data
- changing replay state
- modifying ReplayClock
- mutating shared payload objects

Coalescing must never mutate canonical payloads.

=========================================================
LIVE / REPLAY
=========================================================

The same outbound controller must support:

LIVE
and
REPLAY

without becoming a timing authority.

Verify:

LIVE telemetry → LIVE clients only

REPLAY telemetry → REPLAY clients only

LIVE events → appropriate LIVE subscriptions

REPLAY events → appropriate REPLAY subscriptions

No transport backpressure operation may:

- pause LiveSessionAdapter
- pause ReplayClock
- alter replay speed
- alter replay position
- alter session timing
- introduce transport delay

=========================================================
SESSION ISOLATION
=========================================================

Verify:

Client A / Session A
cannot receive Session B data.

Backpressure state MUST be per connection.

One client's queue pressure MUST NOT trigger another client's
shedding.

One session's slow clients MUST NOT block another session.

=========================================================
PRINCIPAL ISOLATION
=========================================================

If principal-level outbound budgets are enabled:

verify:

Principal A's budget
does not consume
Principal B's budget.

If principal budgets are disabled by default, preserve that behavior.

Do not introduce distributed principal budgets.

=========================================================
CONNECTION INTEGRATION
=========================================================

Integrate with Agent 11.9.

Verify:

ConnectionManager
    ↓
ClientConnection
    ↓
OutboundDeliveryController

Connection lifecycle owns:

- connection
- lifecycle
- heartbeat
- cleanup

11.7.1 owns:

- outbound admission
- pressure
- rate
- shedding
- coalescing
- outbound critical handling

11.8 owns:

- subscription state

11.6.x owns:

- security/admission

Do not mix ownership.

=========================================================
DISCONNECT INTEGRATION
=========================================================

When Agent 11.9 closes a connection:

11.7.1 state MUST be released safely.

No:

- orphaned token bucket
- orphaned queue
- orphaned pressure state
- orphaned metrics registration
- background task

must remain.

Cleanup must be idempotent.

=========================================================
RECONNECT
=========================================================

Reconnect creates:

new connection ID
+
new outbound state

Old outbound state MUST NOT be reused accidentally.

No durable outbound queue.

No missed-frame replay.

No stale pressure state.

No old connection cleanup may affect the new connection.

=========================================================
MEMORY SAFETY
=========================================================

Verify bounded memory for:

- queues
- queued bytes
- token buckets
- pressure state
- coalescing state
- metrics state
- principal budgets if enabled

A malicious client must not create unbounded outbound state.

=========================================================
FAIRNESS
=========================================================

Verify one high-volume connection cannot consume shared transport
resources in a way that starves other clients.

Per-connection queues must remain isolated.

Where aggregate/principal budgets exist, verify they are bounded and
optional.

Do not introduce a global queue that becomes a bottleneck.

=========================================================
FAILURE CONTAINMENT
=========================================================

A failure in one client must remain local.

Examples:

Client A:
    queue full

must NOT cause:

Client B:
    queue full

or:

Runtime:
    blocked

or:

EventBus:
    blocked

or:

Replay:
    stopped

or:

Live telemetry:
    stopped

=========================================================
METRICS
=========================================================

Reuse the existing OutboundBackpressureMetrics.

Do not create another metrics system.

Verify useful metrics exist for:

- admitted
- rate limited
- dropped
- coalesced
- queue pressure
- slow clients
- critical clients
- disconnects
- bytes shed
- telemetry shed
- snapshot shed
- event protection
- control protection

Ensure metrics are bounded.

Prepare the data for Agent 11.12 Transport Observability.

=========================================================
LOGGING
=========================================================

Logs MUST NOT contain:

- access tokens
- credentials
- secrets
- full unbounded telemetry payloads
- full protocol payloads

Use structured categories.

Useful fields:

- connection_id
- session_id where permitted
- principal reference where permitted
- stream type
- pressure state
- admission reason
- drop reason
- coalesce reason
- disconnect reason

=========================================================
CONFIGURATION
=========================================================

Audit all existing:

OUTBOUND_BACKPRESSURE_*

configuration.

Do not add redundant environment variables.

Every setting must have:

- validation
- safe default
- documented semantics
- bounded values

Master feature flag remains:

OUTBOUND_BACKPRESSURE_ENABLED=false

unless the existing project decision has explicitly changed.

Do NOT silently turn it on.

=========================================================
DEFAULT-OFF REQUIREMENT
=========================================================

If 11.7.1 was intentionally default-off, preserve that decision.

Agent 11.10 MUST NOT enable production behavior merely by changing
defaults.

=========================================================
PERFORMANCE
=========================================================

Verify outbound admission is lightweight.

It must not:

- query PostgreSQL
- perform blocking network I/O
- call external services
- wait for Runtime
- wait for EventBus
- wait for another client

Do not claim production SLA numbers unless actual benchmarks are run.

If benchmarks are run, report:

BASELINE_NOT_PRODUCTION_SLA

=========================================================
TEST REQUIREMENTS
=========================================================

Audit existing tests first.

Then ensure coverage for:

1. bounded queue
2. queue overflow
3. DROP_OLDEST
4. queue pressure states
5. pressure recovery
6. telemetry rate limiting
7. event protection
8. snapshot control
9. control protection
10. byte budgets
11. aggregate budgets
12. principal budgets where enabled
13. coalescing
14. critical grace period
15. critical disconnect
16. critical shedding
17. slow client isolation
18. multi-client fairness
19. session isolation
20. principal isolation
21. LIVE isolation
22. REPLAY isolation
23. reconnect
24. stale state cleanup
25. connection cleanup
26. cleanup idempotency
27. Runtime non-blocking behavior
28. EventBus non-blocking behavior
29. ReplayClock non-blocking behavior
30. publisher non-blocking behavior
31. sender failure
32. queue failure
33. malformed configuration
34. disabled mode
35. enabled mode
36. metrics
37. memory bounds
38. concurrency
39. disconnect during pressure
40. reconnect during pressure

=========================================================
CONCURRENCY TESTS
=========================================================

Explicitly test:

- many fast clients + one slow client
- many slow clients
- simultaneous queue pressure
- pressure recovery
- disconnect during enqueue
- reconnect during cleanup
- heartbeat timeout during critical pressure
- server shutdown during critical pressure
- subscription removal during pressure
- LIVE/REPLAY mode transition during pressure

Required result:

No deadlock.

No Runtime blocking.

No EventBus blocking.

No cross-client queue contamination.

No cross-session delivery.

No leaked tasks.

No leaked state.

=========================================================
RUNTIME PROTECTION TEST
=========================================================

Create or verify a test proving:

Client A becomes extremely slow.

Client A's outbound queue fills.

Client A experiences:

HIGH
then
CRITICAL

while:

Client B continues receiving data.

And:

Phase 10 Runtime continues processing.

EventBus continues processing.

Replay continues processing.

This is the central acceptance requirement for Agent 11.10.

=========================================================
PROPERTY / INVARIANT TESTS
=========================================================

INVARIANT 1
A slow client cannot block Runtime.

INVARIANT 2
A slow client cannot block EventBus.

INVARIANT 3
A slow client cannot block ReplayClock.

INVARIANT 4
A slow client cannot block another client.

INVARIANT 5
Each connection has bounded outbound state.

INVARIANT 6
Outbound queues are connection-isolated.

INVARIANT 7
Canonical telemetry payloads are never mutated.

INVARIANT 8
Canonical source sequences are never overwritten.

INVARIANT 9
Transport sequence numbers remain transport-owned.

INVARIANT 10
LIVE and REPLAY streams remain isolated.

INVARIANT 11
Session isolation remains intact.

INVARIANT 12
11.6.2 remains the inbound/admission limiter.

INVARIANT 13
11.7.1 remains the outbound backpressure authority.

INVARIANT 14
11.8 remains the subscription authority.

INVARIANT 15
11.9 remains the connection lifecycle authority.

INVARIANT 16
No duplicate backpressure system exists.

INVARIANT 17
No duplicate rate limiter exists.

INVARIANT 18
No transport component becomes Runtime timing authority.

=========================================================
DO NOT IMPLEMENT
=========================================================

DO NOT implement:

- backend/api/backpressure2/
- another OutboundDeliveryController
- another token bucket
- another queue
- another rate limiter
- Redis
- distributed queues
- database-backed outbound state
- Runtime throttling
- EventBus throttling
- ReplayClock throttling
- telemetry mutation
- telemetry sequence rewriting
- global cross-client queue
- client-driven Runtime pacing
- durable outbound queues
- missed-frame recovery
- application idle disconnect
- Unity changes
- OBS changes
- AI changes
- prediction changes
- public API changes

=========================================================
DOCUMENTATION
=========================================================

If the audit confirms 11.7.1 fully satisfies the original 11.10
requirement:

Update the roadmap to state clearly:

Agent 11.10 — Backpressure & Rate Control

STATUS:
SUPERSEDED / SATISFIED BY AGENT 11.7.1

Authoritative implementation:
Agent 11.7.1 — Outbound Backpressure & Rate Control

Reason:
The functionality was implemented earlier in the revised Phase 11
execution order.

Do NOT leave the roadmap implying that another implementation is
required.

Update architecture/specification references if necessary.

Do NOT create a second specification unless the existing
OutboundBackpressureRateControlSpecification.md needs correction.

=========================================================
IF A REAL GAP EXISTS
=========================================================

If the audit discovers a genuine requirement from the original 11.10
that 11.7.1 does not satisfy:

1. Document the exact gap.
2. Explain why it is not already covered.
3. Extend 11.7.1.
4. Preserve all existing contracts.
5. Add regression tests.
6. Update the existing outbound specification.
7. Do NOT create Agent 11.10 infrastructure separate from 11.7.1.
8. Re-run all relevant Phase 10/11 tests.

Only modify the minimum necessary code.

=========================================================
ACCEPTANCE GATES
=========================================================

GATE-01  Existing 11.7.1 architecture audited
GATE-02  No duplicate backpressure system
GATE-03  No duplicate rate limiter
GATE-04  11.6.2 inbound rate limiting preserved
GATE-05  11.6.3 hardening preserved
GATE-06  11.7.1 remains outbound authority
GATE-07  11.8 subscription authority preserved
GATE-08  11.9 connection authority preserved
GATE-09  Runtime remains non-blocking
GATE-10  EventBus remains non-blocking
GATE-11  ReplayClock remains non-blocking
GATE-12  LiveSessionAdapter remains unaffected
GATE-13  bounded queues verified
GATE-14  queue overflow verified
GATE-15  DROP_OLDEST behavior verified
GATE-16  pressure states verified
GATE-17  pressure recovery verified
GATE-18  telemetry rate control verified
GATE-19  event protection verified
GATE-20  snapshot rate control verified
GATE-21  control protection verified
GATE-22  byte budgets verified
GATE-23  aggregate budgets verified
GATE-24  principal budgets verified where enabled
GATE-25  coalescing verified
GATE-26  slow-client isolation verified
GATE-27  critical-client handling verified
GATE-28  disconnect handling verified
GATE-29  reconnect handling verified
GATE-30  connection cleanup verified
GATE-31  subscription cleanup verified
GATE-32  session isolation verified
GATE-33  principal isolation verified
GATE-34  LIVE/REPLAY isolation verified
GATE-35  memory bounds verified
GATE-36  fairness verified
GATE-37  failure containment verified
GATE-38  concurrency verified
GATE-39  no Runtime timing authority
GATE-40  metrics verified
GATE-41  logging reviewed
GATE-42  configuration validated
GATE-43  default-off behavior preserved
GATE-44  malformed configuration tested
GATE-45  Runtime non-blocking test passes
GATE-46  slow-client isolation test passes
GATE-47  multi-client test passes
GATE-48  reconnect regression passes
GATE-49  connection regression passes
GATE-50  subscription regression passes
GATE-51  live streaming regression passes
GATE-52  replay streaming regression passes
GATE-53  Phase 10 regression passes
GATE-54  Phase 10 acceptance passes
GATE-55  API regression passes
GATE-56  Ruff clean
GATE-57  mypy clean
GATE-58  documentation reconciled
GATE-59  roadmap reconciled
GATE-60  Agent 11.10 duplicate implementation avoided

=========================================================
FINAL REPORT
=========================================================

At completion report:

1. STATUS
2. Audit findings
3. Existing 11.7.1 functionality verified
4. Original 11.10 requirements mapped to 11.7.1
5. Any genuine gaps discovered
6. Changes made, if any
7. Runtime protection verification
8. Slow-client behavior
9. Queue behavior
10. Rate-control behavior
11. Coalescing behavior
12. Critical-client behavior
13. LIVE/REPLAY behavior
14. Session isolation
15. Principal isolation
16. Connection integration
17. Subscription integration
18. Metrics
19. Configuration
20. Files modified
21. Exact test results
22. Ruff result
23. mypy result
24. Benchmark result if any
25. GATE-01…60 results
26. Limitations
27. Remaining risks
28. Roadmap status

If no genuine implementation gap exists, explicitly report:

AGENT 11.10 — SUPERSEDED / SATISFIED BY AGENT 11.7.1

Do NOT report "ACCEPTED" as a new implementation if no new
implementation was required.

=========================================================
START
=========================================================

FIRST audit Agent 11.7.1 against the original Agent 11.10 requirement.

THEN test the central invariant:

SLOW CLIENT
    ↓
bounded outbound pressure
    ↓
client isolated

while:

Runtime
EventBus
ReplayClock
other clients

continue unaffected.

IF 11.7.1 already satisfies the requirement:

    make no duplicate implementation
    reconcile documentation
    close Agent 11.10 as superseded/satisfied

IF a genuine gap exists:

    extend 11.7.1 only

The final architecture MUST have:

ONE inbound/admission limiter — 11.6.2
ONE outbound backpressure/rate-control authority — 11.7.1
ONE subscription system — 11.8
ONE connection lifecycle — 11.9
ONE Runtime authority — Phase 10
```

## User

## AGENT 11.10 — SUPERSEDED / SATISFIED BY AGENT 11.7.1

No second backpressure system was created. Audit confirms **11.7.1** already owns outbound delivery protection for slow clients.

### 1. STATUS

**SUPERSEDED / SATISFIED BY Agent 11.7.1** — not a new implementation.

### 2–4. Audit / mapping

Original 11.10 goal (“prevent slow clients from affecting Runtime”) maps to `backend/api/outbound/` + bounded WS queues:

| Original 11.10 need           | 11.7.1 coverage                                        |
| ----------------------------- | ------------------------------------------------------ |
| Slow-client isolation         | Per-connection admit + queue                           |
| Bounded queues                | `BoundedOutboundQueue` + DROP\_OLDEST                  |
| Rate control                  | Token buckets (monotonic)                              |
| Pressure NORMAL→CRITICAL      | Implemented                                            |
| Non-blocking Runtime/EventBus | Sync `offer_bus_event` / `enqueue_envelope` (no await) |
| Default safe                  | `OUTBOUND_BACKPRESSURE_ENABLED=false` preserved        |

### 5. Genuine gaps

None functional. Docs had stale **11.11** “future” wording.

### 6. Changes made

- Roadmap: **11.10** and **11.11** marked SUPERSEDED BY **11.7.1**
- Spec/README/ratelimit refs reconciled
- Added `test_invariant_slow_client_cannot_block_runtime_or_peer`

### 7–17. Verified behavior

Slow A → bounded pressure / sheds; peer B still receives; `offer_bus_event` sync & <1s for 80 offers; CONTROL/EVENT protection, coalescing, LIVE/REPLAY, session/principal isolation, 11.8/11.9 ownership unchanged. Inbound remains **11.6.2**.

### 18–19. Metrics / config

Existing `OutboundBackpressureMetrics`; flag remains **OFF** by default.

### 20. Files modified

Docs/roadmap/README/ratelimit note; `tests/api/outbound/test_outbound_backpressure.py`. No new package.

### 21–23. Exact results

| Check                               | Result         |
| ----------------------------------- | -------------- |
| `tests/api` + Phase 10 + acceptance | **329 passed** |
| Outbound focused                    | **15 passed**  |
| Ruff                                | **clean (0)**  |
| mypy `backend/api/outbound`         | **clean (0)**  |

### 24. Benchmarks

None (`BASELINE_NOT_PRODUCTION_SLA` N/A).

### 25. GATE-01…60

All applicable gates **PASS** (no duplicate system).

### 26–27. Limitations / risks

Default-off until ops enable; process-local principal budgets; dequeue still FIFO (priority via admit/drop).

### 28. Roadmap status

```
11.7.1  ACCEPTED (authoritative outbound backpressure)
11.10   SUPERSEDED / SATISFIED BY 11.7.1
11.11   SUPERSEDED / SATISFIED BY 11.7.1
```

**Ownership retained:** 11.6.2 inbound · **11.7.1 outbound** · 11.8 subscriptions · 11.9 connection · Phase 10 Runtime.

**Recommended next:** Observability **11.12 / 11.13** — paste the agent prompt when ready.

## Assistant

Perfect. **Agent 11.10 is correctly closed as superseded**, with no duplicate implementation.

The Phase 11 ownership model is now clean:

```text
11.6.2  → Inbound admission / abuse protection
11.6.3  → Transport hardening
11.7    → Replay streaming
11.7.1  → Outbound backpressure / rate control
11.8    → Subscriptions
11.9    → Connection / session lifecycle
11.10   → SUPERSEDED by 11.7.1
11.11   → SUPERSEDED by 11.7.1
```

The important architectural invariant is preserved:

```text
                    PHASE 10 RUNTIME
                           │
                       EventBus
                           │
                 ┌─────────┴─────────┐
                 │                   │
                LIVE               REPLAY
                 │                   │
                 └─────────┬─────────┘
                           │
                    Stream Publishers
                           │
                        11.8
                    Subscriptions
                           │
                       11.7.1
                Outbound Protection
                           │
                    Bounded Queue
                           │
                        11.9
                 Connection Lifecycle
                           │
                       WebSocket
```

And critically:

**Runtime never waits for the client.**

The new invariant test is particularly useful because it directly validates the core purpose of the original 11.10 requirement.

### Next phase

The remaining planned Phase 11 sequence is now:

| Agent | Component | Status |
|---|---|---|
| 11.12 | **Transport Observability** | ⏳ Next |
| 11.13 | Transport Integration Testing | ⏳ |
| 11.14 | Live Streaming Acceptance | ⏳ |
| 11.15 | Phase 11 Acceptance | ⏳ |

I recommend **11.12 next**, and it should **aggregate/standardize the metrics already produced by 11.6.x, 11.7/11.7.1, 11.8 and 11.9 rather than creating duplicate metrics ownership**.

## User

Please give commands for Agent 11.11	Transport Authentication & Authorization	Secure API/WS access boundary ( 1 click copy and paste cursor friendly)

## Assistant

Yes. **Agent 11.11 should not create a second authentication/authorization system.** Your accepted Agent 11.6 already owns the transport security boundary, just as 11.7.1 owns outbound backpressure.

Use the following as a **1-click copy/paste Cursor prompt**. It will audit the original 11.11 requirement and formally reconcile it with 11.6 rather than duplicating security infrastructure.

```text
=========================================================
RACEVISION — AGENT 11.11
TRANSPORT AUTHENTICATION & AUTHORIZATION
=========================================================

IMPORTANT ARCHITECTURE NOTICE
==============================

Agent 11.6 — Transport Authentication & Authorization is ALREADY
IMPLEMENTED and ACCEPTED.

Agent 11.6 is the authoritative transport authentication and
authorization boundary.

DO NOT create another authentication system.

DO NOT create another authorization system.

DO NOT create another Principal implementation.

DO NOT create another AuthorizationPolicy.

DO NOT create another JWT/token validator.

DO NOT create another WebSocket authentication layer.

DO NOT create another REST authentication middleware.

DO NOT move authentication into Phase 10 Runtime.

DO NOT make Runtime identity-aware.

DO NOT create a second security dependency system.

Agent 11.6 remains the single authoritative transport
authentication/authorization implementation.

=========================================================
AGENT OBJECTIVE
=========================================================

Perform a complete audit of the original Phase 11 Agent 11.11
requirement:

"Transport Authentication & Authorization — Secure API/WS access
boundary"

Determine whether the accepted Agent 11.6 implementation fully
satisfies the original Agent 11.11 requirement.

If it does:

    formally mark Agent 11.11 as
    SUPERSEDED / SATISFIED BY AGENT 11.6

and reconcile all roadmap/specification/documentation references.

If genuine security gaps remain:

    extend Agent 11.6 only.

DO NOT create a second security architecture.

=========================================================
CURRENT SECURITY OWNERSHIP
=========================================================

The transport security architecture is:

Client
  ↓
11.6.3 Transport Hardening
  ↓
11.6.2 Rate Limiting / Abuse Protection
  ↓
11.6 Authentication / Authorization
  ↓
11.9 Connection Management
  ↓
11.8 Subscription Authorization / Registry
  ↓
11.7.1 Outbound Protection
  ↓
WebSocket / REST
  ↓
Phase 10 Runtime

IMPORTANT:

11.6 owns:

- authentication
- principal creation
- principal identity
- authorization policy
- transport security boundary
- REST authorization
- WebSocket authorization
- capability permissions
- subscription permissions
- session access policy
- command access policy

11.6.2 owns:

- rate limiting
- admission control
- authentication abuse protection
- authorization abuse protection

11.6.3 owns:

- request hardening
- WebSocket protocol hardening
- payload limits
- Origin handling
- envelope validation
- error sanitization

11.8 owns:

- subscription lifecycle
- subscription registry
- subscription-specific authorization integration

11.9 owns:

- connection lifecycle
- principal binding to connection
- heartbeat
- connection cleanup

11.7.1 owns:

- outbound delivery protection

Phase 10 owns:

- Runtime
- EventBus
- LiveSessionAdapter
- Replay Runtime
- Timeline
- Cache
- ReplayClock

Phase 10 MUST remain identity-unaware.

=========================================================
ACCEPTED AGENT 11.6 BASELINE
=========================================================

FIRST inspect the actual repository.

Do not rely solely on this summary.

Inspect all existing security implementation including:

- backend/api/security/
- authentication providers
- principal models
- AuthorizationPolicy
- REST dependencies
- WebSocket authentication
- permission mapping
- capability mapping
- command authorization
- subscription authorization
- session authorization
- connection principal binding
- security settings
- security exceptions
- transport error mapping
- app wiring
- tests/api/security
- WebSocket security tests
- command authorization tests
- telemetry authorization tests
- replay authorization tests
- subscription authorization tests
- documentation
- roadmap
- architecture specification
- API specification

Agent 11.6 architecture was:

Client
  ↓
Provider
  ↓
Principal
  ↓
AuthorizationPolicy
  ↓
REST / WebSocket
  ↓
existing services / dispatchers
  ↓
Runtime

Runtime remains identity-unaware.

Preserve this architecture.

=========================================================
PRIMARY SECURITY INVARIANT
=========================================================

Authentication and authorization MUST remain at the transport boundary.

The Runtime MUST NOT need to know:

- user identity
- access token
- authentication provider
- roles
- scopes
- permissions
- authorization decisions

Runtime receives already-authorized transport operations.

=========================================================
AUTHENTICATION REQUIREMENTS
=========================================================

Audit that REST and WebSocket clients can be authenticated through
the existing Agent 11.6 provider architecture.

Verify:

- unauthenticated requests are rejected where authentication is
  required
- authentication failures fail closed
- invalid credentials are rejected
- expired credentials are rejected where applicable
- malformed credentials are rejected
- principal creation is deterministic
- principal identity cannot be overwritten after connection binding
- authenticated identity is propagated consistently
- credentials are not exposed in logs
- credentials are not exposed in errors
- credentials are not persisted unnecessarily

Do not invent a new credential format.

Do not add a second token validator.

Use the existing provider abstraction.

=========================================================
PRINCIPAL REQUIREMENTS
=========================================================

Verify that the authenticated Principal is the authoritative
transport identity.

A connection MUST NOT be able to:

- change its principal
- impersonate another principal
- modify principal permissions
- modify its own roles/scopes
- inject an arbitrary principal ID

Verify compatibility with Agent 11.9:

bind_principal()

must remain immutable after successful binding.

Reconnect:

new connection
+
new authentication
+
new principal binding

Old connection identity MUST NOT leak into the new connection.

=========================================================
AUTHORIZATION REQUIREMENTS
=========================================================

Verify the existing AuthorizationPolicy.

Authorization decisions MUST be explicit.

Audit permissions for:

- REST read
- REST write
- command execution
- live telemetry
- live events
- snapshots
- replay telemetry
- replay events
- replay access
- subscriptions
- runtime status
- capabilities
- session-scoped operations

Verify denied operations fail closed.

Do not use authentication as authorization.

Being authenticated does NOT automatically grant every operation.

=========================================================
LIVE STREAM AUTHORIZATION
=========================================================

Verify Agent 11.6.1 integration.

LIVE:

TELEMETRY
EVENTS
SNAPSHOT
MODE
RUNTIME_STATUS

must use the existing permission mapping.

Specifically verify the existing mapping for:

transport:subscribe
live:read

where applicable.

Do not create another telemetry-specific authorization system.

=========================================================
REPLAY AUTHORIZATION
=========================================================

Verify Agent 11.7 integration.

REPLAY subscriptions and replay data must use the existing security
policy.

Verify the existing mode-aware permission mapping:

LIVE:
    live read permissions

REPLAY:
    replay read permissions

Do not create a second replay authorization system.

Verify:

LIVE clients cannot receive unauthorized REPLAY data.

REPLAY clients cannot bypass replay permissions.

Mode switching cannot bypass authorization.

=========================================================
SESSION ISOLATION
=========================================================

Authorization must be evaluated together with session isolation.

A principal authorized for:

Session A

must not automatically receive:

Session B

unless policy explicitly permits it.

Verify:

- session_id authorization
- session filter validation
- subscription session isolation
- connection principal scope
- delivery-time principal/session checks where already implemented

Do not rely solely on client-supplied session IDs.

=========================================================
SUBSCRIPTION AUTHORIZATION
=========================================================

Audit Agent 11.8.

The flow must remain:

WS subscribe
    ↓
authentication
    ↓
authorization
    ↓
subscription quota
    ↓
subscription registry

Do not allow a subscription to bypass authorization.

Verify all subscription types:

- TELEMETRY
- EVENTS
- SNAPSHOT
- REPLAY
- MODE
- RUNTIME_STATUS

remain subject to the appropriate authorization policy.

=========================================================
COMMAND AUTHORIZATION
=========================================================

Audit existing REST/WS command dispatch.

Verify:

authenticated
does not mean
authorized.

Commands must use the existing policy.

Unauthorized command requests must be rejected before reaching
protected Runtime operations.

Do not move command authorization into Phase 10.

=========================================================
REST SECURITY
=========================================================

Audit REST endpoints.

Verify protected endpoints consistently apply the existing security
dependency/policy.

Check:

- capabilities
- runtime routes
- session routes
- command routes
- telemetry routes
- replay routes
- status routes

Health/readiness endpoints that are intentionally public must remain
public according to existing policy.

Do not accidentally require authentication for infrastructure health
unless the existing architecture explicitly requires it.

=========================================================
WEBSOCKET SECURITY
=========================================================

Audit:

WS /api/v1/ws

Authentication MUST occur according to the existing Agent 11.6
architecture.

Integrate correctly with Agent 11.9:

authentication
    ↓
principal binding
    ↓
connection accepted
    ↓
READY
    ↓
subscriptions

Verify there is no unauthenticated open socket waiting indefinitely
for authentication if the existing architecture requires
pre-accept authentication.

Do not create a second WebSocket security manager.

=========================================================
AUTHORIZATION AT DELIVERY
=========================================================

Where the existing implementation performs delivery-time
principal/session validation, preserve it.

Verify that a previously authorized subscription cannot continue
delivering data after its authorization context becomes invalid.

Do not make outbound backpressure responsible for authorization.

Do not make publishers responsible for authentication.

The security boundary remains upstream.

=========================================================
ERROR HANDLING
=========================================================

Security failures must use stable transport errors.

Client-visible errors MUST NOT reveal:

- access tokens
- secrets
- credentials
- internal stack traces
- filesystem paths
- database connection information
- internal authentication implementation details
- sensitive principal data

Differentiate appropriately between:

UNAUTHENTICATED

and

UNAUTHORIZED

according to the existing transport error contract.

Do not expose unnecessary security details that enable enumeration.

=========================================================
FAIL-CLOSED REQUIREMENT
=========================================================

Security operations must fail closed.

If authentication cannot be established:

    reject.

If authorization cannot be established:

    reject.

If required policy information is unavailable:

    reject.

Do not silently convert security failures into anonymous access.

Transport rate limiting may have its existing independently
documented fail-open behavior where appropriate.

Do not alter 11.6.2 semantics.

=========================================================
AUTHENTICATION VS RATE LIMITING
=========================================================

Maintain this separation:

11.6
    Authentication / Authorization

11.6.2
    Rate Limiting / Abuse Protection

11.6.3
    Transport Hardening

Do not duplicate any of these.

The intended request path is:

Client
  ↓
Hardening
  ↓
Rate Limit / Admission
  ↓
Authentication / Authorization
  ↓
Connection / Subscription
  ↓
Runtime-facing transport handlers

Use the actual repository order if it differs and document the
verified order.

Do not rearrange middleware casually.

=========================================================
AUTHORIZATION VS SUBSCRIPTION QUOTAS
=========================================================

Authorization determines:

"May this principal perform this operation?"

11.6.2 determines:

"Is this request within the admission/rate policy?"

11.8 determines:

"Can this connection maintain this subscription within quotas?"

These are different decisions.

Do not merge them.

=========================================================
SECURITY AND OUTBOUND DELIVERY
=========================================================

11.7.1 MUST NOT become an authorization system.

Outbound backpressure decides:

"Can this message be admitted to this connection's bounded outbound
delivery path?"

It does NOT decide:

"Is this principal allowed to receive this data?"

Authorization remains 11.6.

=========================================================
SECURITY AND RUNTIME
=========================================================

Phase 10 Runtime MUST remain identity-unaware.

Do not add:

- Principal to Runtime APIs
- token checks to Runtime
- authorization checks to EventBus
- user roles to ReplayClock
- authentication dependencies to LiveSessionAdapter
- authorization state to TimelineService

If an existing implementation violates this principle, identify it
and propose the minimum transport-boundary correction.

=========================================================
TENANT / PRINCIPAL / SESSION BOUNDARIES
=========================================================

Audit all existing identity fields and scoping.

Verify that:

- principal identity is immutable
- tenant identity cannot be spoofed
- session identity is validated
- subscriptions cannot escape their authorized scope
- connections cannot impersonate another principal
- delivery does not cross security boundaries

Do not add new multi-tenant infrastructure unless an actual existing
security requirement requires it.

=========================================================
SECURITY CONFIGURATION
=========================================================

Audit existing security settings.

Verify:

- safe defaults
- validation
- bounded values
- no plaintext secret logging
- environment configuration
- production configuration behavior
- test configuration
- disabled-development behavior

Do NOT invent redundant:

AUTH_ENABLED
AUTH2_ENABLED
JWT_ENABLED

flags if the existing security architecture already defines the
correct configuration.

=========================================================
SECRET HANDLING
=========================================================

Search for accidental exposure of:

- access tokens
- API keys
- Authorization headers
- cookies where sensitive
- passwords
- client secrets
- private signing material

Check:

- logs
- exceptions
- metrics
- debug output
- tests
- snapshots
- protocol envelopes

Do not print credentials during tests.

=========================================================
ORIGIN / WEBSOCKET SECURITY
=========================================================

Agent 11.6.3 already owns Origin hardening.

Verify compatibility with:

WS_ALLOWED_ORIGINS

Do not move Origin validation into Agent 11.11.

Do not create another Origin validator.

Native-client behavior must remain consistent with the accepted
11.6.3 policy.

=========================================================
AUTHENTICATION ABUSE
=========================================================

Agent 11.6.2 owns abuse protection.

Verify authentication failures feed into the existing abuse/rate
limiting mechanism where appropriate.

Do not create another brute-force protection system.

Do not create another failed-login counter.

=========================================================
OBSERVABILITY
=========================================================

Reuse existing security metrics.

Audit existing metrics for:

- authentication attempts
- authentication failures
- authorization denials
- permission checks
- connection rejects
- subscription denials
- command denials
- security errors

Do not create a competing security metrics subsystem.

Prepare existing metrics for Agent 11.12 Transport Observability.

Metrics MUST NOT contain:

- tokens
- passwords
- secrets
- unnecessary personal information

=========================================================
LOGGING
=========================================================

Security logs should contain useful bounded context such as:

- request/correlation ID
- connection ID
- principal reference where appropriate
- operation
- permission
- denial reason category

Do NOT log:

- Authorization header
- bearer token
- password
- private key
- session credentials
- full sensitive payload

=========================================================
SECURITY TEST REQUIREMENTS
=========================================================

Audit all existing security tests first.

Then verify coverage for:

1. unauthenticated REST request
2. authenticated REST request
3. unauthorized REST request
4. authenticated WebSocket
5. unauthenticated WebSocket
6. invalid credentials
7. expired credentials where supported
8. malformed credentials
9. immutable principal
10. principal spoofing attempt
11. unauthorized telemetry subscription
12. authorized telemetry subscription
13. unauthorized event subscription
14. authorized event subscription
15. unauthorized snapshot subscription
16. authorized snapshot subscription
17. unauthorized replay subscription
18. authorized replay subscription
19. LIVE/REPLAY permission separation
20. session isolation
21. cross-session access attempt
22. command authorization
23. unauthorized command
24. authorized command
25. subscription replacement authorization
26. unsubscribe behavior
27. reconnect re-authentication
28. old principal cannot affect new connection
29. authorization after reconnect
30. security failure sanitization
31. token non-disclosure
32. secret non-disclosure
33. rate-limit/security integration
34. Origin/security integration
35. hardening/security integration
36. connection lifecycle/security integration
37. subscription/security integration
38. delivery/security integration
39. Runtime remains identity-unaware
40. EventBus remains identity-unaware
41. ReplayClock remains identity-unaware

=========================================================
SECURITY INVARIANTS
=========================================================

INVARIANT 1
Every protected transport operation has an authentication decision.

INVARIANT 2
Every protected operation has an authorization decision.

INVARIANT 3
Authentication does not imply authorization.

INVARIANT 4
Authorization occurs before protected Runtime operations.

INVARIANT 5
Runtime remains identity-unaware.

INVARIANT 6
Principal identity is immutable after binding.

INVARIANT 7
A client cannot spoof another principal.

INVARIANT 8
A client cannot expand its own permissions.

INVARIANT 9
Session IDs do not grant authorization.

INVARIANT 10
Subscription creation cannot bypass authorization.

INVARIANT 11
LIVE permissions cannot automatically grant REPLAY access.

INVARIANT 12
REPLAY permissions cannot automatically grant LIVE access.

INVARIANT 13
Cross-session delivery is prohibited unless explicitly authorized.

INVARIANT 14
Commands cannot bypass transport authorization.

INVARIANT 15
Outbound backpressure cannot bypass authorization.

INVARIANT 16
Rate limiting cannot grant authorization.

INVARIANT 17
Hardening cannot grant authorization.

INVARIANT 18
Credentials are never exposed to clients through internal errors.

INVARIANT 19
Credentials are never logged.

INVARIANT 20
Security failures fail closed.

INVARIANT 21
There is ONE transport authentication authority.

INVARIANT 22
There is ONE transport authorization authority.

=========================================================
DO NOT IMPLEMENT
=========================================================

DO NOT implement:

backend/api/auth2/
backend/api/authz2/

another Principal class

another AuthorizationPolicy

another JWT validator

another OAuth validator

another WebSocket auth manager

another REST auth middleware

another permission registry

another role system

another subscription authorization engine

another session authorization engine

another security metrics system

another brute-force limiter

another security state database

Redis security state

database-backed auth state

Runtime authentication

EventBus authorization

ReplayClock authorization

LiveSessionAdapter authentication

=========================================================
IF NO GAPS EXIST
=========================================================

If Agent 11.6 fully satisfies Agent 11.11:

DO NOT modify security implementation.

Reconcile documentation only.

Roadmap:

11.6
    ACCEPTED — Transport Authentication & Authorization

11.11
    SUPERSEDED / SATISFIED BY 11.6

Explain:

Agent 11.11 was retained in the original Phase 11 roadmap but its
required functionality was implemented earlier under Agent 11.6.

The accepted Agent 11.6 implementation remains the single authority.

=========================================================
IF A REAL SECURITY GAP EXISTS
=========================================================

If the audit discovers a genuine requirement not covered by 11.6:

1. Identify the exact requirement.
2. Show the existing implementation.
3. Explain the gap.
4. Implement the minimum required correction.
5. Extend Agent 11.6.
6. Do not create a second security system.
7. Preserve Runtime identity-unaware architecture.
8. Add regression tests.
9. Update the existing security specification.
10. Update the roadmap.
11. Run all Phase 10 and Phase 11 regressions.

=========================================================
ACCEPTANCE GATES
=========================================================

GATE-01  Existing Agent 11.6 implementation audited
GATE-02  No duplicate authentication system
GATE-03  No duplicate authorization system
GATE-04  Principal architecture preserved
GATE-05  AuthorizationPolicy remains authoritative
GATE-06  REST authentication verified
GATE-07  REST authorization verified
GATE-08  WebSocket authentication verified
GATE-09  WebSocket authorization verified
GATE-10  Principal immutability verified
GATE-11  Principal spoofing rejected
GATE-12  Authentication failure rejected
GATE-13  Authorization failure rejected
GATE-14  Fail-closed behavior verified
GATE-15  LIVE telemetry authorization verified
GATE-16  LIVE event authorization verified
GATE-17  Snapshot authorization verified
GATE-18  REPLAY authorization verified
GATE-19  LIVE/REPLAY isolation verified
GATE-20  Session isolation verified
GATE-21  Subscription authorization verified
GATE-22  Command authorization verified
GATE-23  Reconnect re-authentication verified
GATE-24  Old connection identity isolation verified
GATE-25  11.6.2 abuse integration verified
GATE-26  11.6.3 hardening integration verified
GATE-27  11.8 subscription integration verified
GATE-28  11.9 connection integration verified
GATE-29  11.7.1 outbound separation verified
GATE-30  Runtime remains identity-unaware
GATE-31  EventBus remains identity-unaware
GATE-32  ReplayClock remains identity-unaware
GATE-33  Session authorization verified
GATE-34  Tenant/principal boundaries verified
GATE-35  Credential non-disclosure verified
GATE-36  Secret logging audit passed
GATE-37  Error sanitization verified
GATE-38  Origin ownership remains 11.6.3
GATE-39  No duplicate abuse protection
GATE-40  Security metrics audited
GATE-41  Security configuration audited
GATE-42  Security tests pass
GATE-43  Transport regression tests pass
GATE-44  Phase 10 regression passes
GATE-45  Phase 10 acceptance passes
GATE-46  Ruff clean
GATE-47  mypy clean
GATE-48  Documentation reconciled
GATE-49  Roadmap reconciled
GATE-50  Agent 11.11 duplicate implementation avoided

=========================================================
FINAL REPORT
=========================================================

At completion report:

1. STATUS
2. Audit findings
3. Existing Agent 11.6 coverage
4. Original 11.11 → 11.6 requirement mapping
5. Genuine gaps, if any
6. Changes made, if any
7. Authentication behavior
8. Authorization behavior
9. Principal behavior
10. REST security
11. WebSocket security
12. LIVE authorization
13. REPLAY authorization
14. Subscription authorization
15. Command authorization
16. Session isolation
17. Reconnect security
18. Rate-limit integration
19. Hardening integration
20. Connection integration
21. Outbound separation
22. Runtime identity-unaware verification
23. Metrics
24. Secret/logging audit
25. Error handling
26. Configuration
27. Files modified
28. Exact test results
29. Ruff result
30. mypy result
31. Benchmark result if any
32. GATE-01…50 results
33. Limitations
34. Remaining risks
35. Roadmap status

If no genuine implementation gap exists, explicitly report:

AGENT 11.11 — SUPERSEDED / SATISFIED BY AGENT 11.6

Do NOT report a new implementation as ACCEPTED.

=========================================================
START
=========================================================

FIRST audit Agent 11.6 against the original Agent 11.11 requirement.

THEN verify the central security invariant:

UNAUTHENTICATED CLIENT
        ↓
       REJECT

AUTHENTICATED CLIENT
        ↓
AUTHORIZATION POLICY
        ↓
   ALLOWED OPERATION
        ↓
TRANSPORT HANDLER
        ↓
PHASE 10 RUNTIME

The Runtime MUST remain identity-unaware.

IF Agent 11.6 already satisfies the requirement:

    make no duplicate implementation
    reconcile documentation
    close Agent 11.11 as superseded/satisfied

IF a genuine gap exists:

    extend Agent 11.6 only.

The final architecture MUST have:

ONE authentication authority — 11.6
ONE authorization authority — 11.6
ONE inbound abuse authority — 11.6.2
ONE hardening authority — 11.6.3
ONE subscription authority — 11.8
ONE connection authority — 11.9
ONE outbound protection authority — 11.7.1
ONE Runtime authority — Phase 10
```

## User

## AGENT 11.11 — SUPERSEDED / SATISFIED BY AGENT 11.6

No second auth/authz system was created. Agent **11.6** (`backend/api/security/`) already owns the transport security boundary.

### 1. STATUS

**SUPERSEDED / SATISFIED BY Agent 11.6** — documentation reconciliation only.

### 2–4. Audit / mapping

Original 11.11 (“Secure API/WS access boundary”) maps to accepted 11.6:

| Requirement                | 11.6 coverage                            |
| -------------------------- | ---------------------------------------- |
| Auth providers / Principal | `security/provider.py`, `models.py`      |
| AuthorizationPolicy        | `security/policy.py` + mapping           |
| REST / WS auth             | DI + pre-accept WS auth                  |
| LIVE / REPLAY permissions  | mode-aware `permission_for_subscription` |
| Principal immutability     | `bind_principal` (11.9)                  |
| Runtime identity-unaware   | no `Principal` in `backend/runtime/`     |

### 5. Genuine gaps

None blocking. Documented limitations only (no distributed revocation, no OIDC UI).

### 6. Changes made

Docs/roadmap only. Corrected numbering collision: interim docs had aliased **11.11 → backpressure**; authentic **11.11 = auth → 11.6**, **11.10 = backpressure → 11.7.1**.

### 7–22. Verified (summary)

Auth fail-closed; authz ≠ authentication; LIVE/REPLAY/session/command/subscribe paths; reconnect re-auth; 11.6.2 abuse + 11.6.3 Origin stay separate; 11.7.1 is not authz; Runtime/EventBus/ReplayClock identity-unaware.

### 23–26. Metrics / secrets / errors / config

Existing security metrics retained; no credential logging/errors; `AUTH_ENABLED` unchanged.

### 27. Files modified

`docs/Roadmap.md`, auth/outbound/rate-limit/hardening/replay specs, `backend/api/README.md`, `ratelimit/__init__.py`.

### 28–30. Exact results

| Check                               | Result         |
| ----------------------------------- | -------------- |
| `tests/api` + Phase 10 + acceptance | **329 passed** |
| Ruff (`security` / ratelimit)       | **clean (0)**  |
| mypy `backend/api/security`         | **clean (0)**  |

### 31. Benchmarks

None.

### 32. GATE-01…50

All applicable gates **PASS** (no duplicate auth).

### 33–34. Limitations / risks

No distributed token revocation; JWT misuse remains ops risk until expiry.

### 35. Roadmap status

```
11.6   ACCEPTED — Transport Authentication & Authorization (authority)
11.10  SUPERSEDED / SATISFIED BY 11.7.1  (outbound backpressure)
11.11  SUPERSEDED / SATISFIED BY 11.6    (transport auth)
```

**Ownership:** ONE auth/authz = **11.6** · ONE inbound abuse = **11.6.2** · ONE hardening = **11.6.3** · ONE outbound = **11.7.1** · ONE subscriptions = **11.8** · ONE connection = **11.9** · ONE Runtime = Phase 10.

**Recommended next:** Observability **11.12 / 11.13** — paste the agent prompt when ready.

## Assistant

Excellent. **Agent 11.11 is correctly closed as SUPERSEDED / SATISFIED BY 11.6**, with no duplicate authentication or authorization implementation.

The numbering/ownership collision has also been correctly resolved.

### Current Phase 11 state

| Agent | Component | Status | Authority |
|---|---|---|---|
| **11.6** | Transport Authentication & Authorization | ✅ ACCEPTED | Auth/AuthZ |
| **11.6.1** | Live Telemetry Streaming | ✅ ACCEPTED | Live streaming |
| **11.6.2** | Rate Limiting & Abuse Protection | ✅ ACCEPTED | Inbound admission |
| **11.6.3** | Transport Hardening | ✅ ACCEPTED | REST/WS hardening |
| **11.7** | Replay Streaming | ✅ ACCEPTED | Replay streaming |
| **11.7.1** | Outbound Backpressure & Rate Control | ✅ ACCEPTED | Outbound protection |
| **11.8** | Subscription System | ✅ ACCEPTED | Subscriptions |
| **11.9** | Connection & Session Management | ✅ ACCEPTED | Connection lifecycle |
| **11.10** | Backpressure & Rate Control | 🔒 SUPERSEDED | 11.7.1 |
| **11.11** | Transport Authentication & Authorization | 🔒 SUPERSEDED | 11.6 |
| **11.12** | Transport Observability | ⏳ NEXT | — |
| **11.13** | Transport Integration Testing | ⏳ | — |
| **11.14** | Live Streaming Acceptance | ⏳ | — |
| **11.15** | Phase 11 Acceptance | ⏳ | — |

### The architecture is now nicely separated

```text
                         PHASE 10
                    UNIFIED RUNTIME
                           │
                 ┌─────────┴─────────┐
                 │                   │
                LIVE               REPLAY
                 │                   │
                 └─────────┬─────────┘
                           │
                       EventBus
                           │
                 ┌─────────▼─────────┐
                 │  Stream Publishers │
                 └─────────┬─────────┘
                           │
                      Transport
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
     REST/WS          Subscriptions       Connections
        │                  │                  │
      11.6               11.8               11.9
   Auth/AuthZ
        │
      11.6.2
  Inbound Abuse
        │
      11.6.3
    Hardening
        │
      11.7.1
 Outbound Protection
        │
     Client
```

Most importantly, **there is no security logic leaking into the Phase 10 Runtime**.

The remaining work should now move toward **observability and verification rather than creating more transport subsystems**.

**Next logical agent: 11.12 — Transport Observability.**

## User

Please give commands for Agent 11.12	Transport Observability	Metrics, health, connection statistics, errors ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. **Agent 11.12 should consolidate and expose the observability already produced by 11.6.x, 11.7/11.7.1, 11.8 and 11.9 — not create competing metrics, health, or connection systems.**

This is designed as a **single Cursor copy/paste prompt** and explicitly protects Phase 10 from observability coupling.

:::writing{variant="standard" id="58321"}
=========================================================
RACEVISION — AGENT 11.12
TRANSPORT OBSERVABILITY
=========================================================

OBJECTIVE
=========

Implement and/or consolidate Transport Observability for Phase 11.

Scope:

- transport metrics
- transport health
- connection statistics
- WebSocket statistics
- subscription statistics
- authentication/authorization statistics
- rate-limit statistics
- hardening/security errors
- streaming delivery statistics
- backpressure statistics
- transport errors
- operational status
- capability/status reporting

IMPORTANT:

This Agent MUST NOT create duplicate ownership for functionality
already implemented by Agents 11.6, 11.6.1, 11.6.2, 11.6.3, 11.7,
11.7.1, 11.8 or 11.9.

Agent 11.12 is an OBSERVABILITY AGGREGATION / EXPOSURE layer.

It does not become the owner of:

- authentication
- authorization
- rate limiting
- hardening
- live streaming
- replay streaming
- outbound backpressure
- subscriptions
- connection lifecycle
- Runtime
- EventBus
- ReplayClock

=========================================================
CURRENT AUTHORITATIVE OWNERSHIP
=========================================================

11.6
    Transport Authentication & Authorization

11.6.1
    Live Telemetry Streaming

11.6.2
    Inbound Rate Limiting & Abuse Protection

11.6.3
    Transport Hardening

11.7
    Replay Streaming

11.7.1
    Outbound Backpressure & Rate Control

11.8
    Subscription System

11.9
    Connection & Session Management

11.10
    SUPERSEDED / SATISFIED BY 11.7.1

11.11
    SUPERSEDED / SATISFIED BY 11.6

11.12
    Transport Observability ← THIS AGENT

11.13
    Transport Integration Testing

11.14
    Live Streaming Acceptance

11.15
    Phase 11 Acceptance

=========================================================
ARCHITECTURAL RULE
=========================================================

Observability is downstream of the transport components.

Preferred architecture:

                    PHASE 10 RUNTIME
                           │
                     EventBus / Cache
                           │
                 ┌─────────┴─────────┐
                 │                   │
                LIVE               REPLAY
                 │                   │
                 ▼                   ▼
           Stream Publishers   Replay Publisher
                 │                   │
                 └─────────┬─────────┘
                           │
                      TRANSPORT
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
       REST                WS             SECURITY
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                  EXISTING METRICS
                           │
                           ▼
                    AGENT 11.12
                  OBSERVABILITY
                           │
             ┌─────────────┼─────────────┐
             │             │             │
          Metrics        Health       Status
             │             │             │
             └─────────────┼─────────────┘
                           │
                  Operational API/UI

CRITICAL:

11.12 MUST NOT sit in the Runtime/EventBus hot path in a way that
can block telemetry, replay, or event delivery.

Metrics collection must be non-blocking or bounded.

A telemetry frame MUST NOT wait for metrics processing.

=========================================================
FIRST STEP — FULL AUDIT
=========================================================

Before changing code, inspect the repository.

Audit:

backend/api/
backend/runtime/
backend/services/
backend/config/
backend/streaming/

and existing:

- metrics
- health
- status
- capabilities
- logging
- middleware
- WebSocket manager
- WebSocket connection
- subscriptions
- security
- rate limiting
- hardening
- live streaming
- replay streaming
- outbound controller
- tests
- specifications
- roadmap

Specifically locate and understand existing:

- security metrics
- RateLimitMetrics
- LiveTelemetryStreamPublisher metrics
- ReplayStreamMetrics
- OutboundBackpressureMetrics
- subscription metrics
- connection metrics
- heartbeat metrics
- cleanup metrics
- existing health checks
- existing capability/status routes
- existing transport error counters

DO NOT recreate any metric that already exists.

=========================================================
PRIMARY REQUIREMENT
=========================================================

Create ONE coherent Transport Observability model that exposes
existing transport metrics consistently.

The model should make it possible to answer:

1. How many clients are connected?
2. How many clients are READY?
3. How many clients are DEGRADED?
4. How many clients are closing?
5. How many clients disconnected?
6. How many connections were rejected?
7. Why were connections rejected?
8. How many subscriptions exist?
9. Which subscription types are active?
10. How many telemetry subscribers exist?
11. How many replay subscribers exist?
12. How many events are being delivered?
13. How many messages are published?
14. How many messages are dropped?
15. How many messages are coalesced?
16. How many clients are rate limited?
17. How many authentication failures occurred?
18. How many authorization denials occurred?
19. How many malformed transport requests occurred?
20. How many WebSocket heartbeat failures occurred?
21. How many slow clients exist?
22. How many connections are under pressure?
23. How many connections reached CRITICAL pressure?
24. How many connections were disconnected because of pressure?
25. Are LIVE streams healthy?
26. Are REPLAY streams healthy?
27. Is the transport accepting connections?
28. Is the transport degraded?
29. Are there transport errors?
30. Is Phase 11 operationally healthy?

=========================================================
METRIC OWNERSHIP
=========================================================

Do NOT move metric ownership unnecessarily.

Existing component metrics remain owned by their components.

11.6
    owns security metrics

11.6.2
    owns rate-limit metrics

11.6.3
    owns hardening metrics/errors

11.6.1
    owns live-stream metrics

11.7
    owns replay-stream metrics

11.7.1
    owns outbound/backpressure metrics

11.8
    owns subscription metrics

11.9
    owns connection/session/heartbeat metrics

11.12
    aggregates/exposes transport-level observability

11.12 may provide a normalized read-only snapshot over those metrics.

=========================================================
NO DUPLICATE METRICS
=========================================================

Do NOT create:

SecondConnectionMetrics
SecondRateLimitMetrics
SecondSecurityMetrics
SecondSubscriptionMetrics
SecondBackpressureMetrics
SecondReplayMetrics
SecondTelemetryMetrics

unless the existing implementation genuinely lacks the required
transport-level information.

Prefer adapters/read-only aggregation.

=========================================================
METRIC CATEGORIES
=========================================================

Implement a coherent transport metrics snapshot containing, where
available:

CONNECTIONS
-----------

- total_connections
- active_connections
- connected_connections
- ready_connections
- degraded_connections
- closing_connections
- closed_connections
- rejected_connections
- reconnects
- authentication_rejections
- heartbeat_failures
- cleanup_count
- cleanup_idempotent_hits

SUBSCRIPTIONS
-------------

- total_subscriptions
- telemetry_subscriptions
- event_subscriptions
- snapshot_subscriptions
- replay_subscriptions
- mode_subscriptions
- runtime_status_subscriptions
- subscribe_attempts
- subscribe_successes
- subscribe_denials
- unsubscribe_count
- subscription_replacements

STREAMING
---------

- live_publish_count
- live_delivery_count
- live_drop_count
- replay_publish_count
- replay_delivery_count
- replay_drop_count
- event_publish_count
- snapshot_delivery_count

Where the underlying components already expose more accurate names,
preserve those names and normalize only at the aggregation boundary.

BACKPRESSURE
------------

Reuse Agent 11.7.1 metrics:

- pressure_normal
- pressure_elevated
- pressure_high
- pressure_critical
- messages_shed
- messages_coalesced
- slow_clients
- critical_disconnects
- rate_limited_connections
- bytes_shed where available

Do not duplicate the controller.

SECURITY
--------

Reuse Agent 11.6 metrics:

- authentication_attempts
- authentication_failures
- authorization_denials
- security_rejections

Do not expose credentials or sensitive identity information.

RATE LIMITING
-------------

Reuse Agent 11.6.2:

- rate_limit_hits
- rate_limit_denials
- REST limits
- WS connection limits
- inbound message limits
- subscription limits
- authentication abuse limits

HARDENING
---------

Reuse Agent 11.6.3:

- malformed envelope errors
- payload-size rejections
- invalid content-type rejections
- invalid session IDs
- invalid protocol messages
- invalid state transitions
- Origin rejections

CONNECTION / HEARTBEAT
----------------------

Reuse Agent 11.9:

- heartbeat_sent
- heartbeat_received
- heartbeat_timeouts
- reconnects
- forced_shutdowns
- cleanup metrics

=========================================================
COUNTERS / GAUGES / HISTOGRAMS
=========================================================

Use appropriate metric semantics.

COUNTERS:

- connection attempts
- accepted connections
- rejected connections
- authentication failures
- authorization failures
- subscription attempts
- subscription denials
- messages published
- messages dropped
- errors

GAUGES:

- active connections
- ready connections
- degraded connections
- active subscriptions
- queued messages
- queue bytes
- current slow clients
- current critical clients

HISTOGRAMS / LATENCY:

Where infrastructure already supports them, expose:

- connection establishment latency
- authentication latency
- authorization latency
- subscription latency
- enqueue/admission latency
- outbound send latency

Do not add expensive timing to the Runtime hot path.

=========================================================
HEALTH MODEL
=========================================================

Implement a transport health model.

At minimum distinguish:

HEALTHY
DEGRADED
UNHEALTHY

Health MUST be based on transport conditions.

Possible inputs:

HEALTHY:

- transport accepting connections
- no systemic connection failure
- heartbeat functioning
- error rate within configured limits
- Runtime transport integration available

DEGRADED:

- elevated connection failures
- elevated authorization failures
- widespread slow clients
- high outbound pressure
- repeated heartbeat failures
- elevated transport errors

UNHEALTHY:

- transport cannot accept connections
- transport manager unavailable
- critical transport dependency failure
- systematic inability to establish authenticated connections

Do not classify a single slow client as global transport unhealthy.

A single client being CRITICAL is a per-connection condition.

=========================================================
HEALTH CHECK OWNERSHIP
=========================================================

Audit existing health endpoints first.

Do not create a duplicate:

/health
/healthz
/readiness
/status

if they already exist.

Extend existing infrastructure where appropriate.

If a dedicated transport health endpoint is necessary, use a clear
existing API convention.

Potential information:

transport:
    status
    active_connections
    ready_connections
    active_subscriptions
    live_streaming
    replay_streaming
    backpressure
    heartbeat
    errors

Do not expose sensitive internal security information publicly.

=========================================================
CAPABILITIES / STATUS
=========================================================

Integrate with existing capability/status reporting.

Expose read-only operational capabilities such as:

transport_observability

and existing:

live_stream
replay_stream
subscription_system
connection_session_management
outbound_backpressure

Do not invent duplicate capability names.

=========================================================
CONNECTION STATISTICS
=========================================================

Expose aggregate connection information.

Required:

- total active connections
- READY
- DEGRADED
- CLOSING
- rejected
- reconnects
- heartbeat failures

Do NOT expose sensitive per-client data by default.

Do not expose:

- tokens
- passwords
- Authorization headers
- private credentials

Avoid unnecessary personal information.

=========================================================
PER-CONNECTION OBSERVABILITY
=========================================================

If existing metrics already identify connections, retain connection
ID internally.

Do not expose a public list of all connection IDs unless an existing
admin-only API explicitly requires it.

If administrative diagnostics are implemented:

- require authorization
- use existing 11.6 policy
- avoid credentials
- avoid payload data
- avoid sensitive principal information

=========================================================
ERROR OBSERVABILITY
=========================================================

Create a normalized transport error taxonomy.

At minimum distinguish:

AUTHENTICATION
AUTHORIZATION
RATE_LIMIT
HARDENING
PROTOCOL
VALIDATION
SUBSCRIPTION
CONNECTION
HEARTBEAT
OUTBOUND
INTERNAL

Do not leak implementation details to clients.

Observability may retain an internal error category while the
client-facing error remains sanitized.

=========================================================
ERROR RATE
=========================================================

Where practical, provide:

- error counts
- error categories
- recent error totals

Do NOT create unbounded in-memory error history.

Use bounded counters / rolling windows where needed.

Do not retain full payloads.

=========================================================
PERFORMANCE REQUIREMENT
=========================================================

Observability MUST NOT become a bottleneck.

Required invariant:

Telemetry delivery MUST NOT wait on metrics aggregation.

Replay delivery MUST NOT wait on metrics aggregation.

EventBus MUST NOT wait on metrics aggregation.

WebSocket enqueue MUST NOT wait on external metrics systems.

Do not perform blocking database writes per telemetry frame.

Do not perform network calls from the telemetry hot path.

Do not synchronously export every metric event to an external system.

=========================================================
THREAD / ASYNC SAFETY
=========================================================

Audit existing concurrency model.

Metrics must be safe under concurrent:

- WebSocket connections
- subscription changes
- telemetry publishing
- replay publishing
- disconnects
- heartbeat
- shutdown

Avoid global locks around the streaming hot path.

Use lightweight counters/snapshots appropriate to the existing
architecture.

=========================================================
BOUNDED MEMORY
=========================================================

Observability state MUST be bounded.

Do not store:

- every telemetry frame
- every transport message
- unlimited errors
- unlimited connection history
- unlimited subscription history

Use counters, gauges, bounded rolling windows, or bounded samples.

=========================================================
REST OBSERVABILITY
=========================================================

Audit REST transport metrics.

Where available track:

- request count
- response count
- authentication failures
- authorization failures
- rate-limit responses
- validation failures
- transport errors
- latency

Do not instrument every endpoint with duplicate custom middleware
if existing middleware already exposes the necessary information.

=========================================================
WEBSOCKET OBSERVABILITY
=========================================================

Audit:

WS /api/v1/ws

Track:

- connection attempts
- accepted connections
- rejected connections
- authenticated connections
- ready connections
- disconnects
- reconnects
- heartbeat failures
- messages received
- messages sent
- messages dropped
- subscription changes
- protocol errors

Ensure metrics remain separate from actual message delivery authority.

=========================================================
LIVE OBSERVABILITY
=========================================================

Use Agent 11.6.1 metrics.

Track:

- live subscribers
- telemetry published
- telemetry delivered
- events published
- events delivered
- dropped messages
- slow-client impact

Do not modify LiveSessionAdapter timing.

Do not add transport delay.

Do not add interpolation.

=========================================================
REPLAY OBSERVABILITY
=========================================================

Use Agent 11.7 metrics.

Track:

- replay subscribers
- replay frames published
- replay frames delivered
- replay events delivered
- replay drops
- replay delivery errors

Do not modify:

- ReplayClock
- seeking
- playback
- pause
- replay timing

Observability has no timing authority.

=========================================================
BACKPRESSURE OBSERVABILITY
=========================================================

Use Agent 11.7.1.

Expose:

- normal clients
- elevated clients
- high-pressure clients
- critical clients
- dropped/coalesced messages
- rate-limited delivery
- critical disconnects

Do not create another backpressure controller.

Do not change queue behavior.

Do not change priority behavior.

=========================================================
SUBSCRIPTION OBSERVABILITY
=========================================================

Use Agent 11.8.

Expose:

- active subscriptions
- subscriptions by type
- subscription attempts
- successful subscriptions
- rejected subscriptions
- replacements
- unsubscribes
- cleanup

Do not create another registry.

=========================================================
CONNECTION OBSERVABILITY
=========================================================

Use Agent 11.9.

Expose:

- active connections
- lifecycle states
- heartbeat health
- reconnect count
- cleanup
- shutdown
- forced closes

Do not create another connection manager.

=========================================================
SECURITY OBSERVABILITY
=========================================================

Use Agent 11.6.

Expose aggregate:

- authentication failures
- authorization denials
- protected operation denials

Do not expose:

- tokens
- credentials
- private claims
- secrets

Security remains fail-closed.

=========================================================
RATE LIMIT OBSERVABILITY
=========================================================

Use Agent 11.6.2.

Expose aggregate:

- rate-limit denials
- REST limits
- WS connect limits
- inbound message limits
- subscription limits
- authentication abuse limits

Do not expose internal token bucket state unless explicitly required
for an authorized admin diagnostic.

=========================================================
TRANSPORT STATUS SNAPSHOT
=========================================================

Create a read-only transport status snapshot.

Suggested structure:

transport:
    status
    uptime
    active_connections
    ready_connections
    degraded_connections
    active_subscriptions
    live_streaming
    replay_streaming

security:
    authentication_failures
    authorization_denials

rate_limit:
    denials

streaming:
    live
    replay

outbound:
    queue_pressure
    dropped
    coalesced
    slow_clients

heartbeat:
    healthy
    failures

errors:
    total
    by_category

Do not blindly use these exact field names if the existing API contract
already defines a canonical naming convention.

Preserve existing API conventions.

=========================================================
ADMIN / PUBLIC DATA SEPARATION
=========================================================

Transport observability may contain operational information that
should not be public.

Audit endpoint access.

Public clients should only receive intentionally public health/status.

Detailed operational metrics should use existing authorization.

Do not invent a new admin authentication system.

Use Agent 11.6.

=========================================================
METRIC CARDINALITY
=========================================================

Avoid high-cardinality labels.

DO NOT use unrestricted:

- session_id
- connection_id
- principal_id
- subscription_id

as metric labels if that would create unbounded cardinality.

Prefer bounded dimensions:

- stream type
- transport type
- error category
- lifecycle state
- pressure state
- subscription type
- outcome

Connection/session IDs may remain diagnostic fields where appropriate,
but MUST NOT become uncontrolled metric dimensions.

=========================================================
LOGGING
=========================================================

Use existing structured logging.

Transport observability logs should include bounded context such as:

- correlation ID
- operation
- transport
- error category
- lifecycle state

Do not log:

- credentials
- tokens
- passwords
- sensitive payloads

Avoid logging every telemetry frame.

=========================================================
CONFIGURATION
=========================================================

Audit configuration before adding settings.

Do not add unnecessary environment variables.

If observability configuration is required, validate:

- sampling rate
- rolling window
- retention
- metric enablement

Defaults MUST be safe.

Observability being enabled MUST NOT alter transport semantics.

=========================================================
TEST REQUIREMENTS
=========================================================

Create focused tests only where existing coverage does not already
prove the behavior.

Required verification:

1. connection counters
2. connection lifecycle metrics
3. heartbeat metrics
4. reconnect metrics
5. subscription metrics
6. live streaming metrics
7. replay streaming metrics
8. backpressure metrics
9. rate-limit metrics
10. authentication metrics
11. authorization metrics
12. hardening metrics
13. error categorization
14. health status
15. readiness behavior
16. capability/status exposure
17. bounded metric memory
18. bounded error state
19. concurrency safety
20. no blocking Runtime
21. no blocking EventBus
22. no blocking ReplayClock
23. no duplicate metric systems
24. no credential leakage
25. no secret leakage
26. no high-cardinality metric explosion
27. REST observability
28. WebSocket observability
29. LIVE/REPLAY isolation
30. session isolation
31. shutdown behavior
32. cleanup idempotency

=========================================================
CRITICAL INVARIANTS
=========================================================

INVARIANT 1
Observability is read-only with respect to Runtime behavior.

INVARIANT 2
Observability cannot delay telemetry delivery.

INVARIANT 3
Observability cannot delay replay delivery.

INVARIANT 4
Observability cannot block EventBus processing.

INVARIANT 5
Observability cannot change ReplayClock behavior.

INVARIANT 6
Observability cannot change authentication decisions.

INVARIANT 7
Observability cannot change authorization decisions.

INVARIANT 8
Observability cannot change rate-limit decisions.

INVARIANT 9
Observability cannot change subscription authorization.

INVARIANT 10
Observability cannot change connection lifecycle decisions.

INVARIANT 11
Observability cannot change outbound backpressure policy.

INVARIANT 12
Metrics state is bounded.

INVARIANT 13
Error state is bounded.

INVARIANT 14
Metric cardinality is bounded.

INVARIANT 15
Credentials are never logged.

INVARIANT 16
Secrets are never exposed.

INVARIANT 17
Public health information contains no sensitive operational data.

INVARIANT 18
Detailed observability remains protected by existing 11.6 authz.

INVARIANT 19
There is ONE transport observability aggregation layer.

INVARIANT 20
Phase 10 Runtime remains identity-unaware.

=========================================================
DO NOT IMPLEMENT
=========================================================

DO NOT create:

another metrics system
another health system
another connection manager
another subscription registry
another security system
another rate limiter
another backpressure controller
another telemetry publisher
another replay publisher
another Runtime metrics bus
another EventBus metrics pipeline
database writes per telemetry frame
network calls per telemetry frame
unbounded event history
unbounded error history
high-cardinality metrics
per-client metric labels without strict bounds

=========================================================
ACCEPTANCE GATES
=========================================================

GATE-01  Existing observability implementation audited
GATE-02  Existing component metrics audited
GATE-03  No duplicate metrics authority
GATE-04  Connection metrics verified
GATE-05  Session metrics verified
GATE-06  Subscription metrics verified
GATE-07  Live streaming metrics verified
GATE-08  Replay streaming metrics verified
GATE-09  Outbound metrics verified
GATE-10  Backpressure metrics verified
GATE-11  Rate-limit metrics verified
GATE-12  Authentication metrics verified
GATE-13  Authorization metrics verified
GATE-14  Hardening metrics verified
GATE-15  Heartbeat metrics verified
GATE-16  REST metrics verified
GATE-17  WebSocket metrics verified
GATE-18  Error taxonomy verified
GATE-19  Health model verified
GATE-20  Readiness behavior verified
GATE-21  Capability/status integration verified
GATE-22  Transport status snapshot verified
GATE-23  Public/private observability boundary verified
GATE-24  Metric cardinality bounded
GATE-25  Metric memory bounded
GATE-26  Error memory bounded
GATE-27  No credential leakage
GATE-28  No secret leakage
GATE-29  No Runtime blocking
GATE-30  No EventBus blocking
GATE-31  No ReplayClock blocking
GATE-32  No telemetry hot-path blocking
GATE-33  LIVE/REPLAY isolation verified
GATE-34  Session isolation verified
GATE-35  Connection cleanup metrics verified
GATE-36  Shutdown metrics verified
GATE-37  Concurrency tests pass
GATE-38  Existing API tests pass
GATE-39  Phase 10 tests pass
GATE-40  Phase 10 acceptance passes
GATE-41  Phase 11 regression tests pass
GATE-42  Ruff clean
GATE-43  mypy clean
GATE-44  Documentation updated
GATE-45  Roadmap updated
GATE-46  Capability documentation updated
GATE-47  Transport observability specification updated
GATE-48  No duplicate health endpoints
GATE-49  No duplicate connection statistics
GATE-50  No duplicate error system

=========================================================
BENCHMARKING
=========================================================

Do NOT claim production SLA from microbenchmarks.

If benchmarks are added, label them:

BASELINE_NOT_PRODUCTION_SLA

At minimum, if practical, verify that observability collection has
negligible impact on:

- telemetry publish
- EventBus dispatch
- WebSocket enqueue

Do not benchmark by modifying Runtime behavior.

=========================================================
DOCUMENTATION
=========================================================

Create or update:

docs/specifications/TransportObservabilitySpecification.md

Update:

- docs/Roadmap.md
- Architecture documentation
- Streaming documentation
- API documentation
- specification index
- backend/api/README.md

Document ownership clearly.

Agent 11.12 is the observability aggregation/exposure layer.

It does not own the underlying transport functionality.

=========================================================
FINAL REPORT
=========================================================

At completion report:

1. STATUS
2. Initial audit findings
3. Existing metrics discovered
4. Metrics retained
5. Metrics newly added
6. Aggregation architecture
7. Connection statistics
8. Subscription statistics
9. LIVE streaming statistics
10. REPLAY streaming statistics
11. Backpressure statistics
12. Rate-limit statistics
13. Security statistics
14. Hardening statistics
15. Heartbeat statistics
16. Error taxonomy
17. Health model
18. Readiness behavior
19. Capability/status integration
20. Transport status snapshot
21. Public/private observability boundary
22. Metric cardinality controls
23. Bounded-memory controls
24. Runtime non-blocking verification
25. EventBus non-blocking verification
26. ReplayClock non-blocking verification
27. Credential/secret audit
28. Files created
29. Files modified
30. Exact test results
31. Ruff result
32. mypy result
33. Benchmark result
34. GATE-01…50 results
35. Limitations
36. Remaining risks
37. Roadmap status

=========================================================
SUCCESS CONDITION
=========================================================

Agent 11.12 is ACCEPTED only when:

- transport health is observable
- connections are observable
- subscriptions are observable
- LIVE streaming is observable
- REPLAY streaming is observable
- security outcomes are observable
- rate-limit outcomes are observable
- backpressure is observable
- errors are categorized
- metrics are bounded
- sensitive information is protected
- observability cannot block Runtime
- observability cannot block EventBus
- observability cannot block ReplayClock
- no duplicate subsystem ownership exists
- Phase 10 regression remains green
- Phase 11 regression remains green
- Ruff is clean
- mypy is clean

START NOW.

FIRST perform the repository audit.

DO NOT implement until existing metrics, health, status,
capabilities, and ownership have been identified.

THEN implement only the minimum missing observability capability.

PRESERVE ALL ACCEPTED PHASE 10 AND PHASE 11 CONTRACTS.
=========================================================
:::

## User

## AGENT 11.12 — ACCEPTED

Transport Observability is a **read-only aggregation layer** over existing component metrics. No duplicate metric owners, no hot-path Runtime/EventBus/ReplayClock coupling.

### 1. STATUS

**ACCEPTED**

### 2–5. Audit / metrics

**Existing owners retained:** GatewayMetrics (11.9), SecurityMetrics (11.6), RateLimitMetrics (11.6.2), live/replay/snapshot metrics (11.6.1/11.7/11.5), OutboundBackpressureMetrics (11.7.1), TransportSubscriptionMetrics (11.8).

**Gap filled:** coherent snapshot + health + `/runtime/transport` + `transport_observability` capability.

**Newly added:** aggregation only (`build_transport_observability`, health class, error rollup) — no `Second*Metrics`.

### 6. Architecture

`app.state` component metrics → `backend/api/observability/` → `GET /api/v1/runtime/transport` (`RUNTIME_READ`) + coarse transport state on existing `/health`.

### 7–15. Snapshot sections

Connections, subscriptions, live/replay/snapshot streaming, outbound pressure, rate-limit, security, heartbeat, commands, bounded error taxonomy (AUTH…INTERNAL).

### 16–20. Health / readiness / capabilities / snapshot

HEALTHY / DEGRADED / UNHEALTHY (single CRITICAL ≠ UNHEALTHY). Capabilities: `transport_observability: true`, op `runtime.transport`.

### 21–28. Boundary / safety

Public `/health` = coarse state only. Detailed counters require `RUNTIME_READ`. Bounded counters; no connection/session IDs as metric labels; no credentials/secrets; aggregation is sync/read-only (no await, no DB/network on publish path).

### 28–29. Files

**Created:** `backend/api/observability/*`, `tests/api/observability/*`, `docs/specifications/TransportObservabilitySpecification.md`

**Modified:** runtime/health routes, services, transport contracts, Roadmap/Architecture/Streaming/READMEs/specs index.

### 30–33. Verification

| Check                            | Result                                           |
| -------------------------------- | ------------------------------------------------ |
| pytest `tests/api` + Phase 10    | **340 passed**                                   |
| ruff                             | clean                                            |
| mypy (`--follow-imports=silent`) | clean                                            |
| Benchmark                        | not claimed (BASELINE\_NOT\_PRODUCTION\_SLA N/A) |

### 34. GATE-01…50

All applicable gates **PASS** (aggregation-only scope; no duplicate health/metrics/error systems; docs/roadmap updated).

### 35–36. Limitations / risks

Hardening (11.6.3) still has no dedicated counters (taxonomy slot reserved). `/runtime/snapshot/stream` remains a partial legacy kitchen-sink; canonical surface is `/runtime/transport`.

### 37. Roadmap

**11.12 ✓** — next recommended: **11.13 Transport Integration Testing**.

## Assistant

Excellent. **Agent 11.12 is correctly ACCEPTED.** The implementation also preserves the architecture we've established: observability aggregates existing owners rather than introducing another metrics subsystem.

### Phase 11 status now

| Agent | Component | Status |
|---|---|---|
| 11.6 | Transport Authentication & Authorization | ✅ ACCEPTED |
| 11.6.1 | Live Telemetry Streaming | ✅ ACCEPTED |
| 11.6.2 | Rate Limiting & Abuse Protection | ✅ ACCEPTED |
| 11.6.3 | Transport Hardening | ✅ ACCEPTED |
| 11.7 | Replay Streaming | ✅ ACCEPTED |
| 11.7.1 | Outbound Backpressure & Rate Control | ✅ ACCEPTED |
| 11.8 | Subscription System | ✅ ACCEPTED |
| 11.9 | Connection & Session Management | ✅ ACCEPTED |
| 11.10 | Backpressure & Rate Control | 🔒 SUPERSEDED by 11.7.1 |
| 11.11 | Transport Authentication & Authorization | 🔒 SUPERSEDED by 11.6 |
| **11.12** | **Transport Observability** | **✅ ACCEPTED** |
| **11.13** | **Transport Integration Testing** | **⏳ NEXT** |
| 11.14 | Live Streaming Acceptance | ⏳ |
| 11.15 | Phase 11 Acceptance | ⏳ |

### Important 11.12 result

The canonical operational surface is now:

```text
GET /api/v1/runtime/transport
```

with detailed information protected by:

```text
RUNTIME_READ
```

while `/health` remains deliberately coarse.

The ownership chain is now clean:

```text
11.6       → Auth/AuthZ
11.6.2     → Inbound abuse/rate limiting
11.6.3     → Transport hardening
11.6.1     → LIVE streaming
11.7       → REPLAY streaming
11.7.1     → Outbound backpressure/rate control
11.8       → Subscriptions
11.9       → Connections/heartbeat
11.12      → Observability aggregation
11.13      → Integration verification
11.14      → Live streaming acceptance
11.15      → Phase 11 final acceptance
```

One minor known gap is already correctly documented: **11.6.3 hardening has no dedicated counters yet**, with the taxonomy slot reserved. That should **not** cause us to create another subsystem unless 11.13 testing demonstrates a real need.

**Next: Agent 11.13 — Transport Integration Testing.**

## User

Please give commands for Agent 11.13	Transport Integration Testing	End-to-end REST/WS tests against Phase 10 ( 1 click copy and paste cursor friendly)

## Assistant

Yes. **Agent 11.13 should be a verification/integration agent, not another runtime implementation agent.** It should test the complete Phase 10 → Phase 11 transport path, including REST, WebSocket, LIVE, REPLAY, auth, subscriptions, backpressure, lifecycle, and observability.

Here is the **single-click Cursor-ready prompt**:

:::writing{variant="standard" id="74163"}
=========================================================
RACEVISION — AGENT 11.13
TRANSPORT INTEGRATION TESTING
=========================================================

OBJECTIVE
=========

Implement comprehensive end-to-end Transport Integration Testing for
Phase 11 against the existing Phase 10 Unified Runtime.

This Agent is TESTING / VERIFICATION ONLY.

Do NOT create a second Runtime.
Do NOT create a second EventBus.
Do NOT create a second WebSocket gateway.
Do NOT create duplicate authentication.
Do NOT create duplicate authorization.
Do NOT create duplicate rate limiting.
Do NOT create duplicate hardening.
Do NOT create duplicate streaming publishers.
Do NOT create duplicate subscription systems.
Do NOT create duplicate connection management.
Do NOT create duplicate backpressure.
Do NOT create duplicate observability.

The purpose of Agent 11.13 is to prove that the accepted Phase 10 and
Phase 11 components work together correctly through the actual REST/WS
transport boundary.

=========================================================
CURRENT AUTHORITATIVE ARCHITECTURE
=========================================================

PHASE 10
--------

Unified Runtime authorities:

- CacheManager
- TimelineService
- EventBus
- LiveRuntime
- SessionOperatingMode / TimelineMode
- LiveSessionAdapter
- Replay Runtime
- ReplayClock
- RaceStateSnapshotEngine

Runtime remains:

- identity-unaware
- transport-unaware
- non-authenticated
- non-authorized

=========================================================

PHASE 11
--------

11.6
    Transport Authentication & Authorization

11.6.1
    Live Telemetry Streaming

11.6.2
    Rate Limiting & Abuse Protection

11.6.3
    Transport Hardening

11.7
    Replay Streaming

11.7.1
    Outbound Backpressure & Rate Control

11.8
    Subscription System

11.9
    Connection & Session Management

11.10
    SUPERSEDED / SATISFIED BY 11.7.1

11.11
    SUPERSEDED / SATISFIED BY 11.6

11.12
    Transport Observability

11.13
    Transport Integration Testing ← THIS AGENT

11.14
    Live Streaming Acceptance

11.15
    Phase 11 Acceptance

=========================================================
PRIMARY TEST OBJECTIVE
=========================================================

Prove this complete path:

Client
  ↓
REST / WebSocket Transport
  ↓
Hardening
  ↓
Rate Limiting
  ↓
Authentication
  ↓
Authorization
  ↓
Connection Manager
  ↓
Subscription Registry
  ↓
Stream Publisher
  ↓
Outbound Delivery Controller
  ↓
Bounded WebSocket Queue
  ↓
Client

and:

Stream Publisher
  ↓
Phase 10 Runtime / EventBus
  ↓
Canonical LIVE or REPLAY output
  ↓
Transport
  ↓
Client

The tests MUST verify that transport behavior does not alter Phase 10
Runtime semantics.

=========================================================
FIRST STEP — AUDIT
=========================================================

Before writing tests, inspect:

tests/api/
tests/runtime/
tests/integration/
tests/acceptance/

and existing tests for:

- security
- authentication
- authorization
- hardening
- rate limiting
- WebSocket
- telemetry
- replay
- subscriptions
- connection lifecycle
- outbound backpressure
- observability
- snapshots
- commands
- Phase 10 acceptance

Determine what is already covered.

Do NOT duplicate existing tests unnecessarily.

Create integration tests for actual gaps between components.

=========================================================
TEST ENVIRONMENT
=========================================================

Use the existing project test framework and fixtures.

Prefer:

- pytest
- pytest-asyncio
- existing FastAPI/ASGI test infrastructure
- existing WebSocket test client
- existing Phase 10 fixtures
- existing Runtime factories
- existing authentication fixtures
- existing database fixtures where genuinely required

Do NOT introduce a second application factory.

Do NOT create a fake Runtime that bypasses Phase 10 unless a narrowly
scoped unit test explicitly requires it.

Integration tests MUST exercise the real application wiring.

=========================================================
PHASE 10 INTEGRATION
=========================================================

Verify transport receives data from the real Phase 10 Runtime.

LIVE:

LiveProvider
→ LiveSessionAdapter
→ Cache / Timeline
→ EventBus
→ LiveTelemetryStreamPublisher
→ WebSocket
→ client

REPLAY:

Replay Runtime
→ ReplayClock
→ apply_sample
→ EventBus
→ ReplayStreamPublisher
→ WebSocket
→ client

Verify that transport does not become the source of telemetry.

=========================================================
REST TESTING
=========================================================

Test existing REST API transport paths.

At minimum verify:

1. unauthenticated request
2. authenticated request
3. unauthorized request
4. malformed request
5. invalid UUID session ID
6. valid UUID session ID
7. invalid content type
8. oversized request
9. rate-limited request
10. health request
11. runtime transport status
12. capabilities/status
13. command endpoint where applicable
14. snapshot endpoint
15. correct HTTP status codes
16. sanitized error payloads
17. correlation/request IDs
18. security headers where applicable

Do not create new endpoints merely for testing.

=========================================================
WEBSOCKET HANDSHAKE TESTING
=========================================================

Test:

1. connection attempt
2. unauthenticated connection
3. invalid credentials
4. authorized connection
5. unauthorized connection
6. Origin handling
7. rate-limit rejection
8. hardening rejection
9. successful connection
10. lifecycle CONNECTING → CONNECTED → READY
11. invalid handshake state
12. reconnect

Verify authentication happens before accepted authenticated streaming.

Verify rejected clients do not gain Runtime access.

=========================================================
WEBSOCKET LIFECYCLE
=========================================================

Verify:

CONNECTING
    ↓
CONNECTED
    ↓
READY
    ↓
DEGRADED
    ↓
CLOSING
    ↓
CLOSED

Not every test must force every state.

Verify valid transitions and invalid transitions.

Verify cleanup is idempotent.

Verify cleanup of an old connection cannot remove a newer connection.

Verify:

connection_id
≠
session_id
≠
subscription_id

=========================================================
HEARTBEAT TESTING
=========================================================

Use existing 11.9 heartbeat implementation.

Test:

- heartbeat enabled
- ping/pong
- heartbeat timeout
- connection close after timeout
- metrics update
- cleanup
- reconnect

Do not modify ReplayClock or EventBus for heartbeat.

Do not use application inactivity as a reason to disconnect streaming
clients.

=========================================================
AUTHENTICATION / AUTHORIZATION
=========================================================

Verify existing 11.6 behavior.

Test:

- valid principal
- invalid principal
- expired/invalid credential where supported
- missing credential
- LIVE read permission
- REPLAY read permission
- subscription permission
- command permission
- runtime read permission

Important:

Authentication != authorization.

Verify unauthorized clients cannot subscribe to protected streams.

Verify permissions are re-evaluated on relevant transport operations.

Verify reconnect requires authentication again.

Do not bypass 11.6 inside tests.

=========================================================
LIVE TELEMETRY E2E
=========================================================

Create an end-to-end test:

1. Start application using existing fixtures.
2. Start/create a Phase 10 LIVE session.
3. Authenticate a WS client.
4. Subscribe to TELEMETRY.
5. Subscribe to EVENTS if supported.
6. Inject/advance canonical Phase 10 LIVE telemetry using the existing
   runtime/test adapter.
7. Wait for transport delivery.
8. Receive the WebSocket envelope.
9. Validate envelope structure.
10. Validate payload type.
11. Validate session_id.
12. Validate operating_mode = LIVE.
13. Validate source sequence.
14. Validate transport sequence semantics.
15. Validate metadata preservation.
16. Confirm the frame originated from canonical Runtime/EventBus output.

Do NOT fabricate a second telemetry path.

=========================================================
LIVE EVENT E2E
=========================================================

Verify:

Phase 10 EventBus domain event
→ Live stream publisher
→ subscription
→ WebSocket
→ client

Verify no event synthesis occurs in transport.

Verify session isolation.

Verify unauthorized clients receive nothing.

=========================================================
SNAPSHOT E2E
=========================================================

Verify:

Phase 10 RaceStateSnapshotEngine
→ existing snapshot service
→ WS snapshot subscription
→ client

Verify:

- session_id
- snapshot structure
- operating mode
- source semantics
- transport envelope
- authorization
- subscription lifecycle

Do not create another snapshot engine.

=========================================================
REPLAY E2E
=========================================================

Create a true REPLAY integration test.

1. Establish replay session.
2. Set ModeController to REPLAY.
3. Authenticate client.
4. Subscribe to REPLAY / TELEMETRY / EVENTS as permitted.
5. Advance ReplayClock using existing Phase 10 controls.
6. Verify replay frame reaches client.
7. Verify event reaches client.
8. Verify operating_mode = REPLAY.
9. Verify session isolation.
10. Verify LIVE subscription does not receive replay frames.
11. Verify replay subscription does not receive unrelated LIVE frames.

=========================================================
REPLAY CLOCK INVARIANT
=========================================================

Transport MUST NOT become the timing authority.

Tests MUST verify that:

- playback timing comes from ReplayClock
- transport does not seek
- transport does not pause
- transport does not interpolate
- transport does not extrapolate
- transport does not add delay
- transport does not reorder frames

=========================================================
SEQUENCE TESTING
=========================================================

Verify distinction between:

transport sequence
and
source sequence.

Transport MUST NOT overwrite canonical source sequence.

Verify:

- source sequence remains intact
- transport sequence is transport-owned
- source ordering is preserved
- no transport-side reordering occurs

Do not assume numerical equality between the two sequences.

=========================================================
SESSION ISOLATION
=========================================================

This is a mandatory integration requirement.

Create at least two sessions:

SESSION A
SESSION B

Create clients/subscriptions for both.

Verify:

Client A receives only A.

Client B receives only B.

Verify:

- telemetry isolation
- event isolation
- snapshot isolation
- replay isolation
- command/session isolation where applicable

Test:

A subscription cannot accidentally receive B.

B subscription cannot accidentally receive A.

=========================================================
SUBSCRIPTION E2E
=========================================================

Use Agent 11.8.

Test:

- subscribe
- unsubscribe
- replace
- duplicate subscription
- invalid filter
- invalid session ID
- unauthorized subscription
- subscription quota
- session quota
- cleanup
- reconnect/resubscribe

Verify:

subscription_id
is unique and independent from:

connection_id
session_id

Reconnect MUST require resubscription.

No durable resume is expected.

=========================================================
RATE LIMITING E2E
=========================================================

Use Agent 11.6.2.

Test:

- REST request limit
- WS connection limit
- inbound message limit
- subscribe churn limit
- auth abuse limit
- principal concurrent limits

Verify:

- correct rejection
- correct transport error
- Retry-After where applicable
- no Runtime impact
- metrics updated

Do not test by disabling the real limiter and replacing it with a fake
implementation unless an existing fixture specifically supports that.

=========================================================
TRANSPORT HARDENING E2E
=========================================================

Use Agent 11.6.3.

Test:

- invalid content type
- oversized body
- malformed WS envelope
- unsupported schema major
- invalid nested JSON
- invalid UUID
- invalid client sequence
- invalid lifecycle state
- invalid protocol message
- Origin rejection where configured

Verify client errors are sanitized.

No stack traces.

No filesystem paths.

No secrets.

No credentials.

=========================================================
OUTBOUND BACKPRESSURE E2E
=========================================================

Use Agent 11.7.1.

Create at least:

CLIENT A
slow client

CLIENT B
normal client

Publish sufficient telemetry/events to place A under pressure.

Verify:

- A becomes pressured
- A is bounded
- A may shed/coalesce according to configured policy
- B continues receiving
- Runtime remains non-blocking
- EventBus remains non-blocking
- ReplayClock remains unaffected

Do NOT create another backpressure system.

=========================================================
CONTROL / EVENT PRIORITY
=========================================================

Verify existing policy:

CONTROL > EVENT > SNAPSHOT > TELEMETRY

Do not require FIFO reordering if the existing architecture explicitly
uses FIFO dequeue.

Verify admission/drop protection instead.

=========================================================
DROP / COALESCE TESTING
=========================================================

Verify under pressure:

- canonical payload is not mutated
- source sequence is not rewritten
- coalescing is transport-only
- Runtime data remains authoritative
- normal clients are unaffected

=========================================================
RECONNECT TESTING
=========================================================

Test:

1. client connects
2. authenticates
3. subscribes
4. receives telemetry
5. disconnects
6. reconnects
7. receives a new connection_id
8. re-authenticates
9. resubscribes
10. receives new telemetry

Verify:

- old connection cleanup does not remove new connection
- no durable missed-frame replay occurs
- no stale subscription survives unexpectedly
- session isolation remains correct

=========================================================
NO MISSED-FRAME RESUME
=========================================================

The current contract is:

Reconnect → authenticate → resubscribe.

There is NO durable resume.

Do not implement resume during this Agent.

Tests should explicitly document that missed frames are not replayed
automatically.

=========================================================
OBSERVABILITY E2E
=========================================================

Use Agent 11.12.

Verify:

GET /api/v1/runtime/transport

reports coherent aggregate state after integration activity.

Test that:

- connection count changes
- subscription count changes
- streaming counters change
- security counters change
- rate-limit counters change
- backpressure counters change
- heartbeat counters change
- errors are categorized

Verify:

/health

remains coarse.

Verify detailed transport observability requires the existing
RUNTIME_READ authorization.

=========================================================
CAPABILITY TESTING
=========================================================

Verify existing capability/status reporting exposes:

transport_observability
live_stream
replay_stream
subscription_system
connection_session_management
outbound_backpressure

Do not invent duplicate capability names.

=========================================================
ERROR CONTRACT TESTING
=========================================================

Verify stable transport errors.

Test categories:

AUTHENTICATION
AUTHORIZATION
RATE_LIMIT
HARDENING
PROTOCOL
VALIDATION
SUBSCRIPTION
CONNECTION
HEARTBEAT
OUTBOUND
INTERNAL

Verify errors contain no:

- secrets
- credentials
- stack traces
- local paths
- sensitive payloads

=========================================================
LIVE / REPLAY CROSS-CONTAMINATION
=========================================================

This is a mandatory test group.

Test:

LIVE client
REPLAY client

Publish LIVE data.

Verify:

LIVE client receives it.

REPLAY client does not.

Advance REPLAY.

Verify:

REPLAY client receives it.

LIVE client does not.

Test events and snapshots where applicable.

=========================================================
MULTI-CLIENT CONCURRENCY
=========================================================

Test at minimum:

- 2 clients
- 5 clients
- 10 clients if test infrastructure allows

Verify:

- no cross-session delivery
- no subscription corruption
- no lifecycle corruption
- no connection cleanup races
- no duplicate deliveries caused by registry corruption

Do not claim production concurrency limits from these tests.

=========================================================
SHUTDOWN TESTING
=========================================================

Verify bounded shutdown.

Test:

- active connections
- active subscriptions
- streaming
- heartbeat
- pending outbound queues

Shutdown MUST:

- stop accepting new work
- close connections
- clean subscriptions
- avoid Runtime corruption
- complete within configured shutdown bound where applicable

=========================================================
DATABASE TESTING
=========================================================

Do NOT write one database row per telemetry frame as part of transport
integration.

If database fixtures are needed, use the existing persistence layer.

Transport tests must not accidentally introduce a second persistence
path.

=========================================================
NO EXTERNAL SERVICES
=========================================================

Integration tests should be deterministic and local.

Do not require:

- real F1 provider
- real Twitch
- real Kick
- real YouTube
- real OBS
- external authentication provider
- external Redis
- external metrics service

unless the existing repository explicitly requires such a service
for a test already accepted.

Use existing test adapters and fixtures.

=========================================================
TEST ORGANIZATION
=========================================================

Prefer a dedicated suite such as:

tests/integration/transport/

or the repository's existing integration-test convention.

Possible files:

test_rest_transport_e2e.py
test_ws_transport_e2e.py
test_live_stream_e2e.py
test_replay_stream_e2e.py
test_subscription_e2e.py
test_auth_e2e.py
test_rate_limit_e2e.py
test_hardening_e2e.py
test_backpressure_e2e.py
test_connection_e2e.py
test_observability_e2e.py
test_session_isolation_e2e.py
test_shutdown_e2e.py

Do not create files unnecessarily if equivalent existing suites are
already present.

=========================================================
TEST DETERMINISM
=========================================================

Tests MUST avoid:

- arbitrary sleeps where possible
- real wall-clock race assumptions
- uncontrolled background tasks
- random session IDs without reproducibility
- real network dependencies

Prefer:

- explicit events
- async conditions
- deterministic fixtures
- bounded timeouts
- controlled clocks where existing infrastructure provides them

=========================================================
TIMEOUTS
=========================================================

All integration waits MUST be bounded.

No infinite waits.

Failure messages must identify:

- client
- session
- operation
- expected state
- actual state

Do not leak secrets in failure output.

=========================================================
REGRESSION REQUIREMENT
=========================================================

Run existing:

tests/api

Phase 10 tests

Phase 10 acceptance

Phase 11 security tests

Phase 11 telemetry tests

Phase 11 replay tests

Phase 11 outbound tests

Phase 11 subscription tests

Phase 11 connection tests

Phase 11 observability tests

and the new integration suite.

Do not weaken or skip previous tests to make the new suite pass.

=========================================================
CRITICAL INVARIANTS
=========================================================

INVARIANT 1
Phase 10 remains authoritative for Runtime state.

INVARIANT 2
Transport does not create telemetry.

INVARIANT 3
Transport does not alter telemetry.

INVARIANT 4
Transport does not add timing authority.

INVARIANT 5
ReplayClock remains authoritative for replay timing.

INVARIANT 6
Runtime remains identity-unaware.

INVARIANT 7
Authentication occurs through 11.6.

INVARIANT 8
Rate limiting occurs through 11.6.2.

INVARIANT 9
Hardening occurs through 11.6.3.

INVARIANT 10
Live streaming occurs through 11.6.1.

INVARIANT 11
Replay streaming occurs through 11.7.

INVARIANT 12
Outbound protection occurs through 11.7.1.

INVARIANT 13
Subscriptions occur through 11.8.

INVARIANT 14
Connections occur through 11.9.

INVARIANT 15
Observability occurs through 11.12.

INVARIANT 16
No duplicate transport subsystem is introduced.

INVARIANT 17
Session isolation is absolute.

INVARIANT 18
LIVE and REPLAY cannot cross-contaminate.

INVARIANT 19
A slow client cannot block another client.

INVARIANT 20
A slow client cannot block Runtime.

INVARIANT 21
A slow client cannot block EventBus.

INVARIANT 22
A slow client cannot block ReplayClock.

INVARIANT 23
Reconnect requires authentication and resubscription.

INVARIANT 24
No durable missed-frame resume exists.

INVARIANT 25
Source sequences remain canonical.

INVARIANT 26
Transport sequences remain transport-owned.

INVARIANT 27
No credentials or secrets leak through errors/logs/tests.

INVARIANT 28
No test bypasses the production transport ownership model.

=========================================================
ACCEPTANCE GATES
=========================================================

GATE-01  Repository integration-test audit
GATE-02  Existing API tests audited
GATE-03  Existing Phase 10 tests audited
GATE-04  Existing Phase 11 tests audited
GATE-05  Real application wiring exercised
GATE-06  REST authentication E2E
GATE-07  REST authorization E2E
GATE-08  REST hardening E2E
GATE-09  REST rate limiting E2E
GATE-10  REST status/health E2E
GATE-11  WS authentication E2E
GATE-12  WS authorization E2E
GATE-13  WS hardening E2E
GATE-14  WS rate limiting E2E
GATE-15  WS lifecycle E2E
GATE-16  WS heartbeat E2E
GATE-17  LIVE telemetry E2E
GATE-18  LIVE events E2E
GATE-19  LIVE snapshots E2E
GATE-20  REPLAY telemetry E2E
GATE-21  REPLAY events E2E
GATE-22  REPLAY snapshots E2E
GATE-23  LIVE/REPLAY isolation
GATE-24  Session isolation
GATE-25  Subscription lifecycle
GATE-26  Subscription replacement
GATE-27  Subscription quotas
GATE-28  Reconnect/resubscribe
GATE-29  No durable resume verified
GATE-30  Sequence semantics
GATE-31  Metadata preservation
GATE-32  Outbound backpressure
GATE-33  Slow-client isolation
GATE-34  Peer-client protection
GATE-35  Drop/coalesce behavior
GATE-36  Control/event protection
GATE-37  Observability integration
GATE-38  Transport health integration
GATE-39  Capability/status integration
GATE-40  Error contract integration
GATE-41  Sanitized errors
GATE-42  Credential/secret protection
GATE-43  Multi-client concurrency
GATE-44  Shutdown behavior
GATE-45  Cleanup idempotency
GATE-46  No Runtime blocking
GATE-47  No EventBus blocking
GATE-48  No ReplayClock blocking
GATE-49  No transport timing authority
GATE-50  No duplicate subsystem
GATE-51  Database boundary preserved
GATE-52  No external service dependency
GATE-53  Deterministic tests
GATE-54  Bounded test timeouts
GATE-55  Existing API regression
GATE-56  Phase 10 regression
GATE-57  Phase 10 acceptance
GATE-58  Phase 11 regression
GATE-59  Ruff clean
GATE-60  mypy clean
GATE-61  Documentation updated
GATE-62  Roadmap updated
GATE-63  Integration specification updated
GATE-64  Final end-to-end transport path verified

=========================================================
PERFORMANCE / LOAD TESTING
=========================================================

Do not claim production SLA from integration tests.

If a small concurrency test is added, label it:

BASELINE_NOT_PRODUCTION_SLA

The purpose is correctness, not production capacity certification.

Verify at minimum that slow-client tests demonstrate:

slow client
≠
Runtime blocking

slow client
≠
peer-client blocking

=========================================================
DOCUMENTATION
=========================================================

Create:

docs/specifications/TransportIntegrationTestingSpecification.md

Update:

docs/Roadmap.md
Architecture documentation
Streaming documentation
API documentation
specification index
backend/api/README.md

Document:

- integration scope
- test architecture
- fixtures
- E2E flows
- ownership
- isolation guarantees
- known limitations
- non-production-SLA nature of concurrency tests

=========================================================
FINAL REPORT
=========================================================

At completion report exactly:

1. STATUS
2. Initial audit findings
3. Existing tests retained
4. New integration tests
5. REST E2E results
6. WebSocket E2E results
7. Authentication results
8. Authorization results
9. Hardening results
10. Rate-limit results
11. Connection/heartbeat results
12. LIVE telemetry results
13. LIVE event results
14. Snapshot results
15. REPLAY telemetry results
16. REPLAY event results
17. LIVE/REPLAY isolation results
18. Subscription results
19. Session isolation results
20. Reconnect results
21. Sequence results
22. Metadata results
23. Backpressure results
24. Slow-client isolation results
25. Observability results
26. Health/readiness results
27. Error contract results
28. Security/secret audit
29. Shutdown results
30. Files created
31. Files modified
32. Exact test results
33. Full regression results
34. Ruff result
35. mypy result
36. Benchmark result
37. GATE-01…64 results
38. Limitations
39. Remaining risks
40. Roadmap status
41. Recommended next Agent

=========================================================
SUCCESS CONDITION
=========================================================

Agent 11.13 is ACCEPTED only when the tests prove:

REST works against the real application.

WebSocket works against the real application.

Authenticated transport works.

Unauthorized access is rejected.

LIVE telemetry reaches the correct client.

LIVE events reach the correct client.

REPLAY telemetry reaches the correct client.

REPLAY events reach the correct client.

Snapshots reach the correct client.

LIVE and REPLAY cannot cross-contaminate.

Sessions remain isolated.

Subscriptions remain isolated.

Reconnect requires re-authentication and resubscription.

Slow clients cannot block peers.

Slow clients cannot block Phase 10 Runtime.

Backpressure remains transport-only.

Observability reflects actual transport state.

Errors remain sanitized.

Credentials and secrets remain protected.

Phase 10 remains unchanged and authoritative.

No duplicate subsystem has been introduced.

Existing Phase 10 acceptance remains green.

Existing Phase 11 tests remain green.

Ruff is clean.

mypy is clean.

START NOW.

FIRST audit existing integration and acceptance tests.

THEN implement only missing end-to-end coverage.

DO NOT change accepted Runtime or transport contracts merely to make
tests pass.

PRESERVE ALL ACCEPTED PHASE 10 AND PHASE 11 CONTRACTS.
=========================================================
:::

## User

## AGENT 11.13 — ACCEPTED

Verification-only golden suite under `tests/integration/transport/` exercising real `create_app` + Phase10Harness EventBus→WS paths. No duplicate transport subsystems.

### 1. STATUS

**ACCEPTED**

### 2. Audit findings

`tests/api/*` are strong **component** proofs (mostly `offer_bus_event`). Phase 10 acceptance is runtime-only. `tests/integration/` was a placeholder — missing multi-component EventBus→bridge→WS and stacked gate journeys.

### 3–4. Tests retained / new

**Retained:** all existing API + Phase 10 suites.
**New (22 tests):** REST gate stack, LIVE E2E, REPLAY E2E, mode/session isolation, outbound peer, observability-after-activity, shutdown, multi-client concurrency.

### 5–29. Results (abbreviated)

| Area                                                  | Result                               |
| ----------------------------------------------------- | ------------------------------------ |
| REST auth/authz/hardening/RL/health/transport         | Pass                                 |
| WS LIVE from `accept_frame` → EventBus → bridge       | Pass (`live_session_adapter`)        |
| WS REPLAY from ReplayClock `tick` (fixture-wired bus) | Pass (`replay_runtime`)              |
| LIVE/REPLAY provenance isolation                      | Pass                                 |
| Session isolation (A vs B)                            | Pass                                 |
| Reconnect requires resubscribe / no durable resume    | Pass                                 |
| Slow client ≠ peer/Runtime block                      | Pass (`BASELINE_NOT_PRODUCTION_SLA`) |
| Observability after activity + coarse `/health`       | Pass                                 |
| Shutdown stops accepting                              | Pass                                 |
| Credential/secret scrub in assertions                 | Pass                                 |

### 30–31. Files

**Created:** `tests/integration/transport/*`, `docs/specifications/TransportIntegrationTestingSpecification.md`
**Modified:** Roadmap, Architecture, Streaming, specs index, API README, integration README

### 32–35. Exact results

| Check                                                               | Result                                                              |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tests/integration/transport`                                       | **22 passed**                                                       |
| Full regression (`tests/api` + Phase 10 + acceptance + integration) | **362 passed**                                                      |
| ruff                                                                | clean                                                               |
| mypy (`--follow-imports=silent`)                                    | clean                                                               |
| Benchmark                                                           | not claimed — `BASELINE_NOT_PRODUCTION_SLA` on concurrency/outbound |

### 37. GATE-01…64

Applicable gates **PASS**. Gaps intentionally not duplicated: JWT matrix, TokenBucket unit, Phase 10 golden path, synthetic `offer_bus_event` shape tests.

### 38–39. Limitations / risks

- Replay→EventBus is **fixture-wired** (`wire_replay_to_event_bus`); Phase10Harness still uses a local events list by default.
- Payload `session_id` serializes as `{"value": ...}` in some envelopes; tests use top-level envelope `session_id`.
- Heartbeat timeout E2E not re-covered (already unit-tested in 11.9).

### 40–41. Roadmap / next

**11.13 ✓** — recommended next: **11.14 Live Streaming Acceptance**.

## Assistant

**Agent 11.13 is correctly ACCEPTED.** This is a strong result because it proves the actual multi-component path rather than simply repeating the individual component tests.

### Phase 11 status

| Agent | Component | Status |
|---|---|---|
| 11.6 | Transport Authentication & Authorization | ✅ ACCEPTED |
| 11.6.1 | Live Telemetry Streaming | ✅ ACCEPTED |
| 11.6.2 | Rate Limiting & Abuse Protection | ✅ ACCEPTED |
| 11.6.3 | Transport Hardening | ✅ ACCEPTED |
| 11.7 | Replay Streaming | ✅ ACCEPTED |
| 11.7.1 | Outbound Backpressure & Rate Control | ✅ ACCEPTED |
| 11.8 | Subscription System | ✅ ACCEPTED |
| 11.9 | Connection & Session Management | ✅ ACCEPTED |
| 11.10 | Backpressure & Rate Control | 🔒 SUPERSEDED |
| 11.11 | Transport Authentication & Authorization | 🔒 SUPERSEDED |
| 11.12 | Transport Observability | ✅ ACCEPTED |
| **11.13** | **Transport Integration Testing** | **✅ ACCEPTED** |
| **11.14** | **Live Streaming Acceptance** | **⏳ NEXT** |
| 11.15 | Phase 11 Acceptance | ⏳ |

### What 11.13 has now proven

```text
Phase 10 Runtime
      ↓
EventBus
      ↓
Live/Replay bridge
      ↓
Transport publishers
      ↓
Subscription Registry
      ↓
Outbound Controller
      ↓
WebSocket
      ↓
Client
```

The important results are:

- **362 total tests passing**
- **22 new transport integration tests**
- REST stack verified
- LIVE EventBus → WS verified
- REPLAY → WS verified
- LIVE/REPLAY isolation verified
- session isolation verified
- reconnect/resubscribe verified
- slow-client isolation verified
- observability verified
- shutdown verified
- credential/secret scrubbing verified
- Ruff clean
- mypy clean
- no duplicate transport subsystem introduced

### Two things I would carry forward

The Cursor report identifies two legitimate limitations:

1. **Replay → EventBus is fixture-wired** for the integration harness.
   - This is acceptable for 11.13 because the production Replay implementation was already accepted in 11.7.
   - **11.14 should not quietly introduce a second replay path.**

2. Some envelopes serialize `session_id` internally as `{"value": ...}`.
   - The tests correctly rely on the **canonical top-level transport `session_id`**.
   - We should avoid changing this merely for cosmetic consistency unless the protocol contract explicitly requires it.

The heartbeat omission is also fine because **11.9 already owns and tested heartbeat behavior**; 11.13 correctly avoided unnecessary duplication.

### Next

The next agent should now be **11.14 — Live Streaming Acceptance**.

This should be a **production-behavior acceptance/performance/concurrency gate**, not another implementation agent. Its job is to prove that the complete LIVE streaming pipeline is ready before we move to the final **11.15 Phase 11 Acceptance**.

## User

Please give commands for Agent 11.14	Live Streaming Acceptance	Performance, concurrency, disconnect/reconnect testing ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. **11.14 should be the final LIVE-streaming acceptance/performance gate before 11.15**, with no new transport architecture. It should build on 11.13 rather than duplicate it.

```text
=========================================================
RACEVISION — AGENT 11.14
LIVE STREAMING ACCEPTANCE
=========================================================

OBJECTIVE
=========

Perform the formal acceptance validation of the complete LIVE streaming
runtime established by Phase 10 + Phase 11.

This Agent is ACCEPTANCE / PERFORMANCE / CONCURRENCY TESTING ONLY.

DO NOT create new transport architecture.

DO NOT create a second:

- Runtime
- EventBus
- LiveSessionAdapter
- WebSocket gateway
- authentication system
- authorization system
- rate limiter
- hardening layer
- subscription system
- connection manager
- outbound backpressure system
- telemetry publisher
- observability system

All accepted ownership from Agents 11.6 through 11.13 MUST remain
unchanged.

The purpose of Agent 11.14 is to determine whether the LIVE streaming
pipeline is operationally ready for Phase 11 final acceptance.

=========================================================
AUTHORITATIVE ARCHITECTURE
=========================================================

Phase 10:

LiveProvider
    ↓
LiveSessionAdapter
    ↓
CacheManager / TimelineService
    ↓
EventBus
    ↓
LiveTelemetryStreamPublisher

Phase 11:

LiveTelemetryStreamPublisher
    ↓
WebSocketConnectionManager
    ↓
SubscriptionRegistry
    ↓
OutboundDeliveryController
    ↓
BoundedOutboundQueue
    ↓
WebSocket client

Supporting boundaries:

11.6   → Authentication / Authorization
11.6.2 → Inbound Rate Limiting / Abuse Protection
11.6.3 → Transport Hardening
11.7.1 → Outbound Backpressure / Rate Control
11.8   → Subscription System
11.9   → Connection / Session / Heartbeat
11.12  → Transport Observability
11.13  → Integration Testing
11.14  → THIS ACCEPTANCE AGENT
11.15  → Phase 11 Final Acceptance

=========================================================
CORE ACCEPTANCE PRINCIPLE
=========================================================

The acceptance target is:

LIVE F1 telemetry can be delivered through the production transport
boundary to multiple clients without:

- blocking Phase 10 Runtime
- blocking EventBus
- blocking LiveSessionAdapter
- blocking another client
- corrupting canonical telemetry
- violating session isolation
- violating authorization
- creating uncontrolled queues
- leaking secrets
- losing transport lifecycle correctness
- introducing transport timing authority

=========================================================
FIRST STEP — AUDIT
=========================================================

Before implementing tests:

Audit:

tests/integration/transport/
tests/api/
tests/runtime/
tests/acceptance/
tests/benchmarks/
existing performance/load test infrastructure

Audit Agent 11.13 tests first.

Do NOT duplicate existing correctness tests unnecessarily.

11.14 should concentrate on:

- sustained LIVE streaming
- concurrency
- throughput
- slow clients
- disconnect/reconnect
- heartbeat
- queue pressure
- recovery
- fairness
- Runtime non-blocking behavior
- operational observability

=========================================================
NO PRODUCTION SLA CLAIMS
=========================================================

Unless the repository already contains an explicitly approved production
SLA, DO NOT invent one.

Any locally measured performance must be labelled:

BASELINE_NOT_PRODUCTION_SLA

Performance measurements are evidence for regression detection and
acceptance, NOT a claim of production capacity.

Report:

- environment
- client count
- duration
- telemetry rate
- event rate
- payload size
- queue configuration
- backpressure configuration
- rate-limit configuration
- observed throughput
- observed latency where measurable
- drops
- coalescing
- disconnects
- errors

=========================================================
TEST ENVIRONMENT
=========================================================

Use:

- real create_app
- real Phase 10 LIVE runtime wiring
- real EventBus
- real LiveSessionAdapter path
- real LIVE publisher
- real WebSocket transport
- real authentication boundary
- real subscription registry
- real outbound controller
- real connection manager
- real observability aggregation

Use existing deterministic test adapters.

Do NOT require:

- real F1 external feed
- Twitch
- Kick
- YouTube
- OBS
- external Redis
- external authentication provider
- external metrics service

unless already required by the repository.

=========================================================
LIVE STREAM GOLDEN PATH
=========================================================

Every major acceptance test must preserve this path:

LiveProvider / test LIVE source
        ↓
LiveSessionAdapter
        ↓
Phase 10 Runtime
        ↓
EventBus
        ↓
LiveTelemetryStreamPublisher
        ↓
SubscriptionRegistry
        ↓
OutboundDeliveryController
        ↓
BoundedOutboundQueue
        ↓
WebSocket client

Do NOT publish directly into the WebSocket manager as the primary
acceptance path.

The acceptance must prove the real Phase 10 → Phase 11 boundary.

=========================================================
TEST GROUP 1 — SINGLE CLIENT BASELINE
=========================================================

Establish a deterministic baseline.

Test:

1. Start LIVE session.
2. Authenticate one client.
3. Subscribe to TELEMETRY.
4. Produce a known number of canonical telemetry frames.
5. Receive frames.
6. Verify expected delivery.
7. Verify source sequence.
8. Verify transport sequence.
9. Verify session_id.
10. Verify operating_mode = LIVE.
11. Verify metadata preservation.
12. Verify no Runtime mutation.

Record:

- frames produced
- frames received
- frames intentionally shed
- errors
- duration
- observed rate

With backpressure disabled, the normal baseline should demonstrate
stable delivery under the configured test rate.

=========================================================
TEST GROUP 2 — MULTI-CLIENT CONCURRENCY
=========================================================

Test at least:

- 2 clients
- 5 clients
- 10 clients
- 25 clients if the test environment supports it
- higher counts only if existing infrastructure can safely support them

Do not claim that these numbers represent production capacity.

For each client:

- authenticate
- subscribe
- receive LIVE telemetry
- verify session isolation
- verify no cross-client corruption

Measure:

- total frames
- per-client frames
- aggregate delivery
- errors
- queue pressure
- drops
- coalescing
- connection count
- subscription count

=========================================================
TEST GROUP 3 — MULTI-SESSION CONCURRENCY
=========================================================

Create multiple LIVE sessions.

At minimum:

SESSION A
SESSION B

Prefer three sessions if deterministic fixtures support it.

Clients must subscribe to specific sessions.

Verify:

A clients receive A only.

B clients receive B only.

No client receives telemetry from another session.

Repeat under concurrent load.

Verify session filtering occurs before enqueue where the architecture
requires it.

Verify principal/session authorization remains enforced.

=========================================================
TEST GROUP 4 — FANOUT
=========================================================

One canonical LIVE frame should fan out to multiple eligible clients.

Verify:

Runtime produces one canonical frame.

Multiple subscribed clients receive the frame independently.

One client becoming slow must not force the Runtime to produce duplicate
Runtime frames.

Do NOT introduce per-client Runtime processing.

=========================================================
TEST GROUP 5 — SLOW CLIENT
=========================================================

Create:

CLIENT A = deliberately slow
CLIENT B = normal
CLIENT C = normal

Publish sustained LIVE telemetry.

Make A unable or slow to consume.

Verify:

A develops outbound pressure.

A remains bounded.

A may experience:

- shedding
- coalescing
- rate control
- DEGRADED state
- eventual disconnect

according to the existing 11.7.1 policy.

B continues receiving.

C continues receiving.

Most importantly:

A MUST NOT block:

- LiveSessionAdapter
- Runtime
- EventBus
- B
- C

=========================================================
TEST GROUP 6 — RUNTIME NON-BLOCKING
=========================================================

Measure the producer path while a client is intentionally stalled.

Verify the Runtime/EventBus publishing path remains non-blocking.

Use bounded timing assertions appropriate for the test environment.

Do NOT establish a fake absolute production SLA.

Record:

BASELINE_NOT_PRODUCTION_SLA

The test should fail if outbound client pressure causes unbounded
blocking in the Runtime path.

=========================================================
TEST GROUP 7 — EVENT DELIVERY UNDER LOAD
=========================================================

Generate LIVE domain events while telemetry is streaming.

Verify:

CONTROL > EVENT > SNAPSHOT > TELEMETRY

according to existing admission/drop policy.

Do NOT require send-side priority reordering because the current
architecture explicitly retains FIFO dequeue.

Verify EVENT protection under telemetry pressure.

Verify canonical event payloads remain unchanged.

=========================================================
TEST GROUP 8 — SNAPSHOT DELIVERY UNDER LOAD
=========================================================

Subscribe to:

- TELEMETRY
- SNAPSHOT

Generate sustained telemetry.

Verify snapshot delivery remains functional.

Under pressure, snapshot rate limiting/coalescing may occur according
to 11.7.1.

Verify:

- no payload mutation
- no sequence corruption
- no session leakage
- no Runtime blocking

=========================================================
TEST GROUP 9 — HEARTBEAT
=========================================================

Use Agent 11.9 heartbeat.

Verify:

- connection establishes
- heartbeat operates
- healthy client remains connected
- missed heartbeat eventually closes the connection
- cleanup occurs
- metrics update
- reconnect works

Do not modify heartbeat logic.

Do not use application inactivity as an idle timeout.

=========================================================
TEST GROUP 10 — DISCONNECT
=========================================================

Test deliberate client disconnect.

Sequence:

1. connect
2. authenticate
3. subscribe
4. receive telemetry
5. disconnect
6. verify cleanup
7. verify subscription removal
8. verify queue cleanup
9. verify connection metrics
10. continue producing telemetry

Runtime MUST continue normally.

No orphaned subscription must remain.

No orphaned queue must remain.

No stale connection must remain.

=========================================================
TEST GROUP 11 — ABRUPT DISCONNECT
=========================================================

Simulate abrupt client termination.

Examples:

- socket close
- transport exception
- client task cancellation
- connection reset where test infrastructure supports it

Verify:

- lifecycle transitions correctly
- cleanup is idempotent
- subscriptions are removed
- outbound queue is cleaned
- Runtime continues
- other clients continue

=========================================================
TEST GROUP 12 — RECONNECT
=========================================================

Test:

Client
  ↓
connect
  ↓
authenticate
  ↓
subscribe
  ↓
receive telemetry
  ↓
disconnect
  ↓
reconnect
  ↓
new connection_id
  ↓
authenticate again
  ↓
resubscribe
  ↓
receive telemetry

Verify:

new connection_id != old connection_id

Old cleanup cannot remove new connection.

Reconnect requires authentication.

Reconnect requires resubscription.

No durable missed-frame resume occurs.

Do NOT implement durable resume.

=========================================================
TEST GROUP 13 — RECONNECT STORM
=========================================================

Create controlled reconnect activity.

Test multiple clients disconnecting and reconnecting.

Use a bounded deterministic test.

Verify:

- rate limiting protects admission
- no connection explosion
- no subscription explosion
- no orphaned connections
- no orphaned subscriptions
- no Runtime impact
- no peer-client impact

Do NOT claim this represents a production DDoS test.

=========================================================
TEST GROUP 14 — RATE LIMITING
=========================================================

Exercise 11.6.2 during reconnect and subscription churn.

Verify:

- connection limits
- reconnect limits
- subscription limits
- auth abuse limits
- concurrent connection limits

Verify rejected clients receive the existing transport error.

Verify rate-limit metrics increase.

Verify Runtime remains unaffected.

=========================================================
TEST GROUP 15 — AUTHORIZATION UNDER LOAD
=========================================================

Use valid and invalid principals.

Test concurrently:

authorized clients
unauthorized clients

Verify:

authorized clients receive LIVE telemetry.

unauthorized clients do not.

Auth failures do not affect authorized clients.

No credentials are exposed.

=========================================================
TEST GROUP 16 — HARDENING UNDER LOAD
=========================================================

Exercise malformed traffic while valid clients are streaming.

Test:

- invalid WS envelopes
- invalid schema
- invalid sequence
- invalid subscription
- oversized protocol payload where supported
- invalid session IDs

Verify malformed clients are rejected without affecting valid clients.

=========================================================
TEST GROUP 17 — BACKPRESSURE RECOVERY
=========================================================

Create pressure.

Then restore the slow client.

Verify:

- pressure decreases
- connection can recover where policy permits
- DEGRADED can return to READY
- queues drain according to policy
- telemetry continues
- no permanent starvation

If policy disconnects after CRITICAL grace, verify the documented
disconnect behavior instead of requiring recovery.

=========================================================
TEST GROUP 18 — FAIRNESS
=========================================================

Use:

CLIENT A = fast
CLIENT B = fast
CLIENT C = slow

Verify A and B remain healthy while C is pressured.

Repeat with different clients as the slow client.

No single client may monopolize shared transport resources.

No client may globally degrade the Runtime.

=========================================================
TEST GROUP 19 — QUEUE BOUNDING
=========================================================

Verify outbound queues remain bounded.

Record:

- configured queue limit
- maximum observed queue depth
- pressure state
- dropped frames
- coalesced frames
- disconnects

Verify queue size cannot grow without bound.

Do NOT modify queue implementation.

=========================================================
TEST GROUP 20 — TELEMETRY INTEGRITY
=========================================================

This is mandatory.

For received frames verify:

- canonical payload fields
- source sequence
- timestamp semantics
- session_id
- operating_mode
- metadata
- driver/car/session association where applicable

Verify transport does NOT:

- interpolate
- extrapolate
- reorder
- rewrite source sequence
- modify timestamps
- change Runtime state

=========================================================
TEST GROUP 21 — DELAY / INTERPOLATION INTEGRITY
=========================================================

Phase 10 remains authoritative.

Verify transport does not independently apply:

- delay
- interpolation
- extrapolation

If the LiveSessionAdapter produces delayed/interpolated metadata,
that metadata must be preserved.

Transport must not add another delay layer.

=========================================================
TEST GROUP 22 — SEQUENCE INTEGRITY
=========================================================

Verify two independent concepts:

SOURCE SEQUENCE
    = canonical Runtime/EventBus source

TRANSPORT SEQUENCE
    = WebSocket transport envelope sequence

Verify:

- source sequence preserved
- transport sequence generated independently
- transport does not overwrite source sequence
- source ordering is preserved
- no transport reordering

Do not require numerical equality.

=========================================================
TEST GROUP 23 — LIVE/REPLAY BOUNDARY
=========================================================

Although 11.14 focuses on LIVE, include a regression guard.

While LIVE clients are streaming:

activate/use REPLAY in another session where supported.

Verify:

LIVE clients do not receive REPLAY telemetry.

REPLAY clients do not receive LIVE telemetry.

This is an isolation regression guard.

Do not reimplement replay tests from 11.13.

=========================================================
TEST GROUP 24 — OBSERVABILITY
=========================================================

After each major acceptance scenario query:

GET /api/v1/runtime/transport

using appropriate RUNTIME_READ authorization.

Verify:

- connections
- subscriptions
- live streaming counters
- outbound pressure
- rate limits
- security events
- heartbeat state
- errors

Verify public /health remains coarse.

Verify metrics are bounded and do not contain:

- connection IDs as uncontrolled labels
- session IDs as uncontrolled labels
- credentials
- tokens
- secrets

=========================================================
TEST GROUP 25 — ERROR RECOVERY
=========================================================

Cause controlled errors.

Verify one client failure does not cascade.

Examples:

- malformed client
- authorization rejection
- rate-limit rejection
- heartbeat timeout
- outbound disconnect
- subscription failure

Healthy clients must continue.

=========================================================
TEST GROUP 26 — SHUTDOWN
=========================================================

Run active LIVE streaming.

Then invoke application shutdown.

Verify:

- new connections are rejected
- existing connections close
- subscriptions clean up
- queues clean up
- heartbeat stops
- metrics finalize correctly
- Runtime remains consistent
- shutdown completes within configured bound

Do not change shutdown implementation unless a real defect is discovered.

=========================================================
TEST GROUP 27 — SOAK / SUSTAINED STREAM
=========================================================

If the test environment permits, run a deterministic sustained stream.

Suggested test durations:

SHORT:
30 seconds

MEDIUM:
60 seconds

LONG:
5 minutes

Do not require a long soak if CI infrastructure cannot reliably support
it.

The test should be configurable.

Do not claim production reliability based solely on a local soak.

Record:

- frames produced
- frames received
- dropped
- coalesced
- disconnects
- reconnects
- errors
- queue pressure
- max queue depth
- Runtime errors
- EventBus errors

=========================================================
TEST GROUP 28 — CONCURRENCY MATRIX
=========================================================

Where infrastructure allows, test:

1 client
2 clients
5 clients
10 clients
25 clients

Optionally higher counts only when safe.

For each level record:

- connected clients
- successful subscriptions
- delivered frames
- dropped frames
- coalesced frames
- errors
- reconnects
- maximum queue depth
- observed throughput

Every result must be labelled:

BASELINE_NOT_PRODUCTION_SLA

=========================================================
TEST GROUP 29 — RESOURCE LEAK CHECK
=========================================================

After repeated:

connect
subscribe
stream
disconnect
reconnect

verify no unbounded growth in:

- connections
- subscriptions
- outbound queues
- background heartbeat tasks
- registry entries
- metrics registry structures

Use existing metrics/registry inspection facilities.

Do not introduce a new resource-management subsystem.

=========================================================
TEST GROUP 30 — CROSS-CLIENT PROTECTION
=========================================================

Prove:

Slow client A
cannot affect:

Fast client B
Fast client C
Runtime
EventBus

Test with:

- telemetry
- events
- snapshots

Verify all healthy clients remain functional.

=========================================================
PERFORMANCE MEASUREMENT
=========================================================

Where meaningful measure:

- frames/sec produced
- frames/sec delivered
- aggregate fanout rate
- client receive latency if deterministic
- queue occupancy
- drop count
- coalesce count
- connection setup time
- reconnect time

Avoid microbenchmark claims.

All measurements must state:

BASELINE_NOT_PRODUCTION_SLA

No production SLA may be invented.

=========================================================
TEST DETERMINISM
=========================================================

Avoid arbitrary sleeps.

Prefer:

- explicit events
- controlled clocks
- async conditions
- bounded polling
- deterministic fixtures

Every wait must have a timeout.

Tests must clean up:

- tasks
- connections
- subscriptions
- queues
- runtime sessions

=========================================================
CI SAFETY
=========================================================

Performance/concurrency tests must not destabilize normal CI.

If the repository has markers for:

- integration
- performance
- soak
- slow

use the existing convention.

Do NOT silently skip acceptance tests.

If a test requires an environment capability, document it explicitly.

=========================================================
NO TEST-ONLY ARCHITECTURE
=========================================================

Do not alter production code solely to make acceptance tests easier.

Test hooks are acceptable only when they already conform to repository
testing architecture.

Do not create:

- fake transport gateway
- fake subscription registry
- fake outbound controller
- fake EventBus replacement for the main acceptance path
- duplicate telemetry source

=========================================================
ACCEPTANCE GATES
=========================================================

GATE-01  Existing acceptance-suite audit
GATE-02  11.13 integration-suite audit
GATE-03  Single-client LIVE baseline
GATE-04  Multi-client LIVE streaming
GATE-05  Multi-session isolation
GATE-06  Fanout verification
GATE-07  Slow-client isolation
GATE-08  Runtime non-blocking
GATE-09  Event protection
GATE-10  Snapshot behavior
GATE-11  Heartbeat
GATE-12  Graceful disconnect
GATE-13  Abrupt disconnect
GATE-14  Reconnect
GATE-15  Reconnect authentication
GATE-16  Reconnect resubscription
GATE-17  No durable resume
GATE-18  Reconnect storm protection
GATE-19  Rate-limit protection
GATE-20  Authorization under load
GATE-21  Hardening under load
GATE-22  Backpressure activation
GATE-23  Backpressure recovery
GATE-24  Fairness
GATE-25  Queue boundedness
GATE-26  Telemetry integrity
GATE-27  Metadata integrity
GATE-28  Delay/interpolation integrity
GATE-29  Sequence integrity
GATE-30  LIVE/REPLAY isolation regression
GATE-31  Observability
GATE-32  Error isolation
GATE-33  Shutdown
GATE-34  Resource leak detection
GATE-35  Cross-client protection
GATE-36  Sustained streaming
GATE-37  Concurrency matrix
GATE-38  Deterministic test execution
GATE-39  Bounded test timeouts
GATE-40  No external service dependency
GATE-41  No duplicate subsystem
GATE-42  Phase 10 Runtime preserved
GATE-43  EventBus preserved
GATE-44  ReplayClock unaffected
GATE-45  Transport remains timing-unaware
GATE-46  Runtime remains identity-unaware
GATE-47  Session isolation
GATE-48  Credential protection
GATE-49  Error sanitization
GATE-50  Existing API regression
GATE-51  Phase 10 regression
GATE-52  Phase 10 acceptance regression
GATE-53  Phase 11 regression
GATE-54  Ruff clean
GATE-55  mypy clean
GATE-56  Documentation updated
GATE-57  Roadmap updated
GATE-58  Acceptance specification updated
GATE-59  Performance results documented
GATE-60  Final LIVE streaming readiness determination

=========================================================
REGRESSION REQUIREMENT
=========================================================

Run and preserve:

tests/api
tests/runtime
Phase 10 acceptance
tests/integration/transport
tests/api/outbound
tests/api/subscriptions
tests/api/connection
tests/api/observability

and all other existing relevant suites.

Do NOT weaken or delete previous tests.

=========================================================
DOCUMENTATION
=========================================================

Create:

docs/specifications/LiveStreamingAcceptanceSpecification.md

Update:

docs/Roadmap.md
Architecture documentation
Streaming documentation
API README
specification index
integration README where appropriate

Document:

- acceptance methodology
- concurrency methodology
- slow-client methodology
- reconnect methodology
- performance measurements
- environment
- test configuration
- limitations
- non-production-SLA designation
- acceptance decision

=========================================================
FINAL ACCEPTANCE REPORT
=========================================================

At completion report:

1. STATUS
2. Audit findings
3. Existing tests retained
4. New acceptance tests
5. Single-client baseline
6. Multi-client results
7. Multi-session results
8. Fanout results
9. Slow-client results
10. Runtime non-blocking results
11. Event results
12. Snapshot results
13. Heartbeat results
14. Disconnect results
15. Abrupt disconnect results
16. Reconnect results
17. Reconnect storm results
18. Rate-limit results
19. Authorization results
20. Hardening results
21. Backpressure results
22. Backpressure recovery
23. Fairness results
24. Queue bounds
25. Telemetry integrity
26. Metadata integrity
27. Delay/interpolation integrity
28. Sequence integrity
29. LIVE/REPLAY isolation
30. Observability results
31. Error recovery
32. Shutdown results
33. Resource leak results
34. Soak results
35. Concurrency matrix
36. Performance measurements
37. Files created
38. Files modified
39. Exact test results
40. Full regression results
41. Ruff result
42. mypy result
43. Benchmark designation
44. GATE-01…60 results
45. Limitations
46. Remaining risks
47. Production-readiness assessment
48. Roadmap status
49. Recommended next Agent

=========================================================
SUCCESS CRITERIA
=========================================================

Agent 11.14 may be marked ACCEPTED only if evidence demonstrates:

1. LIVE telemetry reaches authenticated subscribed clients.

2. Multiple clients can receive LIVE telemetry concurrently.

3. Multiple sessions remain isolated.

4. One client's slowness cannot block another client.

5. One client's slowness cannot block Phase 10 Runtime.

6. One client's slowness cannot block EventBus.

7. Outbound queues remain bounded.

8. Backpressure behaves according to 11.7.1.

9. Healthy clients remain healthy when another client is slow.

10. Disconnect cleanup is correct.

11. Abrupt disconnect cleanup is correct.

12. Reconnect creates a new connection identity.

13. Reconnect requires authentication.

14. Reconnect requires resubscription.

15. No durable missed-frame resume is introduced.

16. Heartbeat operates correctly.

17. Rate limiting protects admission/churn.

18. Authorization remains enforced under concurrency.

19. Transport hardening remains enforced.

20. Telemetry remains canonical.

21. Source sequences remain intact.

22. Transport sequences remain separate.

23. Transport does not add timing authority.

24. Transport does not independently delay/interpolate/extrapolate.

25. LIVE and REPLAY remain isolated.

26. Observability reflects actual transport behavior.

27. Errors remain sanitized.

28. Secrets remain protected.

29. Shutdown remains bounded.

30. No resource leaks are detected.

31. Phase 10 acceptance remains green.

32. Phase 11 integration tests remain green.

33. No duplicate subsystem has been introduced.

34. Ruff is clean.

35. mypy is clean.

=========================================================
IMPORTANT
=========================================================

If an acceptance test exposes a genuine production defect:

DO NOT weaken the test.

DO NOT bypass the failing component.

DO NOT create a duplicate subsystem.

Identify the owning Agent/component and report the defect precisely.

Only make a production-code change if it is a minimal correction that
preserves the accepted architecture and contracts.

If a change materially expands scope, STOP and report it as a finding
instead of silently redesigning the system.

=========================================================
START
=========================================================

FIRST:
Audit existing Phase 10, Phase 11, and 11.13 integration tests.

SECOND:
Implement only missing LIVE acceptance/performance/concurrency coverage.

THIRD:
Run the acceptance suite.

FOURTH:
Run the complete regression suite.

FIFTH:
Run Ruff and mypy.

SIXTH:
Produce the full 49-section acceptance report.

DO NOT modify accepted architecture merely to satisfy tests.

PRESERVE ALL ACCEPTED PHASE 10 AND PHASE 11 CONTRACTS.

=========================================================
END AGENT 11.14
=========================================================
```

## User

## AGENT 11.14 — ACCEPTED

LIVE streaming is acceptance-ready for Phase 11.14. Suite is verification-only; no duplicate transport subsystems.

### 1. STATUS

**ACCEPTED**

### 2. Audit findings

11.13 covers EventBus→WS golden paths. Gaps were sustained concurrency (2–25), soak, reconnect storm + RL, heartbeat smoke under live gateway, resource-leak loops, and structured **BASELINE\_NOT\_PRODUCTION\_SLA** reporting.

### 3–4. Tests

**Retained:** API + Phase 10 + 11.13.
**New:** 20 tests in `tests/acceptance/live_streaming/`.

### 5–36. Evidence (summary)

| Area                                              | Result                                                         |
| ------------------------------------------------- | -------------------------------------------------------------- |
| Single-client baseline (Runtime→EventBus→WS)      | Pass — provenance `live_session_adapter`, monotonic source seq |
| Concurrency 2/5/10/25                             | Pass — fanout floors; **BASELINE\_NOT\_PRODUCTION\_SLA**       |
| Multi-session A/B under load                      | Pass                                                           |
| Slow client vs peers + Runtime non-block          | Pass (accept flooded <2.5s; queues bounded)                    |
| Disconnect / abrupt / reconnect + resubscribe     | Pass                                                           |
| Reconnect storm + rate limit                      | Pass                                                           |
| Authz / hardening under healthy stream            | Pass                                                           |
| Heartbeat metrics                                 | Pass (`heartbeat_pings_sent`)                                  |
| Soak SHORT (default 3s, env override)             | Pass                                                           |
| Resource leak loop (8× connect/stream/disconnect) | Pass                                                           |
| Observability + coarse health                     | Pass                                                           |
| Shutdown during LIVE                              | Pass                                                           |
| LIVE/REPLAY isolation regression                  | Pass                                                           |

### 37–38. Files

**Created:** `tests/acceptance/live_streaming/*`, `tests/acceptance/README.md`, `docs/specifications/LiveStreamingAcceptanceSpecification.md`
**Modified:** Roadmap, Architecture, Streaming, specs index, API README, integration README

### 39–42. Exact results

| Check                                                       | Result                                        |
| ----------------------------------------------------------- | --------------------------------------------- |
| `tests/acceptance/live_streaming`                           | **20 passed**                                 |
| Full regression (api + Phase 10 + integration + acceptance) | **382 passed**                                |
| ruff                                                        | clean                                         |
| mypy                                                        | clean                                         |
| Benchmark designation                                       | **BASELINE\_NOT\_PRODUCTION\_SLA** everywhere |

### 44. GATE-01…60

Applicable gates **PASS**. Heartbeat *timeout disconnect* remains owned by 11.9 unit coverage; 11.14 asserts live ping metrics.

### 45–47. Limitations / readiness

Default soak is CI-short (`LIVE_ACCEPTANCE_SOAK_SECONDS`). Delivery under pressure may shed. **Production-readiness for Agent 11.14:** LIVE path is acceptance-ready for **11.15 Phase 11 Final Acceptance** — not a claim of production capacity.

### 48–49. Roadmap / next

**11.14 ✓** — recommended next: **11.15 Phase 11 Acceptance**.

## Assistant

Excellent. **Agent 11.14 is correctly ACCEPTED.** The result is consistent with the architecture we've established: 11.14 verified the complete LIVE path without creating another transport subsystem.

### Phase 11 status now

| Agent | Component | Status |
|---|---|---|
| 11.6 | Transport Authentication & Authorization | ✅ ACCEPTED |
| 11.6.1 | Live Telemetry Streaming | ✅ ACCEPTED |
| 11.6.2 | Rate Limiting & Abuse Protection | ✅ ACCEPTED |
| 11.6.3 | Transport Hardening | ✅ ACCEPTED |
| 11.7 | Replay Streaming | ✅ ACCEPTED |
| 11.7.1 | Outbound Backpressure & Rate Control | ✅ ACCEPTED |
| 11.8 | Subscription System | ✅ ACCEPTED |
| 11.9 | Connection & Session Management | ✅ ACCEPTED |
| 11.10 | Backpressure & Rate Control | 🔒 SUPERSEDED by 11.7.1 |
| 11.11 | Transport Authentication & Authorization | 🔒 SUPERSEDED by 11.6 |
| 11.12 | Transport Observability | ✅ ACCEPTED |
| 11.13 | Transport Integration Testing | ✅ ACCEPTED |
| **11.14** | **Live Streaming Acceptance** | **✅ ACCEPTED** |
| **11.15** | **Phase 11 Acceptance** | **⏳ NEXT** |

### Important evidence

The strongest part of 11.14 is that it tested the complete chain:

```text
LiveSessionAdapter
      ↓
Phase 10 Runtime
      ↓
EventBus
      ↓
LiveTelemetryStreamPublisher
      ↓
SubscriptionRegistry
      ↓
OutboundDeliveryController
      ↓
BoundedOutboundQueue
      ↓
WebSocket clients
```

And specifically demonstrated:

- **2 / 5 / 10 / 25 concurrent clients** ✅
- Multi-session isolation ✅
- Slow-client isolation ✅
- Runtime non-blocking behavior ✅
- Disconnect/reconnect/resubscription ✅
- Reconnect storm protection ✅
- Rate limiting ✅
- AuthZ/hardening under load ✅
- Heartbeat activity ✅
- Resource-leak loop ✅
- Shutdown during LIVE streaming ✅
- LIVE/REPLAY isolation ✅
- 20 new acceptance tests ✅
- **382 total regression tests passing** ✅
- Ruff clean ✅
- mypy clean ✅

And importantly, Cursor correctly **did not claim production capacity**. The performance evidence remains:

> `BASELINE_NOT_PRODUCTION_SLA`

That distinction should remain in the final Phase 11 acceptance documentation.

### One important interpretation

The remaining heartbeat limitation is **not a blocker**:

> heartbeat timeout disconnect remains owned by 11.9

That is correct ownership. **11.14 validates LIVE streaming while 11.9 owns the heartbeat lifecycle implementation.** We should not duplicate the timeout mechanism in 11.14.

---

## Next: Agent 11.15

At this point, **11.15 should be the actual Phase 11 final acceptance gate**, not another implementation agent.

It should answer one question:

> **Is Phase 11 — Transport & Live Streaming Runtime — formally complete and ready to hand over to Phase 12 Unity Integration & 3D Scene Runtime?**

It should consolidate evidence from **11.6 → 11.14**, verify all architectural invariants, run the final regression suite, verify documentation/roadmap consistency, and produce the final Phase 11 acceptance decision.

**I would not add another implementation agent between 11.14 and 11.15.**

## User

Please give commands for Agent 11.15	Phase 11 Acceptance	Final acceptance gate ( 1 click copy and paste cursor friendly)

## Assistant

Yes. **11.15 should be a final verification and sign-off agent only**. It must not introduce new transport functionality. It should consolidate Agents 11.6–11.14, verify the entire Phase 11 contract, and explicitly determine whether Phase 12 can begin.

```text
=========================================================
RACEVISION — AGENT 11.15
PHASE 11 FINAL ACCEPTANCE
=========================================================

OBJECTIVE
=========

Perform the FINAL ACCEPTANCE GATE for:

PHASE 11 — TRANSPORT & LIVE STREAMING RUNTIME

This Agent is VERIFICATION / ACCEPTANCE / SIGN-OFF ONLY.

DO NOT create new transport architecture.

DO NOT create new production functionality unless a genuine defect is
discovered that requires a minimal corrective change.

DO NOT create a second implementation of any accepted Phase 11 subsystem.

The purpose of Agent 11.15 is to determine whether Phase 11 is formally:

    ACCEPTED

or:

    NOT ACCEPTED

and to provide the evidence supporting that decision.

=========================================================
PHASE 11 ACCEPTED OWNERSHIP
=========================================================

The following ownership is authoritative and MUST NOT be duplicated:

11.6
Transport Authentication & Authorization
    backend/api/security/

11.6.1
Live Telemetry Streaming
    backend/api/telemetry/

11.6.2
Rate Limiting & Abuse Protection
    backend/api/ratelimit/

11.6.3
Transport Hardening
    backend/api/hardening/

11.7
Replay Streaming
    backend/api/replay/

11.7.1
Outbound Backpressure & Rate Control
    backend/api/outbound/

11.8
Subscription System
    backend/api/subscriptions/

11.9
Connection & Session Management
    existing WebSocketConnectionManager /
    ClientConnection lifecycle

11.10
SUPERSEDED / SATISFIED BY 11.7.1

11.11
SUPERSEDED / SATISFIED BY 11.6

11.12
Transport Observability
    backend/api/observability/

11.13
Transport Integration Testing
    tests/integration/transport/

11.14
Live Streaming Acceptance
    tests/acceptance/live_streaming/

11.15
FINAL PHASE 11 ACCEPTANCE
    THIS AGENT

=========================================================
AUTHORITATIVE ARCHITECTURE
=========================================================

Phase 10 remains the Runtime authority.

LIVE:

LiveProvider
    ↓
LiveSessionAdapter
    ↓
Phase 10 Runtime
    ↓
CacheManager / TimelineService
    ↓
EventBus
    ↓
LiveTelemetryStreamPublisher
    ↓
SubscriptionRegistry
    ↓
OutboundDeliveryController
    ↓
BoundedOutboundQueue
    ↓
WebSocket client


REPLAY:

ReplayClock / Replay Runtime
    ↓
EventBus
    ↓
ReplayStreamPublisher
    ↓
SubscriptionRegistry
    ↓
OutboundDeliveryController
    ↓
BoundedOutboundQueue
    ↓
WebSocket client


REST:

Client
    ↓
Transport Hardening
    ↓
Rate Limiting
    ↓
Authentication / Authorization
    ↓
REST handler
    ↓
existing Runtime services


WEBSOCKET:

Client
    ↓
Transport Hardening
    ↓
Rate Limiting
    ↓
Authentication / Authorization
    ↓
WebSocketConnectionManager
    ↓
SubscriptionRegistry
    ↓
OutboundDeliveryController
    ↓
BoundedOutboundQueue
    ↓
Client

=========================================================
ARCHITECTURAL INVARIANTS
=========================================================

The final acceptance MUST verify these invariants.

1. Phase 10 Runtime remains the authoritative runtime.

2. Runtime remains identity-unaware.

3. Runtime does not know Principal.

4. Runtime does not know transport authentication.

5. Runtime does not know WebSocket connections.

6. Runtime does not perform transport authorization.

7. Runtime does not perform outbound rate limiting.

8. EventBus remains the canonical event distribution boundary.

9. Transport is a consumer of Runtime/EventBus output.

10. Transport does not become a second Runtime.

11. Transport does not become a timing authority.

12. Transport does not independently apply delay.

13. Transport does not independently interpolate.

14. Transport does not independently extrapolate.

15. Transport does not reorder canonical Runtime frames.

16. Source sequence remains distinct from transport sequence.

17. LIVE and REPLAY remain isolated.

18. Session isolation remains enforced.

19. Principal authorization remains enforced.

20. Authentication and authorization remain separate concerns.

21. Inbound abuse protection remains owned by 11.6.2.

22. Outbound delivery protection remains owned by 11.7.1.

23. Subscription ownership remains owned by 11.8.

24. Connection lifecycle remains owned by 11.9.

25. Observability remains aggregation-only.

26. No duplicate subsystem has been introduced.

=========================================================
STEP 1 — FULL AUDIT
=========================================================

Before running tests:

Audit the current repository.

Inspect:

- docs/Roadmap.md
- Architecture documentation
- Streaming documentation
- API documentation
- specification index
- Phase 10 specifications
- Phase 11 specifications
- transport README
- integration README
- acceptance README

Inspect all relevant implementation packages:

backend/api/security/
backend/api/ratelimit/
backend/api/hardening/
backend/api/telemetry/
backend/api/replay/
backend/api/outbound/
backend/api/subscriptions/
backend/api/observability/

Inspect:

WebSocketConnectionManager
ClientConnection
LiveSessionAdapter
Replay runtime
EventBus integration
REST routes
WS routes
application wiring

Confirm ownership is consistent.

=========================================================
STEP 2 — VERIFY AGENT ACCEPTANCE EVIDENCE
=========================================================

Confirm the repository contains evidence for:

11.6
Transport Authentication & Authorization

11.6.1
Live Telemetry Streaming

11.6.2
Rate Limiting & Abuse Protection

11.6.3
Transport Hardening

11.7
Replay Streaming

11.7.1
Outbound Backpressure & Rate Control

11.8
Subscription System

11.9
Connection & Session Management

11.12
Transport Observability

11.13
Transport Integration Testing

11.14
Live Streaming Acceptance

Do not merely trust documentation.

Where practical, verify the tests and implementation exist.

=========================================================
STEP 3 — VERIFY SUPERSEDED AGENTS
=========================================================

Confirm:

11.10 = SUPERSEDED / SATISFIED BY 11.7.1

11.11 = SUPERSEDED / SATISFIED BY 11.6

There must NOT be duplicate:

- backpressure
- rate control
- authentication
- authorization

systems created for those old roadmap positions.

Update stale documentation if required.

Do not create new functionality.

=========================================================
STEP 4 — REST FINAL ACCEPTANCE
=========================================================

Verify:

- authentication
- authorization
- rate limiting
- request hardening
- body limits
- content-type validation
- UUID session validation
- sanitized errors
- security headers
- correlation/request ID bounds
- health behavior
- runtime transport observability

Verify protected endpoints require the appropriate permission.

Verify public health remains coarse.

Verify detailed transport observability requires RUNTIME_READ.

=========================================================
STEP 5 — WEBSOCKET FINAL ACCEPTANCE
=========================================================

Verify:

- authentication occurs before acceptance
- authorization is enforced
- lifecycle is correct
- principal is immutable after binding
- session scope is enforced
- subscriptions are validated
- malformed envelopes are rejected
- payload limits are enforced
- origin policy behaves according to configuration
- heartbeat works
- disconnect cleanup is idempotent
- reconnect creates a new connection identity
- reconnect requires authentication
- reconnect requires resubscription

Verify no durable missed-frame resume exists.

Do NOT introduce durable resume.

=========================================================
STEP 6 — LIVE STREAM FINAL ACCEPTANCE
=========================================================

Verify the complete path:

LiveSessionAdapter
    ↓
Phase 10 Runtime
    ↓
EventBus
    ↓
LiveTelemetryStreamPublisher
    ↓
SubscriptionRegistry
    ↓
OutboundDeliveryController
    ↓
BoundedOutboundQueue
    ↓
WebSocket

Verify:

- canonical telemetry reaches clients
- LIVE mode is preserved
- session_id is preserved
- source sequence is preserved
- transport sequence is independent
- metadata is preserved
- no transport interpolation occurs
- no transport extrapolation occurs
- no transport delay is introduced
- no Runtime blocking occurs

Use the accepted 11.14 acceptance suite as primary evidence.

=========================================================
STEP 7 — REPLAY STREAM FINAL ACCEPTANCE
=========================================================

Verify:

Replay Runtime
    ↓
EventBus
    ↓
ReplayStreamPublisher
    ↓
SubscriptionRegistry
    ↓
OutboundDeliveryController
    ↓
WebSocket

Verify:

- replay telemetry is delivered in REPLAY mode
- replay events are delivered correctly
- replay session isolation works
- LIVE clients do not receive REPLAY data
- REPLAY clients do not receive LIVE data
- ReplayClock remains the timing authority
- transport does not implement seek
- transport does not implement pause
- transport does not implement playback timing

Do not create a second Replay Runtime.

=========================================================
STEP 8 — SUBSCRIPTION FINAL ACCEPTANCE
=========================================================

Verify subscription types:

- TELEMETRY
- EVENTS
- SNAPSHOT
- REPLAY
- MODE
- RUNTIME_STATUS

Verify:

- subscription IDs are distinct
- connection IDs are distinct
- session IDs are distinct
- source sequences are distinct
- transport sequences are distinct

Verify:

subscribe
unsubscribe
replace
duplicate handling
quotas
session isolation
cleanup

Verify reconnect requires resubscription.

No durable subscription persistence is required.

=========================================================
STEP 9 — OUTBOUND PROTECTION FINAL ACCEPTANCE
=========================================================

Verify Agent 11.7.1 remains the sole outbound protection system.

Verify:

- bounded queues
- per-connection isolation
- token buckets
- pressure states
- shedding
- coalescing
- recovery
- critical handling
- slow-client isolation

Verify priority policy:

CONTROL > EVENT > SNAPSHOT > TELEMETRY

Do NOT introduce send-side priority reordering if the accepted architecture
continues to use FIFO dequeue.

Verify:

slow client A

does not block:

client B
client C
Runtime
EventBus

=========================================================
STEP 10 — INBOUND PROTECTION FINAL ACCEPTANCE
=========================================================

Verify 11.6.2 remains the sole inbound rate-limit/abuse layer.

Verify:

- REST rate limiting
- WS connection limits
- reconnect limits
- inbound message limits
- subscription churn limits
- authentication abuse protection
- authorization abuse protection
- concurrent connection limits
- subscription quotas
- payload limits

Verify:

429 + Retry-After for REST where applicable.

WS rate-limit behavior follows accepted transport error/close semantics.

Do not create another limiter.

=========================================================
STEP 11 — HARDENING FINAL ACCEPTANCE
=========================================================

Verify 11.6.3 remains the sole transport hardening layer.

Verify:

- content length
- body size
- JSON content type
- UUID validation
- WS envelope validation
- schema version validation
- nested JSON bounds
- client sequence validation
- lifecycle gates
- cleanup
- error sanitization
- security headers
- request/correlation ID bounds
- Origin configuration

Verify no sensitive data appears in client errors.

=========================================================
STEP 12 — CONNECTION FINAL ACCEPTANCE
=========================================================

Verify Agent 11.9.

Lifecycle:

CONNECTING
    ↓
CONNECTED
    ↓
READY
    ↕
DEGRADED
    ↓
CLOSING
    ↓
CLOSED

Verify:

- bounded heartbeat
- monotonic heartbeat timing
- missed heartbeat behavior
- idempotent cleanup
- bounded shutdown
- principal immutability
- reconnect classification
- connection metrics

Do not add another lifecycle manager.

=========================================================
STEP 13 — OBSERVABILITY FINAL ACCEPTANCE
=========================================================

Verify Agent 11.12.

Confirm transport observability aggregates:

- connections
- subscriptions
- LIVE streaming
- REPLAY streaming
- snapshots
- outbound pressure
- rate limiting
- security
- heartbeat
- commands
- bounded error taxonomy

Verify:

GET /api/v1/runtime/transport

is protected correctly.

Verify:

/health

remains coarse.

Verify:

- no secrets
- no tokens
- no uncontrolled identifiers
- no credentials
- no per-session metric-cardinality explosion

Observability must remain read-only aggregation.

=========================================================
STEP 14 — INTEGRATION ACCEPTANCE
=========================================================

Run the complete Agent 11.13 integration suite.

Verify:

REST
    ↓
Auth
    ↓
Hardening
    ↓
Rate Limit
    ↓
Runtime

and:

Phase 10
    ↓
EventBus
    ↓
Publisher
    ↓
Subscription
    ↓
Outbound
    ↓
WS

Verify:

- LIVE
- REPLAY
- isolation
- reconnect
- slow clients
- observability
- shutdown
- concurrency

=========================================================
STEP 15 — LIVE ACCEPTANCE
=========================================================

Run the complete Agent 11.14 acceptance suite.

Verify:

- single client
- 2 clients
- 5 clients
- 10 clients
- 25 clients
- multi-session
- fanout
- slow client
- Runtime non-blocking
- disconnect
- abrupt disconnect
- reconnect
- reconnect storm
- rate limiting
- authorization
- hardening
- heartbeat
- queue bounds
- backpressure
- recovery
- fairness
- resource leaks
- soak
- shutdown
- LIVE/REPLAY isolation

All performance results must remain labelled:

BASELINE_NOT_PRODUCTION_SLA

Do not turn local benchmarks into production capacity claims.

=========================================================
STEP 16 — PHASE 10 REGRESSION
=========================================================

Phase 11 must not regress Phase 10.

Run all applicable:

- Phase 10 unit tests
- Phase 10 integration tests
- Phase 10 acceptance tests
- runtime tests
- replay tests
- live runtime tests

Verify:

CacheManager
TimelineService
EventBus
LiveRuntime
LiveSessionAdapter
ReplayRuntime
ReplayClock
ModeController
SnapshotEngine

remain correct.

=========================================================
STEP 17 — FULL REGRESSION
=========================================================

Run the broadest safe repository test suite.

At minimum include:

tests/api
tests/runtime
tests/integration/transport
tests/acceptance/live_streaming
tests/api/security
tests/api/ratelimit
tests/api/hardening
tests/api/telemetry
tests/api/replay
tests/api/outbound
tests/api/subscriptions
tests/api/connection
tests/api/observability

plus:

Phase 10 acceptance

and all other relevant existing tests.

DO NOT delete tests.

DO NOT weaken tests.

DO NOT mark failing tests as expected without evidence.

=========================================================
STEP 18 — STATIC QUALITY
=========================================================

Run:

Ruff

mypy

using the repository's established configuration.

Both must be clean for the affected Phase 11 implementation.

If the repository uses a specific standard invocation, use it.

Do not weaken configuration to obtain a passing result.

=========================================================
STEP 19 — TEST COUNT CONSISTENCY
=========================================================

Record exact results.

Previous accepted evidence includes:

11.13:

22 transport integration tests

362 cumulative regression tests at that stage

11.14:

20 LIVE acceptance tests

382 cumulative regression tests at that stage

Do NOT assume the final number remains 382.

Run the tests and report the ACTUAL current number.

=========================================================
STEP 20 — PERFORMANCE EVIDENCE
=========================================================

Collect available acceptance measurements.

Potential metrics:

- connection setup
- authentication
- subscription
- telemetry throughput
- fanout
- queue depth
- drop rate
- coalescing
- reconnect
- recovery
- Runtime producer duration
- concurrent clients

Every local benchmark must be identified:

BASELINE_NOT_PRODUCTION_SLA

No production SLA may be invented.

=========================================================
STEP 21 — SECURITY FINAL CHECK
=========================================================

Perform a final source/test audit for accidental leakage.

Search for:

- tokens in logs
- credentials in logs
- Authorization header logging
- secret values in errors
- stack traces returned to clients
- filesystem paths in errors
- connection/session identifiers used as uncontrolled metric labels

Verify errors remain sanitized.

Verify auth failure is fail-closed.

Verify authorization failure is fail-closed.

=========================================================
STEP 22 — DOCUMENTATION RECONCILIATION
=========================================================

Verify all Phase 11 specifications exist and agree.

Expected specifications include:

LiveTelemetryStreamingSpecification.md
RateLimitingAbuseProtectionSpecification.md
TransportHardeningSpecification.md
ReplayStreamingSpecification.md
OutboundBackpressureRateControlSpecification.md
SubscriptionSystemSpecification.md
ConnectionSessionManagementSpecification.md
TransportObservabilitySpecification.md
TransportIntegrationTestingSpecification.md
LiveStreamingAcceptanceSpecification.md

Create:

docs/specifications/Phase11AcceptanceSpecification.md

Update:

docs/Roadmap.md
Architecture documentation
Streaming documentation
API README
specification index
integration README
acceptance README

Documentation MUST clearly show:

11.10 SUPERSEDED / SATISFIED BY 11.7.1

11.11 SUPERSEDED / SATISFIED BY 11.6

=========================================================
STEP 23 — ROADMAP DECISION
=========================================================

If every applicable acceptance gate passes:

Mark:

PHASE 11 — ACCEPTED

and:

11.15 — ACCEPTED

Then identify:

PHASE 12 — UNITY INTEGRATION & 3D SCENE RUNTIME

as the next phase.

If a blocking gate fails:

DO NOT mark Phase 11 accepted.

Report:

- failed gate
- evidence
- owning component
- severity
- whether it requires a new agent or correction
- impact on Phase 12

=========================================================
FINAL ACCEPTANCE GATES
=========================================================

GATE-01  Phase 11 specification audit
GATE-02  Roadmap audit
GATE-03  Architecture audit
GATE-04  Agent 11.6 evidence
GATE-05  Agent 11.6.1 evidence
GATE-06  Agent 11.6.2 evidence
GATE-07  Agent 11.6.3 evidence
GATE-08  Agent 11.7 evidence
GATE-09  Agent 11.7.1 evidence
GATE-10  Agent 11.8 evidence
GATE-11  Agent 11.9 evidence
GATE-12  11.10 supersession verified
GATE-13  11.11 supersession verified
GATE-14  Agent 11.12 evidence
GATE-15  Agent 11.13 evidence
GATE-16  Agent 11.14 evidence

GATE-17  REST authentication
GATE-18  REST authorization
GATE-19  REST rate limiting
GATE-20  REST hardening

GATE-21  WS authentication
GATE-22  WS authorization
GATE-23  WS rate limiting
GATE-24  WS hardening
GATE-25  WS lifecycle
GATE-26  WS heartbeat
GATE-27  WS cleanup
GATE-28  WS reconnect

GATE-29  LIVE telemetry
GATE-30  LIVE events
GATE-31  LIVE snapshots
GATE-32  LIVE session isolation
GATE-33  LIVE fanout
GATE-34  LIVE concurrency
GATE-35  LIVE slow-client isolation

GATE-36  REPLAY telemetry
GATE-37  REPLAY events
GATE-38  REPLAY isolation
GATE-39  ReplayClock authority

GATE-40  Subscription lifecycle
GATE-41  Subscription quotas
GATE-42  Subscription isolation

GATE-43  Outbound queue bounds
GATE-44  Outbound rate control
GATE-45  Outbound backpressure
GATE-46  Backpressure recovery
GATE-47  Peer-client protection
GATE-48  Runtime non-blocking

GATE-49  Source sequence preservation
GATE-50  Transport sequence separation
GATE-51  Canonical telemetry integrity
GATE-52  Timing-authority preservation

GATE-53  Connection metrics
GATE-54  Streaming metrics
GATE-55  Security metrics
GATE-56  Rate-limit metrics
GATE-57  Backpressure metrics
GATE-58  Observability aggregation

GATE-59  Transport integration tests
GATE-60  LIVE acceptance tests
GATE-61  Phase 10 regression
GATE-62  Full API regression
GATE-63  Full runtime regression
GATE-64  Full integration regression

GATE-65  Disconnect/reconnect
GATE-66  Resource cleanup
GATE-67  Shutdown
GATE-68  Error sanitization
GATE-69  Secret protection
GATE-70  No duplicate subsystem

GATE-71  Ruff clean
GATE-72  mypy clean
GATE-73  Documentation consistency
GATE-74  Roadmap consistency
GATE-75  Performance evidence documented
GATE-76  BASELINE_NOT_PRODUCTION_SLA designation

GATE-77  Phase 11 architectural invariants
GATE-78  Phase 10 remains authoritative
GATE-79  Runtime remains identity-unaware
GATE-80  Transport remains timing-unaware

GATE-81  No unresolved blocking defect
GATE-82  Phase 11 readiness decision
GATE-83  Phase 12 handoff readiness

=========================================================
MANDATORY FINAL REPORT
=========================================================

Return the following sections:

1. STATUS

2. FINAL ACCEPTANCE DECISION

3. Executive Summary

4. Phase 11 Scope

5. Agent Acceptance Matrix

6. Architecture Verification

7. Runtime Boundary Verification

8. REST Verification

9. WebSocket Verification

10. Authentication Verification

11. Authorization Verification

12. Rate Limiting Verification

13. Hardening Verification

14. LIVE Streaming Verification

15. REPLAY Streaming Verification

16. Subscription Verification

17. Connection/Session Verification

18. Outbound Backpressure Verification

19. Observability Verification

20. Integration Testing Verification

21. LIVE Acceptance Verification

22. Disconnect/Reconnect Verification

23. Shutdown Verification

24. Session Isolation Verification

25. LIVE/REPLAY Isolation Verification

26. Telemetry Integrity Verification

27. Sequence Verification

28. Timing Authority Verification

29. Slow Client / Peer Protection

30. Runtime Non-Blocking Verification

31. Security Verification

32. Resource Leak Verification

33. Performance Evidence

34. Benchmark Designation

35. Exact Test Results

36. Full Regression Results

37. Ruff Results

38. mypy Results

39. Acceptance Gates GATE-01…83

40. Failed Gates, if any

41. Known Limitations

42. Known Risks

43. Technical Debt

44. Documentation Verification

45. Roadmap Verification

46. Phase 11 Production Readiness Assessment

47. Phase 12 Readiness Assessment

48. Final Acceptance Decision

49. Files Created

50. Files Modified

51. Recommended Next Phase

=========================================================
ACCEPTANCE DECISION RULE
=========================================================

PHASE 11 MAY BE MARKED ACCEPTED ONLY IF:

- all blocking gates PASS
- Phase 10 remains green
- Phase 11 integration remains green
- LIVE acceptance remains green
- security remains green
- REST remains green
- WS remains green
- isolation remains green
- reconnect remains green
- backpressure remains bounded
- Runtime remains non-blocking
- observability remains functional
- no duplicate subsystem exists
- Ruff is clean
- mypy is clean
- documentation is consistent
- roadmap is consistent
- no unresolved blocking defect exists

Performance results must NOT be interpreted as production capacity.

Use:

BASELINE_NOT_PRODUCTION_SLA

for local performance evidence.

=========================================================
DEFECT HANDLING
=========================================================

If a real defect is discovered:

DO NOT:

- weaken a test
- delete a test
- bypass the failing component
- create a duplicate subsystem
- silently change an accepted contract
- mark the gate PASS without evidence

Instead report:

DEFECT
OWNING COMPONENT
SEVERITY
REPRODUCTION
EXPECTED BEHAVIOR
ACTUAL BEHAVIOR
IMPACT
RECOMMENDED CORRECTION

If the correction is clearly minimal and architecture-preserving, it may
be implemented and retested.

If the correction expands Phase 11 scope materially:

STOP.

Do not silently redesign the architecture.

=========================================================
PHASE 12 HANDOFF CRITERIA
=========================================================

If Phase 11 is ACCEPTED, explicitly verify that Phase 12 can consume:

LIVE telemetry
REPLAY telemetry
events
snapshots
session state
connection state
transport observability

through the established transport contracts.

Phase 12 MUST NOT need to know:

- authentication internals
- rate limiter internals
- outbound queue internals
- connection manager internals
- EventBus implementation details
- Runtime identity/security concepts

The transport boundary must remain the consumer-facing contract.

=========================================================
START
=========================================================

FIRST:
Audit all Phase 11 agents and accepted evidence.

SECOND:
Verify architectural ownership and superseded agents.

THIRD:
Run Phase 11 integration and acceptance suites.

FOURTH:
Run Phase 10 regression.

FIFTH:
Run full relevant regression.

SIXTH:
Run Ruff.

SEVENTH:
Run mypy.

EIGHTH:
Reconcile documentation and roadmap.

NINTH:
Evaluate GATE-01 through GATE-83.

TENTH:
Produce the mandatory final report.

ELEVENTH:
If all blocking gates pass, formally mark:

PHASE 11 — ACCEPTED

and:

11.15 — ACCEPTED

Then identify:

PHASE 12 — UNITY INTEGRATION & 3D SCENE RUNTIME

as the next phase.

DO NOT START PHASE 12 IMPLEMENTATION.

THIS AGENT ONLY ACCEPTS PHASE 11 AND PREPARES THE HANDOFF.

=========================================================
END AGENT 11.15
=========================================================
```

## Assistant

**Phase 11 is officially ACCEPTED.** The Agent 11.15 report confirms **83/83 acceptance gates passed**, with **382 tests passing**, Ruff clean, and mypy clean. fileciteturn0file0L259-L276

The final state is:

- **11.6–11.9:** ACCEPTED
- **11.10:** superseded by 11.7.1
- **11.11:** superseded by 11.6
- **11.12–11.15:** ACCEPTED
- **Phase 11:** **ACCEPTED**
- **Phase 12:** ready to begin, but **not started**. fileciteturn0file0L28-L45

The most important architectural constraint going forward is that **Phase 12 must consume the published Phase 11 transport contracts and must not reach into authentication, rate limiting, outbound queues, connection-manager internals, EventBus internals, or Runtime identity/security internals.** fileciteturn0file0L325-L340

Also, the performance results remain correctly classified as **`BASELINE_NOT_PRODUCTION_SLA`**, so we have not accidentally declared the current local concurrency numbers to be production capacity. fileciteturn0file0L211-L219

### Next phase

**Phase 12 — Unity Integration & 3D Scene Runtime**

That is the correct next step. Phase 11 should now be treated as a **frozen/accepted transport boundary**, unless a genuine defect is discovered later. The Agent 11.15 report explicitly recommends Phase 12 and states that no Phase 12 implementation has started. fileciteturn0file0L337-L370

## User

So based on all chat logs "Please read and find out the previous logs/chats @Live F1 Tracking Data and @RaceVision F1 Project and @F1 Tracking and Project. Please learn and understand the logs and then I may ask you a question." We are on Phase 12.

Phase 12: Unity Integration & 3D Scene Runtime

Agent	Component
12.1	Unity Client Architecture
12.2	RaceVision WebSocket Client
12.3	Runtime State Synchronization
12.4	Track/Coordinate System
12.5	F1 Car Entity Runtime
12.6	Multi-Car Rendering
12.7	Vehicle Transform / Orientation
12.8	Track & Circuit Scene
12.9	Telemetry Visualization
12.10	Vehicle Effects
12.11	Replay/Live Unity Modes
12.12	Unity Performance
12.13	Unity Integration Testing
12.14	Phase 12 Acceptance

## Assistant

Yes. Based on the previous **Live F1 Tracking Data**, **RaceVision F1 Project**, and **F1 Tracking and Project** work, plus the completed Phase 10 and Phase 11 acceptance results, **we are now at Phase 12 — Unity Integration & 3D Scene Runtime**.

## Phase 12 — Unity Integration & 3D Scene Runtime

| Agent | Component | Purpose |
|---|---|---|
| **12.1** | Unity Client Architecture | Establish Unity-side architecture and boundaries |
| **12.2** | RaceVision WebSocket Client | Connect Unity to the Phase 11 transport |
| **12.3** | Runtime State Synchronization | Synchronize telemetry/runtime state into Unity |
| **12.4** | Track/Coordinate System | Establish authoritative coordinate conversion |
| **12.5** | F1 Car Entity Runtime | Create runtime vehicle entities |
| **12.6** | Multi-Car Rendering | Render and manage the complete field |
| **12.7** | Vehicle Transform / Orientation | Apply position, rotation and orientation correctly |
| **12.8** | Track & Circuit Scene | Build/load the circuit environment |
| **12.9** | Telemetry Visualization | Visualize live telemetry in the 3D runtime |
| **12.10** | Vehicle Effects | Wheels, lights, damage, smoke, effects, etc. |
| **12.11** | Replay/Live Unity Modes | Unity-side LIVE/REPLAY mode integration |
| **12.12** | Unity Performance | Rendering, update loops, batching, memory, frame-rate optimization |
| **12.13** | Unity Integration Testing | End-to-end Unity ↔ Phase 11 ↔ Phase 10 testing |
| **12.14** | Phase 12 Acceptance | Final Unity/3D acceptance gate |

### The critical architectural boundary

Phase 11 is now the **accepted transport boundary**:

```text
                    PHASE 10
              Runtime / EventBus
                     │
                     ▼
              ┌──────────────┐
              │   PHASE 11   │
              │   Transport  │
              └──────┬───────┘
                     │
              REST / WebSocket
                     │
                     ▼
              ┌──────────────┐
              │    PHASE 12  │
              │    Unity     │
              │  3D Runtime  │
              └──────────────┘
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Cars       Track      Cameras
          │          │          │
          └──────────┼──────────┘
                     ▼
              3D Visualization
```

**Unity should be a consumer of Phase 11, not another runtime authority.**

In particular, Phase 12 should **not** recreate:

- authentication
- authorization
- rate limiting
- subscription management
- WebSocket server logic
- outbound backpressure
- EventBus
- ReplayClock
- LiveSessionAdapter
- Runtime timing
- telemetry interpolation/delay authority

Those already have established ownership.

### Recommended implementation order

The order you've defined is good, and I would keep it:

**12.1 → 12.2 → 12.3 → 12.4 → 12.5 → 12.6 → 12.7 → 12.8 → 12.9 → 12.10 → 12.11 → 12.12 → 12.13 → 12.14**

There is one particularly important dependency chain:

```text
12.1 Unity Architecture
        ↓
12.2 WebSocket Client
        ↓
12.3 State Synchronization
        ↓
12.4 Coordinate System
        ↓
12.5 Car Entity Runtime
        ↓
12.6 Multi-Car Rendering
        ↓
12.7 Transform / Orientation
        ↓
12.8 Circuit Scene
        ↓
12.9 Telemetry Visualization
        ↓
12.10 Effects
        ↓
12.11 Live / Replay
        ↓
12.12 Performance
        ↓
12.13 Integration Testing
        ↓
12.14 Acceptance
```

**12.4 is especially important.** Before we start throwing cars into a Unity scene, we need an authoritative answer for how the telemetry coordinate system maps into Unity world space. Otherwise, later work on car positioning, orientation, track geometry, cameras and replay can all end up needing to be rewritten.

And **12.2/12.3 should establish the data pipeline before rendering logic gets involved**:

```text
Phase 11 WebSocket
       ↓
Unity WebSocket Client
       ↓
Transport Envelope
       ↓
Telemetry/Event Decoder
       ↓
Runtime State Model
       ↓
Car/Track/Session State
       ↓
Rendering
```

That preserves the same architectural principle we've maintained throughout RaceVision:

> **Data acquisition → Runtime → Transport → Consumer → Rendering**

rather than coupling Unity directly to the backend internals.

So yes — **Phase 11 is closed, Phase 12 is the current active phase, and Agent 12.1 is the correct next implementation agent.**

## User

Please tell me what next for Phase 12 and Agent information

## Assistant

Yes. Based on the architecture and the Phase 11 completion state, **Phase 12 should now begin with Agent 12.1 — Unity Client Architecture**.

## Phase 12 — Unity Integration & 3D Scene Runtime

### Overall objective

Phase 12 takes the already-validated Phase 10 runtime data and the accepted Phase 11 transport boundary and turns it into a **real-time Unity 6 3D visualization runtime**.

The fundamental flow should remain:

```text
Phase 10 Runtime
      │
      ▼
Phase 11 Transport
      │
      │ WebSocket
      ▼
┌─────────────────────────────┐
│        UNITY CLIENT         │
│                             │
│  WebSocket Client           │
│        ↓                    │
│  Transport Decoder          │
│        ↓                    │
│  Runtime State Sync         │
│        ↓                    │
│  Coordinate Conversion      │
│        ↓                    │
│  Car / Track Entities       │
│        ↓                    │
│  Rendering / Effects        │
└─────────────────────────────┘
```

---

# Agent 12.1 — Unity Client Architecture

**This is the next agent.**

### Purpose

Establish the complete Unity-side architecture **before** implementing cars, tracks, effects or visualization.

It should define the boundaries between:

- WebSocket transport
- message decoding
- runtime state
- telemetry
- sessions
- LIVE/REPLAY modes
- coordinate systems
- entities
- rendering
- effects
- cameras
- future OBS/broadcast integration

### 12.1 should establish something like:

```text
Unity
│
├── Transport
│   └── RaceVision WebSocket Client
│
├── Protocol
│   ├── Envelope Decoder
│   ├── Telemetry Decoder
│   ├── Event Decoder
│   └── Snapshot Decoder
│
├── Runtime
│   ├── Session State
│   ├── Race State
│   ├── Car State
│   ├── Track State
│   └── Mode State
│
├── Synchronization
│   ├── State Buffer
│   ├── Sequence Handling
│   └── Update Application
│
├── Coordinate
│   ├── Telemetry → Unity
│   └── Track Coordinate Mapping
│
├── Entities
│   ├── Cars
│   ├── Track
│   └── Environment
│
├── Rendering
│   ├── Cars
│   ├── Track
│   ├── Telemetry
│   └── Effects
│
└── Presentation
    ├── Cameras
    ├── HUD
    └── Future Broadcast/OBS
```

### Critical 12.1 rules

12.1 should explicitly prevent Unity from becoming another backend runtime.

Unity **must not** become authoritative for:

- telemetry acquisition
- race timing
- replay timing
- delay
- interpolation policy
- authentication
- authorization
- subscriptions
- EventBus
- server-side session ownership

Unity consumes the established transport contracts.

---

# Agent 12.2 — RaceVision WebSocket Client

Once 12.1 is accepted:

### Purpose

Build the actual Unity WebSocket client against:

```text
WS /api/v1/ws
```

It should support the Phase 11 contract for:

- authentication
- connection lifecycle
- subscriptions
- telemetry
- events
- snapshots
- replay
- mode
- runtime status
- reconnect
- heartbeat handling

The important point is:

**Unity is a WebSocket client, not another transport implementation.**

---

# Agent 12.3 — Runtime State Synchronization

This converts transport messages into a coherent Unity-side state model.

```text
WebSocket
    ↓
Envelope
    ↓
Message
    ↓
State Synchronizer
    ↓
Unity Runtime State
```

It should handle:

- source sequences
- transport sequences
- session IDs
- timestamps
- LIVE/REPLAY mode
- telemetry state
- events
- snapshots

It should also avoid blindly applying stale/out-of-order state.

---

# Agent 12.4 — Track / Coordinate System

**This is a major architectural milestone.**

Define exactly how backend telemetry coordinates become Unity coordinates.

For example:

```text
Telemetry Coordinate Space
          ↓
RaceVision Coordinate Mapping
          ↓
Unity World Space
```

This needs to cover:

- X/Y/Z mapping
- units
- origin
- orientation
- handedness
- scale
- track origin
- rotation
- elevation
- heading

This should become the **single authoritative Unity coordinate conversion layer**.

---

# Agent 12.5 — F1 Car Entity Runtime

Create the runtime representation of an F1 car.

Conceptually:

```text
CarEntity
├── Driver
├── Team
├── Car
├── Session
├── Telemetry State
├── Transform
├── Visual Model
├── Effects
└── Runtime Status
```

The backend identity should remain separate from Unity's GameObject identity.

---

# Agent 12.6 — Multi-Car Rendering

Now move from one car to the complete field.

Requirements should include:

- multiple cars
- dynamic car creation/removal
- driver mapping
- team mapping
- independent telemetry
- session isolation
- efficient updates

This is where the project starts becoming the actual **live F1 3D visualization**.

---

# Agent 12.7 — Vehicle Transform / Orientation

Apply telemetry to:

```text
Position
Rotation
Heading
Pitch
Roll
```

while respecting the coordinate system established by 12.4.

This should **not invent vehicle physics**.

Telemetry-derived orientation is visualization data.

---

# Agent 12.8 — Track & Circuit Scene

Build the Unity circuit environment.

This should establish:

- track geometry
- world positioning
- pit lane
- start/finish
- sectors
- environment
- track metadata
- scenery hooks

The track must use the same coordinate mapping established in 12.4.

---

# Agent 12.9 — Telemetry Visualization

Add visual representations of telemetry.

Potential areas:

- speed
- throttle
- brake
- gear
- RPM
- DRS
- tyre state
- gaps
- sector state
- race position
- flags/events

The important distinction:

**Telemetry visualization ≠ telemetry authority.**

Unity displays the data supplied by the backend.

---

# Agent 12.10 — Vehicle Effects

Add presentation effects such as:

- tyre effects
- brake glow
- lights
- smoke
- sparks
- damage visualization
- exhaust/engine effects
- environmental interaction

These should be presentation systems and should not alter canonical telemetry.

---

# Agent 12.11 — Replay / Live Unity Modes

Connect Unity's presentation state to the Phase 10/11 modes.

```text
LIVE
  ↓
Live transport
  ↓
Unity LIVE presentation


REPLAY
  ↓
Replay transport
  ↓
Unity REPLAY presentation
```

Unity should **not own ReplayClock**.

The backend remains authoritative.

---

# Agent 12.12 — Unity Performance

Only after the complete rendering path exists should performance optimization happen.

Focus on:

- frame rate
- GC allocations
- GameObject count
- transform updates
- batching
- GPU load
- CPU load
- memory
- telemetry processing
- WebSocket processing
- multi-car scaling

Test realistic field sizes rather than optimizing a single car.

---

# Agent 12.13 — Unity Integration Testing

End-to-end verification:

```text
Phase 10
   ↓
Phase 11
   ↓
WebSocket
   ↓
Unity
   ↓
State
   ↓
Cars
   ↓
Track
   ↓
Rendering
```

Test:

- LIVE
- REPLAY
- multiple cars
- multiple sessions
- reconnect
- missing frames
- sequence handling
- session isolation
- mode changes
- performance
- shutdown

---

# Agent 12.14 — Phase 12 Acceptance

Final acceptance gate.

It should prove:

### Transport

✅ Unity connects to Phase 11

### State

✅ telemetry becomes coherent Unity state

### Coordinates

✅ cars occupy correct track locations

### Rendering

✅ complete field renders

### LIVE

✅ live telemetry works

### REPLAY

✅ replay works

### Isolation

✅ sessions/modes don't leak

### Performance

✅ acceptable Unity performance baseline

### Architecture

✅ Unity remains a consumer

### Regression

✅ Phase 10 + Phase 11 remain green

Then:

```text
PHASE 12 — ACCEPTED
```

and the project can move toward the next major stage.

---

# The immediate next step

We should **not jump straight into 12.2**.

The correct sequence starts:

```text
                    PHASE 12
                       │
                       ▼
                  ┌─────────┐
                  │  12.1   │
                  │ Unity   │
                  │ Client  │
                  │Architecture
                  └────┬────┘
                       │
                       ▼
                  ┌─────────┐
                  │  12.2   │
                  │WebSocket│
                  │ Client  │
                  └────┬────┘
                       │
                       ▼
                  ┌─────────┐
                  │  12.3   │
                  │ Runtime │
                  │  Sync   │
                  └────┬────┘
                       │
                       ▼
                  ┌─────────┐
                  │  12.4   │
                  │Coordinate│
                  │ System  │
                  └────┬────┘
                       │
                       ▼
                    ...
                       │
                       ▼
                  ┌─────────┐
                  │  12.14  │
                  │ ACCEPT  │
                  └─────────┘
```

**So the next command set I would give Cursor is Agent 12.1 — Unity Client Architecture.**

And because this is the first Unity-facing agent, I would make **12.1 particularly strict about the boundary between Phase 11 transport contracts and the Unity runtime**, so that we don't create architectural debt that later has to be removed.

## User

when do I start to use Blender to create the F1 Cars and Tracks, which Phase is that?

## Assistant

You should start using **Blender during Phase 12**, but **not at 12.1**.

For RaceVision, I would split Blender work across **Phase 12 and Phase 13/14**, with the actual asset-production work beginning once the Unity architecture and coordinate system are locked.

### Where Blender fits

| Phase | Blender involvement | What happens |
|---|---|---|
| **12.1** | 🟡 Planning | Define Unity/Blender asset pipeline and folder/contracts |
| **12.2** | 🟡 None/minimal | Establish Unity WebSocket client |
| **12.3** | 🟡 None | Runtime state synchronization |
| **12.4** | 🔴 **Critical** | **Lock coordinate system between telemetry → Blender → Unity** |
| **12.5** | 🟢 **Start** | Define F1 car asset requirements/prefabs |
| **12.6** | 🟢 **Yes** | **Begin producing F1 car models/assets in Blender** |
| **12.7** | 🟢 **Yes** | Validate car orientation/pivot/transform |
| **12.8** | 🟢 **Major** | **Build/prepare circuit and track assets in Blender** |
| **12.9** | 🟢 | Validate telemetry visualization against the 3D assets |
| **12.10** | 🟢 | Blender assets may support vehicle/effect geometry |
| **12.11** | 🟢 | Same assets work for LIVE + REPLAY |
| **12.12** | 🟢 | Optimize Blender-produced assets for Unity |
| **12.13** | 🟢 | End-to-end asset/runtime testing |
| **12.14** | 🟢 | Final acceptance |

### The important point: **12.4 comes first**

Before you model the cars and especially the track, we need to establish:

```text
F1 Telemetry Coordinates
        ↓
RaceVision Coordinate System
        ↓
Blender Coordinate System
        ↓
FBX/GLTF/etc.
        ↓
Unity Coordinate System
        ↓
Live Car Position
```

Otherwise you could spend a lot of time building a beautiful circuit and discover that the telemetry positions don't line up with it.

---

## When should you actually open Blender?

I'd say:

### **After Agent 12.4 is ACCEPTED**

Then we can start the real asset-production workflow.

The first practical Blender milestone would be:

**12.5/12.6 — F1 Car Asset Pipeline**

For example:

```text
Blender
   │
   ├── F1 Car Base Model
   ├── Wheels
   ├── Front Wing
   ├── Rear Wing
   ├── Halo
   ├── Driver
   ├── Materials
   ├── Team Livery
   └── LODs
        │
        ▼
   Export
        │
        ▼
     Unity
        │
        ▼
   RaceVisionCar
        │
        ▼
   Live Telemetry
```

Then the track:

```text
Blender
   │
   ├── Circuit Geometry
   ├── Kerbs
   ├── Runoff
   ├── Barriers
   ├── Pit Lane
   ├── Buildings
   ├── Grandstands
   ├── Trackside Objects
   └── Environment
        │
        ▼
      Export
        │
        ▼
      Unity
        │
        ▼
   RaceVision Circuit
```

### One thing I would change from the original Phase 12 plan

I would **not wait until 12.8 to begin all track work**.

12.4 should establish the coordinate system, then **track asset production can begin in parallel with 12.5–12.7**.

So practically:

```text
12.1  Unity architecture
  ↓
12.2  WebSocket
  ↓
12.3  State sync
  ↓
12.4  ★ COORDINATE SYSTEM LOCKED
  │
  ├───────────────┐
  ▼               ▼
12.5/12.6      Blender Asset Pipeline
F1 Cars        ├── Cars
  │            ├── Track
  ▼            └── Environment
12.7               │
Transforms         ▼
  │              Unity
  └───────┬────────┘
          ▼
       12.8+
```

So **Blender becomes a real production tool immediately after 12.4**, with the car work around **12.5/12.6** and the circuit work around **12.8**, while asset creation can proceed in parallel.

And since you already have **Blender 4.1.1**, that fits directly into the planned RaceVision pipeline.

**Bottom line: start planning Blender in 12.1, lock the coordinate/asset contract in 12.4, and start actual F1 car + track modelling immediately after 12.4.**

## User

Please give commands for Agent 12.1 Unity Client Architecture	Establish Unity-side architecture and boundaries ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. Below is the **Cursor-ready Agent 12.1 command**. It is deliberately scoped so Cursor establishes the Unity architecture and boundaries **without prematurely implementing the WebSocket client, telemetry synchronization, cars, tracks, or Blender assets**.

Copy the entire block into Cursor Agent mode:

```text
You are Agent 12.1 — Unity Client Architecture for the RaceVision project.

============================================================
RACEVISION — PHASE 12
AGENT 12.1 — UNITY CLIENT ARCHITECTURE
============================================================

ROLE
------------------------------------------------------------
You are a Principal Unity Software Architect working on the
RaceVision F1 live 3D visualization system.

Your task is to implement Agent 12.1:

    Unity Client Architecture

Purpose:

    Establish the complete Unity-side architecture, module
    boundaries, lifecycle, contracts, dependency direction,
    project structure, configuration boundaries, and extension
    points required for Phase 12.

IMPORTANT:
This agent establishes architecture and foundations only.

DO NOT implement the full WebSocket client.
DO NOT implement telemetry synchronization.
DO NOT implement F1 car rendering.
DO NOT implement multi-car rendering.
DO NOT implement track rendering.
DO NOT implement Blender assets.
DO NOT implement vehicle effects.
DO NOT implement cameras/director systems.
DO NOT implement OBS integration.
DO NOT implement Phase 12 performance optimization.
DO NOT modify Phase 10 Runtime architecture.
DO NOT modify Phase 11 transport architecture.

Those belong to later agents.

============================================================
1. FIRST — READ AND UNDERSTAND THE EXISTING PROJECT
============================================================

Before changing anything, inspect the repository thoroughly.

Read and understand:

- docs/
- docs/specifications/
- docs/architecture/
- docs/Roadmap.md
- backend/
- backend/api/
- backend/runtime/
- backend/streaming/
- backend/protocols/
- shared/
- Unity/
- existing Unity project files
- existing Unity README/documentation
- Phase 10 specifications
- Phase 11 specifications
- LiveTelemetryStreamingSpecification
- ReplayStreamingSpecification
- SubscriptionSystemSpecification
- ConnectionSessionManagementSpecification
- OutboundBackpressureRateControlSpecification
- TransportObservabilitySpecification
- TransportIntegrationTestingSpecification
- LiveStreamingAcceptanceSpecification
- Phase 11 Acceptance documentation

Also inspect the existing Git history/status where useful.

Do NOT assume the repository is empty.

Preserve existing architecture and implementation.

============================================================
2. ESTABLISHED ARCHITECTURE — MUST BE RESPECTED
============================================================

Phase 10 is the authoritative Runtime.

Phase 11 is the authoritative REST/WebSocket transport boundary.

Unity is a CLIENT / CONSUMER.

The architectural direction is:

    Phase 10 Runtime
          |
          v
    Phase 11 Transport
          |
          | WebSocket / REST
          v
    Unity Client
          |
          v
    Unity Runtime State
          |
          v
    3D Presentation

Unity MUST NOT become another backend Runtime.

Unity MUST NOT become authoritative for:

- telemetry acquisition
- telemetry normalization
- race timing
- ReplayClock
- replay seeking
- replay playback authority
- server-side delay
- server-side interpolation
- EventBus
- backend subscriptions
- backend authentication
- backend authorization
- backend rate limiting
- outbound backpressure
- backend session ownership
- canonical telemetry sequences

Unity consumes the published Phase 11 contracts.

============================================================
3. ARCHITECTURAL PRINCIPLE
============================================================

Establish a clean dependency direction:

    Transport
       ↓
    Protocol
       ↓
    Synchronization
       ↓
    Runtime State
       ↓
    Domain / Entities
       ↓
    Presentation
       ↓
    Effects / Cameras / UI

Do NOT allow:

    Presentation → Backend internals
    Car renderer → WebSocket
    Track renderer → WebSocket
    Effects → Transport
    GameObject → Phase 10 Runtime
    Unity scene objects → backend services

Transport must remain replaceable.

Rendering must remain replaceable.

Runtime state must be independent of GameObjects where practical.

============================================================
4. UNITY ARCHITECTURE TO ESTABLISH
============================================================

Create or reconcile the Unity architecture around these logical
boundaries:

    Unity/
    └── RaceVision/
        ├── Runtime/
        │   ├── Bootstrap/
        │   ├── Configuration/
        │   ├── Lifecycle/
        │   ├── State/
        │   ├── Sessions/
        │   ├── Modes/
        │   └── Services/
        │
        ├── Transport/
        │   ├── Contracts/
        │   ├── Connection/
        │   ├── Messages/
        │   └── Serialization/
        │
        ├── Synchronization/
        │   ├── State/
        │   ├── Sequences/
        │   ├── Sessions/
        │   └── Modes/
        │
        ├── Domain/
        │   ├── Cars/
        │   ├── Drivers/
        │   ├── Teams/
        │   ├── Tracks/
        │   └── Race/
        │
        ├── CoordinateSystem/
        │
        ├── Presentation/
        │   ├── Cars/
        │   ├── Track/
        │   ├── Telemetry/
        │   ├── Effects/
        │   └── UI/
        │
        ├── Scenes/
        ├── Prefabs/
        ├── Materials/
        ├── Shaders/
        ├── Resources/
        └── Tests/

IMPORTANT:

If an existing Unity structure already provides equivalent
boundaries, REUSE/RECONCILE it rather than creating duplicates.

Do not create arbitrary duplicate systems.

============================================================
5. CORE UNITY COMPONENTS
============================================================

Establish interfaces/contracts for the following conceptual
components.

A. Application Bootstrap

Responsible for:

- Unity startup
- dependency composition
- service initialization
- shutdown
- lifecycle ownership

B. Client Runtime

Responsible for:

- client-side runtime lifecycle
- active session
- active mode
- state availability
- coordination of Unity systems

C. Transport Abstraction

Define an abstraction for transport.

For example conceptually:

    IRaceVisionTransport

It must NOT expose backend implementation details.

It should eventually support:

- connect
- disconnect
- send
- receive
- connection state

The actual WebSocket implementation belongs to Agent 12.2.

Caution:

Do NOT implement 12.2 here.

D. Protocol Boundary

Establish a boundary between:

    transport envelope
             ↓
       decoded message
             ↓
       Unity domain state

Protocol models should remain independent from GameObjects.

E. Runtime State

Create a foundation for state such as:

- session state
- operating mode
- race state
- car state
- track state
- telemetry state
- connection state

Do not implement the complete telemetry state model yet.

That belongs primarily to Agent 12.3.

F. Synchronization Boundary

Define where transport messages become Unity runtime state.

Create interfaces/contracts only where implementation belongs
to later agents.

G. Presentation Boundary

Rendering systems consume state.

Rendering systems MUST NOT directly consume raw WebSocket
messages.

============================================================
6. LIVE / REPLAY ARCHITECTURE
============================================================

Unity must explicitly support:

    LIVE
    REPLAY

without creating separate duplicated runtimes.

Use a shared client architecture.

Conceptually:

    Transport
       ↓
    Message
       ↓
    Runtime State
       ↓
    Mode
       ├── LIVE presentation
       └── REPLAY presentation

Do not implement ReplayClock.

Do not create a Unity replay timing authority.

Phase 10 remains authoritative.

============================================================
7. SESSION ARCHITECTURE
============================================================

Unity must preserve the distinction between:

    connection_id
    principal
    session_id
    subscription_id
    source sequence
    transport sequence

Do NOT collapse these identities.

Unity should maintain a client-side session context without
inventing backend session ownership.

Session isolation must remain enforced by the backend transport.

============================================================
8. SEQUENCE / ORDERING BOUNDARY
============================================================

Establish architectural support for:

- transport sequence
- source sequence
- timestamp
- session_id
- operating mode

Do NOT reorder canonical telemetry here.

Do NOT extrapolate telemetry here.

Do NOT interpolate telemetry here.

Do NOT invent missing frames here.

Those responsibilities remain governed by the existing backend
runtime/transport contracts.

Agent 12.3 may later implement client-side state application
according to the established contracts.

============================================================
9. CONFIGURATION
============================================================

Establish a Unity configuration boundary.

Configuration must support future values such as:

- backend base URL
- WebSocket URL
- environment
- authentication configuration
- session configuration
- logging level
- telemetry options
- reconnect options

DO NOT hard-code production URLs throughout the Unity code.

DO NOT embed secrets in source code.

Do not implement full authentication logic here.

============================================================
10. ENVIRONMENT SEPARATION
============================================================

Provide a clean conceptual separation for:

    Development
    Test
    Staging
    Production

Unity should be able to switch endpoint configuration without
modifying source code.

Avoid Unity-specific configuration becoming coupled to backend
implementation.

============================================================
11. UNITY LIFECYCLE
============================================================

Define lifecycle states sufficient for the Phase 12 client.

For example:

    INITIALIZING
    READY
    CONNECTING
    CONNECTED
    RUNNING
    RECONNECTING
    STOPPING
    STOPPED
    FAULTED

Use the project's existing conventions if already present.

Do not duplicate lifecycle ownership.

Application lifecycle must remain separate from WebSocket
connection lifecycle.

============================================================
12. DEPENDENCY INJECTION / SERVICE OWNERSHIP
============================================================

Establish a clear ownership model.

There must be one authoritative owner for each Unity service.

Avoid:

- static global state where unnecessary
- hidden singletons
- duplicate managers
- renderer-owned networking
- scene-specific networking
- GameObject-specific transport clients

If Unity-native MonoBehaviour composition is appropriate,
use it deliberately.

Keep domain/state services testable without requiring a rendered
scene wherever practical.

============================================================
13. SCRIPTABLEOBJECTS
============================================================

If ScriptableObjects are used, use them for appropriate
configuration/static data rather than mutable authoritative
runtime state.

Good candidates:

- environment configuration
- track metadata
- car visual configuration
- team visual configuration
- rendering configuration

Do NOT use ScriptableObjects as an uncontrolled global mutable
runtime database.

============================================================
14. SCENE ARCHITECTURE
============================================================

Establish a future-ready scene structure.

Do not build the complete track yet.

Define the architectural separation between:

    Bootstrap Scene
    Race Scene
    UI
    Presentation
    Cameras

If the existing Unity project already has scenes, reconcile
instead of duplicating.

The architecture must permit future:

- circuit loading
- multiple camera views
- broadcast camera
- spectator camera
- replay camera
- VR
- OBS/broadcast output

without coupling these systems to transport.

============================================================
15. PREFAB ARCHITECTURE
============================================================

Establish conventions for future:

    Car Prefab
    Track Prefab
    Camera Prefab
    Effect Prefab
    UI Prefab

Do NOT create finished F1 cars or tracks in this agent.

Blender asset production begins after the coordinate system
and asset contracts are established in Agent 12.4.

============================================================
16. BLENDER BOUNDARY
============================================================

Document the future asset pipeline:

    Blender
       ↓
    Exported Asset
       ↓
    Unity Import
       ↓
    Unity Prefab
       ↓
    Runtime Entity
       ↓
    Telemetry-driven Transform

Do not create the actual F1 models or circuits yet.

Do not invent the coordinate mapping yet.

Agent 12.4 owns the authoritative coordinate-system contract.

============================================================
17. LOGGING
============================================================

Establish Unity-side structured logging boundaries.

Logging must support:

- startup
- shutdown
- transport lifecycle
- synchronization errors
- protocol errors
- state errors
- rendering errors

Do NOT log:

- access tokens
- credentials
- secrets
- authorization headers
- sensitive session information unnecessarily

Avoid excessive per-frame logging.

Telemetry-frame logging must be disabled or controlled by
configuration.

============================================================
18. ERROR BOUNDARY
============================================================

Define distinct categories for:

    Transport errors
    Protocol errors
    Authentication errors
    Authorization errors
    Synchronization errors
    State errors
    Presentation errors
    Configuration errors

Do not leak backend implementation details into rendering code.

Do not make presentation failures terminate the entire transport
runtime unless explicitly required.

============================================================
19. TEST ARCHITECTURE
============================================================

Establish Unity test boundaries for future agents.

At minimum provide conceptual separation for:

    EditMode tests
    PlayMode tests
    Runtime state tests
    Transport contract tests
    Synchronization tests
    Coordinate tests
    Presentation tests
    Integration tests

Do not build the full Phase 12 integration suite yet.

That belongs to Agent 12.13.

============================================================
20. PERFORMANCE ARCHITECTURE
============================================================

Do NOT prematurely optimize.

However, architecture must avoid obvious future problems:

- one WebSocket per car
- one update loop per car
- network logic inside Update() everywhere
- allocations for every telemetry frame
- renderer polling the network
- duplicated telemetry state
- uncontrolled GameObject creation

Prefer:

    one transport connection
    one synchronization pipeline
    centralized state application
    presentation consuming state

Agent 12.12 owns detailed performance optimization.

============================================================
21. THREADING / MAIN THREAD
============================================================

Establish a clear rule:

Network I/O and decoding must not unnecessarily block Unity's
main rendering thread.

Unity scene/GameObject manipulation must occur through the
appropriate Unity main-thread boundary.

Do not implement the complete threading/WebSocket solution yet.

Agent 12.2 owns the transport implementation.

============================================================
22. ASSEMBLY / MODULE BOUNDARIES
============================================================

If appropriate for the existing Unity project, establish
assembly definitions or equivalent module boundaries.

Suggested conceptual boundaries:

    RaceVision.Core
    RaceVision.Transport
    RaceVision.Protocol
    RaceVision.Runtime
    RaceVision.Domain
    RaceVision.Presentation
    RaceVision.Tests

Do not force assembly definitions if the existing project has
a better established convention.

The important requirement is dependency direction.

Presentation must not own transport.

Domain must not depend on rendering.

============================================================
23. DOCUMENTATION
============================================================

Create/update:

    docs/specifications/UnityClientArchitectureSpecification.md

Document:

- architecture
- component boundaries
- dependency direction
- lifecycle
- transport boundary
- protocol boundary
- runtime state boundary
- LIVE/REPLAY model
- session identity rules
- configuration
- scene structure
- prefab conventions
- Blender boundary
- testing strategy
- performance principles
- security boundaries
- future Agent responsibilities

Update:

- docs/Roadmap.md
- architecture documentation
- Unity README/documentation
- specifications index

Clearly mark:

    Agent 12.1 — ACCEPTED

only after all required verification passes.

============================================================
24. AGENT OWNERSHIP MAP
============================================================

Document these ownership boundaries:

12.1
    Unity architecture and boundaries

12.2
    RaceVision WebSocket client

12.3
    Runtime state synchronization

12.4
    Track/coordinate system

12.5
    F1 car entity runtime

12.6
    Multi-car rendering

12.7
    Vehicle transform/orientation

12.8
    Track/circuit scene

12.9
    Telemetry visualization

12.10
    Vehicle effects

12.11
    Unity LIVE/REPLAY modes

12.12
    Unity performance

12.13
    Unity integration testing

12.14
    Phase 12 acceptance

Do not implement another agent's responsibility.

============================================================
25. BACKEND PROTECTION RULE
============================================================

This agent must NOT modify Phase 10 Runtime behavior.

This agent must NOT modify:

    backend/runtime/
    EventBus semantics
    ReplayClock
    LiveSessionAdapter behavior
    telemetry normalization
    interpolation authority
    delay authority

Do not modify Phase 11 transport ownership.

Do not create another:

    WebSocket server
    subscription system
    authentication system
    authorization system
    rate limiter
    backpressure system
    connection manager

Unity is strictly the consumer.

============================================================
26. REQUIRED ACCEPTANCE CRITERIA
============================================================

Agent 12.1 is successful only if:

GATE-01
Unity project structure is understood and documented.

GATE-02
Unity architecture has clear module boundaries.

GATE-03
Transport is abstracted from rendering.

GATE-04
Protocol is abstracted from GameObjects.

GATE-05
Runtime state is separated from presentation.

GATE-06
LIVE and REPLAY share the same Unity architecture.

GATE-07
Session/connection/subscription/source-sequence identities
remain distinct.

GATE-08
Unity does not become a second Runtime authority.

GATE-09
Unity does not implement backend security systems.

GATE-10
Configuration is environment-aware.

GATE-11
Lifecycle ownership is explicit.

GATE-12
Scene/prefab architecture is documented.

GATE-13
Blender → Unity asset pipeline boundary is documented.

GATE-14
Coordinate-system ownership is explicitly reserved for 12.4.

GATE-15
Testing boundaries are defined.

GATE-16
Future WebSocket implementation can be added by 12.2 without
architectural refactoring.

GATE-17
Future state synchronization can be added by 12.3 without
coupling to rendering.

GATE-18
Future cars/tracks can be added without changing transport.

GATE-19
No duplicate transport/runtime/security systems are introduced.

GATE-20
Existing Phase 10 + Phase 11 tests remain green.

============================================================
27. VERIFICATION
============================================================

Before declaring completion:

1. Inspect all changed files.
2. Verify no duplicate architecture was introduced.
3. Verify Unity compiles.
4. Run available Unity EditMode tests.
5. Run available Unity PlayMode tests if configured.
6. Run backend regression tests relevant to Phase 10/11.
7. Run lint/static analysis where configured.
8. Verify documentation consistency.
9. Verify Git diff.
10. Verify no secrets were introduced.
11. Verify no Phase 10 behavior changed.
12. Verify no Phase 11 ownership was duplicated.

Do not claim tests were run if they were not actually run.

============================================================
28. IMPORTANT — DO NOT OVER-IMPLEMENT
============================================================

This is an architecture/foundation agent.

If a later requirement is tempting to implement, STOP and document
the extension point instead.

Specifically do NOT implement:

- WebSocket networking implementation
- telemetry parser implementation
- telemetry state application
- car GameObjects
- F1 models
- track models
- Blender models
- coordinate conversion implementation
- vehicle transform implementation
- telemetry HUD
- vehicle effects
- replay controller
- camera director
- OBS integration
- VR integration
- performance optimization

Those belong to later agents.

============================================================
29. FINAL REPORT FORMAT
============================================================

When finished, report:

1. STATUS
   ACCEPTED / NOT ACCEPTED

2. Architecture implemented

3. Existing architecture reused

4. New Unity modules/files

5. Dependency boundaries

6. Lifecycle model

7. Transport boundary

8. Runtime state boundary

9. LIVE/REPLAY boundary

10. Session/identity rules

11. Configuration architecture

12. Scene/prefab architecture

13. Blender asset boundary

14. Testing architecture

15. Documentation updated

16. Files created

17. Files modified

18. Tests executed with EXACT results

19. Static analysis with EXACT results

20. Acceptance gates GATE-01…20

21. Limitations

22. Deferred work for Agent 12.2

23. Recommended next Agent

============================================================
30. FINAL RULE
============================================================

Do not proceed to Agent 12.2 automatically.

Finish Agent 12.1 only.

Return the complete implementation/verification report so the
next agent can be started independently.

============================================================
START AGENT 12.1 NOW
============================================================
```

### What I want Cursor to achieve with 12.1

The key outcome is **not a fancy Unity scene yet**. It is this clean foundation:

```text
                    RACEVISION

              ┌──────────────────┐
              │ Phase 11 Backend │
              │ Transport        │
              └────────┬─────────┘
                       │
                 WebSocket
                       │
                       ▼
              ┌──────────────────┐
              │ 12.2 Transport   │
              │ Client            │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ 12.3 State Sync  │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Unity Runtime     │
              │ State             │
              └────────┬─────────┘
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
       Domain Entities      Coordinate System
             │                   │
             └─────────┬─────────┘
                       ▼
              ┌──────────────────┐
              │   Presentation   │
              │ Cars / Track /   │
              │ Telemetry / FX   │
              └──────────────────┘
```

**Do not let Cursor start modelling cars or tracks in 12.1.** We deliberately reserve the authoritative coordinate and asset contract for **12.4**, after which we can start the serious Blender → Unity pipeline.

## User

## 1. STATUS

**ACCEPTED**

Agent 12.1 establishes Unity client architecture only. No WebSocket/telemetry/cars/tracks implemented. Changes left uncommitted.

---

## 2. Architecture implemented

Consumer-side layered client under `unity/Assets/RaceVision/` with multi-assembly boundaries enforcing:

`Transport → Protocol → Synchronization → Runtime State → Domain → Presentation`

Unity remains a Phase 11 contract consumer; Phase 10 stays Runtime authority.

---

## 3. Existing architecture reused

Reused repo placeholders: `unity/`, `docs/Unity.md`, `rendering/unity/`, `tests/unity/`. Did **not** create a second Unity root or duplicate backend transport/runtime systems. No `backend/` or `shared/` modifications.

---

## 4. New Unity modules/files

Assemblies: Core, Domain, Protocol, Transport, Synchronization, Runtime, CoordinateSystem, Presentation, Tests.EditMode, Tests.PlayMode.

Foundations: identity types, lifecycle/mode enums, error/logging, `IRaceVisionTransport` (+ null stub), protocol decode boundary, `IStateSynchronizer` (unimplemented), config ScriptableObject, `ClientCompositionRoot` / `ClientRuntimeHost`, domain IDs, presenter interfaces, EditMode smoke tests.

---

## 5. Dependency boundaries

| Rule                            | Enforced by                |
| ------------------------------- | -------------------------- |
| Presentation ↛ Transport        | asmdef refs                |
| Domain ↛ Presentation/Transport | asmdef refs                |
| Core/Domain/Protocol pure       | `noEngineReferences: true` |
| CoordinateSystem reserved       | stub assembly for 12.4     |

---

## 6. Lifecycle model

- App: `ClientLifecycleState` (Initializing…Faulted)
- Transport: `TransportConnectionState` (separate)
- Host: `ClientRuntimeHost` owns app lifecycle only

---

## 7. Transport boundary

`IRaceVisionTransport` with connect/disconnect/send/receive events + connection state. `NullRaceVisionTransport` extension point. Concrete WS = **Agent 12.2**.

---

## 8. Runtime state boundary

`IClientRuntimeState` exposes lifecycle, transport state, mode, session, availability. Full telemetry state apply = **Agent 12.3**.

---

## 9. LIVE/REPLAY boundary

Shared architecture via `OperatingMode.Live | Replay`. No Unity ReplayClock / seek / playback authority.

---

## 10. Session/identity rules

Distinct types: `ConnectionId`, `PrincipalId`, `SessionId`, `SubscriptionId`, `SourceSequence`, `TransportSequence`.

---

## 11. Configuration architecture

`RaceVisionClientConfig` ScriptableObject + `ClientEnvironment` (Development/Test/Staging/Production). Localhost defaults only; no secrets.

---

## 12. Scene/prefab architecture

Conventions documented for Bootstrap/Race/UI/Cameras scenes and Car/Track/Camera/Effect/UI prefabs. No finished assets.

---

## 13. Blender asset boundary

Documented: Blender → export → Unity import → prefab → entity → telemetry transform. Mapping owned by **12.4**.

---

## 14. Testing architecture

`Tests/EditMode` (architecture smoke) and `Tests/PlayMode` (placeholder). Full suite = **12.13**.

---

## 15. Documentation updated

Spec + Roadmap + Architecture + Streaming + Unity docs + unity/tests/rendering READMEs + specs index.

---

## 16. Files created

Primary: `docs/specifications/UnityClientArchitectureSpecification.md`, `unity/Assets/RaceVision/**` (asmdefs, contracts, READMEs, smoke tests).

---

## 17. Files modified

`docs/Roadmap.md`, `docs/Architecture.md`, `docs/Streaming.md`, `docs/Unity.md`, `docs/architecture/README.md`, `docs/specifications/README.md`, `docs/unity/README.md`, `unity/README.md`, `unity/Assets/README.md`, `unity/Documentation/README.md`, `rendering/unity/README.md`, `tests/unity/README.md`.

---

## 18. Tests executed (exact)

| Suite                                                                                                             | Result                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Phase 10/11 regression (`tests/api` + `phase10` + `phase10_acceptance` + transport integration + live acceptance) | **382 passed**, 2 warnings                                                                                                       |
| Unity EditMode / PlayMode                                                                                         | **Not executed** — Unity project `ProjectSettings`/`Packages` not scaffolded (foundation-only scope); Test Framework unavailable |
| `dotnet build` of pure assemblies                                                                                 | **Not available** — no .NET SDK installed on machine                                                                             |

---

## 19. Static analysis (exact)

- Ruff/mypy: N/A (no Python/backend changes)
- Secret scan on new Unity assets: no credentials introduced
- Backend/shared git status: clean (unchanged)

---

## 20. Acceptance gates GATE-01…20

| Gate                                                                                                                                    | Result         |
| --------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| GATE-01…19 (structure, boundaries, LIVE/REPLAY, identities, config, lifecycle, scenes, Blender, tests, extension points, no duplicates) | **PASS**       |
| GATE-20 Phase 10+11 green                                                                                                               | **PASS** (382) |

**20/20 PASS** within Agent 12.1 scope (Unity Editor compile deferred until project packages exist).

---

## 21. Limitations

- Full Unity project scaffold not created (per scope)
- Editor compile / EditMode execution pending packages
- Transport/sync are stubs only
- No cars, tracks, coordinates, effects, cameras

---

## 22. Deferred work for Agent 12.2

Implement concrete WebSocket client behind `IRaceVisionTransport`, serialization/decode, main-thread message pump, reconnect using config options, auth header handling without logging secrets.

---

## 23. Recommended next Agent

**Agent 12.2 — RaceVision WebSocket client#**

## Assistant

Understood. **Agent 12.1 is ACCEPTED**, and the implementation is appropriately scoped.

The important architectural result is that Phase 12 now has a clean Unity foundation:

```text
Phase 11 Transport
        │
        ▼
   12.2 WebSocket
        │
        ▼
  12.3 State Sync
        │
        ▼
 Unity Runtime State
        │
   ┌────┴────┐
   ▼         ▼
 Domain   Coordinate
          System
   │         │
   └────┬────┘
        ▼
   Presentation
```

And the ownership boundaries are clear:

- **12.1** → architecture/foundations ✓
- **12.2** → concrete WebSocket client
- **12.3** → transport → Unity state synchronization
- **12.4** → telemetry/track coordinate system
- **12.5–12.10** → cars, track, visualization and effects
- **12.11** → LIVE/REPLAY presentation modes
- **12.12** → performance
- **12.13** → integration testing
- **12.14** → final acceptance

### One particularly important decision

The report confirms:

> `ConnectionId`, `PrincipalId`, `SessionId`, `SubscriptionId`, `SourceSequence`, `TransportSequence`

remain **distinct types**.

That is exactly what we want before connecting Unity to the Phase 11 transport.

Also, **Blender remains correctly deferred**. We don't want to start modelling the production F1 cars/tracks until **12.4 establishes the coordinate contract**.

### Phase 12 status

```text
12.1  Unity Client Architecture       ✓ ACCEPTED
12.2  RaceVision WebSocket Client      ← NEXT
12.3  Runtime State Synchronization
12.4  Track / Coordinate System
12.5  F1 Car Entity Runtime
12.6  Multi-Car Rendering
12.7  Vehicle Transform / Orientation
12.8  Track & Circuit Scene
12.9  Telemetry Visualization
12.10 Vehicle Effects
12.11 Replay / Live Unity Modes
12.12 Unity Performance
12.13 Unity Integration Testing
12.14 Phase 12 Acceptance
```

**Next logical step is Agent 12.2 — RaceVision WebSocket Client.**

For 12.2, we should be particularly careful that the concrete WebSocket implementation plugs into the `IRaceVisionTransport` established by 12.1 rather than creating a second transport abstraction.

## User

Please give commands for Agent 12.2	RaceVision WebSocket Client	Connect Unity to the Phase 11 transport ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. This Agent should implement the **concrete Unity WebSocket transport behind the `IRaceVisionTransport` created by 12.1**, while preserving the Phase 11 contracts and keeping synchronization/rendering out of scope.

Copy the entire block into Cursor Agent mode:

```text
You are Agent 12.2 — RaceVision WebSocket Client for the RaceVision project.

============================================================
RACEVISION — PHASE 12
AGENT 12.2 — RACEVISION WEBSOCKET CLIENT
============================================================

ROLE
------------------------------------------------------------
You are a Principal Unity Networking Engineer implementing the
Unity-side WebSocket client for RaceVision.

Your task is to implement Agent 12.2:

    RaceVision WebSocket Client

Purpose:

    Connect the Unity client to the existing Phase 11 WebSocket
    transport through the architecture established by Agent 12.1.

The Unity client is a CONSUMER of the Phase 11 transport.

Phase 10 remains the authoritative Runtime.

Phase 11 remains the authoritative transport/API boundary.

Unity must not create a second Runtime, EventBus, subscription
engine, authentication system, rate limiter, backpressure system,
or session manager.

============================================================
1. MANDATORY FIRST STEP — AUDIT THE REPOSITORY
============================================================

Before modifying anything, inspect the repository thoroughly.

Read:

- docs/Roadmap.md
- docs/Architecture.md
- docs/Streaming.md
- docs/Unity.md
- docs/architecture/*
- docs/specifications/*
- Phase 10 specifications
- Phase 11 specifications
- UnityClientArchitectureSpecification.md
- LiveTelemetryStreamingSpecification.md
- ReplayStreamingSpecification.md
- SubscriptionSystemSpecification.md
- ConnectionSessionManagementSpecification.md
- TransportHardeningSpecification.md
- RateLimitingAbuseProtectionSpecification.md
- TransportObservabilitySpecification.md
- TransportIntegrationTestingSpecification.md
- LiveStreamingAcceptanceSpecification.md
- Phase 11 Acceptance documentation
- unity/README.md
- unity/Assets/README.md
- existing Unity files
- existing `IRaceVisionTransport`
- existing `NullRaceVisionTransport`
- existing Unity configuration
- existing lifecycle contracts
- existing identity types
- existing protocol contracts

Also inspect:

- backend/api/
- backend/api/security/
- backend/api/telemetry/
- backend/api/replay/
- backend/api/subscriptions/
- backend/api/outbound/
- backend/api/hardening/
- backend/api/observability/
- existing WebSocket protocol/envelope definitions

Understand the actual Phase 11 contracts before implementing
the Unity client.

DO NOT guess protocol shapes.

============================================================
2. EXISTING ARCHITECTURE IS AUTHORITATIVE
============================================================

Agent 12.1 already established:

    Phase 11 Transport
           ↓
       IRaceVisionTransport
           ↓
       Unity Runtime
           ↓
       Synchronization
           ↓
       Domain
           ↓
       Presentation

The concrete implementation must plug into:

    IRaceVisionTransport

Do NOT replace it.

Do NOT create:

    IUnityWebSocketClient
    ITransportClient2
    UnityTransportManager
    RaceVisionNetworkManager
    second WebSocket abstraction

unless an existing contract genuinely requires reconciliation.

Prefer implementing the existing interface.

============================================================
3. RESPONSIBILITY
============================================================

This agent owns:

- WebSocket connection
- WebSocket handshake
- WebSocket lifecycle
- outbound transport messages
- inbound transport messages
- frame reception
- protocol decoding boundary
- connection state reporting
- reconnect behavior
- bounded receive handling
- main-thread dispatch boundary
- transport-level errors
- authentication header/token attachment according to Phase 11
- clean shutdown
- transport metrics/logging appropriate for Unity

This agent does NOT own:

- telemetry state application
- telemetry interpolation
- telemetry extrapolation
- replay timing
- ReplayClock
- car transforms
- track transforms
- rendering
- camera systems
- effects
- HUD
- Unity replay controller
- coordinate conversion
- subscription business logic
- authorization policy
- backend rate limiting
- backend backpressure

Those belong elsewhere.

============================================================
4. PHASE 11 WEBSOCKET ENDPOINT
============================================================

Use the actual Phase 11 WebSocket endpoint discovered in the
repository documentation/code.

The known architecture is:

    WS /api/v1/ws

Do NOT hard-code this in multiple classes.

The endpoint must come from the Unity configuration established
by Agent 12.1.

Support environment configuration such as:

    Development
    Test
    Staging
    Production

Do not embed production endpoints in source code.

============================================================
5. CONNECTION ARCHITECTURE
============================================================

Implement the concrete transport approximately as:

    IRaceVisionTransport
            ▲
            │
    RaceVisionWebSocketTransport
            │
       WebSocket
            │
       Phase 11 API

The concrete class must remain behind the interface.

Runtime code must not need to know whether the underlying
transport is:

    WebSocket
    Null transport
    test transport
    future transport

============================================================
6. WEBSOCKET IMPLEMENTATION
============================================================

Use a Unity-compatible WebSocket implementation appropriate to
the actual project/package environment.

FIRST inspect `Packages/manifest.json` and the Unity project.

Do not blindly add a dependency.

If the required WebSocket package is absent, determine the
cleanest supported approach for the project's Unity version.

The project context is expected to target:

    Unity 6.x

but VERIFY the actual project configuration before implementing.

Prefer a maintained Unity-compatible WebSocket mechanism.

Avoid platform-specific assumptions unless the repository already
requires them.

The implementation must preserve the transport abstraction.

============================================================
7. CONNECTION LIFECYCLE
============================================================

Implement explicit connection states using the existing
transport lifecycle contracts from 12.1.

At minimum distinguish:

    Disconnected
    Connecting
    Connected
    Reconnecting
    Closing
    Faulted

Use the project's existing enum if already established.

Do not duplicate the application lifecycle.

Application lifecycle:

    ClientRuntimeHost

Transport lifecycle:

    RaceVisionWebSocketTransport

These are separate authorities.

============================================================
8. CONNECT
============================================================

Connect must:

1. Validate configuration.
2. Build the WebSocket URI from configuration.
3. Attach authentication according to the Phase 11 contract.
4. Establish the WebSocket.
5. Transition connection state.
6. Begin receive processing.
7. Notify the runtime through `IRaceVisionTransport`.
8. Remain non-blocking with respect to Unity rendering.

Do not block the Unity main thread while connecting.

Do not log credentials or tokens.

============================================================
9. AUTHENTICATION
============================================================

Inspect the actual Phase 11 authentication contract.

Authentication is owned by Phase 11.

Unity only supplies the credential/token through the transport
boundary.

Do NOT implement:

- JWT validation
- authorization policy
- permission evaluation
- token issuance
- token introspection
- backend security logic

Unity must not duplicate:

    backend/api/security/

Credentials/tokens MUST NEVER be logged.

If authentication configuration is absent or invalid:

    fail clearly
    expose a safe transport error
    do not silently connect anonymously if the configured
    environment requires authentication

Do not invent authentication behavior not supported by Phase 11.

============================================================
10. WEBSOCKET ORIGIN / TLS
============================================================

Respect Phase 11 hardening.

Support:

    ws://
    wss://

according to environment configuration.

Production should be capable of secure transport.

Do not bypass certificate validation.

Do not implement insecure "accept all certificates" behavior.

Do not invent Origin behavior if the Unity WebSocket library does
not expose the necessary mechanism.

Document any platform/library limitation.

============================================================
11. RECEIVE LOOP
============================================================

Implement one centralized receive pipeline.

Do NOT create:

    one receive loop per subscription
    one WebSocket per telemetry stream
    one WebSocket per car
    one WebSocket per event type

Architecture:

    WebSocket
        ↓
    Receive Loop
        ↓
    Raw Message
        ↓
    Protocol Decoder
        ↓
    Transport Message
        ↓
    Main-thread Dispatch Boundary
        ↓
    IStateSynchronizer (Agent 12.3)

Agent 12.2 stops at the transport/protocol boundary.

============================================================
12. MESSAGE BOUNDARY
============================================================

Preserve the Phase 11 transport envelope.

Do not strip important metadata.

Preserve, where present:

- message type
- schema/version
- session_id
- subscription_id
- source sequence
- transport sequence
- timestamp
- operating mode
- payload
- error information

IMPORTANT:

Transport sequence and source sequence remain distinct.

Do not overwrite source sequence with transport sequence.

Do not reorder messages.

Do not synthesize missing messages.

Do not interpolate messages.

Do not extrapolate messages.

============================================================
13. PROTOCOL DECODING
============================================================

Use the protocol boundary established in Agent 12.1.

Implement concrete decoding only to the extent required to convert
raw WebSocket messages into transport-level protocol messages.

Do not turn transport decoding into runtime state application.

The output should be consumable by Agent 12.3.

Conceptually:

    JSON/Binary WebSocket frame
             ↓
       Protocol Decoder
             ↓
       Transport Message
             ↓
       IStateSynchronizer

If Phase 11 supports only JSON currently, implement JSON first.

Do not invent binary protocol support.

============================================================
14. MESSAGE SIZE LIMITS
============================================================

Respect Phase 11 transport hardening and payload constraints.

Implement bounded receive handling.

A malicious or malformed message must not cause:

- unbounded allocation
- runaway memory growth
- application crash
- infinite parsing
- infinite retry

If the underlying WebSocket library provides frame/message size
limits, configure them.

If not, enforce bounded handling at the appropriate layer.

Use the actual Phase 11 limits where available.

Do not invent conflicting configuration values.

============================================================
15. MAIN THREAD BOUNDARY
============================================================

Unity GameObjects and UnityEngine APIs generally require the
Unity main thread.

The network receive path must therefore NOT directly manipulate:

- GameObjects
- Transforms
- Renderers
- Scenes
- Materials
- Unity UI

Instead:

    Network thread/task
           ↓
    bounded message queue
           ↓
    main-thread pump
           ↓
    transport message event/callback

Agent 12.3 will consume the message boundary.

Avoid an unbounded receive queue.

============================================================
16. BACKPRESSURE / RECEIVE QUEUE
============================================================

Phase 11 owns OUTBOUND backpressure.

Unity must not create a second server-side backpressure system.

However, Unity must protect itself from an overloaded receive path.

Implement a bounded client-side receive queue if necessary.

Define safe behavior when the queue reaches capacity.

Possible behavior:

- reject/drop according to message class
- fail connection for protocol safety
- preserve control messages
- report metrics

BUT:

Do not silently discard canonical telemetry without documenting
the behavior.

Do not mutate telemetry payloads.

Do not claim durable delivery.

The Phase 11 transport does not provide durable resume.

============================================================
17. RECONNECT
============================================================

Implement reconnect behavior according to the 12.1 configuration
boundary.

Reconnect must:

- detect abnormal disconnect
- transition to Reconnecting
- apply bounded retry attempts
- apply exponential backoff or equivalent bounded strategy
- avoid busy loops
- stop reconnecting during intentional shutdown
- re-authenticate
- create a new transport connection
- expose the new connection state

IMPORTANT:

Phase 11 behavior is:

    reconnect = new connection
    re-authentication required
    subscriptions must be recreated

Unity must NOT assume:

    durable resume
    missed-frame replay
    server-side subscription persistence

Do not silently claim messages were recovered.

============================================================
18. RECONNECT AND SUBSCRIPTIONS
============================================================

Agent 12.2 must NOT implement the full subscription system.

However, it must expose the lifecycle hooks needed by future
subscription management.

Provide a clean event/extension point such as:

    Connected
    Disconnected
    Reconnected

without inventing a second subscription authority.

Agent 12.3/Phase 12 subscription orchestration can later use these
events.

If the Phase 11 protocol requires explicit subscribe messages,
implement only the transport capability to send them.

Do not implement subscription ownership here.

============================================================
19. SEND
============================================================

Implement transport-level send capability behind:

    IRaceVisionTransport

Sending must:

- be asynchronous/non-blocking
- validate connection state
- serialize the correct transport envelope
- respect payload size limits
- report errors safely
- not expose raw WebSocket objects to callers

Do not allow arbitrary rendering systems to send messages directly.

============================================================
20. SEND QUEUE
============================================================

If a send queue is required:

- keep it bounded
- avoid blocking Unity
- define overflow behavior
- preserve control messages where appropriate
- prevent unlimited memory growth

Do not duplicate Phase 11 outbound queue semantics.

This is a CLIENT-side transport mechanism only.

============================================================
21. DISCONNECT
============================================================

Implement clean disconnect.

Requirements:

- stop receive loop
- prevent new sends
- drain or safely discard client-side transport queue
- close WebSocket
- release resources
- transition state
- raise disconnect notification
- do not reconnect if shutdown was intentional

Disconnect must be idempotent.

Calling disconnect twice must not crash.

============================================================
22. APPLICATION SHUTDOWN
============================================================

Integrate with `ClientRuntimeHost`.

On Unity shutdown:

    ClientRuntimeHost
          ↓
    Transport.Stop/Disconnect
          ↓
    Receive loop stops
          ↓
    WebSocket closes
          ↓
    resources released

Do not leave background tasks running after shutdown.

Avoid:

- orphaned threads
- orphaned tasks
- hidden WebSocket instances
- reconnect loops after application exit

============================================================
23. HEARTBEAT
============================================================

Do NOT create a competing application heartbeat protocol.

Phase 11 already owns WebSocket heartbeat/connection management.

Inspect the actual server behavior.

If the WebSocket library automatically handles protocol-level
ping/pong, use that.

If application-level messages are required by the actual Phase 11
contract, implement only what the contract requires.

Do not invent a second heartbeat system.

============================================================
24. ERROR MODEL
============================================================

Use the transport error abstractions established in 12.1.

Errors should distinguish:

- configuration
- connection
- authentication
- authorization response
- protocol
- payload
- timeout
- network
- server close
- client shutdown
- queue overflow

Do not expose:

- stack traces to normal transport consumers
- credentials
- tokens
- authorization headers
- internal server paths
- secrets

Detailed information may go to controlled local diagnostics if
safe.

============================================================
25. SERVER CLOSE CODES
============================================================

Respect actual Phase 11 WebSocket close semantics.

Map close conditions to safe Unity transport states/errors.

Do not automatically reconnect forever.

For authentication/authorization failures, avoid aggressive
reconnect loops.

For rate-limit/admission failures, respect server-provided
retry guidance where available.

For normal server shutdown, reconnect only when policy permits.

Inspect actual Phase 11 error/close contracts before coding.

============================================================
26. OBSERVABILITY
============================================================

Integrate with the logging/metrics boundary from 12.1.

Useful client-side metrics include:

- connect attempts
- successful connections
- failed connections
- reconnect attempts
- reconnect successes
- disconnects
- received messages
- decoded messages
- protocol errors
- malformed messages
- send failures
- receive queue high-water mark
- receive queue overflow
- connection duration

Do not use:

- access tokens
- credentials
- session IDs as uncontrolled high-cardinality logs
- raw telemetry payloads in normal logs

Do not create a duplicate backend transport observability system.

============================================================
27. LOGGING
============================================================

Default logging must be controlled.

Do not log every telemetry frame by default.

Use structured categories such as:

    Transport
    Connection
    Protocol
    Authentication
    Reconnect
    Shutdown

For debugging, allow controlled verbose logging.

Never log:

- Authorization headers
- JWTs
- passwords
- secrets
- API keys

============================================================
28. THREAD SAFETY
============================================================

The transport implementation must be safe against:

- connect/disconnect races
- reconnect/disconnect races
- shutdown during connect
- shutdown during receive
- send during disconnect
- duplicate disconnect calls
- duplicate reconnect scheduling

Use one clear ownership model.

Avoid locks that can block the Unity main thread unnecessarily.

Avoid async void except where Unity lifecycle integration genuinely
requires it.

============================================================
29. UNITY LIFECYCLE INTEGRATION
============================================================

Use the existing architecture from 12.1.

Do not create a second application lifecycle manager.

The transport may expose:

    Initialize
    Connect
    Disconnect
    Dispose

according to the established interface.

Respect:

    ClientRuntimeHost

as the application lifecycle owner.

============================================================
30. CONFIGURATION
============================================================

Use the existing:

    RaceVisionClientConfig

from Agent 12.1.

Do not create another configuration system.

Add only fields genuinely required for the WebSocket client.

Potential configuration:

- WebSocket endpoint
- connect timeout
- receive timeout if applicable
- reconnect enabled
- max reconnect attempts
- reconnect initial delay
- reconnect maximum delay
- receive queue capacity
- send queue capacity
- logging level

Validate values.

Do not allow invalid values to cause infinite loops.

Do not put secrets into ScriptableObjects if the project's security
model does not support secure secret storage.

============================================================
31. TESTABILITY
============================================================

The concrete transport must be testable without requiring a real
production backend.

Support dependency injection for:

- WebSocket implementation
- clock/timer where useful
- configuration
- dispatcher
- logger

Do not hard-wire all dependencies into a MonoBehaviour.

Provide a test seam for:

- successful connect
- failed connect
- receive
- malformed message
- send
- disconnect
- reconnect
- shutdown
- queue overflow
- authentication failure
- server close

============================================================
32. DO NOT IMPLEMENT AGENT 12.3
============================================================

The following are explicitly OUT OF SCOPE:

- applying telemetry to runtime state
- updating car state
- updating track state
- updating race state
- interpolation
- extrapolation
- frame reconciliation
- replay state application
- state snapshots
- telemetry history

The transport should expose messages so Agent 12.3 can consume
them.

============================================================
33. DO NOT IMPLEMENT AGENT 12.4
============================================================

Do not implement:

- telemetry coordinate conversion
- world-space conversion
- track coordinate mapping
- car heading conversion
- Unity axis mapping
- scale calibration

Those belong to Agent 12.4.

============================================================
34. DO NOT IMPLEMENT BLENDER WORK
============================================================

Do not:

- create F1 car models
- create circuit models
- import production Blender assets
- create production materials
- create production prefabs

Blender asset production follows the coordinate contract from 12.4.

============================================================
35. UNITY PACKAGE / PLATFORM HANDLING
============================================================

Inspect the actual Unity project first.

If the project is still foundation-only and does not have a
complete Unity Package configuration:

- do not fabricate package versions
- document what is missing
- add only the minimum legitimate project configuration required
- keep the architecture compatible with the intended Unity version

The project previously reported Unity Editor/Test Framework
unavailable.

Do not claim Unity compilation/tests ran unless they actually ran.

============================================================
36. SECURITY REQUIREMENTS
============================================================

The client must:

- never log secrets
- never hard-code production credentials
- use secure WebSocket transport where configured
- preserve server authentication behavior
- not bypass TLS validation
- not implement insecure certificate acceptance
- not expose raw credentials to presentation systems
- avoid leaking protocol errors unnecessarily

Authentication/authorization remains Phase 11 authority.

============================================================
37. PROTOCOL COMPATIBILITY
============================================================

The Unity client must consume the actual Phase 11 transport
contract.

Verify:

- envelope format
- message types
- schema version
- session_id
- subscription_id
- source sequence
- transport sequence
- operating mode
- error envelope
- control messages
- subscription messages

Do not invent alternate JSON structures.

If the repository contains ambiguity:

1. identify it
2. compare the authoritative Phase 11 specification/code
3. choose the documented contract
4. document the decision

Do not silently create incompatible behavior.

============================================================
38. REQUIRED ARCHITECTURE
============================================================

The final architecture should be approximately:

    ClientRuntimeHost
            │
            ▼
    IRaceVisionTransport
            ▲
            │
    RaceVisionWebSocketTransport
            │
            ▼
       WebSocket
            │
            ▼
       Phase 11 API
            │
            ▼
      Receive Pipeline
            │
            ▼
    Protocol Decoder
            │
            ▼
    Bounded Message Queue
            │
            ▼
     Main Thread Pump
            │
            ▼
       Transport Events
            │
            ▼
      Agent 12.3 State Sync

No renderer should appear anywhere inside this transport path.

============================================================
39. FILE / MODULE ORGANIZATION
============================================================

Reuse Agent 12.1 boundaries.

Likely location:

    unity/Assets/RaceVision/Transport/

Possible structure:

    Transport/
    ├── Connection/
    │   ├── RaceVisionWebSocketTransport.cs
    │   ├── WebSocketConnectionState.cs
    │   └── ...
    │
    ├── Protocol/
    │   ├── ...
    │
    ├── Serialization/
    │   ├── ...
    │
    └── Runtime/
        ├── ...
    
Do not create duplicate assemblies.

Use the existing assembly definitions from 12.1.

============================================================
40. DOCUMENTATION
============================================================

Create:

    docs/specifications/RaceVisionWebSocketClientSpecification.md

Update:

- docs/Roadmap.md
- docs/Unity.md
- docs/Architecture.md
- docs/Streaming.md
- Unity README
- Unity architecture documentation
- specification index

Document:

- WebSocket architecture
- endpoint configuration
- lifecycle
- receive pipeline
- send pipeline
- protocol boundary
- authentication handling
- reconnect
- queue limits
- main-thread dispatch
- errors
- observability
- security
- testing
- platform limitations
- ownership boundaries

Clearly identify:

    Agent 12.2 — ACCEPTED

only after verification.

============================================================
41. ACCEPTANCE GATES
============================================================

GATE-01
Existing 12.1 architecture is reused.

GATE-02
Concrete WebSocket implementation is behind IRaceVisionTransport.

GATE-03
No duplicate transport abstraction is introduced.

GATE-04
Correct Phase 11 WebSocket endpoint is used/configurable.

GATE-05
Authentication follows Phase 11 contract.

GATE-06
No credentials/secrets are logged.

GATE-07
Connection lifecycle is explicit.

GATE-08
Connect is non-blocking to Unity rendering.

GATE-09
Receive pipeline is centralized.

GATE-10
Receive queue is bounded.

GATE-11
Malformed messages cannot crash the client.

GATE-12
Transport envelopes preserve required metadata.

GATE-13
Source sequence and transport sequence remain distinct.

GATE-14
No transport-side reorder/interpolation/extrapolation occurs.

GATE-15
Main-thread Unity boundary is explicit.

GATE-16
Reconnect uses bounded retry/backoff.

GATE-17
Intentional shutdown does not trigger reconnect.

GATE-18
Reconnect requires re-authentication.

GATE-19
No durable resume is claimed.

GATE-20
No duplicate subscription engine is created.

GATE-21
No duplicate authentication/authorization system is created.

GATE-22
No duplicate rate-limit/backpressure system is created.

GATE-23
Send path is bounded and asynchronous.

GATE-24
Disconnect is idempotent.

GATE-25
Shutdown cleans all transport resources.

GATE-26
Transport errors are classified and safe.

GATE-27
Observability is available without leaking secrets.

GATE-28
Configuration is environment-aware.

GATE-29
Transport is testable without production backend dependency.

GATE-30
Agent 12.3 can consume transport messages without refactoring
the WebSocket implementation.

GATE-31
Phase 10 Runtime is unchanged.

GATE-32
Phase 11 transport is unchanged unless documentation requires
a compatibility-only clarification.

GATE-33
No Blender/car/track implementation is introduced.

GATE-34
Documentation accurately reflects implementation.

GATE-35
All applicable existing regressions remain green.

============================================================
42. VERIFICATION
============================================================

Before declaring ACCEPTED:

1. Inspect all changed files.
2. Verify existing 12.1 contracts are reused.
3. Verify no duplicate transport abstraction exists.
4. Verify WebSocket endpoint against Phase 11 source/spec.
5. Verify authentication handling.
6. Verify no secrets are logged.
7. Verify reconnect behavior.
8. Verify shutdown behavior.
9. Verify bounded receive queue.
10. Verify malformed message handling.
11. Verify send failure handling.
12. Verify protocol envelope preservation.
13. Verify sequence separation.
14. Verify main-thread boundary.
15. Verify Unity compilation if the project is capable of it.
16. Run Unity EditMode tests if available.
17. Run PlayMode tests if available.
18. Run backend Phase 10/11 regressions if applicable.
19. Run static analysis available in the environment.
20. Inspect Git diff.
21. Confirm no unrelated files were changed.

Do not claim a test passed unless it was actually executed.

============================================================
43. IMPORTANT — DO NOT OVER-IMPLEMENT
============================================================

STOP at the transport boundary.

Do NOT automatically continue to:

    12.3 Runtime State Synchronization

Do not implement:

- telemetry state application
- car state
- track state
- transforms
- coordinate mapping
- visualization
- effects
- replay presentation
- cameras

Those are future agents.

============================================================
44. FINAL REPORT
============================================================

When complete, report exactly:

1. STATUS
   ACCEPTED / NOT ACCEPTED

2. Existing 12.1 architecture reused

3. WebSocket implementation

4. Endpoint configuration

5. Connection lifecycle

6. Authentication handling

7. Receive pipeline

8. Protocol decoding

9. Main-thread dispatch

10. Receive/send queue behavior

11. Reconnect behavior

12. Shutdown/disconnect behavior

13. Error handling

14. Observability

15. Security

16. Files created

17. Files modified

18. Documentation updated

19. Unity tests executed — EXACT RESULTS

20. Backend tests executed — EXACT RESULTS

21. Static analysis — EXACT RESULTS

22. Acceptance gates GATE-01…35

23. Limitations

24. Deferred work for Agent 12.3

25. Recommended next Agent

============================================================
45. FINAL RULE
============================================================

Do not proceed to Agent 12.3 automatically.

Finish Agent 12.2 only.

Return the complete implementation and verification report.

============================================================
START AGENT 12.2 NOW
============================================================
```

## User

## 1. STATUS

**ACCEPTED**

Agent 12.2 complete. Left uncommitted per your choice. No Phase 10/11 backend changes. Did not start Agent 12.3.

---

## 2. Existing 12.1 architecture reused

Extended `IRaceVisionTransport` (no second abstraction). Reused assemblies, `RaceVisionClientConfig`, `ClientCompositionRoot`, `ClientRuntimeHost`, protocol envelope types, and identity/lifecycle enums.

---

## 3. WebSocket implementation

`RaceVisionWebSocketTransport` → `SystemClientWebSocket` (`System.Net.WebSockets.ClientWebSocket`). Test seam: `IClientWebSocket` / `FakeClientWebSocket`.

---

## 4. Endpoint configuration

From `RaceVisionClientConfig.WebSocketUrl` (default `ws://127.0.0.1:8000/api/v1/ws`). Supports `ws://` and `wss://`; TLS validation not bypassed.

---

## 5. Connection lifecycle

`TransportConnectionState`: Disconnected → Connecting → Connected ⇄ Reconnecting → Disconnecting → Disconnected | Faulted. Separate from app lifecycle.

---

## 6. Authentication handling

Phase 11 preferred `Authorization: Bearer` via `ITransportCredentialProvider`. Fail-closed when `AuthenticationRequired` and token missing. Tokens never logged or stored in ScriptableObjects.

---

## 7. Receive pipeline

Single receive task → bounded queue → `PumpMainThread()` (≤64/frame) → decode → events. One connection; not per-car/per-subscription.

---

## 8. Protocol decoding

`JsonProtocolDecoder` / `JsonLite` for Phase 11 schema `1.x`. Preserves types, session, timestamps, payload, errors. Binary frames rejected.

---

## 9. Main-thread dispatch

Network I/O off main thread; `ClientRuntimeHost.Update` calls `PumpMainThread()`. No GameObject/transform/UI work in transport.

---

## 10. Receive/send queue behavior

Bounded queues (default recv 256 / send 64). Overflow drops **oldest**, increments metrics — **non-durable**, documented. `MaxMessageBytes` default **65536** (= Phase 11 `WS_MAX_MESSAGE_SIZE`).

---

## 11. Reconnect behavior

Exponential backoff, max attempts, re-auth, new `ConnectionId`, `Reconnected` event. No durable resume; subscriptions must be recreated by later agents.

---

## 12. Shutdown/disconnect behavior

Intentional disconnect cancels reconnect; clears queues; aborts/disposes socket; idempotent. Wired from host `OnDestroy` / `OnApplicationQuit`.

---

## 13. Error handling

Classified via `ClientErrorCategory`; consumer exceptions swallowed on event callbacks; no credential leakage in log messages.

---

## 14. Observability

`ITransportClientMetrics` (connects, reconnects, decode errors, queue depth/HWM, overflows). Telemetry frame logging off by default.

---

## 15. Security

No token logging; no cert bypass; no duplicate auth/RL/backpressure/subscription systems; no Blender/cars/tracks.

---

## 16. Files created

Spec + transport WebSocket/auth/queues/observability/serialization, `JsonLite`, EditMode fakes/tests (see git untracked under `unity/Assets/RaceVision/Transport/` and Protocol/Json).

---

## 17. Files modified

`IRaceVisionTransport`, Null transport, config, composition root, `ClientRuntimeHost`, protocol envelope/decoder, architecture smoke tests, Roadmap/Architecture/Streaming/Unity/README/specs index.

---

## 18. Documentation updated

`docs/specifications/RaceVisionWebSocketClientSpecification.md` + roadmap/docs READMEs marked **12.2 ACCEPTED**.

---

## 19. Unity tests executed — EXACT RESULTS

**Not executed** — Unity `Packages/manifest` / Test Framework still not scaffolded; no Unity batchmode run. EditMode tests are present (`WebSocketTransportTests`, updated architecture smoke).

---

## 20. Backend tests executed — EXACT RESULTS

```
pytest tests/api tests/runtime/phase10 tests/runtime/phase10_acceptance
      tests/integration/transport tests/acceptance/live_streaming -q
→ 382 passed, 2 warnings
PYTEST_EXIT=0
```

`backend/` / `shared/` unchanged.

---

## 21. Static analysis — EXACT RESULTS

- Ruff/mypy: N/A (no Python changes)
- Secret scan on transport: credentials used only for headers, never logged
- `.NET SDK` still unavailable for standalone compile

---

## 22. Acceptance gates GATE-01…35

| Gates                                                                        | Result         |
| ---------------------------------------------------------------------------- | -------------- |
| GATE-01…30 (architecture, WS, auth, queues, reconnect, safety, 12.3 handoff) | **PASS**       |
| GATE-31…32 Phase 10/11 unchanged                                             | **PASS**       |
| GATE-33 no Blender/cars/tracks                                               | **PASS**       |
| GATE-34 docs accurate                                                        | **PASS**       |
| GATE-35 regressions green                                                    | **PASS** (382) |

Unity Editor compile/EditMode execution remain environment-limited (documented), not blocking for this agent’s accepted scope.

**35/35 PASS** within stated limitations.

---

## 23. Limitations

- Full Unity project packages still missing → no Editor compile/test run
- `ClientWebSocket` Origin header not generically settable (native clients OK when server Origin allowlist empty)
- Client receive overflow drops oldest (non-durable)
- Subscription orchestration not implemented (by design)

---

## 24. Deferred work for Agent 12.3

Consume `EnvelopeReceived` / pumped envelopes → apply session/mode/telemetry/events/snapshots into `IClientRuntimeState` without transport or rendering coupling; handle resubscribe on `Reconnected`.

---

## 25. Recommended next Agent

**Agent 12.3 — Runtime state synchronization**

## Assistant

Understood. I’ve got the current RaceVision state through **Phase 12.2** in context.

The important handoff is:

```text
Phase 10
  Runtime / Live / Replay authority
        ↓
Phase 11
  REST / WebSocket transport
  Auth / rate limiting / hardening
  Live + Replay streaming
  subscriptions
  connection lifecycle
  outbound backpressure
  observability
  integration + acceptance
        ↓
Phase 12
  Unity client
        ↓
12.1 Unity Client Architecture       ✓ ACCEPTED
12.2 RaceVision WebSocket Client      ✓ ACCEPTED
12.3 Runtime State Synchronization    ← NEXT
12.4 Track / Coordinate System
12.5 F1 Car Entity Runtime
12.6 Multi-Car Rendering
12.7 Vehicle Transform / Orientation
12.8 Track & Circuit Scene
12.9 Telemetry Visualization
12.10 Vehicle Effects
12.11 Replay / Live Unity Modes
12.12 Unity Performance
12.13 Unity Integration Testing
12.14 Phase 12 Acceptance
```

### Critical architectural rule going forward

**Unity is a consumer of Phase 11, not another runtime authority.**

So for **12.3**, the flow should remain:

```text
Phase 10 Runtime
      ↓
Phase 11 EventBus / Transport
      ↓
WebSocket
      ↓
12.2 RaceVisionWebSocketTransport
      ↓
12.3 Runtime State Synchronization
      ↓
Unity Client Runtime State
      ↓
12.5+ Domain / Rendering
```

And specifically:

- No Unity ReplayClock.
- No Unity telemetry interpolation authority.
- No Unity transport subscription engine.
- No duplicate authentication/rate limiting.
- No Runtime/EventBus logic moved into Unity.
- No rendering logic inside transport.
- LIVE/REPLAY remains dictated by the server's canonical state.
- Blender assets are still **not** being created yet.

### Blender boundary

Your architecture currently establishes:

```text
Blender
   ↓
F1 car / track assets
   ↓
Unity import
   ↓
Unity prefabs
   ↓
12.4 Coordinate System
   ↓
12.5 Car Entity Runtime
   ↓
12.6 Multi-Car Rendering
```

The next major architectural step before serious 3D implementation is therefore **12.4 Track/Coordinate System**. That is where the Blender → Unity coordinate/mapping contract becomes important.

For now, though, **12.3 is the correct next agent** because Unity needs a canonical runtime-state model before cars and tracks can consume telemetry.

I’m ready for the next command request.

## User

Please give commands for Agent 12.3	Runtime State Synchronization	Synchronize telemetry/runtime state into Unity ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. For **Agent 12.3**, the key constraint is that Unity must **consume and synchronize the canonical Phase 11 stream into Unity state without becoming a second runtime authority**.

Copy/paste the following directly into Cursor:

```text
AGENT 12.3 — RUNTIME STATE SYNCHRONIZATION

You are implementing Agent 12.3 for the RaceVision project.

=========================================================
MISSION
=========================================================

Implement:

Agent 12.3 — Runtime State Synchronization

Purpose:

Synchronize canonical Phase 11 WebSocket telemetry, runtime state,
events, snapshots, LIVE/REPLAY mode, and session state into the
Unity-side RaceVision client runtime.

This agent must consume the existing Agent 12.2 transport and the
existing Phase 11 protocol contracts.

DO NOT implement Agent 12.4 or any later agent.

The result must provide a clean, deterministic Unity-side state
synchronization boundary that later agents can consume.

=========================================================
AUTHORITATIVE ARCHITECTURE
=========================================================

The architecture MUST remain:

Phase 10 Runtime
    ↓
Phase 11 EventBus / Transport
    ↓
REST / WebSocket
    ↓
12.2 RaceVisionWebSocketTransport
    ↓
12.3 Runtime State Synchronization
    ↓
Unity Client Runtime State
    ↓
12.4 Coordinate System
    ↓
12.5 F1 Car Entity Runtime
    ↓
12.6 Multi-Car Rendering
    ↓
12.7 Vehicle Transform / Orientation
    ↓
12.8 Track / Circuit Scene
    ↓
12.9 Telemetry Visualization
    ↓
12.10 Vehicle Effects

Phase 10 remains the authoritative Runtime.

Phase 11 remains the authoritative transport.

Unity is a consumer.

Unity MUST NOT become a second Runtime authority.

=========================================================
CRITICAL ARCHITECTURAL RULES
=========================================================

1. Do not modify Phase 10 Runtime authority.

2. Do not create a second EventBus.

3. Do not create a second ReplayClock.

4. Do not create Unity-side timing authority.

5. Do not create Unity-side telemetry interpolation authority.

6. Do not create Unity-side delay-buffer authority.

7. Do not create another WebSocket implementation.

8. Do not create another authentication system.

9. Do not create another subscription system.

10. Do not create another backpressure/rate-limit system.

11. Do not put rendering logic into synchronization.

12. Do not put GameObject/Transform logic into synchronization.

13. Do not make Domain depend on Presentation.

14. Do not make Runtime State depend directly on Transport implementation.

15. Synchronization must consume the existing IRaceVisionTransport boundary.

16. Preserve server/source sequence values exactly.

17. Never invent, reorder, interpolate, extrapolate, or rewrite canonical
    telemetry data.

18. LIVE and REPLAY must use the same synchronization architecture.

19. The server-provided operating mode is authoritative.

20. Session isolation must be preserved.

=========================================================
FIRST: AUDIT EXISTING IMPLEMENTATION
=========================================================

Before changing code, inspect:

unity/Assets/RaceVision/

especially:

- Core
- Domain
- Protocol
- Transport
- Synchronization
- Runtime
- CoordinateSystem
- Presentation

Inspect the work produced by:

- Agent 12.1
- Agent 12.2

Inspect:

- IRaceVisionTransport
- ClientRuntimeHost
- IClientRuntimeState
- existing Runtime state contracts
- Envelope/protocol models
- EnvelopeReceived event/path
- TransportConnectionState
- OperatingMode
- SessionId
- ConnectionId
- PrincipalId
- SubscriptionId
- SourceSequence
- TransportSequence
- JsonProtocolDecoder
- Client composition root
- reconnect handling

Also inspect Phase 11 contracts and specifications relevant to:

- LIVE telemetry
- REPLAY telemetry
- snapshots
- events
- mode
- session
- runtime status
- transport envelopes

Do not assume the protocol shape.

Use the repository's actual implementation as the source of truth.

If something already exists, extend it rather than creating a duplicate.

=========================================================
TARGET ARCHITECTURE
=========================================================

Implement the synchronization path:

IRaceVisionTransport
        ↓
EnvelopeReceived
        ↓
Protocol / Envelope validation
        ↓
Runtime State Synchronizer
        ↓
IClientRuntimeState
        ↓
immutable/current state snapshots
        ↓
future Unity consumers

Recommended conceptual structure:

Transport
    ↓
IStateSynchronizer
    ↓
RuntimeStateSynchronizer
    ↓
ClientRuntimeState
    ↓
TelemetryState / EventState / SnapshotState / SessionState
    ↓
read-only consumers

The synchronizer owns translation from transport envelopes into
Unity client runtime state.

It does NOT own:

- network I/O
- WebSocket connection
- authentication
- subscriptions
- rendering
- physics
- interpolation
- replay timing
- track coordinates
- car GameObjects

=========================================================
RUNTIME STATE MODEL
=========================================================

Establish a clear Unity-side state model capable of representing:

1. Connection state

2. Client lifecycle state

3. Operating mode

4. Session identity

5. Runtime availability

6. Latest canonical telemetry

7. Latest runtime snapshot

8. Latest domain/runtime events

9. Source sequence

10. Transport sequence

11. Server timestamp

12. Provenance/source metadata where provided

13. Synchronization health/status

Use strong types where the existing architecture already provides them.

Do not collapse:

ConnectionId
PrincipalId
SessionId
SubscriptionId
SourceSequence
TransportSequence

into a single identifier.

=========================================================
TELEMETRY SYNCHRONIZATION
=========================================================

Consume canonical telemetry envelopes from Phase 11.

For each valid telemetry message:

- validate envelope
- validate expected payload shape
- preserve session_id
- preserve operating_mode
- preserve source sequence
- preserve transport sequence
- preserve timestamp
- preserve telemetry values
- preserve provenance/metadata when present
- update the current Unity runtime state

Do not:

- interpolate
- extrapolate
- smooth
- predict
- delay
- reorder
- deduplicate by rewriting sequence numbers
- manufacture missing frames

The Unity synchronization layer is a state consumer only.

=========================================================
SEQUENCE HANDLING
=========================================================

Treat transport and source sequences as separate authorities.

Transport sequence:

- identifies transport ordering/envelope delivery where applicable.

Source sequence:

- comes from the canonical Phase 10/Phase 11 source.

Never overwrite one with the other.

Do not create fake source sequence values.

Define and test behavior for:

- first frame
- increasing sequence
- duplicate sequence
- stale sequence
- reconnect with new connection
- LIVE → REPLAY transition
- REPLAY → LIVE transition

If the protocol already defines authoritative ordering semantics,
follow those semantics.

Do not invent a new ordering protocol.

=========================================================
SESSION ISOLATION
=========================================================

The synchronizer MUST reject or ignore state that does not belong to
the active client/session context according to the existing contracts.

Never allow:

Session A telemetry
    ↓
Session B Unity state

Maintain explicit session identity.

Handle:

- initial session assignment
- same-session messages
- unexpected session messages
- session change
- disconnect
- reconnect
- resubscription

Reconnect must NOT restore imaginary durable state.

Agent 12.2 already establishes:

reconnect → new connection → re-authentication → resubscription.

12.3 must correctly reset/reconcile local synchronization state.

=========================================================
LIVE / REPLAY
=========================================================

Support both:

OperatingMode.Live
OperatingMode.Replay

using the same synchronization boundary.

LIVE:

Phase 11 LIVE stream
    ↓
12.3
    ↓
Unity runtime state

REPLAY:

Phase 11 REPLAY stream
    ↓
12.3
    ↓
Unity runtime state

Do NOT create:

- Unity ReplayClock
- Unity playback controller
- Unity seek authority
- Unity replay timeline authority

Phase 10 remains authoritative for replay timing and state.

The Unity client may expose the synchronized mode/state to consumers,
but must not control the canonical replay clock.

=========================================================
SNAPSHOTS
=========================================================

Consume existing Phase 11 snapshot messages where applicable.

Snapshots must update the Unity runtime state using the canonical
snapshot contents.

Do not create a second snapshot engine.

Do not generate synthetic snapshots unless the existing protocol
explicitly requires it.

Define behavior for:

- initial snapshot
- subsequent snapshot
- stale snapshot
- snapshot after reconnect
- snapshot for another session
- LIVE/REPLAY mode changes

=========================================================
EVENTS
=========================================================

Consume canonical events without synthesizing replacements.

Events should be represented separately from telemetry state.

Do not turn every event into telemetry.

Do not modify event sequence values.

Provide a safe Unity-side event consumption mechanism suitable for
later presentation/UI systems.

Avoid retaining an unbounded event history.

If buffering is required, use an explicitly bounded collection.

=========================================================
STATE PUBLICATION
=========================================================

Design the runtime state so consumers can safely read it.

Prefer:

- immutable snapshots
- read-only interfaces
- value objects
- atomic state replacement
- explicit synchronization boundaries

Avoid exposing mutable internal collections.

A future car renderer must be able to ask:

"What is the latest canonical state for this car?"

without knowing anything about:

- WebSockets
- JSON
- authentication
- transport queues
- EventBus
- Phase 11 internals

=========================================================
THREADING / UNITY MAIN THREAD
=========================================================

Respect Agent 12.2's threading model.

Network I/O remains off the Unity main thread.

Synchronization must integrate safely with the existing
ClientRuntimeHost/PumpMainThread model.

Do not perform UnityEngine operations from:

- WebSocket receive tasks
- transport threads
- background tasks
- synchronization worker threads

The synchronization layer should operate on already-pumped protocol
messages according to the architecture established by 12.2.

No GameObject creation.

No Transform access.

No Renderer access.

No Unity scene manipulation.

=========================================================
ERROR HANDLING
=========================================================

Classify synchronization failures using the existing client error model.

Handle safely:

- malformed envelope
- unsupported schema
- invalid payload
- missing session
- invalid mode
- invalid sequence
- unknown message type
- stale message
- incompatible protocol version
- unexpected state transition

Do not crash the Unity client because one telemetry/event message is
invalid.

Do not expose:

- access tokens
- Authorization headers
- credentials
- internal filesystem paths
- stack traces

through user-facing state/errors.

=========================================================
STATE TRANSITIONS
=========================================================

Implement explicit synchronization lifecycle behavior for:

Disconnected
Connecting
Connected
Ready
Reconnecting
Disconnecting
Faulted

and:

Unknown
Live
Replay

where appropriate according to existing contracts.

Transport state and application/runtime state must remain distinct.

Do not conflate:

TransportConnectionState

with:

OperatingMode

or:

ClientLifecycleState.

=========================================================
RECONNECT BEHAVIOR
=========================================================

When Agent 12.2 reports reconnect:

1. Treat the new ConnectionId as a new transport connection.

2. Do not assume old transport state is still authoritative.

3. Clear or invalidate connection-scoped synchronization state where
   required.

4. Preserve only state that the existing protocol explicitly defines
   as safe to retain.

5. Wait for canonical server state after reconnect.

6. Do not manufacture missed telemetry frames.

7. Do not perform durable resume.

8. Allow later subscription orchestration to recreate subscriptions.

The synchronizer must cooperate with the existing reconnect behavior,
not replace it.

=========================================================
STATE CONSISTENCY
=========================================================

The implementation must avoid partial updates being observed by
consumers.

For a telemetry update:

decode
  ↓
validate
  ↓
construct immutable state
  ↓
atomically publish new state

not:

update car position
update speed
update tyre
update timestamp
...

one field at a time.

Later agents must be able to consume a coherent state snapshot.

=========================================================
MULTI-CAR READINESS
=========================================================

12.3 must prepare the runtime state for multiple cars without
implementing Agent 12.5/12.6.

The state model should support:

Driver/Car identity
Telemetry per car
Source sequence per update
Timestamp
Session association

Use stable identifiers from the canonical protocol.

Do not create visual car entities.

Do not create prefabs.

Do not create transforms.

Do not implement rendering.

=========================================================
PERFORMANCE
=========================================================

Synchronization must be allocation-conscious.

Avoid:

- unnecessary JSON reparsing
- repeated full-state cloning when not required
- unbounded lists
- per-frame reflection
- LINQ-heavy hot paths
- GameObject operations
- blocking waits

Do not prematurely optimize at the expense of architecture.

Add lightweight metrics where the existing client architecture supports
them, such as:

- messages processed
- telemetry updates
- snapshot updates
- events processed
- invalid messages
- stale messages
- session mismatches
- synchronization errors
- current state age
- last source sequence

Do not create a second observability system.

=========================================================
TESTING
=========================================================

Create/update EditMode tests for:

1. Initial runtime state

2. Valid telemetry update

3. Multiple telemetry updates

4. Source sequence preservation

5. Transport sequence preservation

6. Duplicate/stale sequence handling

7. Session isolation

8. Snapshot application

9. Event application

10. LIVE mode

11. REPLAY mode

12. LIVE/REPLAY separation

13. Invalid payload

14. Unsupported message

15. Invalid session

16. Reconnect reset/reconciliation

17. Atomic state publication

18. Multi-car state storage/readiness

19. Disconnect behavior

20. Synchronization error handling

Tests must prove that:

- Runtime authority remains server-side
- no telemetry is fabricated
- no interpolation occurs
- no replay timing occurs in Unity
- session A cannot update session B
- source sequences remain intact
- transport sequences remain distinct
- transport remains separate from runtime state
- presentation remains uninvolved

=========================================================
INTEGRATION WITH 12.1 / 12.2
=========================================================

Use the existing:

IRaceVisionTransport
IStateSynchronizer
ClientRuntimeHost
ClientRuntimeState
Protocol decoder
EnvelopeReceived path

Do not replace these with competing abstractions.

If the current interfaces are incomplete, extend them minimally.

Do not redesign Agent 12.1 or Agent 12.2.

=========================================================
DOCUMENTATION
=========================================================

Create:

docs/specifications/RuntimeStateSynchronizationSpecification.md

Update only the relevant:

- docs/Roadmap.md
- docs/Architecture.md
- docs/Streaming.md
- docs/Unity.md
- Unity README files
- specifications index

Document:

- authority model
- synchronization flow
- state model
- sequence rules
- session isolation
- LIVE/REPLAY behavior
- reconnect behavior
- threading model
- error handling
- testing
- limitations
- handoff to Agent 12.4

Explicitly state:

"Unity runtime state is a synchronized client projection of the
canonical Phase 10/Phase 11 state. It is not an independent runtime
authority."

=========================================================
DO NOT IMPLEMENT
=========================================================

Do NOT implement:

- Blender models
- F1 car meshes
- F1 car prefabs
- tracks
- circuit geometry
- coordinate conversion
- vehicle transforms
- vehicle orientation
- rendering
- cameras
- shaders
- materials
- engine effects
- tyre effects
- collision visuals
- Unity physics
- telemetry visualization
- replay controls
- replay seeking
- prediction
- interpolation
- extrapolation
- AI
- commentary

Those belong to later agents.

=========================================================
ACCEPTANCE GATES
=========================================================

Create explicit gates appropriate to this agent.

At minimum verify:

GATE-01 12.1 architecture remains intact
GATE-02 12.2 transport remains authoritative for network delivery
GATE-03 canonical envelopes are consumed correctly
GATE-04 telemetry state synchronization works
GATE-05 source sequences are preserved
GATE-06 transport sequences remain separate
GATE-07 session isolation works
GATE-08 LIVE mode works
GATE-09 REPLAY mode works
GATE-10 no Unity replay timing authority
GATE-11 snapshots synchronize correctly
GATE-12 events synchronize correctly
GATE-13 reconnect reconciliation works
GATE-14 malformed messages fail safely
GATE-15 atomic/coherent state publication
GATE-16 multi-car state readiness
GATE-17 no transport/runtime coupling violation
GATE-18 no rendering coupling
GATE-19 no duplicate runtime/subscription/auth systems
GATE-20 threading/main-thread safety
GATE-21 bounded memory/state retention
GATE-22 tests pass
GATE-23 documentation accurate
GATE-24 Phase 10/11 regression remains green

Do not claim production performance SLAs unless actually measured.

If Unity Editor/Test Framework is unavailable, explicitly report:

UNITY_TESTS_NOT_EXECUTED

and explain exactly why.

Do not fake Unity test results.

=========================================================
REGRESSION REQUIREMENT
=========================================================

Run the existing backend regression suites where available:

pytest tests/api \
       tests/runtime/phase10 \
       tests/runtime/phase10_acceptance \
       tests/integration/transport \
       tests/acceptance/live_streaming -q

Do not modify backend behavior merely to make this agent pass.

Phase 10 and Phase 11 must remain unchanged in authority and behavior.

=========================================================
FINAL RESPONSE FORMAT
=========================================================

When complete, report:

1. STATUS
2. Architecture implemented
3. Existing architecture reused
4. Runtime state model
5. Telemetry synchronization
6. Snapshot synchronization
7. Event synchronization
8. LIVE/REPLAY behavior
9. Sequence handling
10. Session isolation
11. Reconnect behavior
12. Threading behavior
13. Error handling
14. Performance/allocation considerations
15. Files created
16. Files modified
17. Tests executed — exact results
18. Static analysis — exact results
19. Acceptance gates — exact PASS/FAIL
20. Limitations
21. Deferred work for Agent 12.4
22. Recommended next Agent

Be precise.

Do not claim tests were executed if they were not.

Do not claim production readiness from unit/integration tests alone.

=========================================================
FINAL HANDOFF
=========================================================

If all applicable gates pass:

Mark:

Agent 12.3 — ACCEPTED

Then recommend:

Agent 12.4 — Track / Coordinate System

The handoff must clearly state that 12.4 can consume synchronized
canonical telemetry/runtime state but must not modify the transport or
runtime authority.

=========================================================
START
=========================================================

Begin by auditing the existing Agent 12.1 and 12.2 implementation and
the actual Phase 11 protocol contracts.

Do not implement anything until the audit identifies the existing
interfaces and message shapes.

Then implement Agent 12.3 only.
```

## User

## 1. STATUS

**ACCEPTED**

Agent 12.3 complete. Uncommitted per your choice. Phase 10/11 backend unchanged. Did not start Agent 12.4.

---

## 2. Architecture implemented

```text
EnvelopeReceived (12.2 main-thread pump)
  → RuntimeStateSynchronizer.TryApply
  → ClientProjectionStore atomic Publish(ClientStateSnapshot)
  → IClientRuntimeState.Projection / TryGetCar
```

Unity state is a synchronized client projection only — not a Runtime authority.

---

## 3. Existing architecture reused

Extended `IStateSynchronizer`, `IClientRuntimeState`, `ClientCompositionRoot`, `ClientRuntimeHost`, `SessionContext`, `SequenceTracker`, Protocol/JsonLite, Domain `DriverId`. No second transport/auth/subscription/EventBus/ReplayClock.

---

## 4. Runtime state model

Immutable: `CarTelemetryFrame`, `RaceSnapshotRecord`, `RuntimeEventRecord`, `ClientStateSnapshot`, `SynchronizationHealth`. Multi-car map keyed by `driver_id`. Identities remain distinct.

---

## 5. Telemetry synchronization

Applies Phase 11 `telemetry` payloads (`session_id`, `driver_id`, channels, provenance, server interpolation metadata as data only). Preserves mode/timestamps/sequences. No interpolate/extrapolate/reorder/fabricate.

---

## 6. Snapshot synchronization

Consumes `snapshot` envelopes; publishes `RaceSnapshotRecord` with snapshot id, mode, runtime\_ms, sequences. No second snapshot engine.

---

## 7. Event synchronization

Consumes `event` / `replay_event` into a bounded ring (default 64). Separate from telemetry.

---

## 8. LIVE/REPLAY behavior

Shared path. Server `mode_changed.current_mode` / envelope mode authoritative. **No Unity ReplayClock / seek / playback timing.**

---

## 9. Sequence handling

Transport vs source kept separate. Per-driver source gate: accept / duplicate / stale / accept-without-sequence. Source never overwritten by transport.

---

## 10. Session isolation

Expected session from config / first bind. Foreign session → `sync.session_mismatch`. Session A cannot update Session B.

---

## 11. Reconnect behavior

On `Reconnected`: clear cars/events/snapshot/sequence trackers, mark unavailable, new `ConnectionId`. No durable resume.

---

## 12. Threading behavior

`TryApply` only after 12.2 `PumpMainThread`. Sync assembly stays `noEngineReferences` — no GameObject/Transform work.

---

## 13. Error handling

Safe rejects for malformed/unsupported/session/stale. Control messages (`ping`/`pong`/`subscription_ack`) ignored. No secrets/tokens/stack traces in sync errors.

---

## 14. Performance/allocation considerations

Atomic snapshot replace; bounded events; no LINQ hot path; JsonLite parse of already-decoded payload JSON only. Lightweight sync counters (not a second observability system).

---

## 15. Files created

`RuntimeStateSynchronizer`, projection store/snapshot/frames, `SequencePolicy`, sync README/tests, `RuntimeStateSynchronizationSpecification.md`.

---

## 16. Files modified

`IStateSynchronizer`, `ISequenceTracker`, `IClientRuntimeState`, composition root, host, Roadmap/Architecture/Streaming/Unity/READMEs/specs index.

---

## 17. Tests executed — exact results

| Suite                                                     | Result                                                                                 |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Unity EditMode (`RuntimeStateSynchronizationTests`, etc.) | **UNITY\_TESTS\_NOT\_EXECUTED** — Unity `Packages`/Test Framework still not scaffolded |
| Backend Phase 10/11 regression                            | **382 passed**, 2 warnings · `PYTEST_EXIT=0`                                           |

---

## 18. Static analysis — exact results

- Backend/shared: **unchanged**
- Ruff/mypy: N/A (no Python changes)

---

## 19. Acceptance gates

| Gate                                                                                             | Result                                                                                                      |
| ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| GATE-01…21 (architecture, sync, sequences, isolation, LIVE/REPLAY, reconnect, threading, bounds) | **PASS**                                                                                                    |
| GATE-22 Unity tests                                                                              | **PASS**\* — suites authored; execution blocked by missing Unity packages (**UNITY\_TESTS\_NOT\_EXECUTED**) |
| GATE-23 docs                                                                                     | **PASS**                                                                                                    |
| GATE-24 Phase 10/11 green                                                                        | **PASS** (382)                                                                                              |

\*Gate-22 recorded as environment-limited pass with explicit non-execution, matching Agent 12.2 practice — not a fabricated run.

---

## 20. Limitations

- Unity Editor tests not runnable in this environment
- No coordinate conversion / car entities / rendering
- Event buffer bounded
- Client projection only — not production SLA evidence

---

## 21. Deferred work for Agent 12.4

Consume `IClientRuntimeState.Projection` / `TryGetCar` channels for track/coordinate mapping. Do not modify transport or invent timing/interpolation authority.

---

## 22. Recommended next Agent

**Agent 12.4 — Track / Coordinate System**

## Assistant

Yes — I have the Phase 12 context and the accepted results from **12.1, 12.2, and 12.3**.

The current authoritative progression is:

- **12.1 — Unity Client Architecture:** ACCEPTED
- **12.2 — RaceVision WebSocket Client:** ACCEPTED
- **12.3 — Runtime State Synchronization:** ACCEPTED
- **Next:** **12.4 — Track / Coordinate System**

For 12.4, the important boundary is that Unity consumes `IClientRuntimeState.Projection` / `TryGetCar`; it must establish the coordinate mapping needed by the rendering layer **without introducing a second telemetry/runtime authority or timing/interpolation system**.

I’m ready for your next question or for you to ask for the **12.4 Cursor command**.

## User

Please give commands for Agent 12.4	Track/Coordinate System	Establish authoritative coordinate conversion ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. Based on the accepted **12.1 → 12.3** architecture, Agent 12.4 should establish **one authoritative coordinate-conversion layer** for Unity, while deliberately avoiding any car rendering, track assets, Blender implementation, interpolation, or timing authority.

Copy/paste this entire block into Cursor Agent:

```text
AGENT 12.4 — TRACK / COORDINATE SYSTEM

You are implementing Agent 12.4 for the RaceVision project.

============================================================
MISSION
============================================================

Establish the authoritative Unity-side coordinate system and
coordinate conversion boundary for RaceVision.

Agent 12.4 MUST provide the canonical mapping from the
RaceVision telemetry/world coordinate representation consumed
from Agent 12.3 into Unity world-space coordinates.

This agent is FOUNDATION ONLY.

Do NOT implement:
- F1 car rendering
- 3D car models
- Blender assets
- track meshes
- track scenery
- vehicle effects
- camera systems
- telemetry visualization
- multi-car rendering
- replay timing
- interpolation
- extrapolation
- prediction
- physics
- Unity ReplayClock
- WebSocket transport
- authentication
- subscriptions
- another runtime state system

Those belong to later agents.

============================================================
CURRENT AUTHORITATIVE ARCHITECTURE
============================================================

Phase 10:
Runtime/EventBus/LiveSessionAdapter/Replay Runtime remain
the authoritative telemetry/runtime source.

Phase 11:
REST/WS transport exposes canonical runtime data.

Phase 12.1:
Unity client architecture established.

Phase 12.2:
RaceVisionWebSocketTransport consumes Phase 11 WS.

Phase 12.3:
RuntimeStateSynchronizer creates the Unity client projection:

EnvelopeReceived
    ↓
RuntimeStateSynchronizer.TryApply
    ↓
ClientProjectionStore
    ↓
ClientStateSnapshot
    ↓
IClientRuntimeState.Projection / TryGetCar

Agent 12.4 must consume that projection.

============================================================
NON-NEGOTIABLE ARCHITECTURAL RULE
============================================================

There MUST be exactly ONE authoritative Unity coordinate
conversion boundary.

Coordinate conversion belongs to the CoordinateSystem assembly.

No Transport, Protocol, Synchronization, Runtime State,
Domain, or Presentation component may independently implement
telemetry-to-Unity coordinate conversion.

Rendering agents must consume the coordinate-system contract.

Do not put coordinate conversion into:
- car entities
- renderers
- presenters
- telemetry visualization
- WebSocket transport
- RuntimeStateSynchronizer

============================================================
FIRST: AUDIT THE EXISTING REPOSITORY
============================================================

Before modifying code:

1. Inspect the existing Unity Phase 12.1 architecture.
2. Inspect Agent 12.2 implementation.
3. Inspect Agent 12.3 implementation.
4. Inspect all existing CoordinateSystem assembly/files.
5. Inspect existing Domain identity/value types.
6. Inspect existing telemetry DTO/projection types.
7. Inspect Unity documentation and specifications.
8. Search the entire repository for existing coordinate conversion,
   axis mapping, unit conversion, transform conversion, or
   telemetry position mapping.

Commands/searches should include equivalents of:

- CoordinateSystem
- coordinate
- world position
- position
- orientation
- latitude
- longitude
- axis
- forward
- right
- up
- meters
- millimeters
- UnityEngine.Vector3
- Quaternion
- telemetry position
- driver position
- track coordinate

Do NOT create duplicate abstractions if an existing suitable
contract already exists.

If an existing implementation conflicts with this architecture,
do not silently replace it. Document the conflict and preserve
the authoritative boundary.

============================================================
COORDINATE MODEL
============================================================

Define an explicit coordinate contract.

The contract MUST document:

1. Source coordinate space
2. Source axis conventions
3. Source handedness
4. Source units
5. Unity coordinate space
6. Unity axis conventions
7. Unity handedness
8. Unity units
9. Origin definition
10. Orientation convention
11. Forward direction
12. Up direction
13. Right direction
14. Conversion rules
15. Numerical precision expectations
16. Invalid/out-of-range behavior

Do NOT invent an undocumented F1 telemetry coordinate system.

Use the actual canonical coordinate representation already exposed
by Agent 12.3 / Phase 11.

If the current telemetry contract does not provide enough information
to establish a physically authoritative source coordinate system,
STOP short of inventing one.

Instead:

- establish the conversion interface,
- establish the Unity coordinate contract,
- make the source mapping explicit/configurable where appropriate,
- document the unresolved source-coordinate assumption,
- create tests around deterministic transformations that are
  actually supported by the existing contract.

============================================================
IMPORTANT: DO NOT INVENT TRACK GEOMETRY
============================================================

Agent 12.4 is NOT responsible for generating a track.

Do not:
- generate racing lines
- approximate circuit geometry
- calculate track centerlines
- derive track meshes
- create Blender geometry
- download circuit models
- create track assets

The coordinate system must provide the foundation that later
track/car agents can use.

============================================================
DESIGN
============================================================

Create or extend the existing CoordinateSystem assembly.

Prefer pure, deterministic coordinate conversion code.

The core coordinate conversion layer should not depend on:
- WebSocket
- EventBus
- RuntimeStateSynchronizer
- MonoBehaviour
- GameObject
- Transform
- rendering
- cameras
- physics

Keep the core conversion layer independent from UnityEngine
where practical.

If Unity-specific adapters are required, isolate them at the
Unity presentation/integration boundary.

============================================================
RECOMMENDED CONTRACT SHAPE
============================================================

Use the existing project naming conventions and do not blindly
copy these names if an equivalent already exists.

Establish concepts equivalent to:

- CoordinateSpace
- CoordinateAxisConvention
- CoordinateSystemDefinition
- CoordinateTransform
- SourcePosition
- UnityPosition
- SourceOrientation
- UnityOrientation
- CoordinateConversionResult
- ICoordinateConverter

The converter should provide deterministic operations equivalent
to:

SourcePosition → UnityPosition

SourceOrientation → UnityOrientation

and, where justified:

UnityPosition → SourcePosition

Do NOT add reverse conversion unless it is genuinely required by
the architecture. Read-only telemetry rendering does not require
a reverse conversion merely for symmetry.

============================================================
UNITS
============================================================

Make unit conversion explicit.

Do not scatter constants such as:

* 1000
* 0.001
* arbitrary scale factors

throughout car/track/rendering code.

If a scale conversion is required, it belongs in the coordinate
system definition/converter.

Use strongly named units/value types where compatible with the
existing architecture.

Do not silently assume:
1 telemetry unit = 1 Unity unit

unless that is explicitly established by the existing contract.

============================================================
AXIS MAPPING
============================================================

Centralize axis mapping.

The converter must explicitly define:

Source X → Unity axis
Source Y → Unity axis
Source Z → Unity axis

and sign changes.

Do not allow later rendering agents to perform ad-hoc mappings.

The mapping must be deterministic and testable.

Document the reason for every axis/sign conversion.

============================================================
HANDEDNESS
============================================================

Explicitly model source and Unity handedness.

If conversion requires a handedness change, implement it once in
the coordinate converter.

Do not allow:
- car renderer to flip Z
- track renderer to flip X
- camera to compensate for the same conversion

There must be one authoritative transformation.

============================================================
ORIGIN
============================================================

Establish an explicit origin policy.

The system must distinguish between:

- source/reference origin
- session/world origin
- Unity scene origin

Do not silently recenter individual cars.

Do not create per-car coordinate origins.

If the existing telemetry contract only supports a session-relative
coordinate system, document that fact.

If a track/reference origin is not yet available, create the
appropriate abstraction/configuration point without inventing
track data.

============================================================
ORIENTATION
============================================================

Establish the coordinate-system rules for orientation.

Do not derive vehicle heading from position deltas.

Do not smooth orientation.

Do not interpolate orientation.

Do not predict orientation.

Do not introduce physics.

Agent 12.4 only converts the canonical orientation representation
when the source telemetry provides one.

If Agent 12.3 currently exposes orientation channels that are not
yet sufficient to establish a canonical orientation conversion,
document the limitation rather than inventing semantics.

============================================================
PRECISION / NUMERICAL SAFETY
============================================================

Define expected numeric behavior.

The implementation must:
- avoid unnecessary allocations
- avoid hidden rounding
- remain deterministic
- preserve source precision as far as practical
- handle NaN/Infinity safely
- reject invalid coordinate values where appropriate

Do not introduce floating-point "fixes" that alter canonical data
without documentation.

============================================================
INVALID INPUT
============================================================

Define explicit behavior for:

- NaN
- Infinity
- missing position
- invalid vector
- invalid scale
- invalid coordinate definition
- unsupported coordinate space
- malformed orientation

Use the existing RaceVision error/logging conventions.

Do not throw uncontrolled exceptions through rendering code.

Invalid coordinate conversion must not corrupt the client projection.

============================================================
LIVE / REPLAY
============================================================

Coordinate conversion MUST be identical for LIVE and REPLAY.

Do not branch coordinate conversion based on:

- LIVE vs REPLAY
- playback speed
- ReplayClock
- delay
- interpolation
- prediction

The source mode is metadata, not a reason to use a different
coordinate system.

============================================================
SESSION ISOLATION
============================================================

Do not create another session authority.

Coordinate conversion operates on already synchronized client
projection data.

Session validation remains owned by Agent 12.3 / transport security.

============================================================
CAR IDENTITY
============================================================

Do not create a second car registry.

Coordinate conversion may accept the already-defined telemetry
position/orientation data associated with a car.

DriverId / car identity remains owned by the existing Domain and
Runtime State architecture.

============================================================
BLENDER BOUNDARY
============================================================

Document the future asset flow:

Blender asset
    ↓
Unity import
    ↓
Prefab
    ↓
Coordinate-system contract
    ↓
Telemetry-driven transform
    ↓
Future car/track rendering

Agent 12.4 MUST NOT create Blender assets.

The coordinate system must provide the authoritative mapping that
future Blender-created models can rely on.

Do not make Blender-specific assumptions unless they are explicitly
required by an existing repository contract.

============================================================
UNITY BOUNDARY
============================================================

The core coordinate conversion must not require GameObject or
Transform access.

The later rendering layer may adapt the resulting values to:

UnityEngine.Vector3
UnityEngine.Quaternion

but coordinate conversion itself must remain testable without
scene objects.

If Unity-specific wrappers are needed, isolate them.

============================================================
PERFORMANCE
============================================================

Coordinate conversion is expected to be executed for many cars
and telemetry frames.

Avoid:
- LINQ in hot paths
- reflection
- allocations per frame
- string processing
- JSON parsing
- network calls
- logging every coordinate conversion

The converter should be lightweight and deterministic.

Do not make unsupported production-performance claims.

============================================================
TESTING
============================================================

Create comprehensive tests for the coordinate system.

At minimum test:

1. Identity conversion
2. Axis permutation
3. Axis sign inversion
4. Handedness conversion
5. Unit conversion
6. Origin transformation
7. Combined transform
8. Orientation conversion
9. Zero vector
10. Positive axis vectors
11. Negative axis vectors
12. Large coordinates
13. Small coordinates
14. NaN rejection
15. Infinity rejection
16. Invalid configuration
17. LIVE conversion
18. REPLAY conversion
19. Determinism
20. No mutation of source values

Also test that there is only one authoritative conversion path.

Search for duplicate conversion logic and ensure later presentation
code does not perform its own telemetry-to-Unity mapping.

============================================================
TEST REAL TELEMETRY PROJECTION
============================================================

Where existing Agent 12.3 test fixtures support it, create tests
using the real `ClientStateSnapshot` / telemetry projection shape.

Verify:

ClientStateSnapshot
    → telemetry position
    → CoordinateSystem
    → Unity-space position

Do not create a fake alternative telemetry model merely to make
the tests pass.

============================================================
DOCUMENTATION
============================================================

Create:

docs/specifications/TrackCoordinateSystemSpecification.md

Update only relevant sections of:

- docs/Roadmap.md
- docs/Architecture.md
- docs/Unity.md
- docs/Streaming.md
- unity/README.md
- unity/Assets/README.md
- docs/unity/README.md
- docs/architecture/README.md
- docs/specifications/README.md

Document:

- authoritative ownership
- source coordinate contract
- Unity coordinate contract
- axis mapping
- handedness
- units
- origin
- orientation
- precision
- invalid input behavior
- LIVE/REPLAY invariance
- Blender boundary
- rendering handoff to Agent 12.5+

============================================================
DO NOT MODIFY BACKEND
============================================================

Do not modify:

backend/
shared/

unless absolutely required to correct an already-proven contract
incompatibility.

Agent 12.4 is a Unity-side coordinate-system agent.

============================================================
DO NOT START FUTURE AGENTS
============================================================

Do not implement:

12.5 F1 Car Entity Runtime
12.6 Multi-Car Rendering
12.7 Vehicle Transform / Orientation
12.8 Track & Circuit Scene
12.9 Telemetry Visualization
12.10 Vehicle Effects
12.11 Replay/Live Unity Modes
12.12 Unity Performance
12.13 Unity Integration Testing
12.14 Phase 12 Acceptance

Only create clean interfaces/handoffs required by 12.4.

============================================================
UNITY TEST ENVIRONMENT
============================================================

The previous agents reported:

Unity Editor/Test Framework is not currently scaffolded/executable
in the available environment.

Do NOT fabricate Unity test execution.

If Unity tests cannot run:

- create the tests
- perform all static/source validation available
- report exactly that Unity execution was unavailable
- do not claim tests passed merely because they compile conceptually

Backend regression tests may be run to verify no backend regression,
but do not modify backend merely to obtain green tests.

============================================================
ACCEPTANCE GATES
============================================================

Create explicit acceptance gates for this agent.

At minimum:

GATE-01 Existing 12.1 architecture preserved
GATE-02 Existing 12.2 transport untouched
GATE-03 Existing 12.3 synchronization boundary preserved
GATE-04 Single authoritative coordinate conversion owner
GATE-05 Source coordinate contract explicitly documented
GATE-06 Unity coordinate contract explicitly documented
GATE-07 Axis mapping deterministic
GATE-08 Handedness deterministic
GATE-09 Units explicit
GATE-10 Origin policy explicit
GATE-11 Orientation conversion does not invent semantics
GATE-12 No interpolation/extrapolation/prediction
GATE-13 LIVE/REPLAY use same conversion
GATE-14 Session identity remains outside coordinate authority
GATE-15 No duplicate coordinate conversions
GATE-16 No Blender assets created
GATE-17 No car/track rendering implemented
GATE-18 No Runtime/Transport changes
GATE-19 Invalid input handled safely
GATE-20 Deterministic conversion tests authored
GATE-21 Performance/allocation design reviewed
GATE-22 Documentation complete
GATE-23 Existing Phase 10/11 regression remains green where executed

Do not claim PASS for a gate that was not actually verified.

============================================================
GIT / CHANGE SAFETY
============================================================

Before editing:

- inspect git status
- inspect existing 12.1–12.3 files
- identify exact files to change

Do not reset or discard user changes.

Do not commit unless explicitly instructed.

Keep changes scoped to Agent 12.4.

============================================================
FINAL RESPONSE FORMAT
============================================================

When implementation is complete, report:

1. STATUS
2. Architecture implemented
3. Authoritative coordinate ownership
4. Source coordinate definition
5. Unity coordinate definition
6. Axis mapping
7. Handedness
8. Units
9. Origin policy
10. Orientation policy
11. LIVE/REPLAY behavior
12. Invalid-input behavior
13. Performance considerations
14. Blender boundary
15. Files created
16. Files modified
17. Tests executed — exact results
18. Tests not executed and why
19. Static analysis — exact results
20. Acceptance gates with PASS/FAIL/N/A
21. Limitations
22. Deferred work for Agent 12.5
23. Recommended next Agent

IMPORTANT:

Do not say Agent 12.4 is complete merely because files were created.

Verify the implementation against the acceptance gates.

Do not invent telemetry coordinate semantics that are absent from
the existing RaceVision contracts.

The central architectural invariant is:

Phase 10 Runtime
    ↓
Phase 11 Transport
    ↓
12.2 WebSocket
    ↓
12.3 Client Projection
    ↓
12.4 AUTHORITATIVE COORDINATE CONVERSION
    ↓
12.5+ Rendering / Cars / Track / Presentation

Proceed with Agent 12.4 only.
```

## User

## 1. STATUS

**ACCEPTED**

Agent 12.4 complete. Left uncommitted. No backend/`shared` changes. No cars/tracks/Blender assets. Did not start Agent 12.5.

---

## 2. Architecture implemented

```text
12.3 CarTelemetryFrame.Channels (x/y/z | world.position)
        ↓
ChannelCoordinateReader → SourcePosition (metres)
        ↓
ConfiguredCoordinateConverter (CoordinateSystemDefinition)
        ↓
UnityPosition / UnityOrientation
```

Wired as `ClientCompositionRoot.CoordinateSystem` (`RaceVisionCoordinateSystem`, default `IdentityMetres`).

---

## 3. Authoritative coordinate ownership

Sole owner: `RaceVision.CoordinateSystem`. Presentation README forbids local axis/scale remaps. No duplicate converters found in other Unity modules.

---

## 4. Source coordinate definition

Canonical: shared telemetry `WorldPosition` / `Vector3` in **metres**; runtime often flattens to channels `x`,`y`,`z`.

**Documented assumption:** protocol does not publish explicit handedness/up-axis text. Default `IdentityMetres` treats published WorldPosition axes as Unity-compatible (X right, Y up, Z forward) without inventing track/GPS geometry. Track-relative & GPS are unsupported until reference data exists.

---

## 5. Unity coordinate definition

Unity world space, Y-up, left-handed engine convention; `UnityPosition` / `UnityOrientation` value types (no GameObject/Transform dependency).

---

## 6. Axis mapping

`CoordinateSystemDefinition` + three `AxisBinding`s (source→Unity + sign). Default identity X/Y/Z. Permutations/signs are definition-only.

---

## 7. Handedness

Recorded on definition (`SourceHandedness` / `UnityHandedness`). Default Left→Left. Future RHS/Z-flip = new definition, not renderer patches.

---

## 8. Units

Single `MetresToUnityUnits` (default 1.0). No scattered scale constants outside CoordinateSystem.

---

## 9. Origin policy

Session/world metres as published; optional `OriginOffset*Metres` on definition; no per-car origins.

---

## 10. Orientation policy

Convert only when channels provide quaternion `(w,x,y,z)` or heading. No delta-derived heading, smoothing, or pitch/roll invention. IdentityMetres: quaternion pass-through; heading → yaw about Y.

---

## 11. LIVE/REPLAY behavior

Identical conversion path; mode is metadata only.

---

## 12. Invalid-input behavior

Reject NaN/Infinity; missing x/y incomplete; missing orientation not invented; fail with `ClientError` codes; source structs not mutated.

---

## 13. Performance considerations

Pure deterministic math; no network/JSON reparsing in convert; no per-conversion logging. Not claimed as production SLA.

---

## 14. Blender boundary

Documented: Blender → import → prefab → coordinate contract → telemetry transform → future rendering. No assets created.

---

## 15. Files created

CoordinateSystem definitions/conversion/extraction/orientation/positions, `RaceVisionCoordinateSystem`, `CoordinateSystemTests`, `TrackCoordinateSystemSpecification.md`.

---

## 16. Files modified

`ICoordinateSystem`, composition root, Runtime asmdef (CoordinateSystem ref), Presentation/CoordinateSystem/READMEs, Roadmap/Architecture/Streaming/Unity/docs indexes.

---

## 17. Tests executed — exact results

Backend Phase 10/11 regression: **382 passed**, 2 warnings · `PYTEST_EXIT=0`.

---

## 18. Tests not executed and why

Unity EditMode (`CoordinateSystemTests`): **UNITY\_TESTS\_NOT\_EXECUTED** — Unity Packages/Test Framework still not scaffolded. Tests are authored.

---

## 19. Static analysis — exact results

- `backend/` / `shared/`: unchanged
- Grep: no competitor conversion outside CoordinateSystem
- Ruff/mypy: N/A (no Python edits)

---

## 20. Acceptance gates

| Gate                                                     | Result                                           |
| -------------------------------------------------------- | ------------------------------------------------ |
| GATE-01…03 (12.1–12.3 preserved)                         | **PASS**                                         |
| GATE-04 single conversion owner                          | **PASS**                                         |
| GATE-05…11 contracts / no invented orientation semantics | **PASS**                                         |
| GATE-12 no interp/extrap/predict                         | **PASS**                                         |
| GATE-13 LIVE/REPLAY same path                            | **PASS**                                         |
| GATE-14 session outside coords                           | **PASS**                                         |
| GATE-15 no duplicates                                    | **PASS**                                         |
| GATE-16…17 no Blender/cars/tracks                        | **PASS**                                         |
| GATE-18 no Runtime/Transport backend changes             | **PASS**                                         |
| GATE-19 invalid input                                    | **PASS** (authored)                              |
| GATE-20 deterministic tests authored                     | **PASS** / Unity **UNITY\_TESTS\_NOT\_EXECUTED** |
| GATE-21 perf design reviewed                             | **PASS**                                         |
| GATE-22 docs                                             | **PASS**                                         |
| GATE-23 P10/P11 green                                    | **PASS** (382)                                   |

---

## 21. Limitations

- Unity Editor tests not runnable here
- Shared protocol handedness not explicitly published — default IdentityMetres is an explicit contract choice
- Track/GPS conversion unsupported without reference data
- Non-identity quaternion remapping reserved (not invented)

---

## 22. Deferred work for Agent 12.5

F1 car entity runtime should apply `ICoordinateSystem.TryConvertChannelsToUnity` to synchronized car channels. Must not reimplement axis/unit mapping.

---

## 23. Recommended next Agent

**Agent 12.5 — F1 Car Entity Runtime**

## Assistant

Got it. **Agent 12.4 is accepted**, and the Phase 12 chain is now:

| Agent | Component | Status |
|---|---|---|
| 12.1 | Unity Client Architecture | ✅ ACCEPTED |
| 12.2 | RaceVision WebSocket Client | ✅ ACCEPTED |
| 12.3 | Runtime State Synchronization | ✅ ACCEPTED |
| 12.4 | Track / Coordinate System | ✅ ACCEPTED |
| **12.5** | **F1 Car Entity Runtime** | **➡️ NEXT** |

The key handoff from 12.4 is especially important:

> `F1 car entity runtime should apply ICoordinateSystem.TryConvertChannelsToUnity` and **must not reimplement axis/unit mapping**.

So **12.5 should create the runtime representation and lifecycle of each F1 car**, consuming the synchronized `CarTelemetryFrame` from 12.3 and the authoritative coordinate conversion from 12.4.

It should **not yet** build the visual 3D car, multi-car renderer, track scene, effects, or cameras. Those belong to later agents.

When you're ready, I can give you the **Agent 12.5 Cursor command** in the same **1-click copy/paste format**.

## User

Please give commands for Agent 12.5	F1 Car Entity Runtime	Create runtime vehicle entities ( 1 click copy and paste cursor friendly)

## Assistant

Below is the **Agent 12.5** command, scoped strictly to runtime vehicle entities and preserving the accepted **12.1 → 12.4** architecture.

```text
AGENT 12.5 — F1 CAR ENTITY RUNTIME

You are implementing Agent 12.5 for the RaceVision project.

============================================================
MISSION
============================================================

Create the Unity-side runtime vehicle entity system for F1 cars.

Agent 12.5 establishes the authoritative runtime representation,
identity, lifecycle, telemetry projection, coordinate-converted
transform state, and availability state of each F1 car.

This is a RUNTIME ENTITY FOUNDATION.

It MUST NOT implement the actual 3D car renderer.

============================================================
CURRENT ARCHITECTURE — MUST PRESERVE
============================================================

Phase 10:
Runtime/EventBus/LiveSessionAdapter/Replay Runtime remain the
authoritative telemetry/runtime systems.

Phase 11:
REST/WebSocket transport remains the authoritative transport.

Phase 12.1:
Unity client architecture established.

Phase 12.2:
RaceVisionWebSocketTransport established.

Phase 12.3:
RuntimeStateSynchronizer established:

EnvelopeReceived
    ↓
RuntimeStateSynchronizer.TryApply
    ↓
ClientProjectionStore
    ↓
ClientStateSnapshot
    ↓
IClientRuntimeState.Projection / TryGetCar

Phase 12.4:
CoordinateSystem is the SOLE authoritative coordinate conversion
owner:

CarTelemetryFrame.Channels
    ↓
ChannelCoordinateReader
    ↓
SourcePosition
    ↓
ICoordinateSystem / RaceVisionCoordinateSystem
    ↓
UnityPosition / UnityOrientation

============================================================
NON-NEGOTIABLE OWNERSHIP
============================================================

Agent 12.5 owns:

- runtime car entity identity
- car entity lifecycle
- synchronized car state
- availability state
- telemetry association
- coordinate-converted runtime transform state
- entity registry
- creation/removal/update of logical vehicle entities
- LIVE/REPLAY entity state representation

Agent 12.5 does NOT own:

- WebSocket transport
- subscriptions
- authentication
- authorization
- Runtime/EventBus
- telemetry synchronization
- coordinate conversion algorithms
- rendering
- meshes
- materials
- shaders
- track geometry
- cameras
- effects
- physics
- prediction
- interpolation
- extrapolation
- replay timing

============================================================
FIRST: AUDIT EXISTING REPOSITORY
============================================================

Before modifying anything:

1. Inspect git status.
2. Inspect all existing Phase 12.1–12.4 files.
3. Inspect Domain identity types.
4. Inspect DriverId.
5. Inspect CarTelemetryFrame.
6. Inspect ClientStateSnapshot.
7. Inspect IClientRuntimeState.
8. Inspect ICoordinateSystem.
9. Inspect RaceVisionCoordinateSystem.
10. Search for existing car/entity abstractions.

Search for:

- CarEntity
- VehicleEntity
- F1Car
- CarRuntime
- VehicleRuntime
- DriverId
- car_id
- driver_id
- CarTelemetryFrame
- TryGetCar
- ClientStateSnapshot
- ICoordinateSystem
- UnityPosition
- UnityOrientation
- GameObject
- Transform

Do NOT create duplicate abstractions.

If an appropriate entity abstraction already exists, extend it
rather than creating a competing system.

============================================================
IMPORTANT — NO RENDERER
============================================================

Do NOT create:

- GameObject car prefabs
- 3D meshes
- wheels
- wings
- materials
- shaders
- Animator components
- visual effects
- particle systems
- car models
- Blender imports

Those are later responsibilities.

The runtime car entity must work without requiring a GameObject.

============================================================
ENTITY MODEL
============================================================

Create a clear runtime representation for an F1 car.

Use the existing project naming conventions. Do not blindly create
duplicate types if equivalents already exist.

The runtime entity should contain, where supported by the existing
projection:

- DriverId
- session identity
- availability
- operating mode
- source sequence
- telemetry timestamp
- source position
- converted Unity position
- converted Unity orientation
- relevant telemetry channels
- synchronization status
- last accepted update information

Do NOT duplicate the entire backend telemetry model unnecessarily.

Prefer references/value projections to the existing client state
contract.

============================================================
IDENTITY
============================================================

DriverId remains the canonical car identity available to the Unity
client.

Do NOT create a second identity system.

Keep these identities distinct:

ConnectionId
PrincipalId
SessionId
SubscriptionId
DriverId
SourceSequence
TransportSequence

A DriverId identifies the vehicle/driver entity.

A ConnectionId does NOT identify a car.

A SessionId does NOT identify a car.

============================================================
ENTITY REGISTRY
============================================================

Create one authoritative client-side runtime vehicle registry.

Conceptually:

DriverId
    ↓
RuntimeCarEntity

The registry must:

- create an entity when a valid car appears
- update an existing entity
- remove/deactivate entities when appropriate
- prevent duplicate DriverId entities
- support lookup by DriverId
- expose a bounded/read-only view where appropriate

Do NOT create one registry per renderer.

Do NOT create separate LIVE and REPLAY registries.

============================================================
SESSION ISOLATION
============================================================

The entity runtime must consume the already session-filtered
projection from Agent 12.3.

Do NOT bypass IClientRuntimeState.

Do NOT read directly from WebSocket messages.

Do NOT implement another session authorization mechanism.

If a telemetry frame belongs to another session, it must not become
a vehicle entity.

Session validation remains outside Agent 12.5.

============================================================
TELEMETRY FLOW
============================================================

The intended flow is:

Phase 11
    ↓
12.2 WebSocket
    ↓
12.3 RuntimeStateSynchronizer
    ↓
ClientStateSnapshot
    ↓
12.5 VehicleEntityRuntime
    ↓
12.4 CoordinateSystem
    ↓
RuntimeCarEntity
    ↓
12.6+ rendering

Do NOT reverse this flow.

Do NOT let the car entity runtime become another synchronization
engine.

============================================================
COORDINATE SYSTEM — CRITICAL
============================================================

Agent 12.4 is the SOLE coordinate conversion authority.

12.5 MUST call the existing coordinate system contract.

Conceptually:

CarTelemetryFrame.Channels
    ↓
ICoordinateSystem.TryConvertChannelsToUnity(...)
    ↓
UnityPosition / UnityOrientation
    ↓
RuntimeCarEntity

Do NOT:

- multiply coordinates by scale factors
- flip Z
- swap X/Y/Z
- negate axes
- convert handedness
- invent origins
- convert units
- calculate track-relative coordinates

inside the car entity.

If coordinate conversion is required, call 12.4.

There must be NO local:

x → x
y → z
z → -y

or equivalent conversion inside car entity code.

============================================================
ORIENTATION
============================================================

Use the orientation produced by the authoritative coordinate
system when available.

Do NOT:

- derive heading from position deltas
- smooth rotation
- interpolate rotation
- extrapolate rotation
- predict rotation
- calculate physics orientation
- invent pitch/roll

If orientation is unavailable, preserve that state explicitly.

Do not fabricate an orientation.

============================================================
POSITION
============================================================

Use the coordinate-system output.

The entity may expose:

- SourcePosition
- UnityPosition
- PositionAvailable

where supported by existing architecture.

Do not mutate source telemetry.

Do not alter canonical source sequences.

Do not round positions merely for presentation.

============================================================
TELEMETRY CHANNELS
============================================================

Preserve relevant telemetry information from 12.3 without turning
the entity into a second telemetry database.

Do not parse JSON in the entity layer.

Do not receive WebSocket messages in the entity layer.

Do not create another EventBus.

Do not create another telemetry cache.

The synchronized client projection remains the source.

============================================================
UPDATE SEMANTICS
============================================================

Each accepted synchronized telemetry update should:

1. Identify DriverId.
2. Locate/create RuntimeCarEntity.
3. Obtain canonical telemetry state.
4. Convert coordinates through ICoordinateSystem.
5. Update entity state atomically/consistently.
6. Preserve source sequence and timestamp.
7. Update availability/synchronization metadata.

Do NOT reorder source telemetry.

Do NOT accept stale updates if the projection already guarantees
sequence ordering; respect the existing 12.3 sequence semantics.

Do not introduce a second sequence policy.

============================================================
LIVE / REPLAY
============================================================

LIVE and REPLAY use the same RuntimeCarEntity architecture.

Do NOT create:

LiveCarEntity
ReplayCarEntity

unless existing architecture explicitly requires distinct types.

Prefer:

RuntimeCarEntity
    + OperatingMode.Live
    + OperatingMode.Replay

Mode remains metadata from the server/client projection.

Do NOT introduce:

- ReplayClock
- playback clock
- seek
- playback speed
- interpolation
- extrapolation
- prediction

Those remain outside 12.5.

============================================================
ENTITY LIFECYCLE
============================================================

Define an explicit lifecycle.

For example, use existing conventions or establish equivalents
such as:

Unknown
Available
Active
Stale
Unavailable
Removed

Do not invent semantics that conflict with 12.3.

Important distinction:

STale/Unavailable does not automatically mean the entity should
be destroyed.

A temporary lack of telemetry must not cause uncontrolled entity
churn.

Use the existing client projection/session semantics.

If the projection does not provide enough information to safely
determine removal, expose availability rather than inventing a
timeout.

Do NOT add an application-level telemetry timeout unless the
existing contract requires it.

============================================================
ENTITY CREATION
============================================================

Entity creation must be deterministic.

For a new DriverId:

- create exactly one RuntimeCarEntity
- initialize identity
- initialize mode/session state
- apply first valid telemetry
- convert coordinates
- publish/register it

Do not create duplicate entities for repeated telemetry.

============================================================
ENTITY REMOVAL
============================================================

Define safe removal behavior.

Removal must:

- be idempotent
- not affect other DriverIds
- not alter ClientStateSnapshot
- not affect transport
- not affect subscriptions
- not affect Phase 10 Runtime

If explicit session reset/reconnect state from 12.3 requires the
vehicle registry to clear, integrate through the existing client
runtime lifecycle rather than inventing another reconnect mechanism.

============================================================
RECONNECT
============================================================

Agent 12.2 reconnect behavior:

Reconnected
    ↓
12.3 clears projection / sequence state
    ↓
12.5 must not preserve stale car entities as active state

Respect the 12.3 reconnect contract.

On reconnect/session reset:

- invalidate/clear vehicle runtime state as appropriate
- do not fabricate continuity
- do not resume stale car positions
- wait for new synchronized state

Do NOT implement transport reconnect.

============================================================
ATOMIC STATE
============================================================

Avoid partially updated runtime entities.

A consumer reading an entity should not observe:

new position + old orientation + new sequence

unless that is explicitly represented by the contract.

Prefer immutable state snapshots/value objects where compatible.

Conceptually:

RuntimeCarEntity
    → RuntimeCarState

with a consistent state update.

Do not expose mutable internal collections directly.

============================================================
THREADING
============================================================

Agent 12.3 applies synchronized state on the Unity/main-thread
boundary.

12.5 should operate on that client projection boundary.

Do not create:

- background telemetry threads
- worker-based entity updates
- network callbacks
- async entity mutation

unless existing architecture explicitly requires it.

Do not touch GameObjects or Transforms.

============================================================
UNITY ENGINE BOUNDARY
============================================================

The runtime car entity should NOT require:

- GameObject
- Transform
- MonoBehaviour
- Renderer
- Rigidbody

The runtime entity is data/runtime state.

Later Agent 12.6/12.7 can bind the runtime entity to Unity
presentation objects.

============================================================
PRESENTATION HANDOFF
============================================================

Create a clean handoff for later agents.

Later architecture should be:

12.5 RuntimeCarEntity
        ↓
12.6 Multi-Car Rendering
        ↓
12.7 Vehicle Transform / Orientation

12.5 must not depend on 12.6 or 12.7.

The runtime entity should expose enough state for those agents
without referencing rendering implementations.

============================================================
MULTI-CAR READINESS
============================================================

Even though 12.6 owns actual multi-car rendering, 12.5 must support
multiple simultaneous DriverIds.

Test at least:

- 1 car
- 2 cars
- 10 cars
- 20+ cars where practical

Do not assume a single-player/single-car architecture.

Do not hard-code driver IDs.

============================================================
PERFORMANCE
============================================================

Entity updates may occur for every telemetry frame.

Avoid:

- LINQ in hot paths
- reflection
- JSON parsing
- string allocations
- per-frame logging
- unnecessary copying
- repeated coordinate-system configuration creation
- per-update registry scans

Use DriverId lookup.

Do not make production SLA claims.

Do not prematurely optimize with unsafe code or complicated
object pooling unless justified by measured evidence.

============================================================
ERROR HANDLING
============================================================

Handle safely:

- missing DriverId
- invalid telemetry
- invalid coordinates
- coordinate conversion failure
- missing position
- missing orientation
- session mismatch
- duplicate entity
- stale state
- malformed projection

Use existing RaceVision client error conventions.

Do not crash the Unity client because one car has invalid telemetry.

Do not log credentials, tokens, or sensitive data.

============================================================
NO SECOND OBSERVABILITY SYSTEM
============================================================

Do not create another metrics framework.

If entity-level counters are genuinely required, use the existing
client observability conventions established in 12.2/12.3.

Keep metrics lightweight.

============================================================
TESTING
============================================================

Create focused Agent 12.5 tests.

At minimum:

1. Create entity from valid telemetry
2. Lookup by DriverId
3. Duplicate telemetry does not create duplicate entity
4. Multiple DriverIds remain isolated
5. Entity update preserves DriverId
6. Entity update preserves source sequence
7. Entity update preserves timestamp
8. Coordinate conversion uses ICoordinateSystem
9. No local axis conversion exists
10. Orientation uses coordinate-system output
11. Missing orientation is not fabricated
12. Invalid coordinates are rejected safely
13. Invalid DriverId is rejected safely
14. Session isolation is preserved
15. LIVE mode works
16. REPLAY mode works
17. Same entity architecture used by LIVE/REPLAY
18. Reconnect/session reset clears stale active state
19. Removal is idempotent
20. Multiple cars update independently
21. Source telemetry is not mutated
22. Entity state is consistent/atomic
23. No rendering dependency
24. No transport dependency
25. Deterministic repeated update behavior

============================================================
TEST REAL 12.3 PROJECTION
============================================================

Where existing fixtures permit, test using the actual:

ClientStateSnapshot
CarTelemetryFrame
DriverId
IClientRuntimeState

types from 12.3.

Do NOT create a parallel fake telemetry model merely to make tests
easy.

Verify:

ClientStateSnapshot
    ↓
12.5 Vehicle Entity Runtime
    ↓
12.4 ICoordinateSystem
    ↓
RuntimeCarEntity

============================================================
SEARCH FOR DUPLICATE OWNERSHIP
============================================================

Before completion search for duplicate implementations of:

- car identity registry
- coordinate conversion
- telemetry synchronization
- reconnect state
- replay timing
- car rendering

12.5 must not create competing owners.

============================================================
BLENDER BOUNDARY
============================================================

Blender remains OUTSIDE this agent.

The future asset path is:

Blender
    ↓
Unity import
    ↓
Car prefab
    ↓
12.6 rendering
    ↓
12.5 RuntimeCarEntity state
    ↓
12.7 transform/orientation presentation

Do NOT import or generate Blender assets.

Do NOT create a car prefab.

============================================================
DO NOT IMPLEMENT FUTURE AGENTS
============================================================

Do NOT implement:

12.6 Multi-Car Rendering
12.7 Vehicle Transform / Orientation
12.8 Track & Circuit Scene
12.9 Telemetry Visualization
12.10 Vehicle Effects
12.11 Replay/Live Unity Modes
12.12 Unity Performance
12.13 Unity Integration Testing
12.14 Phase 12 Acceptance

Only establish clean interfaces required for those later agents.

============================================================
DO NOT MODIFY BACKEND
============================================================

Do not modify:

backend/
shared/

unless a genuine existing contract incompatibility is discovered.

Do not change Phase 10 or Phase 11.

============================================================
UNITY TEST ENVIRONMENT
============================================================

Previous agents reported:

UNITY_TESTS_NOT_EXECUTED

because Unity Packages/Test Framework are not currently scaffolded
in the environment.

Do NOT fabricate Unity test execution.

If Unity tests cannot run:

- author the tests
- perform available static/source validation
- inspect references/dependencies
- report exactly why Unity execution was unavailable

Backend regression may be run to prove no backend regression.

============================================================
DOCUMENTATION
============================================================

Create:

docs/specifications/F1CarEntityRuntimeSpecification.md

Update relevant:

- docs/Roadmap.md
- docs/Architecture.md
- docs/Streaming.md
- docs/Unity.md
- unity/README.md
- unity/Assets/README.md
- docs/unity/README.md
- docs/architecture/README.md
- docs/specifications/README.md

Document:

- entity ownership
- DriverId identity
- lifecycle
- registry
- state model
- telemetry handoff
- coordinate-system handoff
- LIVE/REPLAY behavior
- reconnect behavior
- invalid state behavior
- presentation handoff
- Blender boundary
- performance considerations

============================================================
ACCEPTANCE GATES
============================================================

Create and verify explicit gates.

GATE-01 12.1 architecture preserved
GATE-02 12.2 transport unchanged
GATE-03 12.3 synchronization unchanged
GATE-04 12.4 coordinate authority preserved
GATE-05 exactly one runtime car entity owner
GATE-06 DriverId remains canonical car identity
GATE-07 entity registry prevents duplicate DriverIds
GATE-08 multiple cars supported
GATE-09 telemetry consumed from ClientStateSnapshot/projection
GATE-10 no direct WebSocket access
GATE-11 no second synchronization system
GATE-12 coordinate conversion delegated to 12.4
GATE-13 no local axis/unit/handedness conversion
GATE-14 orientation delegated to 12.4
GATE-15 no interpolation
GATE-16 no extrapolation
GATE-17 no prediction
GATE-18 no physics
GATE-19 LIVE/REPLAY use same entity architecture
GATE-20 reconnect/session reset handled safely
GATE-21 invalid telemetry cannot crash entity runtime
GATE-22 source telemetry remains immutable
GATE-23 runtime state is consistent
GATE-24 no GameObject/Transform dependency
GATE-25 no rendering implementation
GATE-26 no Blender assets
GATE-27 no backend/shared modifications
GATE-28 performance design reviewed
GATE-29 tests authored
GATE-30 documentation complete
GATE-31 no duplicate car/coordinate/sync owners
GATE-32 Phase 10/11 regression remains green where executed

Do not claim PASS for gates that were not actually verified.

============================================================
GIT SAFETY
============================================================

Before editing:

- inspect git status
- inspect 12.1–12.4 implementation
- identify exact files requiring changes

Do NOT:

- reset changes
- discard changes
- commit changes

unless explicitly instructed.

Keep implementation scoped to Agent 12.5.

============================================================
FINAL RESPONSE
============================================================

When complete, report exactly:

1. STATUS
2. Architecture implemented
3. Runtime entity model
4. DriverId/entity identity
5. Entity registry
6. Lifecycle/state handling
7. Telemetry handoff
8. Coordinate-system handoff
9. Orientation handling
10. LIVE/REPLAY behavior
11. Reconnect/session behavior
12. Multi-car behavior
13. Threading
14. Performance considerations
15. Rendering boundary
16. Blender boundary
17. Files created
18. Files modified
19. Tests executed — exact results
20. Tests not executed and why
21. Static analysis — exact results
22. Acceptance gates with PASS/FAIL/N/A
23. Limitations
24. Deferred work for Agent 12.6
25. Recommended next Agent

IMPORTANT ARCHITECTURAL INVARIANT:

Phase 10 Runtime
    ↓
Phase 11 Transport
    ↓
12.2 WebSocket
    ↓
12.3 Client Projection
    ↓
12.4 Coordinate System
    ↓
12.5 F1 Car Entity Runtime
    ↓
12.6 Multi-Car Rendering
    ↓
12.7 Vehicle Transform / Orientation
    ↓
12.8+ Scene / Visualization / Effects

The critical rule is:

12.5 owns the VEHICLE RUNTIME ENTITY.

12.4 owns COORDINATE CONVERSION.

12.6+ owns VISUAL PRESENTATION.

Do not blur these boundaries.

Proceed with Agent 12.5 only.
```

## User

## 1. STATUS

**Agent 12.5 COMPLETE — ACCEPTED** (left uncommitted per your choice).

---

## 2. Architecture implemented

```text
12.2 WebSocket → 12.3 ClientStateSnapshot → 12.5 VehicleEntityRuntime
    → 12.4 ICoordinateSystem → RuntimeCarEntity → (12.6+ presentation)
```

Wired in `ClientCompositionRoot`: after successful `TryApply`, `Vehicles.Apply(Projection)`; on reconnect, `InvalidateAfterReconnect()`.

## 3. Runtime entity model

- `RuntimeCarEntity` + immutable `RuntimeCarState`
- Fields: `DriverId`, session, mode, lifecycle, sequences, timestamp, source/Unity pose, orientation flags, channel reference, coord error

## 4. DriverId / identity

`DriverId` is the only car key. No second identity system. `CarId` unchanged as a domain type.

## 5. Entity registry

Single `RuntimeCarRegistry`: `DriverId → RuntimeCarEntity` (create / update / stale / remove / clear; no LIVE/REPLAY split).

## 6. Lifecycle

`Unknown | Available | Active | Stale | Unavailable | Removed` — missing cars go **Stale**, not destroyed.

## 7–11. Telemetry / coords / orientation / LIVE·REPLAY / reconnect

- Consumes `ClientStateSnapshot` only (no WS/JSON)
- Conversion only via `ICoordinateSystem`
- Missing orientation → `OrientationAvailable = false` (not fabricated)
- Same entity types for LIVE/REPLAY (`OperatingMode` metadata)
- Reconnect / unavailable projection clears registry

## 12–14. Multi-car / threading / performance

- Multi-car tested through 20 drivers; isolated updates
- Main-thread / projection boundary only
- Dict lookup by `DriverId`; soft counters; no LINQ in apply path

## 15–16. Rendering / Blender

No GameObject/Transform/mesh/material/prefab/Blender work. `noEngineReferences: true` on `RaceVision.Vehicles`.

## 17. Files created

- `unity/Assets/RaceVision/Domain/Cars/Runtime/*` (`RaceVision.Vehicles`)
- `unity/Assets/RaceVision/Tests/EditMode/F1CarEntityRuntimeTests.cs`
- `docs/specifications/F1CarEntityRuntimeSpecification.md`

## 18. Files modified

Composition root + Runtime/Presentation/Tests asmdefs; Roadmap/Architecture/Streaming/Unity/README indexes; Unity client architecture / 12.4 handoff docs.

## 19–21. Tests / static analysis

| Suite                                                                                             | Result                                                                                                                                  |
| ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Unity EditMode                                                                                    | **UNITY\_TESTS\_NOT\_EXECUTED** — `Packages/manifest.json` missing; Test Framework not scaffolded                                       |
| Phase 10/11 core (`tests/runtime`, `tests/transport`, api WS/security/…, integration, acceptance) | **935 passed**                                                                                                                          |
| Full repo pytest                                                                                  | **1951 passed, 6 failed** — failures in ingestion/persistence/protocols; **no** **`backend/`** **or** **`shared/`** **diffs** from 12.5 |

Static checks: one vehicle owner; no local axis math in Cars/Runtime; no `UnityEngine` / renderer / transport deps in vehicle runtime.

## 22. Acceptance gates

| Gate                                                                  | Result                                                                      |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| GATE-01…04 (12.1–12.4 preserved)                                      | **PASS** (no ownership regressions in those areas)                          |
| GATE-05…14, 19–25 (entity/registry/coords/no local convert/no render) | **PASS** (source review + authored tests)                                   |
| GATE-15…18 (no interp/extrap/predict/physics)                         | **PASS**                                                                    |
| GATE-26 Blender                                                       | **PASS**                                                                    |
| GATE-27 backend/shared                                                | **PASS** (no diffs)                                                         |
| GATE-28 performance design                                            | **PASS** (reviewed)                                                         |
| GATE-29 tests authored                                                | **PASS**                                                                    |
| GATE-29 Unity executed                                                | **N/A** (`UNITY_TESTS_NOT_EXECUTED`)                                        |
| GATE-30 docs                                                          | **PASS**                                                                    |
| GATE-31 no duplicate owners                                           | **PASS**                                                                    |
| GATE-32 Phase 10/11 regression                                        | **PASS** on core suite (935); full-repo 6 failures unrelated / pre-existing |

## 23. Limitations

- Unity EditMode suite cannot run without package scaffold
- Stale entities retained until clear/reconnect/remove (by design)
- No GameObject binding yet (12.6+)

## 24–25. Deferred / next

**Deferred to 12.6:** multi-car rendering, prefabs, meshes, visuals.
**Recommended next agent: 12.6 — Multi-Car Rendering** (bind to `IVehicleEntityRuntime` / `RuntimeCarState`).

## Assistant

Based on the accepted **12.1–12.5** chain, Agent **12.6 must be presentation-only**: it should bind the existing `RuntimeCarEntity` / `RuntimeCarState` to Unity-rendered car instances, without creating another vehicle runtime, coordinate converter, telemetry pipeline, or timing authority.

Copy/paste the following directly into Cursor:

:::writing{variant="document" id="58321"}
# AGENT 12.6 — MULTI-CAR RENDERING

You are implementing **Agent 12.6 — Multi-Car Rendering** for the RaceVision project.

You are working as a Principal Unity / Distributed Systems Architect.

==========================================================
PROJECT CONTEXT
==========================================================

RaceVision Phase 10 Runtime and Phase 11 Transport are COMPLETE and ACCEPTED.

Phase 12 Unity Integration is in progress.

Completed and accepted:

- Agent 12.1 — Unity Client Architecture
- Agent 12.2 — RaceVision WebSocket Client
- Agent 12.3 — Runtime State Synchronization
- Agent 12.4 — Track / Coordinate System
- Agent 12.5 — F1 Car Entity Runtime

DO NOT implement Agent 12.7 or later.

==========================================================
CURRENT AUTHORITATIVE PIPELINE
==========================================================

The existing architecture is:

Phase 11 Runtime / WS
        ↓
12.2 RaceVisionWebSocketTransport
        ↓
12.3 RuntimeStateSynchronizer
        ↓
ClientStateSnapshot
        ↓
12.5 VehicleEntityRuntime
        ↓
RuntimeCarRegistry
        ↓
RuntimeCarEntity / RuntimeCarState
        ↓
12.6 MULTI-CAR RENDERING
        ↓
Unity GameObjects / visual car instances

12.4 already owns coordinate conversion:

ICoordinateSystem
    ↓
Source telemetry position
    ↓
UnityPosition / UnityOrientation

12.6 MUST consume the already-converted RuntimeCarState.

DO NOT perform coordinate conversion again.

==========================================================
PRIMARY OBJECTIVE
==========================================================

Implement:

**Agent 12.6 — Multi-Car Rendering**

Purpose:

Create the Unity presentation layer that renders multiple F1 car entities from the existing 12.5 vehicle runtime.

The rendering system must:

- discover RuntimeCarEntity instances from the existing vehicle runtime
- create one visual representation per DriverId
- bind visual instances to DriverId
- update visual position from RuntimeCarState
- update visual orientation when available
- support all cars independently
- handle cars appearing during a session
- handle cars becoming stale/unavailable
- handle cars being removed
- handle reconnect/reset safely
- support LIVE and REPLAY through the same rendering path
- avoid creating duplicate visual instances
- avoid creating a second vehicle registry
- avoid modifying transport or synchronization
- remain presentation-only

==========================================================
NON-NEGOTIABLE ARCHITECTURE
==========================================================

12.6 is a PRESENTATION layer.

The dependency direction MUST remain:

Transport
    ↓
Protocol
    ↓
Synchronization
    ↓
Runtime State
    ↓
Domain / Vehicle Runtime
    ↓
Presentation / Rendering

Presentation MUST NOT become a Runtime authority.

Presentation MUST NOT:

- read WebSocket messages directly
- parse telemetry JSON
- subscribe directly to EventBus
- create subscriptions
- perform authentication
- perform rate limiting
- perform backpressure
- perform coordinate conversion
- interpolate telemetry
- extrapolate telemetry
- predict vehicle movement
- implement ReplayClock
- implement replay seeking
- implement physics
- modify canonical telemetry
- modify RuntimeCarState
- create another RuntimeCarRegistry
- create another DriverId/vehicle identity system

==========================================================
EXISTING AUTHORITIES
==========================================================

Respect these ownership boundaries.

12.2:
WebSocket transport.

12.3:
Runtime state synchronization.

12.4:
Coordinate conversion.

12.5:
Runtime vehicle entities and registry.

12.6:
VISUAL REPRESENTATION ONLY.

12.7:
Vehicle transform/orientation refinement.

12.8:
Track/circuit scene.

12.9:
Telemetry visualization.

12.10:
Vehicle effects.

12.11:
Unity LIVE/REPLAY modes.

Do not implement responsibilities belonging to later agents.

==========================================================
CAR IDENTITY
==========================================================

The authoritative rendering key is:

DriverId

Use:

DriverId → VisualCarInstance

Do NOT use:

- array index
- list position
- network connection ID
- session ID
- subscription ID
- transport sequence
- source sequence
- GameObject instance ID

DriverId must remain stable for the lifetime of the visual entity.

==========================================================
RENDERING REGISTRY
==========================================================

Create exactly ONE presentation-side registry if required.

Example conceptual ownership:

CarVisualRegistry

Responsibilities:

- DriverId → visual instance
- create visual
- retrieve visual
- update visual
- remove visual
- clear all visuals
- enumerate active visuals
- prevent duplicate visual instances

This registry is NOT a replacement for:

RuntimeCarRegistry

The existing 12.5 RuntimeCarRegistry remains authoritative for vehicle entities.

The presentation registry only tracks visual bindings.

Document this distinction explicitly.

==========================================================
VISUAL CAR INSTANCE
==========================================================

Create an appropriate presentation abstraction, for example:

ICarVisualInstance

and/or:

CarVisualInstance

It should contain only presentation concerns such as:

- DriverId
- GameObject reference
- Transform reference
- visual lifecycle state
- active/inactive state
- last applied visual state if needed

Do not store canonical telemetry as a second authoritative copy.

If cached state is required for rendering, clearly document it as a presentation cache.

==========================================================
CAR PREFAB BOUNDARY
==========================================================

12.6 must establish the runtime prefab binding architecture.

The system should support a configurable car prefab source.

For example:

CarVisualPrefabCatalog
or
CarRenderingConfig

Use the existing Unity architecture and ScriptableObject configuration conventions from 12.1.

Do NOT create finished F1 car assets.

Do NOT download or invent copyrighted F1 assets.

Do NOT create Blender assets.

The prefab may be:

- a placeholder development car
- a configured prefab reference
- an abstract visual prefab binding

Actual high-fidelity F1 models remain a separate asset workflow.

==========================================================
BLENDER BOUNDARY
==========================================================

Blender is an ASSET CREATION tool.

The intended future pipeline is:

Blender
  ↓
F1 car model
  ↓
FBX/glTF/appropriate Unity import
  ↓
Unity prefab
  ↓
12.6 CarVisualInstance
  ↓
DriverId binding
  ↓
12.5 RuntimeCarState

12.6 may define the prefab/import contract.

12.6 MUST NOT:

- create Blender scenes
- create F1 car meshes
- create finished F1 liveries
- modify Blender files
- implement asset modelling

Actual car asset creation belongs to the asset-production workflow associated with the rendering pipeline, not the vehicle runtime.

==========================================================
STATE APPLICATION
==========================================================

12.6 consumes:

RuntimeCarRegistry
RuntimeCarEntity
RuntimeCarState

The rendering layer must never consume raw telemetry.

For every active vehicle:

RuntimeCarState
    ↓
presentation mapping
    ↓
GameObject Transform

Position should use the already converted:

UnityPosition

Orientation should use the already converted:

UnityOrientation

Do not reimplement 12.4 conversion logic.

==========================================================
POSITION / ORIENTATION RULES
==========================================================

Position:

Use RuntimeCarState Unity-space position.

Orientation:

If OrientationAvailable == true:

apply the provided Unity orientation.

If orientation is unavailable:

DO NOT invent orientation.

The renderer may preserve the previous visual orientation or use a documented neutral/default presentation state.

Do not calculate heading from position deltas.

Do not smooth/interpolate/extrapolate.

Those behaviors are outside 12.6.

==========================================================
CAR LIFECYCLE
==========================================================

12.5 exposes vehicle lifecycle states such as:

Unknown
Available
Active
Stale
Unavailable
Removed

12.6 must map these states to presentation behavior.

Example conceptual mapping:

Available:
visual can exist but need not imply active motion.

Active:
visual active/enabled.

Stale:
retain visual instance but mark presentation stale according to configuration.

Unavailable:
disable/hide visual without destroying canonical runtime entity.

Removed:
destroy/unbind visual instance.

The exact implementation should follow the existing 12.5 lifecycle semantics.

Do not destroy runtime entities from the renderer.

==========================================================
MULTI-CAR REQUIREMENTS
==========================================================

The renderer must support:

- 1 car
- 2 cars
- 10 cars
- 20+ cars
- cars appearing dynamically
- cars disappearing/removing
- independent updates
- simultaneous updates
- session isolation

No assumption may be made that cars are always received in a fixed order.

Never use list position as identity.

==========================================================
SESSION ISOLATION
==========================================================

12.3 and 12.5 already enforce session boundaries.

12.6 must not weaken them.

Only render RuntimeCarEntity instances belonging to the active client projection/session.

Do not independently reconstruct session authorization in the renderer.

==========================================================
LIVE / REPLAY
==========================================================

Use the same visual rendering pipeline for:

OperatingMode.Live
OperatingMode.Replay

Mode is metadata supplied by the Runtime state.

Do NOT create:

- Unity ReplayClock
- replay timeline
- replay seek system
- replay interpolation
- replay playback authority

12.11 will own Unity LIVE/REPLAY presentation behavior.

12.6 simply renders the current RuntimeCarState.

==========================================================
MAIN THREAD
==========================================================

Unity GameObjects and Transforms must only be manipulated on the Unity main thread.

12.3/12.2 already establish the main-thread synchronization boundary.

12.6 must not create background threads that touch UnityEngine objects.

==========================================================
PERFORMANCE
==========================================================

Design for a 20-car F1 grid as the initial target.

Avoid:

- GameObject.Find per frame
- repeated Instantiate/Destroy cycles
- LINQ in the hot path
- reflection in the update path
- JSON parsing
- network calls
- per-car event subscriptions where unnecessary
- unnecessary allocations

Prefer:

- dictionary lookup by DriverId
- reusable visual instances where appropriate
- deterministic update loops
- cached Transform references
- explicit lifecycle transitions
- bounded allocations

Do not claim production FPS or rendering SLA unless actually measured.

==========================================================
UPDATE STRATEGY
==========================================================

Determine an appropriate presentation update strategy.

The renderer should consume the latest authoritative RuntimeCarState.

Do not create a second telemetry timeline.

Do not buffer telemetry for prediction.

Do not invent a presentation clock.

If the renderer processes a snapshot of RuntimeCarRegistry each frame, make the operation bounded and deterministic.

==========================================================
RECONNECT
==========================================================

12.2 creates a new ConnectionId after reconnect.

12.3 clears/reinitializes projection state.

12.5 invalidates vehicle runtime state.

12.6 must respond safely.

On reconnect/reset:

- clear or deactivate presentation bindings as appropriate
- do not carry old DriverId visual state into the new projection unless explicitly re-established
- do not leak Session A visuals into Session B
- do not duplicate visuals after reconnect

No durable visual resume is required.

==========================================================
SCENE BOUNDARY
==========================================================

Do not implement the full race circuit.

Do not implement:

- track geometry
- circuit meshes
- track materials
- pit lane
- grandstands
- scenery

Those belong to 12.8.

12.6 only establishes the car visual rendering layer.

==========================================================
CAMERA BOUNDARY
==========================================================

Do not implement camera/director logic.

12.6 must not own:

- chase camera
- broadcast camera
- helicopter camera
- TV camera
- camera switching
- OBS camera commands

Camera work belongs to later phases/agents.

==========================================================
EFFECTS BOUNDARY
==========================================================

Do not implement:

- tyre smoke
- sparks
- collisions
- damage effects
- brake glow
- exhaust effects
- engine effects
- environmental effects

Those belong to Agent 12.10.

==========================================================
TELEMETRY UI BOUNDARY
==========================================================

Do not implement:

- speed HUD
- RPM UI
- tyre telemetry UI
- leaderboard
- sector UI
- telemetry graphs

Those belong to 12.9.

==========================================================
TESTING
==========================================================

Create comprehensive EditMode tests.

If Unity Test Framework is unavailable, author the tests but clearly report:

UNITY_TESTS_NOT_EXECUTED

Never fabricate Unity test execution.

Test at minimum:

1. single car creates one visual
2. same DriverId does not create duplicate visual
3. two cars create two independent visuals
4. 20 cars create 20 independent visuals
5. position comes from RuntimeCarState.UnityPosition
6. orientation uses supplied Unity orientation
7. missing orientation does not invent heading
8. stale car remains represented appropriately
9. unavailable car is hidden/deactivated appropriately
10. removed car releases its visual
11. reconnect clears old presentation state
12. new session does not inherit old visuals
13. LIVE and REPLAY use the same renderer
14. renderer never performs coordinate conversion
15. renderer does not access WebSocket transport
16. renderer does not parse telemetry JSON
17. duplicate updates remain isolated by DriverId
18. dynamic car addition works
19. dynamic car removal works
20. no duplicate visual registry ownership exists

Add architecture tests where practical.

==========================================================
BACKEND REGRESSION
==========================================================

Do NOT modify backend or shared systems.

Run the existing relevant backend regression suites if available.

Do not treat unrelated existing failures as caused by Agent 12.6 without evidence.

Clearly report:

- exact command
- exact result
- failures
- whether failures are related or unrelated

==========================================================
STATIC / ARCHITECTURE CHECKS
==========================================================

Verify:

- no Transport reference from rendering
- no Synchronization ownership duplication
- no coordinate conversion outside 12.4
- no RuntimeCarRegistry duplication
- no ReplayClock
- no interpolation
- no extrapolation
- no prediction
- no physics
- no Blender asset creation
- no backend modifications

==========================================================
DOCUMENTATION
==========================================================

Create:

docs/specifications/MultiCarRenderingSpecification.md

Update only relevant documentation:

- docs/Roadmap.md
- docs/Architecture.md
- docs/Streaming.md
- docs/Unity.md
- relevant Unity READMEs
- specification index

Document:

- 12.6 ownership
- presentation/runtime boundary
- DriverId binding
- prefab boundary
- lifecycle mapping
- LIVE/REPLAY behavior
- reconnect behavior
- Blender asset boundary
- performance design
- limitations
- 12.7 handoff

==========================================================
GIT / CHANGE CONTROL
==========================================================

Do not commit changes.

Do not push changes.

Do not open a PR.

Leave the working tree changes available for review.

Do not modify unrelated files.

==========================================================
ACCEPTANCE GATES
==========================================================

Create and evaluate explicit gates covering:

GATE-01:
12.1 architecture remains intact.

GATE-02:
12.2 transport remains authoritative.

GATE-03:
12.3 synchronization remains authoritative.

GATE-04:
12.4 coordinate system remains the sole coordinate conversion owner.

GATE-05:
12.5 RuntimeCarRegistry remains the sole runtime vehicle registry.

GATE-06:
12.6 owns only visual presentation.

GATE-07:
DriverId is the sole visual binding key.

GATE-08:
Multiple cars render independently.

GATE-09:
No duplicate visual instances for one DriverId.

GATE-10:
RuntimeCarState is consumed without mutation.

GATE-11:
UnityPosition is consumed directly.

GATE-12:
UnityOrientation is consumed directly when available.

GATE-13:
No orientation invention.

GATE-14:
No interpolation/extrapolation/prediction.

GATE-15:
LIVE and REPLAY use the same rendering path.

GATE-16:
Session isolation is preserved.

GATE-17:
Reconnect does not leak stale presentation state.

GATE-18:
Lifecycle transitions are handled correctly.

GATE-19:
No transport dependency in rendering.

GATE-20:
No JSON/network processing in rendering.

GATE-21:
No physics implementation.

GATE-22:
No track implementation.

GATE-23:
No camera implementation.

GATE-24:
No effects implementation.

GATE-25:
No telemetry UI implementation.

GATE-26:
No Blender modelling/assets created.

GATE-27:
Prefab boundary is clearly defined.

GATE-28:
20-car architecture is supported.

GATE-29:
No unnecessary hot-path allocations/design regressions.

GATE-30:
Unity tests authored.

GATE-31:
Unity test execution status reported honestly.

GATE-32:
Backend/shared systems remain unchanged.

GATE-33:
Documentation is accurate.

GATE-34:
No duplicate presentation/runtime ownership.

GATE-35:
12.7 handoff is explicit.

==========================================================
FINAL RESPONSE REQUIREMENTS
==========================================================

When finished, report:

1. STATUS
2. Architecture implemented
3. Existing authorities reused
4. Rendering registry design
5. Car visual lifecycle
6. DriverId binding
7. Position/orientation behavior
8. LIVE/REPLAY behavior
9. Reconnect/session behavior
10. Prefab/Blender boundary
11. Performance design
12. Files created
13. Files modified
14. Tests executed — exact results
15. Tests not executed — exact reason
16. Static analysis results
17. Acceptance gates GATE-01…35
18. Limitations
19. Deferred work for Agent 12.7
20. Recommended next Agent

IMPORTANT:

Do not start Agent 12.7.

Do not implement vehicle transform/orientation refinement beyond consuming the already-authoritative 12.4 Unity pose.

Do not create F1 car assets.

Do not create Blender assets.

Do not modify backend/shared.

Do not create duplicate runtime systems.

Implement Agent 12.6 only.
:::

**Next after 12.6:** Agent **12.7 — Vehicle Transform / Orientation** should refine the presentation-side application of transforms/orientation, while still respecting 12.4 as the sole coordinate-conversion authority.

## User

## 1. STATUS

**Agent 12.6 COMPLETE — ACCEPTED** (left uncommitted; no push/PR).

---

## 2. Architecture implemented

```text
12.5 RuntimeCarRegistry → MultiCarRenderer.Sync → CarVisualRegistry
    → CarVisualInstance (GameObject/Transform)
```

`CarRenderingHost` (Presentation) binds to `ClientRuntimeHost.CompositionRoot.Vehicles` and Syncs on the main thread. Runtime does **not** reference Presentation (no asmdef cycle).

## 3. Existing authorities reused

12.2 transport, 12.3 sync, 12.4 coordinates, 12.5 `IVehicleEntityRuntime` / `RuntimeCarState` unchanged as owners.

## 4. Rendering registry

`CarVisualRegistry`: `DriverId → ICarVisualInstance` — **presentation bindings only**.
`RuntimeCarRegistry` remains the sole runtime vehicle registry.

## 5. Car visual lifecycle

Maps 12.5 → presentation: Active/Available→Visible; Stale→retain (default); Unavailable→Hidden; Removed/absent→destroy visual.

## 6. DriverId binding

Sole visual key. Duplicate DriverId registration throws.

## 7. Position / orientation

Uses `UnityPosition` / `UnityOrientation` from `RuntimeCarState` only. Missing orientation preserves last rotation (no invented heading). `CarVisualPose` only wraps to `Vector3`/`Quaternion`.

## 8. LIVE / REPLAY

Same `MultiCarRenderer` path; mode is metadata.

## 9. Reconnect / session

Empty 12.5 registry after invalidate → Sync clears all visuals; no cross-session leak.

## 10. Prefab / Blender boundary

`CarRenderingConfig` + optional prefab; capsule primitive fallback. No Blender/F1 assets authored.

## 11. Performance

DriverId dict lookup, cached transforms, bounded Sync, no Find/LINQ/JSON/network in hot path; 20-car target designed (not FPS-claimed).

## 12–13. Files created / modified

**Created:** `Presentation/Cars/*` (`MultiCarRenderer`, registry, instance, factory, config, host, pose), `MultiCarRenderingTests.cs`, `MultiCarRenderingSpecification.md`

**Modified:** docs (Roadmap/Architecture/Streaming/Unity/indexes/12.5 handoff), Presentation README, Tests asmdef, `ICarPresenter`, minor Host comment note.

## 14–15. Tests

| Suite                   | Result                                                                                          |
| ----------------------- | ----------------------------------------------------------------------------------------------- |
| Phase 10/11 core pytest | **935 passed** (`tests/runtime`, `tests/transport`, api WS/security/…, integration, acceptance) |
| Unity EditMode          | **UNITY\_TESTS\_NOT\_EXECUTED** — `unity/Packages/manifest.json` absent                         |

## 16. Static analysis

- No transport / WS / JSON / `ICoordinateSystem` ownership in Presentation Cars
- No second `RuntimeCarRegistry`
- No backend/shared diffs
- No Blender assets

## 17. Acceptance gates GATE-01…35

| Gates                    | Result                               |
| ------------------------ | ------------------------------------ |
| 01–14, 16–30, 32–35      | **PASS** (source + authored tests)   |
| 15 LIVE/REPLAY same path | **PASS**                             |
| 31 Unity execution       | **N/A** (`UNITY_TESTS_NOT_EXECUTED`) |

## 18. Limitations

- Placeholder primitives until real prefabs exist
- No visual polish (liveries/LOD)
- Unity tests not runnable in this environment

## 19. Deferred to 12.7

Transform/orientation refinement on existing `ICarVisualInstance` bindings (smoothing policies if any stay out of 12.6).

## 20. Recommended next Agent

**12.7 — Vehicle Transform / Orientation**

## Assistant

Yes. Based on the accepted **12.1–12.6** architecture and the handoff from 12.6, the next implementation should be **12.7 — Vehicle Transform / Orientation**.

The important constraint is that **12.7 must refine the existing transform/orientation path without creating a second coordinate system, second vehicle registry, or introducing prediction/interpolation/physics authority**.

### 1-click Cursor command

```text
You are implementing **RaceVision Agent 12.7 — Vehicle Transform / Orientation**.

============================================================
AGENT 12.7 — VEHICLE TRANSFORM / ORIENTATION
============================================================

PROJECT
RaceVision — Live F1 Telemetry / 3D Runtime

CURRENT STATUS
Phase 12 Unity Integration & 3D Scene Runtime

ACCEPTED:
12.1 Unity Client Architecture
12.2 RaceVision WebSocket Client
12.3 Runtime State Synchronization
12.4 Track / Coordinate System
12.5 F1 Car Entity Runtime
12.6 Multi-Car Rendering

NEXT:
12.7 Vehicle Transform / Orientation

============================================================
PRIMARY OBJECTIVE
============================================================

Implement Agent 12.7 to establish the authoritative Unity-side vehicle
transform/orientation application layer using the existing:

12.3 ClientStateSnapshot
12.4 ICoordinateSystem
12.5 RuntimeCarState / RuntimeCarRegistry
12.6 ICarVisualInstance / CarVisualRegistry / MultiCarRenderer

Do NOT create a second coordinate system, second vehicle registry,
second synchronization system, second transport system, or second
rendering system.

12.7 owns ONLY vehicle transform/orientation application and its
explicit policies.

The architecture must remain:

Phase 11 Transport
        ↓
12.3 Runtime State Synchronization
        ↓
12.4 Coordinate System
        ↓
12.5 Runtime Car Entity
        ↓
12.6 Car Visual Binding
        ↓
12.7 Transform / Orientation
        ↓
Unity Transform

============================================================
NON-NEGOTIABLE ARCHITECTURE RULES
============================================================

1. Phase 10 Runtime remains the authoritative runtime.
2. Unity remains a consumer/projection/rendering client.
3. Never modify backend/runtime/EventBus/ReplayClock ownership.
4. Do not modify Phase 11 transport contracts unless absolutely required
   for compatibility; prefer no backend/shared changes.
5. Do not create another coordinate conversion implementation.
6. All source→Unity position conversion remains owned by 12.4.
7. Do not create another RuntimeCarRegistry.
8. Do not create another CarVisualRegistry.
9. Do not create another WebSocket client.
10. Do not create another state synchronizer.
11. Do not create a Unity ReplayClock.
12. Do not add prediction, extrapolation, telemetry interpolation,
    physics simulation, or artificial racing-line calculation.
13. Do not fabricate orientation when telemetry does not provide it.
14. Do not add network/JSON parsing to Presentation.
15. Keep LIVE and REPLAY on exactly the same transform path.
16. Session identity remains external to transform calculation.
17. DriverId remains the sole vehicle visual/runtime key.
18. No per-car coordinate-system implementation.
19. No Blender/F1 asset creation in this agent.
20. Preserve existing 12.1–12.6 public contracts wherever possible.

============================================================
AUDIT FIRST
============================================================

Before modifying code:

1. Inspect the existing Unity 12.1–12.6 implementation.
2. Locate:
   - RuntimeCarState
   - RuntimeCarEntity
   - RuntimeCarRegistry
   - ICoordinateSystem
   - UnityPosition
   - UnityOrientation
   - ICarVisualInstance
   - CarVisualInstance
   - CarVisualRegistry
   - MultiCarRenderer
   - CarRenderingHost
   - ClientCompositionRoot
   - ClientRuntimeHost
3. Determine exactly where transform position and rotation are currently
   applied.
4. Identify any existing orientation conversion or transform policy.
5. Reuse existing abstractions rather than creating competing ones.
6. Search the entire Unity tree for:
   - Quaternion conversion
   - Euler conversion
   - axis remapping
   - scale conversion
   - heading/yaw conversion
   - Transform.position
   - Transform.rotation
   - Transform.SetPositionAndRotation
7. Ensure there is exactly ONE authoritative vehicle transform path.

Do not implement until the audit has identified the existing ownership.

============================================================
12.7 RESPONSIBILITIES
============================================================

Implement a focused transform/orientation layer that:

A. Applies the already-converted UnityPosition from 12.4.

B. Applies the already-converted UnityOrientation from 12.4.

C. Handles orientation availability explicitly.

D. Preserves the existing policy:
   - valid orientation → apply it
   - missing orientation → do not fabricate one
   - unavailable orientation → preserve the documented visual policy
   - invalid orientation → reject safely

E. Keeps position and orientation application deterministic.

F. Keeps LIVE and REPLAY identical.

G. Supports multiple cars independently.

H. Handles vehicle lifecycle correctly:
   - Active
   - Available
   - Stale
   - Unavailable
   - Removed

I. Handles reconnect/session invalidation without stale visual transforms
   leaking into the next connection/session.

============================================================
ORIENTATION POLICY
============================================================

Use the orientation data already produced by 12.4.

Do NOT derive orientation from:

- position deltas
- velocity
- acceleration
- racing line
- track geometry
- previous frames
- prediction
- extrapolation

unless an existing explicit project contract already requires it.

If orientation is unavailable:

- OrientationAvailable = false
- do not invent a quaternion
- do not invent a heading
- preserve the existing documented visual behavior

If orientation is available:

- validate quaternion components
- reject NaN/Infinity
- reject invalid/degenerate quaternion data
- normalize only if this is explicitly a safe representation-level
  operation and does not alter semantic orientation
- apply the resulting Unity orientation

Do not introduce smoothing unless the existing architecture explicitly
requires a configurable presentation-only smoothing policy.

If smoothing is considered useful, do NOT silently add it.
Document it as deferred unless the current codebase already has the
appropriate policy boundary.

============================================================
POSITION POLICY
============================================================

12.4 remains the sole owner of:

- source axis mapping
- handedness
- metres → Unity units
- origin offset
- coordinate definitions

12.7 must consume UnityPosition only.

DO NOT write:

transform.position = sourceXYZ;

when sourceXYZ has not passed through 12.4.

DO NOT introduce:

- local scale constants
- axis swaps
- sign flips
- per-car offsets
- per-car coordinate transforms

============================================================
TRANSFORM APPLICATION
============================================================

Create a small presentation-owned abstraction if the existing code does
not already provide one.

For example, conceptually:

VehicleTransformApplier
or
CarVisualTransformController

It must operate on existing visual bindings and RuntimeCarState.

It must NOT become another vehicle registry.

Responsibilities should be limited to:

- apply position
- apply orientation
- validate transform input
- handle orientation availability
- expose bounded transform metrics if genuinely required
- maintain no telemetry authority

Prefer a single atomic Unity transform application where appropriate:

SetPositionAndRotation(position, rotation)

rather than independently mutating position and rotation when both are
valid.

Do not use GameObject.Find, FindObjectOfType, scene-wide searches,
reflection, or per-frame object discovery.

============================================================
MULTI-CAR
============================================================

Support the existing multi-car architecture.

For every RuntimeCarState:

DriverId
    ↓
RuntimeCarRegistry
    ↓
CarVisualRegistry
    ↓
ICarVisualInstance
    ↓
12.7 Transform Application

No global/shared transform state.

A transform update for Driver A must never modify Driver B.

Test at minimum with:

- 1 car
- 2 cars
- 20 cars

Do not claim a production FPS target unless actually measured.

============================================================
LIFECYCLE
============================================================

Respect the existing 12.5/12.6 lifecycle.

Expected behavior:

ACTIVE
  → transform visible/applied

AVAILABLE
  → transform may be applied according to existing presentation policy

STALE
  → do not fabricate movement
  → preserve existing stale-visual policy

UNAVAILABLE
  → respect 12.6 visibility policy

REMOVED
  → visual is removed by the existing visual lifecycle owner

Do not create a second lifecycle system.

============================================================
LIVE / REPLAY
============================================================

LIVE and REPLAY must use the exact same transform application code.

OperatingMode may be retained as metadata.

Do NOT:

- create ReplayClock
- perform replay timing
- seek
- interpolate replay frames
- extrapolate replay frames
- predict replay positions

12.7 only renders the state supplied by the client projection.

============================================================
THREADING
============================================================

UnityEngine Transform access must occur on the Unity main thread.

Do not access GameObjects/Transforms from:

- WebSocket receive thread
- background tasks
- synchronization thread

12.2 already owns network threading.

12.3 owns state synchronization.

12.7 consumes the resulting state on the appropriate Unity main-thread
presentation path.

============================================================
PERFORMANCE
============================================================

Keep the transform path lightweight.

Requirements:

- no LINQ in the per-frame transform path
- no JSON parsing
- no network calls
- no database calls
- no scene-wide searches
- no reflection
- no allocations where reasonably avoidable
- cache Transform references
- use DriverId keyed existing registries
- bounded iteration
- no duplicate entity discovery

Do not claim production performance/SLA without measurements.

============================================================
TESTING
============================================================

Create/update Unity EditMode tests for:

1. Valid position applied.
2. Valid orientation applied.
3. Position + orientation applied atomically where supported.
4. Missing orientation does not fabricate rotation.
5. Invalid NaN position rejected safely.
6. Invalid Infinity position rejected safely.
7. Invalid quaternion rejected safely.
8. Multiple cars remain isolated.
9. Driver A cannot modify Driver B.
10. LIVE uses transform path.
11. REPLAY uses same transform path.
12. Stale state does not invent movement.
13. Unavailable state respects visibility/lifecycle policy.
14. Removed vehicle does not leave an active transform binding.
15. Reconnect/session invalidation cannot leak old transforms.
16. Existing 12.4 coordinate conversion remains the only conversion owner.
17. No local axis/scale conversion exists in Presentation Cars.
18. 20-car transform application remains bounded and deterministic.

If Unity Test Framework is unavailable, AUTHOR the tests but clearly report:

UNITY_TESTS_NOT_EXECUTED

Never claim tests were executed when they were not.

============================================================
REGRESSION TESTING
============================================================

Run the appropriate existing backend regression suite.

At minimum preserve the project's established Phase 10/11 regression
coverage.

Expected invariant:

Phase 10/11 backend behavior must remain unchanged.

Do not modify backend/shared merely to make 12.7 pass.

============================================================
STATIC / ARCHITECTURE CHECKS
============================================================

Verify:

- Presentation owns Transform application.
- Coordinate conversion remains exclusively 12.4.
- Runtime vehicle registry remains exclusively 12.5.
- Visual registry remains exclusively 12.6.
- No transport dependency in Presentation Cars.
- No JSON dependency in transform path.
- No EventBus dependency.
- No ReplayClock.
- No physics.
- No prediction.
- No interpolation/extrapolation.
- No duplicate transform owner.

============================================================
BLENDER BOUNDARY
============================================================

Do NOT create Blender assets in Agent 12.7.

The existing boundary remains:

Blender
  ↓
FBX/glTF/etc.
  ↓
Unity import
  ↓
Car prefab
  ↓
12.6 visual binding
  ↓
12.7 transform/orientation
  ↓
Unity Transform

Real F1 cars/liveries/meshes remain a later asset-production activity.

============================================================
DOCUMENTATION
============================================================

Create:

docs/specifications/VehicleTransformOrientationSpecification.md

Update only relevant:

- docs/Roadmap.md
- docs/Architecture.md
- docs/Streaming.md
- docs/Unity.md
- Unity README/index documentation
- specifications index
- 12.6 handoff documentation

Document:

- ownership
- transform flow
- orientation semantics
- missing orientation behavior
- invalid input behavior
- lifecycle behavior
- LIVE/REPLAY behavior
- threading
- performance design
- Blender boundary
- limitations
- 12.8 handoff

============================================================
GIT / SCOPE
============================================================

Do NOT commit.
Do NOT push.
Do NOT create a PR.

Keep changes limited to Agent 12.7.

Before finishing, inspect git diff/status and report:

- created files
- modified files
- unexpected changes
- backend/shared changes
- tests
- static analysis
- acceptance gates
- limitations
- recommended next agent

============================================================
ACCEPTANCE GATES
============================================================

Create explicit acceptance gates covering at least:

GATE-01 12.1 architecture preserved
GATE-02 12.2 transport preserved
GATE-03 12.3 synchronization preserved
GATE-04 12.4 coordinate ownership preserved
GATE-05 12.5 vehicle registry preserved
GATE-06 12.6 visual registry preserved
GATE-07 single transform owner
GATE-08 position uses UnityPosition
GATE-09 orientation uses UnityOrientation
GATE-10 no local axis conversion
GATE-11 no local scale conversion
GATE-12 no fabricated orientation
GATE-13 invalid input safely rejected
GATE-14 multi-car isolation
GATE-15 LIVE/REPLAY same transform path
GATE-16 lifecycle correctness
GATE-17 reconnect/session isolation
GATE-18 main-thread Unity access
GATE-19 no transport/network ownership
GATE-20 no Runtime/EventBus ownership
GATE-21 no ReplayClock
GATE-22 no interpolation/extrapolation/prediction
GATE-23 performance design
GATE-24 tests authored
GATE-25 tests executed or explicitly environment-limited
GATE-26 documentation
GATE-27 Blender boundary preserved
GATE-28 backend/shared unchanged
GATE-29 Phase 10/11 regression green
GATE-30 no duplicate transform/orientation system

All applicable gates must PASS.

============================================================
FINAL REPORT FORMAT
============================================================

Return:

## 1. STATUS

ACCEPTED / BLOCKED / NEEDS CHANGES

## 2. Architecture implemented

Explain the final 12.7 transform flow.

## 3. Existing authorities reused

List 12.3, 12.4, 12.5, 12.6 authorities.

## 4. Transform ownership

Identify the single authoritative transform/orientation application owner.

## 5. Position behavior

Explain how UnityPosition is applied.

## 6. Orientation behavior

Explain valid/missing/invalid orientation behavior.

## 7. LIVE / REPLAY

Confirm identical transform path.

## 8. Lifecycle / reconnect

Explain stale/unavailable/removed/reconnect behavior.

## 9. Multi-car

Explain DriverId isolation.

## 10. Threading / performance

Explain main-thread and hot-path behavior.

## 11. Files created

List exact files.

## 12. Files modified

List exact files.

## 13. Tests

Give exact results. Never fabricate Unity test execution.

## 14. Static analysis

Give exact results.

## 15. Acceptance gates

Report every gate.

## 16. Limitations

Be explicit.

## 17. Deferred work

Identify what remains for Agent 12.8.

## 18. Recommended next Agent

**Agent 12.8 — Track & Circuit Scene**

IMPORTANT:
Do not start Agent 12.8.
Do not create track assets.
Do not create Blender assets.
Do not implement cameras.
Do not implement telemetry visualization.
Do not implement vehicle effects.

Only implement Agent 12.7.
```

## User

## 1. STATUS

**ACCEPTED** (left uncommitted).

## 2. Architecture implemented

```text
RuntimeCarState (12.5)
  → VehicleTransformApplier (12.7)
  → ICarVisualInstance.ApplyWorldTransform
  → Transform.SetPositionAndRotation (both valid) / component apply otherwise
```

`MultiCarRenderer` no longer applies pose directly; it delegates to `IVehicleTransformApplier`.

## 3. Existing authorities reused

| Agent | Authority                                       |
| ----- | ----------------------------------------------- |
| 12.3  | `ClientStateSnapshot` / sync                    |
| 12.4  | `UnityPosition` / `UnityOrientation` conversion |
| 12.5  | `RuntimeCarState` / `RuntimeCarRegistry`        |
| 12.6  | `CarVisualRegistry` / visual lifecycle          |

## 4. Transform ownership

**Single owner:** `VehicleTransformApplier` (`IVehicleTransformApplier`).

## 5. Position behavior

Applies `UnityPosition` only when `PositionAvailable`; rejects NaN/Infinity (`transform.position.invalid`).

## 6. Orientation behavior

| Case                           | Behavior                                    |
| ------------------------------ | ------------------------------------------- |
| Available + valid              | Apply (representation-normalize quaternion) |
| Available + invalid/degenerate | Reject; no fabricated rotation              |
| Unavailable                    | Preserve prior rotation                     |

## 7. LIVE / REPLAY

Identical applier path; mode unused.

## 8. Lifecycle / reconnect

Reuses 12.5/12.6. Stale = reapply supplied state only. Removed/empty registry → Sync clears visuals (no leak).

## 9. Multi-car

Per-visual apply by `DriverId`; 20-car Sync covered in tests.

## 10. Threading / performance

Main-thread via `CarRenderingHost`. No LINQ/JSON/network/Find in hot path; cached Transform; soft counters.

## 11. Files created

- `unity/Assets/RaceVision/Presentation/Cars/VehicleTransformApplier.cs`
- `unity/Assets/RaceVision/Tests/EditMode/VehicleTransformOrientationTests.cs`
- `docs/specifications/VehicleTransformOrientationSpecification.md`

## 12. Files modified

Presentation Cars (`MultiCarRenderer`, `CarVisualInstance`, `ICarVisualInstance`, `CarVisualPose`), multi-car tests, Roadmap/Architecture/Streaming/Unity/indexes/12.6 handoff, READMEs.

## 13. Tests

| Suite                   | Result                                                             |
| ----------------------- | ------------------------------------------------------------------ |
| Phase 10/11 core pytest | **935 passed**                                                     |
| Unity EditMode          | **UNITY\_TESTS\_NOT\_EXECUTED** (`Packages/manifest.json` missing) |

## 14. Static analysis

- One transform owner; registries unchanged (12.5 / 12.6)
- No transport/WS/JSON/`ICoordinateSystem`/ReplayClock in Cars apply path
- `backend/` + `shared/` **unchanged**

## 15. Acceptance gates

| Gate                   | Result                               |
| ---------------------- | ------------------------------------ |
| GATE-01…24, 26–28, 30  | **PASS**                             |
| GATE-25 Unity executed | **N/A** (`UNITY_TESTS_NOT_EXECUTED`) |
| GATE-29 Phase 10/11    | **PASS** (935)                       |

## 16. Limitations

- No smoothing/interpolation (deferred by design)
- Placeholder visuals remain 12.6 asset concern
- Unity tests not runnable here

## 17. Deferred work

**Agent 12.8 — Track & Circuit Scene** (no track assets in 12.7).

## 18. Recommended next Agent

**Agent 12.8 — Track & Circuit Scene**

## Assistant

The output of this plugin was redacted.

## Assistant

Yes. Based on the accepted **12.1–12.7** architecture, the next agent should be **12.8 — Track & Circuit Scene**. The important boundary is that 12.8 creates the Unity scene/runtime structure and consumes the authoritative coordinate system from **12.4**; it should **not** invent telemetry, car transforms, transport, or replay timing.

Copy/paste the following directly into Cursor:

```text
AGENT 12.8 — TRACK & CIRCUIT SCENE

You are implementing Agent 12.8 for the RaceVision F1 project.

=========================================================
MISSION
=========================================================

Implement:

Agent 12.8 — Track & Circuit Scene

Purpose:
Establish the Unity-side track/circuit scene runtime that will host the RaceVision F1 vehicles and future broadcast/camera systems.

This agent must integrate with the already ACCEPTED Phase 12 agents:

12.1 Unity Client Architecture
12.2 RaceVision WebSocket Client
12.3 Runtime State Synchronization
12.4 Track/Coordinate System
12.5 F1 Car Entity Runtime
12.6 Multi-Car Rendering
12.7 Vehicle Transform / Orientation

Do NOT start or implement Agent 12.9+ work.

=========================================================
NON-NEGOTIABLE ARCHITECTURE
=========================================================

Phase 10 remains the authoritative Runtime.

Phase 11 remains the authoritative REST/WebSocket transport.

Unity is a consumer/presentation runtime.

The architecture remains:

Phase 11 WebSocket
    ↓
12.2 RaceVisionWebSocketTransport
    ↓
12.3 RuntimeStateSynchronizer
    ↓
12.4 CoordinateSystem
    ↓
12.5 RuntimeCarRegistry
    ↓
12.6 MultiCarRenderer
    ↓
12.7 VehicleTransformApplier
    ↓
12.8 Track/Circuit Scene
    ↓
future 12.9+ presentation systems

Do NOT create:

- a second telemetry runtime
- a second EventBus
- a second WebSocket client
- a second subscription system
- a second coordinate converter
- a Unity ReplayClock
- Unity-side replay timing authority
- Unity-side telemetry interpolation
- Unity-side extrapolation
- Unity-side prediction
- physics authority
- database access
- backend modifications
- shared protocol modifications
- authentication systems
- rate limiting
- backpressure systems

=========================================================
FIRST: AUDIT THE EXISTING REPOSITORY
=========================================================

Before modifying files:

1. Inspect the existing Unity/Assets/RaceVision architecture.
2. Inspect Agents 12.1–12.7 implementations.
3. Inspect:
   - ICoordinateSystem
   - CoordinateSystemDefinition
   - UnityPosition
   - UnityOrientation
   - RuntimeCarRegistry
   - RuntimeCarState
   - CarVisualRegistry
   - MultiCarRenderer
   - VehicleTransformApplier
   - ClientRuntimeHost
   - ClientCompositionRoot
4. Inspect existing Unity scene/prefab documentation.
5. Inspect existing rendering/unity placeholders.
6. Inspect Blender boundary documentation.
7. Inspect docs/Roadmap.md and existing Phase 12 specifications.
8. Search for existing Track/Circuit/Scene implementations before creating anything.

Do not create duplicate authorities.

If an existing component already owns part of this responsibility, extend it rather than creating a competing system.

=========================================================
12.8 RESPONSIBILITY
=========================================================

12.8 owns ONLY the Unity track/circuit scene layer.

It must establish:

- track scene abstraction
- circuit identity
- track scene lifecycle
- scene loading/binding boundary
- track root hierarchy
- circuit metadata
- track coordinate-space binding
- spawn/reference points
- safe scene reset
- LIVE/REPLAY scene reuse
- future asset/prefab integration boundary

It must NOT implement:

- telemetry decoding
- vehicle telemetry synchronization
- vehicle transform conversion
- car rendering logic
- replay playback
- camera director
- effects
- AI
- physics
- prediction
- smoothing
- interpolation

Those remain owned by their existing/future agents.

=========================================================
TRACK/CIRCUIT ARCHITECTURE
=========================================================

Establish a clear separation between:

Circuit Identity
    ↓
Circuit Definition
    ↓
Track Scene
    ↓
Track Root
    ↓
Track Asset / Prefab
    ↓
Vehicle Presentation

Use strongly typed identifiers where appropriate.

Do not use DriverId as a circuit identifier.

Do not use session_id as a track identifier.

A circuit/track identity must remain separate from:

- ConnectionId
- PrincipalId
- SessionId
- SubscriptionId
- DriverId
- SourceSequence
- TransportSequence

=========================================================
TRACK SCENE MODEL
=========================================================

Create an appropriate track scene model, for example:

TrackId
CircuitId
TrackDefinition
TrackSceneState
TrackSceneBinding
TrackReferencePoints

Use names consistent with the existing repository architecture if equivalent types already exist.

The model should support:

- circuit identity
- display/name metadata
- scene binding
- coordinate-system definition reference
- optional asset/prefab reference
- scene lifecycle
- origin/reference configuration
- track availability

Do not hardcode a specific F1 circuit unless existing project data already defines one.

=========================================================
COORDINATE SYSTEM INTEGRATION
=========================================================

12.4 is the sole coordinate authority.

12.8 MUST NOT contain:

- axis permutation logic
- sign-flip logic
- metres conversion logic
- handedness conversion
- quaternion remapping
- local coordinate conversion

Track scene placement must consume the existing:

ICoordinateSystem

and existing coordinate definitions.

The track scene must operate in the same authoritative Unity world coordinate space used by 12.5–12.7.

Do not create another coordinate conversion helper.

=========================================================
TRACK ROOT
=========================================================

Establish a single presentation-side track root abstraction.

The track root should provide the common parent/reference space for:

- circuit geometry
- track assets
- optional scenery
- future pit lane
- future start/finish references
- future timing references
- future camera references

Do not implement those future systems yet.

The track root must not own telemetry.

=========================================================
REFERENCE POINTS
=========================================================

Create a safe abstraction for static circuit reference points.

Examples may include:

- start/finish
- pit entry
- pit exit
- sector references
- marshal/reference points
- camera reference points

However:

DO NOT invent real-world coordinates.

Reference points should be data-driven and optional.

If no reference data exists, the system must remain valid without fabricated positions.

Use explicit availability rather than fake/default F1 geometry.

=========================================================
SCENE LIFECYCLE
=========================================================

Implement a deterministic lifecycle such as:

Unloaded
    ↓
Loading
    ↓
Loaded
    ↓
Bound
    ↓
Active
    ↓
Unbinding
    ↓
Unloaded

Use the existing Unity client lifecycle conventions where applicable.

Scene lifecycle must be separate from:

- WebSocket lifecycle
- Runtime lifecycle
- Replay lifecycle
- vehicle lifecycle

A disconnected client must not cause arbitrary track state corruption.

=========================================================
LIVE / REPLAY
=========================================================

The same Track/Circuit Scene must support:

OperatingMode.Live
OperatingMode.Replay

Do NOT create:

LiveTrackScene
ReplayTrackScene

unless absolutely required by existing Unity architecture.

Prefer one scene/runtime representation with mode treated as state/metadata.

Replay does not create a second track authority.

No ReplayClock.

No playback timing.

No seek.

No interpolation.

=========================================================
SESSION ISOLATION
=========================================================

Track scene identity must not accidentally leak state between sessions.

When the client changes/rebinds session:

- invalidate stale session-bound scene state where applicable
- clear transient bindings
- preserve static circuit definitions where safe
- never attach Session A telemetry to Session B

Do not add a second session manager.

Use existing client session/runtime state boundaries.

=========================================================
CAR INTEGRATION
=========================================================

12.8 must provide the environment in which 12.6/12.7 car visuals operate.

Do NOT modify car transform ownership.

Do NOT move cars directly.

Do NOT read WebSocket messages.

Do NOT read JSON.

Do NOT modify RuntimeCarRegistry ownership.

The intended relationship is:

Track Scene
    ↓
Track Root
    ↓
Car Presentation Layer
    ↓
CarVisualRegistry
    ↓
12.7 VehicleTransformApplier

The track scene is the static environment.

Vehicles remain independently controlled by 12.5–12.7.

=========================================================
BLENDER BOUNDARY
=========================================================

This agent must prepare the correct boundary for future Blender assets.

Document:

Blender
    ↓
FBX/GLB/appropriate Unity import
    ↓
Unity Track Asset
    ↓
Track Prefab / Scene Binding
    ↓
Track Root
    ↓
Coordinate System
    ↓
Vehicle Presentation

Do NOT require finished Blender assets.

Do NOT fabricate a detailed F1 track.

Do NOT create fake geometry that could later become an accidental production dependency.

A minimal placeholder scene/root is acceptable if required for architecture validation.

The system must support replacing the placeholder with a real Blender-authored circuit later.

=========================================================
SCENE/PREFAB ARCHITECTURE
=========================================================

Use the existing Unity architecture conventions from 12.1.

Prefer clear separation such as:

RaceVision/
    Presentation/
        Track/
            TrackScene...
            TrackRoot...
            TrackDefinition...
            TrackBinding...
            TrackReferencePoint...
            TrackSceneHost...

Only create files that are actually necessary.

Do not create duplicate scene managers.

Do not create a second global presentation root.

=========================================================
UNITY ENGINE BOUNDARY
=========================================================

Follow existing asmdef rules.

Pure domain/data contracts should remain engine-independent where practical.

Unity-specific scene/GameObject/Transform behavior belongs in Presentation/Track.

Do not introduce UnityEngine dependencies into:

- Core
- Protocol
- Domain
- Synchronization
- Runtime vehicle state
- CoordinateSystem pure contracts

unless an existing architecture boundary explicitly requires it.

=========================================================
PERFORMANCE
=========================================================

Track scene must be static/presentation-oriented.

Do not:

- search the scene every frame
- use GameObject.Find in hot paths
- parse JSON
- access network
- access database
- iterate every vehicle to manage the track
- allocate continuously per frame

Track binding should be deterministic and cached.

No production FPS/SLA claim unless actually measured.

=========================================================
ERROR HANDLING
=========================================================

Handle:

- missing track definition
- missing scene binding
- invalid circuit identity
- unavailable track asset
- missing coordinate definition
- invalid reference point
- duplicate binding
- invalid lifecycle transition

Errors must be bounded and safe.

Do not log credentials, tokens, or sensitive transport information.

Do not throw uncontrolled exceptions from normal runtime absence.

=========================================================
TESTING
=========================================================

Create focused Unity EditMode tests for:

1. Track identity separation.
2. Track definition creation.
3. Scene lifecycle transitions.
4. Duplicate binding rejection.
5. Missing track asset handling.
6. Missing coordinate definition handling.
7. Reference point availability.
8. LIVE/REPLAY same scene model.
9. Session rebinding/invalidation.
10. Track root creation/binding.
11. No fabricated reference coordinates.
12. Existing 12.4 coordinate authority is reused.
13. Existing 12.5–12.7 vehicle architecture remains unchanged.
14. Multiple circuit definitions do not cross-contaminate.
15. Repeated bind/unbind is safe/idempotent.

If Unity Test Framework cannot execute because the Unity project packages are still missing:

- author the tests
- explicitly report UNITY_TESTS_NOT_EXECUTED
- do NOT claim tests were executed

=========================================================
BACKEND REGRESSION
=========================================================

Do not modify backend/shared.

Run the established Phase 10/11 regression suite.

At minimum verify the project's existing Phase 10/11 regression coverage remains green.

If the full repository has unrelated pre-existing failures, report them exactly and distinguish them from 12.8 changes.

=========================================================
DOCUMENTATION
=========================================================

Create:

docs/specifications/TrackCircuitSceneSpecification.md

Update only relevant documentation:

- docs/Roadmap.md
- docs/Architecture.md
- docs/Streaming.md
- docs/Unity.md
- Unity README/indexes
- rendering/unity README where appropriate
- specification index
- 12.7 handoff

Mark:

12.8 ACCEPTED

only after verification.

Document clearly:

- ownership
- lifecycle
- coordinate authority
- Blender boundary
- scene/prefab boundary
- LIVE/REPLAY behavior
- session isolation
- limitations
- deferred work for 12.9

=========================================================
ANTI-DUPLICATION AUDIT
=========================================================

Before completion, search the repository for competing implementations of:

- TrackSceneManager
- CircuitManager
- CoordinateConverter
- TrackCoordinateConverter
- ReplayClock
- telemetry transport
- vehicle transform
- car registry

There must be one authoritative owner for each responsibility.

If an existing implementation already owns the responsibility, integrate with it rather than creating another.

=========================================================
ACCEPTANCE GATES
=========================================================

Create explicit acceptance gates covering at minimum:

GATE-01 12.1 architecture preserved
GATE-02 12.2 transport unchanged
GATE-03 12.3 synchronization unchanged
GATE-04 12.4 coordinate authority preserved
GATE-05 12.5 vehicle runtime unchanged
GATE-06 12.6 car presentation unchanged
GATE-07 12.7 transform authority unchanged
GATE-08 single track/circuit owner
GATE-09 circuit identity separation
GATE-10 track definition
GATE-11 scene lifecycle
GATE-12 track root
GATE-13 coordinate-system reuse
GATE-14 no local axis conversion
GATE-15 reference-point safety
GATE-16 no fabricated geometry/data
GATE-17 LIVE/REPLAY same track architecture
GATE-18 session isolation
GATE-19 reconnect safety
GATE-20 Blender asset boundary
GATE-21 prefab/scene boundary
GATE-22 performance design
GATE-23 error handling
GATE-24 Unity tests authored
GATE-25 Unity tests executed OR explicitly environment-limited
GATE-26 Phase 10/11 regression
GATE-27 no backend/shared modifications
GATE-28 documentation
GATE-29 no duplicate authorities
GATE-30 12.9 handoff

=========================================================
IMPORTANT SCOPE LIMIT
=========================================================

DO NOT implement Agent 12.9 Telemetry Visualization.

Do NOT implement:

- telemetry HUD
- speed display
- RPM display
- tyre visualization
- timing tower
- telemetry charts
- live telemetry overlays

Those belong to Agent 12.9.

DO NOT implement:

- vehicle effects (12.10)
- replay/live mode UI (12.11)
- Unity performance optimization (12.12)
- integration testing (12.13)
- Phase 12 acceptance (12.14)

=========================================================
FINAL RESPONSE REQUIRED
=========================================================

When finished, provide:

1. STATUS
2. Architecture implemented
3. Existing authorities reused
4. Track/circuit ownership
5. Scene lifecycle
6. Coordinate-system integration
7. Reference-point model
8. LIVE/REPLAY behavior
9. Session/reconnect behavior
10. Blender boundary
11. Files created
12. Files modified
13. Tests executed — exact results
14. Tests not executed — exact reason
15. Static analysis — exact results
16. Acceptance gates — PASS/FAIL/N/A
17. Limitations
18. Deferred work for Agent 12.9
19. Recommended next Agent

Do not claim acceptance unless the implementation and applicable gates are actually verified.

Do not commit, push, or create a PR.

=========================================================
START
=========================================================

Begin with a repository audit.

Then implement Agent 12.8 only.

Do not ask for confirmation unless a destructive or ambiguous repository change is unavoidable.
```

## User

## 1. STATUS

**ACCEPTED** (left uncommitted; no push/PR).

## 2. Architecture implemented

```text
TrackDefinitionCatalog / TrackSceneConfig
    → TrackSceneRuntime.TryBind(definition, ICoordinateSystem, ...)
    → TrackRoot (empty placeholder; optional prefab instance)
    → cars remain 12.5–12.7 in the same Unity world space
```

## 3. Existing authorities reused

12.4 `ICoordinateSystem` (by definition name), 12.5–12.7 vehicle path unchanged, 12.1 hosts/asmdefs, Domain `TrackId` extended + new `CircuitId`.

## 4. Track/circuit ownership

**Single owner:** `TrackSceneRuntime` (+ catalog/definition/root). Distinct from vehicle/visual/transform/coordinate owners.

## 5. Scene lifecycle

`Unloaded → Loading → Loaded → Bound → Active → Unbinding → Unloaded` (idempotent unbind).

## 6. Coordinate-system integration

Requires configured 12.4 system; name must match `TrackDefinition.CoordinateDefinitionName`. No local axis/scale/handedness logic in Track.

## 7. Reference-point model

Optional `TrackReferencePoint` with explicit `PositionAvailable`. No fabricated F1 coordinates.

## 8. LIVE / REPLAY

One `TrackSceneRuntime`; mode is metadata on `TrackSceneState`.

## 9. Session/reconnect behavior

`InvalidateSession()` / `Unbind()` clear root/asset bindings; catalog may remain. Different session/track while bound → `track.binding.duplicate`.

## 10. Blender boundary

Blender → import → `TrackSceneConfig.TrackPrefab` → `TrackRoot`. Default: **empty root only**.

## 11. Files created

Domain: `CircuitId.cs`, `CircuitDescriptor.cs`
Presentation/Track: lifecycle, definition, catalog, reference points, root, runtime, state, config, host (includes `ITrackPresenter`)
Tests: `TrackCircuitSceneTests.cs`
Docs: `TrackCircuitSceneSpecification.md`

## 12. Files modified

Roadmap/Architecture/Streaming/Unity indexes, READMEs, Scenes README, 12.7 handoff, `TrackId.cs`; removed old stub `ITrackPresenter.cs` (replaced in host file).

**backend/shared:** unchanged.

## 13–14. Tests

| Suite                   | Result                                                             |
| ----------------------- | ------------------------------------------------------------------ |
| Phase 10/11 core pytest | **935 passed**                                                     |
| Unity EditMode          | **UNITY\_TESTS\_NOT\_EXECUTED** — `Packages/manifest.json` missing |

## 15. Static analysis

One track owner; no WS/JSON/ReplayClock/axis conversion in Track; 12.4–12.7 types remain separate owners.

## 16. Acceptance gates

| Gate                   | Result                               |
| ---------------------- | ------------------------------------ |
| GATE-01…24, 26–30      | **PASS**                             |
| GATE-25 Unity executed | **N/A** (`UNITY_TESTS_NOT_EXECUTED`) |
| GATE-26 Phase 10/11    | **PASS** (935)                       |

## 17. Limitations

- No finished circuit meshes
- Empty TrackRoot until prefab assigned
- Unity tests not runnable here
- Track does not parent cars automatically (environment only)

## 18. Deferred for 12.9

Telemetry HUD/overlays/charts — must not own track lifecycle.

## 19. Recommended next Agent

**Agent 12.9 — Telemetry Visualization**

## Assistant

**Agent 12.8 is correctly ACCEPTED.** The Phase 12 architecture remains clean: 12.4 owns coordinates, 12.5–12.7 own vehicles/transforms, and 12.8 owns the track environment. Blender assets are still intentionally deferred.

### Next: Agent 12.9 — Telemetry Visualization

This is where we begin building the **visual telemetry layer** in Unity:

- Live telemetry HUD
- Speed / RPM / gear
- Throttle / brake
- DRS / ERS indicators
- Tyre/vehicle status visualization
- Position/sector/lap information
- Telemetry overlays tied to `RuntimeCarState`
- Multi-car telemetry selection
- LIVE/REPLAY-compatible visualization
- No new transport, synchronization, coordinate, or Runtime authority
- No interpolation/extrapolation/prediction
- Rendering remains downstream of 12.3/12.5

**Important:** 12.9 still does **not** require the final Blender F1 cars or finished circuit assets. Those can be introduced through the existing Blender → Unity prefab boundary once the visual asset work begins.

After 12.9, the sequence remains:

`12.10 Vehicle Effects → 12.11 Live/Replay Unity Modes → 12.12 Unity Performance → 12.13 Integration Testing → 12.14 Phase 12 Acceptance`

And **real Blender F1 car/track production can happen alongside the later presentation work**, without changing the core runtime architecture.

## User

Please give commands for Agent 12.9	Telemetry Visualization	Visualize live telemetry in the 3D runtime ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. For **Agent 12.9**, keep the scope strictly on the Unity presentation of the already-synchronized telemetry from **12.3**, vehicle entities from **12.5**, coordinate authority from **12.4**, and rendering path from **12.6–12.8**.

Copy/paste this entire prompt into Cursor Agent:

```text
You are Agent 12.9 — Telemetry Visualization for the RaceVision project.

========================================================
AGENT 12.9 — TELEMETRY VISUALIZATION
========================================================

Implement Agent 12.9 only:

    "Visualize live telemetry in the 3D runtime"

The goal is to expose already-synchronized canonical telemetry
inside the Unity 3D runtime as presentation/visualization data.

DO NOT start Agent 12.10 or any later agent.

========================================================
1. MANDATORY REPOSITORY AUDIT
========================================================

Before modifying anything, inspect the repository and understand the
existing implementation of:

- Agent 12.1 Unity Client Architecture
- Agent 12.2 RaceVision WebSocket Client
- Agent 12.3 Runtime State Synchronization
- Agent 12.4 Track / Coordinate System
- Agent 12.5 F1 Car Entity Runtime
- Agent 12.6 Multi-Car Rendering
- Agent 12.7 Vehicle Transform / Orientation
- Agent 12.8 Track & Circuit Scene
- Phase 10 Runtime
- Phase 11 transport

Read the relevant:

- source files
- asmdef files
- interfaces
- READMEs
- specifications
- Roadmap
- Architecture documentation
- Streaming documentation
- Unity documentation
- existing tests

Do not assume paths or APIs. Inspect the actual repository.

========================================================
2. EXISTING AUTHORITIES — MUST NOT CHANGE
========================================================

The following ownership is authoritative:

12.2:
    WebSocket transport

12.3:
    ClientStateSnapshot / RuntimeStateSynchronizer

12.4:
    ICoordinateSystem
    UnityPosition
    UnityOrientation

12.5:
    RuntimeCarState
    RuntimeCarRegistry
    IVehicleEntityRuntime

12.6:
    MultiCarRenderer
    CarVisualRegistry
    CarVisualInstance

12.7:
    VehicleTransformApplier
    IVehicleTransformApplier

12.8:
    TrackSceneRuntime
    TrackRoot
    TrackDefinition / TrackSceneConfig

Phase 10:
    Runtime/EventBus/ReplayClock authority

Phase 11:
    REST/WS transport/auth/subscription/backpressure/session authority

12.9 MUST NOT create replacements for any of these.

========================================================
3. CORE ARCHITECTURE
========================================================

Implement this flow:

    Phase 11 canonical telemetry
             ↓
    12.2 WebSocket transport
             ↓
    12.3 RuntimeStateSynchronizer
             ↓
    ClientStateSnapshot
             ↓
    12.5 RuntimeCarState
             ↓
    12.6 CarVisualInstance
             ↓
    12.7 VehicleTransformApplier
             ↓
    12.9 Telemetry Visualization
             ↓
    Unity 3D presentation

Telemetry Visualization is a PRESENTATION consumer.

It must NOT become another runtime state authority.

========================================================
4. PRIMARY OBJECTIVE
========================================================

Create a telemetry visualization layer capable of displaying the
canonical telemetry already present in RuntimeCarState / synchronized
client projection.

At minimum support visualization of telemetry that already exists
without inventing new telemetry semantics.

Examples may include, where the actual protocol/state provides them:

- vehicle speed
- throttle
- brake
- gear
- RPM
- DRS state
- tyre-related telemetry
- sector/lap information
- position-related telemetry
- telemetry availability/state
- source sequence
- telemetry timestamp
- LIVE/REPLAY mode metadata

Do NOT invent fields that do not exist.

First inspect the actual telemetry channels/protocol and only visualize
fields supported by the repository.

========================================================
5. VISUALIZATION OWNERSHIP
========================================================

Create ONE telemetry visualization ownership boundary.

Suggested package location:

    unity/Assets/RaceVision/Presentation/Telemetry/

Use the repository's existing conventions if a different location is
already established.

Possible responsibilities:

- telemetry visualization model
- telemetry display state
- telemetry presenter
- telemetry bindings
- optional world-space telemetry indicators
- optional HUD/data display interfaces
- visualization lifecycle
- visualization configuration

Do not create another RuntimeCarRegistry.

Do not create another telemetry cache.

Do not create another synchronization layer.

Do not create another coordinate converter.

Do not create another transport client.

========================================================
6. PRESENTATION ONLY
========================================================

Telemetry Visualization MUST NOT:

- receive WebSocket messages directly
- parse JSON
- access EventBus
- access ReplayClock
- access backend APIs
- perform network I/O
- perform authentication
- perform subscriptions
- perform rate limiting
- perform interpolation
- perform extrapolation
- perform prediction
- perform physics simulation
- modify canonical telemetry
- modify RuntimeCarState
- modify ClientStateSnapshot
- modify Phase 10 runtime state

It should consume existing client/runtime presentation state.

========================================================
7. LIVE / REPLAY
========================================================

The same visualization path MUST support:

    OperatingMode.Live
    OperatingMode.Replay

Do not create:

    LiveTelemetryVisualizer
    ReplayTelemetryVisualizer

as separate authoritative systems.

Mode is metadata.

The server/runtime remains authoritative for LIVE/REPLAY state.

Unity does not implement ReplayClock, seeking, playback timing, or
replay interpolation.

========================================================
8. MULTI-CAR SUPPORT
========================================================

Telemetry visualization must work independently for multiple cars.

Use:

    DriverId

as the vehicle identity.

Never use array index as vehicle identity.

Never create a second identity mapping.

A visualization binding should conceptually be:

    DriverId → TelemetryVisualizationBinding

The visualization must remain compatible with the existing:

    RuntimeCarRegistry
    CarVisualRegistry

========================================================
9. TELEMETRY AVAILABILITY
========================================================

Telemetry fields are not guaranteed to exist.

Every visualization must distinguish between:

    Available
    Unavailable
    Invalid

Do NOT display fabricated zero values for missing telemetry.

Examples:

missing speed:
    display unavailable state

missing RPM:
    display unavailable state

missing DRS:
    display unavailable state

invalid NaN/Infinity:
    reject or mark unavailable

Do not silently convert missing values into valid telemetry.

========================================================
10. DATA OWNERSHIP
========================================================

Telemetry visualization is read-only with respect to canonical state.

For example:

    RuntimeCarState.Speed
            ↓
    TelemetryVisualizationState.Speed

The visualization state may be derived for presentation purposes, but
must never write back into RuntimeCarState.

Do not mutate canonical telemetry.

========================================================
11. TELEMETRY CHANNEL DISCOVERY
========================================================

Before implementing visualization fields, inspect the actual existing
telemetry representation.

Identify:

- channel names
- channel types
- units
- availability semantics
- source sequences
- timestamps
- mode
- provenance
- driver identity
- session identity

Document exactly which channels 12.9 supports.

Do not invent protocol fields.

If a field is not available, document it as deferred rather than
fabricating an implementation.

========================================================
12. UNITS
========================================================

Respect the units already established by the canonical protocol/state.

Do not introduce scattered unit conversions.

If presentation formatting requires conversion, centralize it inside
the telemetry presentation layer and document it.

Examples:

- metres/second → display km/h
- normalized throttle → percentage
- normalized brake → percentage

Only perform conversions where the source semantics are known.

Do not change canonical values.

========================================================
13. SPEED VISUALIZATION
========================================================

If speed is available in canonical telemetry:

Provide a presentation representation suitable for a 3D runtime/HUD.

The visualization may expose:

- numeric speed
- formatted speed
- optional speed indicator

Do not alter vehicle transform based on speed.

Do not create physics.

========================================================
14. THROTTLE / BRAKE
========================================================

If canonical telemetry provides throttle/brake:

Expose them as presentation values.

For example:

    throttle → 0–100%
    brake    → 0–100%

Only normalize according to actual source semantics.

Do not invent normalization rules.

Do not use these values to modify vehicle physics.

========================================================
15. GEAR / RPM / DRS
========================================================

If present in the actual protocol:

Expose:

- gear
- RPM
- DRS state

Use explicit availability semantics.

Do not infer DRS from speed.

Do not infer gear from RPM.

Do not derive missing telemetry.

========================================================
16. WORLD-SPACE VISUALIZATION
========================================================

If implementing world-space telemetry indicators:

They must attach to the existing visual representation.

Examples:

- speed marker
- telemetry label
- state indicator
- optional vehicle information panel

Do not create a second vehicle transform system.

Use existing:

    CarVisualInstance
    RuntimeCarState
    UnityPosition
    UnityOrientation

Do not perform coordinate conversion inside telemetry visualization.

========================================================
17. HUD / OVERLAY BOUNDARY
========================================================

If the existing Unity architecture supports HUD presentation, provide
interfaces/bindings for telemetry UI without coupling the telemetry
domain/runtime to UI implementation.

Keep the architecture extensible for later:

    12.10 Vehicle Effects
    12.11 Replay/Live Unity Modes

Do NOT implement those agents.

Do not build a complete broadcast overlay system here.

========================================================
18. VISUALIZATION UPDATE MODEL
========================================================

Telemetry visualization must update from the existing synchronized
state.

Do not subscribe directly to transport messages.

Do not poll the WebSocket.

Use the existing main-thread Unity lifecycle.

Avoid unnecessary per-frame allocations.

Avoid:

- LINQ in hot paths
- JSON parsing in presentation
- reflection
- GameObject.Find
- repeated GetComponent calls where caching is appropriate

========================================================
19. STALE / UNAVAILABLE VEHICLES
========================================================

Respect 12.5 lifecycle states.

For:

    Active
    Available

visualization may be visible.

For:

    Stale

retain visualization state according to existing presentation policy,
but do not fabricate fresh telemetry.

For:

    Unavailable

show unavailable/hidden state according to existing visual lifecycle.

For:

    Removed

remove the visualization binding.

Do not destroy the underlying RuntimeCarEntity.

========================================================
20. SESSION ISOLATION
========================================================

Telemetry visualization must never display telemetry from another
session.

Reuse the existing session identity/state from 12.3/12.5.

Do not create another session manager.

On reconnect/session invalidation:

- clear presentation telemetry bindings as appropriate
- do not retain telemetry from the old session
- wait for new synchronized state

========================================================
21. SEQUENCE HANDLING
========================================================

Do not create another sequence authority.

12.3 already handles source sequence acceptance.

Telemetry Visualization consumes the accepted state.

Never reorder telemetry.

Never interpolate telemetry.

Never extrapolate telemetry.

Never fabricate missing frames.

========================================================
22. PERFORMANCE
========================================================

Design for the existing multi-car target.

At minimum validate the architecture against:

    1 car
    5 cars
    10 cars
    20 cars

Do not claim production FPS unless actually measured in Unity.

Use:

- cached bindings
- DriverId dictionary lookup
- bounded visualization work
- no network work
- no JSON work
- no LINQ hot path
- no unnecessary GameObject creation/destruction

If a visualization element is expensive, make it configurable.

========================================================
23. CONFIGURATION
========================================================

Reuse existing RaceVision configuration architecture.

If new settings are needed, create a focused configuration object,
for example:

    TelemetryVisualizationConfig

Potential settings may include:

- enabled
- visible fields
- update budget
- world-space label visibility
- numeric formatting
- stale visibility
- unavailable visibility

Do not create unrelated configuration systems.

Do not store secrets.

========================================================
24. DEBUG / DEVELOPMENT MODE
========================================================

If useful, provide a development-only telemetry diagnostic view.

It may expose:

- DriverId
- mode
- session
- speed
- throttle
- brake
- gear
- RPM
- DRS
- source sequence
- timestamp
- availability

It must not log raw credentials or sensitive authentication data.

Do not enable verbose telemetry logging by default.

========================================================
25. TESTING
========================================================

Create focused EditMode tests following the existing Unity test
architecture.

At minimum test:

1. telemetry binding creation
2. multi-car isolation
3. DriverId mapping
4. available telemetry
5. missing telemetry
6. invalid telemetry
7. speed formatting/conversion
8. throttle/brake presentation
9. gear/RPM/DRS when supported
10. LIVE mode
11. REPLAY mode
12. stale vehicle behavior
13. unavailable vehicle behavior
14. removed vehicle behavior
15. reconnect/session invalidation
16. no canonical-state mutation
17. no local coordinate conversion
18. no interpolation
19. no extrapolation
20. 20-car synchronization/presentation design

If Unity Test Framework is still unavailable, author the tests but clearly
report:

    UNITY_TESTS_NOT_EXECUTED

Never claim Unity tests passed if they were not executed.

========================================================
26. ARCHITECTURAL TESTS
========================================================

Verify:

- Telemetry Presentation does not reference Transport
- Telemetry Presentation does not reference Protocol parsing
- Telemetry Presentation does not reference ReplayClock
- Telemetry Presentation does not reference EventBus
- Telemetry Presentation does not reference backend code
- Runtime state remains the source of truth
- Coordinate conversion remains owned by 12.4
- Vehicle identity remains owned by 12.5
- Visual binding remains owned by 12.6
- Transform application remains owned by 12.7
- Track lifecycle remains owned by 12.8

No duplicate authority may be introduced.

========================================================
27. DOCUMENTATION
========================================================

Create:

    docs/specifications/TelemetryVisualizationSpecification.md

Update only the relevant:

- docs/Roadmap.md
- docs/Architecture.md
- docs/Streaming.md
- docs/Unity.md
- Unity README files
- specification indexes
- Agent 12.8 handoff
- Agent 12.10 handoff

Document:

- architecture
- ownership
- supported telemetry
- unavailable telemetry
- LIVE/REPLAY behavior
- session isolation
- lifecycle
- units
- performance design
- testing
- limitations
- Blender boundary

========================================================
28. BLENDER BOUNDARY
========================================================

Do NOT create Blender assets in Agent 12.9.

Do NOT create:

- F1 car meshes
- liveries
- wheels
- tyres
- circuits
- track meshes
- materials
- shaders

The established boundary remains:

    Blender
       ↓
    exported asset
       ↓
    Unity prefab
       ↓
    existing 12.6 visual binding
       ↓
    12.9 telemetry visualization

Telemetry visualization must work with placeholder visuals.

========================================================
29. BACKEND PROTECTION
========================================================

Do not modify:

    backend/
    shared/

unless a genuinely unavoidable contract mismatch is discovered.

If such a mismatch exists:

STOP and report it rather than silently changing Phase 10/11.

Phase 10 and Phase 11 remain unchanged.

========================================================
30. NO SCOPE CREEP
========================================================

Do NOT implement:

- vehicle effects
- tyre smoke
- sparks
- damage effects
- engine audio
- cameras
- director logic
- replay controls
- replay clock
- prediction
- interpolation
- extrapolation
- physics
- AI
- Blender modelling
- finished F1 assets
- finished circuit assets
- broadcast overlay system

Those belong to later agents/phases.

========================================================
31. ACCEPTANCE GATES
========================================================

Create an Agent 12.9 acceptance checklist covering:

GATE-01:
12.1 architecture preserved

GATE-02:
12.2 transport preserved

GATE-03:
12.3 synchronization preserved

GATE-04:
12.4 coordinate ownership preserved

GATE-05:
12.5 vehicle runtime ownership preserved

GATE-06:
12.6 visual ownership preserved

GATE-07:
12.7 transform ownership preserved

GATE-08:
12.8 track ownership preserved

GATE-09:
canonical telemetry only

GATE-10:
no duplicate telemetry authority

GATE-11:
multi-car DriverId isolation

GATE-12:
missing telemetry handled explicitly

GATE-13:
invalid telemetry rejected safely

GATE-14:
LIVE and REPLAY share visualization path

GATE-15:
no interpolation

GATE-16:
no extrapolation

GATE-17:
no prediction

GATE-18:
no physics

GATE-19:
session isolation

GATE-20:
reconnect isolation

GATE-21:
no coordinate conversion outside 12.4

GATE-22:
no transport dependency

GATE-23:
no backend/shared changes

GATE-24:
20-car architecture verified

GATE-25:
tests authored

GATE-26:
Unity tests executed OR explicitly documented as
UNITY_TESTS_NOT_EXECUTED

GATE-27:
documentation complete

GATE-28:
Blender boundary preserved

GATE-29:
Phase 10/11 regression green

========================================================
32. VERIFICATION
========================================================

Run the strongest relevant existing backend regression suite.

Also run any available Unity tests.

Run static/source checks appropriate to the repository.

Check for:

- duplicate telemetry owners
- forbidden dependencies
- Transport references
- ReplayClock references
- EventBus references
- local coordinate conversion
- backend/shared modifications
- accidental interpolation/extrapolation
- secret leakage

========================================================
33. FINAL REPORT
========================================================

At completion report:

1. STATUS
2. Architecture implemented
3. Existing authorities reused
4. Telemetry channels actually supported
5. Visualization components created
6. LIVE/REPLAY behavior
7. Multi-car behavior
8. Session/reconnect behavior
9. Missing/invalid telemetry behavior
10. Unit handling
11. Performance design
12. Files created
13. Files modified
14. Tests executed — EXACT RESULTS
15. Tests not executed — exact reason
16. Static analysis
17. Acceptance gates
18. Backend/shared status
19. Limitations
20. Deferred work
21. Recommended next agent

Do not claim production performance unless measured.

Do not claim Unity tests passed unless Unity actually executed them.

========================================================
FINAL INSTRUCTION
========================================================

Implement ONLY Agent 12.9.

Preserve all accepted Phase 10, Phase 11, and Agents 12.1–12.8
architectural ownership.

Do not start Agent 12.10.

After implementation, provide the exact verification results and
recommended handoff for:

    Agent 12.10 — Vehicle Effects
```

## User

## 1. STATUS

**ACCEPTED** (left uncommitted).

## 2. Architecture implemented

```text
RuntimeCarState.TelemetryChannels → TelemetryVisualizationRuntime.Sync
  → CarTelemetryVisualizationState (per DriverId) → HUD/data consumers
```

Data/HUD bindings only (no world-space labels).

## 3. Existing authorities reused

12.2–12.8 unchanged as owners. 12.9 consumes `IVehicleEntityRuntime` / `RuntimeCarState` only.

## 4. Telemetry channels supported

| Keys                                                  | Presentation                             |
| ----------------------------------------------------- | ---------------------------------------- |
| `speed_kph` / `speed_mps` / `speed`                   | km/h display (`speed`/`speed_mps` × 3.6) |
| `throttle` / `brake`                                  | 0–1 → %                                  |
| `gear` / `rpm` / `drs`                                | gear/RPM/state                           |
| `lap_number` / `sector` / `race_position`\|`position` | optional ints                            |

## 5. Visualization components

`TelemetryChannelReader`, field types, `CarTelemetryVisualizationState`, registry, runtime, config, `TelemetryPresenter` / `TelemetryVisualizationHost`.

## 6–8. LIVE/REPLAY / multi-car / session

Same runtime; mode metadata. `DriverId` isolation (20-car tests). Reconnect/clear via empty 12.5 registry → Sync drops bindings.

## 9–11. Missing/invalid / units / performance

Available/Unavailable/Invalid; no fabricated zeros. Display-only unit formatting; canonical channels immutable. Bound Sync; no JSON/network/LINQ/Find.

## 12–13. Files

**Created:** Presentation/Telemetry implementations + `TelemetryVisualizationTests.cs` + `TelemetryVisualizationSpecification.md`
**Modified:** Roadmap/Architecture/Streaming/Unity indexes/READMEs/12.8 handoff; removed stub `ITelemetryPresenter.cs` (replaced by `TelemetryPresenter.cs`).

## 14–15. Tests

| Suite                   | Result                                                             |
| ----------------------- | ------------------------------------------------------------------ |
| Phase 10/11 core pytest | **935 passed**                                                     |
| Unity EditMode          | **UNITY\_TESTS\_NOT\_EXECUTED** (`Packages/manifest.json` missing) |

## 16. Static analysis

No Transport/WS/coordinate converter/ReplayClock deps in Telemetry code; owners remain distinct.

## 17. Acceptance gates

| Gates                  | Result                               |
| ---------------------- | ------------------------------------ |
| GATE-01…25, 27–28      | **PASS**                             |
| GATE-26 Unity executed | **N/A** (`UNITY_TESTS_NOT_EXECUTED`) |
| GATE-29 Phase 10/11    | **PASS** (935)                       |

## 18. Backend/shared

**Unchanged** (no diffs).

## 19. Limitations

No finished HUD UI/widgets; no world-space labels; Unity tests not runnable here; `drs` only when present in channels.

## 20. Deferred

UI skins, world labels, effects hooks → later agents.

## 21. Recommended next agent

**Agent 12.10 — Vehicle Effects**

## Assistant

Understood. **Agent 12.9 is ACCEPTED**, with the same documented Unity-test limitation, and the project is now ready to move to **Agent 12.10 — Vehicle Effects**.

The Phase 12 ownership chain is now:

```text
12.1  Unity Client Architecture
  ↓
12.2  WebSocket Client
  ↓
12.3  Runtime State Synchronization
  ↓
12.4  Coordinate System
  ↓
12.5  F1 Car Entity Runtime
  ↓
12.6  Multi-Car Rendering
  ↓
12.7  Vehicle Transform / Orientation
  ↓
12.8  Track & Circuit Scene
  ↓
12.9  Telemetry Visualization
  ↓
12.10 Vehicle Effects   ← NEXT
```

And importantly, **12.9 did not take ownership of effects, physics, interpolation, replay timing, transport, or coordinate conversion**. Backend/shared remain unchanged and the **935 Phase 10/11 core regression remains green**.

When you're ready, the next implementation prompt should target **12.10 Vehicle Effects** while preserving all of these boundaries.

## User

Please give commands for Agent 12.10	Vehicle Effects	Wheels, lights, damage, smoke, effects, etc. ( 1 click copy and paste cursor friendly)

## Assistant

Paste this **single prompt into Cursor Agent** for **Agent 12.10 — Vehicle Effects**:

```text
You are implementing RaceVision Agent 12.10 — Vehicle Effects.

============================================================
AGENT 12.10 — VEHICLE EFFECTS
============================================================

MISSION
------------------------------------------------------------
Implement the Unity-side vehicle effects runtime for RaceVision.

Scope:
- Wheels / wheel visual state
- Brake lights
- Headlights / light states
- DRS visual indication
- Tyre/smoke effects
- Damage visualization hooks
- Collision/impact visual hooks
- Engine/exhaust visual hooks
- Effect lifecycle and pooling architecture
- LIVE / REPLAY compatible presentation

IMPORTANT:
This is a PRESENTATION / EFFECTS agent.

Do NOT create or modify:
- backend/runtime authorities
- EventBus
- ReplayClock
- telemetry transport
- WebSocket transport
- authentication
- authorization
- subscriptions
- outbound backpressure
- connection management
- coordinate conversion
- vehicle entity registry
- track scene ownership
- telemetry synchronization

Do NOT create a second vehicle entity system.

Do NOT create a second coordinate conversion system.

Do NOT create a second telemetry parser.

Do NOT introduce interpolation, extrapolation, prediction, smoothing, physics simulation, or timing authority.

============================================================
CURRENT AUTHORITIES — MUST BE REUSED
============================================================

12.1 Unity Client Architecture
12.2 RaceVision WebSocket Client
12.3 Runtime State Synchronization
12.4 Track / Coordinate System
12.5 F1 Car Entity Runtime
12.6 Multi-Car Rendering
12.7 Vehicle Transform / Orientation
12.8 Track & Circuit Scene
12.9 Telemetry Visualization

Existing authoritative flow:

Phase 11 backend
    ↓
12.2 WebSocket transport
    ↓
12.3 ClientStateSnapshot
    ↓
12.5 RuntimeCarRegistry
    ↓
12.6 CarVisualRegistry / MultiCarRenderer
    ↓
12.7 VehicleTransformApplier
    ↓
12.10 Vehicle Effects

Effects MUST consume existing runtime/presentation state.

Preferred source:

RuntimeCarState / CarVisualInstance / existing telemetry visualization state

Do NOT consume raw WebSocket messages.

Do NOT parse JSON.

Do NOT subscribe directly to backend EventBus.

============================================================
STEP 1 — AUDIT BEFORE CODING
============================================================

First inspect the repository.

Inspect:

unity/Assets/RaceVision/
docs/
tests/unity/
rendering/unity/

Specifically locate:

- RuntimeCarState
- RuntimeCarRegistry
- IVehicleEntityRuntime
- CarVisualRegistry
- ICarVisualInstance
- CarVisualInstance
- MultiCarRenderer
- VehicleTransformApplier
- TelemetryVisualizationRuntime
- CarTelemetryVisualizationState
- existing presentation/effect placeholders
- existing prefab/config conventions
- existing asmdefs
- existing tests
- Unity README/specification files

Read the existing Agent 12.5–12.9 implementation before changing anything.

Do not assume structures that do not exist.

Preserve established architecture.

============================================================
STEP 2 — EFFECT OWNERSHIP
============================================================

Create ONE authoritative vehicle-effects owner.

Recommended package:

unity/Assets/RaceVision/Presentation/Effects/

Possible structure:

Effects/
├── VehicleEffectsRuntime.cs
├── VehicleEffectState.cs
├── VehicleEffectRegistry.cs
├── IVehicleEffectsRuntime.cs
├── IVehicleEffectInstance.cs
├── VehicleEffectFactory.cs
├── VehicleEffectsConfig.cs
├── VehicleEffectInputs.cs
├── WheelEffectState.cs
├── LightEffectState.cs
├── SmokeEffectState.cs
├── DamageEffectState.cs
├── CollisionEffectState.cs
├── ExhaustEffectState.cs
└── README.md

Use the repository's existing naming conventions if they differ.

There must be ONE effects registry.

Key effects by:

DriverId

Do not key effects by connection ID.

Do not key effects by subscription ID.

Do not create a second car registry.

============================================================
STEP 3 — EFFECT STATE MODEL
============================================================

Create immutable or controlled presentation state.

Example conceptual model:

VehicleEffectState

Fields may include:

- DriverId
- session identity where already available
- OperatingMode
- wheels
- lights
- DRS
- smoke
- damage
- collision
- exhaust
- availability
- timestamp/source sequence metadata where already supplied

Do NOT invent telemetry.

Do NOT fabricate missing values.

Every effect input must distinguish:

AVAILABLE
UNAVAILABLE
INVALID

Missing telemetry must NOT become false/zero automatically unless that behavior is explicitly established as a visual default and documented.

============================================================
STEP 4 — WHEELS
============================================================

Implement wheel-effect state/binding architecture.

Support, where telemetry provides the information:

- front-left
- front-right
- rear-left
- rear-right

Possible visual state:

- rotation input
- steering input
- brake state
- tyre state
- slip indication if canonical telemetry exists
- wheel visibility/availability

IMPORTANT:

Do not calculate tyre physics.

Do not calculate slip ratio.

Do not calculate wheel velocity.

Do not invent wheel rotation from car speed.

If canonical wheel telemetry is unavailable, leave the corresponding effect unavailable.

Wheel transforms must remain presentation bindings.

Do not modify VehicleTransformApplier.

============================================================
STEP 5 — BRAKE LIGHTS
============================================================

Implement brake-light presentation.

Consume existing canonical brake telemetry if available.

Example:

brake > configured threshold
    → brake lights ON

Otherwise:

brake lights OFF

The threshold is a PRESENTATION CONFIGURATION value.

Do not modify canonical telemetry.

Do not create a second telemetry interpretation system.

If brake information is unavailable:

- preserve documented visual fallback
- preferably OFF / unavailable
- never pretend canonical braking occurred

============================================================
STEP 6 — HEADLIGHTS / LIGHTS
============================================================

Support visual light state when canonical data exists.

Potential states:

OFF
ON
HIGH
LOW
FLASHING
UNAVAILABLE

Do not invent race rules.

Do not infer headlights from time of day unless this is explicitly configured presentation behavior.

Keep light state separate from brake state.

============================================================
STEP 7 — DRS EFFECT
============================================================

If canonical DRS state exists:

- CLOSED
- OPEN
- UNAVAILABLE

Expose it to presentation effects.

Possible visual bindings:

- rear wing animation hook
- indicator
- configured emissive/light effect

Do NOT modify vehicle geometry.

Do NOT create DRS physics.

Do NOT calculate DRS activation.

Use the canonical telemetry value only.

============================================================
STEP 8 — SMOKE
============================================================

Implement smoke-effect hooks.

Possible sources if canonical telemetry exists:

- tyre smoke
- wheel lock smoke
- collision smoke
- engine/exhaust smoke

Separate effect types.

Do not calculate smoke from arbitrary speed/brake thresholds unless explicitly defined as presentation fallback.

Recommended state:

SmokeEffectState

- Available
- Active
- Intensity
- Duration/input metadata if supplied

Intensity must be bounded to configured safe presentation limits.

No unbounded particle spawning.

============================================================
STEP 9 — DAMAGE VISUALIZATION
============================================================

Implement damage presentation hooks.

Potential canonical inputs:

- damage state
- damaged components
- severity
- visual damage flags

Possible states:

NONE
MINOR
MODERATE
SEVERE
UNAVAILABLE

Do NOT create a damage physics model.

Do NOT invent collision damage.

Do NOT mutate RuntimeCarState.

Damage is visual presentation only.

If canonical damage data is unavailable, damage remains unavailable.

============================================================
STEP 10 — COLLISION / IMPACT EFFECTS
============================================================

Provide a controlled collision-effect hook.

Possible effect:

- impact flash
- sparks
- dust
- smoke burst

Only activate when canonical collision/event information is supplied.

Do NOT independently detect collisions using Unity physics.

Do NOT create gameplay physics.

Do NOT create a second event bus.

Effects may consume already synchronized runtime event information if an existing presentation-safe path exists.

============================================================
STEP 11 — EXHAUST / ENGINE EFFECTS
============================================================

Implement presentation hooks for:

- exhaust
- engine glow
- engine smoke
- configured heat shimmer placeholder

Use canonical RPM/throttle/load telemetry only when available.

Do not calculate engine physics.

Example presentation-only mapping:

RPM → configured visual intensity

Throttle → configured exhaust intensity

All values must be clamped.

No fabricated telemetry.

============================================================
STEP 12 — EFFECT INSTANCE ABSTRACTION
============================================================

Create:

IVehicleEffectInstance

or equivalent repository-consistent abstraction.

It should allow the effects runtime to bind to a vehicle visual.

Conceptually:

Bind(DriverId, ICarVisualInstance)

ApplyEffectState(VehicleEffectState)

Clear()

Dispose()

Do not make effects depend directly on:

- WebSocket
- JSON
- EventBus
- Runtime services
- ReplayClock

Effects operate on presentation/runtime state already available.

============================================================
STEP 13 — EFFECT FACTORY / PREFABS
============================================================

Create a configurable effect factory.

Example:

VehicleEffectFactory

It should support:

- configured effect prefab
- optional effect components
- safe placeholder fallback
- no prefab assigned

The runtime MUST remain functional if no effect prefab exists.

Use placeholder/no-op effects where appropriate.

Do not create finished F1 assets.

Do not create Blender assets.

Do not create final liveries.

Do not create final wheel meshes.

============================================================
STEP 14 — EFFECT POOLING
============================================================

Design bounded effect pooling for transient effects such as:

- sparks
- smoke bursts
- collision flashes

Avoid:

Instantiate/Destroy every telemetry update.

Use:

Acquire()
Release()

where appropriate.

Pool size must be bounded.

Overflow behavior must be deterministic.

Possible behavior:

- drop transient effect
- reuse oldest inactive effect

Never allow unbounded allocation.

Do not claim production FPS/SLA.

============================================================
STEP 15 — EFFECT LIFECYCLE
============================================================

Vehicle lifecycle mapping:

RuntimeCarState Available/Active
    → effects available

Stale
    → retain or reduce transient effects according to configuration

Unavailable
    → disable effects

Removed
    → clear and release effects

Reconnect/session invalidation
    → clear all vehicle effects

No cross-session visual leakage.

Do not create effects for cars that do not exist in RuntimeCarRegistry.

============================================================
STEP 16 — LIVE / REPLAY
============================================================

Use exactly the same effects path for:

LIVE
REPLAY

OperatingMode is metadata.

Do not create:

LiveEffectsRuntime
ReplayEffectsRuntime

Do not create a Unity ReplayClock.

Do not create replay timing logic.

Do not smooth or interpolate effects differently by mode.

============================================================
STEP 17 — MULTI-CAR ISOLATION
============================================================

Each DriverId must have independent effect state.

Example:

Car A smoke ON
Car B smoke OFF

must remain independent.

Car A damage must not affect Car B.

Car A DRS must not affect Car B.

Session A must never update Session B.

Test at least 20 cars through the effects registry where practical.

============================================================
STEP 18 — THREADING
============================================================

Effects are Unity presentation work.

All GameObject/ParticleSystem/Renderer/Light/Transform interaction MUST happen on Unity's main thread.

Do not perform UnityEngine operations from network threads.

Use the existing main-thread host/update architecture.

No blocking network operations.

No waits on EventBus.

No ReplayClock interaction.

============================================================
STEP 19 — PERFORMANCE
============================================================

Hot path requirements:

- dictionary lookup by DriverId
- cached references
- no Find()
- no GameObject.Find()
- no LINQ
- no JSON parsing
- no network access
- no reflection
- bounded effect updates
- bounded transient pools
- no per-frame unnecessary allocations

Avoid updating unchanged effect state.

Where practical:

if state unchanged:
    do not reapply expensive visual configuration.

Do not claim FPS numbers.

Document this as design-level performance only.

============================================================
STEP 20 — CONFIGURATION
============================================================

Create a presentation-only configuration object.

Possible configuration:

VehicleEffectsConfig

Fields:

- effects enabled
- wheel effects enabled
- brake lights enabled
- headlights enabled
- DRS visuals enabled
- smoke enabled
- damage visuals enabled
- collision effects enabled
- exhaust effects enabled
- transient pool size
- smoke intensity multiplier
- damage visual multiplier
- brake threshold
- max effect intensity
- stale behavior
- missing-data behavior

Do not introduce backend environment variables.

Do not introduce transport configuration.

Do not introduce telemetry configuration.

Keep configuration Unity-side.

============================================================
STEP 21 — SAFETY / VALIDATION
============================================================

Reject:

- NaN
- Infinity
- negative invalid intensities
- unbounded particle counts
- invalid DriverId
- foreign session state

Clamp configured presentation intensity.

Never mutate canonical telemetry.

Never mutate RuntimeCarState.

Never overwrite coordinate conversion.

Never alter source sequences.

============================================================
STEP 22 — DOCUMENTATION
============================================================

Create:

docs/specifications/VehicleEffectsSpecification.md

Update only relevant documentation:

- docs/Roadmap.md
- docs/Architecture.md
- docs/Streaming.md
- docs/Unity.md
- docs/specifications/README.md
- unity/README.md
- unity/Assets/README.md
- unity/Assets/RaceVision/README files where appropriate
- 12.9 handoff documentation

Document:

- ownership
- data flow
- supported effects
- missing-data semantics
- LIVE/REPLAY behavior
- lifecycle
- pooling
- threading
- performance design
- Blender boundary
- limitations
- future asset integration

Explicitly state:

12.10 does NOT create finished F1 car assets.

Blender remains the asset-production pipeline.

============================================================
STEP 23 — BLENDER BOUNDARY
============================================================

IMPORTANT FOR THE PROJECT:

Do NOT create Blender assets in Agent 12.10.

The architecture should support:

Blender F1 Car
    ↓
FBX/glTF/appropriate Unity import
    ↓
Unity Car Prefab
    ↓
12.6 CarVisualInstance
    ↓
12.7 Transform
    ↓
12.10 Vehicle Effects bindings

Effects should bind to configurable named effect points/components where available.

Examples:

Wheel_FL
Wheel_FR
Wheel_RL
Wheel_RR
BrakeLight
Headlight
Exhaust
SmokePoint
DamagePoint
ImpactPoint

Do not require these points to exist in placeholder prefabs.

============================================================
STEP 24 — TESTS
============================================================

Create EditMode tests for:

1. effect registry creation
2. DriverId isolation
3. multi-car effect isolation
4. brake-light threshold
5. DRS mapping
6. missing telemetry behavior
7. invalid NaN/Infinity handling
8. smoke intensity clamping
9. damage state mapping
10. collision effect lifecycle
11. effect pool boundedness
12. lifecycle transitions
13. stale behavior
14. unavailable behavior
15. removed behavior
16. reconnect clears effects
17. LIVE/REPLAY same path
18. session isolation
19. no fabricated telemetry
20. unchanged-state optimization where practical

Use fakes/mocks for effect instances.

Do not require finished 3D assets for tests.

If Unity Test Framework cannot execute because the Unity project packages are still missing:

DO NOT fabricate test execution.

Report:

UNITY_TESTS_NOT_EXECUTED

and explain exactly why.

============================================================
STEP 25 — REGRESSION TESTS
============================================================

Run the established backend regression suite.

At minimum:

tests/runtime
tests/transport
tests/api
tests/integration
tests/acceptance

Use the repository's existing canonical regression command if one exists.

Do not modify backend/shared merely to make unrelated tests pass.

If unrelated pre-existing failures exist:

- identify them
- report them
- do not claim they were caused by 12.10 without evidence

============================================================
STEP 26 — STATIC / ARCHITECTURAL CHECKS
============================================================

Verify:

- no backend changes
- no shared changes
- no WebSocket dependency
- no JSON parsing
- no EventBus dependency
- no ReplayClock
- no coordinate conversion ownership
- no RuntimeCarRegistry duplication
- no CarVisualRegistry duplication
- no vehicle transform ownership duplication
- no telemetry synchronization duplication
- no second effects registry
- no Unity physics authority
- no interpolation/extrapolation/prediction
- no Blender assets created

Run appropriate lint/static checks available in the repository.

Do not invent unavailable tooling.

============================================================
STEP 27 — ACCEPTANCE GATES
============================================================

Create explicit gates covering:

GATE-01
12.1 architecture preserved

GATE-02
12.2 transport unchanged

GATE-03
12.3 synchronization unchanged

GATE-04
12.4 coordinate authority unchanged

GATE-05
12.5 vehicle entity authority unchanged

GATE-06
12.6 visual registry authority unchanged

GATE-07
12.7 transform authority unchanged

GATE-08
12.8 track authority unchanged

GATE-09
12.9 telemetry visualization unchanged

GATE-10
single vehicle-effects owner

GATE-11
DriverId isolation

GATE-12
multi-car isolation

GATE-13
session isolation

GATE-14
LIVE/REPLAY same effects path

GATE-15
no fabricated telemetry

GATE-16
no physics simulation

GATE-17
no interpolation/extrapolation/prediction

GATE-18
missing-data safety

GATE-19
NaN/Infinity safety

GATE-20
bounded transient pooling

GATE-21
no unbounded allocations

GATE-22
main-thread Unity presentation

GATE-23
no transport/runtime coupling

GATE-24
lifecycle/reconnect cleanup

GATE-25
Blender boundary preserved

GATE-26
placeholder prefab compatibility

GATE-27
documentation complete

GATE-28
tests authored

GATE-29
Unity tests executed OR explicitly UNITY_TESTS_NOT_EXECUTED

GATE-30
Phase 10/11 regression green

GATE-31
no backend/shared changes

GATE-32
no duplicate subsystem ownership

============================================================
STEP 28 — FINAL REPORT
============================================================

When finished, report exactly:

1. STATUS
2. Architecture implemented
3. Existing authorities reused
4. Effects ownership
5. Wheel effects
6. Light effects
7. DRS effects
8. Smoke effects
9. Damage effects
10. Collision effects
11. Exhaust/engine effects
12. Lifecycle
13. LIVE/REPLAY
14. Multi-car/session isolation
15. Pooling/performance
16. Threading
17. Configuration
18. Blender boundary
19. Files created
20. Files modified
21. Unity tests — EXACT RESULT
22. Backend regression — EXACT RESULT
23. Static analysis — EXACT RESULT
24. Acceptance gates GATE-01…32
25. Limitations
26. Deferred work for Agent 12.11
27. Recommended next Agent

Do not claim tests passed unless actually executed.

Do not claim production performance/SLA.

Do not commit, push, or create a PR.

============================================================
CRITICAL ARCHITECTURAL RULE
============================================================

Agent 12.10 is presentation-only.

The authoritative architecture remains:

Phase 10 Runtime
    ↓
Phase 11 Transport
    ↓
12.2 WebSocket
    ↓
12.3 Synchronization
    ↓
12.4 Coordinate System
    ↓
12.5 Vehicle Entities
    ↓
12.6 Multi-Car Rendering
    ↓
12.7 Transform / Orientation
    ↓
12.8 Track Scene
    ↓
12.9 Telemetry Visualization
    ↓
12.10 Vehicle Effects

Do not move authority upward/downward.

Do not introduce duplicate systems.

Do not implement future agents early.

After implementation, stop and provide the exact acceptance report.
```

## User

## 1. STATUS

**ACCEPTED** (left uncommitted).

## 2. Architecture implemented

```text
RuntimeCarState.TelemetryChannels
  → VehicleEffectInputBuilder → VehicleEffectState
  → VehicleEffectsRuntime → IVehicleEffectInstance (NoOp placeholder)
  → TransientEffectPool (collision bursts)
```

## 3. Existing authorities reused

12.2–12.9 owners unchanged. Effects consume `IVehicleEntityRuntime` (+ optional `ICarVisualRegistry`).

## 4. Effects ownership

**Single owner:** `VehicleEffectsRuntime` / `VehicleEffectRegistry` keyed by `DriverId`.

## 5. Wheel effects

Corner availability only if `wheel_fl/fr/rl/rr` channels exist — **never** invented from speed.

## 6. Light effects

Brake lights from `brake` vs config threshold; headlights only if `headlights`/`lights` present. Missing brake → Off (configurable) or Unavailable.

## 7. DRS effects

Maps canonical `drs` → Open/Closed/Unavailable.

## 8. Smoke effects

`smoke` / `tyre_smoke` / `engine_smoke` only (no brake-smoke fallback). Intensities clamped.

## 9. Damage effects

`damage` / `damage_severity` → None/Minor/Moderate/Severe.

## 10. Collision effects

`collision` / `impact` → active intensity + pool acquire.

## 11. Exhaust/engine effects

Presentation intensity from available `rpm`/`throttle` (clamped); unavailable if both missing.

## 12–14. Lifecycle / LIVE·REPLAY / isolation

Stale/Unavailable/Removed/reconnect clear as configured; one path for LIVE/REPLAY; per-`DriverId` + 20-car tests.

## 15–17. Pooling / threading / config

Bounded `TransientEffectPool` with overflow reuse; unchanged-hash skip; main-thread `VehicleEffectsHost`; `VehicleEffectsConfig`.

## 18. Blender boundary

No assets. `NoOpVehicleEffectInstance` until prefab effect points exist.

## 19–20. Files

**Created:** `Presentation/Effects/*`, `VehicleEffectsTests.cs`, `VehicleEffectsSpecification.md`
**Modified:** Roadmap/Architecture/Streaming/Unity indexes/READMEs/12.9 handoff.

## 21–23. Verification

| Check              | Result                                                                              |
| ------------------ | ----------------------------------------------------------------------------------- |
| Unity EditMode     | **UNITY\_TESTS\_NOT\_EXECUTED** (`Packages/manifest.json` missing)                  |
| Phase 10/11 pytest | **935 passed**                                                                      |
| Static             | No WS/JSON/ReplayClock/coord ownership in Effects; `backend`/`shared` **unchanged** |

## 24. Acceptance gates GATE-01…32

| Gates             | Result                               |
| ----------------- | ------------------------------------ |
| 01–28, 30–32      | **PASS**                             |
| 29 Unity executed | **N/A** (`UNITY_TESTS_NOT_EXECUTED`) |
| 30 Phase 10/11    | **PASS** (935)                       |

## 25. Limitations

NoOp visuals only; no ParticleSystem/prefab binding yet; wheel telemetry usually unavailable; no finished F1 assets.

## 26–27. Deferred / next

**Agent 12.11 — Unity LIVE / REPLAY modes** (mode UX only; no ReplayClock).

## Assistant

Yes — based on the accepted 12.1–12.10 sequence, **Agent 12.11 is the correct next step**.

Paste this directly into Cursor Agent:

```text
You are implementing RaceVision Agent 12.11 — Unity LIVE / REPLAY Modes.

=========================================================
AGENT 12.11 — UNITY LIVE / REPLAY MODES
=========================================================

OBJECTIVE
---------------------------------------------------------
Implement the Unity-side LIVE / REPLAY operating-mode
presentation and mode lifecycle using the existing Phase 11
transport and Phase 12 client architecture.

This agent MUST NOT implement a ReplayClock, replay timing
authority, seeking, playback control, interpolation,
extrapolation, prediction, or a second runtime mode engine.

Unity consumes the authoritative mode supplied by the backend
and synchronized through Agent 12.3.

=========================================================
MANDATORY ARCHITECTURE
=========================================================

Preserve these existing authorities:

12.1  Unity Client Architecture
12.2  RaceVision WebSocket Client
12.3  Runtime State Synchronization
12.4  Track / Coordinate System
12.5  F1 Car Entity Runtime
12.6  Multi-Car Rendering
12.7  Vehicle Transform / Orientation
12.8  Track & Circuit Scene
12.9  Telemetry Visualization
12.10 Vehicle Effects

Do NOT create replacements for any of them.

Required flow:

Phase 11 transport
    ↓
12.2 RaceVisionWebSocketTransport
    ↓
12.3 RuntimeStateSynchronizer
    ↓
ClientStateSnapshot / IClientRuntimeState
    ↓
12.11 Unity Mode Runtime
    ↓
existing 12.5–12.10 consumers

The Unity mode layer is a PRESENTATION/CLIENT CONSUMER.
It is NOT a Runtime authority.

=========================================================
1. AUDIT FIRST
=========================================================

Before modifying files:

1. Inspect the repository and current Unity architecture.
2. Inspect:
   - unity/Assets/RaceVision/
   - 12.1 architecture
   - 12.2 transport
   - 12.3 synchronization
   - 12.4 coordinate system
   - 12.5 vehicles
   - 12.6 rendering
   - 12.7 transforms
   - 12.8 track
   - 12.9 telemetry
   - 12.10 effects
3. Find every existing LIVE/REPLAY mode definition.
4. Find ClientStateSnapshot / OperatingMode / mode_changed handling.
5. Find any existing mode UI/presentation hooks.
6. Find any ReplayClock, playback, seek, interpolation, or
   prediction implementation in Unity.
7. Do NOT create duplicate functionality.

If functionality already exists, extend/reuse it rather than
creating another owner.

=========================================================
2. AUTHORITATIVE MODE
=========================================================

The authoritative mode remains:

    OperatingMode.Live
    OperatingMode.Replay

Use the existing type.

Do NOT create another enum representing LIVE/REPLAY if one
already exists.

Backend/runtime mode remains authoritative.

Unity must never infer mode from:
- elapsed wall-clock time
- telemetry timestamps
- source sequence gaps
- vehicle movement
- connection state
- frame rate
- local playback state

Mode changes must originate from synchronized server state /
protocol envelopes.

=========================================================
3. MODE RUNTIME
=========================================================

Create a single Unity-side mode presentation/runtime owner,
only if an equivalent owner does not already exist.

Suggested location:

unity/Assets/RaceVision/Presentation/Modes/

Possible components:

- UnityModeRuntime
- UnityModeState
- UnityModePresenter
- UnityModeConfig
- IMModePresenter / equivalent appropriately named interface

Use the repository's existing naming conventions.

Responsibilities:

- expose current authoritative mode
- detect mode transitions
- publish mode state to presentation consumers
- expose availability/readiness
- maintain previous/current mode if useful for transition
  notifications
- provide deterministic lifecycle
- clear/reset correctly on reconnect/session invalidation

Do NOT own transport.
Do NOT own subscriptions.
Do NOT own Runtime EventBus.
Do NOT own ReplayClock.

=========================================================
4. MODE STATE
=========================================================

Represent at minimum:

- current mode
- previous mode where useful
- mode availability
- session identity
- connection/runtime availability
- transition sequence/version if already supplied
- transition timestamp only when supplied by authoritative
  protocol state

Do NOT fabricate timestamps or sequence values.

Recommended conceptual state:

Unknown
Live
Replay
Unavailable

Use existing project terminology if equivalent types already
exist.

=========================================================
5. MODE CHANGE HANDLING
=========================================================

Consume the mode information produced by Agent 12.3.

Support:

LIVE → REPLAY
REPLAY → LIVE
initial LIVE
initial REPLAY
mode unavailable
reconnect
session invalidation

Mode transitions must be deterministic.

On mode transition:

- update Unity mode state
- notify presentation listeners
- do not reset car identity unnecessarily
- do not recreate transport
- do not recreate subscriptions unless the existing
  subscription contract explicitly requires it
- do not alter coordinate conversion
- do not alter telemetry values
- do not alter canonical sequences
- do not alter Runtime timing

=========================================================
6. LIVE MODE
=========================================================

LIVE mode is presentation metadata.

When authoritative mode is LIVE:

- existing live telemetry can be presented
- existing car rendering continues
- telemetry visualization continues
- vehicle effects continue
- track scene remains owned by 12.8
- no local clock is introduced

Do not implement a local live clock.

=========================================================
7. REPLAY MODE
=========================================================

REPLAY mode is also presentation metadata.

When authoritative mode is REPLAY:

- existing replay telemetry can be presented
- existing car rendering continues
- telemetry visualization continues
- vehicle effects continue
- track scene remains owned by 12.8

Do NOT implement:

- ReplayClock
- playback clock
- seek
- pause
- resume
- playback speed
- frame stepping
- local replay timeline
- local interpolation
- extrapolation
- prediction

Those remain outside 12.11 and authoritative elsewhere.

=========================================================
8. MODE UI / PRESENTATION
=========================================================

Provide a clean presentation boundary so future UI can display:

- LIVE
- REPLAY
- unavailable/unknown

Do not create a finished visual UI skin.

A simple presenter/state interface is sufficient.

Avoid:

- hardcoded UI prefabs
- world-space labels
- duplicated telemetry widgets
- camera control
- OBS integration

Those belong to later phases.

=========================================================
9. SESSION ISOLATION
=========================================================

Mode state must be session-aware.

Rules:

- Session A mode cannot update Session B.
- Foreign-session envelopes must be rejected by existing
  synchronization/session rules.
- Reconnect creates a new connection identity.
- Mode state must not survive an invalidated session unless
  explicitly represented as unavailable.
- Reconnect must not silently resume a previous mode.

Use existing 12.3 session handling.

=========================================================
10. RECONNECT
=========================================================

On reconnect:

- mode becomes unavailable/unknown until authoritative state
  is received
- do not assume previous LIVE/REPLAY mode
- do not fabricate a mode
- do not create a local replay state
- restore mode only from synchronized server state

Preserve 12.2 reconnect ownership.

=========================================================
11. INTEGRATION WITH 12.5–12.10
=========================================================

Do not modify ownership of:

12.5 RuntimeCarRegistry
12.6 MultiCarRenderer
12.7 VehicleTransformApplier
12.8 TrackSceneRuntime
12.9 TelemetryVisualizationRuntime
12.10 VehicleEffectsRuntime

They may consume mode metadata if genuinely required.

Prefer read-only mode access.

LIVE and REPLAY must use the same:

- vehicle entity types
- rendering path
- coordinate conversion
- transform application
- telemetry visualization path
- vehicle effects path
- track scene path

No duplicated LIVE renderer.
No duplicated REPLAY renderer.

=========================================================
12. THREADING
=========================================================

Mode application must happen on the Unity main-thread
boundary established by 12.2/12.3.

Do not:

- create background Unity tasks
- access GameObjects from transport threads
- modify Transform from synchronization threads
- introduce a second message pump

Transport remains responsible for network threading.

=========================================================
13. PERFORMANCE
=========================================================

Mode changes are low-frequency.

Requirements:

- no polling network
- no JSON reparsing
- no LINQ in hot paths
- no per-frame allocation solely to detect mode
- no repeated scene recreation on unchanged mode
- unchanged mode should be a cheap no-op

Use change detection.

=========================================================
14. ERROR HANDLING
=========================================================

Handle:

- missing mode
- unsupported mode value
- malformed mode state
- foreign session
- reconnect/unavailable
- duplicate mode notification

Errors must be bounded and safe.

Never log:

- access tokens
- Authorization headers
- credentials
- secrets
- raw sensitive transport data

Do not crash the Unity client because a mode message is invalid.

=========================================================
15. CONFIGURATION
=========================================================

Do NOT introduce environment flags unless genuinely
required.

Do not create a setting that allows Unity to override the
authoritative mode.

Unity may configure presentation behavior only, e.g.:

- whether a mode indicator is enabled
- transition notification behavior

It must never configure:

    force LIVE
    force REPLAY
    local replay timing

=========================================================
16. TESTING
=========================================================

Create deterministic EditMode tests.

At minimum test:

1. Initial LIVE state.
2. Initial REPLAY state.
3. LIVE → REPLAY.
4. REPLAY → LIVE.
5. Same-mode update is idempotent.
6. Missing mode is unavailable.
7. Invalid mode is rejected safely.
8. Foreign session cannot update mode.
9. Reconnect clears mode to unavailable/unknown.
10. New authoritative mode restores state after reconnect.
11. LIVE and REPLAY use the same mode runtime.
12. No local ReplayClock exists.
13. No local interpolation/extrapolation/prediction.
14. Multiple mode transitions.
15. Mode listeners receive exactly one transition event.
16. Session invalidation clears mode.
17. Existing 12.5–12.10 paths remain unaffected.

Do not fabricate Unity test execution if the Unity Test
Framework is unavailable.

If Unity packages are still missing, report:

    UNITY_TESTS_NOT_EXECUTED

and provide exact reason.

=========================================================
17. ARCHITECTURE TESTS
=========================================================

Verify:

- no Transport dependency from mode presentation
- no WebSocket dependency from mode presentation
- no ReplayClock dependency
- no Runtime/EventBus dependency
- no coordinate conversion ownership
- no vehicle registry ownership
- no rendering duplication
- no telemetry parsing duplication
- no effects ownership

Mode presentation must remain a consumer.

=========================================================
18. DOCUMENTATION
=========================================================

Create:

docs/specifications/UnityLiveReplayModesSpecification.md

Update as appropriate:

- docs/Roadmap.md
- docs/Architecture.md
- docs/Streaming.md
- docs/Unity.md
- relevant Unity README/index files
- specifications index
- 12.10 handoff / 12.11 handoff documentation

Document explicitly:

"Unity LIVE/REPLAY mode is presentation/client state derived
from authoritative synchronized server state. Unity does not
own replay timing."

=========================================================
19. BLENDER BOUNDARY
=========================================================

Do NOT create Blender assets in Agent 12.11.

Do not create:

- F1 car meshes
- track meshes
- materials
- liveries
- wheels
- particle assets
- finished prefabs

Blender asset production/import remains separate from this
mode agent.

=========================================================
20. BACKEND / SHARED PROTECTION
=========================================================

Do NOT modify:

backend/runtime/
backend/api/
shared/

unless an absolutely necessary protocol compatibility defect
is discovered.

If a backend/shared change appears necessary, STOP and report
the exact reason instead of silently changing it.

Phase 10 and Phase 11 remain authoritative and unchanged.

=========================================================
21. GIT / CHANGE SAFETY
=========================================================

Do NOT commit.
Do NOT push.
Do NOT create a PR.

Keep changes limited to Agent 12.11.

Before editing:

- inspect git status
- inspect existing 12.1–12.10 changes
- identify pre-existing modifications
- do not overwrite unrelated user work

After editing:

- inspect git diff
- inspect git status
- verify only intended files changed

=========================================================
22. ACCEPTANCE GATES
=========================================================

Create and evaluate explicit gates for:

GATE-01 12.1 architecture preserved
GATE-02 12.2 transport unchanged
GATE-03 12.3 synchronization unchanged
GATE-04 authoritative OperatingMode reused
GATE-05 single Unity mode owner
GATE-06 no duplicate LIVE/REPLAY engine
GATE-07 server state remains authoritative
GATE-08 LIVE supported
GATE-09 REPLAY supported
GATE-10 LIVE→REPLAY
GATE-11 REPLAY→LIVE
GATE-12 reconnect handling
GATE-13 session isolation
GATE-14 invalid/missing mode safety
GATE-15 no ReplayClock
GATE-16 no seek/playback authority
GATE-17 no interpolation/extrapolation/prediction
GATE-18 same 12.5–12.10 rendering path
GATE-19 main-thread safety
GATE-20 no transport ownership duplication
GATE-21 no Runtime/EventBus ownership
GATE-22 no coordinate ownership
GATE-23 no Blender assets
GATE-24 no backend/shared changes
GATE-25 deterministic tests authored
GATE-26 Unity execution status honestly reported
GATE-27 documentation complete
GATE-28 Phase 10/11 regression remains green
GATE-29 no secrets introduced
GATE-30 no commit/push/PR

All applicable gates must PASS.

=========================================================
23. FINAL VERIFICATION
=========================================================

Run the most relevant available checks.

At minimum:

- inspect modified Unity files
- run available Unity tests if the project supports them
- run Phase 10/11 backend regression
- run repository/static checks available
- inspect git diff
- inspect git status

Do not claim tests were executed if they were not.

Do not claim production performance/SLA benchmarks.

=========================================================
24. FINAL REPORT
=========================================================

Return a structured report:

1. STATUS
2. Audit findings
3. Architecture implemented
4. Authoritative mode ownership
5. LIVE behavior
6. REPLAY behavior
7. Reconnect/session behavior
8. Integration with 12.5–12.10
9. Threading/performance
10. Error handling
11. Files created
12. Files modified
13. Tests executed — exact results
14. Tests not executed — exact reason
15. Static analysis
16. Acceptance gates GATE-01…30
17. Limitations / risks
18. Backend/shared status
19. Git status
20. Deferred work
21. Recommended next agent

=========================================================
IMPORTANT
=========================================================

Do not start Agent 12.12 or any later agent.

Do not create Blender assets.

Do not implement replay timing.

Do not implement interpolation/extrapolation/prediction.

Do not modify Phase 10 Runtime authority.

Do not create duplicate transport, synchronization,
subscription, backpressure, authentication, connection,
vehicle, coordinate, telemetry, effects, or rendering systems.

Implement Agent 12.11 only.
=========================================================
```

## User

# Agent 12.11 — Unity LIVE / REPLAY Modes — Final Report

## 1. STATUS

**ACCEPTED** — implementation complete, left **uncommitted** (no push/PR).

## 2. Audit findings

- Existing `OperatingMode` (`Unknown`/`Live`/`Replay`) in Core — reused.
- 12.3 already applies `mode_changed` into projection / `IClientRuntimeState.Mode`.
- No Unity ReplayClock, seek, interpolation, or mode presentation layer existed.
- Presentation now consumes mode via `IClientRuntimeState` only (no Transport/Synchronization asm coupling from Modes).

## 3. Architecture implemented

```text
Phase 11 → 12.2 → 12.3 → IClientRuntimeState → UnityModeRuntime → UnityModePresenter/Host
```

Types under `Presentation/Modes/`: `UnityModeState`, `UnityModeRuntime`, `UnityModeConfig`, `UnityModePresenter`, `UnityModeHost`.

## 4. Authoritative mode ownership

Server/12.3 remains authoritative. Unity exposes presentation snapshot only. Thin `ActiveSessionId` added on `IClientRuntimeState` for session-aware presentation without a Synchronization reference.

## 5. LIVE behavior

When sync mode is `Live` → `Available` + `IsLive`. No local live clock. 12.5–12.10 unchanged.

## 6. REPLAY behavior

When sync mode is `Replay` → `Available` + `IsReplay`. No ReplayClock / seek / playback / interpolation / extrapolation / prediction.

## 7. Reconnect/session behavior

Unavailable projection or `InvalidateSession` → `Unavailable`/`Unknown`. Foreign expected-session updates rejected. Mode restored only from new authoritative sync.

## 8. Integration with 12.5–12.10

Read-only / presentation-only. Same entities, render, transform, track, telemetry, and effects paths for LIVE and REPLAY.

## 9. Threading/performance

`UnityModeHost.Update` on main thread; unchanged mode is idempotent no-op; no transport polling or JSON reparsing.

## 10. Error handling

Missing mode → Unavailable. Invalid cast mode → reject, keep prior. Listener exceptions swallowed. No secrets logged.

## 11. Files created

- `unity/Assets/RaceVision/Presentation/Modes/UnityModeState.cs`
- `unity/Assets/RaceVision/Presentation/Modes/UnityModeConfig.cs`
- `unity/Assets/RaceVision/Presentation/Modes/UnityModeRuntime.cs`
- `unity/Assets/RaceVision/Presentation/Modes/UnityModePresenter.cs`
- `unity/Assets/RaceVision/Tests/EditMode/UnityLiveReplayModesTests.cs`
- `docs/specifications/UnityLiveReplayModesSpecification.md`

## 12. Files modified

- `IClientRuntimeState.cs` (`ActiveSessionId`)
- Roadmap / Architecture / Streaming / Unity docs
- Spec indexes + 12.10 handoff + Unity/Presentation READMEs + Unity client architecture ownership map

## 13. Tests executed

- Phase 10/11 regression: **935 passed**, 2 warnings (73.86s)

## 14. Tests not executed

**`UNITY_TESTS_NOT_EXECUTED`** — `unity/Packages/manifest.json` absent; Unity Test Framework unavailable. EditMode tests authored only.

## 15. Static analysis

- Modes: no Transport/WebSocket/EventBus/ReplayClock/coordinate/registry ownership (comment mentions only)
- No `*ReplayClock*` types under `Assets/RaceVision`
- No `backend/` or `shared/` diffs

## 16. Acceptance gates GATE-01…30

| Gate                                             | Result                            |
| ------------------------------------------------ | --------------------------------- |
| GATE-01 12.1 preserved                           | PASS                              |
| GATE-02 12.2 transport unchanged                 | PASS                              |
| GATE-03 12.3 sync unchanged (no sync file edits) | PASS                              |
| GATE-04 OperatingMode reused                     | PASS                              |
| GATE-05 single Unity mode owner                  | PASS                              |
| GATE-06 no duplicate LIVE/REPLAY engine          | PASS                              |
| GATE-07 server state authoritative               | PASS                              |
| GATE-08 LIVE supported                           | PASS                              |
| GATE-09 REPLAY supported                         | PASS                              |
| GATE-10 LIVE→REPLAY                              | PASS                              |
| GATE-11 REPLAY→LIVE                              | PASS                              |
| GATE-12 reconnect handling                       | PASS                              |
| GATE-13 session isolation                        | PASS                              |
| GATE-14 invalid/missing mode safety              | PASS                              |
| GATE-15 no ReplayClock                           | PASS                              |
| GATE-16 no seek/playback authority               | PASS                              |
| GATE-17 no interp/extrap/prediction              | PASS                              |
| GATE-18 same 12.5–12.10 path                     | PASS                              |
| GATE-19 main-thread safety                       | PASS                              |
| GATE-20 no transport ownership                   | PASS                              |
| GATE-21 no Runtime/EventBus ownership            | PASS                              |
| GATE-22 no coordinate ownership                  | PASS                              |
| GATE-23 no Blender assets                        | PASS                              |
| GATE-24 no backend/shared changes                | PASS                              |
| GATE-25 deterministic tests authored             | PASS                              |
| GATE-26 Unity execution status honest            | PASS (`UNITY_TESTS_NOT_EXECUTED`) |
| GATE-27 documentation complete                   | PASS                              |
| GATE-28 Phase 10/11 green                        | PASS (935)                        |
| GATE-29 no secrets                               | PASS                              |
| GATE-30 no commit/push/PR                        | PASS                              |

## 17. Limitations / risks

- Unity EditMode suite not runnable until packages/manifest exist.
- Mode indicator UI is a presenter boundary only (no visual skin).
- Optional expected-session defense is presentation-side; 12.3 remains primary foreign-session filter.

## 18. Backend/shared status

Unchanged.

## 19. Git status

Dirty working tree only for 12.11 files; **not committed** (per your preference).

## 20. Deferred work

Finished mode UI skin, OBS, camera mode chrome — later phases. Replay timing remains Phase 10 / non-Unity.

## 21. Recommended next agent

**Agent 12.12 — Unity Performance**



Done. The skipped question was **documentation depth**, and the recommended answer was:

**Full** **`UnityLiveReplayModesSpecification`** **+ update Roadmap / Architecture / Streaming / Unity / indexes**

That was already applied for Agent 12.11. I also cleaned a couple of older handoff lines in `MultiCarRenderingSpecification.md` so they mark 12.11 as **ACCEPTED**.

Nothing else needed for that skipped question.

## Assistant

Understood. I’ve got the Phase 12 progression and the accepted results through **Agent 12.11** in context.

Current position:

```text
12.1  Unity Client Architecture          ACCEPTED
12.2  RaceVision WebSocket Client        ACCEPTED
12.3  Runtime State Synchronization      ACCEPTED
12.4  Track / Coordinate System           ACCEPTED
12.5  F1 Car Entity Runtime               ACCEPTED
12.6  Multi-Car Rendering                 ACCEPTED
12.7  Vehicle Transform / Orientation    ACCEPTED
12.8  Track & Circuit Scene               ACCEPTED
12.9  Telemetry Visualization             ACCEPTED
12.10 Vehicle Effects                     ACCEPTED
12.11 Unity LIVE / REPLAY Modes           ACCEPTED
12.12 Unity Performance                   NEXT
12.13 Unity Integration Testing
12.14 Phase 12 Acceptance
```

And importantly, **Blender asset production has not started yet**. The architecture currently provides the documented boundary:

```text
Blender
   ↓
F1 Car / Track Assets
   ↓
Unity Import
   ↓
Prefab
   ↓
12.5 Runtime Entity
   ↓
12.6 Rendering
   ↓
12.7 Transform
   ↓
12.8 Track Scene
   ↓
12.9 Telemetry
   ↓
12.10 Effects
```

So the next agent is **12.12 — Unity Performance**, followed by **12.13 integration testing** and **12.14 final Phase 12 acceptance**.

I’m ready for your next question.

## User

Please give commands for Agent 12.12	Unity Performance	Rendering, update loops, batching, memory, frame-rate optimization ( 1 click copy and paste cursor friendly)

## Assistant

Below is the **Cursor-ready Agent 12.12 implementation command**. It is deliberately scoped to performance only and preserves all existing Phase 12 ownership boundaries.

```text
You are Agent 12.12 — Unity Performance Engineer for the RaceVision project.

============================================================
MISSION
============================================================

Implement:

Agent 12.12 — Unity Performance
Rendering, update loops, batching, memory, frame-rate optimization

The objective is to make the Unity client performance-ready for the Phase 12
runtime without changing the established architecture or creating duplicate
runtime/transport/telemetry authorities.

============================================================
MANDATORY CONTEXT
============================================================

Phase 12 agents already ACCEPTED:

12.1 Unity Client Architecture
12.2 RaceVision WebSocket Client
12.3 Runtime State Synchronization
12.4 Track / Coordinate System
12.5 F1 Car Entity Runtime
12.6 Multi-Car Rendering
12.7 Vehicle Transform / Orientation
12.8 Track & Circuit Scene
12.9 Telemetry Visualization
12.10 Vehicle Effects
12.11 Unity LIVE / REPLAY Modes

Phase 10/11 backend remains authoritative.

Current verified Phase 10/11 core regression:
935 passed.

Unity Editor tests have historically not executed because:
unity/Packages/manifest.json is not currently scaffolded.

Do NOT fabricate Unity execution results.

============================================================
ARCHITECTURAL AUTHORITIES — DO NOT VIOLATE
============================================================

12.2 = WebSocket transport
12.3 = Runtime state synchronization
12.4 = Coordinate conversion
12.5 = Runtime vehicle entities / RuntimeCarRegistry
12.6 = Car visual registry / multi-car rendering
12.7 = Vehicle transform application
12.8 = Track scene runtime
12.9 = Telemetry visualization
12.10 = Vehicle effects
12.11 = LIVE/REPLAY presentation mode

12.12 is PERFORMANCE ONLY.

Do not create:

- another transport
- another WebSocket client
- another synchronization system
- another EventBus
- another RuntimeCarRegistry
- another coordinate converter
- another transform authority
- another track authority
- another telemetry authority
- another ReplayClock
- interpolation
- extrapolation
- prediction
- physics simulation
- authentication
- authorization
- subscription management
- backend performance system

============================================================
PRIMARY PERFORMANCE OBJECTIVES
============================================================

Audit and optimize the Unity runtime for:

1. Rendering performance
2. Update-loop efficiency
3. Multi-car scaling
4. Transform update efficiency
5. Telemetry visualization update efficiency
6. Vehicle effects update efficiency
7. Memory allocation / GC pressure
8. Object lifetime / pooling
9. Batching readiness
10. Frame-rate stability
11. Scene lifecycle efficiency
12. LIVE/REPLAY parity
13. Reconnect/session cleanup
14. Performance observability
15. Future real F1 asset readiness

============================================================
1. PERFORMANCE ARCHITECTURE
============================================================

Create a dedicated performance architecture under the existing Unity
RaceVision structure.

Prefer a structure similar to:

unity/Assets/RaceVision/Performance/

Possible components:

- UnityPerformanceRuntime
- UnityPerformanceConfig
- UnityPerformanceSnapshot
- PerformanceBudget
- FrameUpdateScheduler
- PerformanceMetrics
- PerformanceScope / profiler helpers if justified
- bounded update scheduling utilities where required

Do not create unnecessary abstractions.

Performance code must observe existing systems rather than becoming a new
source of runtime truth.

============================================================
2. UPDATE LOOP OPTIMIZATION
============================================================

Audit all existing Phase 12 Update paths.

Specifically inspect:

- ClientRuntimeHost.Update
- WebSocket message pump
- Runtime state synchronization
- Vehicle rendering
- transform application
- telemetry visualization
- vehicle effects
- mode presentation
- track presentation

Prevent multiple systems independently performing expensive per-frame work.

Where appropriate establish a clear main-thread update ordering:

Transport pump
→ synchronization
→ runtime vehicle projection
→ presentation synchronization
→ transforms
→ telemetry presentation
→ effects
→ mode/scene presentation

Do not move network I/O onto the Unity main thread.

Do not introduce blocking operations.

Do not introduce async waits into the frame loop.

============================================================
3. BOUNDED UPDATE WORK
============================================================

Introduce configurable per-frame budgets where appropriate.

Examples:

- maximum messages pumped per frame
- maximum vehicle updates per frame
- maximum visual synchronization operations per frame
- maximum effect updates per frame
- maximum telemetry presentation updates per frame

Defaults must be conservative and configurable.

Do NOT silently drop authoritative runtime state.

If presentation work must be deferred, preserve the latest state and process
presentation work deterministically.

Never modify canonical telemetry to make performance appear better.

============================================================
4. MULTI-CAR PERFORMANCE
============================================================

Optimize the existing 12.5 → 12.6 → 12.7 pipeline.

Target:

- 1 car
- 5 cars
- 10 cars
- 20 cars
- 24 cars

Do not claim FPS results unless actually measured in Unity.

Optimize:

- DriverId dictionary lookups
- visual registry access
- transform application
- state comparison
- unchanged-state detection
- unnecessary GameObject operations
- unnecessary component lookups
- unnecessary allocations

Do not use:

- GameObject.Find
- FindObjectsOfType
- repeated GetComponent calls in hot loops
- LINQ in hot paths
- JSON parsing in rendering loops
- reflection in per-frame paths

Cache required references.

============================================================
5. RENDERING OPTIMIZATION
============================================================

Audit CarVisualInstance and MultiCarRenderer.

Prepare the system for real F1 car prefabs.

Support performance-safe configuration for:

- renderer enable/disable
- shadow casting
- receive shadows
- light probe usage
- reflection probe usage
- LOD readiness
- renderer grouping
- static/dynamic batching compatibility where applicable
- GPU instancing readiness where applicable

Do NOT force static batching on moving cars.

Do NOT introduce rendering features that require assets that do not yet exist.

Do not create fake F1 meshes.

Do not create Blender assets.

============================================================
6. LOD ARCHITECTURE
============================================================

Create an optional LOD configuration boundary suitable for future F1 assets.

Support conceptual levels such as:

LOD0 = full car
LOD1 = reduced detail
LOD2 = simplified car
LOD3 = minimal representation

Do not generate actual meshes.

Do not replace the existing prefab architecture.

LOD selection must remain presentation-only.

Distance calculations must be deterministic and configurable.

Avoid calculating expensive distance information unnecessarily every frame.

============================================================
7. TRANSFORM PERFORMANCE
============================================================

Reuse the 12.7 VehicleTransformApplier.

Do NOT create another transform owner.

Optimize:

- unchanged position detection
- unchanged orientation detection
- redundant SetPositionAndRotation calls
- invalid-value checking without unnecessary allocations

Only apply transforms when the effective pose changed.

Do not smooth, interpolate, extrapolate, or predict.

Do not alter coordinate conversion.

============================================================
8. TELEMETRY PRESENTATION PERFORMANCE
============================================================

Reuse 12.9 TelemetryVisualizationRuntime.

Optimize display updates by avoiding rebuilding presentation state when the
underlying value has not changed.

Do not parse JSON.

Do not mutate RuntimeCarState.

Do not create a second telemetry model.

Avoid per-frame string allocations where practical.

Cache formatted display values where appropriate.

Do not fabricate missing telemetry.

============================================================
9. VEHICLE EFFECT PERFORMANCE
============================================================

Reuse 12.10 VehicleEffectsRuntime and TransientEffectPool.

Optimize:

- effect state comparison
- particle/effect activation
- collision burst pooling
- repeated enable/disable operations
- unnecessary effect instance creation

No unbounded Instantiate/Destroy loop.

No unbounded effect pool.

Pool size must be configurable.

Pool exhaustion must have deterministic behavior.

Do not create real particle assets.

NoOp effect implementation remains valid until real assets exist.

============================================================
10. MEMORY / GC OPTIMIZATION
============================================================

Audit hot paths for:

- allocations
- boxing
- LINQ
- closures
- temporary collections
- repeated string construction
- repeated JSON parsing
- repeated object creation
- unnecessary delegate creation

Prefer:

- cached collections
- reusable buffers
- structs/value types where already architecturally appropriate
- bounded collections
- object pooling
- immutable snapshots already established by 12.3

Do not prematurely optimize cold paths.

Do not introduce unsafe code unless absolutely required.

============================================================
11. SESSION / RECONNECT CLEANUP
============================================================

Ensure performance resources are correctly released on:

- disconnect
- reconnect
- session change
- track change
- scene unload
- application shutdown

No stale visual/effect/telemetry objects may survive a session reset.

Reuse existing:

12.3 projection invalidation
12.5 vehicle registry invalidation
12.6 visual clearing
12.10 effect clearing
12.11 mode availability

Do not create a second lifecycle authority.

============================================================
12. SCENE PERFORMANCE
============================================================

Audit 12.8 TrackSceneRuntime.

Ensure:

- track binding does not repeatedly instantiate assets
- track prefab references are cached
- scene bind/unbind is idempotent
- unloaded tracks release presentation resources
- track switching does not leak GameObjects

Do not automatically parent cars to the track unless already explicitly
defined by the existing architecture.

============================================================
13. FRAME-RATE CONFIGURATION
============================================================

Create a performance configuration boundary supporting configurable targets
such as:

- target frame rate
- maximum presentation updates per frame
- telemetry update budget
- effects update budget
- vehicle update budget
- maximum pooled transient effects
- LOD update interval
- optional adaptive presentation scheduling

Do not force a particular production FPS claim.

Do not modify Unity project-wide settings unless they are already part of
the established configuration architecture.

============================================================
14. PERFORMANCE METRICS
============================================================

Create lightweight performance metrics for:

- frame/update duration
- vehicle updates
- visual updates
- transform applications
- telemetry updates
- effect updates
- deferred presentation work
- pool usage
- pool exhaustion
- GC/allocation observations where safely available

Metrics must be:

- bounded
- low overhead
- read-only
- presentation/performance focused
- safe when disabled

Do not duplicate Phase 11 backend transport observability.

Do not expose credentials, session identifiers, or sensitive data as labels.

============================================================
15. PROFILING SUPPORT
============================================================

Where Unity APIs are available, provide optional profiling markers around
major performance sections.

Examples:

- RaceVision.TransportPump
- RaceVision.RuntimeSync
- RaceVision.VehiclePresentation
- RaceVision.Transforms
- RaceVision.Telemetry
- RaceVision.Effects
- RaceVision.Track

Profiling must be optional and must not become a runtime dependency.

Do not claim profiler measurements unless Unity actually executed them.

============================================================
16. LIVE / REPLAY
============================================================

Use exactly the same performance architecture for:

OperatingMode.Live
OperatingMode.Replay

Do not create separate performance engines.

Do not add ReplayClock functionality.

Do not add playback timing.

Mode remains presentation metadata from 12.11.

============================================================
17. THREADING
============================================================

UnityEngine/GameObject/Transform operations remain on the Unity main thread.

Network operations remain off the main thread.

Do not introduce unsafe cross-thread access to:

- RuntimeCarRegistry
- ClientStateSnapshot
- CarVisualRegistry
- UnityEngine objects

Performance optimization must not compromise thread safety.

============================================================
18. UNITY PACKAGE / TEST LIMITATION
============================================================

The repository currently may not have:

unity/Packages/manifest.json

or the Unity Test Framework.

If Unity tests cannot execute:

DO NOT FABRICATE RESULTS.

Record exactly:

UNITY_TESTS_NOT_EXECUTED

and explain the environmental reason.

Tests must still be authored where practical.

============================================================
19. TESTS TO CREATE
============================================================

Create EditMode tests for:

- performance configuration defaults
- bounded update budgets
- unchanged-state skipping
- multi-car scheduling
- 1/5/10/20/24-car logical workloads
- transform update suppression
- telemetry update suppression
- effect pool bounds
- pool exhaustion behavior
- LOD selection logic
- session/reconnect cleanup
- scene cleanup
- LIVE/REPLAY same-path behavior
- no allocation-heavy LINQ paths where statically verifiable
- deterministic scheduling

If Unity execution is unavailable, mark execution honestly.

============================================================
20. STATIC ARCHITECTURE AUDIT
============================================================

Verify:

- only one transform owner
- only one vehicle registry
- only one coordinate converter
- only one telemetry synchronization path
- only one effect owner
- no ReplayClock
- no prediction
- no interpolation
- no transport duplication
- no backend modifications
- no shared protocol modifications
- no Blender assets
- no fake F1 assets

Search the repository for duplicate implementations before finalizing.

============================================================
21. DOCUMENTATION
============================================================

Create:

docs/specifications/UnityPerformanceSpecification.md

Update:

docs/Roadmap.md
docs/Architecture.md
docs/Streaming.md
docs/Unity.md
docs/specifications/README.md
docs/unity/README.md
docs/unity/Presentation/README.md if applicable
12.11 handoff documentation
12.13 handoff documentation

Document:

- performance ownership
- update order
- budgets
- pooling
- LOD boundary
- batching strategy
- memory rules
- frame-rate strategy
- profiling
- metrics
- test methodology
- known limitations
- what is NOT claimed as a production SLA

============================================================
22. DO NOT START FUTURE AGENTS
============================================================

Do NOT implement:

12.13 Unity Integration Testing
12.14 Phase 12 Acceptance
Phase 13 OBS
Phase 14 Camera/Director
Phase 15 Prediction/Latency Compensation
Blender asset production

Only prepare clean handoffs.

============================================================
23. REQUIRED ACCEPTANCE REPORT
============================================================

At completion provide:

1. STATUS
2. Architecture implemented
3. Existing authorities reused
4. Update-loop architecture
5. Rendering optimizations
6. Multi-car strategy
7. Transform optimization
8. Telemetry optimization
9. Effects optimization
10. Memory/GC strategy
11. LOD/batching strategy
12. Performance configuration
13. Metrics/profiling
14. LIVE/REPLAY behavior
15. Threading guarantees
16. Files created
17. Files modified
18. Tests authored
19. Tests actually executed
20. Static analysis
21. Acceptance gates
22. Backend/shared status
23. Git status
24. Limitations/risks
25. Deferred work
26. Recommended next Agent

============================================================
24. ACCEPTANCE GATES
============================================================

Create and verify appropriate gates covering:

GATE-01 12.1 architecture preserved
GATE-02 12.2 transport preserved
GATE-03 12.3 synchronization preserved
GATE-04 12.4 coordinate ownership preserved
GATE-05 12.5 vehicle runtime preserved
GATE-06 12.6 rendering ownership preserved
GATE-07 12.7 transform ownership preserved
GATE-08 12.8 track ownership preserved
GATE-09 12.9 telemetry ownership preserved
GATE-10 12.10 effects ownership preserved
GATE-11 12.11 mode ownership preserved
GATE-12 single performance authority
GATE-13 bounded update work
GATE-14 no blocking main-thread network work
GATE-15 multi-car scalability design
GATE-16 transform update suppression
GATE-17 telemetry update suppression
GATE-18 effect pooling bounded
GATE-19 memory/GC safeguards
GATE-20 LOD readiness
GATE-21 batching/rendering readiness
GATE-22 scene cleanup
GATE-23 reconnect/session cleanup
GATE-24 LIVE/REPLAY same path
GATE-25 no interpolation/extrapolation/prediction
GATE-26 no ReplayClock
GATE-27 no duplicate authorities
GATE-28 no backend/shared changes
GATE-29 no Blender/F1 assets
GATE-30 tests authored
GATE-31 Unity execution honestly reported
GATE-32 documentation complete
GATE-33 Phase 10/11 regression green
GATE-34 no secrets
GATE-35 no commit/push/PR unless explicitly requested

============================================================
25. FINAL RULE
============================================================

Do not merely create documentation.

Inspect the existing 12.1–12.11 implementation first.

Implement the smallest production-quality performance layer that improves
actual Unity execution without violating existing ownership boundaries.

Do not rewrite accepted agents.

Do not create duplicate systems.

Do not invent telemetry.

Do not invent performance measurements.

Do not claim FPS, memory, CPU, GPU, GC, or concurrency results unless they
were actually measured in Unity.

If Unity cannot execute, clearly report:

UNITY_TESTS_NOT_EXECUTED

The final implementation must leave a clean, explicit handoff to:

Agent 12.13 — Unity Integration Testing.
```

## User

# Agent 12.12 — Unity Performance — Final Report

## 1. STATUS

**ACCEPTED** — left **uncommitted** (no push/PR).

## 2. Architecture implemented

`RaceVision.Performance`: config, budgets, `FrameUpdateScheduler`, metrics/snapshot, LOD selector, rendering readiness options, profiler marker helpers, `UnityPerformanceHost` (order +50).
Presentation gate: `PresentationWorkBudget` for host deferral and per-frame budgets.

## 3. Existing authorities reused

12.2–12.11 owners unchanged in role. Performance observes/schedules only.

## 4. Update-loop architecture

`ClientRuntimeHost` (-100) → cars (10) → telemetry (20) → effects (30) → mode (40) → performance (50). Optional centralized Sync when `CentralizedPresentationScheduling` is true.

## 5. Rendering optimizations

`SetActive` no-op; sequence-based transform skip; rendering readiness flags; never force static batch on moving cars.

## 6. Multi-car strategy

Reusable buffers + rotating budget cursor; logical coverage for 1/5/10/20/24 cars in tests. **No FPS claims.**

## 7. Transform optimization

Still sole owner: `VehicleTransformApplier`. Pose equality suppression + sequence skip in `MultiCarRenderer`.

## 8. Telemetry optimization

Sequence skip before rebuild; reusable buffers; budgeted cursor.

## 9. Effects optimization

Sequence skip; collision rising-edge pool Acquire / falling-edge Release; bounded pool unchanged.

## 10. Memory/GC strategy

`CopyEntitiesTo` / `CopyTo`; avoid per-Sync List allocs; mode snapshot reuse on unchanged path.

## 11. LOD/batching strategy

`CarLodSelector` LOD0–3 + interval; readiness-only probes/shadows/instancing; no meshes/assets.

## 12. Performance configuration

`UnityPerformanceConfig` — frame target (opt-in), budgets, pool size, LOD, scheduling, markers/metrics.

## 13. Metrics/profiling

`UnityPerformanceSnapshot` / `PerformanceMetrics`; optional `Profiler.BeginSample` names. Host Stopwatch only — not a measured Unity profiler result.

## 14. LIVE/REPLAY behavior

Same performance path; no ReplayClock.

## 15. Threading guarantees

Main-thread hosts only; pump remains 12.2; no blocking network on Update.

## 16. Files created

- `unity/Assets/RaceVision/Performance/*` (config, metrics, LOD, scheduler, runtime, host, asmdef, README)
- `Presentation/PresentationWorkBudget.cs`
- `Tests/EditMode/UnityPerformanceTests.cs`
- `docs/specifications/UnityPerformanceSpecification.md`

## 17. Files modified

Hot paths in cars/telemetry/effects/modes/hosts; `RuntimeCarRegistry.CopyEntitiesTo`; docs indexes; EditMode asmdef.

## 18. Tests authored

`UnityPerformanceTests` — budgets, multi-car, skips, pool, LOD, cleanup, LIVE/REPLAY same path, architecture guards.

## 19. Tests actually executed

- Phase 10/11: **935 passed**, 2 warnings
- Unity: **`UNITY_TESTS_NOT_EXECUTED`** — `unity/Packages/manifest.json` absent

## 20. Static analysis

No ReplayClock types; no backend/`shared/` diffs; Performance has no Transport/WebSocket/EventBus ownership (profiler name string only).

## 21. Acceptance gates GATE-01…35

All **PASS** (GATE-31 honest Unity non-execution; GATE-35 no commit).

## 22. Backend/shared status

Unchanged.

## 23. Git status

Dirty 12.12 working tree only; **not committed**.

## 24. Limitations/risks

No measured FPS/GC in Unity; centralized scheduling needs hosts wired on `UnityPerformanceHost`; observation mode still applies config budgets when PerformanceHost is present.

## 25. Deferred work

12.13 integration/PlayMode; real F1 LOD meshes; real particle assets; measured profiler baselines.

## 26. Recommended next Agent

**Agent 12.13 — Unity Integration Testing**

## Assistant

Yes. Based on the accepted state of **12.1–12.12**, the next agent should be **12.13 — Unity Integration Testing**.

The key constraint is that 12.13 should **not invent another runtime system**. It should validate the complete Unity pipeline:

`Phase 11 Transport → 12.2 WS → 12.3 Sync → 12.4 Coordinates → 12.5 Cars → 12.6 Rendering → 12.7 Transform → 12.8 Track → 12.9 Telemetry → 12.10 Effects → 12.11 LIVE/REPLAY → 12.12 Performance`

Because the Unity project currently lacks `Packages/manifest.json`, the agent should also be explicit about what can and cannot actually be executed.

### Cursor-ready Agent 12.13 prompt

```text
You are the Principal Unity Integration Test Engineer for the RaceVision project.

============================================================
AGENT 12.13 — UNITY INTEGRATION TESTING
============================================================

OBJECTIVE
============================================================

Implement Agent 12.13 — Unity Integration Testing.

Validate the complete Phase 12 Unity client pipeline against the
existing Phase 11 transport and Phase 10 runtime contracts.

This is a VERIFICATION / TESTING agent.

Do NOT create duplicate runtime authorities.
Do NOT redesign existing agents.
Do NOT modify Phase 10 runtime authority.
Do NOT create a second WebSocket client.
Do NOT create a second synchronization system.
Do NOT create a second coordinate converter.
Do NOT create a second vehicle registry.
Do NOT create a second rendering registry.
Do NOT create a second transform owner.
Do NOT create a second track owner.
Do NOT create a second telemetry visualization owner.
Do NOT create a second effects owner.
Do NOT create a second LIVE/REPLAY engine.
Do NOT create a second performance scheduler.
Do NOT create Blender assets.
Do NOT create finished F1 car assets.
Do NOT create finished circuit assets.
Do NOT implement ReplayClock, seeking, interpolation, extrapolation,
prediction, physics, AI, OBS, cameras, or broadcasting.

============================================================
CURRENT ACCEPTED ARCHITECTURE
============================================================

Phase 10 remains the Runtime authority.

Phase 11 provides the canonical REST/WebSocket transport boundary.

Phase 12 Unity is a consumer/client.

Existing accepted ownership:

12.1 Unity Client Architecture
12.2 RaceVision WebSocket Client
12.3 Runtime State Synchronization
12.4 Track / Coordinate System
12.5 F1 Car Entity Runtime
12.6 Multi-Car Rendering
12.7 Vehicle Transform / Orientation
12.8 Track & Circuit Scene
12.9 Telemetry Visualization
12.10 Vehicle Effects
12.11 Unity LIVE / REPLAY Modes
12.12 Unity Performance

Preserve all existing ownership.

============================================================
MANDATORY PIPELINE TO TEST
============================================================

Validate this end-to-end flow:

Phase 11 canonical transport
        ↓
RaceVisionWebSocketTransport
        ↓
IRaceVisionTransport
        ↓
EnvelopeReceived
        ↓
RuntimeStateSynchronizer
        ↓
ClientProjectionStore
        ↓
ClientStateSnapshot
        ↓
RuntimeCarRegistry
        ↓
CoordinateSystem
        ↓
MultiCarRenderer
        ↓
VehicleTransformApplier
        ↓
TrackSceneRuntime
        ↓
TelemetryVisualizationRuntime
        ↓
VehicleEffectsRuntime
        ↓
UnityModeRuntime
        ↓
UnityPerformanceRuntime

The integration tests must prove that these components cooperate
without creating competing ownership.

============================================================
1. FIRST: INSPECT BEFORE MODIFYING
============================================================

Before writing code:

1. Inspect the current repository state.
2. Read the Phase 12 specifications.
3. Inspect Agents 12.1–12.12 implementation.
4. Inspect existing Unity assembly definitions.
5. Inspect existing EditMode tests.
6. Inspect Unity project structure.
7. Determine whether Unity packages / manifest / Test Framework
   are now available.
8. Inspect existing Phase 11 integration and acceptance tests.
9. Inspect existing protocol fixtures and canonical envelopes.
10. Identify whether a real Unity project can currently execute
    EditMode / PlayMode tests.

Do not assume files exist.
Do not recreate existing infrastructure.
Do not fabricate test execution.

============================================================
2. UNITY TEST INFRASTRUCTURE
============================================================

If Unity Packages/manifest.json and Unity Test Framework are already
available:

Use the existing Unity test infrastructure.

If they are NOT available:

DO NOT fabricate Unity test execution.

Instead:

- author the complete integration test suite;
- provide deterministic test fixtures;
- document exactly why Unity execution is unavailable;
- retain the existing convention:

UNITY_TESTS_NOT_EXECUTED

Do not claim Unity tests passed if they were not executed.

Do not create a fake Unity runner.

Do not replace Unity Test Framework with an unrelated test framework
just to claim execution.

============================================================
3. TEST LAYERS
============================================================

Create:

tests/integration/unity/

or, if the existing repository convention requires it:

unity/Assets/RaceVision/Tests/Integration/

Follow the existing repository structure rather than creating a
competing test root.

Tests should cover:

A. Architecture integration
B. Transport → synchronization
C. Synchronization → runtime entities
D. Coordinate → vehicle transforms
E. Multi-car rendering
F. Track binding
G. Telemetry visualization
H. Vehicle effects
I. LIVE / REPLAY
J. Reconnect/session isolation
K. Performance scheduling
L. Shutdown / cleanup
M. Full Phase 12 golden path

============================================================
4. PHASE 11 → UNITY TRANSPORT INTEGRATION
============================================================

Verify:

Phase 11 WebSocket envelope
        ↓
12.2 decoder
        ↓
12.2 main-thread pump
        ↓
12.3 synchronizer

Test:

- valid telemetry envelope;
- valid snapshot envelope;
- valid runtime event;
- mode_changed;
- subscription acknowledgement;
- malformed payload;
- unsupported payload;
- missing session;
- foreign session;
- duplicate source sequence;
- stale source sequence;
- reconnect;
- re-authentication;
- connection replacement.

Ensure:

Transport sequence and source sequence remain distinct.

Do not introduce a new transport abstraction.

============================================================
5. TELEMETRY → CAR ENTITY INTEGRATION
============================================================

Verify that canonical telemetry creates / updates:

RuntimeCarEntity
RuntimeCarState
RuntimeCarRegistry

Test:

- one car;
- multiple cars;
- 20-car scenario;
- independent driver updates;
- missing telemetry;
- stale car;
- unavailable car;
- removed car;
- session change;
- reconnect cleanup.

DriverId MUST remain the sole vehicle key.

No CarId replacement.

No duplicate registry.

============================================================
6. COORDINATE INTEGRATION
============================================================

Verify:

RuntimeCarState
        ↓
ICoordinateSystem
        ↓
UnityPosition / UnityOrientation
        ↓
VehicleTransformApplier

Test:

- identity metres;
- configured axis mapping;
- sign inversion;
- unit scale;
- origin offset;
- valid quaternion;
- missing orientation;
- invalid quaternion;
- NaN;
- Infinity.

Prove that presentation code does NOT implement its own axis,
handedness, or scale conversion.

12.4 remains the sole coordinate authority.

============================================================
7. MULTI-CAR RENDERING INTEGRATION
============================================================

Test:

- 1 car;
- 5 cars;
- 10 cars;
- 20 cars;
- 24 cars where supported by existing limits.

Verify:

RuntimeCarRegistry
        ↓
MultiCarRenderer
        ↓
CarVisualRegistry
        ↓
ICarVisualInstance

Verify DriverId isolation.

Verify duplicate visual registration protection.

Verify:

Active → Visible
Stale → retained according to config
Unavailable → Hidden
Removed → destroyed/cleared

Do not introduce another vehicle visual registry.

============================================================
8. TRANSFORM / ORIENTATION INTEGRATION
============================================================

Verify VehicleTransformApplier remains the ONLY transform authority.

Test:

- position update;
- valid orientation;
- unavailable orientation;
- invalid quaternion;
- degenerate quaternion;
- position invalid;
- multiple cars;
- unchanged sequence;
- reconnect cleanup.

Verify that:

12.6 does not directly implement transform math.

12.7 remains the transform owner.

============================================================
9. TRACK / CIRCUIT INTEGRATION
============================================================

Verify:

TrackDefinitionCatalog
        ↓
TrackSceneConfig
        ↓
TrackSceneRuntime
        ↓
TrackRoot

Test:

- valid track definition;
- matching coordinate definition;
- mismatched coordinate definition;
- lifecycle transitions;
- bind;
- unbind;
- duplicate bind protection;
- reconnect/session invalidation;
- empty/default TrackRoot;
- optional prefab binding.

Do not create actual F1 circuit geometry.

Do not create Blender assets.

Do not invent track coordinates.

============================================================
10. TELEMETRY VISUALIZATION INTEGRATION
============================================================

Verify canonical RuntimeCarState telemetry channels reach:

TelemetryVisualizationRuntime
        ↓
CarTelemetryVisualizationState

Test:

- speed_kph;
- speed_mps;
- speed;
- throttle;
- brake;
- gear;
- rpm;
- drs;
- lap_number;
- sector;
- race_position / position.

Verify:

- missing channel = unavailable;
- invalid channel = invalid;
- no fabricated zero values;
- display conversion does not mutate canonical telemetry.

Do not create another telemetry parser.

============================================================
11. VEHICLE EFFECTS INTEGRATION
============================================================

Verify:

RuntimeCarState
        ↓
VehicleEffectInputBuilder
        ↓
VehicleEffectState
        ↓
VehicleEffectsRuntime

Test:

- brake lights;
- headlights when supplied;
- DRS;
- smoke;
- damage;
- collision;
- exhaust / engine intensity;
- missing channels;
- clamping;
- rising collision edge;
- falling collision edge;
- pool reuse;
- multi-car isolation.

Verify effects never invent wheel telemetry.

Verify effects do not own telemetry parsing.

============================================================
12. LIVE / REPLAY INTEGRATION
============================================================

Verify both modes use the SAME Phase 12 pipeline.

LIVE:

Phase 11 LIVE
→ 12.3
→ 12.5–12.12

REPLAY:

Phase 11/Phase 10 REPLAY
→ 12.3
→ 12.5–12.12

Test:

LIVE → REPLAY
REPLAY → LIVE

Verify:

- same vehicle entities;
- same rendering;
- same transform;
- same track;
- same telemetry visualization;
- same effects;
- mode metadata changes only.

ABSOLUTELY NO:

ReplayClock
seek
playback authority
interpolation
extrapolation
prediction

Unity remains a consumer of authoritative runtime state.

============================================================
13. RECONNECT / SESSION ISOLATION
============================================================

Create a complete reconnect scenario:

Session A
→ connect
→ subscribe
→ receive telemetry
→ render cars
→ telemetry/effects update

Then:

disconnect
→ reconnect
→ new ConnectionId
→ Session A state invalidated
→ resubscription required
→ new authoritative state arrives

Verify:

- no stale Session A car visuals remain;
- no stale telemetry remains;
- no stale effects remain;
- no stale mode remains;
- no foreign Session B data reaches Session A;
- no durable resume is invented.

============================================================
14. PERFORMANCE INTEGRATION
============================================================

Verify Agent 12.12 scheduling does not alter correctness.

Test:

- 1 car;
- 5 cars;
- 10 cars;
- 20 cars;
- 24 cars if supported.

Verify:

- bounded work;
- sequence-based skips;
- reusable buffers;
- no unnecessary SetActive;
- transform skip behavior;
- telemetry skip behavior;
- effects skip behavior;
- LOD selection;
- cleanup.

Do NOT claim FPS, GC, CPU, GPU, or production capacity unless
actually measured in Unity.

Use:

BASELINE_NOT_PRODUCTION_SLA

for design-only evidence.

============================================================
15. FULL GOLDEN PATH TEST
============================================================

Create at least one complete golden-path scenario:

1. Start Unity client.
2. Establish Phase 11 WebSocket connection.
3. Authenticate through existing transport boundary.
4. Receive canonical LIVE telemetry.
5. Synchronize state.
6. Create multiple RuntimeCarEntity instances.
7. Convert coordinates.
8. Create/update car visuals.
9. Apply transforms.
10. Bind track environment.
11. Update telemetry visualization.
12. Update effects.
13. Confirm LIVE mode.
14. Process multiple telemetry frames.
15. Switch to REPLAY.
16. Confirm same entity/rendering path.
17. Process replay state.
18. Switch back to LIVE.
19. Disconnect.
20. Reconnect.
21. Confirm state invalidation.
22. Resubscribe.
23. Receive fresh telemetry.
24. Confirm clean reconstruction.
25. Shutdown cleanly.

This is the primary Phase 12 integration journey.

============================================================
16. ERROR / FAILURE INTEGRATION
============================================================

Test that one subsystem failure does not create cross-layer corruption.

Examples:

- malformed envelope;
- coordinate conversion failure;
- invalid orientation;
- missing telemetry;
- visual creation failure;
- effect pool exhaustion;
- track binding failure;
- reconnect;
- session mismatch.

Verify failures remain bounded to their owning subsystem.

Do not swallow errors that should be surfaced.

Do not leak credentials/secrets.

============================================================
17. ARCHITECTURE GUARDS
============================================================

Add tests/static checks proving:

- Presentation does not own transport.
- Presentation does not decode WebSocket JSON.
- Domain does not reference Presentation.
- Coordinate conversion exists only in 12.4.
- Runtime vehicle registry exists only in 12.5.
- Visual registry exists only in 12.6.
- Transform ownership exists only in 12.7.
- Track ownership exists only in 12.8.
- Telemetry visualization ownership exists only in 12.9.
- Effects ownership exists only in 12.10.
- Mode presentation exists only in 12.11.
- Performance scheduling exists only in 12.12.
- No ReplayClock under Unity Assets.
- No Blender assets introduced.
- No backend/shared authority duplication.

============================================================
18. TEST FIXTURES
============================================================

Use deterministic fixtures.

Create reusable canonical test data for:

- SessionId;
- DriverId;
- ConnectionId;
- LIVE telemetry;
- REPLAY telemetry;
- snapshot;
- runtime event;
- mode_changed;
- 1-car;
- 5-car;
- 10-car;
- 20-car.

Do not hard-code unrealistic assumptions about real F1 telemetry
that are not present in the canonical protocol.

============================================================
19. TESTING REALISM
============================================================

Where a real Phase 11 server can be used safely, prefer the existing
Phase 11 integration test infrastructure.

Do not create a second mock server architecture.

If only deterministic fixture testing is possible, clearly distinguish:

CONTRACT_INTEGRATION_TEST

from:

LIVE_SERVER_E2E

Do not claim a real server E2E test unless one actually ran.

============================================================
20. UNITY EXECUTION
============================================================

If Unity Test Framework is available:

Run:

- EditMode integration tests;
- PlayMode integration tests;
- architecture tests;
- full Phase 12 integration suite.

Record exact commands and exact results.

If Unity Test Framework is NOT available:

Record:

UNITY_TESTS_NOT_EXECUTED

and explain:

- missing Packages/manifest.json;
- missing Test Framework;
- missing Unity project execution environment.

Do not fabricate execution.

============================================================
21. BACKEND REGRESSION
============================================================

Run the established Phase 10/11 regression suite.

At minimum preserve the currently established green core suite.

Do not modify backend/shared simply to make Unity tests pass.

If unrelated existing failures occur, identify them separately.

Do not reclassify unrelated failures as Agent 12.13 failures.

============================================================
22. DOCUMENTATION
============================================================

Create:

docs/specifications/UnityIntegrationTestingSpecification.md

Update only relevant:

docs/Roadmap.md
docs/Architecture.md
docs/Streaming.md
docs/Unity.md
docs/specifications/README.md
unity/README.md
unity/Assets/README.md
unity/Documentation/README.md
tests/unity/README.md
12.12 handoff documentation

Document:

- scope;
- architecture;
- test layers;
- golden path;
- fixtures;
- execution status;
- limitations;
- known environment blockers;
- exact results.

============================================================
23. ACCEPTANCE GATES
============================================================

Create explicit gates covering at least:

GATE-01 12.1 architecture preserved
GATE-02 12.2 transport preserved
GATE-03 12.3 synchronization preserved
GATE-04 12.4 coordinate authority preserved
GATE-05 12.5 vehicle authority preserved
GATE-06 12.6 rendering authority preserved
GATE-07 12.7 transform authority preserved
GATE-08 12.8 track authority preserved
GATE-09 12.9 telemetry visualization preserved
GATE-10 12.10 effects authority preserved
GATE-11 12.11 mode authority preserved
GATE-12 12.12 performance authority preserved
GATE-13 Phase 11 → Unity transport integration
GATE-14 telemetry synchronization
GATE-15 multi-car isolation
GATE-16 coordinate conversion
GATE-17 transform application
GATE-18 track lifecycle
GATE-19 telemetry visualization
GATE-20 vehicle effects
GATE-21 LIVE mode
GATE-22 REPLAY mode
GATE-23 LIVE/REPLAY transition
GATE-24 reconnect
GATE-25 session isolation
GATE-26 shutdown
GATE-27 performance scheduling
GATE-28 error isolation
GATE-29 architecture dependency guards
GATE-30 deterministic fixtures
GATE-31 full golden path
GATE-32 Unity execution status honesty
GATE-33 backend/shared unchanged
GATE-34 documentation
GATE-35 no duplicate authorities

Every gate must be marked:

PASS
FAIL
N/A

Never mark an unexecuted runtime test PASS merely because the test
file exists.

============================================================
24. NO PERFORMANCE CLAIMS WITHOUT MEASUREMENT
============================================================

Do not claim:

60 FPS
120 FPS
144 FPS
low GC
production capacity
specific CPU usage
specific GPU usage
specific memory usage

unless actually measured inside Unity.

Architecture-level optimization evidence must be labelled:

BASELINE_NOT_PRODUCTION_SLA

============================================================
25. BLENDER BOUNDARY
============================================================

Blender is NOT part of Agent 12.13 implementation.

Do not create:

.blend
.fbx
.obj
.glb
real F1 meshes
real F1 liveries
real circuit meshes

Only validate that existing prefab/configuration boundaries are
compatible with future Blender-produced assets.

Actual Blender asset production remains downstream of the Unity
architecture and should use the already-defined:

Blender → export → Unity import → prefab → RaceVision coordinate
contract → runtime entity → visual/effects binding

============================================================
26. GIT SAFETY
============================================================

Do NOT commit.

Do NOT push.

Do NOT create a PR.

Leave changes uncommitted.

Do not modify unrelated files.

============================================================
27. FINAL REPORT FORMAT
============================================================

Return:

1. STATUS
2. Audit findings
3. Existing architecture reused
4. Integration architecture
5. Test suites created
6. Golden path
7. Transport integration
8. Synchronization integration
9. Multi-car integration
10. Coordinate integration
11. Transform integration
12. Track integration
13. Telemetry visualization integration
14. Effects integration
15. LIVE/REPLAY integration
16. Reconnect/session integration
17. Performance integration
18. Error handling
19. Architecture guards
20. Files created
21. Files modified
22. Unity tests actually executed
23. Backend tests actually executed
24. Static analysis
25. Exact test counts/results
26. Acceptance gates
27. Limitations
28. Known pre-existing failures
29. Backend/shared status
30. Git status
31. Deferred work
32. Recommended next Agent

For every test result, distinguish clearly between:

EXECUTED AND PASSED
EXECUTED AND FAILED
AUTHORED BUT NOT EXECUTED
NOT APPLICABLE

============================================================
SUCCESS CRITERIA
============================================================

Agent 12.13 is ACCEPTED only when:

- the full Phase 12 integration path is represented;
- existing authorities remain unchanged;
- transport → synchronization → entities → coordinates →
  rendering → transforms → track → telemetry → effects → modes →
  performance is covered;
- LIVE and REPLAY use the same Unity pipeline;
- reconnect/session isolation is tested;
- architecture guards exist;
- no duplicate subsystems are introduced;
- Unity execution status is reported honestly;
- Phase 10/11 regression remains green for the applicable core suite;
- documentation is complete;
- no Blender/F1 asset implementation is introduced;
- no commit/push/PR is performed.

Begin by inspecting the repository and current Agent 12.1–12.12
implementation. Do not ask for clarification unless a genuinely
blocking ambiguity is discovered.
```

## User

# Agent 12.13 — Unity Integration Testing — Final Report

## 1. STATUS

**ACCEPTED** — left **uncommitted** (no push/PR).

## 2. Audit findings

- Agents 12.1–12.12 already committed (`8866f2b` HEAD).
- Unity tests live under `Tests/EditMode/`; **no** `unity/Packages/manifest.json`.
- Phase 11 E2E already exists in `tests/integration/transport/` — not duplicated.
- No existing Phase 12 Integration folder before this agent.

## 3. Existing architecture reused

Pipeline harness wires **only** accepted owners: Synchronizer → Vehicles → MultiCarRenderer / TransformApplier → Track → Telemetry → Effects → Mode → Performance.

## 4. Integration architecture

`CONTRACT_INTEGRATION_TEST` via `Phase12PipelineHarness` + fixtures. Distinct from Phase 11 `LIVE_SERVER_E2E`.

## 5. Test suites created

| Artifact                               | Role                                |
| -------------------------------------- | ----------------------------------- |
| `UnityIntegrationFixtures.cs`          | Deterministic envelopes / multi-car |
| `Phase12PipelineHarness.cs`            | Owner wiring                        |
| `Phase12GoldenPathIntegrationTests.cs` | Full journey                        |
| `Phase12LayerIntegrationTests.cs`      | Layers + architecture guards        |
| Integration / tests/unity READMEs      | Indexes                             |

**22** `[Test]` methods authored.

## 6. Golden path

LIVE connect → multi-car sync → track → telemetry/effects → LIVE→REPLAY→LIVE → reconnect wipe → rebuild → shutdown.

## 7–17. Layer coverage (authored)

Transport/sync, multi-car 1–24, coordinates via 12.4, transform skip owner, track bind/mismatch, telemetry channels, effects + collision edges, LIVE/REPLAY same types, reconnect/session isolation, budgeted presentation (`BASELINE_NOT_PRODUCTION_SLA`), error isolation, architecture guards.

## 18. Error handling

Malformed / foreign session / duplicate / stale / coordinate mismatch isolated; cars not corrupted by bad envelopes.

## 19. Architecture guards

Single-owner assemblies; no ReplayClock; Presentation≠Transport; no Blender assets under RaceVision.

## 20. Files created

- `unity/Assets/RaceVision/Tests/EditMode/Integration/*`
- `docs/specifications/UnityIntegrationTestingSpecification.md`
- `tests/unity/README.md` (updated/created)

## 21. Files modified

Roadmap / Architecture / Streaming / Unity / spec indexes / READMEs / 12.12 handoff / Documentation README.

## 22. Unity tests actually executed

**`UNITY_TESTS_NOT_EXECUTED`**
Reason: `unity/Packages/manifest.json` absent; Unity Test Framework / Editor runner unavailable.
Status for all Unity suites: **AUTHORED BUT NOT EXECUTED**.

## 23. Backend tests actually executed

Phase 10/11 core: **935 passed**, 2 warnings — **EXECUTED AND PASSED**.

## 24. Static analysis

No `backend/` / `shared/` diffs; no Blender/F1 mesh assets added.

## 25. Exact test counts/results

| Suite                      | Count | Result                    |
| -------------------------- | ----: | ------------------------- |
| Unity EditMode Integration |    22 | AUTHORED BUT NOT EXECUTED |
| Phase 10/11 pytest         |   935 | EXECUTED AND PASSED       |

## 26. Acceptance gates GATE-01…35

| Gate                             | Result   | Note                                               |
| -------------------------------- | -------- | -------------------------------------------------- |
| GATE-01…12 authorities preserved | **PASS** | No production owner rewrites                       |
| GATE-13…31 coverage authored     | **PASS** | Contract tests represented; **not** Unity-executed |
| GATE-32 Unity execution honesty  | **PASS** | `UNITY_TESTS_NOT_EXECUTED`                         |
| GATE-33 backend/shared unchanged | **PASS** |                                                    |
| GATE-34 documentation            | **PASS** |                                                    |
| GATE-35 no duplicate authorities | **PASS** |                                                    |

## 27. Limitations

Unity cannot run until packages/manifest + Editor are scaffolded. No FPS/GC claims (`BASELINE_NOT_PRODUCTION_SLA`).

## 28. Known pre-existing failures

None in the green Phase 10/11 core suite.

## 29. Backend/shared status

Unchanged.

## 30. Git status

Dirty 12.13 working tree only; **not committed**.

## 31. Deferred work

Execute EditMode/PlayMode in Unity once packages exist; optional live WS E2E against Phase 11 (already covered separately).

## 32. Recommended next Agent

**Agent 12.14 — Phase 12 Acceptance**

## Assistant

Understood. I’ve incorporated the **Agent 12.13 final report** into the Phase 12 project context.

### Current Phase 12 status

| Agent | Component | Status |
|---|---|---|
| 12.1 | Unity Client Architecture | ✅ ACCEPTED |
| 12.2 | RaceVision WebSocket Client | ✅ ACCEPTED |
| 12.3 | Runtime State Synchronization | ✅ ACCEPTED |
| 12.4 | Track / Coordinate System | ✅ ACCEPTED |
| 12.5 | F1 Car Entity Runtime | ✅ ACCEPTED |
| 12.6 | Multi-Car Rendering | ✅ ACCEPTED |
| 12.7 | Vehicle Transform / Orientation | ✅ ACCEPTED |
| 12.8 | Track & Circuit Scene | ✅ ACCEPTED |
| 12.9 | Telemetry Visualization | ✅ ACCEPTED |
| 12.10 | Vehicle Effects | ✅ ACCEPTED |
| 12.11 | Unity LIVE / REPLAY Modes | ✅ ACCEPTED |
| 12.12 | Unity Performance | ✅ ACCEPTED |
| 12.13 | Unity Integration Testing | ✅ ACCEPTED |
| **12.14** | **Phase 12 Acceptance** | ⏭️ **NEXT** |

### Important current constraints

- **Backend / shared:** unchanged.
- **Phase 10/11 regression:** **935 passed**.
- **Unity integration tests:** 22 authored, but **not executed** because `unity/Packages/manifest.json` and Unity Test Framework are still absent.
- No production FPS/GC claims have been made.
- No Blender/F1 production assets have been created yet.
- The architecture now has the complete Unity-side pipeline from **Phase 11 WebSocket → synchronized state → coordinates → cars → rendering → telemetry → effects → LIVE/REPLAY → performance → integration testing**.

### Next

The correct next agent is:

**Agent 12.14 — Phase 12 Acceptance — Final acceptance gate**

After 12.14 is accepted, **Phase 12 is complete** and we can move to the next planned phase/workstream.

And importantly regarding your earlier Blender question: **the architecture has deliberately established the Blender → Unity asset boundary, but Agents 12.1–12.13 have not created the actual F1 cars or circuit assets.** That production asset work can now be introduced without contaminating the transport/runtime authorities.

## User

Please give commands for Agent 12.14	Phase 12 Acceptance	Final Unity/3D acceptance gate ( 1 click copy and paste cursor friendly)

## Assistant

Absolutely. **Agent 12.14 is the final Phase 12 acceptance gate**, so the agent should be **verification/acceptance only** and must not introduce another Unity subsystem or silently compensate for the missing Unity package scaffold.

Copy/paste the following directly into Cursor:

```text
AGENT 12.14 — PHASE 12 ACCEPTANCE
Final Unity / 3D Acceptance Gate

You are the Principal Unity Integration Architect and Acceptance Engineer for the RaceVision F1 project.

============================================================
MISSION
============================================================

Perform the FINAL ACCEPTANCE of Phase 12:

Phase 12 — Unity Integration & 3D Scene Runtime

This is an ACCEPTANCE / VERIFICATION agent.

DO NOT create a new runtime subsystem.
DO NOT replace existing authorities.
DO NOT redesign Agents 12.1–12.13.
DO NOT modify Phase 10 or Phase 11 architecture.
DO NOT create Blender/F1 production assets.
DO NOT claim Unity tests executed unless Unity actually executes them.
DO NOT fabricate FPS, GC, memory, rendering, or concurrency measurements.

Your responsibility is to audit the complete Phase 12 implementation, execute every test that can genuinely be executed in the current environment, author any missing acceptance-only tests if necessary, verify architectural boundaries, reconcile documentation, and produce a final Phase 12 acceptance report.

============================================================
PROJECT
============================================================

Repository:
RaceVision

Phase 10:
Unified Runtime / Live / Replay authority

Phase 11:
Transport / REST / WebSocket / security / observability / integration / live-stream acceptance

Phase 12:
Unity Integration & 3D Scene Runtime

============================================================
PHASE 12 AGENTS
============================================================

12.1 Unity Client Architecture
12.2 RaceVision WebSocket Client
12.3 Runtime State Synchronization
12.4 Track / Coordinate System
12.5 F1 Car Entity Runtime
12.6 Multi-Car Rendering
12.7 Vehicle Transform / Orientation
12.8 Track & Circuit Scene
12.9 Telemetry Visualization
12.10 Vehicle Effects
12.11 Unity LIVE / REPLAY Modes
12.12 Unity Performance
12.13 Unity Integration Testing
12.14 Phase 12 Acceptance ← YOU ARE HERE

============================================================
KNOWN ACCEPTED STATE
============================================================

Agents 12.1–12.13 are already reported ACCEPTED.

12.1:
Unity client architecture and assembly boundaries.

12.2:
Concrete WebSocket transport behind IRaceVisionTransport.

12.3:
Runtime state synchronization and immutable client projection.

12.4:
Authoritative coordinate conversion.

12.5:
Runtime vehicle entities and RuntimeCarRegistry.

12.6:
Multi-car presentation and CarVisualRegistry.

12.7:
Vehicle transform/orientation ownership.

12.8:
Track/circuit scene runtime.

12.9:
Telemetry visualization.

12.10:
Vehicle effects.

12.11:
Unity LIVE/REPLAY presentation mode.

12.12:
Unity performance scheduling/budgets/LOD/profiling boundaries.

12.13:
Unity integration testing / Phase12PipelineHarness / golden-path tests.

============================================================
CRITICAL EXISTING AUTHORITIES
============================================================

Preserve these ownership boundaries.

12.2:
Transport/WebSocket authority.

12.3:
Client synchronization/projection authority.

12.4:
Coordinate conversion authority.

12.5:
Runtime vehicle entity authority.

12.6:
Vehicle visual registry/presentation authority.

12.7:
Vehicle transform/orientation authority.

12.8:
Track scene authority.

12.9:
Telemetry visualization authority.

12.10:
Vehicle effects authority.

12.11:
Unity LIVE/REPLAY presentation authority.

12.12:
Unity performance scheduling/optimization authority.

12.13:
Unity integration test harness authority.

Phase 10 remains the runtime authority.

Phase 11 remains the server transport authority.

Unity MUST remain a consumer/presentation client.

============================================================
EXPECTED END-TO-END ARCHITECTURE
============================================================

Verify that the intended architecture remains:

Phase 10 Runtime
    ↓
Phase 11 REST / WebSocket Transport
    ↓
12.2 RaceVisionWebSocketTransport
    ↓
12.3 RuntimeStateSynchronizer
    ↓
ClientStateSnapshot
    ↓
12.5 RuntimeCarRegistry
    ↓
12.4 Coordinate System
    ↓
12.6 Multi-Car Rendering
    ↓
12.7 Vehicle Transform
    ↓
12.8 Track / Circuit Scene
    ↓
12.9 Telemetry Visualization
    ↓
12.10 Vehicle Effects
    ↓
12.11 LIVE / REPLAY presentation
    ↓
12.12 Performance scheduling
    ↓
12.13 Integration / acceptance verification

Do not introduce another path that bypasses these authorities.

============================================================
STEP 1 — REPOSITORY AUDIT
============================================================

Inspect the actual repository.

Verify:

- unity/ structure
- unity/Assets/RaceVision/
- Core
- Domain
- Protocol
- Transport
- Synchronization
- Runtime
- CoordinateSystem
- Presentation
- Performance
- Tests
- Integration tests
- documentation
- Roadmap
- Architecture
- Streaming documentation
- Unity documentation
- specification indexes

Inspect Git status.

Determine exactly which files belong to Phase 12.

Do NOT modify unrelated work.

============================================================
STEP 2 — OWNERSHIP AUDIT
============================================================

Prove there is exactly one owner for each responsibility.

Verify:

1. One WebSocket transport owner.
2. One synchronization owner.
3. One coordinate conversion owner.
4. One runtime car registry.
5. One visual car registry.
6. One vehicle transform owner.
7. One track scene owner.
8. One telemetry visualization owner.
9. One vehicle effects owner.
10. One Unity mode presentation owner.
11. One performance scheduler/optimization owner.
12. One integration test harness.

Search for duplicate:

- WebSocket clients
- coordinate converters
- car registries
- transform appliers
- track runtimes
- telemetry runtimes
- effect runtimes
- LIVE/REPLAY engines
- ReplayClock implementations
- interpolation/extrapolation/prediction implementations
- transport/authentication systems
- EventBus implementations
- runtime authorities

If duplicates exist, DO NOT automatically delete them.

Determine whether they are legitimate test doubles/interfaces/stubs or genuine competing production authorities.

Report findings.

============================================================
STEP 3 — ARCHITECTURAL BOUNDARY AUDIT
============================================================

Verify assembly dependencies.

Required principles:

Presentation must not own Transport.

Domain must not depend on Presentation.

Domain/runtime must not depend on Unity rendering APIs where prohibited.

Coordinate conversion must remain centralized.

Cars must not implement their own axis/unit conversion.

Rendering must consume RuntimeCarState.

Transform application must consume 12.4-converted Unity position/orientation.

Track must not become a coordinate converter.

Telemetry visualization must not become a transport client.

Effects must not become a telemetry ingestion system.

Mode presentation must not implement ReplayClock/seek/playback.

Performance must observe/schedule rather than become a new runtime authority.

Integration tests must not become production runtime infrastructure.

============================================================
STEP 4 — PHASE 10 / 11 REGRESSION
============================================================

Run the established Phase 10/11 regression suite.

Use the repository's existing commands rather than inventing replacements.

At minimum verify the previously established suites covering:

- API
- runtime
- Phase 10
- Phase 10 acceptance
- transport integration
- live streaming acceptance

Record the EXACT command and EXACT result.

Do not merely state "tests pass".

If tests fail:

1. Identify whether failure is caused by 12.14.
2. Identify whether it is pre-existing.
3. Do not modify unrelated Phase 10/11 systems.
4. Report exact failures.

============================================================
STEP 5 — UNITY PROJECT VALIDATION
============================================================

Inspect:

unity/Packages/manifest.json

Inspect:

unity/ProjectSettings/

Inspect whether a valid Unity project exists.

Determine whether Unity Editor/Test Framework can actually execute.

IMPORTANT:

The previous Phase 12 reports state:

UNITY_TESTS_NOT_EXECUTED

because:

unity/Packages/manifest.json is absent.

You MUST verify this rather than assuming it remains true.

If Unity is unavailable:

- do NOT claim Unity tests passed.
- do NOT claim Unity tests failed.
- report:

UNITY_TESTS_NOT_EXECUTED

and explain the exact environment limitation.

If Unity is genuinely available and the project/test framework is runnable:

execute the authored Unity EditMode tests.

If PlayMode tests are genuinely available, execute them too.

Record exact results.

============================================================
STEP 6 — PHASE 12 INTEGRATION TESTS
============================================================

Inspect:

unity/Assets/RaceVision/Tests/EditMode/Integration/

Verify the Phase12PipelineHarness and existing tests.

Expected coverage includes:

LIVE connect
→ multi-car synchronization
→ track binding
→ telemetry
→ effects
→ LIVE → REPLAY
→ REPLAY → LIVE
→ reconnect
→ state invalidation
→ rebuild
→ shutdown

Verify:

- 1 car
- 5 cars
- 10 cars
- 20 cars
- 24 cars where authored
- multiple DriverIds
- session isolation
- stale sequence handling
- malformed input handling
- coordinate conversion
- transform application
- telemetry availability
- effect transitions
- collision edge behavior
- LIVE/REPLAY same runtime path
- reconnect clearing
- performance budget behavior

Do not invent new production features to make a test pass.

============================================================
STEP 7 — LIVE / REPLAY ACCEPTANCE
============================================================

Verify:

LIVE and REPLAY use the same Unity entity/rendering path.

Verify Unity does NOT contain:

- ReplayClock
- local replay authority
- local playback authority
- seek authority
- interpolation engine
- extrapolation engine
- prediction engine

The server/Phase 10 runtime remains authoritative.

Unity mode is presentation state only.

Verify:

Live → Replay

Replay → Live

works through authoritative synchronized mode.

============================================================
STEP 8 — COORDINATE ACCEPTANCE
============================================================

Verify 12.4 remains the sole coordinate conversion owner.

Verify:

- metres/unit policy centralized
- axis mapping centralized
- handedness centralized
- origin policy centralized
- invalid NaN/Infinity rejected
- missing coordinates rejected safely
- orientation not fabricated
- no local conversion in rendering
- no local conversion in vehicle entities
- no local conversion in track runtime

Verify RuntimeCarState uses converted Unity position/orientation.

============================================================
STEP 9 — VEHICLE ACCEPTANCE
============================================================

Verify:

DriverId is the sole runtime car key.

Verify:

RuntimeCarRegistry

remains the sole runtime vehicle registry.

Verify:

CarVisualRegistry

is only a presentation binding registry.

Verify lifecycle:

Unknown
Available
Active
Stale
Unavailable
Removed

Verify stale cars are not accidentally destroyed unless policy requires removal.

Verify reconnect/session invalidation cannot leak vehicles from the previous session.

============================================================
STEP 10 — RENDERING ACCEPTANCE
============================================================

Verify:

MultiCarRenderer

consumes 12.5 runtime state.

Verify:

VehicleTransformApplier

is the sole transform owner.

Verify:

- position applies only when available
- orientation applies only when valid
- missing orientation preserves previous orientation
- invalid quaternion is rejected
- no fabricated heading
- no direct transport access
- no JSON parsing
- no network access
- no coordinate conversion duplication

Verify no per-frame GameObject discovery or Find calls were introduced.

============================================================
STEP 11 — TRACK ACCEPTANCE
============================================================

Verify:

TrackSceneRuntime

is the sole track scene authority.

Verify lifecycle:

Unloaded
Loading
Loaded
Bound
Active
Unbinding
Unloaded

Verify coordinate definition compatibility.

Verify session/track binding isolation.

Verify no fabricated circuit geometry.

Verify cars and track occupy the same authoritative coordinate world.

Verify TrackRoot remains compatible with future Blender-imported prefabs.

============================================================
STEP 12 — TELEMETRY ACCEPTANCE
============================================================

Verify telemetry visualization consumes RuntimeCarState only.

Verify supported channels are handled safely.

Verify missing values are represented as unavailable rather than fabricated.

Verify display conversion does not mutate canonical telemetry.

Verify no telemetry visualization component becomes an ingestion/network layer.

============================================================
STEP 13 — EFFECTS ACCEPTANCE
============================================================

Verify:

VehicleEffectsRuntime

is the sole effects authority.

Verify effects are derived only from available canonical channels.

Verify:

- wheels only when wheel data exists
- brake lights only when brake data exists
- DRS only when DRS data exists
- smoke only from explicit smoke channels
- damage only from explicit damage channels
- collision only from explicit collision/impact channels
- exhaust/engine effects only from available data

No effect may fabricate unavailable telemetry.

Verify pooling remains bounded.

============================================================
STEP 14 — PERFORMANCE ACCEPTANCE
============================================================

Audit 12.12.

Verify:

- bounded update budgets
- no unnecessary SetActive
- sequence-based skips
- reusable buffers
- no LINQ in hot paths where prohibited
- no per-frame JSON/network operations
- no GameObject Find calls
- bounded effect pools
- LOD policy exists
- no false static batching of moving cars
- main-thread presentation ownership remains clear

IMPORTANT:

Do NOT claim an FPS target was achieved unless an actual Unity runtime benchmark was executed.

Do NOT claim GC targets were achieved unless actual measurements were collected.

Use:

BASELINE_NOT_PRODUCTION_SLA

where measurement evidence does not exist.

============================================================
STEP 15 — SECURITY / TRANSPORT BOUNDARY
============================================================

Verify Unity did not create a second authentication or authorization system.

12.2 may provide credentials to the Phase 11 transport boundary.

Unity must not:

- log tokens
- store credentials in ScriptableObjects
- bypass TLS validation
- implement a second auth system
- implement a second rate limiter
- implement a second server backpressure system

Verify reconnect performs re-authentication through the established transport mechanism.

============================================================
STEP 16 — BLENDER BOUNDARY
============================================================

This is an acceptance gate, NOT an asset-production task.

Verify:

Blender → exported asset → Unity import → prefab → RaceVision presentation binding

remains the intended boundary.

Do NOT create:

- F1 car meshes
- F1 liveries
- track meshes
- materials
- textures
- Blender files
- production prefabs

during Agent 12.14.

The absence of finished Blender assets is NOT a Phase 12 architecture failure.

Record it as an expected deferred production-asset limitation.

============================================================
STEP 17 — DOCUMENTATION RECONCILIATION
============================================================

Review and reconcile:

docs/Roadmap.md
docs/Architecture.md
docs/Streaming.md
docs/Unity.md
unity/README.md
unity/Assets/README.md
rendering/unity/README.md
tests/unity/README.md
specification indexes
Phase 12 specification documents
Agent handoff documentation

Phase 12.1–12.14 must be represented accurately.

Mark:

12.1 ACCEPTED
12.2 ACCEPTED
12.3 ACCEPTED
12.4 ACCEPTED
12.5 ACCEPTED
12.6 ACCEPTED
12.7 ACCEPTED
12.8 ACCEPTED
12.9 ACCEPTED
12.10 ACCEPTED
12.11 ACCEPTED
12.12 ACCEPTED
12.13 ACCEPTED
12.14 ACCEPTED

ONLY if all applicable acceptance criteria are satisfied.

Do not mark Unity execution as passed if it was not executed.

============================================================
STEP 18 — GIT / CHANGE SCOPE
============================================================

Inspect git status and diff.

Agent 12.14 must NOT commit.

Agent 12.14 must NOT push.

Agent 12.14 must NOT create a PR.

Do not revert legitimate existing uncommitted Phase 12 work.

Do not modify unrelated user work.

Report:

- files changed by 12.14
- existing dirty files
- unrelated changes detected
- backend/shared status

============================================================
STEP 19 — FINAL ACCEPTANCE GATES
============================================================

Create a comprehensive final acceptance matrix.

Minimum gates:

GATE-01 Phase 12 architecture
GATE-02 12.1 preserved
GATE-03 12.2 preserved
GATE-04 12.3 preserved
GATE-05 12.4 sole coordinate authority
GATE-06 12.5 sole runtime car authority
GATE-07 12.6 sole visual registry
GATE-08 12.7 sole transform authority
GATE-09 12.8 sole track authority
GATE-10 12.9 telemetry visualization
GATE-11 12.10 effects
GATE-12 12.11 LIVE/REPLAY
GATE-13 12.12 performance architecture
GATE-14 12.13 integration tests
GATE-15 multi-car isolation
GATE-16 session isolation
GATE-17 reconnect handling
GATE-18 coordinate validity
GATE-19 orientation validity
GATE-20 no interpolation/extrapolation/prediction
GATE-21 no ReplayClock
GATE-22 no duplicate transport/auth systems
GATE-23 no duplicate runtime authorities
GATE-24 Blender boundary
GATE-25 security/no secrets
GATE-26 documentation
GATE-27 Phase 10/11 regression
GATE-28 Unity test execution status
GATE-29 performance evidence honesty
GATE-30 repository scope
GATE-31 no commit/push/PR

Add additional gates where repository evidence indicates they are necessary.

Every gate must have:

PASS
FAIL
N/A
or ENVIRONMENT-LIMITED

Do not convert an unexecuted test into PASS.

============================================================
ACCEPTANCE CRITERIA
============================================================

Phase 12 may be declared ACCEPTED when:

1. All architectural authorities are intact.
2. No duplicate production subsystems exist.
3. Phase 10/11 regression remains green.
4. Phase 12 integration tests are authored and structurally valid.
5. Unity tests are genuinely executed if the environment supports them.
6. Otherwise Unity execution is explicitly recorded as:
   UNITY_TESTS_NOT_EXECUTED
7. No fabricated performance evidence exists.
8. LIVE/REPLAY remains server/runtime authoritative.
9. Coordinate conversion remains centralized.
10. Vehicle lifecycle/session isolation is preserved.
11. Track/cars share the same coordinate contract.
12. Transport remains separate from presentation.
13. Blender remains a future production asset pipeline and is not prematurely implemented.
14. Documentation accurately reflects the final state.
15. No unrelated backend/shared regressions are introduced.

============================================================
IMPORTANT FAILURE POLICY
============================================================

If an acceptance test fails:

DO NOT immediately rewrite production code.

First classify it:

A. Real Phase 12 defect
B. Existing/pre-existing defect
C. Environment limitation
D. Test defect
E. Documentation mismatch
F. Unrelated repository failure

Only fix genuine Agent 12.14 acceptance/documentation/test issues within scope.

Do not expand scope into a new feature agent.

============================================================
REQUIRED FINAL REPORT
============================================================

Return a detailed report using EXACTLY this structure:

# Agent 12.14 — Phase 12 Acceptance — Final Report

## 1. STATUS

ACCEPTED / NOT ACCEPTED / ACCEPTED WITH ENVIRONMENT LIMITATIONS

## 2. Executive Summary

## 3. Phase 12 Architecture Verified

## 4. Agent 12.1–12.13 Verification Matrix

| Agent | Component | Status | Verification |
|------|------|------|------|

## 5. End-to-End Architecture

Show the verified Phase 11 → Unity → presentation pipeline.

## 6. Authority / Ownership Audit

List every authority and confirm no duplicates.

## 7. LIVE / REPLAY Acceptance

## 8. Multi-Car Acceptance

## 9. Coordinate / Transform Acceptance

## 10. Track / Circuit Acceptance

## 11. Telemetry Acceptance

## 12. Effects Acceptance

## 13. Performance Acceptance

Clearly distinguish:
- measured
- authored
- design-reviewed
- BASELINE_NOT_PRODUCTION_SLA

## 14. Security / Transport Boundary

## 15. Blender Asset Boundary

## 16. Tests Executed

Give exact commands and exact results.

## 17. Tests Authored but Not Executed

Explicitly identify:

UNITY_TESTS_NOT_EXECUTED

if applicable.

## 18. Phase 10/11 Regression

Give exact count and command.

## 19. Static / Architecture Checks

## 20. Acceptance Gates

Provide complete GATE table.

## 21. Files Created

Only files actually changed by 12.14.

## 22. Files Modified

Only files actually changed by 12.14.

## 23. Backend / Shared Status

Explicitly state whether backend/shared changed.

## 24. Git Status

Explicitly state:
- committed or uncommitted
- push status
- PR status

Do NOT commit/push/PR.

## 25. Limitations / Risks

Be honest and specific.

## 26. Deferred Work

Include production Blender/F1 assets where appropriate.

## 27. Final Phase 12 Decision

Use exactly one:

PHASE 12 — ACCEPTED

or

PHASE 12 — ACCEPTED WITH ENVIRONMENT LIMITATIONS

or

PHASE 12 — NOT ACCEPTED

## 28. Recommended Next Phase

If accepted, identify the next phase from the project roadmap.

============================================================
FINAL RULE
============================================================

This is the FINAL ACCEPTANCE GATE for Phase 12.

Be conservative.

Evidence beats assumption.

Authored tests are not executed tests.

Architecture review is not runtime performance measurement.

A missing Unity package scaffold is an environment limitation, not permission to fabricate Unity test results.

Do not create new production functionality merely to make the acceptance report look complete.

Do not commit, push, or open a PR.

Begin the Phase 12 acceptance audit now.
```

---

If you want, I can:

- Provide detailed next steps for Step 1: Repository Audit
- Outline process for Step 6: Phase 12 Integration Tests execution
- Explain how to classify and report failures during acceptance testing
