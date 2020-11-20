# list of things we've covered/mentioned
(does not include oracle)

### Keywords / Statements
```sql
-- query build parts
insert
    into
    values
update
    set
create
    table
select
    top
    case
        when
        then
        else
        end
    as
from
    left outer join     -- left join
    right outer join    -- right join
    full outer join     -- full join
    inner join          -- join
    cross join          -- -> generate combinations
        on
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

-- datatypes
identity
null

int
smallint
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
--

user
weekday
cast()

-- etc
use -- database to use
go -- tell the server to execute (aka the preiously listed commands must be executed before executing the next ones)
datefirst
language
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
abs()
pi()
floor()
ceiling()
round()
sqrt()
power()
stdev()
avg()

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

len() -- datalength()
str()
ascii()
convert()
```

### Operators
```sql
=
!=
* -- all / multiplication
+ -- concatenation / addition
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


-- global variables
@@version -- ::= @@<x> -> global variable x

-- example: set first day of week
select @@datefirst set datefirst 1

@@datefirst
@@language
@@version
@@servername
```