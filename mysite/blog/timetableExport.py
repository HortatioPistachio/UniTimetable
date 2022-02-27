
from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account

import json

# If modifying these scopes, delete the file token.json.

def verifyData(ttData):
    try:
        dictTable = json.loads(ttData)
        return True
    except:
        return False



def dictToCalApi(uniClass, colour):
    #this function takes a row(class) from the timetable json data and converts it into pretty data for the calendar
    summary = uniClass['course'] + ' (' + uniClass['type']+')'
    location = uniClass['room'] + ' (' + uniClass['building'] +')'
    startTime = uniClass['date'] +'T' + uniClass['start_time'] +':00'
    endTime = uniClass['date'] +'T'+ uniClass['end_time'] +':00'

    formattedUniClass = {
        'summary':summary,
        'location':location,
        'start':{
            'dateTime':startTime,
            'timeZone': 'Australia/Adelaide'
            },
        'end':{
            'dateTime':endTime,
            'timeZone': 'Australia/Adelaide'
            },
        'reminders': {
            'useDefault':'false',
        },

        'colorId':colour,
    }

    return formattedUniClass
        


def createCal(email, ttData, colour):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
   
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    SERVICE_ACCOUNT_FILE =  os.path.join(os.path.dirname(os.path.dirname(__file__)),'blog/static/unitimetable-312108-a8e9ffa78078.json')

    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes = SCOPES)

    service = build('calendar', 'v3', credentials=creds)

    
    dictTable = json.loads(ttData)


    #creating a new calendar for the timtbale to go into
    year = datetime.date.today().year
    calAdd = {
        'summary':str(year)+' Uni Timetable'
    }

    create_cal_list_entry = service.calendars().insert(body=calAdd).execute()
    calID = create_cal_list_entry['id']

    #create new batch
    batch = service.new_batch_http_request()
    
    #go through each class and add it to the timetable
    for uniClass in dictTable:
        calClass = dictToCalApi(uniClass, colour)
        event = batch.add(service.events().insert(calendarId=calID,body=calClass))
        
    batch.execute()
        

    #sharing the calendar with my friends
    rule = {
        'scope': {
            'type':'user',
            'value':email
        },
        'role': 'writer'
    }
    create_rule = service.acl().insert(calendarId=calID,body=rule).execute()