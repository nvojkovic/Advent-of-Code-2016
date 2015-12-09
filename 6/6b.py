from collections import defaultdict
lights = defaultdict(int)

def change(start, end, amount):
	startx, starty = map(int, start.split(","))
	endx, endy = map(int, end.split(","))

	for x in range(startx, endx+1):
		for y in range(starty, endy+1):
			lights[(x,y)] = max(lights[(x,y)] + amount, 0)


with open("input.txt") as f:
	for string in f.readlines():
		lis = string.split(" ")
		if string[:7] == "turn on":
			change(lis[2], lis[4], 1)
		elif string[:7] == "turn of":
			change(lis[2], lis[4], -1)
		elif string[:7] == "toggle ":
			change(lis[1], lis[3], 2)

print(sum(lights.values()))