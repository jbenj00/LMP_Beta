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
# LMP-only MK3 wing enrollment must be separate from GT's experimental bridge.
native = ET.parse(ROOT / "LMP_Wing.xml").getroot()
def wing_library(name):
    found = [n for n in native.iter("library") if n.get("name") == name]
    assert len(found) == 1, name
    return found[0]
enroll = wing_library("LMP_RegisterDedicatedWing")
enroll_xml = ET.tostring(enroll, encoding="unicode")
assert "GUNPIRE_IsGTManagedShip" in enroll_xml
assert "LMP_ShipRegistry.LMP_EnrollShip" in enroll_xml
assert "LMP_WING_CONFIG_ONLY" in enroll_xml
assert "'WING'" in enroll_xml
assert "GalaxyTraderMK3" not in enroll_xml, "Dedicated LMP wings cannot require GT's default order"
assert not list(enroll.iter("create_order")) and not list(enroll.iter("create_trade_order"))
home = wing_library("LMP_SetDedicatedWingHome")
home_xml = ET.tostring(home, encoding="unicode")
assert "$mode == 'SECTOR'" in home_xml and "$mode == 'STATION'" in home_xml and "$mode == 'NONE'" in home_xml
assert "$home.isclass.sector" in home_xml and "$home.isclass.station" in home_xml
assert "LMP_WING_CONFIG_ONLY" in home_xml and "$role != 'WING'" in home_xml
for node in home.iter():
    assert node.tag not in ("create_order", "cancel_order", "create_trade_order", "remove_value"), "Home config cannot mutate ship work"
member_enroll = wing_library("LMP_EnrollDedicatedWingMember")
member_xml = ET.tostring(member_enroll, encoding="unicode")
assert "$member.commander != $commander" in member_xml
assert "LMP_WING_CONFIG_ONLY" in member_xml
assert "GUNPIRE_IsGTManagedShip" in member_xml
assert "'WING_MEMBER'" in member_xml
assert "$member.cargo.list.count gt 0" in member_xml
assert "$member.tradeorders.count gt 0" in member_xml
assert "$member.defaultorder.id != 'Assist'" in member_xml, "Native escort Assist must remain eligible"
assert "GUNPIRE_IsGTManagedShip" in member_xml, "GT-backed Assist must remain excluded"
assert 'name="global.$LMP_Ships.{$member}.$wingCommander" exact="$commander"' in member_xml
for unsafe in ("create_order", "cancel_order", "create_trade_order", "remove_value"):
    assert not list(member_enroll.iter(unsafe)), "Enrollment cannot change ship orders"
member_release = wing_library("LMP_UnenrollDedicatedWingMember")
member_release_xml = ET.tostring(member_release, encoding="unicode")
assert "$role != 'WING_MEMBER'" in member_release_xml
assert "$wingCommander != $commander" in member_release_xml
assert "$member.cargo.list.count gt 0" in member_release_xml
assert "$member.tradeorders.count gt 0" in member_release_xml
assert "$member.defaultorder.id != 'Assist'" in member_release_xml, "Safe release must preserve native Assist"
assert len(list(member_release.iter("remove_value"))) == 1
for unsafe in ("create_order", "cancel_order", "create_trade_order"):
    assert not list(member_release.iter(unsafe)), "Unenrollment cannot alter work"
capacity = wing_library("LMP_GetWingCapacity")
capacity_xml = ET.tostring(capacity, encoding="unicode")
assert "global.$LMP_Wings.{$commander}.$state == 'LMP_WING_CONFIG_ONLY'" in capacity_xml
assert "$role != 'WING_MEMBER'" in capacity_xml
assert "$wingCommander != $commander" in capacity_xml
release = wing_library("LMP_UnregisterDedicatedWing")
release_xml = ET.tostring(release, encoding="unicode")
assert "LMP_WING_CONFIG_ONLY" in release_xml
assert "$role != 'WING'" in release_xml
assert "$commander.cargo.list.count gt 0" in release_xml
assert "$commander.tradeorders.count gt 0" in release_xml
assert "$commander.orders.count gt 0" in release_xml
assert "$commander.defaultorder?" in release_xml
assert len(list(release.iter("remove_value"))) == 2
assert "global.$LMP_Ships.keys" in release_xml, "Commander release must inspect detached members"
assert "global.$LMP_Ships.{$enrolledShip}.$wingCommander == $commander" in release_xml
for unsafe in ("cancel_order", "create_order", "create_trade_order"):
    assert not list(release.iter(unsafe)), "Releasing config must not affect orders"
commands = ET.parse(ROOT / "LMP_Wing_Commands.xml").getroot()
unreg = [n for n in commands.iter("cue") if n.get("name") == "LMP_Wing_CommandUnregister"]
assert len(unreg) == 1
assert "LMP_UnregisterDedicatedWing" in ET.tostring(unreg[0], encoding="unicode")
planner = ET.parse(ROOT / "LMP_Wing_Planner.xml").getroot()
def planner_library(name):
    matched = [node for node in planner.iter("library") if node.get("name") == name]
    assert len(matched) == 1, f"expected one planner library: {name}"
    return matched[0]
scope = planner_library("LMP_CheckDedicatedWingRouteScope")
scope_xml = ET.tostring(scope, encoding="unicode")
assert "LMP_WING_CONFIG_ONLY" in scope_xml and "$role != 'WING'" in scope_xml
assert "$seller.sector == $wing.$homeSector" in scope_xml
assert "$buyer.sector == $wing.$homeSector" in scope_xml
assert "$seller == $wing.$homeStation" in scope_xml
assert "$buyer == $wing.$homeStation" in scope_xml
assert "not $wing.$homeSector.exists" in scope_xml
preview = planner_library("LMP_PreviewDedicatedWingRoute")
preview_xml = ET.tostring(preview, encoding="unicode")
assert "LMP_CheckDedicatedWingRouteScope" in preview_xml
assert "LMP_PlanWingCargo" in preview_xml
assert preview_xml.index("LMP_CheckDedicatedWingRouteScope") < preview_xml.index("LMP_PlanWingCargo")
assert "$quoteOnly = true" in preview_xml
assert "$requiresMarketValidation = true" in preview_xml
assert "global.$GT_" not in preview_xml
for read_only in (scope, preview):
    for prohibited in ("create_order", "cancel_order", "create_trade_order", "remove_value"):
        assert not list(read_only.iter(prohibited)), "Independent LMP preview cannot mutate ship state"
print(f"PASS: {len(WING)} parsed wing scripts, {len(libraries)} libraries; no trade/order mutations")
print("NOTE: This is a static parse / invariant check, not XSD validation or an in-game test.")
