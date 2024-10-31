class ssr_sw:

  def __init__(self,ssr_pin):
    self.ssr_pin = ssr_pin;  #このクラスが持つ「num」変数に引数を格納
    import RPi.GPIO as GPIO
    self.pin_id=str(ssr_pin)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ssr_pin,GPIO.OUT)
    
  def run(self,ton,tstop)
    path = './go'+self.pin_id+'.txt'
    while True:
      try:
	    is_file = os.path.isfile(path)
	    if is_file:
	      print("find go"+gself.pin_id+".txt\n")
	    else:
	      print("stop this proram")
#	    f=open("ssr_"+gid+"_log.txt",'a',encoding="utf-8")
#	    t_delta = datetime.timedelta(hours=9)
#	    JST = datetime.timezone(t_delta, 'JST')
#	    now = datetime.datetime.now(JST)
#	    d = now.strftime('%Y %m %d %H:%M:%S')
#	    s1=d+": ssr_"+gid+" "+str(ont)+" "+str(offt)+" stops\n"
#	    f.write(s1)
#	    f.close()
	      GPIO.output(ssr_pin, 0)
	      exit()
	    GPIO.output(ssr_pin, 1)
	    print("SSR "+self.pin_id+" ON ("+str(ont)+"sec)\n")
	    time.sleep(ton)
	    if tstop != 0.0:
	      GPIO.output(ssr_pin, 0)
	      print("SSR "+self.pin_id+" OFF ("+str(offt)+"sec)\n")
	      time.sleep(tstop)
      except KeyboardInterrupt:
        print("stop this proram")
#        f=open("ssr"+gid+"_log.txt",'a',encoding="utf-8")
#        t_delta = datetime.timedelta(hours=9)
#        JST = datetime.timezone(t_delta, 'JST')
#        now = datetime.datetime.now(JST)
#        d = now.strftime('%Y %m %d %H:%M:%S')
#        s1=d+": ssr_"+gid+" "+str(ont)+" "+str(offt)+" stops\n"
#        f.write(s1)
#        f.close()
        GPIO.output(ssr_pin, False)
        exit()
        