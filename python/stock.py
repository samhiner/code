import urllib
import json
import random
import matplotlib.pyplot as plt

KEY = '1JUJBPIR1KXVLPXM'
sp500 = ['MSFT']
NUM_SIMS = 100000

changes = []

for stock in sp500:
	history = json.load(urllib.urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&apikey=%s' % (stock, KEY)))
	for x in history['Time Series (Daily)']:
		curr_stock = history['Time Series (Daily)'][x]
		changes.append(float(curr_stock['4. close']) / float(curr_stock['1. open']))

plt.hist(changes)
plt.show()

deviation = sum(changes) / len(changes) - 1
changes = [x - deviation for x in changes]

total = 0

for x in range(NUM_SIMS):
	price = 1

	while 0.95 < price < 1.05:
		price *= random.choice(changes)

	if price > 1.05:
		total += 1

print(total)