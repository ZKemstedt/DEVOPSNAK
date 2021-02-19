# Server Name & Type
### Primär Domänkontrollant
### DC1

# Description
## *Vad* <!-- Virtuell -->
## *Var*
## *Komponenter*
* Main Disk
  - Type: Differential
  - Location: C:\VM\DC1\DC1.vhdx
  - Parent Location: C:\VM\Moderdiskar\ModerdiskW2019.vhd
  - Size: 40GB
* Generation: 1
* RAM
  - Dynamic: True
  - MinimumBytes: 800MB
  - StartupBytes: 1500MB 
  - MaximumBytes: 4GB
  - Priority: 80
  - Buffer: 25
* Processor
  - Count: 2
* Virtual Switch: Klassrumsnät

# Configuration
* OS: Windows Server 2019 Datacenter Evaluation
* Build: 17763.rs5_release.180914-1434
* Display Resolution: 1024x768
* Network Configuration:
  - IP adress 10.6.66.165
  - Subnet mask: 255.0.0.0
  - Default gateway 10.6.68.1
  - Preferred DNS server: 127.0.0.1
  - Alternate DNS server: 8.8.8.8
<!-- * Windows Update Configuration -->
<!-- * Remote Access Configuration -->
<!-- * Local Configuration -->

# Roles and Features
* DNS
* AD DS

# DNS
* Zone name: osthyvel.se
* Static Records:
  - dc1.osthyvel.se         10.6.66.165
* Forwarders:
  - unConditional           8.8.8.8

# AD DS
* Domain Name: osthyvel.se
* NetBIOS Domain Name: OSTHYVEL
* DSRM password: *Hidden*
* OU-Structure:
[img]
* Groups
  - (*groups*)
* GPO
  - (*gpo*)
