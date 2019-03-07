import csv
import os

from settings import CSVDELIMITER, PROJECTPATH


def save_to_csv(url_data_list, file_path='data.csv'):
    csv_path = os.path.join(PROJECTPATH, file_path)

    if not url_data_list:
        return

    if not os.path.isfile(csv_path):
        try:
            with open(csv_path, 'w', newline='') as csvfile:
                fieldnames = url_data_list[0].keys()
                writer = csv.DictWriter(csvfile,
                                        fieldnames=fieldnames,
                                        delimiter=CSVDELIMITER,
                                        extrasaction='ignore')
                writer.writeheader()
        except:
            os.remove(csv_path)

    with open(csv_path, 'a', newline='') as csvfile:
        fieldnames = url_data_list[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=CSVDELIMITER, extrasaction='ignore')
        for url_data in url_data_list:
            writer.writerow(url_data)
