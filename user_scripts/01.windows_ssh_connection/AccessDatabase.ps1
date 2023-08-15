$REMOTE_USER = "ntuuser"


$env:DISPLAY = "localhost:0"
$width = 60
$height = 3

$host.UI.RawUI.WindowSize = New-Object System.Management.Automation.Host.Size($width,$height)

ssh -Y $REMOTE_USER@hep10.phys.ntu.edu.tw 'source gotoworkspace/01.SharedUI.sh && python /data1/ltsai/workspace/git/SharedUI/mainUI.py'
# Pause