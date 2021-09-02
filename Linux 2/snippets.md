#



## vim
```bash
echo "set number" >> ~/.vimrc
echo "set tabstop=4" >> ~/.vimrc
echo "syntax on" >> ~/.vimrc
echo "set expandtab" >> ~/.vimrc
```

## ssh
* generate keys `ssh-keygen -t ed25519`




# Appendix

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
