#!/usr/bin/env python3
"""PASSIVE stop static regression checks. Not a runtime X4 test."""
from pathlib import Path
from xml.etree import ElementTree as ET

root = Path(__file__).resolve().parents[1] / "gunpire_logistics" / "md"
def read(name):
    return ET.parse(root / name).getroot()

registry = read("LMP_ShipRegistry.xml")
recovery = read("LMP_Recovery.xml")
menu = read("LMP_ContextMenu.xml")
cycle = read("LMP_TradeCycle.xml")

def named(root_node, tag, name):
    result = [n for n in root_node.iter(tag) if n.attrib.get("name") == name]
    assert len(result) == 1, f"Expected one {name}, found {len(result)}"
    return result[0]

final = named(registry, "library", "LMP_FinalizePassiveStop")
stop = named(registry, "library", "LMP_StopPassiveShip")
on_trade = named(recovery, "cue", "LMP_OnTradeCompleted")
tick = named(menu, "cue", "LMP_PassiveTick")
finished = named(cycle, "library", "LMP_TripIsFullyFinished")

assert len(list(final.iter("cancel_order"))) == 1, "Only our own default order can be cancelled"
assert not list(final.iter("cancel_all_orders")), "No queue flush allowed"
assert not list(final.iter("create_order")), "Stopping cannot replace assignments"
assert list(final.iter("remove_value")), "Must unregister released ship"

fxml = ET.tostring(final, encoding="unicode")
assert "LMP_Passive" in fxml, "Must restrict default cancellation to LMP_Passive"
assert "$stopRequested" in fxml, "Must require explicit stop"
assert "$job" in fxml, "Must not release during a job"
assert "LMP_TripIsFullyFinished" in fxml, "Must wait for empty cargo and no trade orders"
assert fxml.index("LMP_TripIsFullyFinished") < fxml.index("<cancel_order"), "Idleness check must precede cancellation"

for label, node in (("Stop action", stop), ("trade completion", on_trade), ("idle tick", tick)):
    assert any(
        e.attrib.get("ref") == "md.LMP_ShipRegistry.LMP_FinalizePassiveStop"
        for e in node.iter("run_actions")
    ), f"{label} must attempt final release"

tail = named(recovery, "library", "LMP_ReconcileDeliveryTail")
tail_xml = ET.tostring(tail, encoding="unicode")
assert "DELIVERY_RECONCILE" in tail_xml, "Tail reconciliation needs observed delivery-completed state"
assert "LMP_TripIsFullyFinished" in tail_xml, "Tail reconciliation needs an empty hold and clear trade queue"
assert "LMP_Reservations.LMP_Release" in tail_xml, "Tail must release reservation at clean boundary"
assert any(e.attrib.get("ref") == "md.LMP_Recovery.LMP_ReconcileDeliveryTail" for e in tick.iter("run_actions")), "Idle tick must revisit delayed delivery completion"
assert any(e.attrib.get("ref") == "md.LMP_Dispatcher.LMP_DispatchOne" for e in on_trade.iter("run_actions"))
assert "cargo.list.count" in ET.tostring(finished, encoding="unicode")
assert "tradeorders.count" in ET.tostring(finished, encoding="unicode")
print("PASS: PASSIVE stop guards, completion and retry hooks are present")
print("NOTE: structural tests do not prove X4 runtime behavior")
