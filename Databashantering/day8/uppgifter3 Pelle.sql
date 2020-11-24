use T618
go


-- 4.   Logga in som PELLE med SQL Manager Studio, läs samtliga rader i Employee.
--      Gick det bra?
select * from Employee
-- Permission Denied


-- 5. Kan PELLE läsa Department? 
select * from Department
-- No


-- 6.   Om ni skriver en join mellan Employee och Department, vad får PELLE se
--      (ingenting, eller bara de poster från Employee)? 
select firstname, lastname, DeptName from employee e
inner join Department d
on e.DeptId = d.DeptId
go
-- Nothing, permission denied

-- EX.
select * from Empshort
