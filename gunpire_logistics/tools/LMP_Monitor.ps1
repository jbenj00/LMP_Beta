<#
GUNPIRE M0 dual-console log viewer. Read-only.
Usage:
  powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\LMP_Monitor.ps1 -LogPath 'C:\path\to\lmp_debug.log'
Open X4 with -logfile lmp_debug.log -debug scripts (check game debug output first).
#>
param(
  [Parameter(Mandatory=$true)][string]$LogPath,
  [ValidateSet('Launcher','Issues','Operations')][string]$View = 'Launcher'
)
$ErrorActionPreference = 'Stop'
$resolved = [IO.Path]::GetFullPath($LogPath)
if (!(Test-Path -LiteralPath $resolved -PathType Leaf)) {
  throw "Log file does not exist: $resolved. Start X4 with script logging, then supply the full path."
}
if ($View -eq 'Launcher') {
  $safeScript = $PSCommandPath.Replace("'", "''")
  $safeLog = $resolved.Replace("'", "''")
  foreach ($mode in @('Issues','Operations')) {
    $cmd = "& '$safeScript' -LogPath '$safeLog' -View '$mode'"
    $encoded = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($cmd))
    Start-Process -FilePath 'powershell.exe' -ArgumentList @('-NoProfile','-NoExit','-ExecutionPolicy','Bypass','-EncodedCommand',$encoded) | Out-Null
  }
  return
}
$Host.UI.RawUI.WindowTitle = "GUNPIRE LMP M0 - $View"
Write-Host "Monitoring $resolved ($View). Press Ctrl+C to stop." -ForegroundColor Cyan
$pattern = if ($View -eq 'Issues') { '\[LMP\]\[(?:INFO|WARN|ERROR|GT-EVENT)\]' } else { '\[LMP\]\[(?:INFO|OP|TRACE|GT-EVENT)\]' }
Get-Content -LiteralPath $resolved -Tail 100 -Wait | ForEach-Object {
  if ($_ -match $pattern) {
    if ($_ -match '\[WARN\]|\[ERROR\]|ABORTED') { Write-Host $_ -ForegroundColor Yellow }
    else { Write-Host $_ }
  }
}
