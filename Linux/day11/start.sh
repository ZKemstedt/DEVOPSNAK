#!/bin/bash

if [[ ! -f .timer ]]
then
	date +%s >> .timer
	echo "Timer started."
else
	echo "timer already started."
fi

