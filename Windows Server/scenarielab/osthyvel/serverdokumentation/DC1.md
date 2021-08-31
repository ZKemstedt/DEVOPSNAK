# Primär Domänkontrollant - DC1
<!-- https://www.dell.com/sv-se/work/shop/servrar-lagring-och-natverk/smart-value-poweredge-t640-server-for-large-smb-customers/spd/poweredge-t640/pet6409a?configurationid=b76a51cd-460c-4811-86b9-aa9579ca3bfe -->

<!-- # Description
## Virtual Machine Running on 
## C003
## Virtuella Komponenter:
* Main Disk
  - Type: Differential
  - Location: C:\VM\DC1\DC1.vhdx
  - Parent Location: C:\VM\Moderdiskar\ModerdiskW2019.vhd
  - Size: 40GB
* Generation: 1
* RAM
  - Dynamic: True
  - MinimumBytes: 800MB
  - StartupBytes: 1500MB 
  - MaximumBytes: 4GB
  - Priority: 80
  - Buffer: 25
* Processor
  - Count: 2
* Virtual Switch: Klassrumsnät -->

## Location
* Brie Server Hall, Tower 1

## Hardware
* RAM: 4x 14GB 3200MT/s
* Processor: 2x Intel Xeon Silver 4214R 2.5GHz
* Hard Drives: 1x 960GB SSD 2.5"

# Configuration
* OS: Windows Server 2019 Datacenter Evaluation
* Build: 17763.rs5_release.180914-1434
* Display Resolution: 1024x768
* Network Configuration:
  - IP adress 10.6.66.165
  - Subnet mask: 255.0.0.0
  - Default gateway 10.6.68.1
  - Preferred DNS server: 127.0.0.1
  - Alternate DNS server: 8.8.8.8
* Windows Update Configuration:
  - Download updates only, using Windows Update
* Remote Access Configuration:
  - Remote Management: Enabled
  - Remote Desktop: Disabled

# Roles and Features
* DNS
* AD DS

# DNS
* Zone name: osthyvel.se
* Static Records:
  - dc1.osthyvel.se         10.6.66.165
* Forwarders:
  - unConditional           8.8.8.8
* Stub-Zone:
  - luddan.se               10.6.66.160

# AD DS
* Domain Name: osthyvel.se
* NetBIOS Domain Name: OSTHYVEL
* DSRM password: *Hidden*

## OU-Structure:

![OU-Structure](OU-Structure.png "Image")

## OU-Delegated Control:
### Brie
* BrieITPersonal -> Brie.osthyvel.se
  - Create, delete and manage user accounts
  - Reset user passwords and force password change at next logon
  - Read all luser information
  - Create, delete and manage groups
  - Modify the membership of a group
* BrieHRPersonal -> Anvandare.Brie.osthyvel.se
  - Create, delete and manage user accounts
  - Reset user passwords and force password change at next logon
  - Read all luser information
  - Modify the membership of a group

### Chevre
* ChevreITPersonal -> Chevre.osthyvel.se
  - Create, delete and manage user accounts
  - Reset user passwords and force password change at next logon
  - Read all luser information
  - Create, delete and manage groups
  - Modify the membership of a group
* ChevreHRPersonal -> Anvandare.Chevre.osthyvel.se
  - Create, delete and manage user accounts
  - Reset user passwords and force password change at next logon
  - Read all luser information
  - Modify the membership of a group

### Emmentaler
* EmmentalerITPersonal -> Emmentaler.osthyvel.se
  - Create, delete and manage user accounts
  - Reset user passwords and force password change at next logon
  - Read all luser information
  - Create, delete and manage groups
  - Modify the membership of a group
* EmmentalerHRPersonal -> Anvandare.Emmentaler.osthyvel.se
  - Create, delete and manage user accounts
  - Reset user passwords and force password change at next logon
  - Read all luser information
  - Modify the membership of a group

### Gouda
* GoudaITPersonal -> Gouda.osthyvel.se
  - Create, delete and manage user accounts
  - Reset user passwords and force password change at next logon
  - Read all luser information
  - Create, delete and manage groups
  - Modify the membership of a group
* GoudaHRPersonal -> Anvandare.Gouda.osthyvel.se
  - Create, delete and manage user accounts
  - Reset user passwords and force password change at next logon
  - Read all luser information
  - Modify the membership of a group

### Mozzarella
* MozzarellaITPersonal -> Mozzarella.osthyvel.se
  - Create, delete and manage user accounts
  - Reset user passwords and force password change at next logon
  - Read all luser information
  - Create, delete and manage groups
  - Modify the membership of a group
* MozzarellaHRPersonal -> Anvandare.Mozzarella.osthyvel.se
  - Create, delete and manage user accounts
  - Reset user passwords and force password change at next logon
  - Read all luser information
  - Modify the membership of a group

## Groups
[DL]: Domain Local Group
[G]: Global Group

* [DL] BriePersonal -> Grupper.Brie.osthyvel.se
  - [G] BrieITPersonal
  - [G] BrieHRPersonal
  - [G] BriePRPersonal
  - [G] BrieButiksPersonal
  - [G] BrieFabriksPersonal
  - [G] BrieKontorsPersonal
  - [G] BrieEkonom
  - [G] BrieProvsmakare
* [DL] ChevrePersonal -> Grupper.Chevre.osthyvel.se
  - [G] ChevreITPersonal
  - [G] ChevreHRPersonal
  - [G] ChevrePRPersonal
  - [G] ChevreButiksPersonal
  - [G] ChevreFabriksPersonal
  - [G] ChevreKontorsPersonal
  - [G] ChevreEkonom
  - [G] ChevreProvsmakare
* [DL] EmmentalerPersonal -> Grupper.Emmentaler.osthyvel.se
  - [G] EmmentalerITPersonal
  - [G] EmmentalerHRPersonal
  - [G] EmmentalerPRPersonal
  - [G] EmmentalerButiksPersonal
  - [G] EmmentalerFabriksPersonal
  - [G] EmmentalerKontorsPersonal
  - [G] EmmentalerEkonom
  - [G] EmmentalerProvsmakare
* [DL] GoudaPersonal -> Grupper.Gouda.osthyvel.se
  - [G] GoudaITPersonal
  - [G] GoudaHRPersonal
  - [G] GoudaPRPersonal
  - [G] GoudaButiksPersonal
  - [G] GoudaFabriksPersonal
  - [G] GoudaKontorsPersonal
  - [G] GoudaEkonom
  - [G] GoudaProvsmakare
* [DL] MozzarellaPersonal -> Grupper.Mozzarella.osthyvel.se
  - [G] MozzarellaITPersonal
  - [G] MozzarellaHRPersonal
  - [G] MozzarellaPRPersonal
  - [G] MozzarellaButiksPersonal
  - [G] MozzarellaFabriksPersonal
  - [G] MozzarellaKontorsPersonal
  - [G] MozzarellaEkonom
  - [G] MozzarellaProvsmakare
* [DL] ITPersonal -> Resursgrupper.osthyvel.se
  - BrieITPersonal
  - ChevreITPersonal
  - EmmentalerITPersonal
  - GoduaITPersonal
  - MozzarellaITPersonal
* [DL] HRPersonal -> Resursgrupper.osthyvel.se
  - BrieHRPersonal
  - ChevreHRPersonal
  - EmmentalerHRPersonal
  - GoduaHRPersonal
  - MozzarellaHRPersonal
* [DL] PRPersonal -> Resursgrupper.osthyvel.se
  - BriePRPersonal
  - ChevrePRPersonal
  - EmmentalerPRPersonal
  - GoduaPRPersonal
  - MozzarellaPRPersonal
* [DL] ButiksPersonal -> Resursgrupper.osthyvel.se
  - BrieButiksPersonal
  - ChevreButiksPersonal
  - EmmentalerButiksPersonal
  - GoduaButiksPersonal
  - MozzarellaButiksPersonal
* [DL] FabriksPersonal -> Resursgrupper.osthyvel.se
  - BrieFabriksPersonal
  - ChevreFabriksPersonal
  - EmmentalerFabriksPersonal
  - GoduaFabriksPersonal
  - MozzarellaFabriksPersonal
* [DL] KontorsPersonal -> Resursgrupper.osthyvel.se
  - BrieKontorsPersonal
  - ChevreKontorsPersonal
  - EmmentalerKontorsPersonal
  - GoduaKontorsPersonal
  - MozzarellaKontorsPersonal
* [DL] Ekonom -> Resursgrupper.osthyvel.se
  - BrieEkonom
  - ChevreEkonom
  - EmmentalerEkonom
  - GoduaEkonom
  - MozzarellaEkonom
* [DL] Provsmakare -> Resursgrupper.osthyvel.se
  - BrieProvsmakare
  - ChevreProvsmakare
  - EmmentalerProvsmakare
  - GoduaProvsmakare
  - MozzarellaProvsmakare
* [DL] Personal -> Resursgrupper.osthyvel.se
  - BriePersonal
  - ChevrePersonal
  - EmmentalerPersonal
  - GoudaPersonal
  - MozzarellaPersonal

## Group Policy Objects (GPO)
See GPOReportsAll.html
