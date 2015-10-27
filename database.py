import sqlite3 as lite

con = lite.connect('tcdata.db')
con.text_factory = str
cur = con.cursor()

def store_in_db(title, published_datetime,author_name, article_url, comment_count):
	sql = "INSERT INTO articles (title, published_datetime,author_name, article_url, comment_count) VALUES (?,?,?,?,?)"
	with con:
	    cur.execute(sql, (title, published_datetime,author_name, article_url, comment_count));

def create_db_tables():
	with con:
		cur.execute('DROP TABLE IF EXISTS articles')
		cur.execute('CREATE TABLE articles (id INTEGER PRIMARY KEY,\
											title TEXT,\
											published_datetime INTEGER,\
											author_name TEXT,\
											article_url TEXT,\
											comment_count INTEGER)');	