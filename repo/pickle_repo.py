import os
import pickle

from settings import PROJECTPATH


def read_data(name):
    update_data_path = os.path.join(PROJECTPATH, '{}.pickle'.format(name))
    if not os.path.isfile(update_data_path):
        return None
    with open(update_data_path, 'rb') as f:
        data = pickle.load(f)
        return data


def save_data(name, data):
    update_data_path = os.path.join(PROJECTPATH, '{}.pickle'.format(name))
    with open(update_data_path, 'wb') as f:
        pickle.dump(data, f)
