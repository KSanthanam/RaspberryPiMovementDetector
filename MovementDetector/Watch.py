class Watch:
  def __init__(self, trig, echo):
    self._trig = trig
    self._echo = echo
  
  def trigger_pin(self):
    return self._trig

  def echo_pin(self):
    return self._echo