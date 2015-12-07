with open("input1.txt") as f:
	position = 0
	for i,x in enumerate(f.read()):
		if x == "(":
			position +=1
		else:
			position -= 1
		if position == -1:
			break
	print(i)