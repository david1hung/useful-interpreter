#!/bin/bash
DIR=$(pwd)
echo "Opening code.ml"
open "code.ml"
echo "Opening code.ml listener"
osascript -e 'tell application "terminal"' -e "do script \"cd '$DIR'; ./checksave.sh code.ml \" " -e 'end tell'

echo "Opening testCase.ml"
open "testCases.ml"
echo "Opening testCases.ml listener to automatically generate tests"
osascript -e 'tell application "terminal"' -e "do script \"cd '$DIR'; ./checkTest.sh testCases.ml code.ml \" " -e 'end tell'

echo "Open testResults.html to display test Results"
open "testResults.html"

echo "Environment setup! Enjoy!"

