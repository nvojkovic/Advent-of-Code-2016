from itertools import permutations
from collections import deque

hapiness = dict()
people = set()

def evaluate(seating):
	a = deque(seating)
	a.rotate(1)
	sum=0
	for x in zip(seating, list(a)):
		sum += hapiness[x]
		sum += hapiness[tuple(reversed(x))]
	return sum

def addMe():
	for x in people:
		hapiness[(x, "Me")] = 0
		hapiness[("Me", x)] = 0
	people.add("Me")

with open("input.txt") as f:
	for line in f.read().splitlines():
		line = line.split()
		person1, direction, amount, person2 = line[0], line[2], int(line[3]), line[10][:-1]
		people.add(person1)
		if direction == "lose":
			hapiness[(person1, person2)] = -amount
		elif direction == "gain":
			hapiness[(person1, person2)] = amount
addMe()
result = 0
people = list(people)
for p in permutations(people[1:]):
	result = max(evaluate([people[0]] + list(p)), result)
print(result)