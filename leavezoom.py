import os
from datetime import datetime
from threading import Timer
import time

inputtime = input("enter time to leave, please do military time, example: 12:40 \n")
try:
    hourtime = inputtime[:2]
    minutetime = inputtime[3:]
    print("hour: " + hourtime + " minute: " + minutetime)
    
    print(hourtime + " " + minutetime)
except:
    print("invalid time, restart the script")

x = datetime.today()
y = x.replace(day=x.day, hour=int(hourtime), minute=int(minutetime), second=0, microsecond=0)
delta_t=y-x

secs=delta_t.total_seconds()

def leave_zoom():
    time.sleep(int(secs))
    close = os.popen('pidof zoom')
    output = close.read()
    outputlist = output.split(' ')
    print(outputlist)
    for i in outputlist:
        os.popen(f'kill -9 {i}')
        print('killed process id: ' + i)

leave_zoom()

