from __future__ import print_function
import datetime
import os.path
import time
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/calendar']

SERVICE_ACCOUNT_FILE =  os.path.join(os.path.dirname(os.path.dirname(__file__)),'unitimetable-312108-a8e9ffa78078.json')

creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes = SCOPES)
service = build('calendar', 'v3', credentials=creds)



count =0
page_token = None
calIds = []

while(1):
    calendar_list = service.calendarList().list(pageToken= page_token).execute()
    

    for calendar_list_entry in calendar_list['items']:
        calIds.append(calendar_list_entry['id'])
    
    try:
        page_token = calendar_list['nextPageToken']
    except:
        print("complete")
        break
#print(calendar_list)

latest = calIds[-3]
print(latest)


page_token = None
while True:
    events = service.events().list(calendarId=latest, pageToken=page_token).execute()
    for event in events['items']:
        #print (event['id'])
        pass
    page_token = events.get('nextPageToken')
    if not page_token:
        break


eventList = service.events().get(calendarId=latest, eventId=events['items'][1]['id']).execute()

for event in events['items']:
    eventList = service.events().get(calendarId=latest, eventId=event['id']).execute()
    #print(event)
    #print(event['start']['dateTime'])
    firstS = event['start']['dateTime'][0:11]
    endS = event['start']['dateTime'][13:len(event['start']['dateTime'])]
    midS = str(int(event['start']['dateTime'][11:13])-1) 

    if(len(midS) == 1):
        midS = '0' + midS
    if(midS == "-1"):
        firstDate = event['start']['dateTime'][0:8]
        endDate = str(int(event['start']['dateTime'][8:10])-1)
        if(endDate == 0):
            endDate = "13"
        firstS = firstDate+endDate +"T"
        midS = "23"

    event['start']['dateTime'] = firstS + midS + endS


    firstE = event['end']['dateTime'][0:11]
    endE = event['end']['dateTime'][13:len(event['end']['dateTime'])]
    midE = str(int(event['end']['dateTime'][11:13])-1) 

    if(len(midE) == 1):
        midE = '0' + midE
    if(midE == "-1"):
        firstDate = event['end']['dateTime'][0:8]
        endDate = str(int(event['end']['dateTime'][8:10])-1)
        if(endDate == 0):
            endDate = "13"
        firstE = firstDate+endDate + "T"
        midE = "23"

    event['end']['dateTime'] = firstE + midE + endE
    print(event['start']['dateTime'])
    print(event['end']['dateTime'])
    print("------------------")

    updated_event = service.events().update(calendarId = latest, eventId=event['id'], body=event).execute()


print("complete")
