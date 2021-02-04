# Wednesday Febuary 3th

* NTFS-dugga 2
* Datorkontons lösenord
* Administrera många konton med GUI
* Kontoadminitration med PowerShell
* Bulkimport med csvde
* Kort om LDIFDE
* Importera användare från fil med PowerShell
* Grupper Kort intro: Vad man har dem till och att de har en SID
* Grupper vs OU
* Group scope
* Manager till en grupp
* Hur man lägger grupper i andra grupper
* Om vi hinner: Administrativa rättigheter i Active Directory

<!-- begin -->

csvde -i -f C:\temp\text.csv

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

SAM vs UPN

Det finns två olika inloggningsnamn i Windows Active Directory (fr.o.m Windows 2000)

SAM eller SAMAccountName = Äldre standard som är NT4-kompatibel
NACKADEMIN\ERIK.BRODIN eller JULTOMTEN\MARTIN

UPN eller UserPrincipalName inkluderar @ och fullständigt domännamn erik.brodin@nackademin.local martin@jultomten.nu

? Hur tolkas om man bara skriver erik.brodin eller martin?
Svar: Olika i olika verktyg och program => Se till att alltid ha samma UPN och SAM
(Samma i betydelsen samma 'användardel' av inloggningsnamnet)


Reverta innan vi börjar importera konton.
När man revertar miljön


# Grupper
* Group Score
* Group Type
  * Security (Only Security groups in this course)
    - "Vanliga grupper"
    - har en sid
    - kan tilldellas rättigheter
    - (Även en security grupp kan mail enablas)
  * Distribution
    - endast för exchange server
    - har ingen sid