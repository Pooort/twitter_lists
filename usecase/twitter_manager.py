from helpers import Singleton
from network.internet import get_response
from network.twitter import get_twitter_urls_data
from repo.pickle_repo import read_data, save_data
from usecase.manager import get_lists_data, get_url_data


class TwitterManager(metaclass=Singleton):

    twitter_lists = get_lists_data()
    processed = None
    repo_name = 'twitter'

    def __init__(self):
        self.processed = read_data(self.repo_name)

    @property
    def processed(self):
        return read_data(self.repo_name)

    @processed.setter
    def processed(self, value):
        save_data(self.repo_name, value)

    def get_article(self):
        for twitter_list in self.twitter_lists:
            slug = twitter_list['slug']
            owner_screen_name = twitter_list['owner_screen_name']
            twitter_urls_data = get_twitter_urls_data(
                slug=slug,
                owner_screen_name=owner_screen_name
            )
            self.processed[(slug, owner_screen_name)] = self.processed.get((slug, owner_screen_name), set()) & set(twitter_urls_data)
            for url_data in twitter_urls_data:
                if url_data in self.processed.get((slug, owner_screen_name), set()):
                    continue
                try:
                    response = get_response(url_data['url'])
                    url_data = get_url_data(response)
                except:
                    pass
                else:
                    yield url_data
                    processed = yield

    def set_article_processed(self, url_data):
        self.processed.get((slug, owner_screen_name), set())

TwitterManager()