from network.twitter import get_twitter_urls
import requests
from bs4 import BeautifulSoup

twitter_urls = get_twitter_urls(slug='media-data', owner_screen_name='ranjanxroy')
for url in twitter_urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

print('!')

#'Account Takeover
'''
https://twitter.com/ranjanxroy/lists/media-data
'''