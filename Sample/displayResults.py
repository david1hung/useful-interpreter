# TestCase class
# contains setup lines and result line 
class TestCase:
	setup = []
	result = 0
	def __init__(self):
		self.setup = []
		self.result = 0

# Loads current test cases
f_testCases = open('testCases.ml', 'r')


# Read all the lines in the file
allLines = []
line = f_testCases.readline()
while line : # read each line
	if line != '\n' :
		line = line.rstrip() #remove \n
	allLines.append(line)
	#print(line)
	line = f_testCases.readline()


# Parse all the lines into testCaseList
testCaseList = [];
x = TestCase()
for i in allLines :
	if i == '\n': #just a line
		continue
	else :
		#print("Check: " + i)
		if i.startswith("- :") : # Case result, save to result, start new testCase
			x.result = i
			#print i

			# start new testcase
			testCaseList.append(x)
			x = TestCase()
		else :
			#print(i)
			i = i.replace("<", "&lt")
			i = i.replace(">", "&gt")
			x.setup.append(i) # Save line to display


# read in the test outputs
# display it in colors, along with testCases
f_output = open('testOutput.txt')

line = f_output.readline()
testResults = []
while line : # read each line
	testResults.append(line)
	#print(line)
	line = f_output.readline()


# Write to HTML with formatting
f_out = open('testResults.html', 'w')
testGen_init = """
<html>
<head><title>Test Results</title></head>
<body>
<h2> Test Results </h2>
"""

testGen_mid = ""
f_out.write(testGen_init)

#print(len(testResults))
# Apply green for success, red for fail
for i in range(len(testResults)):
	cur = ""
	color = "Blue"
	if "Success" in testResults[i]:
		color = "Green"
	elif "Failed" in testResults[i]:
		color = "Red"

	cur += "<pre style='color:" + color + "'>\n"

	cur += "<strong>" + testResults[i].rstrip() + "</strong>"
	for j in range(len(testCaseList[i].setup)):
		cur += "   " + testCaseList[i].setup[j] + "\n"

	cur += "   " + testCaseList[i].result;
	
	cur += "\n</pre>\n";

	testGen_mid += cur

testGen_mid += "\n"
f_out.write(testGen_mid)

testGen_end = """
</body>
"""
f_out.write(testGen_end)


f_testCases.close()
f_out.close()

	