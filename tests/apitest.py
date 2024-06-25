from allcode import buggy, serial_comms
from allcode.enums import Servo, LineSensor

def main():
    car = buggy.Buggy(serial_comms.SerialDevice())
    print(f'API Version: {car.api_version()}')
    print(f'{car.battery_voltage()}V')
    car.forward(100)
    car.backward(50)
    car.left(90)
    car.right(45)
    ir_sensors = [car.ir_sensors.read(i) for i in range(8)]
    print(ir_sensors)
    car.servos.set_speed(Servo.TWO,25)


if __name__ == '__main__':
    main()
