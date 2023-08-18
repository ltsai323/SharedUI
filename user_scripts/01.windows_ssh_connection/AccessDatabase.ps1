$REMOTE_USER = "ntuuser"


$env:DISPLAY = "localhost:0"
$width = 80
$height = 6

$host.UI.RawUI.WindowSize = New-Object System.Management.Automation.Host.Size($width,$height)


$X11Program = "C:\Program Files\VcXsrv\xlaunch.exe"

if (Test-Path -Path $X11Program -PathType Leaf) {
  Start-Process $X11Program
} else {
  Write-Host '--------------------------- WARNING ---------------------------------------------'
  Write-Host '-- Default X11 program not found in computer, you need to execute it manually. --'
  Write-Host '---------------------------------------------------------------------------------'
}
ssh -Y $REMOTE_USER@hep10.phys.ntu.edu.tw 'source gotoworkspace/01.SharedUI.sh && python /data1/ltsai/workspace/git/SharedUI/mainUI.py'
Pause
