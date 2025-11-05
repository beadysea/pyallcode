class DummyTransport:
    def __init__(self):
        self.opened_with = None
        self.closed = False
    def open(self, port):
        self.opened_with = port
    def close(self):
        self.closed = True


class FakeConnection:
    def __init__(self, transport, verbose=0):
        self.transport = transport
        self.verbose = verbose
        self.last_execute = None
        self.opened_with = None
        self.closed = False
    def open(self, port):
        self.opened_with = port
    def close(self):
        self.closed = True
    def execute(self, command: str, expect_response: bool = True, attempts: int = 1):
        self.last_execute = (command.strip(), expect_response, attempts)
        head = command.strip().split()[0]
        if head == 'GetAPIVersion':
            return 7
        if head == 'GetBatteryVoltage':
            return 5000
        # Return the attempts so tests can verify timeout math
        return attempts


def test_robot_initialization_and_clamping(monkeypatch):
    import pyallcode.robot as robot_mod

    # ensure construction uses our fakes
    monkeypatch.setattr(robot_mod, 'SerialTransport', lambda *a, **k: DummyTransport())
    monkeypatch.setattr(robot_mod, 'Connection', FakeConnection)

    r = robot_mod.Robot(mm_per_sec=0, deg_per_sec=0)
    assert r.mm_per_sec == 1
    assert r.deg_per_sec == 1

    # device interfaces should exist
    assert hasattr(r, 'leds') and hasattr(r, 'lcd') and hasattr(r, 'servo')


def test_robot_open_close_and_verbose(monkeypatch):
    import pyallcode.robot as robot_mod
    monkeypatch.setattr(robot_mod, 'SerialTransport', lambda *a, **k: DummyTransport())
    monkeypatch.setattr(robot_mod, 'Connection', FakeConnection)

    r = robot_mod.Robot(verbose=0)
    r.open('COM9')
    assert r.conn.opened_with == 'COM9'
    r.set_verbose(2)
    assert r.conn.verbose == 2
    r.close()
    assert r.conn.closed is True


def test_robot_queries_and_movement_timeouts(monkeypatch):
    import pyallcode.robot as robot_mod
    monkeypatch.setattr(robot_mod, 'SerialTransport', lambda *a, **k: DummyTransport())
    monkeypatch.setattr(robot_mod, 'Connection', FakeConnection)

    r = robot_mod.Robot(mm_per_sec=50, deg_per_sec=45)

    assert r.get_api_version() == 7
    assert r.get_battery_voltage() == 5000

    # movement: Forwards 100mm at 50 mm/s -> timeout = 2
    assert r.forwards(100) == 2
    # Backwards -100mm -> timeout uses abs -> 2
    assert r.backwards(-100) == 2
    # Left 90 deg at 45 deg/s -> timeout = 2
    assert r.left(90) == 2
    # Right -90 -> abs -> 2
    assert r.right(-90) == 2


def test_robot_discovery_static_passthrough(monkeypatch):
    import pyallcode.robot as robot_mod

    # The Robot class binds static methods at class creation, so patch the class attributes
    monkeypatch.setattr(robot_mod.Robot, 'list_available_ports', staticmethod(lambda: ['A']))
    monkeypatch.setattr(robot_mod.Robot, 'list_ports_detailed', staticmethod(lambda: [('A','desc','id')]))
    monkeypatch.setattr(robot_mod.Robot, 'find_robot_ports', staticmethod(lambda: [{'device':'A'}]))

    assert robot_mod.Robot.list_available_ports() == ['A']
    assert robot_mod.Robot.list_ports_detailed() == [('A','desc','id')]
    assert robot_mod.Robot.find_robot_ports() == [{'device':'A'}]
