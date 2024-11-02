import threading
import queue,time
import serial,sys
from ssr_sw_th import ssr
import RPi.GPIO as GPIO
import datetime
from time import sleep

i=1
q1 =queue.Queue()  # queue which stores a result of a thread
q2 =queue.Queue()  # queue which stores a result of a thread
th1 = threading.Thread(target=ssr,args=(8,3,3,q1),name="t1",daemon=True)
th2 = threading.Thread(target=ssr,args=(18,2,2,q2),name="t2",daemon=True)
th1.start()
th2.start()
#print("start thread: "+str(i))
#th.join()
while True:
  try:
    if threading.active_count()==1:
#      data = q.get()
#      print("thread returns "+data)
      i=i+1
      th1 = threading.Thread(target=ssr,args=(8,3,3,q1),name="t1",daemon=True)
      th2 = threading.Thread(target=ssr,args=(18,2,2,q2),name="t2",daemon=True)
      th1.start()
      th2.start()
#      print("start thread: "+str(i))
  except KeyboardInterrupt:
    print("Keyboard Interrupt")
    GPIO.cleanup()
    exit()
