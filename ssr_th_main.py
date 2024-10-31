import threading
import queue,time
import serial,sys
from ssr_sw_th import ssr
import RPi.GPIO as GPIO
import datetime
from time import sleep

#ledpin = 12				# PWM pin connected to LED
#GPIO.setwarnings(False)			#disable warnings
#GPIO.setmode(GPIO.BOARD)		#set pin numbering system
#GPIO.setup(ledpin,GPIO.OUT)
#pi_pwm = GPIO.PWM(ledpin,1000)		#create PWM instance with frequency
#pi_pwm.start(0)				#start PWM of required Duty Cycle 

i=1
q =queue.Queue()  # queue which stores a result of a thread
th = threading.Thread(target=ssr,args=(sys.argv[1],sys.argv[2],sys.argv[3],q),daemon=True)
th.start()
print("start thread: "+str(i))
#th.join()
while True:
  try:
    if threading.active_count()==1:
      data = q.get()
      print("thread returns "+data)
      i=i+1
      if int(data)>=0:
        pi_pwm.ChangeDutyCycle(100)
        print("SSR ON")
      else:
        pi_pwm.ChangeDutyCycle(0)
        print("SSR OFF")
      th = threading.Thread(target=ssr, args=(sys.argv[1],sys.argv[2],sys.argv[3],q),daemon=True)
      th.start()
      print("start thread: "+str(i))
  except KeyboardInterrupt:
    print("Keyboard Interrupt")
    GPIO.cleanup()
    exit()
