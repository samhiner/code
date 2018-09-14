import math

###

board = [
	[[], [1], [1], [1], [1], []],
	[[], 0, 0, 0, 0, 0],
	[[4], 0, 0, 0, 0, 0], #, 0 for testing 6- make sure you update top row when you do this
	[[], 0, 0, 0, 0, 0],
	[[], 0, 0, 0, 0, 0],
	[[], 0, 0, 0, 0, 0]
]

#TODO make row/column numbers decrease when pixels are placed.
#actually above change will require a whole set up to.
#wait is that in usual picross? investigating now

###

width = len(board[0]) - 1
height = len(board) - 1

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

#where algos to figure out what is a pixel are run

iterator = 0
#TODO change iterator to a check if puzzle is done
while iterator == 0:
	must_reach()
	iterator = 1

print(board)