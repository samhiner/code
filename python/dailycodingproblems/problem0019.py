# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

def cheapestRow(houses):
	totalCost = 0
	lastColor = -1
	for x in houses:
		while True:
			smallest = x.index(min(s for s in x))
			if smallest != lastColor:
				break
			x[smallest] = float('inf')
		lastColor = smallest
		totalCost += x[smallest]
	return totalCost

#this is wrong. if the second house is cheaper with x color than the first the first will still have preference to get that color.