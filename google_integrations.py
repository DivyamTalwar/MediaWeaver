import os
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'credentials.json'
SHEET_ID = os.getenv("SHEET_ID")

def get_google_creds():
    return service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def log_to_sheet(values):
    creds = get_google_creds()
    service = build('sheets', 'v4', credentials=creds)
    
    body = {'values': [values]}
    
    result = service.spreadsheets().values().append(
        spreadsheetId=SHEET_ID,
        range='A1',
        valueInputOption='RAW',
        body=body).execute()
    
    return result

if __name__ == '__main__':
    pass
