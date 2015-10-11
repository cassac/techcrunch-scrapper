from datetime import date, timedelta
from helper_functions import get_page_data, process_page

def start_crawler(the_date, end_date):
	print '===== Crawler started ====='

	while the_date <= end_date:
		# Convert to proper formatting used in url
		date = the_date.strftime('%Y/%m/%d')
		# Increate the_date by 1 day to traverse down caldenar dates
		the_date += timedelta(days=1)

		def process_url(url_ext):
			print '=== process_url running with url_ext: ', url_ext
			# Return 'soup' and store in 'page_data' used with below function
			soup = get_page_data(url_ext)
			# Process page - return False if no more pages in pagination
			# return new url and repeat if if more pages available
			has_more_pages = process_page(soup) #, comment_counts_list)
			if has_more_pages:
				print '=== has_more_pages at: ', has_more_pages
				process_url(has_more_pages)

		process_url(date)

	print '===== Crawler stopped ====='


start_date = date(2015, 10, 6) # crawler will begin at this date
end_date = date(2015, 10, 7) # crawler will end at this date

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
