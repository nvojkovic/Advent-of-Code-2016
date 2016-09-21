from math import sqrt
def sumOfDivisors(n):
	sum = 0
	for x in range(1,round(sqrt(n+1))):
		if n % x == 0 and n / x <= 50:
			sum += x
		if n % x == 0 and x <= 50:
			sum += n / x
	return sum*11

input = 29000000
x=1
while sumOfDivisors(x) < input:
	x+=1
	if(x%1000 == 0):
		print(x)
print(x)