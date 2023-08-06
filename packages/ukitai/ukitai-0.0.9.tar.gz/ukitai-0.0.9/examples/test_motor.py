from time import sleep

from ukitai import *

link = uKitAiSerialLink.create("/dev/ttyUSB0")
if link.open():
    # Motor
    ack, response = Motor.turn_motor(id=1, direction=Motor.MotorDirection.CLOCKWISE, speed=140, link=link)
    print("Ack={}".format(ack))
    sleep(1)
    ack, response = Motor.turn_motor(id=1, direction=Motor.MotorDirection.ANTICLOCKWISE, speed=140, link=link)
    print("Ack={}".format(ack))
    sleep(1)
    ack, response = Motor.stop_motor(id=1, link=link)
    print("Ack={}".format(ack))
    sleep(1)
    ack, response = Motor.turn_motor_pwm(id=1, direction=Motor.MotorDirection.CLOCKWISE, pwm=1000, link=link)
    print("Ack={}".format(ack))
    sleep(1)
    ack, response = Motor.turn_motor_pwm(id=1, direction=Motor.MotorDirection.ANTICLOCKWISE, pwm=1000, link=link)
    print("Ack={}".format(ack))
    sleep(1)
    ack, response = Motor.stop_motor(id=1, link=link)
    print("Ack={}".format(ack))

    link.close()
else:
    print('Connect Failure!')
