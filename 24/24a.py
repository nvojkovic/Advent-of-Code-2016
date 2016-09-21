nums = [1,2,3,7,11,13,17,19,23,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]
x=0
def calc(numbers, i):
	global x
	if sum(numbers) == 520:
		#print(numbers, sum(numbers))
		x+=1
		return
	elif sum(numbers) > 520 or i >= len(nums):
		return
	else:
		calc(numbers+[nums[i]], i+1)
		calc(numbers, i+1)

calc([],0)