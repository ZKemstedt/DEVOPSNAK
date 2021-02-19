# Lab 1 - Wednesday February 3rd
## Edit several accounts with powershell

```powershell
Get-ADUser -filter * -SearchBase "ou=anvandare,ou=Stockholm,dc=jultomten,dc=nu" | Set-ADUser -Fax 08745234262
```