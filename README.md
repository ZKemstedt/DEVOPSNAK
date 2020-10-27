# devops20_python_slutuppgift

## Betygskriterier

### För Godkänd (G) krävs att studenten får godkänt på följande kriterier

* Studenten kan utföra socketsprogrammering i Python
* Studenten kan skapa klientapplikationer som kommunicerar med en server via sockets
* Studenten kan skapa enhetstester och kan applicera testdriven utveckling
* Studenten förstår hur versionshantering fungerar i utvecklingsprocessen och kan
  använda något verktyg för versionshantering

### För Väl Godkänd (VG) krävs att studenten får godkänt på samtliga G – respektive VG-kriterier

* Studenten kan självständigt utveckla och optimera klientapplikationer
  som kommunicerar med en server via sockets
* Studenten visar god förmåga att applicera testdriven utveckling för att
  kvalitetssäkra applikationer eller kod som ska deployas

## Instruktioner

### Regler

* Slutuppgiften är enskild
* Det är ok att fråga lärare och varandra generella frågor.
* Ni ska skriva er egen kod, om ni använder er av kodbitar från webben
  t.ex. stackoverflow så måste ni ange källa.
* Ni ansvarar för att Betygskriterierna är uppfyllda, kolla er kursplan.

### Att arbete i Github och Git

* Gör en fork av detta repository
* OBS ni ska alltså clona eran fork, inte detta repo.
* När ni gör en fork så kommer alla få rätt att se innehållet. så innan ni börjar arbeta,
  ta bort alla utom mig från: settings -> Manage Access
* Skapa en branch som ni arbetar i.

### Inlämning 3/11 23:59

* Gör en Pull Request mot eran egen main i eran fork, senast Tisdag, 3/11 23:59
* Dubbelkolla att programmet fungerar, ni kan t.ex. clona repot i en ny folder och testa er branch där.
* Om ni har missat något finns en extra chans på seminariet att visa vad ni kan, var förberedda.
* Seminariet äger rum i små grupper Torsdag 5/11.


## Filserver

I denna uppgift ska du bygga en filserver. Filservern håller ett register över filer.

#### Filserver - Krav G

* Du kan fråga servern om vilka filer den har
* Du kan fråga servern hur stor en fil är
* Du kan be servern ta bort en fil
* Du skriver något enhetstest

#### Filserver - Krav VG

* Ditt protokoll klarar av text samt att hämta och ladda upp filer
* Du kan skicka en uppmaning till alla klienter att en ny fil finns
* Din kod är testbar och har rimliga enhetstester
* Klient och server arbetar på ett icke blockerade vis (trådar eller annan lösning)
* Klient och server arbetar på ett effektivt sätt och hanterar flera klienter
