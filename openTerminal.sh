#!/bin/bash
DIR=$(pwd)
echo "Opening New Terminal Window"
osascript -e 'tell application "terminal"' -e "do script \"cd '$DIR'; ./openInterp.sh $1 \" " -e 'end tell'
#opens temrinal, CD back to current directly, calls the open script