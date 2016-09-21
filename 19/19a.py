from collections import defaultdict
import re
regex = re.compile(r"[A-Z][a-z]?")
dic = defaultdict(list)
solutions = set()

with open("input.txt") as f:
	for x in f.read().splitlines():
		a = x.split(" => ")
		if(len(a) == 1):
			mol = regex.findall(a[0])
		else:
			dic[a[0]].append(a[1])
	for i,x in enumerate(mol):
		if x in dic:
			for y in dic[x]:
				solutions.add(''.join(mol[:i]) + y + ''.join(mol[i+1:]))
	print(len(solutions))