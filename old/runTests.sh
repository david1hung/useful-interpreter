#!/bin/bash
python generateTests.py
ocaml -init 'tests.ml'
python displayResults.py
open testResults.html

