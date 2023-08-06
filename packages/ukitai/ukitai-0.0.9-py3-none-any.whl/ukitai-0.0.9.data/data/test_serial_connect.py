from time import sleep

from ukitai import *

# List All uKitAi Devices connect to this machine
uKitAiSerialLink.listDevices()

# Connect by specify Device Port
# link = uKitAiSerialLink("COM1")  # for Windows Format
link = uKitAiSerialLink.create("/dev/ttyUSB0")
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
