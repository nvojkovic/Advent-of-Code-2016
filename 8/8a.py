import re
sum=0
regex = re.compile(r"(\\[x][0-9a-f][0-9a-f])")

with open("input.txt") as f:
	for line in f.read().splitlines():
		line = line[1:-1]
		sum += 2 + line.count('\\\\') + line.count("\\\"") + len(re.findall(regex, line))*3
	print(sum)