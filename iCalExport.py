from icalendar import Calendar, Event
from datetime import datetime
import tempfile, os
import json

dictTable = {}
with open('timetable.json') as json_file:
    dictTable = json.load(json_file)



cal = Calendar()
# @TODO fix this to be the uni year, not what ever year the user is in
year = 1999#datetime.date.today().year
cal.add('prodid', '-//testCal//')
cal.add('version', '2.0')
cal.add('name', str(year)+' Uni Timetable')
cal.add('X-WR-CALNAME', str(year)+' Uni Timetable')

for uniClass in dictTable:
    summary = uniClass['course'] + ' (' + uniClass['type']+')'
    location = uniClass['room'] + ' (' + uniClass['building'] +')'

    stringStart = uniClass['date'] +'T' + uniClass['start_time'] +':00'
    startTime = datetime.strptime(stringStart, "%Y-%m-%dT%H:%M:%S")
    #startTime = datetime(uniClass['date'] +'T' + uniClass['start_time'] +':00')

    stringEnd = uniClass['date'] +'T'+ uniClass['end_time'] +':00'
    endTime = datetime.strptime(stringEnd, "%Y-%m-%dT%H:%M:%S")
    #endTime = datetime(uniClass['date'] +'T'+ uniClass['end_time'] +':00')

    event = Event()
    event.add('summary', summary)
    event.add('dtstart', startTime)
    event.add('dtend', endTime)
    event.add('tzname','ACST')
    event.add('location', location)

    cal.add_component(event)


#print(cal.to_ical())

f = open('myCal.ics', 'wb')
f.write(cal.to_ical())
f.close()