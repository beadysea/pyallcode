import unittest
from unittest import mock
from pyallcode.robot import Robot


class TestRobot(unittest.TestCase):
    def setUp(self):
        self.mock_serial = mock.MagicMock()
        self.rv = Robot(self.mock_serial)
        self.send = self.mock_serial.send_message

    def test_write_calls_serial_interface_write_method_with_message(self):
        message = "Forwards 1000\n"
        self.rv.device.send_message(message)
        mock.MagicMock.assert_called_with(self.send, "Forwards 1000\n")

    def test_api_version_returns_3(self):
        self.mock_serial.send_message.return_value = 3
        result = self.rv.api_version()
        self.assertEqual(result, 3)

    def test_battery_voltage_returns_4_1(self):
        self.mock_serial.send_message.return_value = 410
        result = self.rv.battery_voltage()
        self.assertEqual(result, 4.1)

    def test_forward_calls_send_message_with_message(self):
        self.rv.forward(1000)
        mock.MagicMock.assert_called_with(self.send, "Forwards 1000\n")

    def test_forward_with_raises_value_error_when_distance_is_greater_than_1000(self):
        with self.assertRaises(ValueError):
            self.rv.forward(1001)

    def test_forward_with_raises_value_error_when_distance_is_less_than_0(self):
        with self.assertRaises(ValueError):
            self.rv.forward(-1)

    def test_reverse_calls_serial_interface_write_method_with_message(self):
        self.rv.backward(1000)
        mock.MagicMock.assert_called_with(self.send, "Backwards 1000\n")

    def test_reverse_with_raises_value_error_when_distance_is_greater_than_1000(self):
        with self.assertRaises(ValueError):
            self.rv.backward(1001)

    def test_reverse_with_raises_value_error_when_distance_is_less_than_0(self):
        with self.assertRaises(ValueError):
            self.rv.backward(-1)

    def test_left_calls_send_message_method_with_message(self):
        self.rv.left(360)
        mock.MagicMock.assert_called_with(self.send, "Left 360\n")

    def test_left_with_raises_value_error_when_angle_is_greater_than_360(self):
        with self.assertRaises(ValueError):
            self.rv.left(361)

    def test_left_with_raises_value_error_when_angle_is_less_than_0(self):
        with self.assertRaises(ValueError):
            self.rv.left(-1)

    def test_right_calls_serial_interface_write_method_with_message(self):
        self.rv.right(360)
        mock.MagicMock.assert_called_with(self.send, "Right 360\n")

    def test_right_with_raises_value_error_when_angle_is_greater_than_360(self):
        with self.assertRaises(ValueError):
            self.rv.right(361)

    def test_right_with_raises_value_error_when_angle_is_less_than_0(self):
        with self.assertRaises(ValueError):
            self.rv.right(-1)
