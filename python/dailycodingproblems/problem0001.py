# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

def addCheck(nums,trySum):
	addable = False
	for x in range(0,len(nums) - 1):
		for y in range(x + 1,len(nums)):
			if nums[x] + nums[y] == trySum:
				addable = True
				break

		if addable == True:
			break

	return addable