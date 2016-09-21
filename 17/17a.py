def find(x, nums):
	if sum(nums) == 150:
		return 1
	if sum(nums) > 150 or x >= len(numbers):
		return 0
	else:
		return find(x+1, nums + [numbers[x]]) + find(x+1, nums)

with open("input.txt") as f:
	numbers = [int(x) for x in f.read().splitlines()]
	print(find(0,[]))
