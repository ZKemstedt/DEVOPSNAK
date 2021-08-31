#!/bin/bash

if [[ -f .timer ]]; then
	start=$(cat .timer)
	since=$(( $(date +%s) - $start ))
	started=$(date -r $start) 
	echo "Timer stopped.
		  $since seconds have passed.
		  started at $started
		 "
	rm .timer
else
	echo "Timer is not running"
fi

