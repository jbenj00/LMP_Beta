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

## Verified source evidence
- Galaxy Trader 1.0.4 `aiscripts/order.trade.galaxytrader.xml`: order id `GalaxyTraderMK3`; the MK3 main trade loop calculates utilization against `this.ship.cargo.capacity.all` (around line 5762). A fleet-capacity-aware **GT adapter** must be introduced at the correct planning points, not just one substitute variable.
- Galaxy Trader 1.0.4 `md/gt_core_system.xml`: `RunCommanderGTReactivationPass` (around line 563) explicitly handles `allsubordinates`, `commander`, and `Assist` base orders. It is unsafe to overwrite them with a second AI.
- Galaxy Trader 1.0.4 `md/gt_home_fleet_profile.xml`: uses `cargo.capacity.container + cargo.capacity.universal` for volume accounting (around line 181). `md/gt_context_diagnose.xml` also uses free container+universal volume (around line 4099).
- Fleet Doctrine README: escort/follow/formation and coordinated gate movement are native to that extension; ships with subordinates are automatically managed unless the user turns the doctrine off.

## Still required before use as a live MK3 convoy
1. Pinpoint **all** MK3 search, buy/sell validation, and cargo-utilization decisions that are single-hull-specific. Reuse GT logic; choose minimal compatible patch/adaptation point.
2. Map an MK3 result into per-member orders with a shared transaction ID, volume-aware quantity distribution, and atomic reservations. Respect ware class, per-ship order queues, prices, money, and intermediate stops.
3. Resolve Fleet Doctrine/native movement vs `create_trade_order`/docking. The safety rule is that an active leg cannot be replaced with formation follow orders.
4. Define a safe wing assignment UI / ship naming path without replacing another mod's orders or GT progression; only then expose `LMP-Wing` enrollment.
5. Handle partial fills, member losses, pirate interruptions, save/reload, regrouping and failed buy/delivery before enabling commerce.
6. Test in a throwaway save with both Fleet Doctrine enabled and disabled. XML parse / validation against the shipped X4 9.00 schemas has not yet been performed.

## Unresolved design choice
The user's **latest** preference is four armed M-class trader ships **staying together**, rather than sending each to independent suppliers. Keep that as the default even if splitting could lower route duration.

## Compatibility / safety invariants
- GT MK3 source is not vendored or rewritten in this branch.
- GT dispatcher/experience and existing ship assignments remain untouched.
- No combat AI clone; no direct Fleet Doctrine script calls.
- No fleet member may be commanded while it has an unrelated job, or when role/ownership is uncertain.
- The planning modules are **non-executing groundwork**, not a completed feature.
