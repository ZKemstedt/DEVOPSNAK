use T618
go


/*
* Clauses
*
*   group by
*     having
*   order by
*/

-- select [distinct | all] {* | <val>...]}
-- from <tableref> [, <tableref> ...]
-- [where <search_condition>]
-- [group by col [collate collation]...]
-- [having <search_condition>]
-- [union <select_expr>]
-- [order by <order_list>]

-- order by
select * from employee
where salary < 20000
order by job, firstname, lastname

-- group by + having vs where
select job, sum(salary) as lön
from employee
-- where -> ändra ingångsdata
group by job
-- having -> ändra group by
having sum(salary) > 60000

-- group by
select countryid, count(*) from city
group by countryid

-- group by having
select firstname, count(*) as antal 
from employee
group by firstname
having count(*) > 1


/*
* Connections
*
*   inner join
*   cross join
*   "self join"
*   left outer join
*   right outer join
*/

-- standard inner join
select vuxna.firstname as vuxen, barn.*
from vuxna
inner join barn
on vuxna.id = barn.vuxen_id

-- alternative syntax
select vuxna.firstname as vuxen, barn.* 
from vuxna, barn
where vuxna.id = barn.vuxen_id

-- with aliasing
select v.firstname, v.lastname, b.firstname as 'childname'
from vuxna as v left join barn as b
on v.id = b.vuxen_id

-- cross join
select v.firstname, b.firstname 'childname'
from vuxna v cross join barn b

-- -- -- --  -- --
-- meny example with self join

--      table elgiganten --
-- id           int              mainkey, autoinc
-- name         varchar(50)      not null
-- parent       int          

-- select
--     e1.name as 'maintitle'
--     e2.name as 'subtitle'
-- from elgiganten as e1
-- inner join elgiganten as e2
-- where e1.id = e2.parent
-- -- -- --  -- --


-- -- -- --  -- --
-- menu example with link-table

--      table menu --
-- id           int
-- name         varchar(50)

--      table articles --
-- id           int
-- name         varchar(50)
-- price        int

--      table linkMA --
-- meny_id      int
-- article_id   int

-- select * from menu m
-- inner join linkMA as L on m.id = L.menu_id
-- inner join articles as a on L.article_id = a.id
-- -- -- --  -- --


/*
* Sub-queries
*
*/

select firstname, lastname
from Employee E
join Department D on E.DeptID = D.DeptID
where location = 'Göteborg'
-- equivalent to
select firstname, lastname from Employee
where DeptId in
(
    select DeptID from Department
    where location = 'Göteborg'
)

select top 1 Firstname, lastname from Employee
order by salary desc
