import re
sum=0
with open("input.txt") as f:
	for line in f.readlines():
		line = line.strip()
		sum += len(re.escape(line)) + 2 - len(line)
	print(sum)