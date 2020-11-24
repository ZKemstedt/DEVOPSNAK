use T618
go


/*
*   Exercise 1.
*
*   Skapa en procedur som har en input parameter. Denna parameter ska representera Name.
*   Om man anropar proceduren utan att ange parametern ska returvärdet vara samtliga
*   personer i Employee. 
*   Om man anropar proceduren med värdet på parametern till A ska returvärdet vara 
*   de som har ett för- eller efternamn som startar på A.
*   Anger man AN ska returvärdet vara de som har ett för- eller efternamn som startar
*   på AN etc. 
*/
create proc usp_search (@name varchar(50) = '%') as
begin
    select @name = @name + '%'

    select * from Employee
    where 
        lastname like @name
        or firstname like @name

end
go

exec usp_search 'an'
go


/*
*   Exercise 2.
*
*   Ändra tabellen Employee, och lägg till kolumner för Username och Password.
*   Försök använda Alter table-kommandot. 
*/
alter table Employee
add username varchar(10)

alter table Employee
add [password] varchar(10)

select * from Employee
go


/*
*   Exercise 3.
*
*   Uppdatera några användare och ge dem lämpliga Username och Password.
*   Försök använda Update-kommandot. 
*/ 
update Employee set [password] = 'hemligt'

update Employee
set username = left(Firstname, 3) + left(Lastname, 3)
go


/*
*   Exercise 4.
*
*   Skapa en procedur som har två input parametrar; en för Username och Password.
*   När man anropar proceduren och dessa Username + password är korrekt, ska returvärdet
*   vara EmpID. Är det fel ska returvärdet vara ”Wrong username” resp ”Wrong password”.
*/
create proc usp_pwdCheck (@user varchar(10), @pwd varchar(10)) as
-- alter proc usp_pwdCheck (@user varchar(10), @pwd varchar(10)) as
begin
    declare @pwd_found varchar(10)
    declare @usr_found varchar(10)
    declare @EmpId int

    select
        @EmpId = EmpID,
        @usr_found = username,
        @pwd_found = [password]
    from Employee
    where
        username = @user
    
    -- user doesn't exist
    if @usr_found is null
    begin
        select 'Wrong username' as Returnvalue
        return
    end

    -- user exists, check pwd
    if @pwd_found = @pwd
        select @EmpId as Returnvalue
    else
        select 'Bad password' as Returnvalue

    -- debug
    -- select @EmpId, @usr_found, @pwd_found

end
go

usp_pwdCheck 'andcar', 'hemligt'
usp_pwdCheck 'andcar', 'asdf'
usp_pwdCheck 'asdf', 'hemligt'

drop proc usp_pwdCheck
go