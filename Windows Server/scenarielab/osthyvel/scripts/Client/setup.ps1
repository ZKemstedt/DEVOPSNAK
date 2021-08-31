
# Virtuell Switch -> Klassrummsnätet

#Skapar en VM för installation av Windows 10

#Skapa VM
New-Item -Path "Klient2W10" -ItemType Directory
New-VM -Name "Klient2W10" -NewVHDPath "C:\VM\Klient2W10\Klient2W10.vhdx" -NewVHDSizeBytes 40GB -Generation 1 -SwitchName VM1
Set-VMMemory Klient2W10 -DynamicMemoryEnabled $true -MinimumBytes 800MB -StartupBytes 1500MB -MaximumBytes 3GB -Priority 80 -Buffer 25
Set-VMProcessor Klient2W10 -Count 1
Set-VMDvdDrive -VMName Klient2W10 -Path "C:\VM\Installationsfiler\19042.508.200927-1902.20h2_release_svc_refresh_CLIENTENTERPRISEEVAL_OEMRET_x64FRE_en-us.iso"

#Boota
Start-vm Klient2W10
