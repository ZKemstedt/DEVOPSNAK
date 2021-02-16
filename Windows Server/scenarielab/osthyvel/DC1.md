# DC1

Create new forest osthyvel.se
DSRM password: (see notes)
NetBIOS domain name: OSTHYVEL

# File structure
## Differential Disk
* path: C:\VM\DC1.vhd
* parent: C:\VM\Moderdiskar\ModerdiskW2019.vhd
* Generation: 1
<!--
VMMemory DynamicMemoryEnabled $true, MinimumBytes 1500MB, StartupBytes 2GB, MaximumBytes 6GB, Priority 80, Buffer 25
VMProcessor Count 2 
-->

# AD DS
# DNS


# TODO
Knowledge Base article 942564
DISABLE

# IP settings
IP adress 10.6.66.165
Subnet mask: 255.0.0.0
Default gateway 10.6.68.1

Preferred DNS server: 127.0.0.1
