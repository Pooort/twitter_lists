import requests
import datetime
from bs4 import BeautifulSoup

from repo.url_data import save_to_csv

domain = 'zawya.com'
main_url = 'https://www.{}'.format(domain)
url = 'https://www.zawya.com/mena/en/the-vault/topnews/filter?language=EN&country=&pillar=&pillarHolder=business%2Ceconomy%2Cmarkets%2Clegal%2Clife&subPillar=&provider=&date=&dateFrom=&dateTo=&pageNumber=1&perPage=50'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
url_data = []

for div_element in soup.find_all('div', class_='featured_story-left'):
    title = div_element.find('a').text
    url = main_url + div_element.find('a').attrs['href']
    date_text = div_element.find('p', class_='featured_story-date-text').text
    created_at = datetime.datetime.strptime(date_text, '%A %d %B %Y')
    data = {
        'url': url,
        'domain': domain,
        'title': title,
        'created_at': created_at
    }
    url_data.append(data)

for div_element in soup.select('div.featured_stories-top > div > div > div'):
    a_element = div_element.select('h3.content-title-text > a')[0]
    title = a_element.text
    url = main_url + a_element.attrs['href']
    date_text = div_element.find('p', class_='featured_story-date-text').text
    created_at = datetime.datetime.strptime(date_text, '%A %d %B %Y')
    data = {
        'url': url,
        'domain': domain,
        'title': title,
        'created_at': created_at
    }
    url_data.append(data)

save_to_csv(url_data, 'zawya.csv')
