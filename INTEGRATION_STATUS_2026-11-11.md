# GUNPIRE integrated trip increment — 2026-11-11

**Target:** X4 9.00, GT 1.0.4 Nov 7 snapshot, VAS planner.

## Delivered source changes (no in-game results claimed)
- `LMP_TradeCycle`: VAS-style paired trade orders; records both buy and delivery order references.
- `LMP_Demand`: live VAS-style build-storage buyer offers, no invented shortage volumes.
- `LMP_Sources`: live suppliers ordered by the VAS gate-distance / physical-distance technique from the ship's *current* location, excluding hostile/unreachable/blacklisted sources.
- `LMP_Dispatcher`: only explicitly enrolled `PASSIVE` ships, empty trade cargo and queue, all candidate build-storage shortages considered, reservations subtracted, capacity capped, paired orders queued, matching order references stored. Does not borrow GT ships.
- `LMP_Recovery`: purchase event only moves to `DELIVERING`; requires a matching delivery event, empty hold and cleared trade queue before releasing reservation and redispatching. Saves with ambiguous in-flight state stay quarantined instead of being silently reset. One-second completion cue delay allows engine order-queue state to settle.
- `LMP_ShipRegistry`: explicit `LMP_StartPassiveShip` / `LMP_StopPassiveShip` library entrypoints; stop honors active delivery.
- Cross-MD `run_actions` calls qualified as `md.Script.Library`.

## Validation
- XML well-formedness checked in the source archive generation.
- Cross-file library references statically checked in the source archive.
- No X4 runtime testing performed and no full X4 MD XSD validation completed.

## Not yet operational
- No player-facing UI, passive behavior registration, or ordinary in-game way to invoke the `LMP_StartPassiveShip` entrypoint.
- No safe ACTIVE GT borrowing or complete trader-settings snapshot restoration.
- No aged POS demand, GT MK1 selling fallback, priority sliders, value-aware source pricing, or manual recovery UI.
- Half-queued orders and ambiguous delivery states are quarantined and require reconciliation.
- Passive ships may need a valid trade-order-processing default behavior to execute queued trades.
- No in-game compatibility claims.

**This is a source-code increment, not a complete production mod.**

## Continuation: player control and persistent PASSIVE order

- Added `LMP_ContextMenu.xml`: SirNukes/GT-style right-click Start and Stop Passive Logistics actions for a selected player-owned non-GT ship.
- Added `aiscripts/order.lmp.passive.xml`: native `LMP_Passive` default order and event-driven idle demand retry every 90 seconds.
- `LMP_StartPassiveShip` now requires the ship to be idle and cargo-empty before it assigns the passive default order; enrollment is valid even with no immediately available trip.
- Expanded GT ownership protection to the actual 1.0.4 protected order IDs, including MK1 and Assist base orders.
- Static XML parsing and cross-script call resolution passed locally. X4 schema compilation timed out; runtime and in-game behavior remain untested.

This is a substantial integration increment, but ACTIVE trader handoff, station-demand aging, MK1-style fallback, full recovery and richer UI are not implemented yet.

## Further continuation: aged player-station demand

- Added `md/LMP_StationDemand.xml`, deriving buyer discovery from GT MK4 player-station logic and buy-offer filtering from VAS.
- Records the first time each player-owned station/ware buy need is seen and retains it across saves; sorts older needs first.
- Dispatcher now tries all build-storage needs before aged POS buy orders and reuses the same sourcing, quantity, reservation and paired delivery path.
- Does not yet expire stale age entries or provide GT MK1-style fallback selling.

No in-game execution or compatibility result is claimed.

## Current approved LMP operating model (supersedes earlier ACTIVE plans)

- **LMP-owned ships only.** Ships are explicitly assigned to LMP; no borrowing existing Galaxy Trader ships.
- **PASSIVE:** dedicated construction gap-filler traders, with reservations, completed-trip reconciliation and safe stop.
- **MK3 Wing:** LMP-managed Universal Trader wing with a commander and coordinated subordinate cargo. Home system/home station preferences and familiar GT-style trading toggles are required.
- **GT pilot progression:** pilot-bound XP/level remains in the existing GT data; LMP must not reset or overwrite it.
- **GT takeover is removed from scope.** Legacy ACTIVE takeover logic stays disabled and new ACTIVE enrollment is rejected.
- **Implementation gap:** the existing experimental Wing bridge is still GT-MK3-order-dependent. It is NOT proof of an independent LMP MK3 executor and must be replaced or isolated before that capability is claimed.
- **Testing:** source/CI checks do not establish in-game execution, save safety, or compatibility with Rebirth(ed).

