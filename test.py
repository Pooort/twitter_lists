import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('Test-bd04a274485a.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("Twitter List Extraction").sheet1
wks.get_all_values()
print('!')
