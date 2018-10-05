#TODO add documentation
#TODO add winning
#TODO add an opponent
#TODO add input control
#TODO input('connect') that way you say if its connect 4, 5, 1, etc.

def display_grid():
	final = ''
	for x in range(len(grid[0])):
		for y in range(len(grid)):
			final += str(grid[y][x]) + ' '
		final += '\n'

	print(final)


grid = [[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,1,1],
		[0,0,0,0,0,0,0]]

display_grid()

def place_chip(choice, curr):
	if curr == -8:
		return 'filled'

	if grid[choice][curr] == 1:
		return place_chip(choice, curr - 1)
	else:
		grid[choice][curr] = 1


def turn(curr):
	if curr/2 == int(curr/2):
		pass
	else:
		pick = int(input('1-7: ')) - 1
		if place_chip(pick, -1) == 'filled':
			print('Choose a column that is not filled up')
			return turn(curr)

	display_grid()

	#TODO fix this
	end = None

	if end == 'win' or end == 'loss':
		return end

	return turn(curr + 1)

if turn(1) == 'win':
	print('You Win')
else:
	print('You Lose')