#!/usr/bin/env python3

from datetime import datetime
import time
import epics
import json
import requests
import gpwd

'''gpwd.py file has a two function:
def: myauth():
     return ('usrid', 'passwd')
def: myurl():
     return "https://etc.etc"
'''

url = gpwd.myurl()
myobj = {'cryo': 'newvalues',
         'temp1': epics.caget('CTC:Temp1'),
         'temp2': epics.caget('CTC:Temp2'),
         'temp3': epics.caget('CTC:Temp3'),
         'temp4': epics.caget('CTC:Temp4'),
         'pirani': epics.caget('pirani:PRESSURE'),
         'CC1': epics.caget('CC1:PRESSURE'),
         'turbo_rot': epics.caget('Turbo:rotspeed'),
         'turbo_current': epics.caget('Turbo:current'),
         'turbo_hours': epics.caget('Turbo:hours'),
         'cryo_water_in': epics.caget('cryo:waterIn'),
         'cryo_water_out': epics.caget('cryo:waterOut'),
         'cryo_oil': epics.caget('cryo:oil'),
         'cryo_helium': epics.caget('cryo:helium'),
         'cryo_lowpress_avg': epics.caget('cryo:lowPressureAvg'),
         'cryo_highpress_avg': epics.caget('cryo:highPressureAvg'),
         'cryo_hours': epics.caget('cryo:hours')
         }

#print(myobj)
x = requests.post(url, data = myobj, auth = gpwd.myauth())

#print (x)

#print(date_time)
