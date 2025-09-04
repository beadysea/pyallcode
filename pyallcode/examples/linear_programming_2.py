#!/usr/bin/env python
"""

Filename:
"""
__version__ = "1.0.0"
__author__ = "type your name here"
__date__ = "type the date in yyyy-mm-dd format"
import time
import math
from pyallcode.devices.light_sensor import LightSensor
from pyallcode.devices.leds import LEDs
from pyallcode.serial_comms import SerialDevice


def main() -> None:
    """_summary_"""
    serial = SerialDevice()
    light_sensor = LightSensor(serial)
    leds = LEDs(serial)

    light_sample_1 = light_sensor.read()
    led_value = math.floor(light_sample_1 * 255 / 4095)
    leds.write(led_value)
    print(f"Light Sample 1: {light_sample_1}")
    time.sleep(10)
    light_sample_2 = light_sensor.read()
    led_value = math.floor(light_sample_2 * 255 / 4095)
    leds.write(led_value)
    print(f"Light Sample 2: {light_sample_2}")
    time.sleep(10)
    light_sample_3 = light_sensor.read()
    led_value = math.floor(light_sample_3 * 255 / 4095)
    leds.write(led_value)
    print(f"Light Sample 3: {light_sample_3}")
    time.sleep(10)
    light_sample_4 = light_sensor.read()
    led_value = math.floor(light_sample_4 * 255 / 4095)
    leds.write(led_value)
    print(f"Light Sample 4: {light_sample_4}")
    time.sleep(10)
    light_sample_5 = light_sensor.read()
    led_value = math.floor(light_sample_5 * 255 / 4095)
    leds.write(led_value)
    print(f"Light Sample 5: {light_sample_5}")
    time.sleep(10)
    light_sample_6 = light_sensor.read()
    led_value = math.floor(light_sample_6 * 255 / 4095)
    leds.write(led_value)
    print(f"Light Sample 6: {light_sample_6}")


if __name__ == "__main__":
    main()
