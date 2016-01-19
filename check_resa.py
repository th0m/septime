#!/usr/bin/env python
import json
import requests

r = requests.get('https://module.lafourchette.com/fr_FR/resa/pick-date/10889-d34ca/54499')
c = json.loads(r.text)
availableDateList = c['availableDateList']
for availableDate in availableDateList:
    r = requests.get('https://module.lafourchette.com/fr_FR/resa/pick-time/{}/10889-d34ca/54499'.format(availableDate['date']))
    c = json.loads(r.text)
    availableTimeslotList = c['availableTimeslotList']
    for availableTimeslot in availableTimeslotList:
        if availableTimeslot['name'] == 'DINER' and availableTimeslot['timeslots']:
            print(availableDate['date'])
            for timeslot in availableTimeslot['timeslots']:
                print(timeslot['time'])
