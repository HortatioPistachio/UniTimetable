from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

import json

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def dictToCalApi(uniClass):
    #this function takes a row(class) from the timetable json data and converts it into pretty data for the calendar
    summary = uniClass['course'] + ' (' + uniClass['type']+')'
    location = uniClass['room'] + ' (' + uniClass['building'] +')'
    startTime = uniClass['date'] +'T' + uniClass['start_time']+':00+09:30'
    endTime = uniClass['date'] +'T'+ uniClass['end_time']+':00+09:30'

    formattedUniClass = {
        'summary':summary,
        'location':location,
        'start':{
            'dateTime':startTime,
            },
        'end':{
            'dateTime':endTime,
            },
        'reminders': {
            'useDefault':'false',
        },

        'colorId':'7',
    }

    return formattedUniClass
    


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    rawTable = open('timetable.json','r')
    dictTable = json.load(rawTable)
    
    #go through each class and add it to the timetable
    for uniClass in dictTable:
        calClass = dictToCalApi(uniClass)
        event = service.events().insert(calendarId='primary',body=calClass).execute()
        

if __name__ == '__main__':
    main()