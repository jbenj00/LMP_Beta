# GUNPIRE / Galaxy Trader handoff — revised design decision

**Date:** 2026-11-09  
**Decision:** A GUNPIRE-owned default behavior is necessary for exclusive GUNPIRE trade dispatch, but **not safe to assign to GT ships unconditionally in GT 1.0.4**.

## User-provided in-game evidence

- There is **no Active checkbox** to pause GT.
- Follow Ship, Fly and Wait, and Dock and Wait commands work with a GT ship.
- The player expects GT to interfere with independent trade orders while it retains control, so using ordinary orders beneath an active GT default behavior is rejected for the actual dispatcher.

## Verified source findings

1. `aiscripts/order.trade.galaxytrader.xml` near lines 2541–2569: MK3 AI sees `this.ship.tradeorders.count > 0` and waits for trade-order completion. This **does not prove** an external trade order is safe in all branches.
2. `aiscripts/order.trade.galaxytrader.xml` near lines 9093–9102: MK3 `on_abort` explicitly classifies a *different default order* as permanent removal. MK4 contains analogous code near lines 10917–10926.
3. `md/gt_ship_state_manager.xml` near lines 506–629: protected GT default-order cancellation can trigger orphan checks and `GT_Ship_Order_Aborted` cleanup.
4. `md/gt_order_monitor_bridge.xml` near lines 468–563: Lua order-change detection also emits abort after verification when a GT order has disappeared.
5. `md/gt_core_system.xml` near lines 4561–5063: GT abort cleanup touches trade tracking and GT modifications, not just XP.
6. `md/gt_core_system.xml` near lines 5066–5209: even GT's `GT_Ship_Order_Paused` handler clears/rebuilds parts of the ship registry and modifies some training/mod tracking while preserving pilot XP. It is an internal lifecycle event, **not a documented external pause API**.

## Architecture consequence

**Active ship contract:**

1. Ship remains on GT while it has existing cargo, queued orders, reservations, training or maintenance commitments.
2. When eligible, record a full original-state snapshot including GT behavior ID/parameters, commander, pilot, home/range, and restoration status.
3. Start a GUNPIRE-exclusive lease **only after a tested, cooperative GT handoff exists**. Do not change GT default order first and hope cleanup is reversible.
4. Execute GUNPIRE orders under custom GUNPIRE behavior; GT cannot concurrently schedule the ship.
5. On release, finish/resolve cargo; restore original assignment; verify that GT re-registers and all recorded settings/progression survive.
6. If no lossless handoff is available for an order variant, mark that variant **GT_UNSUPPORTED_FOR_TAKEOVER**. Do not hijack it.

**Compatibility approach to investigate in M1:** an isolated GT-aware adapter, potentially a narrowly scoped compatibility patch or upstream GT hook that suppresses permanent-removal cleanup only while a validated GUNPIRE lease is active, and defines a restoration handshake. No such hook is claimed to exist or be tested. Do not directly modify GT's global tables to fake compatibility.

**Other ship types:** GUNPIRE can support unassigned/vanilla ships through separate verified handoff paths without relaxing GT safety.

## Changed from previous design

Rejected: running GUNPIRE trade orders underneath a still-running GT default behavior, based solely on manual Fly/Wait/Dock/Wait success.

Retained: empty-cargo-only takeover, one delivery at a time, no resetting XP, no job loss, restoration on OFF, event-driven coordination and reliable save/load recovery.
