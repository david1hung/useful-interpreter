#!/bin/bash
python $1 #generate.py
ocaml -init 'test2.ml'
python displayResults.py
open testResults.html