# GUNPIRE Logistics integration map — X4: Foundations 9.00

## Verified contracts and limits

| API / property | Source | What is established |
|---|---|---|
| `create_trade_order` | `refs/x4_scripting_ref/schemas/common.xsd:24057-24082` | Creates an AI trade order in an object's order queue and associates a trade deal. The schema does not define a build-storage destination or prove that the order deposits at that destination. |
| `find_sell_offer` | `refs/x4_scripting_ref/schemas/common.xsd:28283-28347,9238-9310` | Filters offers through the `wares` attribute and trade filters; it does not accept a nested `match_ware` element. |
| Trade completion events | `refs/x4_scripting_ref/schemas/common.xsd:16739-16788` | `event_trade_completed` supplies a tradeoffer and tradeorder. This is not a documented build-storage deposit confirmation. `event_trade_cancelled` supplies a tradeoffer, not a ship/job/order correlation key. |
| Cargo and order properties | `refs/x4_scripting_ref/schemas/scriptproperties.xml:324-330,694,1919-1923,1997-2007` | A container exposes cargo as a ware-amount list; wares expose `iscargo`, `isammo`, and `isdeployable`; the ship exposes queued orders and tradeorders. Unknown cargo classifications fail closed. Pending transfers and a complete eligibility protocol are not established. |
| Build shortage | `refs/x4_scripting_ref/schemas/scriptproperties.xml:687-690,1711-1723` | `neededbuildresources.{$build}` takes a concrete build object. `plannedconstruction.sequence` is a construction sequence, not that build object. The current scanner records build-storage objects but no unverified quantity. |
| GT order identifiers and cleanup risk | `refs/M0/GT_HANDOFF_DECISION.md:14-34` | Galaxy Trader 1.0.4 takeover remains hard-blocked; replacing its default order may trigger permanent removal and cleanup. |

The schema bundle verifies syntax and declared properties, not engine behavior. The repository does not include vanilla `order.trade.perform`/related AI or MD source files; `refs/03_Extracted_Source_Index.md` is an index, not those source files. Therefore the engine's purchase-to-destination behavior cannot be established here.

## Status

### IMPLEMENTED

- Unknown, loaded, or unclassifiable trade cargo rejects takeover; ammo and deployables are not treated as trade cargo.
- All takeover is blocked until complete snapshot/restore and eligibility contracts are verified. Galaxy Trader MK1/MK2/MK3/MK4/MK42 are explicitly blocked.
- Production dispatch and direct order creation are hard-gated. The five profiles remain; `TEST_SINGLE_SHIP` retains its one-ship limit, and `TEST_DISPATCHER` / `TEST_UI` cannot issue production orders.
- Invented Hull Parts quantities are removed. A trade completion updates only the exactly matched ship/order/job to “awaiting deposit”; it does not release the reservation. Cancellation and save/load ambiguity retain records and commitments.

### STATICALLY VALIDATED

- Run `python -m unittest discover -s tests -v` for XML well-formedness and lifecycle-safety assertions.
- The tests are static checks only. Well-formed XML is not XSD validation.
- Logistics MD cue/library contents were checked against the bundled X4 9.00 MD XSD; API and event declarations were cross-checked against the bundled common/property schemas. No game engine was used.

### RUNTIME UNTESTED

- No behavior has been tested in X4. No save files were read or modified.

### BLOCKED

- **Purchase → destination deposit:** `create_trade_order` is documented as a queued trade deal, but no destination parameter or deposit behavior is documented. Required missing contract: the vanilla AI/MD implementation or an engine API proving the order deposits to a specified buildstorage, plus an observable deposit-completion signal.
- **Non-GT takeover/restoration:** no complete, verified snapshot/restore contract for default behavior parameters, queued orders, commander/home/range, or safe resumption.
- **Cargo eligibility:** current cargo list/type metadata is documented, but pending transfers/reservations and a complete safe-handoff signal are not.
- **Demand:** no concrete `$build` object is presently available to query `neededbuildresources`; the dispatcher records no shortage and cannot run.
- **Galaxy Trader 1.0.4:** remains hard-blocked; no cooperative pause/lease/restore handshake is established.

## Concise acceptance checklist

- [x] No cargo-empty bypass; unknown cargo state rejects takeover, while ammo/deployables are excluded from trade cargo.
- [x] Galaxy Trader takeover hard-blocked; unverified non-GT takeover/restoration hard-gated.
- [x] No fabricated ware or quantity; dispatch requires a positive shortage record.
- [x] Trade completion is separate from destination deposit; reservations survive callbacks, cancellation, and save/load uncertainty.
- [ ] Verify purchase and destination deposit against actual vanilla AI/MD or engine behavior.
- [ ] Verify non-GT snapshot/restore and pending-transfer eligibility in X4 before enabling execution.
- [ ] Run the checklist in-game on a copy of a save; mark no item game-tested until performed in X4.
