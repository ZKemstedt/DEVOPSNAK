# Day 6

## Recap
* Database design
* Datatypes
* Normalization
* Entity Relationship
* Data Model            <!--not part of powerpoint-->
  * Conceptual
  * Logical
  * Physical
  * ER-diagram


## Today
* more on syntax, `insert`, `update`, `delete`
* stored procedures


## Manipulating data
* `insert` - add new rows
* `update` - edit rows
* `delete` - remove rows
* The shared aspect of `insert`, `update`, `delete` is that they manipulate data, as compared to `select` wich does not.



## Insert
* Used to add rows to a table
* syntax
  ```sql
  insert into <table> [(col[, col ...])]
  {values (<val> [, <val> ...]) | <select_expr>}
  ```
* example
  ```sql
  insert into Employee (EmpId, Firstname, Lastname, Salary, DeptId)
  values (1234, 'James', 'Bond', 25000, 50)
  ```

* `insert` without providing columns (1)
  * If you provide data for all columns, you don't have to specify the columns.
  * The values must be in the order that is defined by the table.
  * This is not recommended for stored procedures or script because the table's definition might be changed in the future.
  * example
    ```sql
    insert into Employee
    values (1234, 'James', 'Bond', 25000, 50)
    ```
  * Not recommended to use this feature in program code. If the table definition changes at a later point in time, you would have to change the code again. The order, datatype and number of columns must be the same as those specified by the insert statement.
  * This method is adventageous when using interactive tools such as MS SQL Server Management Studio.

* `insert` with sub-queries
  * You can use values from other tables to fill a table
  * Instead of providing `values` (...) you provide a `select` query (sub-query) that matches the columns provided to `insert`.
  * example
    ```sql
    insert into kunder (name, adress, state, zip)
    values = (
        select lastname, street ...
    )
    ```
  * The two tables do not have to be similar; in fact, the sub-query can `select` from multiple tables.
  * The important aspect is that the data that is returned by the sub-query mathes that witch is specified by `insert`

  * Rules for Insert- och Select- statements
    * Select can't target the same table as the insert
    * The amount of columns of the select and insert statements must be the same
    * the columns's datatype must be the same


## Update
* Used to edit data in existing rows
* syntax
  ```sql
  update {table}
  set col = <val> [, col = <val> ...]
    [where <search_condition>]
  ```
* example
  ```sql
  update Employee
  set Job = 'Agent'
  where EmpID = 1234
  ```
* Do not forget the `where`-condtition, otherwise ALL rows will be updated

* Update with subquerry
  * Update Employee so that all säljare get 25% increase to commission, but they are not allowed to have higher income than the salary of the employee with the highest salary.
  ```sql
  update Employee
  set Commission = Commission * 1.25
  where Job = 'Säljare'
  and Salary + isnull(Commission, 0) * 1.25 <
    (
    select max(Salary) from Employee
    )


## Delete
* Used to remove rows from tables
* syntax
  ```sql
  delete [from] table [where <search_condition>]
  ```
* Depending on the usage of the `delete`-statement and `where`-clause, the following can be done.
  * No row is removed
  * One row is removed
  * Many rows are removed
  * All rows are removed
* Think about the following things
  * Do not use `delete` to remove values in a column. (use `update` for that)
  * Just like `insert` and `update`, removal of a row from a table can cause integrity issiues. This is important to consider when editing data in a database.
  * `delete` removes rows, not the actual table.
    * to remove a table, `drop` is used.
* example
  ```sql
  delete from Kunder
  where ZIP < 5000
  ```
* Never forget the `where` clause or `delete` will remove ALL rows.


## Comments regarding Update and Delete
* Use these statements with caution, a single miss in the `where` clause may cause tremendous damage.
* Encourage trying out the `where` clause in a select statement since it's safe.


## Exercises 
transactions, commits and rollbacks
```sql
-- begin transaction
begin tran
update vuxna
set lastname = 'pettersson'
where id = 4
-- fail?
rollback tran
-- success?
commit tran
```


# More about relations. Create, alter and remove databases and tables


### One-to-one relations
  * Rare because it usually means it's the same object
  * Sometimes it's usefull to split an object into multiple tables. Examples include very large columns and passwords.


### Many-to-many relations
  * Requires a link-table


## Relation rules
* When defining the relation between two objects we can also define some rules for that relation
* For the child and parent respectivel, we can set rules for `update`, `insert` and `delete`.
* The primary rules we can set are `restrict` and `cascade`.


## Restrict
* Control what can be inserted, removed or changed in a row when other tables's data has relations to the data that is changing.
* Example
  * We have a relation between Department and Employee (DeptId)
  * On this relation we set the restriction `On Child Insert Restrict`
  * This means that... On `insert` to `Employee`, the `DeptId`-value will be checked against `Department`, and if it doesn't exist, the insert is denied.
* This is standard in all modern systems and it's key to avoid issues with inconsistencies. It requires some computational resources from the system and for that reason it is sometimes skipped. In those cases it's important that it's handled by the applications that work toward the database instead.
* In modern relation-databases this is handled using Primary and Foreign keys.


## Cascade
* when changes are applied to the table, also apply changes to related tables
* Example
  * We have a relation between Department and Employee (DeptId)
  * On this relation we set the rule `On Parent Update Cascade`
  * This means that... When updating DeptId in Department, DeptId in Employee will also be updated for the Employees that are affected.
* It is rare to have `On Parent Update Cascade` in large transaction databases since the it can be very performance heavy and give rise to problems with inconsistencies.
* It's better to set relations on keyvalues that are not reliant on the bussines or values that can change. Use unique values such as IDs.


## Constraints
* In MSSQL Server these relation rules are called `constraints`
* They can be used to create different rules but `cascade` and `restrict` are the ones directly tied to relation-databases
* Constraints will be explained further later.


# Create and maintain databases and tables
## Statements
```sql
create database   -- creates a database
alter database    -- changes the definitions of a database
drop database     -- removes a database

create table      -- creates a table
alter table       -- changes the design of a table
drop table        -- removes a table
```


## Create a database
* syntax
  ```sql
  create database database_name
  ```
* example
  ```sql
  create database Personal
  ```
* In MS SQL more parameters can be specified, such as where database files and logfiles should be located, and how large they should be.


## Creating Tables
* syntax
  ```sql
  create table table_name (
    column datatype [not null],
    column datatype [not null]
    ...
    )
  ```
* example
  ```sql
  create table Person (
    name    varchar (30),
    adress  varchar (30),
    salary  int
  )
  ```
* extensive example (as generated by MSSQL Server Management Studio)
  ```sql
  set ansi_nulls on
  go

  set quoted_identifier on
  go

  create table [dbo].[orderdetail]
  (
      [OrderDetails_id] [int] identity(1, 1) not null,
      [Orders_id] [int] not null,
      [Amount] [int] null,
      [Prod_id] [int] null,
      [Name] [varchar](50) null,
      [Price] [decimal](12, 2) null,
      [Vat_id] [int] null,
      [VatValue] [int] null,
      [isDeliveryItem] [int] null
  ) on [primary]
  go
  ```


## Note
In order to prevent excessive disk fragmentation, consider setting the initial size and autogrowth parameters when creating new things.


## Datatypes
### Datatypes in MS SQL Server (Oracle in paranthesis, max size is for MS SQL Server)
* char (char) -- Alphanumeric chars with a set length, max 8000 chars.
* varchar (varchar2) -- Alphanumeric data with variable length, max 8000 chars.
* text (long) -- Alphanumeric string, variable length, up to 2GB, not indexable.
* decimal/int (number) -- integers and floating point numbers.
* datetime (date) -- Datum, including year, month, day, hour, minute and second.
* binary (raw) -- binary data up to 8000 bytes
* image (long raw) -- binary data up to 2GB
### rowid in Oracle, MS SQL Server uses identity


## Not null
* forces a column to filled on `insert` and `update`, a row must always have a value in that column.
* example
  ```sql
  create table Person
  (
    Name    varchar (30)    not null,
    Adress  varchar (40),
    Salary  numeric (12, 2) not null
  )
  ```


## Create a table from an existing table
* syntax
  ```sql
  select (col1, col2, col3)
  into new_table
  from old_table
  <where ...>
  ```
* example
  ```sql
  -- create a kopy of Employee with everyone who has a Salary above 25000
  select *
  into CopyOfEmployee
  from Employee
  where Salary > 25000
  ```


## primary key
* One or more columns that uniquely identifies each row in a table.
* The column will be automatically set to `not null` and a unique `index` is created on that column.
* example
  ```sql
  create table Department (
    DeptId    int             primary key,
    DeptName  varchar (14),
    Location  varchar (13)
  )
  ```


## Foreign key
#### (Referential Integrity Constraint)
* one or more columns that refer to a primary key in another table
* the content must exist in the refered table
* example
  ```sql
  create table Employee (
    EmpId         int             not null
    Firstname     varchar (10)
    Lastname      varchar (10)
    Job           varchar (9)
    ManagerId     smallint
    Hiredate      datetime
    Salary        int
    Commission    int
    DeptId        int
    constraint fk_DeptId foreign key(DeptId)
    references Department(DeptId)
  )
  ```

## Foreign key
### with "on delete cascade"
* You can set rules on foreign keys.
* By default `on delete restrict` -> you cannot remove a primary key until all foreign keys (referenced rows) have been removed.
* If you remove the referenced primary key, you can set a rule to automatically remove all associated rows.
* example
  ```sql
  create table employee (
    empid       int           not null,
    firstname	  varchar(10),
    lastname	  varchar(10),
    job     	  varchar(9),
    managerid   int,
    hiredate    datetime,
    salary   	  int,
    commission  int,
    deptid  	  int,
    constraint fk_deptid foreign key(deptid)
    references department(deptid) on delete cascade)
  ```


## Additional rules on `insert` and `update`
* You can set rules to check columns against certain criteria.
* Such rules are called check constraints and can only handle columns in the active row.
* They are used to move bussiness rules down to the lowest level (the database), this means that regardless of how access it made, the rules cannot be circumvented. The advantage of this is that the rules don't have to be implemented on the Applciation level, the programming becomes easier and cleaner.
* example
  ```sql
  -- Salary + Commission must be 5000 or higher.
  create table Employee (
    EmpId       int         not null,
    Firstname   varchar (10),
    Lastname    varchar(10),
    Job         varchar(0),
    ManagerId   int,
    Hiredate    datetime,
    Salary      int,
    Commission  int,
    DeptID      int,
    check (Salary + Commission <= 5000)
  )
  ```


## Change a table's design
* `alter table` let's you do two things.
  * add a column in an existing table
  * edit an existing columns settings
* syntax
  ```sql
  alter table table_name
  < add column_name data_type |
  alter column column_name data_type >
  ```
* examples
  ```sql
  alter table employee
  add kommentar varchar(80) 
  ```

  ```sql
  alter table employee
  alter column lastname varchar(40) 
  ```

* Restrictions when altering tables
  * Can be used to change a column-setting from `not null` to `null`. However the oposite might fail.
  * A column-setting can only be changed from `null` to `not null` if there are no `null` values in the column.
  * The same rule applies when changing the columns datatype
  * To *shorten* the length of a columns datatype, the column must be `null`


## Removing a Table
* syntax
  ```sql
  drop table table_name
  ```
* example
  ```sql
  drop table Employee
  ```


## Removing a Database
* syntax
  ```sql
  drop database database__name
  ```
* example
  ```sql
  drop database Personal
  ```
