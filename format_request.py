import requests
base_url = 'http://techcrunch.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5)'}

def make_request(url_ext):
	url = base_url + url_ext
	r = requests.get(url, headers=headers)
	return r