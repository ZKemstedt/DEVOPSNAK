## Ex 1
* Warm upp exercise:
List all installed packets on your Linux machine, take a look at the things you recognize.
```sh
apt list # Ubuntu
apk list # Alpine
```


## Ex 2
* Install the Apache webbserver
  - the packet is called apache2
* Start the daemon
* verify that the daemon is running
* see more information with `systemctl list-dependencies`, `systemctl cat` and `systemctl show`
```sh
sudo apt install apache2
sudo systemctl enable apache2
sudo systemctl start apache2
systemctl is-active apache2
systemctl list-dependencies apache2
systemctl cat
systemctl show
```


# Ex 3
* create a simple program that writes a timestamp to a logfile of your choosing when it starts and then loops forever (doing nothing)
* make a daemon of this program called simpled
* start and restart your daemon and verify that it writes to the logfile and stays as a backgroundprocess
```sh
# -- ~/day3/ex3.sh --
#!/bin/bash
logfile=/home/zephyro/day3/simpled.log;
timestamp=`date +%Y-%d_%H-%M-%S`;
echo $timestamp ": started" >> $logfile
while true
do
    sleep 2
done
# ---

# -- /lib/systemd/system/simpled.service --
# /etc/systemd/system/simpled.service
[Unit]
Description=day3_ex3

[Service]
User=zephyro
WorkingDirectory=/home/zephyro/day3
ExecStart=/home/zephyro/day3/ex3.sh
Restart=always

[Install]
WantedBy=multi-user.target
# ---

sudo systemctl daemon-reload
sudo systemctl start simpled
systemctl status simpled
sudo systemctl restart simpled
cat simpled.log
sudo systemctl stop simpled
```


## Ex 4
...


## Ex 5
* Make a script that check if the apache2 daemon is running and writes the result to a logfile of your choosing with a timestamp
* testrun your script
* add a cronjob that runs your script every minutes monday-friday every week.
* verify that your logfile is increasing
* remove the cronjob
* hints:
  * ```if [ `systemctl is-active apache2` == "active" ]```
  * crontab: `* * * * 1-5 <script_path>`

```sh
# -- ~/day3/ex5.sh --
#!/bin/bash
logfile=/home/zephyro/apache.log
timestamp=`date +%Y-%m-%d_%H-%M-%s`;
if [ `systemctl is-active apache2` == "active" ]
then
    echo "apache active - $timestamp" >> $logfile
else
    echo "apache not active - $timestamp" >> $logfile
fi
# ---

sudo chmod +x apachecheck.sh    # make executeable
./apachecheck.sh                # run
cat apache.log                  # verify output

# add to crontab
crontab -l | { cat; echo "* * * * 1-5 /home/zephyro/day3/ex5.sh"; } | crontab -

# verify that it's running
tail -f apache.log &

# remove from crontab
crontab -l | grep -v 'ex5.sh' | crontab -
```


## Ex 6
* Take a look in `/var/log/apache2`
  * where do you look if you get an error in a php-site on your webbserver?
`error.log`


## Ex 7
