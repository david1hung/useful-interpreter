# Useful-interpreter

## Intro
The Useful-interpreter was an exploration on how to make the REPL environment better. It involves shortening the development cycle by automatically launching the interpreter (e.g. OCaml) of choice upon file save. It also provides an easy way to generate test cases just from the output of the interpreter!


## Currently Implemented
* Auto-launch based on save, using kqwait, bash and AppleScript. (Requires OS X)
* Test generator: generates an OCaml test file, based on input to testCases.ml. Input format is the input and output lines in the interpreter. e.g. 
(# rev [1;2;3];; - : int list = [3; 2; 1]). Works with multi-line too, but a naive implementation
* Test visualization: the test success and fails are displayed, along with the original code, in an HTML file. Green for pass and red for fail. 


## Workflow
1. Save code.ml, which auto-opens an interpreter in a new terminal
2. Type in terminal
3. Copy lines from interpreter input and output lines to testCases.ml. Save. 
4. On same, test is automatically generated
5. Then tests runs automatically 
6. And HTML results is displayed


## Setup
Currently the setup only works on Mac because it uses AppleScript and kqwait which only have Mac versions. 

Auto setup
* Run init.sh and all the files needed will be opened

Manual setup
* Open code.ml (main code base to edit)
* Open testCases.ml (test cases code)* Run ./checkSave code.mlo This listens to whether or not code.ml is updated	* Run ./checkTest testCases.ml code.mlo This listens to whether or not testCases.ml or code.ml is updated, in order to automatically run or re-run the testCases.* Done!* Type some code in code.ml and click Save

###The Sample directory has a version with some sample code and test outputs