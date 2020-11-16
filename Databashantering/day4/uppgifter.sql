use T618
go

-- 1. Visa efternamn (Lastname) och lön (Salary) på alla som arbetar som Säljare i tabellen anställda
--    (Employee). Sortera i bokstavsordning på efternamnet
select lastname, salary
from employee
order by lastname

-- 2. Sortera alla efter grundlön (Salary) med den högst betalde överst. Har två eller fler samma lön ska 
--    bokstavsordning på efternamn gälla. Visa hela tabellen Employee.
select * from employee
order by salary desc, lastname

-- 3. Visa alla anställda efter 2000-01-01(Hiredate), med den sist anställde överst.
select * from employee
where hiredate > '2000-01-01'
order by hiredate desc

-- 4. Räkna ut hur många kunder det finns på varje ort. Använd tabellen Customers.
select city, count(*) as kunder
from customers
group by city

-- 5. Visa de orter och antalet kunder där företaget har fler än 5 kunder. Visa i fallande antal-ordning.
select city as ort, count(*) as kunder
from customers
group by city having count(*) > 1
order by count(*) desc, city

-- 6. Visa de orter och antalet kunder där säljaren Carola Karlsson har fler än en kund. Sortera fallande efter antal.
select * from employee
where firstname like 'carola' -- empid 8125

select 
    city as ort,
    count(*) as kunder
from customers
-- where empid = 8125
where empid = 
( -- subquery
    select empid from employee
    where firstname like 'carola%'
)
group by city having count(*) > 1
order by kunder desc, city

-- 7. Visa de orter och antalet kunder på orten som inte blivit tilldelad en säljrepresentant (dvs där EmpID är NULL).
select city, count(*) as antal
from customers
where empid is null
group by city

-- 8. Visa namnen på de populäraste blommorna följt av antalet. De mest sålda blommorna ska vara överst. Använd tabellen OrderDetails.
select name, sum(Amount) as 'units sold'
from OrderDetails
where IsDeliveryItem = 0
group by name
order by sum(Amount) desc

-- 9. Det kanske inte är lönsamt att ha alla typer av blommor på lager. Visa de buketter som sålts 3 gånger eller färre.
select name, sum(Amount) as 'units sold'
from OrderDetails
where IsDeliveryItem = 0
group by
    name having sum(Amount) < 4

-- 10. Visa intäkt per artikel (oavsett om det är en bukett eller frakt) med den mest inkomstbringande artikeln överst.
--     Visa tre kolumner: artikelns namn, intäkt och antal sålda artiklar.
select
    name,
    sum(price * amount) as 'revenue',
    sum(amount) as 'units sold'
from OrderDetails
group by name
order by 2 desc, 1
