use T618
go

-- 1.   Se till att tabellen Employee blir indexerad på lön,
--      med högsta lönen först.
create index idx_Employee_Salary_desc on Employee (Salary desc)

-- 2.   Ta bort ovanstående index.
drop index idx_Employee_Salary_desc on Employee

-- 3.   Skapa en kopia på Department och döp den till Dept.
--      Skapa därefter ett unikt sammansatt index på kolumnerna
--      DeptName och Location i tabellen Dept.
--      Försök ändra name till Ekonomi där DeptID = 10.
select * into Dept from Department

create index idx_Dept_DeptName_Location on Dept (DeptName, [Location])

update Dept
set DeptName = 'Ekonomi'
where DeptID = 10

select * from Dept

-- 4.   Ta bort tabellen Dept. Försvinner index som du skapade
--      automatiskt när tabellen tas bort?
drop table Dept
-- yes