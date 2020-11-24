# Transactions
## Begin

## Rollback
* example 1
    let's say that we have 2 tables that we want to update.
    We update the first one and it succeeds, but when we update the 
    secondary one it fails. Now we don't want the first update to
    be applied.....

* example 2
  ```sql
  -- session 1
  begin tran
  delete from Employee
  select * from Employee

  -- session 2
  select * from Employee

  -- session 1
  rollback tran
  select * from Employee

  -- session 2
  select * from Employee
  ```

## Savepoint

## Commit

## Buffers

## Rollback segments

## Locks


# Security
* Login (Server)
  * To log in, the user needs to authenticate
* Database
  * The user needs to have the rights to access respective databases
* Access Rights (Objects)
  * the user needs access on tables and views to rewd, write and update rows

user
login

## Server roles
```sql
grant all | statement
to security_account
```

## Database roles



```sql
-- goes to tempdb
select * into #EMPtemp from Employee

```
