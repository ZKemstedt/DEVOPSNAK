use T618
go

-- 1.
select * from Employee

-- 2.
select * from Employee
where HireDate = '2002-12-03'

-- 3.
select * from Employee
where HireDate > '2000-01-01'

-- 4.
select Lastname, job, salary, commission
from Employee
where salary > 20000

-- 5.
select Firstname, Lastname, salary+ISNULL(commission, 0) as revenue
from Employee

-- 6.
select Lastname as Efternamn, salary as Lön, salary * 1.1 as NyLön
from Employee
where salary < 10000

-- 7.
select 
    Lastname as Efternamn,
    salary + ISNULL(commission, 0) as Inkomst,
    (salary + ISNULL(commission, 0)) * 0.3 as Skatt
from Employee

-- 8.
select
    Lastname as Efternamn,
    salary as Lön,
    ISNULL(commission, 0) as Bonus
from Employee
where commission is null

-- 9.
select Lastname, job, salary
from Employee
where Lastname = 'JONES'

-- 10.
select Lastname, job, salary
from Employee
where Lastname != 'JONES'

-- 11.
select * 
from Employee
where Lastname like 'j%' or Lastname like '%ar%'

-- 12.
select lower(firstname + '.' + lastname + '@nackademin.se')
from Employee

-- 21. 
select deptid from Employee
intersect
select deptid from Department

-- 22. Visa de avdelningar som inte har några anställda.
select deptid from Department
except
select deptid from Employee
