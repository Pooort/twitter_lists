import csv

from settings import CSVDELIMITER


def save_to_csv(url_data_list):
    if not url_data_list:
        return
    with open('data.csv', 'w', newline='') as csvfile:
        fieldnames = url_data_list[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=CSVDELIMITER, extrasaction='ignore')
        writer.writeheader()
        for url_data in url_data_list:
            writer.writerow(url_data)
