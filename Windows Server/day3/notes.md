# Thursday January 28th

* Diskar
* Virtuella hårddiskar
* Lokala diskar, SAN och NAS (Se till att förstå skillnaderna)
* Filserverkoncept och användning
* Klient - Server-relation
* Utdelning av foldrar
* Sharerättigheter
* RAID
* Lab: Skapa och testa RAID med GUI
* Lab: Flytta en virtuell disk mellan värddator och VM
* Lab: Administrera diskar med GUI
* Lab: Administrera diskar med Diskpart
* Lab: Administrera diskar med PowerShell

<!-- begin -->

# Diskar

## MBR
- up to 2TB per partition
- max 4 partitions

## GPT
- requires uefi bios
- certain vm cannot boot from GPT

## GUID Partition Table

## Microsoft Disk Tools
- Disk Management (GUI)
  - Manages both basic and dynamik disks, volumes and partitions on both local and remote computer
  - easy to create new partitions
- Diskpart (diskmgmt.msc)
  - scriptable
  - cannot be run remotely
- PowerShell 3.0
  - built in commands for disk management
  - scriptable
  - can be run remotely


## Dynamic Disks

## Mirrored - RAID 1
Disk space is allocated once and used simultaneously
- 50% overhead
- 2 disks
## Spanned
Disk space is added and used sequentially
## Striped - RAID 0
Disk space is allocaated once and used equally across every physical disk in the striped set
- 2-32 dynamic disks
- uses same about on all disks
- disks become 1 volume
- cannot change size of volume

## Raid
*Raid 0*: Utspridd skrivning, ingen driftsäkerhet
*Raid 1*: spegling, 1 disk overhead, ej snabbare skrivning
Raid 4: Utspridd skrivning, en paritetsdisk, 1 disk overhead
*Raid 5*: Utspridd skrivning, roterande paritet, 1 disk overhead
Raid 6: Utspridd skrivning, dubbel paritet, minst 4 diskar, 2 diskar overhead
Raid 10, 01 och 15: Spegling av Raid 0 och 5, mycket overhead men bättre säkerhet och bättre prestanda vid diskfel


## Ändring av storlek på volymer
Man bör ta backupp på diskar som skall byta storlek.


# NAS SAN DAS

## NAS - Network Attached Storage
En filserver, oftast används förkortningen för enklare filservrar.
Används Hemma, små företag och backup-lagring.

## DAS - Direct Attached Storage
Direktanslutna hårddiskar i en servern som använder diskarna.
Ofta anänvds uttrycket JBOD Just a Bunch Of Disks.

## SAN - Storage Area Network
Oftast flera devices som tillsammans delar ut hårddiskar till andra datorer,
i praktiken är det alltid servrar som använder hårdiskarna som ett SAN delar ut.
OBS: Ej utdelning av foldrar eller filar utan hela hårddiskar som egentligen heter 
LUN (Logical Unit Number).
Servrar som kopplar upp sig mot ett SAN upplever LUN:en som likala diskar.
Det är SAN-klienterna(=servrar) som äger och formaterar diskarna.
Det är som att ha en mycket lång kabel till sina hårddiskar som råkar sitta inne i en annan dator.


Sharing
## Basic Sharing
DO NOT
## Advanced Sharing
YES
## Public Folders
Not recommended for controlled environments
## CMD / PS