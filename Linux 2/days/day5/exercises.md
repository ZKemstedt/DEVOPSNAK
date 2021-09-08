## Ex 1
* Find as many risks you can for holding a course at Nackademin
* Evaluate those risks
* Suggest fixes
  
| Risk             | Sannolikhet | Konsekvens | Riskvärde | Åtgärder        |
| ---------------- | ----------- | ---------- | --------- | --------------- |
| Oklar kursplan   | 3           | 4          | 12        | Klargöranden    |
| Ingen Lärare     | 3           | 5          | 15        | Säkrad tillgång |
| Teknikproblem    | 4           | 1          | 4         | -               |
| Sjuk student     | 3           | 4          | 12        | Material på nät |
| Inställd lektion | 2           | 2          | 4         | -               |


## Ex 2
iptables


## Ex 3
* Stäng av din egen Linux-maskins tillgång till en webbsite med iptables
* Testa att blockering fungerar
* Ta bort blockeringen igen


## Ex 4
* Tänk dig att du gör en ip...


## Ex 5
* Gå igenom listan över existerande services på din masking. Vilka av dem används idag?


## Ex 6
Gå igenom listan på öppna portar som lyssnar utåt på din maskin. ...


## Ex 7


## Ex 8
* Antag att ni skall härda två Linuxservrar för drift. Nr1 skall användas som webbserver. Nr2 skall användas för en MySQL-databas som nr1 hämtar data från.
* Hur härdar ni respective server? Gör en åtgärdslista för vardera (och testa gärna konkreta kommandon).

- Nr1 = Webbsesrver
accept http && https in out

- Nr2 = SQL

- Båda
  - Network
    * ports
      - accept ssh on local network
      - accept db-conn (ip specific)
      - deny others
    * Do not respond to pings
  - Användare
    * remove root pwd ? *Tillåt ej att logga in med root*
    * pwd policy
  - shutdown/remove unneccessary processes/programs
  - Logging and monitoring


```bash
# Tillåt ssh från specifikt nätverk:
iptables -A INPUT -i eth0 -p tcp -s 192.168.100.0/24 --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT

# Tillåt all inkommande http:
iptables -A INPUT -i eth0 -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT

# Tillåt all inkommande https:
iptables -A INPUT -i eth0 -p tcp --dport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp --sport 443 -m state --state ESTABLISHED -j ACCEPT

# Tillåt DB data transfer specific IP
iptables -A INPUT -p tcp -s 192.168.100.77 --dport 3306 -j ACCEPT
iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport 3306 -j DROP

# Tillåt inget annat
iptables -A INPUT -j DROP
iptables -A OUTPUT -j DROP
```

