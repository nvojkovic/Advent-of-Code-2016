with open("input3.txt") as f:
	#first coordinates are for santa, second for robo-santa
	coords = [[0,0], [0,0]]
	visited = set([(0,0)])

	for (i, c) in enumerate(f.read()):
		if c == 'v':
			coords[i%2][1] -= 1
		elif c == '^':
			coords[i%2][1] += 1
		elif c == '<':
			coords[i%2][0] -= 1
		elif c == '>':
			coords[i%2][0] +=1
		visited.add(tuple(coords[i%2]))
	print(len(visited))