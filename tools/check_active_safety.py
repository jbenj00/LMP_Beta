#!/usr/bin/env python3
"""Static invariants for experimental ACTIVE GT takeover. Not an X4 runtime test."""
from pathlib import Path
from xml.etree import ElementTree as ET

root = Path(__file__).resolve().parents[1]
takeover = ET.parse(root / "gunpire_logistics/md/LMP_Takeover.xml").getroot()
def library(name):
    found = [n for n in takeover.iter("library") if n.get("name") == name]
    assert len(found) == 1, name
    return found[0]

snap = library("LMP_SnapshotShip")
request = library("LMP_RequestTakeover")
s = ET.tostring(snap, encoding="unicode")
r = ET.tostring(request, encoding="unicode")
assert "$snapshot? and global.$LMP_Ships.{$ship}.$snapshot != null" in s, "Never clobber saved trader snapshot"
assert "global.$LMP_Ships.{$ship}.$role != 'ACTIVE'" in r, "Require explicit ACTIVE role"
assert "GUNPIRE_IsGTManagedShip" in r, "Require documented GT order"
assert "$ship.tradeorders.count gt 0" in r, "Do not borrow queued trades"
assert "GUNPIRE_SafetyCheckCargoEmpty" in r, "Require empty cargo"
assert "$job != null" in r, "Do not interrupt an existing logistics job"
assert "$snapshot != null" in r, "Never overwrite incomplete handoff snapshot"
assert "BLOCKED_GT_HANDOFF" in r, "Must remain non-executing until GT cooperative handoff is proven"
for tag in ("create_order", "cancel_order", "create_trade_order", "remove_value"):
    assert not list(request.iter(tag)), "ACTIVE gate cannot mutate orders: " + tag
assert not list(snap.iter("create_order")) and not list(snap.iter("cancel_order")), "Snapshot must not touch orders"
print("PASS: ACTIVE GT takeover stays non-mutating and fail-closed")
print("NOTE: Static checks do not demonstrate safe in-game handoff or restoration")
