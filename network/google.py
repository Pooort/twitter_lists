import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from settings import PROJECTPATH, CREDENTIALSFILENAME


def get_all_values():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    credentials_file_path = os.path.join(PROJECTPATH, CREDENTIALSFILENAME)

    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file_path, scope)

    gc = gspread.authorize(credentials)

    wks = gc.open("Twitter List Extraction").sheet1
    return wks.get_all_values()
