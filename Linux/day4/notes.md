# Monday March 8th

Directory

/
/bin
/boot
/dev
/etc
    /etc/crontab
    /etc/fstab
    /etc/passwd
/home
/lib
/lost+found
/media
/mnt

...
/opt
/proc
    Processer
    Ett virtuellt filsystem
/root
    Home directory for the root account
/sbin
/tmp
/usr
    /usr/bin
    /usr/lib
    /usr/local
    /usr/sbin
    /usr/share
        /usr/share/doc
/var
    /var/log

# Manipulating Files and Directories
* cp - Copy files and directories
* mv - Move/rename files and directories
* mkdir - Create directories
* rm - Remove files and directories
* ln - Create hard and symbolic links

## Wildcards (also known as globbing)
### Wildcards
| Wildcard        | Meaning                                                          |
|-----------------|------------------------------------------------------------------|
| `*             `| Matches any characters                                           |
| `?             `| Matches any single character                                     |
| `[characters]  `| Matches any character that is a member of the set characters     |
| `[!characters] `| Matches any character that is not a member of the set characters |
| `[[:class:]]   `| Matches any character that is a member of the specified class    |

### Commonly Used Character Classes
| Character Class | Meaning                             |
| ----------------|-------------------------------------|
| `[:alnum:]`     | Matches any alphanumeric character  |
| `[:alpha:]`     | Matches any alphabetic character    |
| `[:digit:]`     | Matches any numerial                |
| `[:lower:]`     | Matches any lowercase letter        |
| `[:upper:]`     | Matches any uppercase letter        |

### Examples
| Pattern                  | Matches                                                                       |
|--------------------------|-------------------------------------------------------------------------------|
| `*                     ` | All files                                                                     |
| `g*                    ` | Any file beginning with "g"                                                   |
| `b*.txt                ` | Any file beginning with "b" followed by any characters and ending with ".txt" |
| `Data?                 ` | Any file beginning with "Data" followed by exactly three characters           |
| `[abc]*                ` | Any file beginning with either an "a", a "b", or a "c"                        |
| `BACKUP.[0-9][0-9][0-9]` | Any file beginning with "BACKUP." followed by exactly three numerals          |
| `[[:upper:]]*          ` | Any file beginning with an uppercase letter                                   |
| `[![:digit:]]*         ` | ANy file not beginning with a numeral                                         |
| `*[[:lower:]123]       ` | Any file ending with a lowercase letter or the numerals "1", "2", or "3"      |


# Permissions
## File Attributes (10 bits)
general: `faaabbbccc`
example: `lrw-rw-rw-`

### File Types (1 bit)

### File Mode (9 bits)
aaa: owner (user -u)
bbb: group (group -g)
ccc: world (others -o)

| Ocagonal | Binary | Symbolic  |
|----------|--------|-----------|
| 0        | 000    | ---       |
| 1        | 011    | --x       |
| 2        | 010    | -w-       |
| 3        | 011    | -wx       |
| 4        | 100    | r--       |
| 5        | 101    | r-x       |
| 6        | 110    | rw-       |
| 7        | 111    | rwx       |

Note that Permissions, Owner and Groupmembership are three different things.
To change permissions, `chmod` is used.
To change owner and group, `chown` is used.

## Chmod
### Symoblic Notation
### Symbolic Notation Examples


umask


# Commands

## Grep
`grep *.txt`
-i: ignore case

## Locate
`locate *.tar`
searches the file index

## Find
`find /from/where/to/start/looking -name <filename>`
`find /dev -type d`
`find /usr/src -name '*.h' -type f -exec grep -i -q int {} \; -print`

# Homework / Laborations
## Laboration 2
TLCL s219-227
TLCL s229
## Laboration 3