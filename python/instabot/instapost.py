#write a script that is set up to be run 3 times a day and will post the most popular, previously unposted, reddit post
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from xml.dom import minidom
import time
from PIL import Image
from io import BytesIO
import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

#modified from somewhere
def make_img_square(img):
    size = max(img.size[0], img.size[1])
    square = Image.new('RGB', (size, size), (0, 0, 0))
    square.paste(img, (int((size - img.size[0]) / 2), int((size - img.size[1]) / 2)))
    return square

def post_to_insta():
	driver.get('https://www.instagram.com/accounts/login/')
	time.sleep(5)
	driver.find_element_by_name('username').send_keys('today_i_learned_reddit')
	driver.find_element_by_name('password').send_keys('MattArm01')

	driver.find_elements_by_css_selector('.sqdOP.L3NKy.y3zKF')[1].click()
	time.sleep(5)
	driver.get('https://www.instagram.com/today_i_learned_reddit')
	print('yizzle')
	time.sleep(5)
	driver.find_element_by_xpath('//div[@role="menuitem"]').click()
	autoit.win_active('Open')
	time.sleep(1)
	autoit.control_send('Open', 'Edit1', 'img.jpg')
	autoit.control_send('Open', 'Edit1', '{ENTER}')
	# ActionChains(driver).move_to_element(driver.find_elements_by_xpath('//input[@accept = "image/jpeg"]')[1]).click().perform()
	# handle = "[CLASS:#32770; TITLE:Open]"
	# autoit.win_wait(handle, 60)
	# autoit.control_set_text(handle, "Edit1", "img.jpg")
	# autoit.control_click(handle, "Button1")
	#driver.find_elements_by_xpath('//input[@accept = "image/jpeg"]')[1].send_keys(os.getcwd() + os.path.sep + 'img.jpg')
	print('yoo')


def post_article(url):
	driver.get(url)
	time.sleep(5)
	driver.execute_script('document.querySelector(".XPromoPopup.m-active").style.display = "none"') #delete mobile popup
	#driver.execute_script('document.querySelector(".PostContent.size-default").style.display = "none"') #delete link and link preview
	driver.execute_script('document.querySelector("body").className = "nightMode"')
	image = driver.find_element_by_css_selector('article.Post.size-default').screenshot_as_png
	im = Image.open(BytesIO(image))  # uses PIL library to open image in memory
	im = make_img_square(im.crop((0, 90, im.size[0], im.size[1])))
	im.save('img.jpg')

	post_to_insta()

	posteds = open('posted.txt', 'a+')
	posteds.write(url.split('/')[6] + ',')
	posteds.close()

#got somewhere
mobile_emulation = {
	"deviceMetrics": { "width": 500, "height": 1000, "pixelRatio": 3.0 },
	"userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" 
}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options = chrome_options)

driver.get('https://www.reddit.com/r/todayilearned/top/.rss')
raw_xml = driver.find_element_by_tag_name('pre').text

parsed_xml = minidom.parseString(raw_xml[:38] + '<root>' + raw_xml[38:] + '</root>')
posts = []
postElements = parsed_xml.getElementsByTagName('entry')
with open('posted.txt') as file:
	used = file.read().split(',')[:-1]
	for postElement in postElements:
		post = postElement.childNodes[4].getAttribute('href')
		print(post.split('/')[6])
		if post.split('/')[6] not in used:
			post_article(post)
			break

driver.quit()

#if list > 200 then take off the first 100