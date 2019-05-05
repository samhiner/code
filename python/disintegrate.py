#example function that is expensive to calculate to show the point of disintegrate function
def prime_factorize(letter):
	x = ord(letter) - 96

	factors = []
	divisor = 2
	while True:
		if x == 1:
			break

		while x % divisor == 0:
			x /= divisor
			factors.append(divisor)

		divisor += 1

	return len(factors) == 3 and (factors[0] in factors[1:] or factors[2] in factors[:2])

class Disintegrate:
	done = False
	def disintegrate(func, *args):
		if Disintegrate.done:
			return False
		else:
			Disintegrate.done = func(*args)
			return Disintegrate.done

	def reset():
		done = False

#we know that there is one character in this string that has three prime factors, two of which are the same number
#this character needs to become a z


from timeit import default_timer as timer
#TODO redo this with imported file so that the time that it takes to set up the Disintegrate function is counted
#TODO make Disintegrate function-specific if you want
startTime = timer()

string = 'dshfjkhjkfdshscituocxuiodssdabnmewqew'
for x in range(len(string)):
	if prime_factorize(string[x]):
		string[x] == 'z'
	else:
		num = ord(string[x]) + 1
		if num == 123:
			num = 97
		string = string[:x] + chr(num) + string[x+1:]
vanilla_time = timer() - startTime
print('Vanilla function took %f seconds.' % vanilla_time)


startTime = timer()
string = 'dshfjkhjkfdshscituocxuiodssdabnmewqew'
for x in range(len(string)):
	if Disintegrate.disintegrate(prime_factorize, string[x]):
		string[x] == 'z'
	else:
		num = ord(string[x]) + 1
		if num == 123:
			num = 97
		string = string[:x] + chr(num) + string[x+1:]
dis_time = timer() - startTime
print('Disintegrated function took %f seconds.' % dis_time)

print('The disintegrated function is %fx as fast as the vanilla function' % (vanilla_time/dis_time))