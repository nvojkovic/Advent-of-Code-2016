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

result = 2**100
for x in permutations(list(locations)):
	sum = 0
	for i in range(len(x)-1):
		sum += distances[(x[i], x[i+1])]
	result = min(result, sum)
print(result)