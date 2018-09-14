print("Oops Python already has native support for it with sets this is obsolete haha. Ending development. This can do basic, two variable expressions with union + intersection at current state.")
print('https://stackoverflow.com/questions/7692324/why-is-not-understood-by-python-sets')

#boolean variable setting
sets = {
#	'a': [1, 2, 3, 4, 5],
#	'b': [4, 5, 6, 7, 8]
}

while True:
	if input('Add a set? Y/N ') not in ['N', 'n']:
		new_set = input('Set: ').split(':')
		sets[new_set[0]] = new_set[1].split(',')
	else:
		break

#expression getting + formatting
def get_exp():
	exp = input('Enter Boolean expression. ')
	#exp = 'a ^ b'
	form_exp = []
	for x in exp:
		if x in sets or x in operators:
			form_exp.append(x)
	return form_exp

#solve the formatted expression
def solve_exp(exp):
	#TODO make it default to a variable so if i just say "a" it returns "[1,2,3]" if that is what a is
	solved = []
	for x in range(0,len(exp)):
		#TODO add more here so it can do more than one operation at a time
		if exp[x] == 'v':
			solved.extend(sets[exp[x - 1]])
			solved.extend(sets[exp[x + 1]])
		elif exp[x] == '^':
			for y in sets[exp[x - 1]]:
				if y in sets[exp[x + 1]]:
					solved.append(y)
	return set(solved)


#where the expression parsing functions are called
operators = ['^', 'v']

while True:
	exp = get_exp()
	print(solve_exp(exp))
	if input('Again? Y/N ') in ['N', 'n']:
		break