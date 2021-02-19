# Lab 1 - Wednesday February 3rd
## Group Administration

### Steg 1 Skapa grupp och utdelning
1. Logga in på DC
2. Öppna t.ex Active Directory Users and Computer 
3. Gå in i OU:t Resursgrupper
4. Skapa en Domänlokal grupp som heter DC_Grupplab_modify
5. Gör gruppen Stockholmsanvändare till medlem i den nya gruppen
6. Öppna filhanteraren på DC ,  gå till C: 
7. Högerklicka och skapa en ny mapp som heter Grupplab
8. Tag properties på den nya mappen Grupplab
9. Gå in på Sharefliken, klicka Advanced Sharing, klicka i Share this folder, Öppna Permissions, ta bort Everyone och ge gruppen Authenticated users share-rättigheten full kontroll och stäng två gånger
10. Gå in på Securityfliken, klicka Edit och addera den nya gruppen DC_Grupplab_modify och ge den rättigheten Modify
11. Klicka sedan på Advance när du är på Securityfliken, klicka på knappen Disable Inheritance och välj Convert
12. Deleta raden Users Special (troligen näst längst ned), om det finns andra rader för Users som ger mer än read skall du deleta även dessa
13. Stäng genom att klicka OK två gånger
14. Stäng Propertiesfönstret

### Steg 2 Testa rättigheterna
1. Logga in på en dator som INTE är domänkontrollant med kontot Erik Brodin (Inloggning erik och lösenord Linux4Ever)
2. Accessa mappen \\dc\grupplaboch försök skapa en fil där
3. Stäng fönstret mot \\dc\grupplab men logga inte ut

### Steg 3 Uppdatera gruppmedlemsskap
1. Logga in på DC
2. Öppna t.ex Active Directory Users and Computer 
3. Gör kontot Erik Brodin till medlem i gruppen Stockholmsanvändare
4. Gå tillbaks till den andra datorn och igen accessa mappen \\dc\grupplab och försök skapa en fil där
5. Stäng fönstret mot \\dc\grupplab

### Steg 4 Uppdatera användarens Kerberosbiljett
1. Logga av och logga in igen med kontot Erik Brodin på datorn som inte var domänkontrollant 
2. Accessa mappen \\dc\grupplab och försök skapa en fil där
