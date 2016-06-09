#!/bin/bash
DIR=$(pwd)
echo "Opening New Terminal Window"
osascript -e 'tell application "terminal"' -e "do script \"cd '$DIR'; ./openInterp.sh $1 \" " -e 'end tell'
osascript -e 'tell application "terminal" to delay 1'
osascript -e 'tell application "terminal" to close first window' & exit

#opens temrinal, CD back to current directly, calls the open script