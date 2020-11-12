
-- -- -- -- as 

-- med fnuttar
select [Location] as 'Stad', DeptName as 'Avdelning' from Department

-- utan fnuttar
select [Location] as Stad, DeptName as Avdelning from Department

-- utan as
select [Location] Stad, DeptName Avdelning from Department

-- med =
select Stad=[Location], Avdelning=DeptName from Department


-- -- -- --
select * from pris


select 
    artikel,
    utpris 'pris exkl moms',
    utpris*1.25 as 'pris incl moms'
from pris


select
    lower(Firstname + '.' + Lastname + '@nackademin.se') as email
from Employee


select *
from employee
where job='chef'


select *
from employee
where salary >= 30000


select *
from employee
where HireDate > '1995-01-01'


select *
from employee
where
    Lastname like '%j%' or lastname like '%sson'

select firstname,
    lastname,
    salary,
    commission,
    salary + isnull(commission, 0) as total
from Employee


-- -- -- --
select top 10 * from Employee

select namn from [dbo].[Department]
union
select namn from [dbo].[Ishockey]