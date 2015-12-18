import re
regex = re.compile(r'\w+ can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds')
finish = 2503
result = 0

def calculate(array, time):
	cycles = time // len(array)
	extra = time % len(array) + 1
	return cycles*sum(array) + sum(array[:extra])

def genMovement(args):
	distance, time, rest = args
	return [distance]*time + [0]*rest

with open("input.txt") as f:
	deers = []
	for line in f.read().splitlines():
		deers.append(map(int, re.findall(regex, line)[0]))

	results = [0]*len(deers)
	movements = list(map(genMovement, deers))
	
	for time in range(1, finish+1):
		distance = list(map(lambda x: calculate(x, time), movements))
		results[distance.index(max(distance))] += 1
	print(max(results))