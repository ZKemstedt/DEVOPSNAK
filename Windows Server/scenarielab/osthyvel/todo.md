[x] Designa och planera er miljö på papper, använd gärna A3-papper. Se till att ni får ett unikt domännamn
[x] Sätt upp era servrar. Börja med att skapa en mapp för varje VM, lägg inga filer direkt i VM-foldern.
[x] Konfigurera dem med de fasta IP-adresser er grupp fått tilldelade, ange 10.6.66.1 som gateway
[x] Byt namn på er första DC och starta om
[x] Promota er första DC
[x] Joina era andra servrar till domänen och byt samtidigt namn på den
[ ] Promota eventuell ytterligare DC
[x] Skapa OU-strukturen
[x] Skapa grupper
[x] Importera eller skapa användarkonton
[x] Populera grupper
[x] Skapa utdelningar och sätt korrekta rättigheter
[x] Skapa och konfigurera önskade GPO:er
[x] Sätt upp två klientdatorer och joina dem till domänen
[x] Testa inställningar och rättigheter
[x] Sammanställ dokumentationen, glöm ej GPO-rapport i HTML-format som man lättast fixar med PowerShell
[ ] Fakturera


<!-- TODO -->


# Documentation
- NAS1
  - Printers
  - Shared Folders
- Klient?

# Invoice (wip)



<!-- Done recently -->
# Namnpekning mot en annan grupp

## Restricted Groups (GPO)

# Skrivare

# Delade Foldrar + Mappning

# GPO - Group Policy Objects
1. Background Images
  - Brie Background Image
  - Gouda Background Image
  - Mozzarella Background Image
  - Emmentaler Background Image
  - Chevre Background Image
  - Background -> Namn Nummer och Mail till deras Admin

<!-- not for local admins -->
2. Restrictions
  - Only Domain Admins can log in to NAS1 / DC1
  - Disable CMD, but not for Admins / IT
  - Heavy restrictions, but not for Brie / Admins / IT

3. Folder Redirection + Shared Folder Mappnings

4. Application Installations
  - Google Chrome
  - Notepad ++

5. Skrivare
  - Deploy [ost]Printer on Computer Basis

6. Restricted Groups
  - Local Administrator Group = Domain Admins + [ost]ITPersonal + lokal admin


# Notes 
,Brie ,Chevre ,Emmentaler ,Gouda ,Mozzarella

* ludgar07 -> Mozzarella IT
* salami37 -> Emmentaler IT
* andahm03 -> Chevre IT
* Filrem60 -> Gouda IT
* Ramher70 -> Gouda
* Johgar14 -> Brie IT

* Klient W10    -> Gouda
* Klient 2 W10  -> Brie

Anvandare: .csv
Script: txt
Dokumentation: pdf
Faktura: pdf
GPO rapport: html


<!-- hardware links -->
# DC
https://www.dell.com/sv-se/work/shop/servrar-lagring-och-natverk/smart-value-poweredge-t640-server-for-large-smb-customers/spd/poweredge-t640/pet6409a?configurationid=bb8d6df9-cfbe-4b85-b351-fd03c0bfa3e7
# NAS
https://www.supermicro.com/en/products/system/4U/6048/SSG-6048R-E1CR36N.cfm
# Extra (disks)
https://www.komplett.se/product/898949/datorutrustning/lagring/haarddisk/haarddisk-35/seagate-barracuda-1tb-35-hdd
