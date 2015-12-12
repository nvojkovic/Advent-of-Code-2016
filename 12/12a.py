import json

sum=0

def addIfInt(x):
	if type(x) is int:
		global sum
		sum += x

def parse(code):
	if type(code) is list:
		for x in code:
			if type(x) in [dict,list]:
				parse(x)
			else:
				addIfInt(x)
	elif type(code) is dict:
		for key, value in code.items():
			addIfInt(key)
			if type(value) in [dict,list]:
				parse(value)
			else:
				addIfInt(value)

with open("input.txt") as f:
	code = f.read()
	parse(json.loads(code))
	print(sum)
