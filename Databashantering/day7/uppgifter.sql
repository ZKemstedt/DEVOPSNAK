use T618
go


-- 1. Sapa en vy baserad på tabellen Customers och kalla den vy1.
--    Ta med kolumnerna Cust_ID, Firstname, Lastname, City och sätt
--    och sätt egna namn på kolumnerna.
create view vy1 as
select 
    Cust_id as id,
    Firstname as Förnamn,
    Lastname as Efternamn,
    City as Stad
from Customers
go

select * from vy1
go

-- 2. Gör en vy av Employee- och Department-tabellerna och kalla den vy2.
--    Den ska innehålla alla anställda som tjänar mer än 10 000. Ta med kolumnerna
--    anställningsnr, efternamn, jobb, lön och avdelningsnamn.
create view vy2 as 
select EmpID, Lastname, Job, Salary, DeptName
from Employee e
join Department d on e.DeptId = d.DeptID
where Salary > 10000
go

select * from vy2
go

-- 3. Skapa vy3 baserad på vy2 där lönen är omvandlad till dollar. 
--    En dollar är värd 7.50 SEK.
create view vy3 as 
select
    EmpID,
    Lastname,
    Job,
    Salary = convert(int, Salary / 7.5),
    DeptName
from vy2
go

select * from vy3
go

-- 4. Ta bort vyerna VY1, VY2 och VY3.
drop view vy1, vy2, vy3
go

-- 5.   Skapa en vy VY5 av Employee-tabellen där man slår ihop Lön (salary) och
--      Bonus (commission) till en kolumn. Ta med efternamn,
--      jobb och den nya lönekolumnen.
create view vy5 as
select Lastname, Job, Salary + isnull(Commission, 0) as Income
from Employee
go

select * from vy5
go

-- 6.   Se till att de som inte har någon bonus ändå får med
--      sin lön i den nya kolumnen.

-- see uppg 5.

-- 7.   Samma som ovan men lägg till en kolumn som visar varje anställds chef.
--      De som inte har någon chef får texten ’The Boss’ i stället.
alter view vy5 as
select
    e.Lastname, 
    e.Job, 
    e.Salary + isnull(e.Commission, 0) as Income, 
    isnull(m.Lastname, 'The Boss') as Boss
from Employee e
left join Employee m
on e.ManagerID = m.EmpID
go

select * from vy5
go


-- Överkurs
-- 8.   Skapa en vy som visar avdelning, plats, antal anställda, medellönen
--      och maxlönen för varje avdelning. 
create view vy8 as
select 
    DeptName,
    [Location], 
    count(*) as Employees, 
    avg(Salary) as avgSalary, 
    max(Salary) as maxSalary
from Employee e
join Department d
on e.DeptID = d.DeptID
group by DeptName, [Location]
go

select * from vy8
go

-- 9.   Skapa en vy som talar om vad varje anställd ska betala i skatt varje
--      månad. Antag att man betalar 30% i skatt. Ta med kolumnerna Namn(lastname)
--      och skatt. De som har bonus (comm) ska betala 50% i skatt på sin bonus
--      men bara 30% på lönen.
create view vy9 as
select
    Lastname as Namn,
    Salary * 0.3 + ISNULL(Commission, 0) * 0.5 as Skatt
from Employee e
go

select * from vy9
go


-- 10.  Ta bort alla vyer
drop view vy5, vy8, vy9
go


-- 11.  Skapa en chefs-vy, enbart bestående av chefer, deras anställningsnummer,
--      lön, jobbtitel, för- och efternamn samt orten där de arbetar.
create view chefvy as
    select EmpID, Firstname, Lastname, [Location], Job, Salary
    from Employee e
    join Department d on e.DeptID = d.DeptID
    where e.EmpID in (
        select distinct ManagerID from Employee
    )
go

select * from chefvy
go

drop view chefvy
go
