# GUNPIRE — UI and Support API Reference

## Confirmed dependencies

- `GalaxyTraderMK3` requires `kuerteeUIExtensionsAndHUD` and `ws_2042901274`.
- Kuertee ships `ui/` assets and a packed `subst_01.cat/dat` catalog.
- SirNukes ships `ext_01.cat/dat` and loose documentation for API capabilities.

## SirNukes declared capabilities

The SirNukes `content.xml` description lists: **Lua Loader API, Time API, Named Pipes API, Hotkey API, Interact Menu API, Simple Menu API**. This does not establish exact callable function names or compatibility with GT's own UI bridges.

## Loose documentation files

- `source/sn_mod_support_apis/change_log.txt` (4,419 bytes)
- `source/sn_mod_support_apis/content.xml` (879 bytes)
- `source/sn_mod_support_apis/python_send_keys.txt` (43,137 bytes)
- `source/sn_mod_support_apis/python_time_api.txt` (2,660 bytes)
- `source/sn_mod_support_apis/readme.txt` (17,752 bytes)
- `source/sn_mod_support_apis/ui_c_library_winpipe_64.txt` (92,160 bytes)

## Kuertee loose files (selected)

- `source/kuertee_ui_extensions/README.md` (63,933 bytes)
- `source/kuertee_ui_extensions/content.xml` (881 bytes)
- `source/kuertee_ui_extensions/kuertee-ui-extensions-readme.txt` (63,933 bytes)
- `source/kuertee_ui_extensions/t/0001-l007.xml` (499 bytes)
- `source/kuertee_ui_extensions/t/0001-l033.xml` (335 bytes)
- `source/kuertee_ui_extensions/t/0001-l049.xml` (357 bytes)
- `source/kuertee_ui_extensions/t/0001-l081.xml` (378 bytes)
- `source/kuertee_ui_extensions/t/0001-l086.xml` (347 bytes)
- `source/kuertee_ui_extensions/t/0001.xml` (308 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_crafting.xpl` (37,390 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_diplomacy.xpl` (219,593 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_docked.xpl` (95,955 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_encyclopedia.xpl` (207,643 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_map.xpl` (1,664,165 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_playerinfo.xpl` (350,897 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_research.xpl` (46,072 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_scenario_debriefing.xpl` (33,106 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_scenario_selection.xpl` (44,918 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_ship_configuration.xpl` (522,553 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_station_configuration.xpl` (319,967 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_station_overview.xpl` (239,598 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_toplevel.xpl` (22,216 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_trader_blueprintsorlicences.xpl` (42,044 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_transactionlog.xpl` (22,996 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_transporter.xpl` (43,751 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitor/menu_userquestion.xpl` (28,326 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_detailmonitorhelper/helper.xpl` (628,667 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_gameoptions/customgame.xpl` (240,831 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_gameoptions/gameoptions.xpl` (576,979 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_interactmenu/menu_interactmenu.xpl` (424,786 bytes)
- `source/kuertee_ui_extensions/ui/addons/ego_targetmonitor/targetmonitor.xpl` (51,225 bytes)
- `source/kuertee_ui_extensions/ui.xml` (573 bytes)

## Galaxy Trader Lua and UI bridge sources

- `source/galaxy_trader/ui/gt_blacklist_manager.lua` (30,991 bytes)
- `source/galaxy_trader/ui/gt_context_academy.lua` (15,097 bytes)
- `source/galaxy_trader/ui/gt_context_diagnose.lua` (24,629 bytes)
- `source/galaxy_trader/ui/gt_context_pilot_exchange_plan.lua` (10,579 bytes)
- `source/galaxy_trader/ui/gt_context_promote.lua` (45,358 bytes)
- `source/galaxy_trader/ui/gt_context_redistribute.lua` (147,723 bytes)
- `source/galaxy_trader/ui/gt_context_rename.lua` (11,083 bytes)
- `source/galaxy_trader/ui/gt_context_sector_blacklist.lua` (12,130 bytes)
- `source/galaxy_trader/ui/gt_credits_due_override.lua` (6,729 bytes)
- `source/galaxy_trader/ui/gt_crew_name_highlight.lua` (11,208 bytes)
- `source/galaxy_trader/ui/gt_fleet_actions.lua` (4,596 bytes)
- `source/galaxy_trader/ui/gt_fleet_bulk_edit.lua` (15,936 bytes)
- `source/galaxy_trader/ui/gt_fleet_data.lua` (18,902 bytes)
- `source/galaxy_trader/ui/gt_fleet_menu.lua` (7,437 bytes)
- `source/galaxy_trader/ui/gt_fleet_menu_adapter.lua` (8,640 bytes)
- `source/galaxy_trader/ui/gt_fleet_model.lua` (17,481 bytes)
- `source/galaxy_trader/ui/gt_fleet_overview.lua` (8,235 bytes)
- `source/galaxy_trader/ui/gt_fleet_view.lua` (47,648 bytes)
- `source/galaxy_trader/ui/gt_lua_player_bridge.lua` (2,301 bytes)
- `source/galaxy_trader/ui/gt_mk2_ware_exchange.lua` (12,646 bytes)
- `source/galaxy_trader/ui/gt_mk3_faction_blacklist.lua` (13,755 bytes)
- `source/galaxy_trader/ui/gt_mod_refit.lua` (8,165 bytes)
- `source/galaxy_trader/ui/gt_mod_removal.lua` (25,130 bytes)
- `source/galaxy_trader/ui/gt_order_monitor.lua` (9,945 bytes)
- `source/galaxy_trader/ui/gt_order_settings.lua` (16,146 bytes)
- `source/galaxy_trader/ui/gt_order_settings_policy.lua` (17,145 bytes)
- `source/galaxy_trader/ui/gt_order_settings_validation.lua` (13,863 bytes)
- `source/galaxy_trader/ui/gt_personnel_name_override.lua` (4,133 bytes)
- `source/galaxy_trader/ui/gt_pilot_data_bridge.lua` (17,567 bytes)
- `source/galaxy_trader/ui/gt_subordinate_access.lua` (2,263 bytes)
- `source/galaxy_trader/ui/gt_ui_library.lua` (11,909 bytes)

## Integration guidance

- GUNPIRE's primary UI needs fleet enrollment, build-site priority, source filters, ON/OFF, and ship statuses.
- Consider Kuertee UI extension patterns for context-menu integration, but verify hooks from source before coding.
- Prefer namespaced GUNPIRE Lua/MD files; do not overwrite `gt_*` Lua modules or Kuertee UI assets.
- SirNukes simple menu may be useful, but API call contracts must be verified by unpacking CAT/DAT or consulting upstream source.
- Test hotkeys, menus and UI refresh with GT's own fleet interface enabled.

## Documentation extracts

### `source/sn_mod_support_apis/readme.txt`

```text
# X4 Mod Support APIs

Warning: several X4 online features are disabled by this mod due to egosoft restrictions when top level menus are patched.

This is a collection of APIs developed to ease mod creation in a variety of ways. Components include:

* Lua Loader API
  - Support for loading lua files
* Simple Menu API
  - Create custom menus
* Interact Menu API
  - Add new context menu commands
* Named Pipes API
  - Inter-process two-way communication
* Hotkey API
  - Create new hotkeys
* Time API
  - Real-time delays

Note: if installed on an existing save, an additional save/load cycle or a /reloadui command may be needed for all apis to fully register correctly.


### Contributors
* Le Leon - German translation
* Arkblade - Japanese translation


# X4 LUA Loader API

This extension provides support functions to aid in loading lua files.

Note: if using these new lua global functions, add a dependency to the mod apis in your ui.xml file to ensure the functions are loaded earlier. Example: 
```
  <environment type="menus">
    <file name="ui/function_user.lua" />
    <dependency name="sn_mod_support_apis" />
  </environment>
```
  
### Support "require" in protected ui mode

Protected UI mode added in X4 7.5 limits the lua "require" function to a handful of whitelisted modules (eg. "ffi"). Mods may write to the global space to pass data, but as an alternative this API patches the "require" function and allows lua files to register for require support.

New lua global:
* Register_Require_Response(require_path, value)
  - Adds "require" support for the require_path string, returning the given value to any require call.
  - The path does not need to match the actual file path.

### Delayed Init function call

Lua files loaded through ui.xml specification will be initially run before a game has fully loaded, so lookups such as `C.GetPlayerID()` will not work. This API provides a convenient option to delay Init functions until after the game has loaded, delayed by a couple frames.

New lua globals:
* Register_OnLoad_Init(function, label)
  - Calls the given function on game start, reload, or ui reload.
  - Label is an optional string printed to the debuglog (along with the specific error message) if the function fails.
  - Functions are called in order of registration, which can be controlled through intermod dependencies and the order of inclusion in ui.xml.
* Register_Require_With_Init(require_path, value, function)
  - Combination of Register_Require_Response and Register_OnLoad_Init, treating the require_path as the error label.

### Loading loose lua files

Pre-7.5, lua files loaded using ui.xml were missing general lua globals ("_G is nil" error). This API provides md cues to trigger a load of loose lua files. Protected UI mode needs to be disabled.

This functionality is retained for legacy support, but is not recommended for use in new mods.

To use, in an MD script add a cue that follows this template code:
```xml
<cue name="Load_Lua_Files" instantiate="true">
  <conditions>
  <event_ui_triggered screen="'Lua_Loader'" control="'Ready'" />
  </conditions>
  <actions>
  <raise_lua_event 
    name="'Lua_Loader.Load'" 
    param="'extensions.your_ext_name.your_lua_file_name'"/>
  </actions>
</cue>
```
The cue name may be anything. Replace "your_ext_name.your_lua_file_name" with the appropriate path to your lua file, without file extension. The lua file needs to be loose, not packed in a cat/dat. The file extension may be ".lua" or ".txt", where the latter may be needed if distributing through steam workshop. If editing the lua code, it can be updated in-game using "/reloadui" in the chat window.

When a loading is complete, a message is printed to the debuglog, and a ui signal is raised. The signal "control" field will be "Loaded " followed by the original param file path. This can be used to set up loading dependencies, so that one lua file only loads after a prior one.

Example dependency condition code:
```xml
<conditions>
  <event_ui_triggered screen="'Lua_Loader'" 
    control="'Loaded extensions.other_ext_name.other_lua_file_name'" />
</conditions>
```

# X4 Simple Menu API

This extension adds support for generating menus using mission director scripts in X4. A lua backend handles the details of interfacing with the x4 ui system.

Two types of menus are supported: options menus that are integrated with the standard x4 options, and standalone menus which will display immediately.

Additionally, a simplified interface is provided for adding options to an extension. These options are simple buttons and sliders that display in the main Extension Options menu.

### Usage

* Basic extension options
  - Call Register_Option with a name, default value, widget type, and callback.
  - Callback will receive the new value whenever the player changes the option.

* Standalone menu
  - Call Create_Menu to open a new menu, closing any others.
  - Fill the menu with rows and widgets, specifying callback cues.
  - Ca
```

### `source/kuertee_ui_extensions/README.md`

```text
UI Extensions and HUD
https://www.nexusmods.com/x4foundations/mods/552
Code: https://github.com/kuertee/x4-mod-ui-extensions
by kuertee.
Contributors: Alakeram, AlexandreTK, ChemODun, Damonya, DiCrash,
DrWhoKnows, DmytroK, Erixon, Faremen, Forleyor,
GoAhead78, HYLT2233, IALuir, Mycu, Orbika, Runekn, sticeIO.

Updates
=======
v9.0.0.19, 23 Oct 2026:
- New feature: by GoAhead78: New callbacks for new a mod.
- New feature: by Mycu: New callbacks for new a mod.

Protected UI Mode
=================
I've been playing with Protected UI Mode active with no adverse effects. I recommend that this mode is active and that the pop-up message about disabling it is ignored. Only deactivate this mode if you experience something unexpected.

Unfortunately, because of how this mod is built, disabling or enabling Protected UI Mode WHILE the mod is active will prevent the menus from reloading.

Either:
1. Activate/deactivate the mod and then restart the game at the operating system level. E.g. Task Manager, Steam, etc.
OR
2. Activate/deactivate Protected UI Mode BEFORE this mod is activated.

Instructions for players
========================
- Install UI Extensions as normal.
- Leave Protected UI Mode active. Ignore the pop-up message about disabling it.
- When extracting the package from github, ensure that the folder you install the mod to is: "(X4 game)/extensions/kuertee_ui_extensions/". Extracting the package from Nexus Mods will extract it to "(X4 game)/extensions/kuertee_ui_extensions/". But be sure it does anyway.
- Read the "CHANGES BUILT INTO THIS MOD (for players)" section.

Instructions for developers
===========================
Custom callbacks documentation by ChemODun: https://chemodun.github.io/x4/modding-support/ui-modding/uix-callbacks/. Thanks, ChemODun!

An overview on how to mod for UIX:
1. Install the mod as a player.
2. Copy the "(X4 game)/extensions/kuertee_ui_extensions/ui" folder into the "(X4 game)/ui" folder. This will overwrite UIX's XPL files into the game.
3. Launch the game with the "-prefersinglefiles" option. This will make the game use UIX XPL files instead of the base game's corresponding files that are in its cat/dat files.
4. Examine one of the callbacks in any of those XPL files. Search for "callback". Add any callback you need in any of the XPL files IN THE GAME FOLDER. If you need any callbacks added to a menu file, let me know (on Discord, Nexus or kuertee@gmail.com).
5. When done adding your callbacks, send me the changed XPL files.
6. I'll merge them with the master UIX files.
7. We'll coordinate release dates so that the new UIX mod with your callbacks is released near the time you release your mod.

For any questions, it's best to @ me on Egosoft's unofficial Discord modding channel: https://discord.gg/RzAGhcY

Read the CHANGES BUILT INTO THIS MOD sections.

Features
========
Modded Lua files with callbacks that allow more than one mod to change the same UI element.

Functionality that adds HUD elements to the Top Level Menu.

Allows other mods to create guidance missions (i.e. missiontype.guidance) that will be listed in the Guidance Missions tab. Also enables the Set Active and Set Inactive buttons in missions listed in the Guidance Missions tab. Examples of these are my mods:
- Loot mining.
- Ship scanner.
- Signal leak hunter - increasing range.
- Station scanner.
- Waypoint fields for deployments.

Mod effects
===========
This is a modder's resource/API. By itself, this mod does not affect the game.

Modders can use this API to mod the game's Lua files that and helps compatibility with other mods that also use this API.

Without this API, some Lua elements can only be modified by one mod. For example, my mods, "NPC reactions: NPC taxis" and "Teleport from transporter room" add buttons to the bottom of the Transporter Room panel. Because its Lua's display () function constructs its frame, table, rows, and content AND THEN immediately calls the frame:display () function, it is impossible for both mods to "rewrite" the display () function and expect both "rewrites" to work.

With this API, specifically its callbacks, it is possible.

CHANGES BUILT INTO THIS MOD (for players)
=========================================

Map Menu: Boarding Menu: Ship assignment tweaks
===============================================
Ensure that subordinates of selected ships acquire their immediate commander's boarding behaviour. In the base-game, when selecting ships, e.g. SHIP A, with subordinates AND those ships' fleet commander (i.e. THE COMMANDER of SHIP A) the subordinates of SHIP A sometimes acquired THE COMMANDER's behaviour (e.g. Maintain Distance) instead of SHIP A's behaviour (e.g. Target Turrets). This tweak allows the player to select wings of a fleet for separate boarding behaviour assignments without needing each wing to be in separate fleets. Note: also check out Kuda's new boarding behaviour changes (https://www.nexusmods.com/x4foundations/mods/839). e.g.: ships on attack orders durin
```

### `source/kuertee_ui_extensions/kuertee-ui-extensions-readme.txt`

```text
UI Extensions and HUD
https://www.nexusmods.com/x4foundations/mods/552
Code: https://github.com/kuertee/x4-mod-ui-extensions
by kuertee.
Contributors: Alakeram, AlexandreTK, ChemODun, Damonya, DiCrash,
DrWhoKnows, DmytroK, Erixon, Faremen, Forleyor,
GoAhead78, HYLT2233, IALuir, Mycu, Orbika, Runekn, sticeIO.

Updates
=======
v9.0.0.19, 23 Oct 2026:
- New feature: by GoAhead78: New callbacks for new a mod.
- New feature: by Mycu: New callbacks for new a mod.

Protected UI Mode
=================
I've been playing with Protected UI Mode active with no adverse effects. I recommend that this mode is active and that the pop-up message about disabling it is ignored. Only deactivate this mode if you experience something unexpected.

Unfortunately, because of how this mod is built, disabling or enabling Protected UI Mode WHILE the mod is active will prevent the menus from reloading.

Either:
1. Activate/deactivate the mod and then restart the game at the operating system level. E.g. Task Manager, Steam, etc.
OR
2. Activate/deactivate Protected UI Mode BEFORE this mod is activated.

Instructions for players
========================
- Install UI Extensions as normal.
- Leave Protected UI Mode active. Ignore the pop-up message about disabling it.
- When extracting the package from github, ensure that the folder you install the mod to is: "(X4 game)/extensions/kuertee_ui_extensions/". Extracting the package from Nexus Mods will extract it to "(X4 game)/extensions/kuertee_ui_extensions/". But be sure it does anyway.
- Read the "CHANGES BUILT INTO THIS MOD (for players)" section.

Instructions for developers
===========================
Custom callbacks documentation by ChemODun: https://chemodun.github.io/x4/modding-support/ui-modding/uix-callbacks/. Thanks, ChemODun!

An overview on how to mod for UIX:
1. Install the mod as a player.
2. Copy the "(X4 game)/extensions/kuertee_ui_extensions/ui" folder into the "(X4 game)/ui" folder. This will overwrite UIX's XPL files into the game.
3. Launch the game with the "-prefersinglefiles" option. This will make the game use UIX XPL files instead of the base game's corresponding files that are in its cat/dat files.
4. Examine one of the callbacks in any of those XPL files. Search for "callback". Add any callback you need in any of the XPL files IN THE GAME FOLDER. If you need any callbacks added to a menu file, let me know (on Discord, Nexus or kuertee@gmail.com).
5. When done adding your callbacks, send me the changed XPL files.
6. I'll merge them with the master UIX files.
7. We'll coordinate release dates so that the new UIX mod with your callbacks is released near the time you release your mod.

For any questions, it's best to @ me on Egosoft's unofficial Discord modding channel: https://discord.gg/RzAGhcY

Read the CHANGES BUILT INTO THIS MOD sections.

Features
========
Modded Lua files with callbacks that allow more than one mod to change the same UI element.

Functionality that adds HUD elements to the Top Level Menu.

Allows other mods to create guidance missions (i.e. missiontype.guidance) that will be listed in the Guidance Missions tab. Also enables the Set Active and Set Inactive buttons in missions listed in the Guidance Missions tab. Examples of these are my mods:
- Loot mining.
- Ship scanner.
- Signal leak hunter - increasing range.
- Station scanner.
- Waypoint fields for deployments.

Mod effects
===========
This is a modder's resource/API. By itself, this mod does not affect the game.

Modders can use this API to mod the game's Lua files that and helps compatibility with other mods that also use this API.

Without this API, some Lua elements can only be modified by one mod. For example, my mods, "NPC reactions: NPC taxis" and "Teleport from transporter room" add buttons to the bottom of the Transporter Room panel. Because its Lua's display () function constructs its frame, table, rows, and content AND THEN immediately calls the frame:display () function, it is impossible for both mods to "rewrite" the display () function and expect both "rewrites" to work.

With this API, specifically its callbacks, it is possible.

CHANGES BUILT INTO THIS MOD (for players)
=========================================

Map Menu: Boarding Menu: Ship assignment tweaks
===============================================
Ensure that subordinates of selected ships acquire their immediate commander's boarding behaviour. In the base-game, when selecting ships, e.g. SHIP A, with subordinates AND those ships' fleet commander (i.e. THE COMMANDER of SHIP A) the subordinates of SHIP A sometimes acquired THE COMMANDER's behaviour (e.g. Maintain Distance) instead of SHIP A's behaviour (e.g. Target Turrets). This tweak allows the player to select wings of a fleet for separate boarding behaviour assignments without needing each wing to be in separate fleets. Note: also check out Kuda's new boarding behaviour changes (https://www.nexusmods.com/x4foundations/mods/839). e.g.: ships on attack orders durin
```
