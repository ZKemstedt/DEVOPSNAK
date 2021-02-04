# Wednesday January 27th

* Snappchot/Checkpoit i Hyper-V
* Installation av Windows Server 2019
* Server Core
* Server Manager
* Hårdvaruhantering i Windows
* Drivrutiner
* Lab: Installation av Windows 2019 Core
* Lab: Post installation konfiguration med GUI
* Lab: Post installation konfiguration av Server Core
* Lab: Server Managern
* Övning: Uppdatera drivrutiner
* Övning: Rollback driver

<!-- begin -->

# Windows Server

## Windows Server 2012 R2 Editions
* Windows Server 2012 R2 Standard *mark*
* Windows Server 2012 R2 Datacenter *mark*
* Windows Server 2012 R2 Foundation
* Windows Server 2012 R2 Essentials
* Microsoft Hyper-V Server 2012 R2 *mark*
* Windows Storage Server 2012 R2 Workgroup
* Windows Storage Server 2012 R2 Standard
* Windows MultiPoint Server 2012 R2 Standard
* Windows MultiPoint Server 2012 R2 Premium

2x Standard a´ 8'000:- = 16'000
Datacenter = 35'000

Datacenter får ha obegränsat antal gäst OS
Standard får ha en host med 4 gäst OS

# Server Core
* Is a more secure, less resource-intensive installation option
* Can be converted to full graphical shell version of Windows Server 2012
  * (This feature is mostly unused and might have been removed in later versions?)
* Is managed locally using sconfig.cmd
With remote management enabled, you rarely will need to sign in locally


# Roles
* Roles are made up of role services components that provide additional functionality associated with the role
* In Server Manager 2012, console servers with a similar role are grouped together
* Role deployment also includes the configuration of dependencies


# Features
* Are components that support the server such as Windows Server Backup or Failover clustering
* Usually do not provide a service directly to clients on the network

Keep in mind the following points:
* Roles can have features as dependencies
* Features on Demand are features that need to be installed using a mounted image as a source


# Installing Windows Server 2012
## Installation Methods
Windows Server 2012 R2 deployment method options include:
Optical disk
USB flash drive
Windows Deployment Services

## Windows Setup
* Upgrade
* Custom
advantages ...
disadvatages...

Just use Custom, always.

## Requirements
Windows Server 2012 R2 has the following minimum hardware requirements:
Processore architecture         x64
Processor speed                 1.4 GHz
Memory (RAM)                    512 MB
Hard disk drive space           32GB
    More hard disk drive space is needed if the server has more than 16 GB of RAM

## Migrating Server Roles
There are tools to migrate server roles

# Post Installation Configuration of Windows Server 2012
* Overview of Post-Installation
* Configuring Server Network Settings
* stuff
* stuff
* stuff



# Powershell
syntax: `Verb-Noun -attribute | Verb-Noun -switch ...`
<!-- attribute / switch ?? -->
notes:
    There is no space between verb and noun but there is a dash.
    There are exclusions to the verb-noun rule, such as new

example: `Get-ADUser -Filter * -SearchBase "OU=Test,DC=brodin,DC=local" | Set-ADUser -Department "Hej"`


# Computer stuff

UPS Uninterupted Power Supply
* Batteries for 20 minutes - several days
* Power Supplies for continous delivery
* Equipment to shut down servers in a controlled manner before battery runs out

IRQ Interrupt Request Queue



# Drivers
Drivers are software that enable communication between Hardware and OS
also, sometimes drivers create frameworks to configure and use the hardware (e.g. printers)

HAL Hardware Abstractation Layer exist between Hardware and OS
contains drivers for Motherboard
HAL makes it so that OS is not dependent on a given architechture

Installation of most drivers these days is handled by *Plug and Play*

Home-made drivers must be managed "manually", pnp-util

Can roll back drivers (one stage)

Signed drivers
64-bit windows will not load unsigned drivers even if they are installed
`driverquery /si` will list signed and unsigned drivers.
Group Policy (PGO) can send out certificates to make clients trust unsigned drivers
Can disable signed-driver enforcement

What happends when you uninstall a Plug-and-Play driver?
If the hardware is still plugged in, it will reinstall automatically.
If you want to stop the driver, disable it instead.