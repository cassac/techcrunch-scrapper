import bs4
from datetime import date, timedelta
from process_page import process_page
from format_request import make_request

def start_crawler(the_date, end_date):

	while the_date <= end_date:
		date = the_date.strftime('%Y/%m/%d')
		the_date += timedelta(days=1)

		def run_program(url_ext):
			print '=== run_program running with url_ext: ', url_ext
			request = make_request(url_ext)
			soup = bs4.BeautifulSoup(request.content, 'html.parser')

			# Process page - return False if no more pages in pagination
			# return new url and repeat if if more pages available
			has_more_pages = process_page(soup)
			if has_more_pages:
				print '=== has_more_pages at: ', has_more_pages
				run_program(has_more_pages)

		run_program(date)

	print '===== Crawler stopped ====='


start_date = date(2015, 10, 6) # crawler will begin at this date
end_date = date(2015, 10, 6) # crawler will end at this date

start_crawler(start_date, end_date)			
# 	process_page(soup)

# Test pages
# page = open('page2.txt', 'r')
# soup = bs4.BeautifulSoup(page, 'html.parser')
# has_more_pages = process_page(soup)
# if has_more_pages:
# 	print has_more_pages

	# with open('test.txt', 'w') as f:
	# 	f.write(str(soup))