# GUNPIRE Logistics — Integration Reference

**Source:** Three user-supplied mod archives, extracted without modifying source. **Game target:** X4: Foundations 9.00. **Inspection:** static source review; no in-game execution or runtime validation.

## Confirmed installed-package identity

| Package | `content.xml` ID | Version metadata | Integration role |
|---|---|---|---|
| GalaxyTrader MK3 | `GalaxyTraderMK3` | `10004`, dated 2026-11-07 (download labeled 1.0.4) | Third-party trader behavior, progression, fleet UI |
| Kuertee UI Extensions and HUD | `kuerteeUIExtensionsAndHUD` | `900` | UI extension host |
| SirNukes Mod Support APIs | `ws_2042901274` | `195` | Shared API bundle |

Galaxy Trader's `content.xml` explicitly declares both UI Extensions and SirNukes as **non-optional** dependencies, plus X4 9.00 (`version=900`). Optional Boron/Split/Terran DLC dependencies are also declared. Its `save=0` is package metadata, **not evidence that its persistent state is absent**.

## Critical implementation implications

1. **Ship takeover must not be implemented as a blind order clear.** GT observes order cancellation, commander changes, subordinate removal and other ship-state events. Those may trigger cleanup/reconciliation.
2. **XP is pilot-associated.** `global.$GT_Pilots` with `$XP`, `$Level`, and `$Ship` occurs in `gt_xp_training.xml`. This is promising, but preservation of these fields alone does not guarantee restored GT operation.
3. **GT maintains ship-level and global runtime state.** `global.$GT_Ships` is used widely. Avoid changing its internal tables directly unless the exact lifecycle is understood.
4. **GT has its own reservations.** `glx_lib_reservations.xml` contains reserve/release/check/cleanup libraries. GUNPIRE must have a separate inbound-demand ledger and must not assume GT reservations are safe to reuse or mutate.
5. **Existing GT UI uses Lua and MD bridges.** Prefer an independent GUNPIRE menu or carefully registered extension over editing GT's source files.
6. **SirNukes API implementation is packed in CAT/DAT.** The archive includes documentation, but not unpacked Lua source for all APIs. Do not claim API signatures are verified from the package alone.
7. **Kuertee UI contains packed `subst_01.cat/dat` assets.** Only loose XML/readme/Lua assets can be audited without unpacking its catalog.

## Confirmed GUNPIRE behavior constraints

- ON: ship with trade cargo > 0 keeps existing task until cargo is empty; then snapshot behavior/order/commander state and take over.
- Empty ship: snapshot and take over immediately.
- One dynamic purchase→build-storage delivery at a time; reevaluate demand and reservations after each delivery.
- OFF: complete current GUNPIRE delivery, release reservation, restore previous assignment and GT automation.
- GT XP, level, pilot association, trader settings and fleet membership must survive.
- Save/load, destroyed ships, failed trade, changed commander, and manual player intervention require explicit recovery behavior.

## Integration decisions to verify before coding

| Question | Required experiment |
|---|---|
| Can a GT ship be safely paused? | On a **copy of a save**, snapshot ship, clear its default order, observe GT state and log/events. |
| What constitutes an empty hold? | Test ship cargo ware quantities separately from inventory/equipment; include reserved and queued transfers. |
| Is GT progression preserved? | Compare pilot XP/level, ship association, and GT settings before/after takeover and restoration. |
| What happens on commander removal? | Test standalone trader and fleet subordinate separately. |
| Can we restore exact previous job? | Test every GT order variant used in the save, including any persistent parameters. |
| Can GT autonomously reclaim a borrowed ship? | Inspect event listeners and run an in-game takeover test while GT scheduling is active. |
| Does OFF leave cargo behind? | Test during purchase, travel, docking, transfer and cancellation windows. |
| Can UI integrations coexist? | Test with both required support mods, without overwriting another mod's files. |

## Priority source map

| Priority | Source | Why inspect |
|---|---|---|
| P0 | `md/gt_ship_state_manager.xml` | Ship-state updates, order cancellation, commander changes, subordinate removal |
| P0 | `md/gt_ship_state_utilities.xml` | Status libraries and GT-controlled checks |
| P0 | `md/gt_ship_management.xml` | GT ship enrollment, naming, management |
| P0 | `md/gt_xp_training.xml` | Pilot XP, level, academy and recovery |
| P0 | `md/gt_trading_ai.xml` | Trading AI lifecycle and signals |
| P0 | `aiscripts/order.trade.galaxytrader.xml` and MK variants | Default orders and trader parameters |
| P1 | `md/gt_trading_execution.xml` | Trade execution coordination |
| P1 | `md/gt_buy_tracking.xml` | Purchase tracking and related state |
| P1 | `md/glx_lib_reservations.xml` | GT trade reservation logic |
| P1 | `md/gt_fleet_data.xml`, `md/gt_fleet_actions.xml` | Fleet membership and fleet actions |
| P1 | `ui/gt_fleet_menu.lua`, `ui/gt_fleet_menu_adapter.lua` | UI integration patterns |
| P1 | `md/gt_order_monitor_bridge.xml` | Lua/MD order-monitor bridge |
| P2 | `md/gt_tradesearch_scheduler*.xml` | Trade scheduling and caching |
| P2 | `md/gt_ship_performance_system.xml` | Ship performance/commander-related events |

## Source evidence excerpts

### XP and recovery
- `source/galaxy_trader/md/gt_xp_training.xml` L9: `<event_game_loaded/>`
- `source/galaxy_trader/md/gt_xp_training.xml` L56: `<cue name="RecoverAcademyEnrollmentsOnLoad" instantiate="true" version="1">`
- `source/galaxy_trader/md/gt_xp_training.xml` L58: `<event_game_loaded/>`
- `source/galaxy_trader/md/gt_xp_training.xml` L68: `<do_if value="global.$GT_Pilots.{$xcpilot}.$XP? and global.$GT_Pilots.{$xcpilot}.$XP gt $xpLevelCap">`
- `source/galaxy_trader/md/gt_xp_training.xml` L69: `<set_value name="$xcLevel" exact="if global.$GT_Pilots.{$xcpilot}.$Level? then global.$GT_Pilots.{$xcpilot}.$Level else 15"/>`
- `source/galaxy_trader/md/gt_xp_training.xml` L71: `<set_value name="global.$GT_Pilots.{$xcpilot}.$XP" exact="$xpLevelCap"/>`
- `source/galaxy_trader/md/gt_xp_training.xml` L72: `<set_value name="global.$GT_Pilots.{$xcpilot}.$Level" exact="15"/>`

### Order / commander state hooks
- `source/galaxy_trader/md/gt_ship_state_manager.xml` L506: `<cue name="DetectOrderCancellation" instantiate="true">`
- `source/galaxy_trader/md/gt_ship_state_manager.xml` L508: `<event_object_order_cancelled object="player.galaxy"/>`
- `source/galaxy_trader/md/gt_ship_state_manager.xml` L519: `<debug_text text="'[GT-State] Phase 7: DetectOrderCancellation triggered - GT order cancelled for ship: ' + $ship.idcode" chance="100"/>`
- `source/galaxy_trader/md/gt_ship_state_manager.xml` L636: `<event_object_subordinate_removed object="player.galaxy"/>`
- `source/galaxy_trader/md/gt_ship_state_manager.xml` L726: `<cue name="DetectCommanderRemoval" instantiate="true">`
- `source/galaxy_trader/md/gt_ship_state_manager.xml` L728: `<event_object_commander_set object="player.galaxy"/>`
- `source/galaxy_trader/md/gt_ship_state_manager.xml` L737: `<debug_text text="'[GT-State] Phase 7: DetectCommanderRemoval triggered - Commander changed for ship: ' + $ship.idcode" chance="100"/>`
- `source/galaxy_trader/md/gt_ship_state_manager.xml` L870: `<debug_text text="'[GT-State] Phase 7: ' + $ship.idcode + ' - Assist/no-commander transition detected in DetectCommanderRemoval, deferring orphan verification'" chance="100"/>`

### GT ship state helper libraries
- `GT_CheckCommanderStatus`
- `GT_IsSubordinateOfGTCommander`
- `GT_GetShipState`
- `GT_RequestShipNameRefresh`
- `GT_RestoreShipName`
- `GT_CheckGTOrderStatus`
- `GT_CheckPilotExchangeStatus`
- `GT_ReconcilePilotExchangeState`
- `GT_ShouldTriggerCleanup`
- `GT_IsGTControlled`
- `GT_IsShipInMaintenance`

### GT reservation library names
- `GLX_GenerateTradeKey`
- `GLX_InitializeTradeIndex`
- `GLX_AddTradeToIndex`
- `GLX_RemoveTradeFromIndex`
- `GLX_GetTradeIndexHomes`
- `GLX_GetFailureReason`
- `GLX_ReserveTrade`
- `GLX_ReleaseTrade`
- `GLX_IsTradeReserved`
- `GLX_CleanupExpiredReservations`
- `GLX_CleanupOrphanedCreditsDueAndReservations`

### Trade AI lifecycle cues
- `SystemInitV3`
- `WakeUpShipsStuckInOldCode`
- `HandleAITradeFailure`
- `ProcessDelayedTradeRequest`
- `HandleAISellRequest`
- `HandleAIStarted`

## Implementation guardrails

- Prefer **cooperative release** if GT provides one; otherwise validate a snapshot/restore protocol under real game conditions before production use.
- Never patch GT's `global.$GT_Pilots` or `global.$GT_Ships` without a verified contract.
- Don't infer that a function named `GT_IsGTControlled` is externally callable; inspect its cue/library signature and invocation context.
- Reserve by destination+ware+quantity and reconcile on trade completion, failure, ship loss and save/load.
- Treat priorities as relative weights; ensure fairness to other builds.
- Do not ship a UI mockup as proof that the underlying X4 scripting works.
- **No direct conflict is proven** merely because these mods share events or menus.

## Limits of this audit

This pack preserves all loose source files from the uploaded ZIPs, and lists packed catalogs unchanged. No CAT/DAT unpacker or game engine was used. Therefore it is a **static integration reference**, not an API certification or compatibility test. The three archives are the only sources inspected here; other Rebirth(ed) mods remain outside this audit.
