# Wednesday March 31 

* Rotating logs
* Disk space
* Memory
* CPU
* Open files
* Stuck processes

## Terminology
watch
sysctl
CPU-hog
zombie

## Centralized logging
rsyslog is the included centralized logging system that comes bundled with Ubuntu.

Another popular variant is ELK-stack,
wich consist of Elasticsearch, Logstash and Kibana.

## journalctl
`journald` is a logging service built into systemd.

## watch
use `watch` to get continous updates from another command.

## stress
use `stress` and `stress-ng` to stresstest computers.

## ulimit
to set restrictions for usage of resources, you can use `ulimit`.
to show what restrictions are active: `ulimit -a`
Configure system limits in `/etc/security/limits.conf`

## Disk space
`df` monitor disk space on all filesystems.
`du` monitor disk usage for a folder or foldertree.
`du -sh [path]` include subdirectories and display sizes in human units.

## CPU
`top` / `htop` 
Load average is displayed with three values, the average of cpu-requests 5 mins ago, 10 mins ago and 15 mins ago.
cpu-requests corresponds to the amount of threads that are waiting to be run on the cpu.

## Memory
`free` / `vmstat`

`oom_reaper` is a special service that may kill processes to prevent memory crashes.

## I/O
`vmstat` is handy to see load on disks in the form of reads and writes.
`iotop` works like `top` but for I/O. Very useful.


## Open files
`lsof -u <name>` open files per user
`lsof -p <pid>` open files per process

## Stuck Processes
### troubleshoot processes
If you don't want to kill the process, find out what it's doing.
`strace` 'system trace' shows which systemcalls are made and wich state the process goes through.
`strace -p <pid>`

There's also zombie processes.

### kill processes
Use `kill` to kill processes
If the process is really stuck, the default signal `SIGTERM` doesn't kill the process, you'll need to use `SIGKILL` or 9: `kill -9`.
This will make the kernel stop the process.

note: `pgrep` is useful for grepping processes.

### stop/continue processes
If you want to temporarily stop a process you can send `SIGSTOP`.
To resume it again use `SIGCONT`.