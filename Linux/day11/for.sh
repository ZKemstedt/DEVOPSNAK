#!/bin/bash

for v in 1 2 3 4; do
	echo $v
done

for f in *.sh; do
	ls $f
done

for z in {A..D}{1..3}; do
	echo $z
done

# for (( i=0; i<5 ; i=i+1 )); do
# 	echo $i
# done
