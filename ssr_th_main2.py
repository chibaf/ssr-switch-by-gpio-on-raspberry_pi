import threading
import queue,time
import serial,sys
from ssr_sw_th import ssr
import RPi.GPIO as GPIO
import datetime
from time import sleep
import os

#j1=1
pin_id1=str(8)
path1='./go'+pin_id1+'.txt'
#j2=1
pin_id2=str(18)
path2='./go'+pin_id2+'.txt'
q1 =queue.Queue()  # queue which stores a result of a thread
q2 =queue.Queue()  # queue which stores a result of a thread
th1 = threading.Thread(target=ssr,args=(8,1,1,q1),name="th1",daemon=True)
th2 = threading.Thread(target=ssr,args=(18,1,1,q2),name="th2",daemon=True)
th1.start()
#th1.join()
th2.start()
#th2.join()
print(th1.name)
print(th2.name)
#print("1: thread started")

while True:
  try:
    if threading.active_count()==3:
      continue
    elif threading.active_count()==1:
     is_file1=os.path.isfile(path1)
     if is_file1:
       #j1=j1+1
       #print("th1:",str(j1))
       th1 = threading.Thread(target=ssr,args=(8,1,1,q1),name="th1",daemon=True)
       th1.start()
#       th1.join()
       print(th1.name)
     is_file2=os.path.isfile(path2)
     if is_file2:
       #j2=j2+1
       #print("th2:",str(j2))
       th2 = threading.Thread(target=ssr,args=(18,1,1,q2),name="th2",daemon=True)
       th2.start()
#       th2.join()
       print(th2.name)
  except KeyboardInterrupt:
    print("Keyboard Interrupt")
    GPIO.cleanup()
    exit()
