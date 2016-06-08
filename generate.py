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
	print(line)

	line = f.readline()



allTestCases = [];
x = testCase()

for i in allLines :
	if i == '\n': #just a line, means end test obj
		print("Found Just a line -- Starting New Object")
		#allTestCases.append(x);
		#x = testCase()

		
	else :
		print(i)

		if i.startswith("- :") :
			index = i.index('=') #find the equal, get everything after
			i = i[index+1:]
			x.result = i
			print i
		else :
			# if i.startswith('#'):  #find setup lines, some lines don't have #
			i = i.replace("#",  '')
			i = i.replace(';;', '')

			print(i)
			x.setup.append(i)

allTestCases.append(x);

j = 1
for i in allTestCases:
	print("\nTest Case: " + str(j))
	print(i.setup)
	print(i.result)
	j += 1
		
		
f.close()

	