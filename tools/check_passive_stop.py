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
reservations = read("LMP_Reservations.xml")

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
cancel = named(recovery, "cue", "LMP_OnTradeCancelled")
cancel_xml = ET.tostring(cancel, encoding="unicode")
load_xml = ET.tostring(named(recovery, "cue", "LMP_Recovery_OnLoad"), encoding="unicode")
assert 'event.param2' not in cancel_xml, "X4 trade-cancelled has no order in param2"
assert 'event.param' in cancel_xml, "Trade cancellation must read documented offer event.param"
assert "$sourceOffer" in cancel_xml and "$targetOffer" in cancel_xml, "Only tracked offers may quarantine an LMP job"
assert "global.$LMP_Ships.keys" in cancel_xml, "Shared offer cancellations must check all enrolled ships"
dispatcher = read("LMP_Dispatcher.xml")
dispatch_xml = ET.tostring(named(dispatcher, "library", "LMP_DispatchOne"), encoding="unicode")
assert "$sourceOffer" in dispatch_xml and "$targetOffer" in dispatch_xml, "Successful trip must record offer handles"
assert "TRADE_CANCELLED_RECONCILE" in cancel_xml, "Cancel must quarantine ship"
assert "$stopRequested" in cancel_xml, "Cancel must block further dispatch"
assert "TRADE_CANCELLED_RECONCILE" in load_xml, "Save-load must preserve quarantined state"
assert "TRADE_CANCELLED_RECONCILE" in ET.tostring(on_trade, encoding="unicode"), "Late trade completion must not erase cancellation"
assert ET.tostring(tail, encoding="unicode").count("$sourceOffer") > 0, "Tail must clear stale offer correlation"
assert ET.tostring(on_trade, encoding="unicode").count("$sourceOffer") > 0, "Completion must clear stale offer correlation"
assert not list(cancel.iter("remove_value")), "No reservations/registry may be released on cancel"
assert not list(cancel.iter("cancel_order")), "Cancellation recovery must not mutate ship order queue"
reserve = named(reservations, "library", "LMP_Reserve")
reserve_xml = ET.tostring(reserve, encoding="unicode")
assert "global.$LMP_Reservations.{$key}?" in reserve_xml, "Duplicate job guard required"
assert reserve_xml.index("global.$LMP_Reservations.{$key}?") < reserve_xml.index('<set_value name="global.$LMP_Reservations.{$key}"'), "Duplicate guard must precede ledger write"
assert any(e.attrib.get("ref") == "md.LMP_Dispatcher.LMP_DispatchOne" for e in on_trade.iter("run_actions"))
assert "cargo.list.count" in ET.tostring(finished, encoding="unicode")
assert "tradeorders.count" in ET.tostring(finished, encoding="unicode")
# Trade completion must account for actual units, never assume requested == delivered.
verify = named(recovery, "library", "LMP_VerifyActualDelivery")
verify_xml = ET.tostring(verify, encoding="unicode")
on_trade_xml = ET.tostring(on_trade, encoding="unicode")
assert "$requestedQty" in dispatch_xml and "$purchasedQty" in dispatch_xml and "$deliveredQty" in dispatch_xml
assert "$entry.$purchasedQty != $entry.$deliveredQty" in verify_xml
assert "$entry.$deliveredQty gt $entry.$requestedQty" in verify_xml
assert "transferredamount" in on_trade_xml
assert "event.param2" in on_trade_xml and "$order == global.$LMP_Ships.{$candidate}.$buyOrder" in on_trade_xml
assert "$order.object" not in on_trade_xml, "Trade deal is not guaranteed to expose owning ship via .object"
assert "$purchasedQty" in on_trade_xml and "$deliveredQty" in on_trade_xml
assert "LMP_VerifyActualDelivery" in on_trade_xml and "LMP_VerifyActualDelivery" in tail_xml
assert "QUANTITY_RECONCILE" in on_trade_xml and "QUANTITY_RECONCILE" in tail_xml
assert "QUANTITY_RECONCILE" in load_xml, "Save-load must preserve unresolved quantities"

# Save/load recovery is deliberately non-destructive and distinguishes
# stranded cargo from missing orders. Neither is a completed delivery.
audit = named(recovery, "library", "LMP_AuditLoadedTrip")
audit_xml = ET.tostring(audit, encoding="unicode")
assert "RECONCILE_ON_LOAD" in audit_xml
assert "STRANDED_CARGO_RECONCILE" in audit_xml
assert "MISSING_ORDER_RECONCILE" in audit_xml
assert "CARGO_UNKNOWN_RECONCILE" in audit_xml
assert "RESERVATION_MISSING_RECONCILE" in audit_xml
assert "RESERVATION_MISMATCH_RECONCILE" in audit_xml
assert "global.$LMP_Reservations.{$key}.$ship != $ship" in audit_xml
assert "$reservationKey" in audit_xml, "Saved jobs must use persisted ledger reference"
assert "$reservationKey" in reserve_xml, "Reservation creator must persist lookup key"
assert "global.$LMP_Reservations.{$key}?" in audit_xml
assert audit_xml.index("state != 'RECONCILE_ON_LOAD'") < audit_xml.index("RESERVATION_MISSING_RECONCILE"), "Audit may not overwrite terminal states"
assert "$ship.cargo.list.count gt 0" in audit_xml
assert "$ship.tradeorders.count gt 0" in audit_xml
assert "$stopRequested" in audit_xml
assert not list(audit.iter("create_trade_order"))
assert not list(audit.iter("cancel_order"))
assert not list(audit.iter("remove_value"))
assert not any("LMP_Reservations.LMP_Release" in e.attrib.get("ref","") for e in audit.iter("run_actions"))
assert "LMP_AuditLoadedTrip" in load_xml
assert "LMP_ReconcileDeliveryTail" in load_xml, "Observed delivery tails must be rechecked on load"
assert "$pendingTails" in load_xml, "Tail completion must run after registry enumeration"
assert "md.LMP_Recovery.LMP_ReconcileDeliveryTail" in load_xml
assert "LMP_AuditLoadedTrip" in ET.tostring(tick, encoding="unicode")
assert "STRANDED_CARGO_RECONCILE" in load_xml and "MISSING_ORDER_RECONCILE" in load_xml
print("PASS: PASSIVE stop guards, completion and retry hooks are present")
print("NOTE: structural tests do not prove X4 runtime behavior")
