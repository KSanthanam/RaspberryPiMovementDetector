import pytest
import sys
import fake_rpi

sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi (GPIO)

try:
    from RPi.GPIO import GPIO
except:
    import RPi as RPi
    GPIO = RPi.GPIO

from MovementDetector.Watch import Watch

@pytest.mark.parametrize('trig, echo', [(23,24)])
class TestWatch():
    def test_trig(self, trig, echo):
        watch = Watch(GPIO, trig, echo)
        assert watch.trigger_pin() == trig
        
    def test_echo(self, trig, echo):
        watch = Watch(GPIO, trig, echo)
        assert watch.echo_pin() == echo

    def test_distance(self, trig, echo):
        watch = Watch(GPIO, trig, echo)
        assert type(watch.get_distance()) is float
         