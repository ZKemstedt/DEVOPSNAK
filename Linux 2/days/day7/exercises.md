## Ex 1
* Tänk er att ni skall skapa driftsmiljö med
  ett publikt webbinterface, ett antal moduler skrivna
  i Java som utför större beräkningar, och data i
  en relationsdatabas.
* Hur förderlar ni detta på olika servrar? Vad
  kommer vara viktigt i miljön på respektive
  server? Vad bör vara öppet och stängt i
  kommunikationen mellan servrarna?

```md
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
```

## Ex 2
* Installera en LAMP-server.
  - Vilka paket behöver ni?
* Skapa en MySQL-databas med en tabell users,
  stoppa in något data, och gör ett enkelt PHP-
  exempel som läser från den för att testa.
    - mysqlconnect.php att utgå från
* Testa att ni kan köra PHP genom Apache och få
  kontakt med MySQL
```php
# --- mysqlconnect.php ---
<?php
$servername = "localhost"; $db = "testdb1"; $user = "dbuser1"; $pwd = "losen1";

function getAllUsers(){
   global $servername, $db, $user, $pwd;     
   $conn = new mysqli($servername, $user, $pwd, $db);  // Create connection
   if ($conn->connect_error) { // Check connection
        die("Connection failed: " . $conn->connect_error);
   }
   // simple sql, as there are no params here
   $sql = "select * from users";
   $result = $conn->query($sql);
   if ($result->num_rows > 0) {  // get data from each row
     $res = [];
     while($row = $result->fetch_assoc()) {
    array_push($res, $row);
    }
    } else {
        $res = [];
    }
    $conn->close();
    return $res;
}

$allUsers=getAllUsers();
echo '<pre>'; print_r($allUsers); echo '</pre>';
?>
```

```bash
# need these packages
sudo apt install -y apache2 mysql-server php libapache2-mod-php php-mysql

# start service
sudo systemctl restart apache2

# Setup DB
sudo mysql
> create database testdb1;
> create user dbuser1 identified by "pw";
> grant all privileges on testdb1.* to "dbuser1";
> use testdb1;
> create table users (id int auto_increment primary key, first_name varchar(60), last_name varchar(80), email varchar(50));
> insert into users (first_name, last_name, email) values ('Olof', 'Palme', 'ololol@sverige.com');
> exit;

# Test php -> DB
php ./mysqlconnect.php

# Test php -> apache -> DB
cp mysqlconnect.php /var/www/html/
http://127.0.0.1/mysqlconnect.php
```

## Ex 3
* Gör nu skript som automatiserar installation av
  LAMP enligt vad vi gjorde i förra övningen.

```bash
# --- install_lamp.sh ---
#!/bin/bash

apt-get update -y
apt-get install -y apache2 mysql-server php libapache2-mod-php php-mysql

systemctl restart apache2

mysql <testdb1.sql

cp mysqlconnect.php /var/ww/html/
```
```sql
-- --- testdb1.sql ---
create database if not exists testdb1;

create user dbuser1 identified by "pw";
grant all privileges on testdb1.* to 'dbuser1';

use testdb1;
create table if not exists users (id int auto_increment
primary key, first_name varchar(60), last_name varchar(80),
email varchar(50));

insert into users (first_name, last_name, email) values ('Olof', 'Palme', 'ololol@sverige.com');
insert into users (first_name, last_name, email) values ('Findus', 'Pettersson', 'borttappad@skogen.nu');
```

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


