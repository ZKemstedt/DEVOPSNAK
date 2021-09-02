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
