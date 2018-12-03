def syracuse(n):
	total = 0
	while n != 1:
		total += 1

		if n & 1:
			n = int(n * 3 + 1)
		else:
			n = int(n / 2)

	return total

for x in range(1,1000001):
	print((x, syracuse(x)))