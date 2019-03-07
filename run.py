from tqdm import tqdm

from network.internet import get_response
from network.twitter import get_twitter_urls_data
from repo.update_data import read_update_data, save_update_data
from repo.url_data import save_to_csv
from usecase.manager import get_url_data, get_lists_data

update_data = read_update_data()

twitter_lists = get_lists_data()

for twitter_list in twitter_lists:
    slug = twitter_list['slug']
    owner_screen_name = twitter_list['owner_screen_name']
    twitter_urls_data = get_twitter_urls_data(
        slug=slug,
        owner_screen_name=owner_screen_name
    )
    bar = tqdm(total=len(twitter_urls_data))
    for url_data in twitter_urls_data:
        bar.update()
        created_at = url_data['created_at']
        last_update = update_data.get((slug, owner_screen_name))
        if last_update and created_at <= last_update:
            continue
        try:
            response = get_response(url_data['url'])
            url_data = get_url_data(response)
        except:
            pass
        else:
            save_to_csv([url_data])
            if not last_update or created_at > last_update:
                update_data[(slug, owner_screen_name)] = created_at
                save_update_data(update_data)
    bar.close()
