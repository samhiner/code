#Using to make Theoretical Percent Composition by Mass in Chemistry easier
while True:
	nums = []
	curr_input = raw_input('Insert Number:')
	while curr_input != '':
		nums.append(int(curr_input))
		curr_input = raw_input('Insert Number:')


	for num in nums:
		print(float(num) / float(sum(nums)))