'''
#NOTE deleted stuff that is no longer useful. integrate the rest into the running code below later

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
		break'''

import math

add = lambda x, y : x + y
subtract = lambda x, y : x - y
multiply = lambda x, y : x * y
divide = lambda x, y : x / y
exponent = lambda x, y : x ** y
root = lambda x, y : y ** (1 / x)

#the lambdas in operations have the same index as the symbols in operators you can get .index of symbols and find the lambda at that place
opGroups = [['^','√'],['*','/'],['+','-']]
operations = [[exponent,root],[multiply,divide],[add,subtract]]

sine = lambda x : math.sin(float(x))
cosine = lambda x : math.cos(float(x))
tangent = lambda x : math.tan(float(x))
asine = lambda x : math.asin(float(x))
acosine = lambda x : math.acos(float(x))
atangent = lambda x : math.atan(float(x))

functionSymbs = ['☺','☻','♥','♦','♣','♠']
functionLambdas = [sine,cosine,tangent,asine,acosine,atangent]
operatorList = ['^','√','*','/','+','-']


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
	for y in range(0,len(opGroups)):
		newArr = []
		for x in range(0,len(formatted)):
			print(str(newArr) + ' at ' + str(x - 1))
			if didOperation:
				didOperation = False
				continue

			if formatted[x] in opGroups[y]:
				#get the correct lambda based on the symbol which was used
				currOperation = operations[y][opGroups[y].index(formatted[x])]
				#do the operation on the numbers that it is between and add that to the new, more calculated list of numbers.
				newArr.append(currOperation(float(newArr[-1]),float(formatted[x + 1])))
				newArr.pop(-2)
				didOperation = True
				continue
			newArr.append(formatted[x])
		#print(str(newArr) + ' with ' + y[0] + ' and  ' + y[1])
		formatted = newArr

	print('Number: ' + str(formatted[0]))
	return formatted[0]

#convert the string that is the user's input into a list of the numbers and operations.
def strToList(string):
	formatted = []
	currNum = ''
	wasOperator = False
	for x in string:
		if x in operatorList:
			#if there is no number before an operator there user's input was wrong so raise an error unless it was a root when it should default to 2
			if currNum == '':
				if x == '√':
					currNum = '2'
				else:
					print(formatted)
					raise SyntaxError('An operator did not have two numbers to compare')

			formatted.extend([currNum,x])
			currNum = ''
		else:
			currNum += x

	#add last number onto equation after making sure it is a number
	#TODO: make it so this is not copied from above
	if currNum == '':
		raise SyntaxError('An operator did not have two numbers to compare')

	formatted.append(currNum)

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

				#if the parentheses are right next to a number assume that means multiplication (ex: 2(2) = 2 * (2))
				opSpace1 = ''
				opSpace2 = ''
				if (exp[parenStart - 1] not in operatorList and parenStart - 1 >= 0) and exp[parenStart - 1] not in functionSymbs:
					opSpace1 = '*'
				elif exp[parenStart - 1] in functionSymbs:
					#TODO: fix repeated code eek
					if exp[parenStart - 2] not in operatorList and parenStart - 2 >= 0:
						opSpace1 = '*'
					parenValue = functionLambdas[functionSymbs.index(exp[parenStart - 1])](parenValue)
					parenStart -= 1		
				#make sure that there is something after the parentheses before checking to see if that thing is an operator
				if len(exp) >= x + 2:
					if exp[x+1] not in operatorList:
						opSpace2 = '*'

				#make the new expression which is the same thing with the part in parens evaluated
				newExp = exp[:parenStart] + opSpace1 + str(float(parenValue)) + opSpace2 + exp[x + 1:]
				break

	if nestLevel != 0:
		raise SyntaxError('Bad number of parentheses.')

	return newExp

#print(parse('1+(2+4)+5'))