import time
# create an EventEmitter instance
from pymitter import EventEmitter
from concurrent.futures import ThreadPoolExecutor


class Watch:
  def __init__(self, gpio, trig, echo, func_in, func_out, offset):
    self._ee = EventEmitter(wildcard=True, new_listener=True, max_listeners=-1)
    self._ee.on("ObjectIn", func_in)
    self._ee.on("ObjectOut", func_out)
    self._gpio = gpio
    self._trig = trig
    self._echo = echo
    self._offset = offset
    self._wasIn = False
    self._observer = ThreadPoolExecutor(max_workers=1)
    self._observer_on = True
    self._future = None

  def trigger_pin(self):
    return self._trig

  def echo_pin(self):
    return self._echo

  def ping(self):
    distance = self.get_distance()
    if distance < self._offset:
      if not self._wasIn:
        self._ee.emit("ObjectIn", distance)
        self._wasIn = True
    else:
      if self._wasIn:
        self._ee.emit("ObjectOut", distance)
        self._wasIn = False
    return

  def poll(self):
    while True:
      if self._observer_on:
        self.ping()
      else:
        return

  def observe(self):
    self._future = self._observer.submit(self.poll)
    return

  def stop(self):
    self._observer_on = False
    time.sleep(3)
    try:
      self._future.shutdown(wait=False)
    except:
      if self._future.running():
        self._observer.shutdown(wait=False)
    return

  def get_distance(self):
    print("Distance Measurement In Progress")
    self._gpio.setup(self._trig, self._gpio.OUT)
    self._gpio.setup(self._echo, self._gpio.IN)
    self._gpio.output(self._trig, False)
    print("Waiting For Sensor To Settle")
    time.sleep(2)

    self._gpio.output(self._trig, True)
    time.sleep(0.00001)
    self._gpio.output(self._trig, False)

    pulse_start = time.time()
    pulse_end = time.time()
    while self._gpio.input(self._echo)==0:
      pulse_start = time.time()

    while self._gpio.input(self._echo)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)

    print("Distance:",distance,"cm")

    self._gpio.cleanup()
    return distance
    
