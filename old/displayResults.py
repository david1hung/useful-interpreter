class testCase:
	setup = []
	result = 0
	def __init__(self):
		self.setup = []
		self.result = 0

f_testCases = open('testCases.txt', 'r')

allLines = []
line = f_testCases.readline()

while line : # read each line
	if line != '\n' :
		line = line.rstrip() #remove \n
	allLines.append(line)
	#print(line)

	line = f_testCases.readline()


testCaseList = [];
x = testCase()

for i in allLines :
	if i == '\n': #just a line, means end test obj
		#print("Found Just a line")
		a = 0
	else :
		#print("Check: " + i)

		if i.startswith("- :") :
			#index = i.index('=') #find the equal, get everything after
			#i = i[index+1:]
			x.result = i
			#print i

			# start new testcase
			testCaseList.append(x)
			x = testCase()
		else :
			#if "val" in i: # it's a function declaration
			#	continue

			# if i.startswith('#'):  #find setup lines, some lines don't have #
			#i = i.replace(";;",  '')
			#i = i.replace("# ",  '')

			#print(i)
			x.setup.append(i)


# read in the test outputs
# display it in colors
f_output = open('testOutput.txt')

line = f_output.readline()
testResults = []
while line : # read each line
	testResults.append(line)
	#print(line)
	line = f_output.readline()



f_out = open('testResults.html', 'w')
testGen_init = """
<html>
<head><title>Test Results</title></head>
<body>
<h1> Test Results </h1>
"""

testGen_mid = ""
f_out.write(testGen_init)

#print(len(testResults))
for i in range(len(testResults)):
	cur = ""
	color = "Blue"
	if "Success" in testResults[i]:
		color = "Green"
	elif "Failed" in testResults[i]:
		color = "Red"

	cur += "<pre style='color:" + color + "'>\n"

	cur += "<strong>" + testResults[i] + "</strong>"
	for j in range(len(testCaseList[i].setup)):
		cur += "   " + testCaseList[i].setup[j] + "\n"

	cur += "   " + testCaseList[i].result;

	cur += "</pre>\n";

	testGen_mid += cur

testGen_mid += "\n"
f_out.write(testGen_mid)

testGen_end = """
</body>
"""
f_out.write(testGen_end)


f_testCases.close()
f_out.close()

	