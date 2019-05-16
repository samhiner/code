states = {}

with open('hr.txt') as f:
	text = f.readlines()
	for line in range(len(text)):
		if text[line][:11] == 'U.S. House ':
			try:
				states[text[line].split(' ')[2].lower()].append(text[line - 2][:-1])
			except KeyError:
				states[text[line].split(' ')[2].lower()] = [text[line - 2][:-1]]

print('var house =', states)

states = {}

with open('senators.txt') as f:
	for line in f:
		sen = line.split('\t')
		try:
			states[sen[1].lower()].append(sen[0].split(' ')[1] + ' ' + sen[0].split(' ')[0][:-1])
		except KeyError:
			states[sen[1].lower()] = [sen[0].split(' ')[1] + ' ' + sen[0].split(' ')[0][:-1]]
		

print('var senate =', states)