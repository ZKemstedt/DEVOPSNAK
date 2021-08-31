#!/bin/bash

for i in $(cat /var/users.txt)
do
    user=$(echo $i | awk -F: '{print $1}')
    useradd --no-log-init -m -g sudo $user
    echo "$i" | chpasswd
done
rm /var/users.txt

if [ ! -f "/etc/ssh/ssh_host_rsa_key" ]; then
    # generate fresh rsa key
    ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa
fi
if [ ! -f "/etc/ssh/ssh_host_dsa_key" ]; then
    # generate fresh dsa key
    ssh-keygen -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa
fi

# prepare run dir
if [ ! -d "/var/run/sshd" ]; then
    mkdir -p /var/run/sshd
fi

exec "$@"

# << EOF >> cat.txt
# awk -F: '{print $1}' $user
# for i in $(cat users.txt)
# do
#     awk -F: '{print $1}' $user
#     # user=$(grep -o "*:" i | )
#     useradd --no-log-init -m -g sudo $user
#     echo "$i" | chpasswd
#     usermod -aG sudo $user
# done