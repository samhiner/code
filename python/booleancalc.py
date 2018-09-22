'''#solve the formatted expression
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
	return set(solved)'''

###########

import math

def unify(arr1, arr2):
	for x in arr2:
		if x not in arr1:
			arr1.append(x)
	return arr1

def intersect(arr1, arr2):
	final = []
	for x in arr1:
		if x in arr2:
			final.append(x)
	return final

#the lambdas in operations have the same index as the symbols in operators you can get .index of symbols and find the lambda at that place
opList = ['^','v']
operations = [intersect, unify]

def parse(userInput):
	#evaluate everything in parentheses before the rest of the expression
	#also converts evaluated bits back to a string so it matches the type of the expression
	while '(' in userInput and ')' in userInput:
		userInput = order(userInput)

	if '(' in userInput or ')' in userInput:
		raise SyntaxError('Bad number of parentheses.')

	#convert the string expression into a list
	formatted = strToList(userInput)

	print('List: ' + str(formatted))

	#for each operator group, iterate through the list and evaluate all parts which are in the scope of that group
	#gives the new list to next operator, this way the ones that come first can be exponents causing order of operations
	didOperation = False
	for y in range(0,len(opList)):
		newArr = []
		for x in range(0,len(formatted)):
			print(str(newArr) + ' at ' + str(x - 1))
			if didOperation:
				didOperation = False
				continue

			if formatted[x] in opList:
				#get the correct lambda based on the symbol which was used
				currOperation = operations[opList.index(formatted[x])]
				#do the operation on the numbers that it is between and add that to the new, more calculated list of numbers.
				newArr.append(currOperation(newArr[-1], formatted[x + 1]))
				newArr.pop(-2)
				didOperation = True
				continue
			newArr.append(formatted[x])
		formatted = newArr

	print('Number: ' + str(formatted[0]))
	return formatted[0]

#convert the string that is the user's input into a list of the numbers and operations.
def strToList(string):
	formatted = []
	currNum = ''
	wasOperator = False
	for x in string:
		if x in opList:
			#if there is no number before an operator there user's input was wrong so raise an error
			if currNum == '':
				print(formatted)
				raise SyntaxError('An operator did not have two numbers to compare')

			formatted.extend([list(sets[currNum]),x])
			currNum = ''
		else:
			currNum += x

	#add last number onto equation after making sure it is a number
	#TODO: make it so this is not copied from above
	if currNum == '':
		raise SyntaxError('An operator did not have two numbers to compare')

	formatted.append(list(sets[currNum]))

	return formatted

#evaluate anything inside of parentheses in the equation
def order(exp):
	nestLevel = 0
	for x in range(0,len(exp)):
		if exp[x] == '(':
			if nestLevel == 0:
				parenStart = x
			nestLevel += 1
		if exp[x] == ')':
			nestLevel -= 1
			if nestLevel == 0:
				parenValue = parse(exp[parenStart + 1:x])
				#make the new expression which is the same thing with the part in parens evaluated
				newExp = exp[:parenStart] + str(float(parenValue)) + exp[x + 1:]
				break

	if nestLevel != 0:
		raise SyntaxError('Bad number of parentheses.')

	return newExp

#boolean variable setting
sets = {
	'a': (1, 2, 3, 4, 5),
	'b': (4, 5, 6, 7, 8)
}

while True:
	if input('Add a set? Y/N ') not in ['N', 'n']:
		new_set = input('Set: ').split(':')
		sets[new_set[0]] = new_set[1].split(',')
	else:
		break

while True:
	print(parse(input('Expression: ')))
	if input('Again? Y/N ') in ['N', 'n']:
		break

#TODO create a set of every unit so you can do inverses