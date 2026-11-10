## Verified trade path (non-GT)

| API | Source | Notes |
|---|---|---|
| `find_sell_offer` | common.xsd ~28283 | Returns actual trade offers. Supports tradepartner, seller, excludeempty, usereservations. |
| `create_trade_order` | common.xsd ~24057 | Creates hard-coded trade order (TradePerform) + trade deal. Added to queue; does **not** replace default order. Params: object, tradeoffer, amount, optional price/name. |
| `.defaultorder.id` | scriptproperties | Used to reject GalaxyTraderMK* ships. |

**create_order default=false** was previously used with guessed TradePerform params. Replaced by verified `create_trade_order`, which is the engine-supported way to queue a trade without altering the default behavior.

**Limitation:** Exact shortage quantities from `.neededbuildresources` still require a concrete `$build` reference; current scan tracks buildstorage objects only. Ware selection remains a probe until that is wired.

## GalaxyTrader MK3 read-only snapshot

The MK3 snapshot inventory is based on the upstream [GalaxyTrader 1.0.4 order definition](https://github.com/GoAhead-at/galaxy_trader_v9/blob/c6d3c9a36b6dea974babb79ef66f3903e978bc83/aiscripts/order.trade.galaxytrader.xml#L1-L112) and package metadata (`version=10004`, dated 2026-11-07) in the same commit. It includes `home`; `maxbuy`, `maxsell`, `priorityscoremultiplier`, `distancepenalty`, `notifications`, `cargotarget`, `debuglevel`; `marketupdatefreq`; all boolean parameters; the four declared lists; and internal `factionblacklist`. The local X4 property reference documents `.defaultorder` and order `$<param>` access in `refs/x4_scripting_ref/schemas/scriptproperties.xml`.

The diagnostic reads only a live `GalaxyTraderMK3` default order. Missing parameters or unknown inventory types abort capture without storing a partial snapshot or using defaults. Every parameter stores independent `present` and `isNull` flags. List collections are copied into new lists before persistence; elements are copied as-is, with object-valued entries retained as identity references and never modified. The snapshot is GUNPIRE-owned persistent data, version 2. It is compared once after capture and once per game-load recovery; there is no polling. The existing GT takeover hard block is unchanged.

The working clone does not contain the extracted `refs/source` tree described by `refs/03_Extracted_Source_Index.md`; the upstream 1.0.4 source above was used to verify the inventory. Static source/schema inspection does not establish in-game property readability, list/reference persistence semantics, or a runtime match. These remain in-game validation items.