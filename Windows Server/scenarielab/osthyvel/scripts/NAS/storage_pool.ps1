# Static
$nas1 = "10.6.66.166"
$dc1 = "10.6.66.165"
$target = $nas1

$pw = ConvertTo-SecureString "Password123" -AsPlainText -Force
$usr = "osthyvel\administrator"

$cred = New-Object System.Management.Automation.PSCredential ($usr, $pw)

# 
#   Begin Session
# 
$session = New-PSSession -computername $target -credential $cred

Invoke-Command -Session $session -ScriptBlock
{    
    $AnvandareDiskar = Get-StorageSubSystem -FriendlyName "Windows Storage*" `
    | Get-PhysicalDisk -CanPool $True `
    | Where-Object {[int]$_.DeviceID -le 12} `
    | Sort-Object {[int]$_.DeviceID}
        New-StoragePool -FriendlyName "AnvandareDiskPool" -StorageSubsystemFriendlyName "Windows Storage*" `
        -PhysicalDisks $AnvandareDiskar `
        -ResiliencySettingNameDefault Mirror `
        -ProvisioningTypeDefault Thin `
        -Verbose `
    | New-VirtualDisk -FriendlyName "AnvandareDisk" -Size 6TB `
    | Initialize-Disk -PassThru `
    | New-Partition -AssignDriveLetter -UseMaximumSize `
    | Format-Volume

    $DelatDiskar = Get-StorageSubSystem -FriendlyName "Windows Storage*" `
    | Get-PhysicalDisk -CanPool $True `
    | Where-Object {[int]$_.DeviceID -gt 12} `
    | Sort-Object {[int]$_.DeviceID}
    New-StoragePool -FriendlyName "DelatDiskPool" -StorageSubsystemFriendlyName "Windows Storage*" `
        -PhysicalDisks $DelatDiskar `
        -ResiliencySettingNameDefault Mirror `
        -ProvisioningTypeDefault Thin `
        -Verbose `
    | New-VirtualDisk -FriendlyName "DelatDisk" -Size 10TB `
    | Initialize-Disk -PassThru `
    | New-Partition -AssignDriveLetter -UseMaximumSize `
    | Format-Volume
}

#
#   End Session
#
Remove-PSSession -Name $session