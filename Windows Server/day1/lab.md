# Lab 1

## Exercise 2
## 9. [optional] Create a differential disk using powershell
```powershell
Import-Module Hyper-V
New-VHD "D:\VM\Lab\Surfdator.vhd" -ParentPath "D:\VM\Moderdiskar\ModerdiskW2019.vhd"
```

## Exercise 3
## 10. [optional] Create a virtual Machine using powershell
```powershell
new-vhd -dynamic D:\VM\lab\Extradisk.vhdx -controllertype SCSI -controllernumber 0
```
Open disk management on the virtual machine to take the disk online and intitialize and format it.
Alternatively you can use powershell
```powershell
get-disk # list the disks and their numbers, this instruction assumes the newly created Extradisk has the id 1
get-disk -number 1 | initialize-disk # note: will initialize as GPT by default
get-disk -number 1 | new-partition -usemaximmsize | format-volume -confirm:$false -filesystem NTFS -newfilesystemlabel PowerShellTest
get-partition # list the partiions and their numbers, by default a GPT disk has the GPT table on partition 1 and the normal at partition 2
set-partition -disknumber 1 - partitionnumber 2 -newdriveletter G
```

## Exercise 4
## 2 - 4
```powershell
import-module hyper-v
enable-vmresourcemetering Surfdator
measure-vm Surfdator
```