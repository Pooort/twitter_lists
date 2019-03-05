from tqdm import tqdm

from network.internet import get_response
from network.twitter import get_twitter_urls
from repo.url_data import save_to_csv
from usecase.manager import get_url_data, get_lists_data

twitter_lists = get_lists_data()
url_data_list = []

for twitter_list in twitter_lists:
    twitter_urls = get_twitter_urls(
        slug=twitter_list['slug'],
        owner_screen_name=twitter_list['owner_screen_name']
    )
    bar = tqdm(total=len(twitter_urls))
    for url in twitter_urls:
        bar.update()
        try:
            response = get_response(url)
            url_data = get_url_data(response)
        except:
            pass
        else:
            url_data_list.append(url_data)
    bar.close()

save_to_csv(url_data_list)
