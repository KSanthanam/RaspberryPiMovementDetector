import pytest

try:
    import RPi.GPIO as GPIO
    import smbus
    SIMULATION = False
except:
    from rpi_hardware.mocked import GPIO
    from rpi_hardware.mocked import smbus
    SIMULATION = True


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
