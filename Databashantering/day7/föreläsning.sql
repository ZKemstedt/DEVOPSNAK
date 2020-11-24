-- SET showplan_xml OFF;

use BikeStores
go

sp_help [sales.customers]

create index idx_customer_lastname on sales.customers(last_name)
create index idx_customer_lastname2 on sales.customers(last_name, first_name)

select first_name, last_name from sales.customers
where last_name = 'Wood'



use T618
go

select * from sysindexes
where status = 0
and id in (
    select id from sysobjects
    where name = 'Department'
)

-- gammalt
DBCC showcontig

-- nyare
select a.index_id, avg_fragmentation_in_percent
from sys.dm_db_index_physical_stats (
    db_id(N't618'),object_id(N'Employee'), null, null, null
    ) as a 
join sys.indexes as b
on a.object_id = b.object_id
and a.index_id = b.index_id

-- indexera om?

-- avg fragmentation > 5% & < 30% 
alter index idx|all on tbl reorganize

-- avg fragmentation > 30%
alter index idx|all on tbl rebuild with (online = on)


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


exec namelist

go
alter proc namelist (@efternamn varchar(50)) as
begin
    -- disable row counter
    set nocount on

    select @efternamn = efternamn + '%'

    -- debug only
    print @efternamn

    -- check number of rows
    declare @cnt int

    select @cnt = count(*)
    from Employee
    where lastname like @efternamn

    if @cnt = 0
    begin
        print("Hello")
        -- stuff
    end

    -- debug
    -- print cast(@cnt as varchar(10))

    -- log access
    insert into AccessLog (AccessTime, Input, NoOfRows)
    values (getdate(), @efternamn, @cnt);

    -- show result
    select
        firstname,
        lastname,
        job
    from Employee
    where lastname like @efternamn
    order by Firstname, Lastname

    -- enable row counter
    set nocount off
end

exec namelist

