#!/bin/bash

while (($(date +%S) % 10 != 0)); do
	echo waiting
	sleep 1
done

echo "It's finally time"
