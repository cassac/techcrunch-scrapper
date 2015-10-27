from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_comment_counts(url):
	"""
	Retrieve the comment counts for all articles located on the page.
	Selenium was used because comments are loaded dynamically after static
	page is rendered. 
	"""
	driver = webdriver.Firefox()
	driver.get(url)
	wait = WebDriverWait(driver, 30)
	wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fb_comments_count')))
	
	try:
		retrieved_counts = driver.find_elements(By.CLASS_NAME, 'fb_comments_count')
	except:
		print '===NO COUNTS RETRIEVED==='
		pass

	counts_list = []
	
	for count in retrieved_counts:
		try:
			counts_list.append(count.text)
		except:
			# -1 will be used for unretrievable counts
			counts_list.append(-1)
	driver.quit()
	return counts_list 

# Test individual page:
# print get_comment_counts('http://techcrunch.com/2015/10/08/')
	