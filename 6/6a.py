from collections import defaultdict
lights = defaultdict(int)

on = lambda x: 1
off = lambda x: 0
toggle = lambda x: 1-x

def change(start, end, function):
	startx, starty = map(int, start.split(","))
	endx, endy = map(int, end.split(","))

	for x in range(startx, endx+1):
		for y in range(starty, endy+1):
			lights[(x,y)] = function(lights[(x,y)])

with open("input.txt") as f:
	for string in f.readlines():
		lis = string.split(" ")
		if string.startswith("turn on"):
			change(lis[2], lis[4], on)
		elif string.startswith("turn of"):
			change(lis[2], lis[4], off)
		elif string.startswith("toggle "):
			change(lis[1], lis[3], toggle)

print(sum(lights.values()))