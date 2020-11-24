use T618
go


-- 1.   Skapa en transaktion. Gör en uppdatering på innehållet i valfri tabell.
begin tran
update Employee
set Salary = '10'

select * from Employee


-- 2.   Skapa en savepoint. Gör en uppdatering till. Skapa en ny savepoint.
--      Gör ytterligare en uppdatering. Kontrollera uppdateringarna.
save tran stage1
update Employee
set Commission = '50'

select * from Employee

save tran stage2
update Employee
set Firstname = 'Jibbzter'

select * from Employee


-- 3.   Backa uppdateringen tillbaks till den andra savepointen. Kontrollera värdena.
--      Gå tillbaks till första savepointen. Vad händer med andra savepointen?
rollback stage2
select * from Employee

rollback stage1
select * from Employee

rollback tran


-- 4.   Gör om övning 1-2 men gör en commit efter andra uppdateringen. 
--      Försök gå tillbaka till savepoint-läget.
begin tran
insert into Employee
values (1234, 'SchulkyS', 'Schulky', 'Ekonomi', 1001, getdate(), 40000, 2000, 10, 's', 's')

save tran stage1
insert into Employee
values (1001, 'Rereveh', 'Zephyland', 'Analytiker', 1001, getdate(), 70000, 15000, 10, 's', 's')

commit tran

rollback stage1

select * from Employee


-- 5.   Ta bort alla rader i någon tabell. Boot:a om datorn (simulera krasch).
--      Logga in mot databasen på nytt och kontrollera den tömda tabellen.

-- Assuming to begin transaction before dropping table.
begin tran
drop table Employee
-- *DB Server restart*
-- Table exists. (due to auto-rollback)


-- 6.   Starta två fönster i Management Studio. Starta transaktioner i bägge sessionerna.
--      Ta bort innehållet i tabellen ISHOCKEY i den ena sessionen.
--      Växla till session 2 och sök ut alla rader i ISHOCKEY-tabellen. Bekräfta
--      raderingen i den första sessionen med Commit och gör om sökningen i session 2.

-- 7.   Starta transaktioner i bägge sessionerna. Ta bort en rad i FOTBOLL-tabellen i
--      session 1. Försök uppdatera samma rad i session 2.
--      Gå tillbaks till session 1 och bekräfta borttagningen.

-- Överkurs
-- 8.   Starta två fönster i Management Studio. Starta en transaktion och ta bort alla
--      rader från tabellen Employee i den ena sessionen. Växla till det andra fönstret
--      och sök ut alla rader i Employee-tabellen. 
    --      Fönster 2 borde inte få något resultat.


-- 9.   Starta ytterligare ett fönster i Management Studio. Skriv sp_lock för att se 
--      låsningen. I kolumnen spid ser man vilken koppling som låser, exempelvis SPID 52.
	--      ”Döda” den process som orsakar låsningen genom KILL 52.
    --      Alla transaktioner i en dödad process kommer att rullas tillbaks. 
	--      Fönster 2 borde få sitt resultat nu.
