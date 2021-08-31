# Wednesday March 17th

## Layers
REST, GraphQL           | Path, POST - data
http, ssh, dns          | url, hostname
tcp / udp / icmp        | port
ip                      | ip-adress
MAC / Ethernet          | MAC-adress

```sh
# Show Interfaces with
$ ip link
# 'lo': loopback interface, all systems have this.
# 'en': typicall name for a standard ethernet interface
```

## Network Configuration
```sh
# ubuntu.com/server/docs/network-configuration

# files go in here
/etc/netplan/

# apply with
sudo netplan apply
```


## Number Systems
bit
nibble
byte

|         |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
| ------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| bits    | 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10    | 11    | 12    | 13    | 14    | 15    | 16    |
| values  | 2     | 4     | 8     | 16    | 32    | 64    | 128   | 256   | 512   | 1024  | 2048  | 4096  | 8192  | 16536 | 32768 | 65536 |
| hex     | 2     | 4     | 8     | 10    | 20    | 40    | 80    | 100   | 200   | 400   | 800   | 1000  | 2000  | 4000  | 8000  | 10000 |


## Netmask
An ip4-adress is a 32 bit integer usually expressed as 4 bits with dots in between, such as `192.168.2.25`  
With the use of a netmask you can restrict the available adress space for a network.

As an example, the 24-bit subnet `192.168.2.0` has the netmask `255.255.255.0`  
A shorter way to express the same net is `192.168.2.0/24`

## Netadress and Broadcast
two adress values are speciall, the one with all bits set and the one with no bits set
The adress with all bits set is called Broadcast adress
The adress with no bits set is called Netadress

## Routing

To see routing settings:
```sh
$ ip route
# alternatively
$ netstat -rn
```


# Basic Tools
```sh
$ ping

$ ip
$ ip addrs
$ ip link
$ ip route

$ netstat

$ host
```

## Troubleshooting

* server side
```sh
$ netstat -utl
# -u = udp
# -t = tcp
# -l = list
```

* client side
```sh
$ nc -z <host> <port> && echo "Yes!"
$ telnet <host> <port>
```

tcpdump - dump trafic with filtering
example
`$ tcpdump port 80`
has to be run with root priveledges

If you have a gui, use Wireshark instead of tcpdump

## iptables

builtin firewall
```sh
# List all rules
sudo iptables -L

# Add a rule to block all traffic from ip 10.0.1.11
sudo iptables -A INPUT -i en01 -s 10.0.1.11 -j DROP
```

chmod
500
