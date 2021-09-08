## Ex 1
* Tänk er att ni skall skapa driftsmiljö med
  ett publikt webbinterface, ett antal moduler skrivna
  i Java som utför större beräkningar, och data i
  en relationsdatabas.

* Hur förderlar ni detta på olika servrar? Vad
  kommer vara viktigt i miljön på respektive
  server? Vad bör vara öppet och stängt i
  kommunikationen mellan servrarna?

´´´md
* Server 1: Webbserver, med program för detta (t ex Apache) och
  presentationslogik. Typiskt på DMZ, öppet för http / https utifrån
  och för ssh från internt nät för administration, samt tillåta trafik in
  till internt nät till moduler på server 2.
* Server 2: JVM och beräkningsmodulerna. Typiskt på internt nät.
  Öppet för trafik till modulerna från server 1 och för trafik till
  databasen på server 3, samt ssh för administration Ingen direkt
  Internet-koppling.
* Server 3: Databasmotor (t ex MySQL), databas med relevant
  data. Öppen för trafik till databasen från server 2, samt ssh för
  administration. Alternativt: Databas i databaskluster på servrar
  för det ändamålet. Ingen direkt Internet-koppling.
´´´



## Ex 2
* Installera en LAMP-server.
  - Vilka paket behöver ni?
* Skapa en MySQL-databas med en tabell users,
  stoppa in något data, och göe ett enkelt PHP-
  exempel som läser från den för att testa.
    - mysqlconnect.php att utgå från
* Testa att ni kan köra PHP genom Apache och få
  kontakt med MySQL
* Paket:
  apache2
  mysql-server
  php libapache2-mod-php php-mysql
* Starta och kör
  systemctl restart apache2
* Testa av Apache + PHP genom Apache
* Skapa databas och stoppa in data



## Ex 3
* Gör nu skript som automatiserar installation av
  LAMP enligt vad vi gjorde i förra övningen.



## Ex 4
* Tänk er att ni har en LAMP-server för en
  webbsite där man kan söka fram uppgifter om
  beslut på en förenings årsmöten genom åren,
  samt tillhörande databas.
* Gör en riskanalys för driften av denna server
  - Vad kan hända?
  - Hur troligt är det?
  - Hur allvarligt är det?
  - Åtgärder för höga riskvärden

| Risk | Sannolikhet | Konsekvens | Riskvärde | Åtgärder |
|------|-------------|------------|-----------|----------|
|      |             |            |           |          |
|      |             |            |           |          |
|      |             |            |           |          |
|      |             |            |           |          |
|      |             |            |           |          |


## Ex 5
* Om vi nu tänker oss vår LAMP-server, vad är
  relevant att ta backup på där? 


## Ex 6
* Implementera nu backup av er MySQL-databas
  i form av regelbunden dump av data till något
  lämpligt ställe på disk (låtsas för sakens skull att
  det är en ansluten extern disk som kommer
  finnas kvar om databasen krachsar)
* Implementera också att mer än 7 dagar gamla
  dumpar resas bort automatiskt en gång per
  dygn
  - tips: `find`


