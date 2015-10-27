from datetime import datetime, date, timedelta
from helper_functions import get_page_data, process_page

def start_scrapper(the_date, end_date):

	print '===== scrapper started @', datetime.now()

	while the_date <= end_date:
		# Convert to proper formatting used in url
		date = the_date.strftime('%Y/%m/%d')
		# Increate the_date by 1 day to traverse down caldenar dates
		the_date += timedelta(days=1)

		def process_url(url_ext):

			soup, comment_counts_list = get_page_data(url_ext)
			# soup may be None due to url 404 error
			# if is None then exit function
			if soup == None:
				return
			
			# Process page - return False if no more pages in pagination
			# return new url and repeat if if more pages available
			has_more_pages = process_page(soup, comment_counts_list)
			
			if has_more_pages:
				process_url(has_more_pages)

		process_url(date)

	print '===== scrapper stopped @', datetime.now()

# Enter date range here
start_date = date(2005, 9, 1) # scrapper will begin at this date
end_date = date(2005, 10, 1) # scrapper will end at this date

start_scrapper(start_date, end_date)			

