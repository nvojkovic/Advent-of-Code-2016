def parse(var):

	if var.isdigit():
		return int(var)
	elif type(exps[var]) is int:
		return exps[var]

	tokens = exps[var].split()

	if len(tokens) == 1 :
		return parse(tokens[0])

	elif tokens[1] == "AND":
		exps[var] = parse(tokens[0]) & parse(tokens[2])

	elif tokens[1] == "OR":
		exps[var] = parse(tokens[0]) | parse(tokens[2])

	elif tokens[1] == "RSHIFT":
		exps[var] = parse(tokens[0]) >> parse(tokens[2])

	elif tokens[1] == "LSHIFT":
		exps[var] = parse(tokens[0]) << parse(tokens[2])

	elif tokens[0] == "NOT":
		exps[var] = 2**16 - 1 - parse(tokens[1])

	return exps[var]

exps = dict()

with open("input.txt") as f:
	for string in f.readlines():
		exp, var = string.strip().split(" -> ")
		
		if exp.isdigit():
			exps[var] = int(exp)
		else:
			exps[var] = exp
exps["b"] = 16076
exps["a"] = parse("a")
print(exps["a"])
