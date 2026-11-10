import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "gunpire_logistics" / "md"


def load_script(name):
    return ET.parse(MD_DIR / name).getroot()


def find_library(root, name):
    return root.find(f"./cues/library[@name='{name}']")


def find_actions(library):
    return library.find("./actions")


class LifecycleSafetyTests(unittest.TestCase):
    def test_logistics_md_is_well_formed(self):
        paths = list(MD_DIR.glob("*.xml")) + list((ROOT / "refs" / "M0" / "md").glob("*.xml"))
        for path in paths:
            with self.subTest(path=path.name):
                ET.parse(path)

    def test_cargo_check_classifies_trade_cargo_and_fails_closed(self):
        root = load_script("GUNPIRE_Core.xml")
        actions = find_actions(find_library(root, "GUNPIRE_SafetyCheckCargoEmpty"))
        children = list(actions)

        self.assertIn("$ship.cargo.count", ET.tostring(actions, encoding="unicode"))
        self.assertIn("$ware.iscargo?", ET.tostring(actions, encoding="unicode"))
        self.assertIn("$ware.isdeployable?", ET.tostring(actions, encoding="unicode"))
        self.assertEqual(children[-1].tag, "return")
        self.assertEqual(children[-1].get("value"), "true")
        self.assertTrue(any(node.tag == "do_if" and node.find("./return[@value='false']") is not None
                            for node in children[:-1]))

    def test_unverified_lifecycle_is_always_blocked(self):
        root = load_script("GUNPIRE_Config.xml")
        actions = find_actions(find_library(root, "GUNPIRE_LifecycleReadyForExecution"))
        self.assertEqual(len(actions), 1)
        self.assertEqual(actions[0].tag, "return")
        self.assertEqual(actions[0].get("value"), "false")

        for filename, library_name in (
            ("LMP_Dispatcher.xml", "LMP_DispatchOne"),
            ("LMP_Orders.xml", "LMP_CreateTradeOrder"),
        ):
            with self.subTest(library=library_name):
                actions = find_actions(find_library(load_script(filename), library_name))
                self.assertEqual(actions[0].get("ref"), "GUNPIRE_LifecycleReadyForExecution")

    def test_dispatch_has_no_fabricated_shortage_fallback(self):
        dispatcher = (MD_DIR / "LMP_Dispatcher.xml").read_text()
        demand = (MD_DIR / "LMP_Demand.xml").read_text()
        self.assertNotIn("ware.hullparts", dispatcher)
        self.assertNotIn("exact=\"100\"", dispatcher)
        self.assertNotIn("$st.neededbuildresources", demand)
        self.assertNotIn(".$qty", demand)
        self.assertIn("no concrete, positive build-storage shortage", dispatcher)

    def test_sell_offer_uses_the_schema_ware_filter(self):
        root = load_script("LMP_Sources.xml")
        offer = root.find(".//find_sell_offer")
        self.assertIsNotNone(offer)
        self.assertEqual(offer.get("wares"), "$ware")
        self.assertFalse(list(offer))

    def test_profiles_and_single_ship_limit_remain(self):
        root = load_script("GUNPIRE_Config.xml")
        config = ET.tostring(root, encoding="unicode")
        for profile in ("TEST_SINGLE_SHIP", "TEST_FLEET", "FULL", "TEST_DISPATCHER", "TEST_UI"):
            with self.subTest(profile=profile):
                self.assertIn(profile, config)

        max_ships = find_actions(find_library(root, "GUNPIRE_MaxControlledShips"))
        self.assertTrue(any(node.tag == "do_if" and node.get("value") == "global.$GUNPIRE_Profile == 'TEST_SINGLE_SHIP'"
                            and node.find("./return[@value='1']") is not None for node in max_ships))
        allows_orders = ET.tostring(find_actions(find_library(root, "GUNPIRE_AllowsRealOrders")), encoding="unicode")
        self.assertNotIn("TEST_DISPATCHER", allows_orders)
        self.assertNotIn("TEST_UI", allows_orders)

    def test_trade_callbacks_keep_reservations_until_deposit(self):
        root = load_script("LMP_Recovery.xml")
        completed = root.find("./cues/cue[@name='LMP_OnTradeCompleted']/actions")
        cancelled = root.find("./cues/cue[@name='LMP_OnTradeCancelled']/actions")
        on_load = root.find("./cues/cue[@name='LMP_Recovery_OnLoad']/actions")

        for actions in (completed, cancelled, on_load):
            self.assertIsNotNone(actions)
            self.assertFalse(actions.findall(".//run_actions[@ref='LMP_Release']"))
        self.assertIn("$eventOrder", ET.tostring(completed, encoding="unicode"))
        self.assertIn("== $eventOrder", ET.tostring(completed, encoding="unicode"))
        self.assertIn("TRADE_COMPLETED_AWAITING_DEPOSIT_CONFIRMATION",
                      ET.tostring(completed, encoding="unicode"))
        self.assertNotIn("event.param2", ET.tostring(cancelled, encoding="unicode"))
        self.assertFalse(on_load.findall(".//remove_value"))

    def test_reservation_release_requires_confirmed_outcome(self):
        root = load_script("LMP_Reservations.xml")
        actions = find_actions(find_library(root, "LMP_Release"))
        self.assertIn("DELIVERY_CONFIRMED", ET.tostring(actions, encoding="unicode"))
        self.assertIn("SAFE_RECONCILIATION_COMPLETE", ET.tostring(actions, encoding="unicode"))
        self.assertTrue(actions.findall(".//remove_value"))


if __name__ == "__main__":
    unittest.main()
