use T618
go

-- 1. Skapa en tabell med namnet anst, som är en kopia på tabellen Employee.
select *
into anst
from Employee

-- 2. Ändra kolumnen Lastname i tabellen anst till VARCHAR(50).
--    Skriv kommandot SP_HELP anst för att se tabellens egenskaper.
alter table anst
alter column Lastname varchar(50)

sp_help anst

-- 3. Lägg till en ny kolumn manager CHAR(1) i tabellen anst.  
alter table anst
add Manager char(1) 

-- 4. Uppdatera tabellen anst och sätt ett ’Y’ i manager-kolumnen 
--    för de som har några anställda underställda sig.
update anst
set Manager = 'Y'
where EmpId in (
    select ManagerId
    from anst
)

-- 5. Uppdatera tabellen anst och sätt ett ’N’ i kolumnen manager
--    för dem som inte har några anställda underställda sig.
update anst
set Manager = 'N'
where Manager is null

-- 6. Ändra kolumnen manager i tabellen anst till NOT NULL.
alter table anst
alter column Manager char(1) not null

-- 7. Skapa en kopia av tabellen Department, namnge den avd.
select *
into avd
from Department

-- 8. Skapa en primärnyckel på kolumnen DeptID i tabellen avd.
alter table avd
add primary key (DeptId)

sp_help avd

-- Överkurs
-- 9. Skapa en referential integrity constraint mellan tabellerna anst och avd,
--    alltså en främmande nyckel på kolumnen deptno i anst. Namnge den FK_DEPTNUM

alter table anst
add constraint FK_DEPTNUM foreign key (DeptId)
references avd(DeptId)

-- 10. Ta bort avdelning 10 från tabellen avd. Gick det?
delete from avd
where DeptId = 10
-- Nope, error :)

-- 11. Ta bort constraint FK_DEPTNUM. 
alter table anst
drop constraint FK_DEPTNUM

-- 12. Pröva nu att ta bort avdelning 10 från avd. Är detta bra? Diskutera!
delete from anst
where DeptId = 10
-- generally speaking it's good that improptu deletion is blocked

-- 13. Ta bort tabellerna avd och anst.
drop table avd, anst

-- 14. Skapa en tabell; Totalinfo. Den ska innehålla alla kolumner från
--     Employee och Department. Ta endast med DeptID en gång. 
--     Vilka fördelar respektive nackdelar finns det med denna enda
--     tabell i stället för två tabeller Employee och Department?
select 
    EmpID,
    Firstname,
    Lastname,
    Job,
    ManagerID,
    HireDate,
    Salary,
    Commission,
    e.DeptId,
    DeptName,
    [Location]
into Totalinfo
from Employee e
join Department d
on e.DeptID = d.DeptID

-- 15. Ta bort Totalinfo.
drop table Totalinfo
