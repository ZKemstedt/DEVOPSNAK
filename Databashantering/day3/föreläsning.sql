use T618
go

select count(*) antal_rader
from Employee
where Commission is null


select
    sum(salary) as 'summa salary',
    sum(salary + isnull(commission, 0)) as 'summa inkomst'
from employee


select
    min(salary) as 'min',
    max(salary) as 'max',
    avg(salary) as 'medel',
    sum(salary) as 'summa salary',
    avg(commission) as 'medel comm',
    avg(isnull(commission, 0)) as 'medel comm',
    count(*) as 'antal anställda'
from employee

-- date tools
select datediff(hh,  '1967-08-15', getdate())

select dateadd(minute, -3000, getdate())

select datepart(qq, getdate())

select datename(weekday, '1967-08-15')


-- första dagen på veckan
select @@DATEFIRST
set datefirst 1

-- ställ in språk
-- sp_helplanguage
set language Swedish
select datename(weekday, '1967-08-15')

set language us_english



select * from employee
where datediff(dd, hiredate, getdate()) = 
    (
    select
        max(datediff(dd, hiredate, getdate()))
    from employee
    )