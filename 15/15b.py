result = 0 
for a in range(0,101): 
    for b in range(0,101 - a): 
        for c in range(0,101 - a - b):
			d = 100 - a - b - c 
			val = max(5*a - b - d,0) * max(-a + 3*b - c, 0) * 8*c*d 
			if 5*a + b + 6*c + 8*d == 500: 
				result = max(result, val)
print(result)