from selenium import webdriver

FIRST_NAME = 'first'
LAST_NAME = 'last'
EMAIL = 'email'

#made its own function to show this could be turned into a more advanced calculator easily
#the best solution is to just make an ML-resistant image
def solve(prob):
	return eval(prob[:-1])

def fill_field(field_name, credential):
	field = driver.find_element_by_name(field_name)
	field.send_keys(credential)

driver = webdriver.Chrome('C:/Users/smhnr/Desktop/Resources/chromedriver.exe')
driver.get('https://petitions.whitehouse.gov/user/login')

prob = driver.find_element_by_class_name('field-prefix').text

solution = solve(prob)

fill_field('profile_main[field_first_name][und][0][value]', FIRST_NAME)
fill_field('profile_main[field_last_name][und][0][value]', LAST_NAME)
fill_field('mail', EMAIL)
fill_field('captcha_response', solution)

driver.find_element_by_id('edit-submit--2').click()