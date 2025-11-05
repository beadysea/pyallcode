def test_public_exports():
    import pyallcode
    assert isinstance(pyallcode.__all__, list)
    for name in ["Robot", "list_available_ports", "list_ports_detailed", "find_robot_ports"]:
        assert name in pyallcode.__all__
        assert hasattr(pyallcode, name)


def test_imports_work():
    from pyallcode import Robot, list_available_ports, list_ports_detailed, find_robot_ports
    assert callable(Robot)
    assert callable(list_available_ports)
    assert callable(list_ports_detailed)
    assert callable(find_robot_ports)
