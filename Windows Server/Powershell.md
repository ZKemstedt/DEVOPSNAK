# Powershell Syntax

## syntax
```
Verb-Noun -parameter | Verb-Noun -parameter ...
```
notes:
    There is no space between verb and noun but there is a dash.
    There are exclusions to the verb-noun rule, such as `new`.

#### example:
```powershell
Get-ADUser -Filter * -SearchBase "OU=Test,DC=brodin,DC=local" | Set-ADUser -Department "Hej"
```

## Use the pipe character(|) to pass a list of objects to a cmdlet for further proessing
```powershell
Get-ADUser -Filter {company -notlike "*"} | Set-ADUser -Company "A. Datum"
Get-ADUser -Filter {lastlogondate -lt "January 1, 2012"} | Disable-ADAccount
Get-Content C:\users.txt | Disable-ADAccount
```

cmdlet

## Querying Objects with Windows PowerShell
```powershell
# Show all the properties for a user account:
Get-ADUser -Name "Administrator" -Properties *

# Show all the user accounts in the Marketing OU and all its subcontainers:
Get-ADUser -Filter * -SearchBase "ou=Marketing,dc=adatum,dc=....
```
```powershell
# Parameter                 # Description
-SearchBase                 # Defines the AD DS path to begin searching
-SearchScope                # Defines at what level below the SearchBase a search should be performed
-ResultSetSize              # ...
-Properties                 #
-Filter                     #
-LDAPFilter                 #

# Description of operators
-eq         # Equal to
-ne         # Not equal to
-lt         # Less than
-le         # Less or equal to
-gt         # Greater than
-ge         # Greater or equal to
-like       # Uses wildcards for pattern matching
```

## Powershell Bulk Import
```powershell
# 1.
$users = import-csv -path "D:/vm/userlist.csv"
# 2.
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
    new-aduser -name "$displayname" -displayname "$displayname" -samaccountname $sam -description "$description" -accountpassword (convertto-securestring $password -asplaintext -force) -enabled $true -path "$ou" -changepasswordatlogin $false -passwordneverexpires $true -server domain.loc
}
# 1. Reads the csv file
# 2. Define rows as users
# 3. Define and assign variables
# 4. Create account
```

## Variables
```powershell
$Firstname = Read-Host "First name?"
$Familyname = Read-Host "Last name?"
$Fullname = $Firstname + " " + $Familyname
$PWD = Read-Host "pwd?"
$OU = Read-Host "city?"
$Path = "OU=Anvandare,OU=" + $OU + ",DC=jultomten,DC=nu"
$SAM = $Firstname
$SAM = $SAM -Replace "å","a"
$SAM = $SAM -Replace "ä","a"
$SAM = $SAM -Replace "ö","o"
$UPN = $SAM + "@jultomten.nu"
New-ADUser -Name "$Fullname" -GivenName $Firstname -Surname $Familyname -SamAccountName $SAM -UserPrincipalName $UPN -Description Kung -Path $Path -accountPassword (ConvertTo-SecureString -AsPlainText "$PWD" -Force) -passThru | Enable-ADAccount
```

## Working with csv files
```powershell
$users=Import-CSV -LiteralPath "C:\users.cvs"
foreach ($user in $users) {
    Write-Host "The first name is: " $user.FirstName
}
```

## Create a differential disk
```powershell
Import-Module Hyper-V
New-VHD "D:\VM\Lab\Surfdator.vhd" -ParentPath "D:\VM\Moderdiskar\ModerdiskW2019.vhd"
```

## Create a virtual Machine
```powershell
new-vhd -dynamic D:\VM\lab\Extradisk.vhdx -controllertype SCSI -controllernumber 0
```

## Take a disk online, intitialize and format it.
```powershell
get-disk # list the disks and their numbers, this instruction assumes the newly created Extradisk has the id 1
get-disk -number 1 | initialize-disk # note: will initialize as GPT by default
get-disk -number 1 | new-partition -usemaximmsize | format-volume -confirm:$false -filesystem NTFS -newfilesystemlabel PowerShellTest
get-partition # list the partiions and their numbers, by default a GPT disk has the GPT table on partition 1 and the normal at partition 2
set-partition -disknumber 1 - partitionnumber 2 -newdriveletter G
```

## Virtual Machine resource metering
```powershell
import-module hyper-v
enable-vmresourcemetering Surfdator
measure-vm Surfdator
```


