# Thursday Febuary 4th
* Administrativa rättigheter i Active Directory
* GPO:er
* GPO-inställningar
* ADMX/ADM-filer och Administartive Templates
* Central Storage
* GPO-inläsningsordning
* Windowsbrandväggen
* Gemensam övning: Sätta och kontrollera administrativa rättigheter i Active Directory
* Gemensam övning: Skapa, länka och editera GPO:er
* Gemensam övning: Central Storage
* Demo: GPO-inställningar för Windows 10, officepaketer och Firefox
* Gemensamma övning: Skapa brandväggsregler med GPO:er
* Utmaning: Skapa ett skript för gruppadministration


## Groups
Group scope determines what members can be assigned to the group and
how the group can be used (join other groups, be assigned permissions)

* Local Group 
  * Only usable locally, not in a domain.
* Global Group
  * Usually rather long
  * Best to read at login, and not elsewhere
  * Members can be Users
* Domain Local Group
  * Can have members from all domains
  * Members can be Users, Computers, Global- Universal- and Domain Local Groups
  * Can only give permissions in it's own domain
  * Sometimes called Resource Group
  * Usually only single Global Groups as members, sometimes Universal Groups
* Universal Group
  * Can have members from all domains from **one** forest
  * Cannot be used over *External trust* - Does not work outside of it's forest
  * Members can be Users, Computers, Global- and Universal groups
  * Recommended to only use when no other solutions are available

Globala grupper har användare som medlemmar och listan medlemmar kan bli ganska lång.
Bra om globala grupper kontrolleras vid inloggning så filserver slipper hämta listan.

Eftersom Domänlokala grupper bara har andra grupper så blir deras listor över medlemmar
väldigt kort och går snabbt att läsas (=hämtas) över nätverk.

Globala gruppen cashas aldrig på en resursserver medan de
DomänLokala grupperna cashas under själva accessen.

### "The Microsoft way" A G D L P
#### **A**nvändare **G**lobalgrupp **D**omän**L**okalgrupp **P**ermissions


## Groups vs OU
* Groups
  - Groups have membership
  - An entity can be a member of max 1000 groups
  - Group Members 
* OU
  - An OU is a **location** in the AD-structure
  - A GPO can be linked to an OU
  - An Administrator can be delegated to an OU


## GPO - Group Policy
GPO is a list of settings
In Azure-AD there's an alternative Intune
* GPO's user-settings are read by the users who's accounts are in the OU which the GPO is linked to.
* GPO's computer-settings are read by the users who's accounts are in the OU which the GPO is linked to.

### GPO read-order - *last read wins!*
1. Local computer registry
2. Local computer policy
3. Site GPO (very rarely used)
4. Domain GPO
5. OU-GPO
6. Under-OU-GPO

