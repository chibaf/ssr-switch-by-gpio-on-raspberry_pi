import numpy as np
import serial,time

def ssr(pin,ton,tstop,q):
  from ssr_sw_class import ssr_sw
  ssr=ssr_sw(int(pin))
  ssr.run(ton,tstop)
  data="stop"
  q.put(data)
  return