use T618
go


-- 1. Ta reda på var alla anställda arbetar med hjälp av tabellerna Employee och Department.
--    Visa efternamn (Lastname), lön (Salary), avdnummer (DeptID) och arbetsplats (Location).
--    Sortera på arbetsplats och namn.
select Lastname, Salary, D.DeptID, Location
from Employee E
join Department D on E.DeptID = D.DeptID

-- 2. Samma som ovan, men visa även de avdelningar som inte har några anställda.
select Lastname, Salary, D.DeptID, Location
from Employee E
right join Department D on E.DeptID = D.DeptID

-- 3. Samma som 1, men ta bara med de som arbetar i Stockholm.
select Lastname, Salary, D.DeptID, Location
from Employee E
right join Department D on E.DeptID = D.DeptID
where Location = 'Stockholm'

-- 4. Vad heter avdelningen där Smith arbetar?
select DeptName
from Employee E
join Department D on E.DeptID = D.DeptID
where Lastname = 'Smith'

select deptname from Department
where deptid = (
    select deptid from Employee
    where lastname like 'smith'
)

-- 5. Lista alla anställningsnummer (EmpID), efternamn (Lastname) och chefens
--    anställningsnummer (ManagerID) från tabellen Employee. Använd vanlig SELECT!
select EmpID, Lastname, ManagerID from Employee

-- 6. Samma som uppgift 5 men ta även med namnet för chefen 
--    (en egenkoppling på Employee-tabellen).
select E.EmpID, E.Lastname, E.ManagerID, C.Lastname as 'Manager Name'
from Employee E
join Employee C on E.ManagerID = C.EmpID

-- 7. Som uppgift 5 men se till att även de som inte har någon chef kommer med i listan. 
--    (Yttre koppling)
select E.EmpID, E.Lastname, E.ManagerID, C.Lastname as 'Manager Name'
from Employee E
left join Employee C on E.ManagerID = C.EmpID

-- 8. Som uppgift 6 men lägg till kolumnerna för de anställdas  och chefernas lön.
--    Gör en restriktion så att endast anställda som tjänar mer än sin chef kommer med.
select E.EmpID, E.Lastname, E.Salary, E.ManagerID, C.Lastname as 'Manager Name', C.Salary
from Employee E
join Employee C on E.ManagerID = C.EmpID
where E.Salary > C.Salary

-- 9. Ta reda på anställningsnummer och efternamn för alla chefer och räkna ut
--    medellönen för de personer som är direkt underställd respektive chef. Visa i ett svar.
select C.EmpID, C.Lastname 'Manager Name', avg(e.Salary) 'Average subjects salary'
from Employee E
join Employee C on E.ManagerID = C.EmpID
group by C.EmpID, C.Lastname

-- 10. Visa namn och jobb på som har samma arbete som CLARK.
select Firstname, Job
from Employee
where job = (
    select Job
    from Employee
    where Lastname = 'Clark'
)

-- 11. Vilken säljare tjänar mest inklusive provision (Commission)? 
--     Observera att det kan förekomma NULL-värden. Hantera i så fall dessa!
select top 1 Lastname
from Employee
where Job = 'Säljare' 
group by Salary + isnull(Commission, 0), Lastname
order by Salary + isnull(Commission, 0) desc

-- Överkurs
-- 12. Vilka anställda har BLAKE som chef?
select Lastname
from Employee
where ManagerID = (
    select EmpID
    from Employee
    where Lastname = 'BLAKE'
)

-- 13. Vilka arbetar i samma stad som Smith?

-- mixed
select Lastname
from Employee e
join Department d on e.DeptID = d.DeptID
where [Location] = (
    select [Location]
    from Employee e
    join Department d on e.DeptID = d.DeptID
    where Lastname = 'Smith'
)

-- nested sub-queries
select Lastname
from Employee
where DeptId in (
    select DeptId
    from Department
    where [Location] = (
        select [Location]
        from Department
        where DeptId = (
            select DeptId
            from Employee
            where Lastname = 'Smith'
        )
    )
)

-- 14. Visa avdelningsnamn och lönekostnad per avdelning. I lönekostnaden ingår provision.
select DeptName, sum(Salary + isnull(Commission, 0)) 'Salary cost'
from Employee e
join Department d on e.DeptID = d.DeptID
group by DeptName
order by 'Salary cost' desc

-- 15. Samma som ovan men ta bara med de avdelningar som har fler än tre anställda. 
select DeptName, sum(Salary + isnull(Commission, 0)) 'Salary cost'
from Employee e
join Department d on e.DeptID = d.DeptID
group by DeptName
    having count(*) > 3
order by 'Salary cost' desc

-- 16. Samma som ovan, men visa även avdelningsort (Location). 
select [Location], DeptName, sum(Salary + isnull(Commission, 0)) 'Salary cost'
from Employee e
join Department d on e.DeptID = d.DeptID
group by DeptName, [Location]
    having count(*) > 3
order by 'Salary cost' desc

-- 17. Visa anställningsdatum för den längsta respektive den kortaste tid någon har
--     varit anställd på varje ort.
select min(HireDate), max(HireDate), [Location]
from Employee e
join Department d on e.DeptID = d.DeptID
group by [Location]