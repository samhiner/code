ordered_counties = [18, 44, 45, 30, 39, 14, 13, 6, 12, 15, 21, 46, 5, 50, 19, 48, 4, 33, 23, 29, 27, 24, 43, 47, 11, 10, 37, 35, 31, 32, 41, 25, 20, 38, 36, 16, 7, 9, 8, 28, 2, 34, 17, 3, 1, 26, 49, 40, 42, 22]
county_lean = {}

with open('raw_data.txt') as file:
	data = file.read().split('\n')
	for county in data:
		county_lean[county.split(' ')[0]] = county.split(' ')[-1]

	for county in ordered_counties:
		print(''.join([x[0] for x in county_lean[str(county)].split('	')]))