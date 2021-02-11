# Monday February 8th

* Folder Redierction
* GPO:n två delar
* Dokumentation av GPO:er
* Säkerhetsfiltrering av GPO:er
* GPO-backup (mycket kort)
* Programinstallation med GPO:er
* Preference inställningar i GPO:er
* Felsökning av GPO:er
* Säkerhetsinställningar med GPO:er
* Auditing = Säkerhetsloggning med GPO
* User Right Assignment
* Gemensamma övning: Koppla skript med GPO:er
* Lab: Folder Redierction
* Gemensamma övning: Säkerhetsfiltrering så att endast en utvald grupp läser in GPO
* Gemensamma övning: Säkerhetsfiltrering så att en utvald grupp inte läser in GPO
* Gemensamma övning: Preferenceinställningar för Strömschema
* Gemensamma övning: Mappning med preferenceinställningar som vilkorats till grupper med hjälp av Item Level Targeting
* Gemensamma övning: Felsöka GPO:er med GPRESULT och Group Policy Results
* Gemensam övning: Automatisera skrivarinstallation med hjälp av GPO:er som konfigureras från Print Management
* Demo: Programinstallation med GPO 

<!-- recap -->

### Byte av Group Scope
Man är tvungen att mellanlande på Universal

### The Microsoft way för grupper
A Användare och/eller datorer
G Globala grupper
DL Domänlokala grupper
P Permissions

### Manager till en grupp
Kan ge begränsade adminrättigheter på gruppen

### Delegera kontroll i AD:t
Skapar lokala OU-administratörer

### Full Kontroll till ett OU
Man måste öppna Advanced

### Länkning av PGO:er
Viktigt att lära sig arvet i OU-strukturen
Sist inläst GPO vinner = Närmast användaren (eller datorn)
Användarinställningar läses in beroended på användarkontots placering
Datorinställningar läses in beroende på datorkontots placering
Undvik att länka till siter om det ej är nödvändigt

### Skript-koppling med GPO
Själva skriptkoden kommer att replikeras till SYSVOL på domänens all DC

### Kunskapsprogression
1. **Hur** man utför handgreppen/administrationen
2. **Vad** som händer, hur tekniken fungerar
3. **Varför**, eller när, ska man implementera detta? Vilken kundnytta ger olika lösningar?

<!-- begin -->

## Storage of User Documents and Data

### Home Computer
- A Challenge
- Difficult to take backups
- Danger of stolen computers
- Issues if user change device

### Central Storage of document
- Home Folders
  - Old setup
  - Requires that users save documents at the correct location
- Roaming profiles
  - Old setup
  - Everything is copied to client at login
  - Local workspace
  - On logout all changes are copied back to server
  - Performance heavy, slow login/logouts
  - Not very compatible with mobile devices, aborted logout syncs lead to corrupted profiles.
- Folder Redirection *Recommended*
  * Work is redirected to the fileserver through shortcuts.
  * Mobile Devices: Default is to enable local caching of users files that sync continously. 
  - Configured by GPO (Always use Basic!!).
    - Creator/Owner: Full Control
    - System: Full Control
    - [optional] Administrators: Full Control
    - Chosen Users: Create Folder + Traverse Folder

## SYSVOL ...
see related lab

## Application installation with GPO
- Free
- Uses .msi files
- Easy to configure
  1. aquire .msi file
  2. create a shared map for the file
  3. create/configure GPO
- No reporting
- No inventory
- Does not suit Large Applications
- No scheduling
- Installation can be bound to user or computer (do not bind to both)
  - User: Auto install at login
  - Computer: Auto install at boot

## Print Queue and Print Device
* Print Device - The physical printer
* Printer - Installation = Printer
* The Service is called Spool Service

# GPO - Two parts 
1. GPO Container
   * Located in AD, NTDS.dit
2. GPO Template
  * Located in SYSVOL

# Documenting GPOs
