from math import sqrt
def sumOfDivisors(n):
	sum = 0
	for x in range(1,round(sqrt(n+1))):
		if n % x == 0:
			sum += x + n/x
	return sum*10

input = 29000000
print(sumOfDivisors(6))
x=1
while sumOfDivisors(x) < input:
	x+=1
	if(x%1000 == 0):
		print(x)
print(x)