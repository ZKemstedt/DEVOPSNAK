# Databashantering - MSSQL



# list of things we've covered/mentioned
(does not include oracle)

### Keywords / Statements
```sql
-- query build parts
alter
create
insert
    into
    values
update
    set
select
    top
from
    left outer join     -- left join
    right outer join    -- right join
    full outer join     -- full join
    inner join          -- join
    cross join
where
    and
    or
    is
    in
    not
    like
group by
    having

intersect
except
union

order by
    asc
    desc

as              -- naming / altering
begin      
end
on              -- do smth on x / set bool to true
off

commit          -- transaction control
rollback        -- transaction control
tran            -- transaction control
transaction     -- transaction control

exec            -- execute procedure
collate     -- key collate language -> makes `key` conform to `language`
use         -- database to use
go          -- tell the server to execute (aka the preiously listed commands must be executed before executing the next ones)
kill        -- kill [session id]

print
if
case
    when
    then
    else

-- datatypes
database
table
column
index
    clustered
    nonclustered
proc
procedure

identity
null

tinyint
bigint
int
bigint

char
varchar
text        -- link -> blob

nchar       -- unicode
nvarchar    -- unicode
ntext       -- unicode

binary
varbinary
image       -- link -> blob

date
time
datetime
datetime2
weekday
datefirst
language
location

-- etc

user        -- built in identifier of some sort
cast()      -- similar to convert()

```

### Built-in functions
```sql
-- etc
isnull()

-- math
min()
max()
sum()
count()
stdev()
avg()

abs()
pi()
floor()
ceiling()
round()
sqrt()
power()

-- dates
getdate()
datename()
datepart()
datediff()
dateadd()

-- string
left()
right()
lower()
upper()
rtrim()
ltrim()

replicate()
substring()
replace()
charindex()

len()       -- datalength()
str()
ascii()
convert()
```

### Operators
```sql
=
!=
*           -- select all / multiplication
+           -- string concatenation / addition
-
>=
<=
<
>
```

### Etc
```sql
-- sub-queries
select x from y
where z = (
    select ...
)

-- single line comment

/*
 * Multi line comment
 *
 */

'% pattern matching'

sp_help -- ::= sp_help <c> -> help for c
sp_help language

sp_who
sp_who2

-- global variables
@@version -- ::= @@<x> -> global variable x

-- example: set first day of week
select @@datefirst set datefirst 1

@@datefirst
@@language
@@version
@@servername

-- built in tables
-- sysindexes
-- sysobjects
-- sys.syslogins
-- sys.sysusers
-- sys.syspermissions


-- Settings
set
-- name                     -- desc
-- default                  recommended

    ansi_nulls              -- ?
                            on
    quoted_identifier       -- ?
                            on

    nocount                 -- count (and show) affected rows
    off                      

    showplan_xml            -- return the execution plan as an xml
    off                     
```