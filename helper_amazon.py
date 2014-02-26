# -*- coding; utf-8 -*-
from bottlenose import api
from bs4 import BeautifulSoup

    
ACCESS_KEY ='****'
SECRET_KEY = '****'
ASSOCIATE_TAG = '****-22'
REGION = 'JP'

amazon = api.Amazon(ACCESS_KEY,SECRET_KEY,ASSOCIATE_TAG, Region=REGION)

def item_search(keywords, search_index='All', item_page=1):
    response = amazon.ItemSearch(SearchIndex = search_index, Keywords=keywords,ItemPage=item_page, ResponseGroup="Medium")
    soup = BeautifulSoup(response)
    
    return soup.findAll('item')



if __name__ == '__main__':
    for item in item_search('Django'):
        title = item.find('title').text
        url = item.find('detailpageurl').text
        image_url = item.find('mediumimage').contents[0].text
        print("%s (%s) - %s" % (title, url, image_url))

