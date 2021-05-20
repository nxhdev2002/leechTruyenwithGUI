import os, sys
import datetime
from res.ggmodule.gglib import Create_Service
from googleapiclient.http import MediaFileUpload

now = datetime.datetime.now()

def login():
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app 
        # path into variable _MEIPASS'.
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    CLIENT_SECRET_FILE = application_path + '/res/ggmodule/cre.json'
    API_SERVICE_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/userinfo.profile']

    service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

    return (service)

class google_sheets():

    def __init__(self, service):
        super().__init__()
        self.service = service

    def create_log_file(self):
        payload = {
            'properties': {
                'title': 'Logging ' + now.strftime("%H:%M - %D")
            }
        }
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
    def create_folder(self, name, parent='1Eq8TUvui_krkTFo3sbwOIg-GdWPSweyy'):
        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [parent]
        }
        file = self.service.files().create(supportsTeamDrives=True,body=file_metadata,
                                    fields='id').execute()
        return file.get('id')
    
    def upload_to_folder(self, img, folder_id):
        file_metadata = {
            'name': img,
            'parents': [folder_id]
        }
        media = MediaFileUpload(img,
                                mimetype='image/jpeg',
                                resumable=True)
        file = self.service.files().create(supportsTeamDrives=True, body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        return file.get('id')

class identity():
    def __init__(self, service):
        super().__init__()
        self.service = service
    def getName(self):
        userinfo = self.service.userinfo().get().execute()
        return userinfo['given_name']