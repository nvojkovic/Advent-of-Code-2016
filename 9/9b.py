from itertools import permutations
locations = set()
distances = dict()

with open("input.txt") as f:
	for line in f.read().splitlines():
		first, second = line.split(" to ")
		second, distance = second.split(" = ")
		locations.add(first)
		locations.add(second)
		distances[(first, second)] = int(distance)
		distances[(second, first)] = int(distance)

result = 0
for x in permutations(list(locations)):
	sum = 0
	for x,y in zip(x,x[1:]):
		sum += distances[(x,y)]
	result = max(result, sum)
print(result)