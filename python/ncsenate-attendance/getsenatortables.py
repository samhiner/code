from bs4 import BeautifulSoup
import requests
import csv

def get_vote_csv(senator_id, year):
	#find html table
	url = 'https://www.ncleg.gov/Legislation/Votes/MemberVoteHistory/' + str(year) + '/S/' + str(senator_id)
	html = requests.get(url).content
	soup = BeautifulSoup(html, features='html5lib')
	table = soup.select_one('table#vote-report')

	#if page actually doesn't exist, redirect to page that is always there or throw error
	if table == None && year != 2019:
		return get_vote_csv(2019)
	else if table == None && year == 2019:
		raise ValueError('Senator ID out of bounds.')

	#
	headers = [th.text.encode('utf-8') for th in table.select('tr th')]

	with open('data/' + senator_id + '.csv', 'w') as file:
		writer = csv.writer(file)
		writer.writerow(headers)
		writer.writerows([[td.text.encode('utf-8') for td in row.find_all('td')] for row in table.select('tr + tr')])

def download_voting_records(senator_list):
	for senator in senator_list:
		#get ID of senator to be used to find vote records
		senator_id = senator[15:18]
		if senator_id[-1] == '"':
			senator_id = senator_id[:-1]

		get_vote_csv(senator_id, 2017)


with open('data/senatorlist.txt') as file:
	senator_list = file.split('\n')

download_voting_records(senator_list)