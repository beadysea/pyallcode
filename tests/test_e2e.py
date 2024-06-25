from time import sleep
import unittest
from allcode import buggy, serial_comms

class TestEndToEnd(unittest.TestCase):
    def setUp(self):
        self.car = buggy.Buggy(serial_comms.SerialDevice())
    
    def test_forwards(self):
        self.car.forward(500)

    def test_reverse(self):
        self.car.backward(500)

    def test_left(self):
        self.car.left(360)
    
    def test_right(self):
        self.car.right(360)

    def test_LEDs(self):
        #testing leds on function
        for i in range(8):
            self.car.leds.on(i)
            sleep(0.1)
        sleep(1)
        
        #testing leds off function
        for i in range(7, -1, -1):
            self.car.leds.off(i)
            sleep(0.1)

        # testing the leds write function 
        self.car.leds.write(255)
        sleep(0.5)
        self.car.leds.write(0)

    #These tests take a while so we run them last
    def test_set_motor_speed(self):
        #run motors through the full speed range
        for i in range(100, -101, -1):
            self.car.set_motor_speeds(i,i)
        self.car.set_motor_speeds(0,0)
        
        #100% reverse direction test
        self.car.set_motor_speeds(100,-100)
        sleep(1)
        self.car.set_motor_speeds(-100,100)
        sleep(1)
        self.car.set_motor_speeds(0,0)

