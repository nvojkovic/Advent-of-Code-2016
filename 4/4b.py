import hashlib
start = "bgvyzdsv"
i=0
while True:
	string = start + str(i)
	if hashlib.md5(string.encode('utf-8')).hexdigest().startswith("000000"):
		print(i)
		break
	i+=1
