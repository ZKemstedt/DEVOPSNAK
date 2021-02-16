
# OU Setup

## Create OUs
```powershell
$ostar = @("Brie", "Chevre", "Gouda", "Emmentaler", "Mozzarella")
foreach ($ost in $ostar)
{
    New-ADOrganizationalUnit -Name $ost -Path "DC=osthyvel,DC=se" -ProtectedFromAccidentalDeletion $false
    New-ADOrganizationalUnit -Name "Anvandare" -Path "OU=$ost,DC=osthyvel,DC=se" -ProtectedFromAccidentalDeletion $false
    New-ADOrganizationalUnit -Name "Datorer" -Path "OU=$ost,DC=osthyvel,DC=se" -ProtectedFromAccidentalDeletion $false
    New-ADOrganizationalUnit -Name "Grupper" -Path "OU=$ost,DC=osthyvel,DC=se" -ProtectedFromAccidentalDeletion $false
}
```

# Remove OUs
```powershell
$ostar = @("Brie", "Chevre", "Gouda", "Emmentaler", "Mozzarella")
foreach ($ost in $ostar)
{
    Remove-ADOrganizationalUnit -Identity "OU=$ost,DC=osthyvel,DC=se" -Recursive -Confirm:$false
}
```