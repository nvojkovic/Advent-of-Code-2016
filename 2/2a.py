with open("input2.txt") as f:
	sum = 0
	for line in f.readlines():
		l, w, h = map(int, line.split('x'))
		sum += (2*(l*w + h*w + l*h) + min(l*w,h*w, l*h))
	
	print(sum)