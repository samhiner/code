#TODO add documentation
#TODO add winning
#TODO add an opponent
#TODO maybe add input control
#TODO input('connect') that way you say if its connect 4, 5, 1, etc. also board size

CONNECT = 4

#prints out the board so the user can see it
def display_board():
	final = ''
	for x in range(len(board[0])):
		for y in range(len(board)):
			final += str(board[y][x]) + ' '
		final += '\n'

	print(final)

#recusive function put the choice at a position where you find the first vertical spot not taken and put the chip there
def place_chip(choice, curr):
	#if the whole column is filled then notify the turn function
	#TODO make -8 depend on board size
	if curr == -8:
		return 'filled'

	if board[choice][curr] == 1:
		return place_chip(choice, curr - 1)
	else:
		board[choice][curr] = 1

#look through the board to see if anyone has "amt" chips in a row
def check_win(amt):
	vert_connect = 0
	horizon_connect = 0

	#vertical and horizontal checks
	for x in range(len(board)):
		for y in range(len(board[0])):
			if board[x][y] == 1:
				horizon_connect += 1
			else:
				horizon_connect = 0

			if board[y][x] == 1:
				vert_connect += 1
			else:
				vert_connect = 0

			if vert_connect >= amt or horizon_connect >= amt:
				return 'win'

	#TODO could save on resource by not checking diags that are smaller than amt
	#top-right -> bottom-left diagonal check
	directions = [1, -1]
	index_adjs = [0, -1]
	for a in range(2):
		'''
		first you check from top left corner to bottom right corner (shift of 0)
		then you try the two diagonals next to that, the ones right above and below (shift of 1)
		above line does both diagonals bc it tries both shift and -shift with the "shift_types" array and following for loop
		repeat this whole process with top-right -> bottom-left using above for loop
		'''
		for shift in range(len(board)):
			diag_connects = [0,0]
			for x in range(len(board)):
				shift_types = [shift, -shift]
				for y in range(2):
					try:
						#direction[a] will change it from 1 to -1 so you can check top right to bottom left instead of other way and index_adj is necessary bc 0 is first but -1 is last, not -0
						if board[directions[a] * (x + shift_types[y]) + index_adjs[a]][x] == 1:
							diag_connects[y] += 1
						else:
							diag_connects[y] = 0
					except IndexError:
						pass

				if amt in diag_connects:
					return 'win'


#recursive function to switch players from turn to turn until someone wins
def turn(curr):
	if curr/2 == int(curr/2):
		pass
		#TODO add computer strats here
		#NOTE when your doing that remember both people need their own chip color (they can't both be 1)
	else:
		pick = int(input('1-7: ')) - 1
		if place_chip(pick, -1) == 'filled':
			print('Choose a column that is not filled up')
			return turn(curr)

	display_board()

	end = check_win(CONNECT)

	if end == 'win' or end == 'loss':
		return end

	return turn(curr + 1)

# RUNNING THE GAME

#create and show the empty board

board = [[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0]]

display_board()

#run the game and print if you won or lost

if turn(1) == 'win':
	print('You Win')
else:
	print('You Lose')