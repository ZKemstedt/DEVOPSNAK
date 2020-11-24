use T618
go


-- 1.   Skapa login för PELLE och ANNA med SQL authentication, med ett enkla lösenord. 
create login Anna with password = 'Anna123'
create login Pelle with password = 'Pelle123'


-- 2.   Se till att ANNA och PELLE är en databas-användare i T618
create user Anna for login Anna
create user Pelle for login Pelle


-- 3.   Tilldela rättigheter till PELLE att köra SELECT på Employee-tabellen
grant select on Employee to Pelle
go


-- 4.   Logga in som PELLE med SQL Manager Studio, läs samtliga rader i Employee.
--      Gick det bra?
-- see [ Uppgifter3 Pelle.sql ]


-- 5.   Kan PELLE läsa Department?
-- see [ Uppgifter3 Pelle.sql ]


-- 6.   Om ni skriver en join mellan Employee och Department, vad får PELLE se
--      (ingenting, eller bara de poster från Employee)? 
-- see [ Uppgifter3 Pelle.sql ]


-- EX.
create view EmpShort as
    select firstname, lastname, DeptName from employee e
    inner join Department d
    on e.DeptId = d.DeptId
go

grant select on EmpShort to Pelle
go

create proc test
as
select * from EmpShort

grant exec on test to Anna

-- test (proc) --> empshort (view) --> Emp + Dept (tables)


-- 7.   Växla tillbaks till motsvarande SA och tilldela PELLE även rätten att skapa
--      en vy.


-- 8.   Växla till Pelle och se till att PELLE skapar en vy med underliggande data
--      såsom SELECT firstname, lastname FROM Employee. 


-- 9.   Tilldela rättigheter till ANNA så hon kan köra SELECT mot PELLEs vy.


-- 10.  Logga in som ANNA.


-- 11.  Låt ANNA köra SELECT * FROM PELLESVY. Hur gick det? Förklara
