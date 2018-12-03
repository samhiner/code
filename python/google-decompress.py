#https://techdevguide.withgoogle.com/paths/advanced/compress-decompression/#!

#Expand string where the num before the bracket says how many times string inside brackets is to be repeated.
#Also "Digits are only to represent amount of repetitions"
def expand(string):
	data = ''
	size = ''
	final = ''
	depth = 0
	collect = False
	for x in string:
		if x == '[':
			depth += 1

			if collect == False:
				collect = True
				continue				
			
		elif x == ']':
			depth -= 1

		if depth == 0 and collect:
			data = expand(data)
			data *= int(size)
			final += data
			data = ''
			size = ''
			collect = False
			continue

		if collect:
			data += x
		else:
			if x.isnumeric():
				size += x
			else:
				final += x

	return final

print(expand('2[3[a]b]'))