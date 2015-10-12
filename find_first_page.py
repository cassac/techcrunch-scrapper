import requests
from datetime import date, timedelta

base_url = 'http://techcrunch.com/'
start_date = date(2005, 6, 5)
days_since_start = timedelta(days=0)
found_first_page = False

while not found_first_page:
	date = start_date + days_since_start
	url = base_url + date.strftime('%Y/%m/%d')
	r = requests.get(url)
	if r.status_code != 404:
		print 'FOUND FIRST VALID URL:', url
		found_first_page = True
	else:
		print '404:', url
		days_since_start += timedelta(days=1)
