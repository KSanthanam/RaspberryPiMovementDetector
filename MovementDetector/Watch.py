import RPi.GPIO as GPIO
import time
class Watch:
  def __init__(self, trig, echo):
    self._trig = trig
    self._echo = echo
  
  def trigger_pin(self):
    return self._trig

  def echo_pin(self):
    return self._echo

  def get_distance(self):
    print("Distance Measurement In Progress")
    GPIO.setup(self._trig, GPIO.OUT)
    GPIO.setup(self._echo, GPIO.IN)
    GPIO.output(self._trig, False)
    print("Waiting For Sensor To Settle")
    time.sleep(2)

    GPIO.output(self._trig, True)
    time.sleep(0.00001)
    GPIO.output(self._trig, False)

    while GPIO.input(self._echo)==0:
      pulse_start = time.time()

    while GPIO.input(self._echo)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)

    print("Distance:",distance,"cm")

    GPIO.cleanup()
    
