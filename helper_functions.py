import requests, bs4
from comment_counts import get_comment_counts
from database import store_in_db

base_url = 'http://techcrunch.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5)'}

def get_page_data(url_ext):

	url = base_url + url_ext
	response = requests.get(url, headers=headers)

	if response.status_code != 200:
		soup = None
		comment_counts_list = None
	else:
		soup = bs4.BeautifulSoup(response.content, 'html.parser')
		comment_counts_list = get_comment_counts(url)

	return soup, comment_counts_list


def process_page(soup, comment_counts_list):

	articles = soup.find_all('li', {'class': 'river-block'})

	# if len(articles) != len(comment_counts_list):
	# 	print 'ERROR: # OF ARTICLES DOESNT MATCH # COMMENT COUNTS'
	# 	return

	for i in range(len(articles)):
		title = articles[i].div.h2.text.encode('UTF-8')
		published_datetime = articles[i].div.time.attrs['datetime'].encode('UTF-8')
		# Some articles don't have an author
		try:
			author_name = articles[i].div.find('a', {'rel': 'author'}).text.encode('UTF-8')
		except:
			author_name = None
		article_url = articles[i].div.h2.a['href'].encode('UTF-8')
		comment_count = comment_counts_list[i].encode('UTF-8')

		store_in_db(title, published_datetime, author_name, article_url, comment_count)

	has_next = soup.find('li', {'class': 'next'})

	if has_next:
		return has_next.a['href']
	return False	