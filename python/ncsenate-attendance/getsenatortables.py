from bs4 import BeautifulSoup
import requests
import csv

#turn online records into csv
def download_voting_record(senator_id, year):
	#find html table
	url = 'https://www.ncleg.gov/Legislation/Votes/MemberVoteHistory/' + str(year) + '/S/' + str(senator_id)
	html = requests.get(url).content
	soup = BeautifulSoup(html, features='html5lib')
	table = soup.select_one('table#vote-report')

	#if page actually doesn't exist, redirect to page that is always there or throw error
	if table == None and year != 2019:
		return download_voting_record(senator_id, 2019)
	elif table == None and year == 2019:
		raise ValueError('Senator ID out of bounds.')

	#write table to csv file
	with open('data/' + senator_id + '.csv', 'w') as file:
		writer = csv.writer(file)
		headers = [th.text.encode('utf-8') for th in table.select('tr th')]
		writer.writerow(headers)
		writer.writerows([[td.text.encode('utf-8') for td in row.find_all('td')] for row in table.select('tr + tr')])

	print('Senator ' + senator_id + ' successfully downloaded for year ' + str(year) + '!')


def get_senator_records(senator_list):
	for senator in senator_list:
		#get ID of senator to be used to find vote records
		senator_id = senator[15:18]
		if senator_id[-1] == '"':
			senator_id = senator_id[:-1]

		download_voting_record(senator_id, 2017)


with open('data/senatorlist.txt') as file:
	senator_list = file.read().split('\n')

get_senator_records(senator_list)