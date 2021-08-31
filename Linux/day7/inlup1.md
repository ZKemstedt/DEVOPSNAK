# Hand-in excersize 1


## 6
```bash
find /home/???? 2>&1 | grep -v "Permission denied" | grep -v "zeke" | sort -k2r -t/ > others
```

## 7
```bash
df -h | head -n 1 > rootspace : df -h | grep "/$" >> rootspace
```

## 8
```bash
#!/bin/bash

DATE=$(date)
MEM=$(free)
JOBS=$(jobs -l)
PROC=$(ps -ly)
PROCALL=$(ps -ely)

# we don't like empty lists
[ -z "$JOBS" ] && JOBS="(no runing jobs)"

cat <<END
# System information report
User: $USER
Date: $DATE

# $USER Jobs
$JOBS

# $USER processes
$PROC

# System Memory Usage
$MEM

# System processes
$PROCALL

END
```