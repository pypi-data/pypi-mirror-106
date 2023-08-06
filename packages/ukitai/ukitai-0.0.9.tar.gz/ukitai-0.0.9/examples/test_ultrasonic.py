from time import sleep

from ukitai import *

link = uKitAiSerialLink.create("/dev/ttyUSB0")
if link.open():
    # Ultrasonic
    ack, response = Ultrasonic.set_state(id=1, enabled=True, link=link)  # Enabled First
    print("Ack={}".format(ack))
    sleep(0.1)
    ack, response = Ultrasonic.show_color_rgb(id=1, color=Color.RED, time=2000, link=link)
    print("Ack={}".format(ack))
    sleep(5)
    ack, response = Ultrasonic.show_color_rgb(id=1, color=Color.BLUE, time=0xFFFFFFFF, link=link)
    print("Ack={}".format(ack))
    sleep(5)
    ack, response = Ultrasonic.turn_off_light(id=1, link=link)
    print("Ack={}".format(ack))

    link.close()
else:
    print('Connect Failure!')
