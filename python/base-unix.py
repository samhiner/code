import time

digit = chr(int(time.time() / 86400))

print('The base-86400 representation of the current UNIX time is %s' % digit)

print('''
The person-number assignment is as follows where the door is at the top right:

 1 | 2 
-------
 3 | 4
''')

if int(time.time() / 86400) % 3 == 0:
	print("Today it is person 1's turn.")
elif int(time.time() / 86400) % 2 == 0:
	print("Today it is person 2's turn.")
else:
	print("Today it is person 3's turn.")