with open("input1.txt") as f:
	string = f.read()
	print(string.count("(") - string.count(")"))