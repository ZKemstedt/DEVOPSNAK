#!/bin/bash

MSG=$1

minfunktion() {
	local arg=$1
	echo "I funktionen: $arg" 
}

minfunktion hej

echo "I skriptet: $MSG"
echo "Argumentet: $arg"
