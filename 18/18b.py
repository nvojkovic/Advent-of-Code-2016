def neighs(x,y):
	sum = 0
	for a in [-1, 0, 1]:
		for b in [-1, 0, 1]:
			if (a != 0 or b != 0) and x+a in range(0, size) and y+b in range(0, size):
				if board[x+a][y+b] == '#':
					sum += 1
	return sum

def new():
	new_board = [['.']*size for x in range(size)]
	for x in range(size):
		for y in range(size):
			neigh = neighs(x,y)
			if (board[x][y] == '#' and neigh < 2 or neigh > 3) or (board[x][y] == '.' and neigh != 3):
				new_board[x][y] = '.'
			else:
				new_board[x][y] = '#'
	return new_board

def count():
	result = 0
	for x in range(size):
		for y in range(size):
			if board[x][y] == '#':
				result += 1
	return result

size = 100
board = [['.']*size for x in range(size)]
with open("input.txt") as f:
	for i, x in enumerate(f.read().splitlines()):
		for j, y in enumerate(x):
			board[i][j] = y

for i in range(100):
	board = new()
	board[0][size-1] = "#"
	board[0][0] = "#"
	board[size-1][0] = "#"
	board[size-1][size-1] = "#"


print(count())