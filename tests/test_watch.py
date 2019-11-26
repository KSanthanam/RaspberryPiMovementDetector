from MovementDetector.Watch import Watch

class TestWatch():
    def test_trig(self):
        watch = Watch(23,24)
        assert watch.trigger_pin() == 23
        
    def test_echo(self):
        watch = Watch(23,24)
        assert watch.echo_pin() == 24
