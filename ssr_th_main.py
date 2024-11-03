import threading
import queue,time
import serial,sys
from ssr_sw_th import ssr
import RPi.GPIO as GPIO
import datetime
from time import sleep
import os

pin_id=str(sys.argv[1])
#print("pin_id:"+pin_id)
path = './go'+pin_id+'.txt'
#print(path)
#exit()
i=1
q =queue.Queue()  # queue which stores a result of a thread
th = threading.Thread(target=ssr,args=(sys.argv[1],sys.argv[2],sys.argv[3],q),daemon=True)
th.start()
#print("start thread: "+str(i))
while True:
  try:
    is_file = os.path.isfile(path)
    if threading.active_count()==1:
#      print(is_file)
      if is_file:
        i=i+1
        print('i=',i)
        th = threading.Thread(target=ssr, args=(sys.argv[1],sys.argv[2],sys.argv[3],q),daemon=True)
        th.start()
        print("start thread: "+str(i))
      else:
        continue
    else:
      continue
  except KeyboardInterrupt:
     print("Keyboard Interrupt")
     GPIO.cleanup()
     exit()
