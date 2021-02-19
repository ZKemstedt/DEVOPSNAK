# Server Name & Type
### Filserver
### NAS1

# Description
## *Vad* <!-- Virtuell -->
## *Var*
## *Komponenter*
* Main Disk
  - Type: Differential
  - Location: C:\VM\NAS1\NAS1.vhdx
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
* Virtual Switch: Klassrumsnät
* Additional Disks:
  - *disks*

# Configuration
* OS: Windows Server 2019 Datacenter Evaluation
* Build: 17763.rs5_release.180914-1434
* Display Resolution: 1024x768
* Network Configuration:
  - IP adress 10.6.66.166
  - Subnet mask: 255.0.0.0
  - Default gateway 10.6.68.1
  - Preferred DNS server: 10.6.66.165
  - Alternate DNS server: *None*
<!-- * Windows Update Configuration -->
<!-- * Remote Access Configuration -->
<!-- * Local Configuration -->


# Roles and Features
*todo*




<!--                                                                -->
<!--                                                                -->
<!--                                                                -->





### The Microsoft way
Users and Computers -> Globala grupper
Permissions -> Domänlokala grupper

 *DL* = Domänklokal Grupp
 *G* = Global Grupp
 *U* = Universal Grupp

## Anvandare
- Ledning *DL*
  - [ost]Ledning *G*
    <!-- KontorsChef, ButiksChef, FabriksChef -->
- Personal *DL*
  - [ost]Personal *G*
  - ITPersonal *DL*
    - [ost]ITPersonal *G*
  - HRPersonal *DL*
    - [ost]HRPersonal *G*
  - PRPersonal *DL*
    <!-- - [ost]PRPersonal -->
  - Ekonomer *DL*
    <!-- - [ost]Ekonomer -->
  - Provsmakare *DL*
    - [ost]Provsmakare *G*
  - ButiksPersonal *DL*
    - [ost]ButiksPersonal *G*
  - FabriksPersonal *DL*
    - [ost]FabriksPersonal *G*
- Externa Sammarbetare *DL*
  - [ExterntGruppNamn] *G*
- Konsulter *G* = Global Grupp
- Praktikanter *G* = Global Grupp

## Datorer
  - Kontor *DL*
    - [ost]Kontor *G*
  - Fabrik *DL*
    - [ost]Fabrik *G*
  - Butik *DL*
    <!-- - [ost]Butik -->
 
<!--
Angående PRPersonal, Ekonomer och Butik som DL grupp:
Prioritering av konsekvent design över Konvention.
-->

<!--
Angående Konsulter och Praktikanter
Globala Deny Grupper.
-->

