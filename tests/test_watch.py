import pytest
import sys
import fake_rpi

sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi (GPIO)
# sys.modules['smbus'] = fake_rpi.smbus # Fake smbus (I2C)

# try:
#     import RPi.GPIO as GPIO
#     SIMULATION = False
# except:
#     from rpi_hardware.mocked import GPIO
#     SIMULATION = True

from RPi.GPIO import GPIO

from MovementDetector.Watch import Watch

class TestWatch():
    @pytest.mark.parametrize('trig, echo', [(23,24)])
    def test_trig(self, trig, echo):
        watch = Watch(GPIO, trig, echo)
        assert watch.trigger_pin() == trig
        
    @pytest.mark.parametrize('trig, echo', [(23,24)])
    def test_echo(self, trig, echo):
        watch = Watch(GPIO, trig, echo)
        assert watch.echo_pin() == echo
