import csv

def print_voting_records(senator_list):
	for senator in senator_list:
		senator_id = senator[15:18]
		if senator_id[-1] == '"':
			senator_id = senator_id[:-1]

		with open('data/' + senator_id + '.csv') as file:
			reader = csv.reader(file)
			next(reader) #skip header row
			didnt_vote = 0
			did_vote = 0
			for row in reader:
				if row != []:
					if row[6] in ["b'Excused Absence'", "b'N/V'", "b'Excused Vote'"]:
						didnt_vote += 1
					else:
						did_vote += 1

			if did_vote + didnt_vote != 0:
				print(did_vote / (did_vote + didnt_vote))
			else:
				print(0)

with open('data/senatorlist.txt') as file:
	senator_list = file.read().split('\n')

print_voting_records(senator_list)