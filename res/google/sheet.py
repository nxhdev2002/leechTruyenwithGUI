import os
import datetime
from gglib import Create_Service

now = datetime.datetime.now()

CLIENT_SECRET_FILE = r'D:\\pycoder\\GUI\\leechTruyen\\res\\google\\cre.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']


payload = {
    'properties': {
        'title': 'Logging ' + now.strftime("%H:%M - %D")
    }
}


service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)
# service1 = Create_Service(CLIENT_SECRET_FILE, 'drive', 'v3', SCOPES)

def create_log_file():
    sheets_file1 = service.spreadsheets().create(body=payload).execute()
    values = [["Thời gian"],["Chap Link"],["Trạng Thái"]]
    value_range_body = {
        'majorDimension': 'COLUMNS',
        'values': values
    }

    service.spreadsheets().values().update(
        spreadsheetId=sheets_file1['spreadsheetId'],
        valueInputOption='USER_ENTERED',
        range='A1',
        body=value_range_body
    ).execute()
    return sheets_file1

def insert(chaplink, data, cell_range_insert, spreadsheet_id):
    values = [[now.strftime("%H:%M")],[chaplink],[data]]
    value_range_body = {
        'majorDimension': 'COLUMNS',
        'values': values
    }

    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        valueInputOption='USER_ENTERED',
        range=cell_range_insert,
        body=value_range_body
    ).execute()


# print(service1)
logfile = create_log_file()
insert("12",'Hoang DZ', 'A2', logfile['spreadsheetId'])
# results = service.files().list(
#         pageSize=10, fields="nextPageToken, files(id, name)").execute()
# items = results.get('files', [])

# if not items:
#     print('No files found.')
# else:
#     print('Files:')
#     for item in items:
#         print(u'{0} ({1})'.format(item['name'], item['id']))

# os.system("pause")