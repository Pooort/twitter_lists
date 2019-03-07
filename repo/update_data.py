import os
import pickle

from settings import PROJECTPATH

update_data_path = os.path.join(PROJECTPATH, 'update_data.pickle')

def read_update_data():
    if not os.path.isfile(update_data_path):
        return {}
    with open(update_data_path, 'rb') as f:
        data = pickle.load(f)
        return data


def save_update_data(data):
    with open(update_data_path, 'wb') as f:
        pickle.dump(data, f)
