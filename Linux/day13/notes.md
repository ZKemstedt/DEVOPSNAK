# Monday March 29th

* Bootstrap
* System services
* systemctl, service
* Scheduled activities
* crontab systemd
* Runlevels

## Terminology
service
daemon
cron, crontab
systemd
unit, target, runlevel

# Bootstrapping
When started, does this in this order:
* load kernel
* load additional required modules
* mount root filesystem 
* start the first process 'init' with pid 1
The program that will be run as 'init' can be supplied via argument to the kernel.

## init
When started, does this in this order:
* read configuration from files in /etc
* mounts filesystems
* start subsystem for network, messageing, et.c.
* start daemons
* start 'login' - the process for interactive logon
Note that init owns the whole process tree and runs as long as the system is up.

## Systemd
The system-daemon 'systemd' is the 'init' used by Ubuntu and some others.
Has builtin functionality that was previously spread out in other daemons and concepts:
* Scheduling (was crond)
* Loggign (was syslogd)
* Login (was logind)
Note! Not completely finished yet.

## Runlevel
'runlevel' is a concept from 'System V init' that specifies which servicelevel a system is running on.
In 'systemd' the corresponding concept is called 'target'.
The primary difference between the two is that only one runlevel can be active, but several targets can be active simultaneously.
| Runlevel | Target            |
|----------|-------------------|
| 0        | poweroff.target   |
| 1        | rescue.target     |
| 2, 3, 4  | multi-user.target |
| 5        | graphical.target  |
| 6        | reboot.target     |

## Default 'target' and configuration
'systemd' is located in `/lib/systemd` and 'init' points to it.
The configuration is located in `/etc/systemd`, it mostly contains references 'units', located in `/lib/systemd/system`.
Each 'target' is such a 'unit' and corresponds to a `.target` file.

## Systemservices and demonprocesses
With systemd, each system service is a 'unit' and is defined by a `.system` file.
As an example, the system service 'ssh' is defined by `ssh.service`. A few lines in the file decides how the service is started.
```
[Service]
EnvironmentFile=-/etc/default/ssh
ExecStartPre=/usr/sbin/sshd -t
ExecStart=/usr/sbin/sshd -D $SSDH_OPTS
ExecReload=/usr/sbin/sshd -t
ExecReload=/bin/kill -HUP $MAINPID
```

## Commands

* Target-commands
```
$ systemctl list-units --type target
$ systemctl get-default
$ systemctl set-default
```
* Service-commands
```
$ systemctl [start | status | reload | stop]
```


# Part 2

## Cron, crontab and crontab
### Cron
Cron is the daemon that manages scheduled tasks

### crontab
Configuration for which tasks are scheduled is done in the 'crontab' file. Each user has a 'crontab'.
each row in the 'crontab' has 6 fields: min hour dom mon dow command
examples: 5 21-23 * * 0,6 /usr/local/bin/my-report

### crontab
`crontab` is also the command used to create and edit 'crontabs'.
`crontab -l` disaplays the users crontab
`crontab -e` edits the users crontab
tip: (https://crontab.guru)


