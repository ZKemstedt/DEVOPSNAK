#!/bin/bash

timestamp=`date +%Y-%m-%d_%H-%M-%s`;
logfile="/home/zephyro/devops/Linux 2/days/day4/ex4.log" 
state=$(ip addr show | grep -E '(enp0s3).*(state UP)')

if [ -z "$state" ]
then
    echo "enp0s3 inactive $timestamp" >> "$logfile"
else
    echo "enp0s3 active $timestamp" >> "$logfile"
fi
