use T618
go

-- 1. Skapa en tabell med namnet ANST, som är en kopia på tabellen Employee.
select *
into ANST
from Employee

-- 2. Ändra kolumnen Lastname i tabellen ANST till VARCHAR(50).
--    Skriv kommandot SP_HELP ANST för att se tabellens egenskaper.
alter table ANST
alter column Lastname varchar(50)
-- sp_help ANST

-- 3. Lägg till en ny kolumn MANAGER CHAR(1) i tabellen ANST.  
alter table ANST
add MANAGER char(1) 

-- 4. Uppdatera tabellen ANST och sätt ett ’Y’ i MANAGER-kolumnen 
--    för de som har några anställda underställda sig.
update ANST
set MANAGER = 'Y'
where EmpId in (
    select ManagerId
    from ANST
)

-- 5. Uppdatera tabellen ANST och sätt ett ’N’ i kolumnen MANAGER
--    för dem som inte har några anställda underställda sig.
update ANST
set MANAGER = 'N'
where not EmpId in (
    select ManagerId
    from ANST
)

-- 6. Ändra kolumnen MANAGER i tabellen ANST till NOT NULL.
alter table ANST
alter column MANAGER char(1) not null

-- 7. Skapa en kopia av tabellen Department, namnge den AVD.
select *
into AVD
from Department

-- 8. Skapa en primärnyckel på kolumnen DeptID i tabellen AVD.
alter table AVD
add primary key (DeptId)

-- Överkurs
-- 9. Skapa en referential integrity constraint mellan tabellerna ANST och AVD,
--    alltså en främmande nyckel på kolumnen deptno i ANST. Namnge den FK_DEPTNUM

alter table AVD
add constraint FK_DEPTNUM
foreign key (deptno) references ANST(deptno)

-- 10. Ta bort avdelning 10 från tabellen AVD. Gick det?
delete from AVD
where deptno = 10
-- Nope, error :)

-- 11. Ta bort constraint FK_DEPTNUM. 
alter table AVD
drop constraint FK_DEPTNUM

-- 12. Pröva nu att ta bort avdelning 10 från AVD. Är detta bra? Diskutera!
delete from AVD
where deptno = 10
-- (discussion ensues)

-- 13. Ta bort tabellerna AVD och ANST.
drop table AVD, ANST

-- 14. Skapa en tabell; Totalinfo. Den ska innehålla alla kolumner från Employee och Department.
--     Ta endast med DeptID en gång. Vilka fördelar respektive nackdelar finns det
--     med denna enda tabell i stället för två tabeller Employee och Department?


-- 15. Ta bort Totalinfo.
drop table Totalinfo
