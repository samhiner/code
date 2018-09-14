import math

# BOARD SETUP

board = [
	[[], [1], [1], [1], [1], []],
	[[], 0, 0, 0, 0, 0],
	[[4], 0, 0, 0, 0, 0], #, 0 for testing 6- make sure you update top row when you do this
	[[], 0, 0, 0, 0, 0],
	[[], 0, 0, 0, 0, 0],
	[[], 0, 0, 0, 0, 0]
]

'''
#put a pixel or an x on the board
	#c_type: 1 for pixel, -1 for x
	#x, y: coordinates of change
def change(c_type, x, y):
	board[x][y] = c_type

	#update counts
	if c_type == 1:
		groups = [0]
		for space in range(1, len(board[x])):
			if board[space] = 1
				groups[-1] += 1
			else:
				groups.append(0)
		for x in groups:
			if x not 0:
				final_groups.append(x)
		if final_groups == board[x][0]:
			pass
			#this is where we would know that a row is done but idk if this function is necessary.
			#I will leave this comented out in case I end up needing it later
'''

# SOLVING ALGOS

#black out spaces that must contain a pixel due to a long group
def must_reach():
	for row in board:
		for group in range(0,len(row[0])):
			#if the group will take up over half of the row
			if row[0][group] > width/2:
				empty_area = width - row[0][group]
				#fill in all of the spaces that must be taken up no matter where the group is in the row
				for space in range(empty_area + 1, width - empty_area + 1):
					row[space] = 1

# RUN SOLVER

width = len(board[0]) - 1
height = len(board) - 1

iterator = 0
#TODO change iterator to a check if puzzle is done
while iterator == 0:
	must_reach()
	iterator = 1

print(board)