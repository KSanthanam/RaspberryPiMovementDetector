# -*- coding: utf-8 -*-

# python imports
import os
import sys
import time
import fake_rpi


# adjust the path to import RaspberryPiMovementDetector
base = os.path.normpath(os.path.join(os.path.abspath(__file__), "../.."))
sys.path.insert(0, base)

# Make it work on non RaspberryPi device
sys.modules['RPi'] = fake_rpi.RPi
try:
    from RPi.GPIO import GPIO
except:
    import RPi as RPi
    GPIO = RPi.GPIO

# create an Watch instance
from MovementDetector import Watch

TRIG = 23
ECHO = 24

def func_moved_in(arg):
  print("process for object entering field")

def func_moved_out(arg):
  print("process for object exiting field")

OFFSET = 200 # 2m

watch = Watch(gpio=GPIO, trig=TRIG, echo=ECHO, func_in=func_moved_in, func_out=func_moved_out, offset=OFFSET)

watch.observe()

time.sleep(100) # Sleep 

watch.stop()

