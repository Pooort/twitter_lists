import twitter
import datetime
from settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)


def get_twitter_urls_data(slug, owner_screen_name):
    twitter_data = api.GetListTimeline(slug=slug, owner_screen_name=owner_screen_name, count=200)
    twitter_urls_data = []
    for data in twitter_data:
        #TO DO remove crated_at
        created_at = datetime.datetime.strptime(data.created_at, '%a %b %d %H:%M:%S +0000 %Y')
        for url in data.urls:
            if 'twitter.com' not in url.expanded_url:
                twitter_urls_data.append({'url': url.expanded_url, 'created_at': created_at})
    #TO DO remove [::-1]
    return twitter_urls_data[::-1]
