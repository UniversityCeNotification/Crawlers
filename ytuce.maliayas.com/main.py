import requests
from bs4 import BeautifulSoup
import re
import hashlib
from pymongo import MongoClient
from dotenv import DotEnv
dotenv = DotEnv('../.env')

if __name__ == '__main__':
    print('[+] Python Crawler Started: ytuce.maliayas.com')
    client = MongoClient(dotenv.get('MongoDbUrl', 'mongodb://localhost:27017'))
    db = client[dotenv.get('MongoDbName', 'universityce')] # which database
    crawlers = db.crawlers  # which collection

    """ Crawling Operations """
    url = 'https://ytuce.maliayas.com/'
    r  = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    for item in soup.find_all('div', 'item'):
        author = item.find('div', 'text_author').find('a')
        title = item.find('div', 'text_title').find('a')
        content = item.find('div', 'text_content').get_text()
        id = hashlib.md5(content.encode('utf-8')).hexdigest()
        time = re.search('(\d{2}\.\d{2}\.\d{4}) (\d{2}:\d{2})', item.find('span', 'date')['title'])
        data = {
            'site': 'ytuce.maliayas.com',
            'authorName': author.get_text(),
            'authorLink': author['href'],
            'titleName': title.get_text(),
            'titleLink': title['href'],
            'content': content,
            'id': id,
            'date': time.group(1),
            'clock': time.group(2),
            'status': 'new'
        }
        """ MongoDb insert Operation """
        result = crawlers.find_one({'id': id})
        if not result:
            print('New Link')
            crawlers.insert_one(data)
    print('[+] Python Crawler Finished: ytuce.maliayas.com')
