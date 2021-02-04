# Tuesday February 2nd

* Active Directory Domäner
* Organisational Units
* Domänkontrollanter
* Användarkonton
* LDAP Destinguage Name
* ADadminitration med PowerShell
* Datorkonton
* If time permits: Administrativa rättigheter I AD
* Gemensam övning: Skapa OU:n
* Gemensam övning: Skapa och administrera konton med GUI
* Gemensam övning: Skapa OU med DSADD-kommando
* Gemensam övning: Skapa OU med PowerShell
* Lab: Skapa konton med hjälp av mallar
* NTFS-Test

<!-- begin -->

# DN - Distinguished Names
* Also called LDAP-names
* Sökväg till objekt i Active Directory
* 3 delar
  1. DC = DOmain Component
  2. OU = Organisational Unit
  3. CN = Common Name
* I AD används endast dessa tre komponenter
* ...

# Relative Distinguished Names
* Har inget med Relative Distinguished Names i Novell att göra 
  <!-- what is Novell? -->
* Är alltid delen längst till vänster av ett distinguished name
* ...


# Delar i Active Directory
* Domäner
* Organisational Unit
* Träd
* Skog
* Siter
* Trust
* Global Catalog

## Domäner
* Logisk gruppering, ej fysisk
* Security Boundary:
  - När vi sätter rättigheter och behövrigheter gäller de i en domän, ej i hela trädet
* Replikeringsområde
  - 

## OU
* Organisational Units
* Kan används för att bygga upp hierarkiska strukturer inom domäner
* Grupperar objekt
* Skapar system för rättigheter
* Administrativ kontroll kan delegeras för olika OU till olika "lokala" administratörer
* Skall användaren inte längre ha ett OU's administratör lyfts han ur OU:t

## OU-design
OU:strukturen ska baseras på
* Administration av domänens delar
* Inläsning av GPO:er
  - Men hänsyn ska i viss mån även tas till
* Ordning och reda

## Träd och skogar
* Tree & Forest
* Ett träd är flera domäner med sammanhängande namn
* En skog är flera domäner eller träd som ej har sammanhängande namn

## Trust
* Trusten är det som ger möjlighet att gå mellan domäner
* Två typer av truster i Windows NT5 & NT6
1. Two Way Transitive Trust
  - Skapad default mellan parent- och childdomäner i ett träd samt mellan parent-domäner i en skog
2. One Way Non-transitive Trust
   - För NT4 Kompatibilitet

## Global Catalog
* Indexerar alla objekten i AD så att man slipper Hoppa runt till massa DC i skogen då man söker objekt
* Ungerfär som sökmotor på Internet
* Tar ej med alla attribut
* Vilka som skall indexeras bestäms i schemat (som editeras i schema master)
* Default finns en Global Catalog Server men vettigt att ha flera ...


# DC - Domain Controler
* *Servers that host the AD DS database (Ntds.dit) and SYSVOL*
* Best practices:
  * Availability:
    - At least two domain controllers in a domain
  * Security:
    - RODC and BitLocker
* *Multiple Master Replication*
* Flera DC i en domän är multiple master vilket innebär att de uppdaterar varandra (replikering)
* Needs access to a DNS, usually DNS is also run on the DC.

## Installing a Domain Controller
1. Add the AD DS Role
2. Promote server to Domain Controller

## Upgrading a Domain Controller
- Do not.
- 

# AD DS is composed of both logical and physical components
1. Logical components
   * Partitions - part of database that affects replication
   * Schema
   * Domains
   * Domain Trees
   * FOrest
   * Sites = physical placement (ip)
   * OUs - *Location in AD*
   * Containers (similar to OU, but not GPO)
2. Physical components
   * Domain Controllers (Has a copy of the AD database, Accepts login tickets)
   * Data stores (Database file ntds.dit)
   * Global catalog servers (Search Engine to AD)
   * RODCs (Bantad installation av domänkontrollant)

* Any domain controller can authenticate any sign-in (kerberos) anywhere in the domain

<!-- break -->

# AD Accounts
Gives an identity that is valid in the whole domain (including the whole forest and domains with trust)
Accounts are identified by SID (Security-ID)
Contains information

# Distinguished Name
CN=Server1,OU=Servers,DC=jultomten,DC=nu <!-- Datorkonto -->
"CN=Donald Trump,OU=User,OU=NYC,DC=jultomten,DC=nu" <!-- User Account -->
OU=User,OU=NYC,DC=jultomten,DC=nu <!-- OU -->


## Namnregler
UPN inloggningsnamnet tex erik@jultomten.nu måste vara unkit i hela skogen (hela miljön)
SAM Account Name tex JULTOMTEN\ERIK måste vara unkit i hela Domänen
Full Name, Förnamn [Initial] Efternamn, måste vara unikt i sitt OU. Full Name + OU = Distinguished Name

