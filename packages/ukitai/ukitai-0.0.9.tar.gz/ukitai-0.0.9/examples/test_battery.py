from time import sleep

from ukitai import *

link = uKitAiSerialLink.create("/dev/ttyUSB0")
if link.open():
    # Battery
    print("BATTERY_LEVEL={}".format(Battery.read_battery_level(link=link)))
    sleep(0.1)
    print("BATTERY_STATUS={}".format(Battery.read_battery_status(link=link)))
    sleep(0.1)
    print("CHARGE_STATUS={}".format(Battery.read_charge_status(link=link)))

    link.close()
else:
    print('Connect Failure!')
