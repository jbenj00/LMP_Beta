# GUNPIRE Logistics — M0 Diagnostic Extension

**Status:** Read-only diagnostic baseline. **Not a working logistics dispatcher.**
**Target:** X4: Foundations 9.00. Galaxy Trader 1.0.4 integration observations.

## Install

1. Back up your save. Extract this folder so X4 sees `extensions/GUNPIRE_Logistics/content.xml` and `extensions/GUNPIRE_Logistics/md/LMP_M0_Diagnostics.xml`. Rename the extracted folder to `GUNPIRE_Logistics` if desired; keep `content.xml` at its root.
2. Enable the extension in X4.
3. For debug text, start X4 with the launch arguments specified by the project roadmap: `-logfile lmp_debug.log -debug scripts` (the 9.00 runtime behavior of these arguments is **not verified** here).
4. Find the output log under your X4 personal-data directory. If the expected file is absent, locate the actual script log before launching the monitor.
5. Run `powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\LMP_Monitor.ps1 -LogPath 'C:\FULL\PATH\TO\lmp_debug.log'` from the extension folder to open two filtered windows.

## Expected diagnostic lines

- `[LMP][INFO] M0 diagnostics active` — load/startup observer began.
- `[LMP][INFO] Galaxy Trader detected` — GT's protected-order ID registry was present at observer startup; absence at this instant is **not proof GT failed to load**.
- `[LMP][GT-EVENT] PAUSED ...` — observed GT's own `GT_Ship_Order_Paused` signal.
- `[LMP][GT-EVENT] ABORTED ...` — observed GT's own `GT_Ship_Order_Aborted` signal; this is not automatically evidence a GUNPIRE action caused it.

## What this build does not do

- Does **not** select or enroll any ships, change default behavior, create/cancel orders, reserve stock, or run a trade.
- Does **not** alter `global.$GT_Ships`, `global.$GT_Pilots`, GT scripts, or their event handlers.
- Does **not** protect GT from cleanup on a future behavior swap; the current source shows GT can treat replacement as permanent removal.
- Does **not** guarantee a working PowerShell monitor or X4 logging until tested in the game.

## Major compatibility finding (GT 1.0.4 source)

GT's `order.trade.galaxytrader.xml` `on_abort` path explicitly classifies a different default order as *PERMANENT REMOVAL* (around lines 9093–9102). The GT bridge then watches GT default-order removal; the core's cleanup path can dismantle GT equipment mod tracking. Even the `GT_Ship_Order_Paused` handler preserves pilot XP while removing/rebuilding parts of `global.$GT_Ships` and clearing some training/modification state.

**M1 gate:** Do not install automatic GT takeover until a cooperative handoff or verifiably lossless return path exists for each supported GT type, including fleet subordinates. Changing GT to another default order without that proof is unsafe.

## Verification performed outside the game

See `VALIDATION.txt` for XML parsing/XSD checks and limitations.
MD script syntax acceptance does **not** establish runtime behavior or X4 9.00 compatibility in the installed environment.
