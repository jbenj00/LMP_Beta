## Verified trade path (non-GT)

| API | Source | Notes |
|---|---|---|
| `find_sell_offer` | common.xsd ~28283 | Returns actual trade offers. Supports tradepartner, seller, excludeempty, usereservations. |
| `create_trade_order` | common.xsd ~24057 | Creates hard-coded trade order (TradePerform) + trade deal. Added to queue; does **not** replace default order. Params: object, tradeoffer, amount, optional price/name. |
| `.defaultorder.id` | scriptproperties | Used to reject GalaxyTraderMK* ships. |

**create_order default=false** was previously used with guessed TradePerform params. Replaced by verified `create_trade_order`, which is the engine-supported way to queue a trade without altering the default behavior.

**Limitation:** Exact shortage quantities from `.neededbuildresources` still require a concrete `$build` reference; current scan tracks buildstorage objects only. Ware selection remains a probe until that is wired.