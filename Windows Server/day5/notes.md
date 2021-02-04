

# Filesystem
MBR / GPT defines partitions
A filesystem exists on each partition
Each filesystem has a file allocation table, wich points to a sector.
- A sector cannot contain more than a single file.
- A file can span several sectors

- The FAT filesystem has a set size on the file allocation table
- NTFS/ReFS is prefered by Microsoft

# NTFS
- manages file access rights
- supports compression
- supports encryption (EFS = Encrypted File System)
- managed "previous versions"
- detects bad sectors on the harddrive
- supports very large partitions
- supports very large files
- no issues with small files on large partitions
- managed symbolic links and junctions
- recommended for all physical disks


SID = Secutiry Identifier

Effective permissions = All currently applicable permissions for a user is added together.
Deny overrides Allow
Users Group = Default usergroup = all users

When sharing a folder on a NTFS partition, the permissions will be combinedd.
- share permissions is checked first, ntfs is checked every time a file is accessed
- The most restrictive permissions will be used
When sharing a folder on a FAT partition, only the share permissions will regulate file access

EFS Encrypted File System
- Similar encryption technology as SSL
- Folders are not encrypted
- The Owner of the file/folder can activate encryption
- Administrators with full control cannot decrypt encrypted files
- in AD domains a recovery agent that can access all encrypted files will be created automatically
- default is the domain admin account Recovery Agent
- It is recommended to remove the decryptioncertificate from the computer environment so that the domain administrator doesn't access the files simply by logging in
- ...
- ...

# Domain (vs Workgroup)
- Single-sign-on 'tickets' by Kerberos
- Everyone trusts the Domain Controller

- Nobody trusts local accounts


# LDAP
- (Before LDAP: NT4)
- hierarchal structure using OU (Organizational)
- group-like, an account cannot exist in several 'groups'