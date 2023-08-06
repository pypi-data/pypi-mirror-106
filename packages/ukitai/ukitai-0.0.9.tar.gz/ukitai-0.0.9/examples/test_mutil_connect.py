from time import sleep

from ukitai import *

link1 = uKitAiBleLink.create(name='uKit2_04AA')
# link1 = uKitAiSerialLink.create("/dev/ttyUSB0")
link2 = uKitAiBleLink.create(name='uKit2_CCBA')
# link2 = uKitAiSerialLink.create("/dev/ttyUSB1")
if link1.open() and link2.open():
    Audio.play_sound(sound=Audio.Machine.CAR_HORN1, link=link1)
    Audio.play_sound(sound=Audio.Machine.CAR_HORN1, link=link2)
    sleep(3)
    Audio.play_sound(sound=Audio.Animal.ELEPHANT, link=link1)
    Audio.play_sound(sound=Audio.Animal.ELEPHANT, link=link2)
    sleep(3)
    Audio.play_sound(sound=Audio.Emotion.HAPPY, link=link1)
    Audio.play_sound(sound=Audio.Emotion.HAPPY, link=link2)
    sleep(3)
    Audio.play_sound(sound=Audio.Command.COVER, link=link1)
    Audio.play_sound(sound=Audio.Command.COVER, link=link2)
    sleep(3)
else:
    print('Connect Failure!')

if link1.isOpen():
    link1.close()

if link2.isOpen():
    link2.close()
