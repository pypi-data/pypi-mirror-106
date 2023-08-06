from time import sleep

from ukitai import *

# List All uKitAi Devices discover by ble
uKitAiBleLink.listDevices()

# Connect by specify Device ID
# link = uKitAiBleLink.create("3F8C61E1-87B0-4300-88E0-D8F3E2F68DBC")  # for MacOS Format
# link = uKitAiBleLink.create("AC:67:B2:76:D8:0E")  # for Linux or Windows Format

# Connect by specify Device Name
link = uKitAiBleLink.create(name='uKit2_04AA')
if link.open():
    ack, response = LedEyes.set_state(id=1, enabled=True, link=link)  # Enabled First
    print("Ack={}".format(ack))
    sleep(0.1)
    ack, response = LedEyes.show_emotion(id=1, emotion=LedEyes.Emotion.BLINK, color=Color.RED, times=3, link=link)
    print("Ack={}".format(ack))
    sleep(5)

    link.close()
else:
    print('Connect Failure!')
