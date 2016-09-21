registers = {"a": 0, "b": 0}
memory = []

def run():

	pc = 0
	running = True

	while running:

		if(pc >= len(memory)):
			break

		op = memory[pc].split()
		move = 1

		if op[0] == "inc":
			registers[op[1]] += 1

		elif op[0] == "hlf":
			registers[op[1]] //= 2

		elif op[0] == "tpl":
			registers[op[1]] *= 3

		elif op[0] == "jmp":
			offset = int(op[1])
			if pc+offset < len(memory):
				move = offset
			else:
				running = False

		elif op[0] == "jie":
			offset = int(op[2])
			if registers[op[1][0]] % 2 == 0:
				if pc+offset < len(memory):
					move = offset
				else:
					running = False

		elif op[0] == "jio":
			offset = int(op[2])
			if registers[op[1][0]] == 1:
				if pc+offset < len(memory):
					move = offset
				else:
					running = False
		pc+=move

with open("input.txt") as f:
	i=1
	for x in f.read().splitlines():
		memory.append(x)
run()
print(registers['b'])