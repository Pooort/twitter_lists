import requests
from bs4 import BeautifulSoup

from repo.url_data import save_to_csv

domain = 'thenational.ae'
main_url = 'https://www.{}/business'.format(domain)
url = main_url
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
main_div = soup.select('div.col-lg-9.col-md-12.col-sm-12.col-xs-12.clearfix.no-padding')[0]
div_elements = main_div.select('div.article-teaser')
div_elements.extend(main_div.select('div.taxonomy-3'))

url_data = []

for div_element in div_elements:
    url = main_url + div_element.find_all('a')[1].attrs['href']
    title = div_element.find('p').text
    data = {
        'url': url,
        'domain': domain,
        'title': title
    }
    url_data.append(data)

save_to_csv(url_data, 'thenational.csv')
