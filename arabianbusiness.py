import requests
from bs4 import BeautifulSoup

from repo.url_data import save_to_csv

domain = 'arabianbusiness.com'
response = requests.get('https://www.{}/'.format(domain))
soup = BeautifulSoup(response.text, 'html.parser')
article_elements = soup.select('.g-tit a')
url_data = []
for el in article_elements:
    data = {
        'url': 'https://www.{}{}'.format(domain, el.attrs['href']),
        'domain': domain,
        'title': el.attrs['title']
    }
    url_data.append(data)

save_to_csv(url_data, 'arabianbusiness.csv')