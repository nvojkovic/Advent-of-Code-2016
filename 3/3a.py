with open("input3.txt") as f:
	x = 0
	y = 0
	visited = set([(0,0)])
	for c in f.read():
		if c == 'v':
			y -= 1
		elif c == '^':
			y += 1
		elif c == '<':
			x -= 1
		elif c == '>':
			x +=1
		visited.add((x,y))
	print(len(visited))