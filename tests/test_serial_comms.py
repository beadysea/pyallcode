import unittest
from unittest import mock
from allcode import serial_comms


class TestSerialDevice(unittest.TestCase):
    def setUp(self):
        serial_patcher = mock.patch('serial.Serial')
        self.mock_serial = serial_patcher.start()
        self.addCleanup(serial_patcher.stop)

        self.device = serial_comms.SerialDevice()

    
    def test_device_send_message_calls_mock_serial_readline(self):
        self.device.send_message('')
        mock.MagicMock.assert_called(self.mock_serial.readline)

    # when we create a serial device the serial_for_url causes
    # these tests to fail when multiple test are run.
    # the problem only happens when we assert mock_serial.write is called.
    def test_device_send_message_calls_mock_serial_write(self):
        self.device.send_message('')
        mock.MagicMock.assert_called(self.mock_serial.write)

    def test_device_send_message_calls_mock_serial_write_with_data(self):
        self.device.send_message('test_message\n')
        mock.MagicMock.assert_called_with(
            self.mock_serial.write, b'test_message\n')
