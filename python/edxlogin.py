import requests

'''
this can be used to get content in a logged in acct in edX.

I was going to use this to check if a submitted answer on 
an archived course is right before giving the answer, but
I found a way better way to do that with JS and Google Apps
Script. Here is the link: 

https://github.com/samhiner/edxarchivetool
'''

USERNAME = ''
PASSWORD = ''
URL = 'https://courses.edx.org/courses/course-v1:RiceX+AdvCAL.1x+2015_T3/courseware/9892c1bbc15f4e218db996f90228de8f/77259027daba44009d1bf04f5daf5143/3?activate_block_id=block-v1%3ARiceX%2BAdvCAL.1x%2B2015_T3%2Btype%40vertical%2Bblock%40b411803b898f4e9cba0e1ed8f693a06b'

session = requests.session()
headers = {'Referer': 'https://courses.edx.org', 'User-Agent':  'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

#stot this if statement from https://stackoverflow.com/questions/13567507/passing-csrftoken-with-python-requests
session.get('https://courses.edx.org/login_ajax')  # sets cookie
if 'csrftoken' in session.cookies:
	# Django 1.6 and up
	csrftoken = session.cookies['csrftoken']
else:
	# older versions
	csrftoken = session.cookies['csrf']


credentials = {'email': EMAIL, 'password': PASSWORD, 'csrfmiddlewaretoken': csrftoken}
login = session.post('https://courses.edx.org/login_ajax', data=credentials, headers=headers)
print(login.content)

request = session.get(URL)
print(request.content)