from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def comment_counts(url):
	"""
	Retrieve the comment counts for all articles located on the page.
	Selenium was used because comments are loaded dynamically after static
	page is rendered. 
	"""
	driver = webdriver.Firefox()
	driver.get(url)
	wait = WebDriverWait(driver, 10)
	wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fb_comments_count')))
	
	retrieved_counts = driver.find_elements(By.CLASS_NAME, "fb_comments_count")
	
	counts_list = []
	
	for count in retrieved_counts:
		try:
			counts_list.append(int(count.text))
			# print count.text
		except:
			counts_list.append(None)
			# print 'Count not retrived'
	driver.quit()
	return counts_list 

# print comment_count('http://techcrunch.com/2015/10/08/')
	