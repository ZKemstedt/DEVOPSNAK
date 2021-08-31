# Monday, March 15th

## Last time...
* PATH
* Arguments
* Input, Output and Redirection
* Foreground and Background Processes
* Job-control
* Exit Codes
* Signals

## Today...
* ssh, scp, sftp
* Server settings
* Klient settings
* Keys and password login
* Tunnels*
* Hand-in excersize #1.

**beyound the scope of this course.*

## Terminology
* ssh
* OpenSSH
* ssh-keys
* network ports
* Tunnels


sudo apt install openssh
ssh user@server

# login with password
is 'secure' because nobody kan read it and the trafic is encrypted.
it's less secure because...
* should be unique, wich is difficult if you manage a lot of servers
* passwords are relativey short and usually easy to copy
* has to be entered at every login
* same password regardless of access location

# login with key.
based on pairs of private + public keys

ssh-agent helps remembering keys (run on client)

# create key-pair
all ssh-klient tools are saved in ~/.ssh
