#!/bin/bash
echo "Generating Tests"
python generateTests.py
echo "Running Tests"
ocaml -init 'tests.ml'
echo "Formatting Results"
python displayResults.py
echo "Displaying Results"
open testResults.html

