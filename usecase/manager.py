from bs4 import BeautifulSoup
from urllib.parse import urlparse

from network.google import get_all_values


def get_url_data(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text.strip()
    url = response.url
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return {'url': url, 'domain': domain, 'title': title}


def get_lists_data():
    all_values = get_all_values()
    keys = all_values[0]
    lists_data = []
    for values in all_values[1:]:
        d = {}
        for i, value in enumerate(values):
            d[keys[i]] = value
        lists_data.append(d)
    return lists_data
