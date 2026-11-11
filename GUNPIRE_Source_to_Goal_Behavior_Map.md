# GUNPIRE Logistics — Goal-to-Source Behavior Map
**Revision:** 2026-11-11 · **Purpose:** Implementation reference for Codex / source-guided development  
**Target:** X4: Foundations 9.00; Galaxy Trader 1.0.4 and heavily modded Rebirth(ed) installation

## Reading this document
This maps **what GUNPIRE must do** to **where an existing implementation or relevant API can be inspected**. It is not permission to copy an entire third-party behavior or replace the existing mod.

**Evidence labels:** `SOURCE` = file and relevant mechanism inspected in the uploaded archive; `GOAL` = user-confirmed desired behavior; `GAP` = not yet demonstrated to work in GUNPIRE. A file being present does not prove interoperability or in-game correctness.

**Source roots (paths below are relative):**
- **LMP**: `GUNPIRE_Full_Project.zip / gunpire_logistics/`
- **Scope**: `GUNPIRE_Full_Project.zip / refs/GUNPIRE_Logistics_Mod_Project_Scope.md`
- **GT**: `GUNPIRE_Mod_Reference_Pack.zip / GUNPIRE_Reference_Pack/source/galaxy_trader/`
- **VAS**: `x4-foundations-supply-needs-planner-main.zip / x4-foundations-supply-needs-planner-main/src/`
- **X4 API reference**: `GUNPIRE_Full_Project.zip / refs/x4_scripting_ref/schemas/` and `X4_Scripting_Reference.html`
- **Indexer**: `GUNPIRE_Indexer.zip / GUNPIRE_Indexer/gunpire_index.db` (symbol/cross-reference index; not a substitute for source text)

## 1. Operating modes — keep these separate

| Goal | Behavioral source / reference | LMP destination | Implementation rule |
|---|---|---|---|
| **Active GT ships** retain normal MK1 or MK3 trading until **FILL BUILD STORAGE** is toggled | `GT/aiscripts/order.trade.galaxytradermk1.xml`; `GT/aiscripts/order.trade.galaxytrader.xml` (MK3 family); `GT/md/gt_ship_state_manager.xml` | `md/LMP_Takeover.xml`, `md/LMP_ShipRegistry.xml` | **GOAL**: GT remains the default behavior; LMP only temporarily borrows at a safe idle/pre-assignment boundary. |
| **Passive ships** use permanent `LMP > PASSIVE` | GT trading scripts as algorithm references, not as ownership model | `md/LMP_Dispatcher.xml`, `md/LMP_ShipRegistry.xml` | **GOAL**: LMP owns dispatch continuously. Do not snapshot/restore a GT job that passive ships are not running. |
| **Temporary active takeover** becomes `LMP > ACTIVE` | `GT/md/gt_ship_state_manager.xml`, `GT/md/gt_ship_state_utilities.xml`; `GT/aiscripts/order.trade.perform.xml`; `GT/md/gt_trading_signals.xml` | `md/LMP_Takeover.xml`, `md/LMP_Recovery.xml` | **GOAL**: intercept → capture original state → Hold safely → verify → LMP ACTIVE → deliver → restore. **GAP**: exact pre-assignment hook and supported Hold/default-order swap still need source-level integration proof. |
| **Eligibility** requires no trading cargo and no active buy/sell/dock/undock commitments | GT ship/order state scripts above; `GT/aiscripts/lib.gt.ship.opstate.xml` | `md/LMP_Takeover.xml` | **GOAL**: idle and empty must both be true. Cargo-empty alone is insufficient. |

**Important:** The original scope's global Build Priority ON/OFF and temporary borrowing description covers the active-ship use case. The user's subsequent explicit **Active vs Passive** distinction is authoritative for this mapping; do not collapse them into one mode.

## 2. Fulfillment hierarchy

| Rank | LMP behavior | Closest source to study | Where to implement |
|---|---|---|---|
| **1** | Player-owned **construction build storage** shortages | `VAS/md/supply_needs_planner_lib.xml` (`SupplyNeedWares`); `VAS/md/supply_needs_planner.xml` (`RunPlannerBody`); `VAS/md/supply_needs_planner_interact_menu.xml` (`HasStorageNeed`) | `LMP_Demand.xml`, `LMP_Dispatcher.xml` |
| **2** | Aged **player-owned station buy orders**, oldest eligible first, weighted strongly above ordinary trade | `GT/aiscripts/lib.gt.mk4.player.stations.xml`; `GT/aiscripts/lib.gt.mk4.tradematch.xml`; `GT/aiscripts/lib.gt.mk4.score.trades.xml`; `GT/aiscripts/order.trade.galaxytradermk4.xml` | `LMP_Demand.xml`, `LMP_Dispatcher.xml` |
| **3** | **MK1-style selling** if no eligible higher-priority work | `GT/aiscripts/order.trade.galaxytradermk1.xml`; `GT/aiscripts/lib.gt.search.sell_only.xml`; `GT/aiscripts/lib.gt.live.search.xml`; `GT/aiscripts/lib.gt.score.trades.xml` | `LMP_Dispatcher.xml`, `LMP_Sources.xml` |

**GOAL:** Reuse GT's buy/sell *search and validation approach*, then apply LMP-specific priorities. A high weight must never turn an invalid offer into a valid trade. Build-storage demand ranks above aged POS buy orders; aged POS orders rank above general selling.

**GAP:** An *age timestamp* for POS orders is not proven to exist in GT's indexed data. If GT does not expose a stable order-created/first-seen time, LMP must persist its own first-seen timestamp, retaining it across rescans and save/load. Do not equate a trade-offer refresh with a new demand.

**GAP:** GT's `lib.gt.mk4.*` AI scripts are not automatically callable as MD `run_actions` libraries. Identify the actual execution boundary and adapt logic only where the script language/API permits.

## 3. Demand detection and quantity calculation

**SOURCE — VAS**
- `md/supply_needs_planner_lib.xml` → `SupplyNeedWares(Target)` enumerates target supply wares.
- `md/supply_needs_planner_interact_menu.xml` → `HasStorageNeed`, `HasAnyRealTradeOffer`, `WareSelectList` separate storage-target needs from visible trade offers.
- `md/supply_needs_planner.xml` → `RunPlannerBody` uses `find_buy_offer` for target/ware/ship, tracks planned amounts, and constructs purchase/delivery legs.

**SOURCE — current LMP**
- `md/LMP_Demand.xml` → `LMP_ScanBuildStorages` already scans player stations and initializes demand/shortage ledgers.
- `md/LMP_Reservations.xml` → `LMP_Reserve` and reservation ledger.

**Copy/adapt:** VAS's distinction between target storage needs and executable buy offers; recompute outstanding quantity after accounting for current stock and LMP inbound/reserved shipments.

**Do not copy:** VAS's whole queued multi-leg planner. Original GUNPIRE scope explicitly requires **one next purchase/delivery per ship**, then a fresh decision.

**GAP:** Existing LMP demand calculation needs line-by-line reconciliation with VAS's storage targets, trade-offer availability, and reservation subtraction before declaring it correct.

## 4. Source selection and trade validity

**SOURCE — GT**
- `aiscripts/lib.gt.mk4.free.supplier.xml`, `lib.gt.mk4.offer.refresh.xml`, `lib.gt.mk4.validate.amounts.xml`, `lib.gt.mk4.validate.reach.xml`, `lib.gt.mk4.tradematch.xml`.
- `aiscripts/lib.gt.live.search.xml`, `lib.gt.cache.search.xml`, `lib.gt.tradematch.xml`, `lib.gt.score.trades.xml`.
- `md/gt_tradesearch_scheduler_mk1.xml`, `md/gt_tradesearch_scheduler_mk4.xml` coordinate searches; these are *not* evidence that LMP may directly call GT's internals.

**SOURCE — VAS**
- `md/supply_needs_planner.xml` → `RunPlannerBody` resolves buy offers, supplier sell offers, quantity, and legs; `ClosestSellOffer` is a *buyer search for existing cargo*, not the main supplier-selection algorithm.
- `md/supply_needs_planner.xml` → `MergeLegsBySite`, `RouteLegsFarthestFirst` are route/queue utilities, useful as reference only.

**SOURCE — current LMP**
- `md/LMP_Sources.xml` → `LMP_FindSellOffers` uses `find_sell_offer`, `tradepartner`, `excludeempty`, `usereservations`, and player/NPC source filtering.
- `md/LMP_Orders.xml` → `LMP_CreateTradeOrder` calls `create_trade_order` but currently blocks GT default orders.

**GOAL:** Source filter player / NPC / both; nearest-to-ship or nearest-to-destination; price-versus-distance slider with **value-aware** savings; respect stock, cargo capacity, range, blacklists, money and reservations.

**GAP:** A direct MD implementation of every GT AI trade-scoring check is not established. Avoid assuming GT's cached offers or reservations can be safely reused as LMP-owned reservations.

## 5. Trade execution and completion

**SOURCE — VAS**
- `md/supply_needs_planner.xml` → `RunPlannerBody` emits `create_trade_order` for buy legs and sell legs.
- `EmitPreExistingShipSetup` can invoke `cancel_all_orders` when flush mode is requested.

**SOURCE — GT**
- `aiscripts/order.trade.perform.xml` is GT's patch of vanilla trade execution.
- `md/gt_trading_signals.xml` → `ProcessTradeSuccess`, `ProcessTradeFailure`, `ProcessTradeSuccessQueue`, `ProcessTradeFailureQueue` process GT trade outcomes and associated state/progression.

**SOURCE — LMP**
- `md/LMP_Orders.xml` → `LMP_CreateTradeOrder`.
- `md/LMP_Dispatcher.xml` → `LMP_DispatchOne`.

**GOAL:** Each ship commits **one** purchase plus delivery cycle, tracks completion, releases/updates reservation, then reevaluates demand.

**DO NOT COPY:** VAS flush mode (`cancel_all_orders`) into GT active handoff. Its default append behavior is also **not** a safe substitute for taking ownership of a GT trader.

**GAP:** VAS's planner does not expose an LMP-specific completion event. GT trade signals are useful evidence, but LMP must correlate *its own* orders with ship/job IDs; observing generic GT trade-completed signals is not enough.

## 6. GT takeover, snapshot, restoration and progression

**SOURCE — GT**
- `md/gt_ship_state_manager.xml` → `UpdateState`, `HandleAIStateUpdate`, `DetectOrderCancellation`, `DelayedVerification`.
- `md/gt_ship_state_utilities.xml` → GT order/commander status checks.
- `md/gt_trading_signals.xml` → trade-success/failure handling and progression/stat updates.
- `md/gt_fleet_coordination.xml`, `md/gt_xp_training.xml`, `md/gt_pilot_ecosystem.xml` → related fleet/progression state.
- `aiscripts/lib.gt.ship.opstate.xml` → operational state signaling.

**SOURCE — current LMP**
- `md/LMP_Takeover.xml` → `LMP_SnapshotShip` currently records ship ID, commander, home, default-order **ID**, capture time. This is **not a complete default-order settings snapshot**.
- `md/LMP_ShipRegistry.xml` → `LMP_EnrollShip` / ship ownership registry.
- `md/LMP_Recovery.xml` → `LMP_Recovery_OnLoad` reconciles registry on game load.

**GOAL:** Preserve exact original GT behavior and parameters, commander/subordinate assignment, cargo and trade restrictions, and GT pilot progression. Hold and verify before setting `LMP > ACTIVE`. Release must restore the exact original settings, not merely the default-order ID.

**GAP / highest-risk area:** A cooperative GT interception point, actual Hold semantics, complete default-order parameter capture and restoration, and GT's handling of temporary default-order replacement are not yet established by this mapping. Do **not** claim this is already implemented or safe.

**Important:** `LMP_Orders.xml` currently rejects GT default-order ships. That is a deliberate existing safety gate, not a completed takeover mechanism; the new controlled state must be explicitly recognized without simply deleting the guard.

## 7. Reservations and multi-ship dispatch

**SOURCE — GT**
- `md/glx_lib_reservations.xml` → `GLX_GenerateTradeKey`, `GLX_InitializeTradeIndex`, `GLX_AddTradeToIndex`, `GLX_RemoveTradeFromIndex`.
- GT trade-key/index logic is **not proof of a cross-mod shared reservation contract**.

**SOURCE — VAS**
- `md/supply_needs_planner.xml` → tracks planned amounts per offer during a planner run, avoiding duplicate allocation within that run.

**SOURCE — LMP**
- `md/LMP_Reservations.xml` → reservation ledger and `LMP_Reserve`.
- `md/LMP_Dispatcher.xml` → per-ship dispatch.
- `md/LMP_Demand.xml` → demand ledger.

**GOAL:** Prevent two LMP ships claiming the same outstanding demand; count in-transit cargo; release or reconcile reservations on delivery, failure, ship destruction, or save/load. Share a fleet across multiple build sites and honor relative per-site priorities without starvation.

**GAP:** Neither GT's trade index nor VAS's single-run planner substitutes for LMP's persistent multi-ship reservation ledger.

## 8. User interface and controls

**SOURCE — VAS**
- `md/supply_needs_planner_interact_menu.xml` → `Add_Interact_Actions`, `OpenStationPlanner`, `OpenBuildStoragePlanner`, `BuildPlannerMenu`, `ExecutePlanner`.
- The interaction uses SirNukes' `Interact_Menu_API.Get_Actions` and the Simple Menu API; VAS's two right-click entries are **Fulfill station needs** and **Fulfill build storage needs**.
- `md/supply_needs_planner_config_menu.xml` → configuration UI support.

**SOURCE — GT**
- `ui/gt_fleet_menu.lua`, `ui/gt_fleet_actions.lua`, `ui/gt_order_settings.lua` show GT's Lua fleet/settings approach.
- `md/gt_order_settings_ui.xml` supports GT's settings integration.

**GOAL:** Compact LMP UI: Active fleet selection and **FILL BUILD STORAGE** toggle; Passive default behavior `LMP > PASSIVE`; target/all/closest build storage; source filter; value/distance controls; relative site-priority sliders and status counts.

**Copy/adapt:** VAS's contextual targeting and compact configurable menu pattern; GT's fleet/settings UI patterns where appropriate. **Do not** clone VAS's manual run planner as LMP's scheduler.

**GAP:** UI registration and `LMP > ACTIVE/PASSIVE` default-order definitions need actual implementation; naming a behavior in an MD variable does not register it as an X4 default order.

## 9. Save/load, recovery, and diagnostics

**SOURCE — LMP**
- `md/LMP_Recovery.xml` → `LMP_Recovery_OnLoad`.
- `md/LMP_ShipRegistry.xml` → `global.$LMP_Ships`.
- `md/LMP_Reservations.xml` → `global.$LMP_Reservations`.
- `md/LMP_M0_Diagnostics.xml` → read-only GT lifecycle observation.
- `md/GUNPIRE_Config.xml` → safety gates and execution profiles.

**SOURCE — GT**
- `md/gt_ship_state_manager.xml` → delayed verification and state reconciliation.
- `md/gt_tradesearch_scheduler_mk4.xml` → `MK4ReinitShipsOnLoad` is a GT-specific save/load reference, not reusable LMP recovery code.

**GOAL:** Restore original work on OFF, finish an active delivery before release, recover stale or destroyed ships, preserve first-seen POS order ages, avoid duplicate orders after load.

**GAP:** Existing LMP recovery is not evidence that all in-flight trade/order state and snapshots are save/load-safe.

## 10. Exact current-code edit targets

| LMP file | Intended responsibility | Primary source reference |
|---|---|---|
| `md/LMP_Takeover.xml` | Active GT safe handoff; snapshot, Hold, verify, LMP ACTIVE, restore | GT ship-state manager/utilities + GT order AI |
| `md/LMP_ShipRegistry.xml` | Active/passive registration and ownership | LMP scope + GT ship state |
| `md/LMP_Demand.xml` | Build storage and aged POS buy demand | VAS `SupplyNeedWares` + GT MK4 station matching |
| `md/LMP_Sources.xml` | Find/validate sell offers; source policy | GT search/match libraries + VAS planner |
| `md/LMP_Dispatcher.xml` | Priority ranking, per-ship one-cycle dispatch, fallback | GT MK4 score/search + GT MK1 selling |
| `md/LMP_Reservations.xml` | LMP-owned inbound/in-flight quantities | GT trade index + VAS planned amounts (patterns only) |
| `md/LMP_Orders.xml` | One buy + one delivery; track outcome | VAS `RunPlannerBody` + GT trade execution |
| `md/LMP_Recovery.xml` | Release/reconcile after save/load/failure | GT state reconciliation + existing LMP registry |
| `md/GUNPIRE_Config.xml` | Feature gates, default behavior modes | Existing LMP config |
| UI **(not yet present in LMP ZIP)** | Active toggle, Passive behavior settings, site priorities | VAS menu + GT Lua fleet UI |

## 11. Source boundaries and integration rules

1. **GT AI scripts vs MD:** `aiscripts/lib.gt.*` and `md/gt_*` use different execution contexts. Do not invent cross-language direct calls.
2. **VAS manual planner vs autonomous dispatcher:** Reuse demand/offer/quantity concepts, **not** its bulk queued execution or `cancel_all_orders` path.
3. **GT progression:** GT signals/state may update XP. Do not reset GT-owned data or assume setting the same default-order ID restores its parameters.
4. **Build storage vs POS buy orders:** Distinct demand classes with explicit precedence; don't use a single unbounded score that can let ordinary selling outrank build storage.
5. **Ownership:** Active ships belong to GT except during an explicitly verified LMP handoff. Passive ships belong to LMP.
6. **Patch conflicts:** GT ships vanilla-named AI XML diff patches, including `order.trade.perform.xml`. Check `<diff>` operations and `sel` targets before adding patches to the same files. The current indexer lacks a complete `patch_ops` inventory.
7. **Compatibility:** Other installed automation mods can alter behavior, offer visibility, reservations, and travel. Source references are not in-game compatibility results.
8. **No unapproved requirement drift:** This mapping documents the original scope plus the user's explicitly clarified Active/Passive/POS priority behavior.

## 12. Explicitly unverified / do not assume

- The exact GT **pre-next-job** interception cue is identified and safe.
- GT MK3 and MK1 state can be restored by merely writing a behavior ID.
- GT MK4 trade-search libraries can be invoked directly from LMP MD.
- Aged POS order timestamps exist as stable GT fields.
- VAS completion notifications are usable as reliable LMP job completion events.
- `LMP > ACTIVE` and `LMP > PASSIVE` are already registered in the current mod.
- The supplied LMP scripts are production-ready or have passed X4 9.00 runtime testing.

**Development instruction:** Modify the existing LMP code only after tracing the named source implementation. When a source behavior is copied, record its exact original file, cue/library/script, relevant input/output assumptions, and any deviations required for LMP. Preserve GT/VAS ownership boundaries and never silently widen scope.

## Addendum — 2026-11-11: GT parity and safe dispatch corrections

**GT baseline:** Galaxy Trader 1.0.4 as supplied in the Nov 7 source snapshot; other GT snapshots may differ. Inspect actual installed copies before changing APIs/IDs.

1. **GT recognition:** GT uses `GalaxyTraderMK3` and `GalaxyTraderMK4Supply`; MK3/MK4 may also appear under `Assist` with `$baseorder`. This is visible in `aiscripts/order.trade.galaxytradermk4.xml`, near line 479. Current LMP guards previously checked obsolete/unmatched IDs, including `GalaxyTraderMK4` and `GalaxyTraderMK42`. The patch consolidates recognition into `GUNPIRE_IsGTManagedShip`.
2. **Rerank each trip:** After each *full* buy-and-deliver transaction, scan demand and source offers again using the ship's **current position**. Never carry a previous supplier ranking across trips. The current dispatcher **does not implement source ranking**; this remains unfinished.
3. **Completion boundary:** GT MK4's main loop checks `this.ship.tradeorders` and waits on `GT_Trade_Completed` / `GT_Trade_Failed` as wakeups before reassessing the order queue. Those events alone do **not** authorize another trip. GUNPIRE additionally requires `ship.tradeorders.count == 0` **and** a verified empty cargo hold before scheduling another job; incomplete/failure jobs need recovery, not an automatic retry.
4. **Existing code hazard:** `LMP_Dispatcher.xml` previously fabricated a 100-hullparts demand when no shortage was found and then queued only the **buy** leg. The initial safety patch removes the invented fallback and prevents incomplete dispatch. This means dispatch intentionally remains **disabled** pending a source-verified paired-trade and recovery implementation.
5. **Cargo eligibility:** `GUNPIRE_Core.xml` formerly returned `true` whenever a ship existed. The guard now uses GT's `ship.cargo.list` empty check, returning false on unavailable cargo data. **Queued order/commitment verification is still missing**; cargo alone does not authorize ACTIVE takeover.