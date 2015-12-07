from collections import defaultdict
lights = defaultdict(int)

def on(start, end):
	startx, starty = map(int, start.split(","))
	endx, endy = map(int, end.split(","))

	for x in range(startx, endx+1):
		for y in range(starty, endy+1):
			lights[(x,y)] = 1

def off(start, end):
	startx, starty = map(int, start.split(","))
	endx, endy = map(int, end.split(","))

	for x in range(startx, endx+1):
		for y in range(starty, endy+1):
			lights[(x,y)] = 0

def toggle(start, end):
	startx, starty = map(int, start.split(","))
	endx, endy = map(int, end.split(","))

	for x in range(startx, endx+1):
		for y in range(starty, endy+1):
			lights[(x,y)] = 1 if lights[(x,y)]== 0 else 0

with open("input.txt") as f:
	for string in f.readlines():
		if string[:7] == "turn on":
			lis = string.split(" ")
			on(lis[2], lis[4])
		elif string[:7] == "turn of":
			lis = string.split(" ")
			off(lis[2], lis[4])
		elif string[:7] == "toggle ":
			lis = string.split(" ")
			toggle(lis[1], lis[3])

print(sum(lights.values()))