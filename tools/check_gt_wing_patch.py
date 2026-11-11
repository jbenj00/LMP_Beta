#!/usr/bin/env python3
"""Check GT MK3 wing patch safety, schema, and optional real GT source match.

Usage: python tools/check_gt_wing_patch.py [path/to/GT/aiscripts/order.trade.galaxytrader.xml]
CI validates syntax and the AI library; local source review validates exact XPath.
These checks are not a substitute for an in-game GT 1.0.4 test.
"""
from pathlib import Path
from sys import argv
from lxml import etree

root = Path(__file__).resolve().parents[1]
patch_path = root / "gunpire_logistics/aiscripts/order.trade.galaxytrader.xml"
helper_path = root / "gunpire_logistics/aiscripts/lib.lmp.wing.extend.xml"
busy_path = root / "gunpire_logistics/aiscripts/lib.lmp.wing.busy.xml"
schema_path = root / "refs/x4_scripting_ref/schemas/aiscripts.xsd"

patch = etree.parse(str(patch_path))
assert patch.getroot().tag == "diff", "GT patch must be XML diff, not a GT script replacement"
ops = patch.getroot().findall("add")
assert len(ops) == 2 and len([x for x in patch.getroot() if isinstance(x.tag, str)]) == 2, "Unexpected GT patch operations"
selector = ops[0].get("sel")
loop_selector = ops[1].get("sel")
assert loop_selector == "//label[@name='main_loop']"
assert ops[1].get("pos") == "after"
gate = ops[1].find("do_if")
assert gate is not None and "global.$LMP_Wings" in gate.get("value", "")
busy_calls = gate.xpath("run_script[@name=\"'lib.lmp.wing.busy'\"]")
assert len(busy_calls) == 1 and gate.find("do_if/resume").get("label") == "main_loop"
assert selector == "//create_trade_order[@object='this.ship'][@tradeoffer='$pendingTrade.$BuyOffer'][@amount='$finalBuyAmount']"
assert ops[0].get("pos") == "after"
insert = ops[0].find("do_if")
assert insert is not None and "global.$LMP_Wing_ExecuteEnabled" in insert.get("value", "")
call = insert.find("run_script")
assert call is not None and call.get("name") == "'lib.lmp.wing.extend'"
for param in ("commander", "buyStation", "sellStation", "ware", "additionalTarget", "commanderAmount", "commanderUnitPrice", "minROI", "minAbsoluteProfit", "buyInternal", "sellInternal"):
    assert call.xpath("param[@name=$p]", p=param), f"Missing GT parameter {param}"

schema = etree.XMLSchema(etree.parse(str(schema_path)))
script = etree.parse(str(helper_path))
assert script.getroot().get("name") == "lib.lmp.wing.extend"
if not schema.validate(script):
    raise SystemExit("\n".join(str(e) for e in schema.error_log))
busy = etree.parse(str(busy_path))
assert busy.getroot().get("name") == "lib.lmp.wing.busy"
if not schema.validate(busy):
    raise SystemExit("\\n".join(str(e) for e in schema.error_log))
print("PASS both AI helpers against X4 aiscripts.xsd")
print("PASS guarded GT MK3 patch structure")

if len(argv) > 1:
    source = etree.parse(argv[1])
    matches = source.xpath(selector)
    loop_matches = source.xpath(loop_selector)
    assert len(loop_matches) == 1, f"GT main_loop should match once, matched {len(loop_matches)}"
    assert len(matches) == 1, f"GT 1.0.4 hook should match once, matched {len(matches)}"
    assert matches[0].get("immediate") == "true", "GT order semantics changed"
    assert matches[0].get("internal") == "$tradeBuyLegInternal"
    print("PASS targeted hook matches supplied GT source exactly once")
else:
    print("NOTE: real GT source not bundled; provide source path for exact XPath check")
print("NOTE: no in-game execution has been tested")
