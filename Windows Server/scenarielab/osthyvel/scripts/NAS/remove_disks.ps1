# Remove Disks From VM
$nas = "NAS1"

$eject1 = $true
$delete1 = $true
$count1 = 12

$eject2 = $true
$delete2 = $true
$count2 = 20

# Anvandare
for ($i = 0; $i -lt $count1; $i++) {
    if ($eject1) {
        Remove-VMHardDiskDrive -VMName $nas -ControllerType SCSI -ControllerNumber 0 -ControllerLocation $i
    }
    if ($delete1) {
        $j = $i + 1
        Get-Item -Path "C:\VM\NAS1\AnvandareDisk$j.vhdx" | Remove-Item 
    }
}

# Delat
for ($i = $count1; $i -lt $count1+$count2; $i++) {
    if ($eject2) {
        Remove-VMHardDiskDrive -VMName $nas -ControllerType SCSI -ControllerNumber 0 -ControllerLocation $i
    }
}
for ($i = 0; $i -lt $count2; $i++) {
    if ($delete2) {
        $j = $i + 1
        Get-Item -Path "C:\VM\NAS1\DelatDisk$j.vhdx" | Remove-Item 
    }
}