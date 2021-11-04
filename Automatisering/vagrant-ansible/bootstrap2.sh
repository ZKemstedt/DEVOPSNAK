#!/usr/bin/env bash

yum install -y net-tools

useradd -c "deploy" -d /home/deploy -m deploy

echo "%deploy ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/vagrant

sudo timedatectl set-timezone Europe/Stockholm

sudo -u deploy bash << EOF
mkdir ~/.ssh
chmod 700 ~/.ssh
chown deploy:deploy ~/.ssh
cat /vagrant/deploy_id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
EOF
