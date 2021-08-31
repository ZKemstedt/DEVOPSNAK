# Filserver - NAS1
<!-- https://www.supermicro.com/en/products/system/4U/6048/SSG-6048R-E1CR36N.cfm -->
<!-- https://www.komplett.se/product/898949/datorutrustning/lagring/haarddisk/haarddisk-35/seagate-barracuda-1tb-35-hdd -->

## Location
* Brie Server Hall, Rack 2 Row 10

## Hardware
* RAM: xxx GB yyy MHz
* Processor: 2x Intel Xeon yyy GHz
* Hard Drives: 32x 1TB HDD 3.5"
* Hard Drives: 1x 1TB SSD ?????

<!-- * Main Disk
  - Type: Differential
  - Location: C:\VM\NAS1\NAS1.vhdx
  - Parent Location: C:\VM\Moderdiskar\ModerdiskW2019.vhd
  - Size: 40GB
* Generation: 1
* RAM
  - Dynamic: True
  - MinimumBytes: 800MB
  - StartupBytes: 1500MB 
  - MaximumBytes: 4GB
  - Priority: 80
  - Buffer: 25 -->

# Configuration
* OS: Windows Server 2019 Datacenter
* Build: 17763.rs5_release.180914-1434
* Display Resolution: 1024x768
* Network Configuration:
  - IP adress 10.6.66.166
  - Subnet mask: 255.0.0.0
  - Default gateway 10.6.68.1
  - Preferred DNS server: 10.6.66.165
  - Alternate DNS server: *None*
* Windows Update Configuration:
  - Download updates only, using Windows Update
* Remote Access Configuration:
  - Remote Management: Enabled
  - Remote Desktop: Disabled

## Printers

## Storage Services
* Storage Pool 1
  * Name: DelatDiskPool
  * Mirror: 2
  * Physical Disks: 20x 1TB
  * Virtual Disks:
    * DelatDisk 10TB
* Storage Pool 2
  * Name: AnvandareDiskPool
  * Mirror: 2
  * Physical Disks: 12x 1TB
  * Virtual Disks:
    * AnvandareDisk 6TB


## Shared Folders

### AnvandareDisk:\Users\$\ -> \\\NAS1\Users$
* Share Permissions:
  * Authenticated Users: Full Control
* NTFS Permissions:
  * System (Allow)
    * Full Control
    * This folder, subfolders and files
  * Administrators (Allow)
    * Full Control
    * This folder, subfolders and files
  * Creator Owner (Allow)
    * Full Control
    * Subfolders and fils only
  * Domain users (Allow)
    * Traverse folder / execute file
    * List folder / read data
    * Create folders / append data
    * This folder only

### DelatDisk:\Global\ -> \\\NAS1\Global
* Share Permissions:
  * Authenticated Users: Full Control
* NTFS Permissions:
  * System (Allow)
    * Full Control
    * This folder, subfolders and files
  * Administrators (Allow)
    * Full Control
    * This folder, subfolders and files
  * Creator Owner (Allow)
    * Full Control
    * Subfolders and fils only
  * Authenticated Users (Allow)
    * Read, write & execute
    * This folder, subfolders and files

### DelatDisk:\Brie\ -> \\\NAS1\Brie
* Share Permissions:
  * Authenticated Users: Full Control
* NTFS Permissions:
  * System (Allow)
    * Full Control
    * This folder, subfolders and files
  * Administrators (Allow)
    * Full Control
    * This folder, subfolders and files
  * Creator Owner (Allow)
    * Full Control
    * Subfolders and fils only
  * BriePersonal (Allow)
    * Read, write & execute
    * This folder, subfolders and files

### DelatDisk:\Chevre\ -> \\\NAS1\Chevre
* Share Permissions:
  * Authenticated Users: Full Control
* NTFS Permissions:
  * System (Allow)
    * Full Control
    * This folder, subfolders and files
  * Administrators (Allow)
    * Full Control
    * This folder, subfolders and files
  * Creator Owner (Allow)
    * Full Control
    * Subfolders and fils only
  * ChevrePersonal (Allow)
    * Read, write & execute
    * This folder, subfolders and files

### DelatDisk:\Emmentaler\ -> \\\NAS1\Emmentaler
* Share Permissions:
  * Authenticated Users: Full Control
* NTFS Permissions:
  * System (Allow)
    * Full Control
    * This folder, subfolders and files
  * Administrators (Allow)
    * Full Control
    * This folder, subfolders and files
  * Creator Owner (Allow)
    * Full Control
    * Subfolders and fils only
  * EmmentalerPersonal (Allow)
    * Read, write & execute
    * This folder, subfolders and files

### DelatDisk:\Gouda\ -> \\\NAS1\Gouda
* Share Permissions:
  * Authenticated Users: Full Control
* NTFS Permissions:
  * System (Allow)
    * Full Control
    * This folder, subfolders and files
  * Administrators (Allow)
    * Full Control
    * This folder, subfolders and files
  * Creator Owner (Allow)
    * Full Control
    * Subfolders and fils only
  * GoudaPersonal (Allow)
    * Read, write & execute
    * This folder, subfolders and files

### DelatDisk:\Mozzarella\ -> \\\NAS1\Mozzarella
* Share Permissions:
  * Authenticated Users: Full Control
* NTFS Permissions:
  * System (Allow)
    * Full Control
    * This folder, subfolders and files
  * Administrators (Allow)
    * Full Control
    * This folder, subfolders and files
  * Creator Owner (Allow)
    * Full Control
    * Subfolders and fils only
  * MozzarellaPersonal (Allow)
    * Read, write & execute
    * This folder, subfolders and files

### DelatDisk:\System Resouces\$\ -> \\\NAS1\System Resouces$
* Share Permissions:
  * Authenticated Users: Full Control
* NTFS Permissions:
  * System (Allow)
    * Full Control
    * This folder, subfolders and files
  * Administrators (Allow)
    * Full Control
    * This folder, subfolders and files
  * Creator Owner (Allow)
    * Full Control
    * Subfolders and fils only
  * Authenticated Users (Allow)
    * Read & execute
    * This folder, subfolders and files

## Mapped Drives

1. Brie
  * Folder: \\\NAS1\Brie
  * Mount as Network Drive
  * Drive letter: First available from I:
  * Item Level Targeting: (Security Group) BriePersonal
2. Chevre
  * Folder: \\\NAS1\Chevre
  * Mount as Network Drive
  * Drive letter: First available from I:
  * Item Level Targeting: (Security Group) ChevrePersonal
3. Emmentaler
  * Folder: \\\NAS1\Emmentaler
  * Mount as Network Drive
  * Drive letter: First available from I:
  * Item Level Targeting: (Security Group) EmmentalerPersonal
4. Gouda
  * Folder: \\\NAS1\Gouda
  * Mount as Network Drive
  * Drive letter: First available from I:
  * Item Level Targeting: (Security Group) GoudaPersonal
5. Mozzarella
  * Folder: \\\NAS1\Mozzarella
  * Mount as Network Drive
  * Drive letter: First available from I:
  * Item Level Targeting: (Security Group) MozzarellaPersonal
6. Global   
  * Folder: \\\NAS1\Global
  * Mount as Network Drive
  * Drive letter: First available from G:

## Printers
1. BrieKontorsskrivare
  * IP: 10.10.10.10
  * Deploy with GPO Per Machine to respective OU
  * Driver: Microsoft IPP Class Driver
  * Noteable Permissions:
    * Allow BriePersonal: Print
    * Allow BrieITPersonal: Print, Manage this printer, Manage documents
    * Allow Creator Owner: Manage documents

2. ChevreKontorsskrivare
  * IP: 10.10.10.11
  * Deploy with GPO Per Machine to respective OU
  * Driver: Microsoft IPP Class Driver
  * Noteable Permissions:
    * Allow ChevrePersonal: Print
    * Allow ChevreITPersonal: Print, Manage this printer, Manage documents
    * Allow Creator Owner: Manage documents

3. EmmentalerKontorsskrivare
  * IP: 10.10.10.12
  * Deploy with GPO Per Machine to respective OU
  * Driver: Microsoft IPP Class Driver
  * Noteable Permissions:
    * Allow EmmentalerPersonal: Print
    * Allow EmmentalerITPersonal: Print, Manage this printer, Manage documents
    * Allow Creator Owner: Manage documents

4. GoudaKontorsskrivare
  * IP: 10.10.10.13
  * Deploy with GPO Per Machine to respective OU
  * Driver: Microsoft IPP Class Driver
  * Noteable Permissions:
    * Allow GoudaPersonal: Print
    * Allow GoudaITPersonal: Print, Manage this printer, Manage documents
    * Allow Creator Owner: Manage documents

5. MozzarellaKontorsskrivare
  * IP: 10.10.10.14
  * Deploy with GPO Per Machine to respective OU
  * Driver: Microsoft IPP Class Driver
  * Noteable Permissions:
    * Allow MozzarellaPersonal: Print
    * Allow MozzarellaITPersonal: Print, Manage this printer, Manage documents
    * Allow Creator Owner: Manage documents


## Roles and Features
*None*
<!-- Add Printer stuff -->
