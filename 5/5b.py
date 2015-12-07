def nice(string):
	between = False
	double = False

	for i in range(0,len(string)-2):
		if string[i] == string[i+2]:
			between=True

	for i in range(0,len(string)-1):
		if string.count(string[i:i+2]) > 1:
			double = True
			
	return between and double

with open("input.txt") as f:
	nices=0
	for line in f.readlines():
		nices += nice(line)
	print(nices)