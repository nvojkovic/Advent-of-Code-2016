import re
order = ["children", "cats", "samoyeds", "pomeranians", "akitas", "vizslas", "goldfish", "trees", "cars", "perfumes"]
gift = ["3","7","2","3","0","0","5","3","2","1"]

def isValid(string):
	for i in range(len(string)):
		if gift[i] != string[i] and string[i] != "*":
			return False
	return True

with open("input.txt") as f:
	i=1
	for x in f.read().splitlines():
		results = x.split(", ")
		results[0] = results[0][results[0].index(":")+2:]
		results = list(map(lambda x: x.split(": "), results))
		tmp = ["*"]*10
		for x in results:
			tmp[order.index(x[0])] = x[1]
		if isValid(tmp):
			print(i)
			break
		i+=1