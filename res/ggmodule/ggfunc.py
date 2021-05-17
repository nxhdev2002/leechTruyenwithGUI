import os, sys
import datetime
from res.ggmodule.gglib import Create_Service

now = datetime.datetime.now()

def login():
    sys.path.append("D:\pycoder\GUI\leechTruyen\res\google")
    CLIENT_SECRET_FILE = 'res/ggmodule/cre.json'
    API_SERVICE_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']


    payload = {
        'properties': {
            'title': 'Logging ' + now.strftime("%H:%M - %D")
        }
    }


    service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

    return (service)

class google_sheets():
    def __init__(self, service):
        super().__init__()
        self.service = service

    def create_log_file(self):
        sheets_file1 = self.service.spreadsheets().create(body=payload).execute()
        values = [["Thời gian"],["Chap Link"],["Trạng Thái"]]
        value_range_body = {
            'majorDimension': 'COLUMNS',
            'values': values
        }

        self.service.spreadsheets().values().update(
            spreadsheetId=sheets_file1['spreadsheetId'],
            valueInputOption='USER_ENTERED',
            range='A1',
            body=value_range_body
        ).execute()
        return sheets_file1


    def insert(self, chaplink, data, cell_range_insert, spreadsheet_id):
        values = [[now.strftime("%H:%M")],[chaplink],[data]]
        value_range_body = {
            'majorDimension': 'COLUMNS',
            'values': values
        }

        self.service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            valueInputOption='USER_ENTERED',
            range=cell_range_insert,
            body=value_range_body
        ).execute()


class google_drive():
    def __init__(self, service):
        super().__init__()
        self.service = service