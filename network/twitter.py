import twitter

from settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)


def get_twitter_urls_data(slug, owner_screen_name):
    twitter_data = api.GetListTimeline(slug=slug, owner_screen_name=owner_screen_name, count=200)
    twitter_urls_data = []
    for data in twitter_data:
        for url in data.urls:
            if 'twitter.com' not in url.expanded_url:
                twitter_urls_data.append({'url': url.expanded_url, 'date': ''})
    #twitter_urls_data = [{'url': url.expanded_url, 'date': ''} for data in twitter_data for url in data.urls if 'twitter.com' not in url.expanded_url]
    return twitter_urls_data
