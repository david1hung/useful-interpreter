#!/bin/bash
# kqwait detects saves on $1 and $2, 
# calls openTerminal.sh to open $1 in a terminal
echo "Checking $1"
while ./kqwait $1 $2; do
	echo "Save Detected" 
	./openTerminal.sh $1	
done
