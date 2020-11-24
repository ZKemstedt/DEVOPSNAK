sp_who2

access rules on columns -- not recommended, use `views` instead

# views
* desc
* syntax
* example
```sql
create view lista as 
select EmpID, Firstname, Lastname, Job
from Employee
```
when inserting with view must make sure that columns not included in the view must allow null.


# index
clustered, non-clustered index

```sql
create index idx_Employee_Lastname on Employee (Lastname)
```

skyffla in mycket data?
1. ta bort index
2. skicka in data
3. bygg upp index


# procedures

```sql

drop proc if exists namelist
go

create proc namelist as
begin
    select
        firstname,
        lastname,
        job
    from Employee
    order by lastname, firstname
end
go

exec namelist
```

```sql
alter proc namelist (@efternamn varchar(50)) as
begin
    select @efternamn = efternamn + '%'

    select
        firstname,
        lastname,
        job
    from Employee
    where lastname like @efternamn
    order by Firstname, Lastname
end

exec namelist

```