import os
import datetime
from gglib import Create_Service

now = datetime.datetime.now()

CLIENT_SECRET_FILE = 'cre.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


payload = {
    'properties': {
        'title': 'Logging ' + now.strftime("%H:%M - %D")
    }
}


service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

def create_log_file():
    sheets_file1 = service.spreadsheets().create(body=payload).execute()
    # dict_keys(['spreadsheetId', 'properties', 'sheets', 'spreadsheetUrl'])
    # print(sheets_file1)
    print(sheets_file1['spreadsheetUrl'])
    print(sheets_file1['spreadsheetId'])
    values = [["ThờI gian"],["Chap Link"],["Trạng Thái"]]
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



create_log_file()
insert("12",'Hoang DZ', 'A2', '1FBmwpxR2RexwzDxEU3DehuEhsfnlzGQ01fP1YlRxIGc')