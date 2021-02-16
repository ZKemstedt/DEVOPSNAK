# Serverdokumentation

<!-- Section 1 -->
## Servertyp och Namn
Domänkontrollant
DC3Sthlm

## Fysisk Beskrivning
Virtuell
Serverhall 2
rad 4
8GB Ram
2 cpu
3 diskar a 2TB

## Konfiguration för hosten
OS inkl version
Nätnverkskonfiguration
upplösning
uppdaterings-inställningar
remote desktop
lokala inställningar

## Lista installerade roller
* DHCP
* DNS
* ADDS
* Fileserver
* Ev. installerade program (only big and important ones)

<!-- Section 2 -->
<!-- Each installed Role becomes a new Header -->

## DHCP
conflict detection 2
scope [kontoret]
10.2.26.1
...

## DNS
Conditional forwarding ...
Zon AD-int
...

## ADDS
* Domän namn
* OU struktur
* Namnstandard
* Grupper
  * mindre domäner för en lista
  * Större domäner beskriver
* GPO lista (inga inställningar)
  * hänvisa till html raporten

## File Server
För varje utdelning
* lokal path
* nätverkspath
* share permissions
* ntfs permissions
### Exempel:
  * F:\gemensamt
  * \\DC3Sthlm\Gemensamn$
  * Share Permissions:
    * AuthenticatedUser FC
  * NTFS Permissions:
    * System FC
    * Administrators FC
    * Creator/Owner FC (Subfolders and files)
    * Domain Users Read
    * Stockholm Users Read & Write
