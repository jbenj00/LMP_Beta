#!/usr/bin/env python3
"""Static regression checks for partial paired-order setup. Not an X4 runtime test."""
from pathlib import Path
from xml.etree import ElementTree as ET

base = Path(__file__).resolve().parents[1] / "gunpire_logistics/md"
def library(file, name):
    root = ET.parse(base / file).getroot()
    found = [x for x in root.iter("library") if x.get("name") == name]
    assert len(found) == 1, name
    return found[0]

dispatch = library("LMP_Dispatcher.xml", "LMP_DispatchOne")
cycle = library("LMP_TradeCycle.xml", "LMP_QueuePairedTrade")
d = ET.tostring(dispatch, encoding="unicode")
c = ET.tostring(cycle, encoding="unicode")
queue_call = d.index('ref="md.LMP_TradeCycle.LMP_QueuePairedTrade"')
for field in ("$job", "$requestedQty", "$purchasedQty", "$deliveredQty",
              "$sourceOffer", "$targetOffer", "$buyOrder", "$deliverOrder"):
    marker = 'name="global.$LMP_Ships.{$ship}.' + field + '"'
    assert marker in d and d.index(marker) < queue_call, "Missing pre-order transaction field: " + field
assert "ORDER_SETUP" in d
assert "QUARANTINED" in d
assert "$stopRequested" in d
assert "global.$LMP_Ships.{$ship}.$buyOrder" in d[d.index('result="$trip"'):], "Must preserve buy handle after call"
assert c.index('name="$buyOrder"') < c.index('name="$deliverOrder"'), "Buy must be attempted first"
assert 'value="table[$buy = $buyOrder]"' in c, "Failed second leg must return live buy handle"
assert not list(dispatch.iter("cancel_order")), "Failure must not cancel queued buys"
assert not list(dispatch.iter("remove_value")), "Failure must not release reservation"
# A completed BUY-only order can be promoted only after actual cargo matches.
recovery = ET.parse(base / "LMP_Recovery.xml").getroot()
menu = ET.parse(base / "LMP_ContextMenu.xml").getroot()
checks = [n for n in recovery.iter("library") if n.get("name") == "LMP_RecheckIncompletePair"]
assert len(checks) == 1, "Missing conservative buy-only reconciliation"
check = checks[0]
chk = ET.tostring(check, encoding="unicode")
assert "QUARANTINED" in chk and "STRANDED_CARGO_RECONCILE" in chk
assert "$entry.$buyOrder?" in chk and "$entry.$deliverOrder?" in chk
assert "$entry.$purchasedQty le 0" in chk and "$entry.$deliveredQty != 0" in chk
assert "LMP_VerifyTripReservation" in chk
assert "$ship.cargo.list.count != 1" in chk
assert "$ship.cargo.{$reservation.$ware}.count != $entry.$purchasedQty" in chk
assert "$ship.tradeorders.count gt 0" in chk
for forbidden in ("create_trade_order", "cancel_order", "remove_value"):
    assert not list(check.iter(forbidden)), "Reclassification cannot mutate ship: " + forbidden
completed = [n for n in recovery.iter("cue") if n.get("name") == "LMP_OnTradeCompleted"]
assert len(completed) == 1
event_xml = ET.tostring(completed[0], encoding="unicode")
assert "state == 'QUARANTINED'" in event_xml
assert "not global.$LMP_Ships.{$ship}.$deliverOrder?" in event_xml
assert "transferredamount" in event_xml
tick = [n for n in menu.iter("cue") if n.get("name") == "LMP_PassiveTick"]
assert len(tick) == 1
tick_xml = ET.tostring(tick[0], encoding="unicode")
assert tick_xml.index("LMP_RecheckIncompletePair") < tick_xml.index("LMP_ResumeStrandedDelivery"), "Recheck before attempting delivery"
print("PASS: partially queued trade preserves buy handle and original reserved job")
