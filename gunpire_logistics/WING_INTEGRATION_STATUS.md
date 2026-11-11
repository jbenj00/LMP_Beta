# LMP-Wing — integration status (2026-11-11)

## Selected implementation
- **One GT MK3 commander, multiple cargo-carrying subordinates.** MK3 remains the trading intelligence. Do **not** replace GT's strategy/XP/parameters with a homemade search engine.
- **Native X4 commander/subordinate topology** is authoritative for wing membership.
- **Fleet Doctrine 2.14.1 remains optional.** Its README says it automatically controls formations in fleets with subordinates, and warns against overlapping escort AI changes. GUNPIRE must not copy, install, depend on, or compete with its movement orders. Fleet Doctrine, when installed and enabled for a fleet, may handle formation travel and defensive behavior; without it, X4 native behavior applies. This integration has **not** been runtime-tested.
- **Pack travel is the default.** Unlike the earlier split-and-reconvene proposal, do not dispatch wing members to far-apart suppliers independently. A common trade itinerary, with individual docking/loading and prompt deliveries, remains the intended behavior.
- **No independent MK3 default orders on subordinates.** Members should not start competing trader searches; a single commander owns the decision. Existing GT assignment and progression must never be destroyed merely by enrolling a wing.

## Implemented on this branch
- `md/LMP_Wing.xml`: opt-in logical registry for an already existing MK3 commander; calculates **direct** subordinate pool, physical container+universal capacity, free capacity, eligible vs skipped ships. Save-persistent global registration. **Does not modify orders.**
- `md/LMP_Wing_Planner.xml`: pure per-ship cargo-volume allocator. Accepts ware/quantity demand, splits quantities between ships and across multiple wares, and returns unallocated demand. **Does not place purchase orders.**
- Both modules are intentionally non-invasive; do not imply that a working convoy trader is shipped.

## Additional integration commits (November 11)
- `md/LMP_Wing_TradeAdapter.xml`: read-only adapter for GT MK3 trade candidate table `$Ware/$BuyOffer/$SellOffer/$Amount/$IsSellOnly`. Distributes **buy+sell candidate** volume among eligible wing members and returns overflow. Ware-specific compatibility uses GT's `$ware.waretransport` and `$ship.cargo.{$ware}.max`. Intentionally rejects sell-only trades until per-ship existing cargo can be accounted.
- `md/LMP_Wing_GTObserver.xml`: listens for the **existing GT emitted signal** `GT_Search_Done` on `player.galaxy` and stores a candidate allocation preview for registered MK3 commanders. This is **not** a confirmed sale or MK3 validation-approved trade. No order interception is attempted.
- `md/LMP_Wing_Commands.xml`: explicit register and unregister signals for future UI integration; changes registry only and never touches ship orders.
- **No automatic wing activation or trading is active.** To connect a UI control, signal `LMP_Wing_Register` on player.galaxy with the MK3 ship as param2, or `LMP_Wing_Unregister`. These commands themselves are not yet exposed to players in a validated UI.

## Post-validation handoff findings (November 11)
- GT 1.0.4 `aiscripts/order.trade.galaxytrader.xml` roughly lines **6300-6403** revalidates live sell/buy offers, trade blacklists and route legality immediately before trade order creation.
- Roughly lines **6552-6570**, GT calls `create_trade_order` for sell and buy legs (using `immediate=\"true\"`, `internal=\"...\"`). **GT owns these orders**, not GUNPIRE.
- Around **6697**, GT emits `GT_Ship_State_Update` with `$UpdateType = 'Trade_Order_Created'` and `$TradeOrderCount`; this is a reliable *source-level* post-order observation point.
- Around **6918**, **when GT logbook entries are enabled**, GT emits `GT_TradeLogging_LogTradeOrder`, carrying final committed `$Amount`, `$BuyOffer`, `$SellOffer`, prices and `$IsSellOnly`. This is later than order creation and much stronger than `GT_Search_Done`.
- `md/LMP_Wing_GTCommitted.xml` **now listens for both signals** and records the commander's committed trade metadata in the wing registry, without changing trade orders or modifying GT progress. This is still observation, not a GT interception hook.
- `md/LMP_Wing_GTObserver.xml` was hardened to persist only scalar preview statistics; it no longer saves live offer references in its preview.
- **Critical**: Neither post-order event permits us to increase the commander's purchase amount retroactively. A real fleet-wide MK3 requires a *pre-commit validated handoff* into wing-level execution, with GT agreeing not to create duplicate commander orders. Read-only post-commit observers are not a substitute for that.

## Current development pass
- Fixed `LMP_Wing_Planner.xml` to track container, solid, liquid, and **one shared universal free-space pool** per ship across multiple wares. Prevents earlier overcommit when a universal hold was counted independently for different transport classes.
- Added `md/LMP_Wing_OfferValidation.xml`: read-only quote revalidation against each subordinate's live `find_sell_offer` and `find_buy_offer` (using that member as `tradepartner`). These quotes **cannot be executed blindly**: shared stock across multiple offers can be overbooked and GT credit/route/price checks remain authoritative.
- GT's `GT_TradeLogging_LogTradeOrder` is **conditional on GT logbook entries being enabled** (verified in `order.trade.galaxytrader.xml` near line 6855). The unconditional `GT_Ship_State_Update` event remains the primary post-order marker; only the optional logging event contains offer and price details.
- `md/LMP_Wing_GTCommitted.xml` now computes a per-subordinate quote preview from the optional GT committed trade metadata and stores scalar units/ship counts. The quoted additional capacity excludes the commander's already-committed hold; **no subordinate orders are created**.
- Added `tools/check_wing_static.py`: parse/consistency/non-mutating-action checks for wing modules. Does not substitute for X4 9.00 schema validation or runtime tests.

## Current handoff and validation changes
- Audited GT 1.0.4 MK3's final commit sequence: its own validation covers offer availability, blacklist/routing restrictions, player funds and then immediately creates `SELL` and `BUY` trade orders (roughly lines 6300–6570). Existing post-order signals cannot replace this with a fleet-level trade after the fact.
- Corrected `LMP_Wing_OfferValidation.xml`: candidate quotes from multiple ships now consume a **shared** seller and buyer quantity budget, rather than counting one station's available ware repeatedly. This remains a conservative quote, **not an atomic reservation**.
- Added `.github/workflows/wing-validation.yml`: Python XML parse/non-mutating checks plus strict X4 `md.xsd` validation. The workflow has been pushed and run queued/in progress; do not claim it passes until GitHub reports success.
- **Execution remains gated.** The safe integration is a synchronous adapter inserted within GT's pre-commit AI sequence, subject to full GT source compatibility, and a consistent way for MK3 to delegate the trade without also creating its normal orders.

## New executable bridge — EXPERIMENTAL (November 11)

- `aiscripts/order.trade.galaxytrader.xml`: a **single XPath `<add>` patch** after GT MK3's own validated BUY order creation. Exact selector matches **one** node in the supplied Galaxy Trader 1.0.4 `order.trade.galaxytrader.xml`; source SHA-256 `b897eac4a126f02ebd23b412b6375a2499c637d995ea62fedc2607ba6d381540`. This is source inspection, **not an in-game loader test**.
- `md/LMP_Wing_Jobs.xml` now remembers each ship under its original commander's `$pendingMembers` ledger. `lib.lmp.wing.busy` checks those originally assigned ships even if a trade order temporarily removes their native subordinate relationship; a detached ship with cargo or outstanding trade orders continues to hold the wing's next-search gate. Missing/destroyed ships are not refunded or silently recreated.
- `aiscripts/lib.lmp.wing.busy.xml` plus a **second one-node GT patch** after `main_loop`: hold MK3's next search until tracked wing members have **no trade orders and no cargo**. Recheck at 10-second intervals only while a wing job is outstanding, not continuous fleet polling. The user can disable wing trading to allow GT to resume without cancelling member cargo or orders. Verified selector matches one GT v1.0.4 `main_loop` label in uploaded source.
- Per-member execution now also applies the MK3 pilot's `$searchMinROI` and global `$searchMinAbsoluteProfit` thresholds against each member's current live prices, matching the conditions in `lib.gt.tradematch`. Its shared budget reserves the commander's already-queued purchase cost before allocating additional orders.
- `aiscripts/lib.lmp.wing.extend.xml`: only runs when BOTH the global gate and the commander's individual execution gate are enabled. It retains GT's original commander trade, then requests **additional same-ware purchases and deliveries for direct subordinates**, using per-member live buyer/seller offers, compatible cargo free volume, one shared wallet budget, and GT's own account selector. It skips illegal wares and ships with cargo or existing trade orders. It excludes GT-managed subordinates (including Assist baseorders).
- For an `additionalTarget=0` request, the helper derives the maximum potential extra units from eligible wing cargo and clamps actual assignments to live buyer/seller offers and funds. This is a FIRST-PASS companion-trade extension; **GT still selected the original route/opportunity using commander-sized logic**, so this is not yet full fleet-aware MK3 scoring/search.
- `md/LMP_Wing_Menu.xml`: SirNukes/GT-style right-click menu on an MK3 commander: register wing, inspect capacity, explicitly enable experimental companion trading, and disable it. Register alone remains **read-only**. Disabling never removes existing orders.
- `md/LMP_Wing_Jobs.xml`: saves event-driven records of subordinate orders requested by the helper. Menu snapshot reports ships with queued trade orders, cargo remaining, and empty holds without polling. These records do **not** prove completion or profit.
- `tools/check_gt_wing_patch.py` and GitHub Actions validate AI schema, patch structure, and safety guard. Developer can run with a path to original GT `order.trade.galaxytrader.xml` to require exactly one XPath match. A prior checker bug (XML comments counted as operations) was fixed.
- Fleet Doctrine 2.14.1 README says Escort maps to native Defence assignment. Wing membership eligibility now admits Defence escorts and other direct subordinate assignments, but excludes independent GT default orders.
- **Do not claim an operational formation convoy:** ships may break formation when native trade orders execute. Fleet Doctrine compatibility and native escort return behavior need in-game testing; do not force formation follow orders over active trade orders. Exact target version is GT 1.0.4, 2026-11-07.
- **Safe activation for testing:** registration is possible; execution is OFF by default. Enable only in a disposable X4 save with GT 1.0.4 installed and Fleet Doctrine on/off comparison. If anything breaks, disable the wing before saving. This does not cancel already issued trade orders.

## Latest safety corrections
- The executable `lib.lmp.wing.extend.xml` now maintains one shared seller-availability and buyer-demand budget across all subordinate orders, conservatively subtracting the MK3 commander's committed quantity and every new assignment. This prevents a fleet of four ships from each reserving the same physical stock. The deduction may be conservative if X4 has already reduced the offer amount after the commander's order; runtime testing must confirm timing.
- `lib.lmp.wing.busy.xml` now **fails closed** when an originally assigned ship is missing or destroyed. The wing cannot silently count missing cargo as delivered and launch another GT job. An explicit wing disable is the manual recovery path until loss/reconciliation handling exists.
- These changes are to the **experimental, opt-in execution path**, not to vanilla GT MK3 behavior. No formation guarantees or completed in-game tests.

## Remaining operational work
1. Validate actual game's **two GT patch targets**, MK3 trade continuation, subordinate order execution, trader XP and escort behavior, with Fleet Doctrine enabled and disabled.
2. Add coherent convoy staging / synchronized multi-stop routing without overriding active trade orders or writing a parallel GT search engine.
3. Convert GT's original trade search and scoring to evaluate the actual **combined eligible wing capacity** prior to selection; the current extension only expands an MK3-selected trade after commander commit.
4. Add robust per-member cancellation/failure recovery, short fills, supplier exhaustion and reservation convergence across simultaneous orders. The current ledger tracks order requests and remaining cargo, but does not yet reconcile confirmed actual deliveries or GT profit records.
5. Support automatic subordinate enrollment and persistent F1-Pn names without fighting GT auto-naming.
6. Validate both XML schemas and in-game behavior for all changed files; CI success alone cannot test gameplay.

## Verified source evidence
- Galaxy Trader 1.0.4 `aiscripts/order.trade.galaxytrader.xml`: order id `GalaxyTraderMK3`; the MK3 main trade loop calculates utilization against `this.ship.cargo.capacity.all` (around line 5762). A fleet-capacity-aware **GT adapter** must be introduced at the correct planning points, not just one substitute variable.
- Galaxy Trader 1.0.4 `md/gt_core_system.xml`: `RunCommanderGTReactivationPass` (around line 563) explicitly handles `allsubordinates`, `commander`, and `Assist` base orders. It is unsafe to overwrite them with a second AI.
- Galaxy Trader 1.0.4 `md/gt_home_fleet_profile.xml`: uses `cargo.capacity.container + cargo.capacity.universal` for volume accounting (around line 181). `md/gt_context_diagnose.xml` also uses free container+universal volume (around line 4099).
- Fleet Doctrine README: escort/follow/formation and coordinated gate movement are native to that extension; ships with subordinates are automatically managed unless the user turns the doctrine off.

## Still required before use as a live MK3 convoy
1. GT's validation and order-creation section is now located (roughly lines 6300-6697). Implement a **coordinated pre-order creation adapter or compatible GT patch**, not an after-the-fact order duplicator. Keep all original GT validation rules, money checks and progression.
2. Map an MK3 result into per-member orders with a shared transaction ID, volume-aware quantity distribution, and atomic reservations. Respect ware class, per-ship order queues, prices, money, and intermediate stops.
3. Resolve Fleet Doctrine/native movement vs `create_trade_order`/docking. The safety rule is that an active leg cannot be replaced with formation follow orders.
4. Define a safe wing assignment UI / ship naming path without replacing another mod's orders or GT progression; only then expose `LMP-Wing` enrollment.
5. Handle partial fills, member losses, pirate interruptions, save/reload, regrouping and failed buy/delivery before enabling commerce.
6. Validate each new XML file against the extracted X4 9.00 XSDs and then test in a throwaway save, both with Fleet Doctrine enabled and disabled. XML parsing and in-game tests have **not yet been performed**.

## Unresolved design choice
The user's **latest** preference is four armed M-class trader ships **staying together**, rather than sending each to independent suppliers. Keep that as the default even if splitting could lower route duration.

## Compatibility / safety invariants
- GT MK3 source is not vendored or rewritten in this branch.
- GT dispatcher/experience and existing ship assignments remain untouched.
- No combat AI clone; no direct Fleet Doctrine script calls.
- No fleet member may be commanded while it has an unrelated job, or when role/ownership is uncertain.
- The planning modules are **non-executing groundwork**, not a completed feature.
