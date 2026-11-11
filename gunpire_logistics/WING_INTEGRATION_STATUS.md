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
- Around **6918**, GT emits `GT_TradeLogging_LogTradeOrder`, carrying final committed `$Amount`, `$BuyOffer`, `$SellOffer`, prices and `$IsSellOnly`. This is later than order creation and much stronger than `GT_Search_Done`.
- `md/LMP_Wing_GTCommitted.xml` **now listens for both signals** and records the commander's committed trade metadata in the wing registry, without changing trade orders or modifying GT progress. This is still observation, not a GT interception hook.
- `md/LMP_Wing_GTObserver.xml` was hardened to persist only scalar preview statistics; it no longer saves live offer references in its preview.
- **Critical**: Neither post-order event permits us to increase the commander's purchase amount retroactively. A real fleet-wide MK3 requires a *pre-commit validated handoff* into wing-level execution, with GT agreeing not to create duplicate commander orders. Read-only post-commit observers are not a substitute for that.

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
