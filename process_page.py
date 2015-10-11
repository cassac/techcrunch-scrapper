# import bs4

# Below URL has 3 pages of articles
# 'http://techcrunch.com/2015/10/06/'
# page = open('page3.txt', 'r')

def process_page(soup):
	# soup = bs4.BeautifulSoup(page, 'html.parser')
	articles = soup.find_all('li', {'class': 'river-block'})

	for article in articles:
		title = article.div.h2.text.encode('UTF-8')
		published = article.div.time.attrs['datetime']
		author = article.div.find('a', {'rel': 'author'}).text.encode('UTF-8')
		article_url = article.div.h2.a['href']
		print 'STORE: ', title, author, published
	#comment_count = commnt_counts()

	has_next = soup.find('li', {'class': 'next'})
	if has_next:
		return has_next.a['href']
	return False
	# 	process_page(has_next.a['href'])

# process_page(page)