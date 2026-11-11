#!/usr/bin/env python3
"""Offline XML and non-invasive wing integration checks. Not an X4 runtime test."""
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / "gunpire_logistics" / "md"
WING = sorted(ROOT.glob("LMP_Wing*.xml"))
assert len(WING) >= 6, f"expected wing modules, found {len(WING)}"
libraries = {}
cues = {}
for f in WING:
    root = ET.parse(f).getroot()
    assert root.tag == "mdscript", f"{f}: invalid root"
    assert root.attrib.get("name") == f.stem, f"{f}: script filename differs from name"
    for item in root.findall(".//library"):
        name = item.attrib["name"]
        assert name not in libraries, f"duplicate library: {name}"
        libraries[name] = f
    for item in root.findall(".//cue"):
        name = item.attrib["name"]
        assert name not in cues, f"duplicate cue: {name}"
        cues[name] = f
    # Wing decision/observation code must never take over GT jobs.
    forbidden = {"create_trade_order", "create_order", "remove_order", "remove_orders", "set_default_order", "set_cargo"}
    for node in root.iter():
        assert node.tag not in forbidden, f"{f.name}: unexpected mutating action {node.tag}"
    print(f"Parsed {f.name}")
for expected in (
    "LMP_RegisterWing", "LMP_GetWingCapacity", "LMP_PlanWingCargo",
    "LMP_PreviewMK3WingTrade", "LMP_ValidateWingQuote",
):
    assert expected in libraries, f"missing library: {expected}"
print(f"PASS: {len(WING)} parsed wing scripts, {len(libraries)} libraries; no trade/order mutations")
print("NOTE: This is a static parse / invariant check, not XSD validation or an in-game test.")
