from time import sleep

from ukitai import *

link = uKitAiSerialLink.create("/dev/ttyUSB0")
if link.open():
    # LedBox
    ack, response = LedBox.show_colors(id=1, colors={1: (1, 5, Color.RED), 2: (5, 10, Color.BLUE)}, link=link)
    print("Ack={}".format(ack))
    sleep(5)
    ack, response = LedBox.move_beads(id=1, move_parameters={1: (1, 5), 2: (5, 5)}, link=link)
    print("Ack={}".format(ack))
    sleep(5)
    ack, response = LedBox.set_lights_brightness(id=1, brightness={1: 20, 2: 80}, link=link)
    print("Ack={}".format(ack))
    sleep(5)
    ack, response = LedBox.turn_off(id=1, belts=[1, 2, 3, 4], link=link)
    print("Ack={}".format(ack))
    sleep(5)
    ack, response = LedBox.show_colors_breath(id=1, colors={1: (1, 5, Color.RED), 2: (5, 10, Color.BLUE)}, link=link)
    print("Ack={}".format(ack))
    sleep(5)
    ack, response = LedBox.show_scene(id=1, expressions_type=LedBox.Scene.COLORED_LIGHTS, times=3, color=Color.RED, port=1, link=link)
    print("Ack={}".format(ack))
    sleep(5)
    ack, response = LedBox.show_scene(id=1, expressions_type=LedBox.Scene.DISCO, times=3, color=Color.RED, port=2, link=link)
    print("Ack={}".format(ack))
    sleep(5)
    ack, response = LedBox.show_scene(id=1, expressions_type=LedBox.Scene.PRIMARY_COLOR, times=3, color=Color.RED, port=1, link=link)
    print("Ack={}".format(ack))
    sleep(5)
    ack, response = LedBox.show_scene(id=1, expressions_type=LedBox.Scene.COLOR_STACKING, times=3, color=Color.RED, port=2, link=link)
    print("Ack={}".format(ack))
    sleep(5)
    print("CHARGE_STATUS={}".format(LedBox.read_blet_nums(id=1, link=link)))

    link.close()
else:
    print('Connect Failure!')

