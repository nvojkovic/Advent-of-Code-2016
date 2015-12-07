def nice(string):
	vowels = sum([string.count(x) for x in "aeiou"])
	forbidden = sum([string.count(x) for x in ["ab", "cd", "pq", "xy"]])
	doubles = sum([string.count(x) for x in [chr(i)*2 for i in range(97,123)]])
	return vowels >= 3 and doubles > 0 and forbidden == 0

with open("input.txt") as f:
	nices=0
	for line in f.readlines():
		nices += nice(line)
	print(nices)