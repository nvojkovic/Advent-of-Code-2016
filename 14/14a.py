import re
regex = re.compile(r'\w+ can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds')
finish = 2503
result = 0

def calculate(array, time):
	cycles = time // len(array)
	extra = time % len(array) + 1
	return cycles*sum(array) + sum(array[:extra])

with open("input.txt") as f:
	for line in f.read().splitlines():
		distance, time, rest = re.findall(regex, line)[0]
		movement = [int(distance)]*int(time) + [0]*int(rest)
		result = max(result, calculate(movement, finish))
	print(result)