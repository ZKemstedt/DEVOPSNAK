# Tuesday February 2nd
## Add DC to existing Domain
```powershell
#
# Windows PowerShell script for AD DS Deployment
#

Import-Module ADDSDeployment
Install-ADDSDomainController `
-NoGlobalCatalog:$false `
-CreateDnsDelegation:$false `
-CriticalReplicationOnly:$false `
-DatabasePath "C:\Windows\NTDS" `
-DomainName "jultomten.nu" `
-InstallDns:$true `
-LogPath "C:\Winwods\NTDS" `
-NoRebootOnCompletion: $false `
-SiteName "Default-First-Site-Name" `
-SysvolPath "C:\Windows\SYSVOL" `
-Force:$true
```