import math

#To get this:
	#I saw a table of who won for n 1-15 and realized that the length of 
	#an x + 2 cycle doubles each time starting with 1. ex: 1, 13, 1357, etc
	#Because of this, it is only 1 when log(n, 2) is a whole number. It steps
	#up by 2 each time after that so the difference between the num and its
	#nearest 2^a * 2 + 1 (plus 1 because it is already 1 so it is a constant
	#that you are stepping up from by 2)
def josephus(n):
	print((n - (2 ** math.floor(math.log(n, 2)))) * 2 + 1)

#Intuition:
	#With an even number of people, you kill half and start back at the beginning
	#The only numbers which are always even no matter how many times you halve 
	#them are 2^a numbers. This is until you reach 2 which halves to 1. That
	#doesn't matter for this problem though bc n = 1 means that the winner is 1.

	#With that established, if you let the simulation run on any number until you
	#are down to 2^a, the person who's turn it currently is will win. You go down
	#by two for each extra person because the person who was killed is skipped
	#(stole this part of the intuition from the internet)

	#You don't have to worry about killing a full half before getting to 2^n (where
	#the + 2 pattern would get messed up because in the algo wouldn't loop back
	#to 1 like real life) because if there is a 2^a at or below half of n, then
	#doubling that should get a 2^a that is above half of n and at or below n