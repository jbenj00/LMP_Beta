# X4: GUNPIRE Logistics Override — Project Handoff
**Status:** Requirements capture / pre-development  
**Game:** X4: Foundations 9.00, heavily modded X4 Rebirth(ed) collection  
**Purpose:** Portable project scope, requirements, compatibility risks, and validation plan.

## 1. Vision
Build a lightweight, low-friction logistics dispatcher that temporarily borrows a user-selected fleet of ships from their normal trading/automation behaviors to fulfill construction build storage needs. It should coordinate multiple construction sites, intelligently source materials, distribute work fairly, minimize wasteful travel, and restore each ship to its prior job afterward.

**Core principle:** The player sets priorities; the dispatcher handles individual deliveries. Avoid an EOC-style wall of configuration.

## 2. Scope — Confirmed Requirements

### 2.1 Fleet selection and activation
- User selects any eligible ships and assigns them to a logistics fleet/pool.
- A simple **Build Priority ON/OFF** toggle activates a temporary override, not a permanent replacement of their existing trader mod.
- For each ship with **nonempty cargo hold**, allow its current assignment to finish and wait for cargo to reach zero before taking control.
- For empty ships, capture the original behavior/assignment/order state and take control.
- Do not count ammunition, deployables, or installed equipment as trade cargo.
- On deactivation, finish the active delivery safely, then restore original behavior and assignments.
- Ships added while active follow the same empty-cargo handoff rule.
- Preserve existing trader progression/leveling; do not reset it.

### 2.2 User-facing supply modes
Requested menu options:
- Fulfill **all** build storages.
- Fulfill **targeted** build storage.
- Fulfill **closest** build storage.
- Additional modes may be added later, without bloating the initial UI.

### 2.3 Source selection and route economics
- Source filter: **Player-owned stations only / non-player-owned only / both**.
- Options for **closest source to ship** and **closest source to deposit**.
- Slider between cheaper sourcing and shorter travel; center gives balanced preference.
- Cost sensitivity should be **value-aware**: saving 25k Cr on a 100M Cr construction project should not justify four jumps for a low-value delivery.
- Relative product/delivery value should influence how strongly savings matter.
- Avoid unnecessary travel and tiny inefficient orders.

### 2.4 Dynamic order scheduling
- On activation, schedule **only the next purchase and delivery** for each available ship, not a long static queue.
- After the ship deposits at build storage and empties its cargo, recalculate current needs, available supplies, priorities, and assignments.
- Continue until needs are satisfied, supply is unavailable, or the override is disabled.
- Recheck build-storage demand and supply offers at each dispatch.
- Track material already reserved, purchased, or in transit to avoid duplicate over-ordering.
- Never intentionally exceed demand or cargo capacity.

### 2.5 Multi-site fleet allocation
Example target: **20 ships servicing 6 active construction sites**.
- Treat ships as a **shared pool**.
- Balance delivery progress across all active sites; do not permanently dedicate ships to a single site.
- Account for combined fleet cargo capacity and individual ship capacity.
- Favor large cargo ships for bulk orders and smaller ships for small outstanding quantities.
- Distribute workload fairly, while considering urgency, cargo efficiency, distance, and current shortages.
- Keep other builds progressing when some sites receive higher priority.

### 2.6 Live site priority
- After starting, expose a compact expandable panel with each active construction site.
- Each site defaults to **50% priority**.
- User can raise, e.g., builds 3 and 5 to **75%**.
- These are **relative scheduling weights**, not fixed percentages of ships or hard exclusivity.
- Priority adjustments apply to future dispatches; don't needlessly interrupt loaded ships.
- Low-priority builds must still receive service (subject to material availability).

### 2.7 Logging and reporting
- Optional logbook notification when a construction supply task completes.
- Optional logbook notice for **unfillable shortages**, identifying the station and ware.
- Avoid spamming duplicate notices for the same unresolved shortage.
- Earlier related idea: selectable station/time-range transaction export; **not required for initial dispatcher** unless separately approved.

## 3. UX Principles
- One fleet selection, one supply-mode selection, one activation toggle.
- Hide advanced routing/source options behind an expandable area.
- Show active / pending takeover / delivering / sourcing / blocked / restoring counts.
- Provide simple per-site priority sliders.
- Present only actionable exceptions, not routine event spam.
- Make OFF mean **return to previous work**, not merely idle.

## 4. Proposed Internal Design (not yet approved implementation)
- **Ship state machine:** Normal → PendingEmpty → Snapshot → Controlled → Delivering → Reevaluate → Restoring → Normal.
- **Demand ledger:** per-station/per-ware requested quantity, stock in build storage, outstanding demand, inbound reservations.
- **Source ledger:** stock and trade offers with freshness/availability checks.
- **Dispatcher:** select site + ware + ship + source; reserve; issue one purchase/delivery; validate completion; recalculate.
- **Priority scoring:** weighted fairness + unmet quantity + cargo utilization + distance + value-adjusted purchase cost.
- **Safety:** prevent stale reservations, duplicate orders, overfilling, deadlocks, and loss of preexisting cargo.
- **Persistence:** survive save/load and toggle cycles; recover gracefully if ships, stations, sources, or orders disappear.
- **Scope boundary:** don't rewrite vanilla economy or the existing trader leveling mod.

## 5. Known Mod Environment & Compatibility Watchlist
These are **reported installed/active or visible in extension settings**, not a verified full Vortex inventory. Risk labels are preliminary hypotheses; they are not confirmed conflicts.

| Mod / system | Known status | Potential interaction | Initial risk |
|---|---|---|---|
| **Existing trader leveling mod** (exact name unconfirmed) | Active, user likes progression | Overriding default behavior, losing mod-specific state/XP, resuming orders | **Critical — identify first** |
| **EOC** (exact mod/full title unconfirmed) | Installed | Competing station/fleet control, automation roles, order changes | High if it controls same ships |
| **KUDA / DeadAir AI Tweaks** | Mostly enabled | Trade offer filtering, reservations, prioritization, movement, ship behaviors | High — test individual toggles |
| **GS QoL Fleet Trade / Repeat Transfer Order** | Visible in extension menu | Competing repeat/transfer orders; safe handoff and restoration | High if shared ships |
| **Station Trader Multi-Order** | Visible | Overlapping station trader assignments/orders | High if shared ships |
| **Station Storage Allocation** | Visible | Ware limits, storage reservations, supply availability | Medium |
| **Kuertee UI Extensions / Trade Analytics** | Visible | UI integration, menu compatibility, log presentation | Medium |
| **Supply Needs Planner** | Visible | Could overlap demand planning, likely coexist if read-only | Medium |
| **DeadAir Blueprint Analysis** | Reported active | Little direct overlap with supply dispatcher | Low |
| **DeadAir Evolution** | Off | No expected active interaction | Low |
| **DeadAir Dynamic War / Dynamic News** | Reported off | No expected active interaction | Low |
| **VRO / Reemergence** | Active collection components | Ship/ware economy changes, modded ships, capacities | Medium |
| **OTAS Shippack** | Active | Additional ship hulls, unusual speed/cargo characteristics | Low–Medium |
| **Other KUDA logistics/navigation options** | Several enabled | ForceTravel, trade filtering, reservations, build storage priority | Medium–High |

**Specific KUDA settings previously observed enabled:** `Job_Helper - BuildAtClosestOnly`, `Job_Helper - HigherDistanceScaling`, trade offer filtering improvements, `ImprovedBuildStoragePrioritization`, `StopIgnoringReservations`, `StopBreakingTrades`, and several movement/travel tweaks. Verify exact setting names and effects against the installed version.

**Important:** The prior chat established the *presence* of several extension menu entries, not necessarily that every entry is active. Confirm enablement/version before attributing conflicts.

## 6. Technical Feasibility Questions / Unknowns
1. Identify exact trader leveling mod, version, and how it stores XP/state.
2. Determine which X4 order/behavior state can be snapshotted and restored reliably, including commander/subordinate relations.
3. Verify how build-storage needs, trade offers, available stock, reservations, and transfer completion are exposed to mod scripts.
4. Check whether third-party behavior state is script-accessible, or if a non-invasive **wait until idle / release** model is safer.
5. Determine correct save/load persistence for dispatcher state and pending shipments.
6. Validate behavior with player-owned versus NPC-owned supply sources, trade restrictions, and faction reputation.
7. Check compatibility with 9.00 and installed KUDA/EOC/UI-extension versions.
8. Decide how to handle partially filled cargo, interrupted trades, destroyed ships, missing stations, source shortages, and toggling OFF mid-delivery.

## 7. Suggested Development Milestones
**M0 — Compatibility reconnaissance:** identify trader mod, inspect installed scripts/API, verify read access to build-storage needs and ship orders.

**M1 — Minimal proof of concept:** 2 ships, 2 construction sites, one ware; safe empty-cargo takeover; one purchase/delivery; restore.

**M2 — Dispatcher:** multi-ware demand ledger, reservations, cargo-aware matching, supply-source selection, dynamic re-evaluation.

**M3 — Controls:** fleet picker, ON/OFF toggle, source filters, cost/distance slider, live per-site priority sliders.

**M4 — Reliability:** save/load, interrupted jobs, no-stock handling, logging, deduplicated shortages, mod compatibility testing.

**M5 — Scale:** test 20 ships / 6 sites, then larger GUNPIRE fleets; benchmark scheduling overhead and order stability.

## 8. Acceptance Criteria
- A ship with cargo never gets hijacked before its cargo is emptied by its existing task.
- A ship with zero cargo can be borrowed and later restored to its previous work.
- Existing trader leveling/progression remains intact.
- Six simultaneous sites receive balanced service; priority sliders adjust attention without starving the rest.
- Large ships preferentially handle large-volume shipments, small ships small-volume shipments.
- No duplicate over-ordering from in-flight shipments.
- One active purchase/deposit cycle per ship; next task selected from updated needs.
- Player/non-player source filters work as selected.
- Shortage and completion notifications can be enabled/disabled.
- No persistent order hijacking, lost cargo, or unbounded log spam.

## 9. Out of Scope for V1
- Replacing the existing trader leveling system.
- Entire EOC-style station role management.
- Automatic factory construction or station blueprint planning.
- Full historical transaction export/dashboard.
- Combat fleet control or military supply automation.
- Autonomous NPC faction logistics changes.

## 10. Project Handoff Notes
**Confirmed user intent:** A temporary, intelligent build-storage supply override for any selected fleet; simple UI; fair and priority-weighted dispatch; value-aware sourcing; cargo-safe takeover and restoration.

**Do not assume:** Exact trader mod name, EOC integration API, or compatibility with all extensions. Those need inspection before code is authored.

**First project task:** Identify the leveling trader mod and test whether its behavior can be paused and restored without resetting progression.
