# Snippets of notes + partial appendix



## vim
```bash
echo "set rnu" >> ~/.vimrc
echo "set number" >> ~/.vimrc
echo "set tabstop=4" >> ~/.vimrc
echo "syntax on" >> ~/.vimrc
echo "set expandtab" >> ~/.vimrc
```

### Default editor
git config --global core.editor "vim"
[link](https://stackoverflow.com/questions/2596805/how-do-i-make-git-use-the-editor-of-my-choice-for-commits)


## ssh
* generate keys `ssh-keygen -t ed25519`




# Appendix

## Network
### commands
  - ifconfig
    - Display / edit interfaces and configuration
  - ip
    - Newer replacement to ifconfig
  - route
    - Display / edit routing table
  - ethtool
    - Display / edit parameters for a network interface
  - ping
    - Test connectivity to an address
  - traceroute
    - Display routing to an adress

## DNS
### Records
  - A
    * Maps name to ip-address
  - CNAME
    * Alias: maps name -> name
  - MX
    * Points out mailserver
  - NS
    * Points out nameserver (DNS)
  - TXT
    * Text, often used for machine-machine interactions and verifications
  - PTR
    * Maps ip-address to name


## Email
### SMTP
  - "Push" to mailserver
  - protocol is connection oriented
  - port: 25 (465 ssl)
  - some commands:
    * `HELO` start session
    * `MAIL FROM` sender
    * `RCPT TO` recipient
    * `DATA` start the actual message
    * `QUIT` end session
    * `HELP` info about availabe cmds
### POP
  - port: 110
### IMAP
  - port: 143
