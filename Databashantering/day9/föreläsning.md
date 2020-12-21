```sql
create proc multikill (@user_login varchar(50))
as
begin
    declare @str varchar(1000)
    set @str = ''

    select @str = @str + 'kill ' + cast(session_id as varchar(10)) + '; '
    from sys.dm_exec_sessions
    where login_name = @user_login

    print @str
    exec (@str)

end    
```

```sql
set nocount on
declare @cnt
set @cnt = 2

while @cnt > 0
begin
    select * from [sales].[customers]
    order by last_name desc

    select * from [sales].[customers]
    order by last_name desc

    select * from [sales].[customers]
    where last_name like '%g'

    select * from [sales].[customers]
    where last_name like '%m'

    print cast(@cnt as varchar(10))
    select @cnt = cnt -1
end
set nocount off

```


<!-- ola hallengren -->
<!-- dbatools.io -->

SQL Server Profiler
trace accessors

index tuning
-> makes indexes


normaliseringsregler

index
    clustered
    non-clustered
views
schemas
