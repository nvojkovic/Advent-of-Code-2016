with open("input2.txt") as f:
	sum = 0
	for line in f.readlines():
		l, w, h = map(int, line.split('x'))
		sum += l*w*h + 2*(l + w + h - max(l, h, w))
	
	print(sum)