## Ex 1
Use commands mentioned in today's lecture to find out
how your linux-machine is set up network-wise
* Does it use eth or wlan?
* Show the routing-table
```bash
ip addr show
route
```


## Ex 2
How would you set your ip address to 10.1.1.101/24 ?
```bash
# using ifconfig
sudo ifconfig enp0s3 10.1.1.101 netmask 255.255.255.0 up

# using ip
sudo ip addr add 10.1.1.101/24 dev enp0s3
sudo ip link set eth1 up

# real ip is 10.0.2.15
```


## Ex 3
Implement the following functionality:
Two times per hour eth0 / wlan0 is checked if it's active and the result is 
written to a log file with timestamp
```bash
# -- day4/ex3.sh --
#!/bin/bash
timestamp=`date +Y-%m-%d_%H-%M-%s`
logfile="~/devops/Linux 2/days/day4/ex4.sh"
state=$(ip addr show | grep -E '(enp0s3).*(state UP)')

if [ -z "$state" ]
then
    echo "enp0s3 inactive $timestamp" >> "$logfile"
else
    echo "enp0s3 active $timestamp" >> "$logfile"
fi
# ---

crontab -l | { cat; echo "0,30 * * * * ~/devops/Linux\ 2/days/day4/ex4.sh"; } | crontab -
crontab -l | grep -v 'day4' | crontab -
```


## Ex 4
Try contacting mail.nackademin.se with the smtp-protocol (eg using telnet)
```bash
telnet mail.nackademin.se
```


## Ex 5
* Use `ping` and `traceroute` to research some known logical adresses
  - www.nackademin.se
  - www.dn.se
* Also use the command `dig` to view lookup of the adresses
```bash
ping www.nackademin.se
ping www.dn.se
traceroute www.nackademin.se
traceroute www.dn.se
dig www.nackademin.se
dig www.dn.se
```


## Ex 6
What can you derive from the following DNS records?
```
www.foobar.se.      2842 IN  CNAME  foobar.se.
foobar.se           3600 IN  N      5.160.254.28
mail.foobare.se.    3595 IN  A      5.150.254.28
foobar.se.          3600 IN  MX     10 foobar-se.mx1.staysecuregroup.com.
foobar.se.          3600 IN  MX     20 foobar-se.mx2.staysecuregroup.net.
```


## Ex 7
Make your machine temporarily believe that it is the name server for the domain
example.se
- continue sending all other requests to the name server you're currently using
- add at least one A record and one CNAME record
- remember to back up relevant files before you do this exercise so that you can easily revert afterwards.
- [extensive example](https://www.digitalocean.com/community/tutorials/how-to-configure-bind-as-a-private-network-dns-server-on-ubuntu-18-04)
 


```


