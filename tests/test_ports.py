from types import SimpleNamespace


def make_port(device, description, hwid):
    return SimpleNamespace(device=device, description=description, hwid=hwid)


def test_list_available_ports(monkeypatch):
    import serial.tools.list_ports
    from pyallcode.comm import ports

    ports_list = [
        make_port('COM3', 'USB Serial Device', 'HWID1'),
        make_port('COM7', 'Bluetooth Port', 'HWID2'),
    ]

    monkeypatch.setattr(serial.tools.list_ports, 'comports', lambda: ports_list)

    assert ports.list_available_ports() == ['COM3', 'COM7']


def test_list_ports_detailed(monkeypatch):
    import serial.tools.list_ports
    from pyallcode.comm import ports

    ports_list = [
        make_port('COM3', 'USB Serial Device', 'HWID1'),
        make_port('COM7', 'Bluetooth Port', 'HWID2'),
    ]
    monkeypatch.setattr(serial.tools.list_ports, 'comports', lambda: ports_list)

    assert ports.list_ports_detailed() == [
        ('COM3', 'USB Serial Device', 'HWID1'),
        ('COM7', 'Bluetooth Port', 'HWID2'),
    ]


def test_find_robot_ports_default_keywords(monkeypatch):
    import serial.tools.list_ports
    from pyallcode.comm import ports

    ports_list = [
        make_port('COM3', 'USB Serial Device', 'HWID1'),
        make_port('COM7', 'Bluetooth Port', 'HWID2'),
        make_port('COM9', 'CP210x USB to UART', 'HWID3'),
        make_port('COM11', 'FTDI something', 'HWID4'),
        make_port('COM12', 'Random device', 'HWID5'),
    ]
    monkeypatch.setattr(serial.tools.list_ports, 'comports', lambda: ports_list)

    found = ports.find_robot_ports()
    devices = {p['device'] for p in found}
    assert devices == {'COM3', 'COM7', 'COM9', 'COM11'}


def test_find_robot_ports_custom_keywords(monkeypatch):
    import serial.tools.list_ports
    from pyallcode.comm import ports

    ports_list = [
        make_port('COM3', 'CustomBoard ABC', 'HWID1'),
        make_port('COM7', 'Other device', 'HWID2'),
    ]
    monkeypatch.setattr(serial.tools.list_ports, 'comports', lambda: ports_list)

    found = ports.find_robot_ports(['customboard'])
    assert len(found) == 1
    assert found[0]['device'] == 'COM3'
    assert 'description' in found[0] and 'hwid' in found[0]
