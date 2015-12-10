def generate(number):
	cnt = 0
	a = number[0]
	result = []
	for x in number:
		if a != x:
			result.append(str(cnt))
			result.append(a)
			cnt = 0
			a = x
		cnt += 1
	result.append(str(cnt))
	result.append(a)
	return ''.join(result)

start = "1321131112"
for x in range(0, 50):
	start = generate(start)
print(len(start))