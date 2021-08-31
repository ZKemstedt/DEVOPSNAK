#!/bin/bash

filestart=$1
lines=0

for f in /etc/$filestart*; do
	if [ -f $f ]; then
		lines=$(( $lines + $(cat $f | mc -l) ))
	fi
done

ehco "Files starting with \"$filestart\" in /etc add up to $lines lines"

