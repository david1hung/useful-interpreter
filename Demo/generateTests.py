# TestCase class
# contains setup lines and result line 
class testCase:
	setup = []
	result = 0
	def __init__(self):
		self.setup = []
		self.result = 0

# Prints all the testCases with proper formatting
def printTestCases(t):
	count = 1
	for i in t:
		print ("\nTest Case: " + str(count))
		count += 1
		for j in i.setup:
			print(j)
		print(i.result)


# Loads current test cases
f = open('testCases.ml', 'r')

# Read all the lines in the file
allLines = []
line = f.readline()
while line : # read each line
	if line != '\n' :
		line = line.rstrip() #remove \n
	allLines.append(line)
	#print(line)

	line = f.readline()


# Parse all the lines into testCaseList
testCaseList = [];
x = testCase()
for i in allLines :
	if i == '\n': #just a line, skip
		continue

	else :
		#print("Check: " + i)

		if i.startswith("- :") : # Case result, save to result, start new testCase
			index = i.index('=') # find the equal, get everything after
			i = i[index+1:]
			x.result = i
			#print i

			# start new testcase
			testCaseList.append(x)
			x = testCase()
		else :
			if "val" in i: # it's a function declaration
				continue  # not safe enough, I think Ocaml has other returns?
			i = i.replace(";;",  '')
			i = i.replace("# ",  '')

			#print(i)
			x.setup.append(i)


#testCaseList.append(x)

#printTestCases(testCaseList)

# Create Tests.ml file to run test in OCaml
fout = open('tests.ml', 'w')


testGen_init = """
open Printf

#use "code.ml" ;;

let testNum = ref (1);;
let file = "testOutput.txt";;
let oc = open_out file;;

let printToFile msg = 
	fprintf oc "Test %d: %s\\n" !testNum msg;
	testNum := (!testNum+1);
;;


"""


fout.write(testGen_init)
testGen_mid = ""

# Output for each test case
for i in testCaseList:
	cur = ""
	for j in range(len(i.setup)-1):
		cur += i.setup[j] + "\n"
		if j == (len(i.setup)-2): # add ;; if it's the second to last line
			cur += ";;"

	cur += "\n"
	# Main test case line, prints success or fail on if code == result
	cur += "if (" + i.setup[len(i.setup)-1] + " = " + i.result + """ ) then printToFile "Success" else printToFile "Failed";;"""

	testGen_mid += cur

testGen_mid += "\n"
fout.write(testGen_mid)

testGen_end = """\nclose_out oc;
					exit 0;;
					"""
fout.write(testGen_end)


f.close()
fout.close()

	