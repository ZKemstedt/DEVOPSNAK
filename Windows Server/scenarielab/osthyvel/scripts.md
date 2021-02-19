# VM Setup

# Extra disks for Filserver
```powershell
for ($i=1; $i -lt 7; $i++) {
    $disk = "C:\VM\NAS1\RAIDDisk" + $i + ".vhdx"
    # This script assumes the newly created disk has the id $i (1-7)
    get-disk -number $i | initialize-disk # note: will initialize as GPT by default
    get-disk -number $i | new-partition -usemaximumsize | format-volume -confirm:$false -filesystem NTFS -newfilesystemlabel PowerShellTest
}
```


# DC Setup

## Promote to DC -> new Forest
```powershell
#
# Windows PowerShell script for AD DS Deployment
#
Import-Module ADDSDeployment
Install-ADDSForest `
-CreateDnsDelegation:$false `
-DatabasePath "C:\Windows\NTDS" `
-DomainMode "WinThreshold" `
-DomainName "osthyvel.se" `
-DomainNetbiosName "OSTHYVEL" `
-ForestMode "WinThreshold" `
-InstallDns:$true `
-LogPath "C:\Winwods\NTDS" `
-NoRebootOnCompletion: $false `
-SysvolPath "C:\Windows\SYSVOL" `
-Force:$true
```


# OU Setup

## Create OUs
```powershell
$ostar = @("Brie", "Chevre", "Gouda", "Emmentaler", "Mozzarella")
foreach ($ost in $ostar) {
    New-ADOrganizationalUnit -Name $ost -Path "DC=osthyvel,DC=se" -ProtectedFromAccidentalDeletion $false
    New-ADOrganizationalUnit -Name "Anvandare" -Path "OU=$ost,DC=osthyvel,DC=se" -ProtectedFromAccidentalDeletion $false
    New-ADOrganizationalUnit -Name "Datorer" -Path "OU=$ost,DC=osthyvel,DC=se" -ProtectedFromAccidentalDeletion $false
    New-ADOrganizationalUnit -Name "Grupper" -Path "OU=$ost,DC=osthyvel,DC=se" -ProtectedFromAccidentalDeletion $false
}
```

# Remove OUs
```powershell
$ostar = @("Brie", "Chevre", "Gouda", "Emmentaler", "Mozzarella")
foreach ($ost in $ostar) {
    Remove-ADOrganizationalUnit -Identity "OU=$ost,DC=osthyvel,DC=se" -Recursive -Confirm:$false
}
```

# Create Groups
```powershell
$groups = @("ITPersonal", "HRPersonal", "PRPersonal", "Ekonomer", "Provsmakare", "ButiksPersonal", "FabriksPersonal")
foreach ($group in $groups) {
    New-ADGroup
    -Name "$Group"
    -GroupCategory Security
    -GroupScope Global
    -DisplayName ""
    -Path ""
    -Description ""
}


```


## Powershell Bulk Import
```powershell
$users = import-csv -path "D:/vm/userlist.csv"
foreach ($user in $users) {
    # 3.
    $firstname = $user.'Firstname'
    $lastname = $user.'Lastname'
    $displayname = $firstname + " " + $lastname
    $ou = $user.'OU'
    $sam = $user.'SAM'
    $upn = $firstname + "." + $lastname + "@" + $user.'Maildomain'
    # strongly recommended to first create SAM, manipulate it to hande åäö etc, and then create UPN from SAM.
    $pwd = $user.'Password'
    # 4. 
    New-ADUser `
    -name "$displayname" `
    -displayname "$displayname" `
    -samaccountname $sam `
    -description "$description" `
    -accountpassword (convertto-securestring $password -asplaintext -force) `
    -enabled $true `
    -path "$ou" `
    -changepasswordatlogin $false `
    -passwordneverexpires $true `
    -server domain.loc
}

New-ADUser -Name "$Fullname"
-GivenName $Firstname
-Surname $Familyname
-SamAccountName $SAM
-UserPrincipalName $UPN
-Description Kung
-Path $Path
-accountPassword (ConvertTo-SecureString -AsPlainText "$PWD" -Force)
-passThru | Enable-ADAccount
```
