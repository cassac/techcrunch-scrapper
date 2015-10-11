import requests, bs4
# from comment_counts import get_comment_counts

base_url = 'http://techcrunch.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5)'}

def get_page_data(url_ext):
	url = base_url + url_ext
	response = requests.get(url, headers=headers)
	soup = bs4.BeautifulSoup(response.content, 'html.parser')
	# comment_counts_list = get_comment_counts(url)
	return soup #, comment_counts_list


def process_page(soup): #, comment_counts_list):

	articles = soup.find_all('li', {'class': 'river-block'})

	for i in range(len(articles)):
		title = articles[i].div.h2.text.encode('UTF-8')
		published = articles[i].div.time.attrs['datetime']
		author = articles[i].div.find('a', {'rel': 'author'}).text.encode('UTF-8')
		article_url = articles[i].div.h2.a['href']
		print 'ARTICLE: ', published, author, title[:25]
	#comment_count = commnt_counts()

	has_next = soup.find('li', {'class': 'next'})
	if has_next:
		return has_next.a['href']
	return False	