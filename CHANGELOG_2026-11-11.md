# GUNPIRE safe source-alignment patch — 2026-11-11

## Changes
- `GUNPIRE_Core.xml`: added `GUNPIRE_IsGTManagedShip` matching GT 1.0.4 MK3/MK4Supply and Assist/baseorder; replaced always-true cargo placeholder with GT cargo-list check.
- `LMP_Orders.xml`: uses shared GT order recognition to prevent unapproved takeover.
- `LMP_Dispatcher.xml`: uses shared recognition; removed fabricated hullparts shortage; checks reservation success; **blocks dispatch** rather than issuing unmatched purchase-only trade orders.
- Source-to-goal MD: corrected identifiers, per-trip reranking requirement and full completion boundary.

## Validation
- XML well-formedness: passed (lxml). Not X4 engine/schema or in-game tested.
- Source comparison: matched GT `order.trade.galaxytradermk4.xml` and `gt_trading_signals.xml`.

## Not implemented / intentionally blocked
- Cooperative GT pre-assignment interception and complete trader settings restoration.
- Paired buy+delivery execution, job/order correlation, event-driven completion and failure recovery.
- Re-ranking source/demand from live position each completed trip; POS aging; passive MK1 fallback.
- Cargo-empty check is only one condition; pending orders/commitments still require verification.

**Do not enable production dispatch or remove the fail-closed block until the missing trade lifecycle is implemented and validated.**