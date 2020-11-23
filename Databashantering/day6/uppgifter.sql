use T618
go

-- Innan vi börjar på övningarna i detta kapitel ska vi starta en transaktion.
-- Exekvera följande sats:
begin transaction
-- Nu kan vi få tillbaka allting som det var vid den tidpunkten vi startade transaktionen,
-- ifall vi skulle göra något fel som ställer till det för de fortsatta övningarna


-- 1. Lägg till en rad med följande värden i tabellen COUNTRY
	-- CountryId: BRA, Country: Brasilien,Population: 140000000, Government: Demokrati
insert into country
    (CountryId, Country, Population, Government)
values
    ('BRA', 'Brasilien', 140000000, 'Demokrati')

-- 2. Lägg till Rio de Janeiro i CITY-tabellen. Rio de Janeiro har 10 miljoner invånare.

-- 3. Lägg till Umeå (40000 invånare), Norrköping (115000 invånare) och Örebro (90000 invånare) utan att ange kolumnnamn i Insert-satsen.

-- 4. Byt ut den svenska beteckningen (COUNTRYID) mot SVE i COUNTRY- och CITY-tabellerna.

-- 5. Det finns ett land och en stad där invånarantalet saknas. Uppdatera dessa kolumner med lämpliga (eller påhittade) värden.

-- 6. Uppdatera befolkningsmängden för alla länder och städer med 100 procent.

-- Överkurs
-- 7. Lägg till alla städer från Customers-tabellen i City-tabellen.
--    Utgå från att alla städer som finns i Customers-tabellen finns i Sverige.
--    Ange inget invånarantal.

-- 8. Ta bort de rader som lades till ovan.

-- 9. Lägg till städer från Customers-tabellen i City-tabellen, men se till att du inte lägger in dubbletter.
--    Undvik också att skapa dubbletter (d v s lägg inte in en stad som redan finns).

-- 10. Sätt alla befolkningstal i Country-tabellen så att summan av befolkningen
--     i de olika städerna utgör hela befolkningen i landet,
--     d v s SUM(City.Population) = Country.Population för varje land. 
update country
set population = (
    select sum(isnull(population, 0))
    from city
    where country.CountryId = cite.CountryId
    group by countryid
)

-- 11. Uppdatera lönen för alla anställda som arbetar i Stockholm med 30 %.
update Employee
set Salary = Salary * 1.3
where DeptId in 
(
    select DeptID from Department
    where location = 'Stockholm'
)

-- 12. Uppdatera STEVE MILLER, så namnet är med inledande versal och resten gemener, d v s Steve Miller.
update Employee set Firstname = 'Steve', lastname = 'Miller' where EmpId = 7934

-- 13. Lägg till en anställd i Employee-tabellen. Valfritt namn, jobb, lön och avdelning.
insert Employee (EmpId, Firstname, Lastname, Job, Salary, DeptId)
values (1234, 'Mikael', 'Lönnroos', 'CEO', 10000, 50)


-- 14. Ta bort alla rader i Department-tabellen. Går det? Borde det gå? Vad händer i så fall med raderna i Employee-tabellen?


-- Till sist ska vi återställa tabellerna.
-- Det gör vi med:
rollback transaction
-- I och med detta är alla ändringar som vi gjort i de senaste övningarna borttagna och övningarna går att göra på nytt.
-- Mer om transaktioner (Begin, Savepoint, Commit och Rollback) går vi igenom lite senare.
