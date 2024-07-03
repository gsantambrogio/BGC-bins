#!/usr/bin/env python3
import epics
from datetime import datetime
import time

now=datetime.now()
date_time_file=now.strftime("%Y%m%d-%H%M%S")+".dat"
#print(date_time)

file = open(date_time_file, "w")
file.write("Time\t Incal\t In2\t In3\t In4\t Pirani\t ColdCathode\n")
file.close()

def dataline():
    now = datetime.now()
    now_time = now.strftime("%Y%m%d-%H:%M:%S")
    t1=epics.caget('CTC:Temp1')
    t2=epics.caget('CTC:Temp2')
    t3=epics.caget('CTC:Temp3')
    t4=epics.caget('CTC:Temp4')
    p1=epics.caget('pirani:PRESSURE')
    p2=epics.caget('CC1:PRESSURE')
    file = open(date_time_file, "a")
    strline = now_time + "\t" + str(t1)+"\t"+str(t2)+"\t"+str(t3)+"\t"+str(t4)+"\t"+str(p1)+"\t"+str(p2)+"\n"
    file.write(strline)
    file.close()
#    print(t1,t2,t3)

while True:
    dataline()
    time.sleep(60)
