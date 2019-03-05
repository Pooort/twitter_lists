from bs4 import BeautifulSoup
from urllib.parse import urlparse


def get_url_data(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    url = response.url
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return {'url': url, 'domain': domain, 'title': title}
