#TODO add documentation
#TODO add winning
#TODO add an opponent
#TODO maybe add input control
#TODO input('connect') that way you say if its connect 4, 5, 1, etc. also board size
#HEY HEY HEY HEY GO TO LINE 80

import random

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
def place_chip(choice, chip, curr = -1):
	#if the whole column is filled then notify the turn function
	#TODO make -8 depend on board size
	if curr == -8:
		return 'filled'

	if board[choice][curr] != 0:
		return place_chip(choice, chip, curr - 1)
	else:
		board[choice][curr] = chip

def can_place(column, row):
	try:
		if board[column][row] == 0:
			if row == len(board[0]) - 1:
				return True
			else:
				if board[column][row - 1] != 0:
					return True
	except IndexError:
		return False

	return False


#TODO split this up into a lot of other functions
#look through the board to see if anyone has "amt" chips in a row
def check_line(chip, amt = CONNECT, find_win = False):
	vert_connect = 0
	horizon_connect = 0

	#vertical and horizontal checks
	for x in range(len(board)):
		for y in range(len(board[0])):
			if board[x][y] == chip:
				horizon_connect += 1
			else:
				horizon_connect = 0

			if board[y][x] == chip:
				vert_connect += 1
			else:
				vert_connect = 0

			if horizon_connect >= amt:
				if find_win:
					if can_place(x + 1, y):
						return [x - amt, y]
					elif can_place(x - amt, y):
						return [x - amt, y]
				else:
					return 'win'

			#TODO fix this duplicated code
			if vert_connect >= amt:
				if find_win:
					if can_place(y, x + 1):
						return [y, x + 1] #####TODO: make it so that is only checks for spaces above the line as you can't go under it and also make it actually work instead of putting check at [0] or [-1]
					elif can_place(y, x - amt):
						return [y, x - amt]
				else:
					return 'win'

	#TODO could save on resource by not checking diags that are smaller than "amt"
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
						if board[directions[a] * (x + shift_types[y]) + index_adjs[a]][x] == chip:
							diag_connects[y] += 1
						else:
							diag_connects[y] = 0
					except IndexError:
						pass

				if amt in diag_connects:
					if find_win:
						pass
						#TODO add robot stuff here
					else:
						return 'win'

	return False


def find_move(chip, size = 1):
	if size == CONNECT:
		return False

	place_coords = check_line(chip, CONNECT - size, True)
	if place_coords != False:
		#place_chip isn't checked to make sure it was placed bc it was already checked by the check_line function
		place_chip(place_coords[0], 'B')
		return True
	else:
		return find_move(chip, size + 1)


#recursive function to switch players from turn to turn until someone wins
#TODO change from 1-7 to 1-BOARDSIZE
def turn(curr):
	if curr/2 == int(curr/2):

		#TODO choose random order of defensive and offensive
		if find_move('B') == False:
			if find_move('A') == False:
				while place_chip(random.randint(1, 7), 'B') == 'filled':
					continue

		player_info = ['B','loss']
	else:
		pick = int(input('1-7: ')) - 1
		if place_chip(pick, 'A') == 'filled':
			print('Choose a column that is not filled up')
			return turn(curr)

		player_info = ['A','win']

	display_board()

	if check_line(player_info[0]) == 'win':
		return player_info[1]

	return turn(curr + 1)

# RUNNING THE GAME

#create and show the empty board

board = [[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,'A','A'],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0]]

display_board()

#run the game and print if you won or lost

if turn(1) == 'win':
	print('You Win')
else:
	print('You Lose')