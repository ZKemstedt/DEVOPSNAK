#!/bin/bash

# Author: Zephyro Kemstedt

# security group
openstack security group create ex1
openstack security group rule create --ingress --protocol tcp --dst-port 80 ex1
openstack security group rule create --ingress --protocol tcp --dst-port 443 ex1

# network
openstack network create ex1net
# subnet
openstack subnet create --network ex1net --subnet-range 10.0.0.0/24 ex1netsub1

# server
openstack server create ex1server --flavor v1-small-1 --image ubuntu-20.04-server-latest --network ex1net --security-group ex1
