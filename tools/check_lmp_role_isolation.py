#!/usr/bin/env python3
"""Validate LMP PASSIVE and MK3 Wing ownership boundaries (static, not runtime)."""
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / "gunpire_logistics" / "md"
registry = ET.parse(ROOT / "LMP_ShipRegistry.xml").getroot()
wing = ET.parse(ROOT / "LMP_Wing.xml").getroot()

def library(root, name):
    matches = [e for e in root.iter("library") if e.get("name") == name]
    assert len(matches) == 1, name
    return matches[0]

def xml(element):
    return ET.tostring(element, encoding="unicode")

enroll = xml(library(registry, "LMP_EnrollShip"))
start = xml(library(registry, "LMP_StartPassiveShip"))
register = xml(library(wing, "LMP_RegisterWing"))
capacity = xml(library(wing, "LMP_GetWingCapacity"))

assert "$role == 'ACTIVE'" in enroll, "Legacy ACTIVE enrollment must be disabled"
assert enroll.index("$role == 'ACTIVE'") < enroll.index('name="global.$LMP_Ships.{$ship}"'), "Reject ACTIVE before registry writes"
assert "$role == 'PASSIVE'" in enroll
assert "global.$LMP_Wings.{$ship}?" in enroll, "Cannot enroll wing commander as PASSIVE"
assert "global.$LMP_Wings.{$ship.commander}?" in enroll, "Cannot enroll wing member as PASSIVE"
assert "global.$LMP_Ships.{$ship}.$role != $role" in enroll, "Cannot switch existing role in place"
assert enroll.index("global.$LMP_Wings.{$ship}?") < enroll.index('name="global.$LMP_Ships.{$ship}"'), "Check wing ownership before allocating registry"
assert "global.$LMP_Wings.{$ship}?" in start and "global.$LMP_Wings.{$ship.commander}?" in start
assert start.index("global.$LMP_Wings.{$ship}?") < start.index("<create_order"), "Check wing ownership before PASSIVE order"
assert "global.$LMP_Ships.{$commander}.$role == 'PASSIVE'" in register
assert "global.$LMP_Ships.{$commander}.$role == 'PASSIVE'" in capacity, "Reject stale wing entry with PASSIVE commander"
assert "global.$LMP_Ships.{$ship}.$role == 'PASSIVE'" in capacity, "Exclude PASSIVE subordinate cargo"
for body in (enroll, register, capacity):
    root = ET.fromstring(body)
    for forbidden in ("create_order", "cancel_order", "create_trade_order", "remove_value"):
        assert not list(root.iter(forbidden)), f"Ownership check must not mutate orders/registry: {forbidden}"
print("PASS: LMP PASSIVE / MK3 Wing role boundaries are guarded; no takeover")
print("NOTE: static checks only; native X4 assignment semantics remain untested.")
