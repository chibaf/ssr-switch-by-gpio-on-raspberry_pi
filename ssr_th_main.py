import threading
import queue,time
import serial,sys
from ssr_sw_th import ssr
import RPi.GPIO as GPIO
import datetime
from time import sleep
import os

#ledpin = 12				# PWM pin connected to LED
#GPIO.setwarnings(False)			#disable warnings
#GPIO.setmode(GPIO.BOARD)		#set pin numbering system
#GPIO.setup(ledpin,GPIO.OUT)
#pi_pwm = GPIO.PWM(ledpin,1000)		#create PWM instance with frequency
#pi_pwm.start(0)				#start PWM of required Duty Cycle 

pin_id=str(sys.argv[1])
print("pin_id:"+pin_id)
path = './go'+pin_id+'.txt'
print(path)
#exit()
i=1
q =queue.Queue()  # queue which stores a result of a thread
th = threading.Thread(target=ssr,args=(sys.argv[1],sys.argv[2],sys.argv[3],q),daemon=True)
th.start()
print("start thread: "+str(i))
#th.join()
while True:
    is_file = os.path.isfile(path)
    print(threading.active_count())
    if threading.active_count()==1:
      print(is_file)
      if is_file:
        i=i+1
        print('i=',i)
        th = threading.Thread(target=ssr, args=(sys.argv[1],sys.argv[2],sys.argv[3],q),daemon=True)
        th.start()
        print("start thread: "+str(i))
      else:
        print("nop")
        continue
    else:
      print(threading.active_count())
      print(is_file)
      print("nop2")
      continue
#    print("Keyboard Interrupt")
#    GPIO.cleanup()
#    exit()
