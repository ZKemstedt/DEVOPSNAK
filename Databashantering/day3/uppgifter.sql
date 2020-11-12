use T618
go


-- 1. Ange hur många anställda som har en grundlön som är mer än 25000 kr.
select count(*) from Employee where Salary > 25000

-- 2. Summera alla anställdas grundlöner.
select sum(Salary) from Employee

-- 3. Hur mycket tjänar den som tjänar mest respektive minst i företaget?
select
    min(Salary) as 'Minst',
    max(Salary) as 'Mest'
from
    Employee

-- 4. Ange den totala kostnaden för samtliga anställdas grundlöner
--    om resp persons grundlön höjs med 10%. 
--    Visa även skillnaden i kronor mot den gammla lönen.
select
    sum(salary) as 'total salary cost',
    sum(salary)*1.1 as 'new total salary cost',
    sum(salary)*1.1 - sum(salary) as 'salary cost increase'
from Employee

-- 5. Flytta fram anställningsdatum ett år för alla anställda. 
--    Visa det som nytt anställningsdatum i svarstabellen.
select *, dateadd(yy, 1, HireDate) as 'New Hire Date' from Employee

-- 6. Vilket datum infaller första söndagen efter anställningsdatum?
--    Visa för alla anställda. Endast Oracle, funktionen saknas i MS SQL Server.
-- skip

-- 7. Beräkna standardavvikelsen för lönen till alla chefer
--    (Chef eller VD). Slå upp i hjälpen!
select
    round(stdev(salary), 0)
from
    Employee
where
    Job in ('Chef', 'VD')

-- 8. Beräkna antalet månader mellan dagens datum och de anställdas
--    anställningsdatum i Employee.
select datediff(mm, HireDate, getdate())
from Employee
