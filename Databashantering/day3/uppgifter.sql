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


-- 9. Fyll ut med understreck _ till höger om efternamn. 
--    Totala stränglängden för kolumnen ska vara 15.

select
    lastname,
    lastname + left('_______________', 15 - len(lastname)) as 'rpad'
from
    employee

-- 10. Byt jobb på alla som är Kontorist till Assistent
select
    firstname,
    lastname,
    job,
    replace(job, 'Kontorist', 'Assistent')
from
    Employee
where
    job = 'Kontorist'

-- 11. Skriv allas namn (lastname) med versal första bokstav,
--     resten gemena.
select
    lastname as 'före',
    upper(left(lastname, 1)) +
    lower(right(lastname, len(lastname) -1)) as 'efter'
from
    Employee

-- 12. Skapa både för- och efternamn i en kolumn, och en signatur
--     i nästa kolumn. Signaturen ska vara versaler och bestå av 
--     första två bokstäverna i förnamn resp efternamn
--     (Göran Persson skulle få signaturen GÖPE). 

select
    firstname + ' ' + lastname as 'Namn',
    upper(left(firstname, 2) + right(lastname, 2)) as 'Signatur'
from
    employee

-- 13. Byt ut sista bokstaven i namnet mot en * på alla som arbetar
--     på avdelning 30.
select 
    firstname = case
        when DeptID = 30 then left(Firstname, len(Firstname)-1) + '*'
        else Firstname
        end
from Employee

-- 14. Visa hur många år den som arbetat längst respektive
--     kortast tid på företaget har arbetat.
select
    datediff(yy, min(HireDate), getdate()),
    datediff(yy, max(HireDate), getdate())
from Employee

-- 15. Visa namnet BLAKE i stället för 7698 för de som har 
--     LAKE som chef, annars visas bara MGR.
--     Visa ENAME, JOB, MGR. Obs! Använd CASE (i Oracle decode).
select
    Firstname + ' ' + Lastname,
    Job,
    Manager = case
        when ManagerID = 7698 then 'BLAKE'
        else 'MGR'
        end
from
    Employee

-- 16. Visa hur många dagar längre den som arbetat längst på
--     företaget har arbetat, jämfört med den som arbetat kortast tid.

select
    datediff(dd, min(HireDate), getdate()) - datediff(dd, max(HireDate), getdate())
    -- datediff(dd, min(hiredate), max(hiredate))
from Employee