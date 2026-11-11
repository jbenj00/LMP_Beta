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
print("PASS: partially queued trade preserves buy handle and original reserved job")
