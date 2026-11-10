# GUNPIRE Logistics — Implementation Roadmap

**Revision:** 1.0 · **Target:** X4: Foundations 9.00, heavily modded Rebirth(ed) installation  
**Status:** Architecture and acceptance plan; **no GUNPIRE implementation or in-game validation claimed**.  
**Source of truth:** `GUNPIRE_Logistics_Mod_Project_Scope.md`, with later user-approved Active/Passive, Intelligent Surge, temporary LMP behavior takeover, and dual-console diagnostics decisions incorporated. Where later decisions extend the original scope, they are marked as expansions.

## 1. Goal

Build a dependable, low-overhead construction-supply dispatcher. The player selects eligible ships and construction priorities. GUNPIRE schedules sourcing, reservations, delivery, and safe return of borrowed ships to their prior work. **No permanent takeover, reset of trader progression, endless static order queues, or EOC-like configuration complexity.**

**Three operating concepts:**

1. **Active / Construction Surge (`[F#/A]`)** — temporarily borrows player-selected GT, vanilla, or station ships for a chosen construction target, within the configured home/operating range, then restores original work.
2. **Passive (`[F#/P]`)** — dedicated, autonomous construction-supply roaming/gap filling. Profit is not a dispatch objective; actual unsatisfied demand is. Longstanding unmet requests gain increasing priority. *Expanded decision beyond the initial scope.*
3. **Shared construction dispatcher** — demand/reservation ledger, ship matching, site fairness, supply and route scoring, reporting. One committed route/job per ship at a time, with reassessment after completed deliveries. A multi-stop route is one bounded job, **not** a queued chain of unrelated future jobs.

## 2. Behavior contract (non-negotiable)

**Before an Active takeover:**
- Ship is enrolled/authorized; target is active and has unmet supply demand.
- Ship is eligible, has **zero active jobs/commitments**, zero trade cargo, and no outstanding transfers or trade reservations. If not, wait; do not interrupt its current trade.
- Preserve original **default behavior and parameters**, station/fleet commander and assignment, home, range, relevant orders, and an identifiable restoration snapshot **before** changing behavior.
- Set custom **LMP Active** behavior only after snapshot validation. Do not directly edit GT pilot XP/level/state tables.

**During Active control:**
- Dispatch only a single bounded purchase/delivery route per ship, reevaluating demand after completion. Consolidated ware/stop routing can be enabled once simple deliveries work.
- Honor selected source restrictions, inherited operating geography, cargo volume, reservations, cost/travel preferences, and live site priorities.
- Do not double-book ship, supply, or destination demand.

**Release:**
- When OFF is selected, finish a loaded/in-progress LMP delivery rather than strand cargo; stop allocating further work.
- Restore saved behavior **with parameters and home/commander assignment**, not merely the behavior name; release reservations; verify resumed state.
- If restoration is blocked, retain the snapshot, mark the ship **RESTORE_REQUIRED**, log a high-priority exception, and do not silently replace it with a generic idle order.

## 3. Technical architecture

### 3.1 Modules (proposed layout)

| Component | Responsibility | Implementation direction |
|---|---|---|
| `LMP_Core` | startup, configuration, persistent state and migration | MD XML |
| `LMP_ShipRegistry` | enrolled ships, eligibility, role, per-ship state | MD XML |
| `LMP_Takeover` | snapshot, handoff, active behavior, exact restoration | MD XML + AI order |
| `LMP_GT_Adapter` | recognize GT orders; observe pause/re-registration events; isolated special handling | MD XML, only if proven necessary |
| `LMP_Demand` | build-storage demand, stock, inbound reservations, shortage ledger | MD XML |
| `LMP_Supply` | supplier/offer freshness, source restrictions, price/distance | MD XML / AI helpers |
| `LMP_Reservation` | per-ware/site/ship commitments and their lifecycle | MD XML |
| `LMP_Dispatcher` | one ship/route selection, priority fairness, ship-size matching | MD XML |
| `LMP_Surge` | near-term next-module urgency and S/M/L/XL wave | MD XML; exact queue inspection requires proof |
| `LMP_Passive` | autonomous shortage gap filling and waiting-time weight | MD XML / AI |
| `LMP_UI` | ship picker, modes, priority panel, filters, statuses | Lua UI + MD bridge (verify hooks) |
| `LMP_Trace` | structured debug events, concise in-game notices | MD `debug_text` + logbook |
| `LMP_Monitor.ps1` | two Windows PowerShell views over one logfile | Windows PowerShell |

All extensions and global state are **GUNPIRE-namespaced**. Avoid editing GT, Kuertee, or SirNukes files unless an actual and unavoidable compatibility defect is demonstrated; maintain any adapter separately.

### 3.2 Stateful data

- **Ship record:** ship ID, pilot, class/capacity, enrollment, Active/Passive role, home/range, current state, job ID, snapshot ID, last health/event.
- **Behavior snapshot:** exact behavior ID, parameters, home/commander link and subordinate group, current applicable settings, capture time and restoration marker.
- **Demand key:** build-storage object + ware; requested, physically stored, game-visible inbound, LMP reserved/in-flight, remaining, priority and age.
- **Source offer:** station, ware, quantity available, offer price, last verified, eligibility and operating range.
- **Job record:** ship, site(s), ware(s), supplier(s), bounded pickup/drop route, quantities, reservation tokens, progression state and recovery history.
- **Persistent settings:** pool membership, activation, supply modes, source and route preferences, per-site priorities, log verbosity, recovery records.

**Derived shortage:** `max(0, requested − stored − externally incoming − LMP committed)` using only reservation quantities not already included in another term. The actual game APIs and inclusion semantics must be validated before this expression is implemented literally.

### 3.3 Ship state machine

`NORMAL → WAITING_FOR_ELIGIBILITY → SNAPSHOTTING → LMP_ACTIVE → SOURCING → PICKUP → DELIVERING → REEVALUATING → RESTORING → NORMAL`

Branches: `BLOCKED`, `JOB_FAILED`, `SHIP_MISSING`, `RESTORE_REQUIRED`, `DISABLED_DRAINING`. Every transition is idempotent and traceable; save/reload reconciles a recorded state against the actual game state before issuing another order.

### 3.4 Scheduling policy

- Shared pool; no permanent per-site ship assignments.
- Select eligible ships; rank shortage and age, site priority, cargo utilization, distance, and economic value of the shipment.
- Site priority starts at **50%** and is a **relative weight**, not a 50% fleet allocation. Low-priority sites continue making progress when serviceable.
- Prefer S / fast M for urgent small next-module needs; M for sustaining supply; L/XL for bulk volume. Do not force a large freighter to deliver a tiny residual unless no sensible alternative exists.
- Respect user modes: **all build storages**, **targeted build storage**, **closest build storage**.
- Source filters: **player only**, **non-player only**, **both**. Closest-to-ship / closest-to-deposit options; cost↔distance slider. Price sensitivity scales with shipment/build impact rather than blindly taking the cheapest offer.
- Revalidate demand and supplier quantities immediately before committing an order and again on completion/failure. Bound periodic reconciliation; favor event-driven wake-ups.

## 4. Delivery phases and exit gates

Each phase ends with a **working, observable vertical slice**. No speculative date estimates. Later features do not delay proving ship safety.

### M0 — Reference freeze and diagnostics harness

**Build:** minimal extension skeleton and startup log, version/config manifest, namespaced MD cues and one PowerShell launcher for two consoles. Use documented X4 launch arguments `-logfile lmp_debug.log -debug scripts`; output is stored in X4's personal data/save folder. Validate that MD `debug_text` writes to the file under 9.00.

**PowerShell Window A — Issues / high-level:** startup/shutdown, takeover success/failure, job failure, missing ware/station, restore failures, significant recovery, deduplicated unfillable shortage.  
**PowerShell Window B — Live operations:** eligibility decisions, state transitions, source candidates, reservation changes, selected orders, pickup/delivery results and relevant API calls.  
Use a shared trace prefix such as `[LMP][WARN][SHIP:...]`, `[LMP][OP][JOB:...]`; one source logfile and two independent filters. Keep INFO readable; TRACE switchable; no per-tick logging.

**Exit:** both windows show test messages live, filtering independently, with logging disabled/low-noise when not debugging.

### M1 — Ship takeover and restoration proof

**Build:** enrollment of one GT ship, strict empty/zero-job eligibility, snapshot, assign minimal LMP Active behavior (initially idle/no trading), restore original behavior and home. Test standalone GT and station/fleet GT variants separately.

**GT facts from supplied code:** `gt_order_monitor_bridge.xml` handles `GTOrderRemoved` and delayed verification; `gt_core_system.xml` preserves pilot XP when pausing but can clean up ship registry/transient state. The experiment is **whether GT actually resumes its complete behavior/settings** after LMP restoration; loss of pilot XP is not the presumed failure mode.

**Exit:** one ship completes takeover→release without cargo loss, XP reset, commander loss, persistent orphan state or changed trader settings. If variant cannot be reliably restored, hold it ineligible until that variant is supported.

### M2 — Build-storage demand and reservations

**Build:** detect player construction sites/build storage; read ware demand and on-hand material, respect game-visible reservations, maintain LMP's own in-flight commitments; support duplicate-request suppression; identify the next valid shortage.

**Exit:** ledger balances for one site with multiple wares while a vanilla/GT ship also delivers. Repeated scans do not create phantom demand or double-subtract the same reservation.

### M3 — First real delivery

**Build:** use one LMP Active freighter to buy one material from one allowed source and deposit it at construction storage; release reservation and restore original assignment or accept another job if still active.

**Exit:** actual in-game delivery, accurate stock and credit effects, no duplicate buy, clean OFF-while-loaded completion. Tests use a **copy** of the user's save.

### M4 — Shared multi-site dispatcher

**Build:** multi-ware shortages, global ship pool, live priority weighting, ship-size/capacity matching, shortage age and fairness, basic source filtering/cost-distance scoring; one bounded delivery per ship with re-evaluation.

**Exit:** two sites / two ships function, then baseline **20 ships / 6 sites** without starvation, overbuying or static job piles.

### M5 — Active Construction Surge

**Build:** user selects a construction target and can mobilize **up to 20 eligible ships for that target**; ship loan begins only after current commitments finish. Use home/sector operating range. Intelligent waves: rapid S/fast M kickstart, M sustain, L/XL bulk, then release.

**Next-module precision:** determine if the 9.00 MD/Lua interfaces expose the actual next ordered construction module's costs, less its stored and incoming materials. **Not yet verified.** If unavailable, use a clearly marked build-storage-shortage fallback instead of inventing module costs or blocking the entire dispatcher.

**Exit:** urgent next-module shortage receives the earliest practical deliveries, bulk supply follows, and idle ships return to original automation without manual repair.

### M6 — Passive fleet

**Build:** `[F#/P]` ships remain independently available to roam for construction shortages; older unfilled buy needs increase in priority nonlinearly; profit is not the mission objective. Passive must not steal Active-reserved quantities or bypass source restrictions.

**Exit:** passive agents service aging unattended sites without interfering with Active Surge or starving other construction sites.

### M7 — Consolidated routes and forecasting

**Build:** where supported and safe, multiple compatible wares per load, opportunistic nearby source pickups and multi-site deposits; minimize stop count and empty travel. During a route, consider near-source/near-destination additions toward roughly **80% useful cargo fill**, but only when reservations and delivery feasibility can be rechecked. Add short-horizon demand anticipation; **six game hours** is the proposed planning horizon, not permission to reserve six hours of inventory.

**Exit:** fewer stops/less empty travel than basic dispatcher, with no deadlocks and no committed material left without a valid destination. If route complexity makes completion fragile, preserve M4 single-leg fallback.

### M8 — Compact management UI

**Build:** accessible fleet selection/enrollment; Active/Passive; ON/OFF; site modes; per-site priority sliders; source ownership filters; cost/travel slider; advanced controls collapsed; counters for available / pending / hauling / blocked / restoring; actionable exceptions. GUI updates should avoid heavy per-frame scans.

**Exit:** all core controls work with GT's UI, Kuertee UI Extensions, and SirNukes present, with no file overwrites or hidden order changes.

### M9 — Persistence, failure recovery, mod compatibility and scale

**Build/test:** save/load during every ship/job state; restart while OFF/draining, lost source/destination/ship, changed commander, interrupted order, 0 stock, lost reservation, partial load, player manual override, SETA, and simultaneous construction sites. Run 20/6 as a minimum fixture and stress progressively larger fleets. Profile scheduler frequency and debug cost; cap retry/backoff and log size by frequency/verbosity.

**Exit:** long unattended play with no indefinite job lock, duplicate commitments, trader dereliction, unrecoverable borrowed ship, or unbounded polling. Failure should degrade gracefully and report one clear actionable exception.

### M10 — Release gate

Package with `content.xml`, documented install and uninstall considerations, config defaults, log launcher, acceptance test checklist, and a known-limitations file. Validate XML against available 9.00 XSDs and inspect resolved script IDs, dependencies and name collisions; in-game behavior can **only** be called tested after actually running it in X4.

## 5. Compatibility matrix (prioritized)

| Integration | Risk / expected interaction | Required test |
|---|---|---|
| Galaxy Trader 1.0.4 | order-removal cleanup and temporary registry state; XP is pilot-associated | standalone and subordinate snapshot→Active→restore; confirm same settings/level and resumed trades |
| Vanilla trader/station subordinate | replacement behavior, commander/home restoration | return to exact prior assignment and operating limits |
| KUDA/DeadAir AI Tweaks | trade-offer filtering, reservation policy, navigation and build-storage priorities | avoid overcommitment and order thrashing under active settings |
| EOC / station automation | competing ship control | explicit exclusive ship ownership / no dual-issued orders |
| Station Trader Multi-Order / repeat-transfer scripts | pending jobs and order chains | block takeover until truly idle and empty |
| Station Storage Allocation / Supply Needs Planner | changes demand availability | read current actual demand, no assumptions about stock |
| Kuertee UI Extensions + SirNukes APIs | UI and bridge coexistence | no overwritten files; verify loaded callbacks and protected-UI behavior |
| VRO, Reemergence, OTAS ships | modded wares, hulls, cargo capacities | read actual runtime values, never assume standard size/ware templates |

These are **test risks**, not confirmed conflicts. The uploaded full GT ZIP and scripting HTML allow source inspection; the rest of the Rebirth(ed) stack has not been fully audited from installed source.

## 6. Exception handling policy

| Event | LMP response |
|---|---|
| Ship has cargo or an active job | leave original behavior intact; WAITING_FOR_ELIGIBILITY |
| Demand disappears before purchase | cancel uncommitted plan, release LMP reservation, recompute |
| Supply offer disappears | try another allowed source or mark BLOCKED with backoff |
| Part of pickup succeeds | update actual cargo and reserve only physically deliverable quantity; complete/resolve safely |
| Destination destroyed or no longer accepts ware | do not dump cargo; enter recovery, seek safe user-approved outcome and warn |
| Ship destroyed | release reservations, retire job, preserve forensic log; no restoration attempt |
| User disables Active while loaded | finish existing delivery, do not accept another, then restore |
| Player manually overrides ship | do not fight the player; record loss of LMP control and avoid restoring over the player's new explicit order without clear safety policy |
| Save loaded mid-job | reconcile actual cargo, orders, destination and reservations before issuing any new job |
| GT not restored | retry only with checked snapshot; RESTORE_REQUIRED and actionable issue log; never fabricate new GT defaults |

## 7. Acceptance tests and required evidence

1. **GT takeover:** capture behavior ID, parameters, range/home, commander, pilot XP/level before and after; log full lifecycle.
2. **Loaded trader:** 0 hijacks while cargo or active job remains; takeover only on confirmed readiness.
3. **OFF during trade:** existing cargo reaches destination; previous job resumes.
4. **Reservations:** two ships cannot commit to the same remaining shortage; competing trader deliveries are reflected.
5. **Fairness:** 20 ships / 6 sites progress according to priorities without starving low-priority sites.
6. **Surge:** up to 20 authorized ships mobilize; small urgent payload arrives before bulk when supply geography permits.
7. **Source policy:** player-only, NPC-only, and both actually constrain offers; distance/cost slider changes choices.
8. **Load/reload:** no duplicated delivery, lost reservation, missing snapshot, or orphaned Active behavior.
9. **Fleet scale:** bounded dispatch work, no frame-by-frame global scans and no tracing flood.
10. **Diagnostic windows:** important events visible in Window A; detailed decisions/API calls visible in Window B; single authoritative log.

## 8. Technical checkpoints — not yet established

- **Exact order snapshot/restore API and completeness** for every GT/vanilla/station job variant.
- **Actual GT re-registration behavior** after restoring the exact previous default order.
- **How 9.00 exposes construction queue/module-specific materials**, if at all. Aggregate build-storage demand already has source examples.
- **Reservation inclusion semantics** between game trade offers, GT's separate ledger and LMP's own ledger.
- **Lua UI callbacks and MD bridge details** under protected UI and existing mods.
- **Multi-pickup/multi-drop feasibility** without a fragile queue; build only after one-leg delivery is reliable.
- **Six-hour prediction quality**; advisory prioritization first, never long-horizon hard reservation.

## 9. Immediate next build

**Start with M0 + M1 together:** an installable, minimal test extension plus `LMP_Monitor.ps1`, with no autonomous trading enabled. Register one safe GT ship; confirm empty/no active job; capture snapshot; activate LMP; restore original assignment; observe GT's pause/cleanup/re-registration events. The first success criterion is **GT performing its original trading again without manual intervention**.

Only then enable the one-ware purchase/delivery slice. This is the shortest path to falsifying the only major uncertain integration assumption without jeopardizing a fleet.

## 10. Verified references

- Uploaded full `Galaxy-Trader 1.0.4 ... .zip`: order monitor and core pilot lifecycle; `gt_order_monitor_bridge.xml`, `gt_core_system.xml`, `gt_ship_management.xml`, `gt_xp_training.xml`.
- Uploaded `X4_Scripting_Reference.html` (9.2 MB): MD/AI actions and script property reference; signatures to check as code is authored.
- Uploaded `01_GUNPIRE_Integration_Reference.md`, `02_UI_and_Support_APIs.md`, `03_Extracted_Source_Index.md`.
- Egosoft X Community Wiki, *Mission Director Guide*, “Script debug output”: `-logfile debuglog.txt`, `-debug scripts`, `<debug_text>`.

**Status legend:** *Specified* = user decision; *Source-confirmed* = GT/guide implementation observed; *To validate* = needs exact API or in-game proof; *Proposed* = internal architecture, not an unapproved change to the player's required behavior.
