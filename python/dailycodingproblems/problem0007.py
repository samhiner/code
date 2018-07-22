# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not allowed.

def decodeWays(msg, numPaths = 0):
	if len(msg) == 0:
		numPaths += 1
		return numPaths

	if len(msg) >= 1:
		if 26 >= int(msg[0]) >= 1:
			numPaths = decodeWays(msg[1:],numPaths)

	if len(msg) > 1:
		if 26 >= int(msg[:2]) >= 1:
			numPaths = decodeWays(msg[2:],numPaths)

	return numPaths

#ISSUE: wrong for cases that shouldn't work like 602