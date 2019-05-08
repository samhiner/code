import urllib.request
from bs4 import BeautifulSoup as bs
import re

def get_country_codes():
	countries = {}
	with open('countrynamedata.txt') as f:
		for line in f:
			countries[line[64:-1].lower()] = line[33:35]
	return countries

def first_items(para):
	commas = 0
	in_paren = 0
	for x in range(len(para)):
		if para[x] == '(':
			in_paren += 1
		if para[x] == ')':
			in_paren -= 1

		if in_paren <= 0 and ord(para[x]) == 44:
			commas += 1
			if commas == 2:
				break

	return re.sub('^\s+|\s+$', '', para[:x])

country_codes = []

with open('questions.txt') as f:
	countries = get_country_codes()
	x = 0
	for line in f:
		if x % 7 == 0:
			country_codes.append(countries[line[:-2].lower()])
		x += 1

with open('questions.txt') as f:
	data = f.readlines()

for a in range(len(country_codes)):
	mysite = urllib.request.urlopen('https://www.cia.gov/library/publications/the-world-factbook/geos/%s.html' % country_codes[a])
	soup = bs(mysite)

	#languages
	data[a * 7 + 1] = data[a * 7 + 1][:-1] + first_items(soup.find(id='field-languages').find(class_='category_data subfield text').find(text=True)) + '\n'

	#religion
	data[a * 7 + 2] = data[a * 7 + 2][:-1] + first_items(soup.find(id='field-religions').find(class_='category_data subfield text').find(text=True)) + '\n'

	#issue
	issues = soup.find(id='field-disputes-international').find(class_='category_data subfield text').find('p').find(text=True)
	for x in range(len(issues)):
		if issues[x] == ';':
			break
	issues = ' ' + issues[0].upper() + issues[1:x] + '.'
	data[a * 7 + 4] = data[a * 7 + 4][:-1] + issues + '\n'
	
	#region
	data[a * 7 + 5] = data[a * 7 + 5][:-1] + ' ' + soup.find('title').find(text=True).split('::')[0] + '\n'

	print(country_codes[a].upper() + ' processed!')

print(''.join(data))
with open('questions.txt', 'w') as f:
	f.write(''.join(data))