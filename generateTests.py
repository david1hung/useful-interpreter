class testCase:
	setup = []
	result = 0
	def __init__(self):
		self.setup = []
		self.result = 0

f = open('testCases.txt', 'r')

allLines = []
line = f.readline()

while line : # read each line
	if line != '\n' :
		line = line.rstrip() #remove \n
	allLines.append(line)
	#print(line)

	line = f.readline()

def printTestCases(t):
	count = 1
	for i in t:
		print ("\nTest Case: " + str(count))
		count += 1
		for j in i.setup:
			print(j)
		print(i.result)

testCaseList = [];
x = testCase()

for i in allLines :
	if i == '\n': #just a line, means end test obj
		#print("Found Just a line")
		a = 0

	else :
		#print("Check: " + i)

		if i.startswith("- :") :
			index = i.index('=') #find the equal, get everything after
			i = i[index+1:]
			x.result = i
			#print i

			# start new testcase
			testCaseList.append(x)
			x = testCase()
		else :
			if "val" in i: # it's a function declaration
				continue

			# if i.startswith('#'):  #find setup lines, some lines don't have #
			i = i.replace(";;",  '')
			i = i.replace("# ",  '')

			#print(i)
			x.setup.append(i)

#testCaseList.append(x)


#printTestCases(testCaseList)
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

testGen_mid = ""

fout.write(testGen_init)


for i in testCaseList:
	cur = ""
	for j in range(len(i.setup)-1):
		cur += i.setup[j] + "\n"
		if j == (len(i.setup)-2):
			cur += ";;"

	cur += "\n"
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

	