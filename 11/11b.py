def convert(n):
	result = 0
	for i,x in enumerate(n):
		result += (ord(x) - ord('a'))*26**(len(n)-i-1)
	return result

def convert2(n):
	result = ""
	while n > 0:
		result += chr(int(n%26) + ord('a'))
		n //= 26
	return result[::-1]

def isValid(password):
	alphabet = [chr(x) for x in range(97,123)]
	increasing = [''.join(x) for x in zip(alphabet, alphabet[1:], alphabet[2:])]
	doubles = [x*2 for x in alphabet]
	forbidden = "iol"
	return sum(map(password.count, increasing)) > 0 and sum(map(password.count, doubles)) > 1 and sum(map(password.count, forbidden)) == 0

password = convert2(convert("vzbxxyzz")+1)
while not isValid(password):
	password = convert2(convert(password)+1)
print(password)
