# import requests

# url = "https://appvector.io/aso-tool/api/v1/reviews/?appId=com.whatsapp&page=1"
  
# payload = ""
# headers = {
#   'Authorization': 'Token fec12362ce406036c57fc0fed7afac3ad99b75a3'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.json())

import requests
import google.auth
from googleapiclient.discovery import build
from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


# The Google Sheets API client
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)


# The ID of the Google Sheet you want to use
SAMPLE_SPREADSHEET_ID = '1toIOJu4EQr1XWzOw2-3hwRi_2ZpQPzaOakKw9Z2T8f0'  

# The headers and API key for the AppVector API
headers = {'Authorization': 'Token 7ee503e86d8d29e71d841b81cbce926b2094baa7'}

# The parameters for the API requests
params = {'country': 'in', 'language': 'en', 'sort': 'recent', 'pageSize': 10}

# The app IDs for the apps you want to get reviews for
app_ids = ['com.facebook.lite']

# A function to append data to the Google Sheet
def append_data(sheet_id, range_name, data):
    body = {'values': data}
    result = service.spreadsheets().values().append(
        spreadsheetId=sheet_id, range=range_name,
        valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS',
        body=body).execute()
    print(f"{result['updates']['updatedRows']} rows appended to {range_name}")

# Looping through the app IDs and get their reviews
for app_id in app_ids:
    print(f"Getting reviews for app ID {app_id}...")
    page = 1
    while True:
        # Making the API request
        url = f"https://appvector.io/aso-tool/api/v1/reviews/?appId={app_id}&page={page}"
        response = requests.get(url, headers=headers, params=params)
        # print(response.json())
        if response.status_code != 200:
            print(f"Failed to get reviews for app ID {app_id}. Error: {response.text}")
            break
        reviews = response.json()
        # print(reviews)
        print(type(reviews))
        print(reviews.keys())

        if len(reviews) == 0:
            print(f"Finished getting reviews for app ID {app_id}")
            break

        # To prepare the data for the Google Sheet
        for review in reviews['results']:
            data = [app_id, review['user_name'], review['text']]

        # To append the data to the Google Sheet
            append_data(SAMPLE_SPREADSHEET_ID, 'Sheet3!A:C', [data])
            page += 1

