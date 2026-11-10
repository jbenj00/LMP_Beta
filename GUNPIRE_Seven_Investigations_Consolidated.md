# GUNPIRE Logistics — Consolidated Source Investigations (01–07)

**Date:** 2026-11-10  
**Game target:** X4: Foundations 9.00 / heavily modded Rebirth(ed) installation  
**Deliverable:** One consolidated Markdown research dump, not a mod build  
**Evidence level:** Static source analysis. **No in-game validation has been performed.**  
**Status:** Seven technical areas reviewed; unresolved interfaces and runtime acceptance tests explicitly preserved.

## Source integrity and scope

This report uses the following supplied artifacts:

- `GUNPIRE_Source_Investigation.zip`, especially `GUNPIRE_Source_Investigation/source/x4_unpacked/` (vanilla extracted script/schema/source files), `source/installed_galaxy_trader/`, `project_snapshot/gunpire_logistics/`, and `RECOVERY_STATUS.md`.
- `GUNPIRE_Collected_Research_Evidence.zip` (overlapping recovered source evidence, not a separate successful investigation).
- `GUNPIRE_Full_Project.zip`, `refs/GUNPIRE_Logistics_Mod_Project_Scope.md`, and `refs/GUNPIRE_Logistics_Implementation_Roadmap.md` for requirements and acceptance criteria.
- `01_GUNPIRE_Integration_Reference.md`, `02_UI_and_Support_APIs.md`, `03_Extracted_Source_Index.md` and `X4_Scripting_Reference.html`.
- `GUNPIRE_Investigation_01_GT_Takeover_Restoration.md` (previous investigation; its conclusions are incorporated here).

**Important provenance limitation:** The recovery archive says seven previous reports were lost, but does not reproduce their original seven titles. The seven sections below are therefore organized around seven *critical technical investigations demanded by the project scope*, rather than falsely claiming to reconstruct the original missing reports. The recovered `project_snapshot` is a snapshot, **not necessarily the latest working tree**. The installed-GT source in the recovery archive reports **1.0.3**, while the independently provided package reference reports **1.0.4**. Differences need a file-level comparison against the currently deployed 1.0.4 package.

**Evidence notation:** Paths beginning `vanilla/` mean `source/x4_unpacked/`. Paths beginning `GT/` mean `source/installed_galaxy_trader/`. Paths beginning `GUNPIRE/` mean `project_snapshot/gunpire_logistics/`. Line locations are indicative for the recovered versions, not promises about later revisions. A schema declaration establishes syntax/metadata, not successful game behavior.

---

# Investigation 01 — Galaxy Trader safe temporary takeover, restoration, and progression

## Objective

Establish whether an existing GT trader (standalone or subordinate) can be borrowed, used for construction deliveries, and restored with its **exact** prior order, parameters, fleet association and pilot progression.

## Verified evidence

1. `GT/md/gt_core_system.xml` defines protected order IDs `GalaxyTraderMK3`, `GalaxyTraderMK4Supply`, `GalaxyTraderMK4Supply2`, `GalaxyTraderMK2`, `GalaxyTraderMK1`, `GalaxyMiner`, `GalaxyExplorer` (around lines 90 and 133).
2. `GT/md/gt_ship_state_manager.xml` monitors `event_object_order_cancelled` and assesses cancelled protected GT orders (around 506–627). If no direct order or GT commander remains, it can mark the ship **orphaned**, clear active-trade count and signal GT orphan/abort handling.
3. The same manager monitors `event_object_subordinate_removed` (around 634–713) and `event_object_commander_set` (around 726–795). Subsequent delayed checks can result in cleanup (around 900–980).
4. `GT/md/gt_core_system.xml` handles `GT_Ship_Order_Aborted` (around 4400–4459) and calls trade-search abort and state reconciliation. Cancelling an order is **not** demonstrably a harmless pause.
5. `GT/md/gt_ship_state_utilities.xml` exposes `GT_CheckGTOrderStatus` and related indicators such as direct GT order, GT commander, registry linkage, pilot registry linkage and cleanup condition (around 214–238). These are status and housekeeping facilities, **not a verified public pause/resume API**.
6. `GT/aiscripts/order.trade.galaxytrader.xml` declares the `GalaxyTraderMK3` behavior with many configurable parameters: home, max buy/sell, restrictions, blacklists/whitelists, ware selection and other trader settings (opening order definition). An order ID is an insufficient restoration snapshot.
7. `GT/md/gt_xp_training.xml` and `GT/md/gt_ship_management.xml` reference `global.$GT_Pilots` XP, level and ship association. This is pilot-associated state; merely leaving these values alone does not prove operational restoration.
8. In `GUNPIRE/md/LMP_Takeover.xml`, snapshot and request paths are currently hard-blocked and ultimately return `false`, preventing this prototype from claiming safe takeover. `GUNPIRE/md/LMP_Dispatcher.xml` also contains a GT block, but incorrectly names `GalaxyTraderMK4` and `GalaxyTraderMK42` instead of the protected `GalaxyTraderMK4Supply` and `GalaxyTraderMK4Supply2` IDs. **This is a classification defect to fix before enabling control**, although the surrounding hard gates are protective.

## Conclusion

**No safe cooperative GT release/resume contract was verified. GT takeover must remain disabled.** This is not proof the technique is impossible; it is proof that the current source review cannot certify it.

## Implementation implications

- Gate on user enrollment, ownership, valid ship, **zero trade cargo**, zero queued/active trade commitments, zero unresolved reservations and a complete persistent restoration snapshot. Empty cargo **alone** is insufficient.
- Record original order ID **and all parameters**, pilot identity, GT-associated role, commander/subordinate relationships, assignment, home/range, queued orders, outstanding trade state and release state.
- Avoid direct writes to GT's private `global.$GT_Pilots`/`global.$GT_Ships` tables as a substitute for supported restoration.
- On incomplete or uncertain restoration, stop and flag `RESTORE_REQUIRED`. Never silently drop the ship into Hold Position.
- Correct GT order-ID recognition in **all** GUNPIRE safety and dispatch paths. Compare actual installed GT 1.0.4 implementation before claiming coverage.

## Required test

On a **copy of the save**, baseline an idle/empty standalone GT MK3 ship (pilot XP/level, settings, orders, commander, cargo). Temporarily replace its behavior, observe GT orphan/abort logs, restore all order parameters, verify GT autonomously resumes **an actual trade**, then save/reload. Repeat separately for GT subordinate and MK1/MK2/MK4 variants. No production GT borrowing before this succeeds.

**Disposition:** Static investigation completed; **critical runtime gate open**.

---

# Investigation 02 — Vanilla trade-order execution and construction delivery

## Objective

Determine the exact supported trade-order creation mechanisms and whether GUNPIRE can schedule one purchase **followed by one deposit into construction storage** without corrupting a ship's default behavior.

## Verified evidence

1. `vanilla/libraries/common.xsd` around **23980** defines `<create_order>`. It appends an AI order to the queue by default; `default="true"` replaces the object's default order. Its `immediate`, `priority` and `override` settings affect queue semantics. **`default="false"` is not itself a guarantee that any existing automation will yield control or continue later unchanged.**
2. `vanilla/libraries/common.xsd` around **24057** defines `<create_trade_order object="..." tradeoffer="..." amount="..." ... />`. Documentation states it creates a trade deal from a trade offer, associates that deal with the order, and adds the corresponding trade order to the queue. The order ID is hard-coded by the engine action.
3. `vanilla/aiscripts/order.trade.perform.xml` has AI script name `order.trade.perform`, but its `<order>` ID is **`TradePerform`**, **not** the script filename. The required parameter is `tradedeal` of type `trade`, with additional optional `cannotdock`, `internalorder`, `debugchance` parameters. The script evaluates `$tradedeal.owner`, buyer/seller and transaction amount and handles cancellation or destroyed counterparties.
4. `vanilla/aiscripts/order.trade.single.xml` defines `SingleTrade` with `ware`, `locations`, `maxamount`, `minamount`, `pricethreshold`, `sell`, `gotrade` etc. It uses `create_trade_order` for an actual selected trade (around line 345).
5. `vanilla/aiscripts/order.trade.routine.xml` around lines **837–844** explicitly pairs sell-offer and buy-offer execution: the first order acquires wares; the second sells them to a buyer. The source comment notes that `create_trade_order` automatically adds the underlying reservation. This is a useful **working design precedent**, not proof that any arbitrary buyer is valid.
6. `GUNPIRE/md/LMP_Orders.xml` creates **one** trade order from an offer, updates the reservation and logs that purchase and destination deposit are **not confirmed**. `GUNPIRE/md/LMP_Dispatcher.xml` first checks `GUNPIRE_LifecycleReadyForExecution`, which currently blocks the unverified lifecycle. The prototype therefore does not implement an end-to-end construction delivery.

## Critical distinction

A seller's `find_sell_offer` result and a `create_trade_order` call can represent a **purchase leg**. They do **not** independently prove that GUNPIRE has a valid **build-storage buy offer**, an accepted delivery transaction, or end-to-end order sequencing. A completed purchase event is not a completed construction-supply job.

## Proposed minimal reliable execution path (not yet implemented/tested)

1. Identify an actual, player-accessible buyer **trade offer** for the target build storage and the target ware. Verify the destination is the build storage, not just the station.
2. Validate the source sell offer, destination buy offer, ware, legal access, ship cargo volume, quantity and available credit.
3. Reserve site/ware demand in GUNPIRE's own ledger **before** queueing trade orders.
4. Use the vanilla, schema-documented `create_trade_order` purchase leg and, once appropriate, the destination-side trade order. Build logic must account for automatic game trade-deal reservations and potentially two queued linked orders.
5. Match order and trade-completion events by exact order/ship/job context; confirm the **destination deposit** and released cargo rather than assuming the purchase completes the job.
6. Recalculate demand and schedule only the next bounded job after delivery confirmation.

**Unverified:** Whether two pre-queued trade deals survive every intermediate supplier/demand change; correct ordering against current default behaviors; precise build-storage buyer eligibility in the user's mod environment; full purchased/delivered amount after partial transfers.

**Disposition:** Vanilla order primitives verified; **end-to-end delivery unimplemented and untested**.

---

# Investigation 03 — Build-storage demand, stock, next-module urgency, and site selection

## Objective

Find script-visible demand and build sequence properties; determine what a live demand ledger must compute rather than inventing shortage quantities.

## Verified evidence

1. `vanilla/libraries/scriptproperties.xml` at **858–859** defines station `.buildstorage` and `.canhavebuildstorage`; around **978** defines the `buildstorage` type, including `.base` to access its parent station.
2. Around **1036** it defines buildmodule `.buildstorage`; around **1075–1091** it defines buildprocessor `.build`, `.queuedbuild`, `.currentslotresources`, `.neededslotresources` and **`.neededsequenceresources`**. The latter is documented as resources needed for the *whole sequence*; `.neededslotresources` is documented as resources needed for the *current build*.
3. `vanilla/md/rml_supplybuildstorage.xml` obtains `$TargetStorage.buildprocessor` and `$BuildProcessor.neededsequenceresources.list` (around lines 61–65). It listens for `<event_trade_completed buyer="$TargetStorage"/>` (around line 127) and later re-reads the needed sequence resources (around 240). This provides an especially relevant **vanilla implementation of construction-storage delivery monitoring**.
4. `vanilla/aiscripts/build.buildstorage.xml` handles `event_build_added` and uses build processing actions. It proves the game exposes a build workflow, but does not establish that GUNPIRE can subscribe to every possible needed-ware change without recalculation.
5. `GUNPIRE/md/LMP_Demand.xml` currently enumerates player-owned stations, identifies `.buildstorage` and creates station/storage records. It does **not** populate per-ware actual shortages from the buildprocessor. It clears/rebuilds global demand/shortage tables and returns detected storages. That is **discovery**, not complete demand modeling.
6. `GUNPIRE/md/LMP_Dispatcher.xml` reads a first entry in `global.$LMP_Shortages` only **if another subsystem has already supplied it**. It does not turn `neededsequenceresources` into normalized, capacity-limited shortage entries. Static source does not establish that any such producer is working.

## Important semantics to verify

- The word **needed** does not automatically mean “total plan minus stored cargo” or “outstanding after inbound game reservations.” `neededsequenceresources` and `neededslotresources` must be compared with actual storage and incoming trade commitments before building the shortage equation.
- Current-build resources are a possible verified **urgency signal**; they are **not** an automatic authorization to ignore other construction sites.
- `.buildstorage` can be missing, nonexistent or scheduled for deconstruction; filter these cases before dispatch.
- Player-owned stations are not the only possible configuration of a construction storage; scope's supply targets require defining eligible site ownership and build context.

## Required test

Create a two-site save: one site needs only Hull Parts, the other needs two wares; seed some cargo in build storage and one inbound trade. Log `.neededsequenceresources.list`, `.neededslotresources.list`, `.cargo` quantities and trade offers before and after a successful delivery. Confirm whether needed quantities already subtract stored and/or reserved goods. Test a paused build and changed construction plan.

**Disposition:** Discovery and demand API **verified**, shortage math and urgency semantics **not verified**.

---

# Investigation 04 — Supplier offers, permissions, prices, routing and cargo capacity

## Objective

Confirm that candidate suppliers are **real offers**, not nearby stations, and identify the validation required before a source is usable.

## Verified evidence

1. `vanilla/libraries/common.xsd` around **28283** defines `<find_sell_offer>` extending the common trade-matching schema. It supports a `tradepartner`, `buyer`, `seller`, `space`, `multiple`, `excludeempty`, `excludemissions`, `usereservations` and other inherited matching attributes. `usereservations` defaults to true according to the schema comment.
2. `vanilla/libraries/scriptproperties.xml` around **1515–1540** exposes trade-offer `owner`, `seller`, `ware`, `amount`, `desiredamount`, `unitprice`, `price`, `offeramount`, `transferredamount` and other fields.
3. **Subtle danger:** The property comment for `.offeramount` says **“Trade amount plus all the reserved amounts”**, while `.amount` is documented as **“Trade amount.”** Therefore using `$offer.offeramount` as an automatically free, purchasable amount is **not justified**. `GUNPIRE/md/LMP_Dispatcher.xml` currently clamps quantity using `$offer.offeramount`; this deserves correction only after validating actual effective availability under active reservation accounting.
4. `GUNPIRE/md/LMP_Sources.xml` uses `find_sell_offer multiple="true" tradepartner="$ship" space="player.galaxy" excludeempty="true" usereservations="true" wares="$ware"`. It filters `$off.seller.owner` against `'player'`, `'npc'` or `'both'`. It does **not** perform a full route/range/faction/price/credit score or verify destination trade acceptance.
5. `GUNPIRE/md/LMP_Dispatcher.xml` chooses `$offers.{1}` (first returned offer) and supplies no value-aware cost/distance ranking. There is no evidence that this first offer is optimal, reachable, legally tradeable or appropriate for the ship's range under all mod settings.
6. Galaxy Trader's `GT/aiscripts/lib.gt.tradematch.xml`, `lib.gt.mk4.tradematch.xml`, `lib.gt.pathfinding.xml`, and related scripts show that an installed trader employs nontrivial selection, pathfinding and policy logic. GUNPIRE should **learn from their filtering strategy**, but must not depend on GT private helper script behavior without a supported compatibility contract.

## Required selection contract

Filter by: seller stock/offer and price; player-only/NPC-only/both policy; ware transport class and cargo volume; ship physical cargo/free space; source/destination trade restrictions; player/faction relation; station accessibility and reachability; operating geography; available funds; job quantity; price-vs-distance preference. Recheck immediately before binding orders. If no valid route exists, record an actionable shortage rather than generating a ghost trade.

## Required test

Use (a) player station, (b) NPC station, (c) hostile/restricted station, (d) out-of-range seller, (e) supplier stock depleted between scan and order, and (f) two ships attempting the same limited offer. Confirm which sources `find_sell_offer` returns and which orders actually execute. Measure prices and booked quantities.

**Disposition:** Offer discovery syntax verified; **availability/route/legal execution unresolved**.

---

# Investigation 05 — Reservations, trade events, concurrency and duplicate-demand suppression

## Objective

Establish a reservation ledger that prevents over-ordering when multiple ships, vanilla trade deals and third-party trader reservations coexist.

## Verified evidence

1. `vanilla/libraries/common.xsd` around **24057** explicitly says `create_trade_order` creates a trade deal. `vanilla/aiscripts/order.trade.routine.xml` around **837–844** comments that the action **adds the reservation automatically**.
2. `vanilla/libraries/common.xsd` around **16739** defines `event_trade_cancelled`: `event.param` is the **tradeoffer**; cancellation does not promise a specific ship/order ID in `param2`. Around **16765**, `event_trade_completed` documents `param` as tradeoffer and `param2` as tradeorder. This difference matters for recovery joins.
3. `GT/md/glx_lib_reservations.xml` implements GT's own reserve/release/check/index mechanisms. GUNPIRE must not assume those internal records belong to it or can be rewritten by it.
4. `GUNPIRE/md/LMP_Reservations.xml` creates an entry keyed by job, with ship/site/ware/qty/state. It rejects duplicate **job keys** and refuses release except from `DELIVERY_CONFIRMED` or `SAFE_RECONCILIATION_COMPLETE`. This is a conservative initial guard.
5. **Missing guarantee:** A unique job key does **not** prevent two different jobs reserving the same site+ware quantity beyond remaining demand; no aggregate check across site/ware is visible in the reserve library. Nor does the reservation contain source offer, source quantity or partial transfer amounts.
6. `GUNPIRE/md/LMP_Recovery.xml` matches `event_trade_completed` to stored order and moves state to `TRADE_COMPLETED_AWAITING_DEPOSIT_CONFIRMATION`; this is safer than treating any trade completion as a delivered shipment. On `event_trade_cancelled`, it logs the unresolvable event rather than releasing commitments blindly.
7. `GUNPIRE/md/LMP_Orders.xml` marks `ORDER_CREATION_ATTEMPTED` before order creation and `RECONCILIATION_REQUIRED` for uncertainty. This improves fail-closed behavior but is **not** a complete idempotent transaction protocol.

## Defect / design gaps

- Double counting: game-visible trade commitments and GUNPIRE reservations may refer to the **same** purchase; subtracting both blindly from shortage could under-order.
- Concurrent ship allocations: per-job uniqueness is insufficient; site+ware and source+ware amounts require serialized validation or equivalent guards.
- Partial load/delivery: actual transferred quantity can differ from reserved requested quantity; ledger must record physically loaded, delivered, lost, and still committed amounts.
- Cancellation events do not independently provide all provenance; persist trade/order object identity and correlate against ship/job state.
- Reservation release must be idempotent and occur only after confirmed settlement or an explicit safe reconciliation outcome.

## Minimal transaction state proposal

`PLANNED → SITE_RESERVED → PURCHASE_ORDERED → PURCHASE_PARTIAL/LOADED → DELIVERY_ORDERED → DELIVERY_PARTIAL → DELIVERY_CONFIRMED → RELEASED`; side branches `ABORTED_RECONCILE`, `SHIP_LOST`, `SOURCE_LOST`, `DESTINATION_LOST`, `RESTORE_REQUIRED`. Store immutable job ID, ship, source, destination buildstorage, ware, intended qty, actual bought/delivered qty and exact order/trade references. This is **proposed**, not existing tested code.

## Required test

Two ships, one shortage of 100 units, offers totaling only 100 units. Trigger simultaneous dispatch and save/reload at each stage. Assert: no overbooking, no orphaned trade deals, no premature reservation release, and correct behavior on 40-unit partial purchase or destroyed ship.

**Disposition:** Schema and basic event semantics verified; **ledger safety at scale unverified**.

---

# Investigation 06 — Persistence, restoration failure and fault recovery

## Objective

Verify what the preserved project actually recovers on load, and what is required to survive saves, OFF toggles, changed commanders and disappearing objects.

## Verified evidence

1. `GUNPIRE/md/LMP_Recovery.xml` installs an `event_game_loaded` handler. For tracked ships it checks existence and marks `SHIP_MISSING_RECONCILIATION_REQUIRED` if missing, otherwise `RECOVERY_REQUIRED`; it retains job/reservation evidence rather than blindly replaying work.
2. `GUNPIRE/md/LMP_Reservations.xml` only initializes its global ledger if absent. This is evidence of *intent to preserve* global state, **not** proof of save/load correctness for every referenced object.
3. `GUNPIRE/md/LMP_Recovery.xml` handles trade completed/cancelled as noted in Investigation 05, but no complete source-driven proof was found of state reconstruction across every half-completed pickup/deposit phase.
4. `GUNPIRE/md/LMP_Takeover.xml` has no verified functioning exact snapshot/restore implementation; both code paths remain deliberately blocked. Thus no currently reliable borrowed-ship restore checkpoint can be established from this snapshot.
5. `GT/md/gt_ship_state_manager.xml` demonstrates GT's own delayed/orphan cleanup behavior, creating timing races if GUNPIRE tries to restore while GT reconciliation continues.

## Recovery invariants

- Never issue a second trade based solely on a serialized `PURCHASING` or `DELIVERING` string.
- Reconcile on load: ship still owned/existing, pilot, commander, live default order and queue, cargo quantities, deal/order state, source and destination existence, buildstorage demand, remaining inbound quantities, and GUNPIRE reservation record.
- Treat a destroyed ship differently from a destroyed offer; separately settle cargo, credited goods, and commitments.
- OFF means **stop new allocations, drain loaded jobs, then restore and verify**. OFF during no-cargo purchasing may need a distinct safe cancel pathway.
- If player manually changes an enrolled ship's orders or commander, do not overwrite the newer player intent; preserve a recovery record and report a conflict.
- Keep snapshot data until the previously assigned automation is **verified resumed**, not just after an attempted order creation.
- Backoff retries and cap scanner cadence. Persistent uncertainty should produce one actionable exception, not endless repeated work.

## Required test matrix

Save/load while idle, pending empty, snapshot captured, purchase queued, docking, partial purchase, en route loaded, delivery queued, partial delivery, just deposited, draining OFF, restoring, and `RESTORE_REQUIRED`. Repeat with ship loss, destroyed construction site, owner change and direct player intervention. Compare cargo and reservation totals before/after.

**Disposition:** Conservative recovery scaffolding exists; **complete persistence and exact restoration unproven**.

---

# Investigation 07 — UI/support integration, mod compatibility, validation and scaling

## Objective

Establish what can be integrated without overriding the installed trader, and identify package/API and performance constraints before GUI implementation.

## Verified evidence

1. `01_GUNPIRE_Integration_Reference.md` identifies the independently supplied **Galaxy Trader MK3 1.0.4** package (`GalaxyTraderMK3`, version metadata 10004), **Kuertee UI Extensions and HUD** (`kuerteeUIExtensionsAndHUD`) and **SirNukes Mod Support APIs 1.95** (`ws_2042901274`). Galaxy Trader declares the latter two as required dependencies. This independent version identity is **not** the same as the recovered installed-GT 1.0.3 source snapshot.
2. `02_UI_and_Support_APIs.md` documents SirNukes capabilities: Lua Loader, Time, Named Pipes, Hotkey, Interact Menu and Simple Menu APIs. The supplied package's principal implementations are in **packed CAT/DAT** assets; **exact Lua function signatures are not verified from this description**.
3. Kuertee's source package contains `ui/` assets as well as a `subst_01.cat/dat` packed override; because it modifies game UI, careless patches to `menu_map`, `menu_ship_configuration` or other UI modules could collide with GT and existing mods.
4. GT contains its own Lua menus/bridges, e.g. `GT/ui/gt_fleet_menu.lua`, `gt_fleet_menu_adapter.lua`, `gt_lua_player_bridge.lua`, and `GT/md/gt_order_monitor_bridge.xml`. These demonstrate **that a Lua/MD integration pattern exists**, not an endorsed shared entrypoint for third-party use.
5. Vanilla `.xsd` schemas and `X4_Scripting_Reference.html` can verify allowed XML actions/attributes and expression-property declarations. They **do not prove** runtime correctness or load-order compatibility.
6. The scope's operating UI includes enrolled ships, Active/Passive control, supply modes (all / targeted / closest), player/NPC source filters, relative per-site priority (default **50%**), cost/distance preference, status counts and actionable restoration/shortage reporting. Those features remain requirements, **not verified features in the preserved prototype**.
7. The roadmap's performance reference is **20 ships across 6 construction sites**, later to be scaled. It calls for bounded periodic reconciliation, event-driven dispatch where possible, and no unnecessary per-tick global polling.

## Recommended integration boundary

- Keep a GUNPIRE-owned, namespaced UI/MD bridge; do not modify GT registry and UI files directly.
- Start with a simple separate GUNPIRE panel before trying to insert controls into GT/Kuertee menus.
- Confirm a **specific** supported SirNukes or Kuertee callback/registration signature from unpacked current version source before writing bridge code.
- Use game events to wake eligible ships and demand refresh, plus staggered bounded reconciliation for missed/cancelled events. No frame-by-frame scanning of all stations and offers.
- Feature-flag Active/GT integration separately from dedicated Passive/vanilla ship operation; a noncritical UI failure must not leave controlled ships stranded.
- Check mod load order and scripts touched by EOC, KUDA, DeadAir, fleet trade mods, VRO and station storage modifiers **against the user's actual installed versions**; the source archive is not an exhaustive deployed mod inventory.

## XML/schema validation qualification

Source files and schema definitions were located, and the substantive trade actions/properties above checked against the extracted schema text. **A complete, passing XSD validation suite is not claimed here.** Expression types, game runtime links, dependency paths, override ordering and UI callbacks still require dedicated validation. Game tests remain mandatory.

## Required test

Run with GT 1.0.4, Kuertee, SirNukes and the user's actual enabled KUDA/EOC stack. Verify menu opens, sliders and toggles persist, ship enroll/remove works, no UI conflict occurs, and a UI failure cannot create duplicate orders. Run the 20-ship/6-site fixture; measure dispatch CPU cost, scan frequency, duplicate reservations, queue depth and log volume over sustained operation.

**Disposition:** Packages and broad integration paths identified; **exact UI API, full compatibility and performance unverified**.

---

# Consolidated blocker register

| Priority | Blocker | Evidence / impact | Next action |
|---|---|---|---|
| P0 | GT cooperative takeover/restore unverified | GT order-cancel / commander handlers may orphan or clean state | Controlled copied-save test; keep GT disabled |
| P0 | End-to-end construction delivery absent | Prototype queues a single offer; delivery deposit not constructed/confirmed | Verify buy offer at buildstorage; implement bounded two-leg lifecycle |
| P0 | Demand ledger doesn't derive shortage | `LMP_Demand` detects storages, not per-ware net needs | Inspect and reconcile buildprocessor/store/inbound quantities |
| P0 | Site+ware reservation atomicity absent | Unique job IDs do not prevent different jobs over-reserving one need | Aggregate reservation guard and idempotent settlement |
| P0 | Unsafe use of `offeramount` as free supply | Property defines amount **plus reserved** | Verify effective availability, adjust clamping |
| P0 | Two incorrect GT MK4 identifiers | Classifier misses `GalaxyTraderMK4Supply` / `GalaxyTraderMK4Supply2` | Fix in all paths before enabling control |
| P1 | GT source version divergence | Archive GT 1.0.3, package reference GT 1.0.4 | Compare deployed 1.0.4 source |
| P1 | Incomplete load/off/manual-intervention recovery | Existing cues retain state but no full reconciliation | State-by-state copy-save matrix |
| P1 | Buyer/source eligibility semantics | Offer existence not the same as legal route/executable job | Restricted station/faction/stock tests |
| P1 | UI hooks not source-verified | SirNukes implementation partly packed | Unpack installed API and inspect signatures |
| P2 | Scale/performance unknown | Fleet selection scans and retries may grow | 20/6 benchmark with bounded refresh |

# Recommended work sequence (separate from this research dump)

1. **Keep hard gates intact.** Do not enable GT takeover or claim the dispatcher works end-to-end.
2. **Build a vanilla, single dedicated-ship vertical slice**: demand → qualified supplier → purchase → construction-storage delivery → physical confirmation → reservation release.
3. Validate that slice against XSD and test a copied X4 save; then add two-ship collision handling, failure and save/load tests.
4. In parallel to later implementation (not assumed here), complete standalone GT cooperative restoration experiment and compare GT 1.0.4 source.
5. Only after proven execution/safety: Active/Passive UI, scheduling fairness, route economics, advanced priorities and fleet stress tests.

# Acceptance / truthfulness statement

**Verified:** Relevant vanilla schema declarations, vanilla order IDs and example usage, construction storage demand properties and vanilla monitoring pattern, recovered GT lifecycle listeners, and specific incomplete prototype modules.  
**Not verified:** A safe third-party trader pause API; exact GT 1.0.4 runtime behavior; trade completion to real buildstorage from GUNPIRE; atomic reservation reconciliation; full source permission/routing guarantees; live UI callback signatures; save compatibility; sustained 20-ship fleet performance.  
**Not performed:** In-game execution, live log inspection, comprehensive XSD acceptance, installed-mod conflict benchmarking, or source-code fixes.

**Bottom line:** The failed historical research deliverable has been replaced with one source-grounded consolidated report. It gives specific source contracts and concrete defects rather than pretending collected files prove a functioning mod. The main outstanding engineering issue is a safe, confirmed purchase-to-construction-delivery lifecycle; GT handoff remains a separate ship-safety blocker.
