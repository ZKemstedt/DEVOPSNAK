#!/bin/bash
if [ "$1" = "add" ]; then
	if ! [ -f ~/.ssh/deploy_id_rsa ]; then
		ssh-keygen -t rsa -b 4096 -N "" -f ~/.ssh/deploy_id_rsa
	fi
	cp ~/.ssh/deploy_id_rsa.pub ./
elif [ "$1" = "del" ]; then
	if  [ -f ~/.ssh/deploy_id_rsa ]; then
		rm ~/.ssh/deploy_id_rsa*
	rm ./deploy_id_rsa.pub
	fi
fi
