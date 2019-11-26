import pytest
from MovementDetector.Watch import Watch

class TestWatch():
    @pytest.mark.parametrize('trig, echo', [(23,24)])
    def test_trig(self, trig, echo):
        watch = Watch(trig,echo)
        assert watch.trigger_pin() == trig
        
    @pytest.mark.parametrize('trig, echo', [(23,24)])
    def test_echo(self, trig, echo):
        watch = Watch(trig,echo)
        assert watch.echo_pin() == echo
