#
# NAS1
# 

New-Item -Path "C:\VM\NAS1" -ItemType Directory
New-VHD -Path C:\VM\NAS1Disk1.vhd -ParentPath "C:\VM\ModerdiskW2019.vhd" -Differencing
New-VM -Name "NAS1" -VHDPath "C:\VM\NAS1\NAS1Disk1.vhd" -BootDevice IDE -Generation 1 -Switchname "Klassrumsnät"
Set-VMMemory NAS1 -DynamicMemoryEnabled $true -MinimumBytes 1GB -StartupBytes 2GB -MaximumBytes 4GB -Priority 80 -Buffer 25
Set-VMProcessor NAS1 -Count 2

#
# NAS2
#

# New-Item -Path "C:\VM\NAS2" -ItemType Directory
# New-VHD -Path C:\VM\NAS2Disk1.vhd -ParentPath "C:\VM\ModerdiskW2019.vhd" -Differencing
# New-VM -Name "NAS2" -VHDPath "C:\VM\NAS2\NAS2Disk1.vhd" -BootDevice IDE -Generation 1 -Switchname "Klassrumsnät"
# Set-VMMemory NAS2 -DynamicMemoryEnabled $true -MinimumBytes 1GB -StartupBytes 2GB -MaximumBytes 4GB -Priority 80 -Buffer 25
# Set-VMProcessor NAS2 -Count 2