# Tuesday March 9th

# Users and Groups

### Primary Groups
All users are members in a primary group.
In Ubuntu, a personal group for each user is created with the same name as the user

### Secondary Groups
Secondary groups are often used to delegate permissions

Group membership is applied at login

## Userdata Location
Userdatabase is `/etc/passwd` by standard, it contains:
`username:x:user-id:primary-group-id:home-folder:shell`

For Non-central user management:
PAM - "Pluggable Authentication Modules".
Example is LDAP: pam_ldap

## Password Location
Located in `/etc/shadow`
`username:pw:a:b:c:d:::`
if pw = * -> user cannot login
pw is hashed and salted.

## Groups Location
Location in `/etc/group`
`group:x:c:<members>`

## User ID
root has id 0
normal users start at 1000
It is mostly the numerical-id, not the username that is used throughout the system.


# Processes and Users
* All processers are executed as users
* The process inherit the permissions of the user
* All process have a process-id 'pid'
* Processes can create new processess, called child processes
* All processes have a parent process, except systemd
```sh
ps                  # my processes
pstree              # processtree from systemd
ps -ef | less       # all processes
pstree 0            # processtree for all processes from systemd
ls -l /sbin/init    # /sbin/init -> /lib/systemd/systemd
```

# Processes and files
In linux, everything is a file.
To work with a file, a process is needed.
```sh
fuser <path>
lsof
lsof -p <pid>
```
# Laboration 1

## 3
```sh
ls -d /proc/*[0-9]
ls -ld /proc/[1-9]???
ls -d /proc/[1-9]* | sort-nr | head

cd /proc
ls -dF [1-9]*
ls -d [1-9]????
```


# User Management
### Commands
```sh
useradd / adduser
usermod
userdel
passwd

groupadd
groupmod
groupdel
```
### Examples
```sh
sudo usermod --shell /bin/bash newuser2
```

# Types of Users
Systemuser
- no home folder
- uid <1000
- no login

Systemparameters for login are set in
/etc/login.defs
/etc/pam.d

# Su and Sudo
TLCL 101

su = **substitute user**
sudo = su do
/etc/sudoers


```sh
# modify password expiration settings for LOGIN
chage [options] LOGIN
```