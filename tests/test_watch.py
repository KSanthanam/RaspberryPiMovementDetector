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

def object_in_func(arg):
    print("object_in_func called with", arg)

def object_out_func(arg):
    print("object_out_func called with", arg)

@pytest.mark.parametrize('trig, echo, func_in, func_out', [(23, 24, object_in_func, object_out_func), (3, 4, object_in_func, object_out_func)])     
class TestWatch():
    def test_trig(self, trig, echo, func_in, func_out):
        watch = Watch(GPIO, trig, echo, func_in, func_out)
        assert watch.trigger_pin() == trig
        
    def test_echo(self, trig, echo, func_in, func_out):
        watch = Watch(GPIO, trig, echo, func_in, func_out)
        assert watch.echo_pin() == echo

    def test_distance(self, trig, echo, func_in, func_out):
        watch = Watch(GPIO, trig, echo, func_in, func_out)
        assert type(watch.get_distance()) is float

    def test_observe(self, trig, echo, func_in, func_out):
        watch = Watch(GPIO, trig, echo, func_in, func_out)
        watch.observe()
