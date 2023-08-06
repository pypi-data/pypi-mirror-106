from time import sleep

from ukitai import *

link = uKitAiSerialLink.create("/dev/ttyUSB0")
if link.open():
    ack, response = InfraredSensor.set_state(id=1, enabled=True, link=link)  # Enabled First
    print("Ack={}".format(ack))
    ack, response = TouchSensor.set_state(id=1, enabled=True, link=link)  # Enabled First
    print("Ack={}".format(ack))
    ack, response = ColorSensor.set_state(id=1, enabled=True, link=link)  # Enabled First
    print("Ack={}".format(ack))
    ack, response = Ultrasonic.set_state(id=1, enabled=True, link=link)  # Enabled First
    print("Ack={}".format(ack))
    for i in range(5):
        print("INFRARED_DISTANCE={}".format(InfraredSensor.read_distance(id=1, link=link)))
        sleep(0.1)
        print("ULTRASONIC_DISTANCE={}".format(Ultrasonic.read_distance(id=1, link=link)))
        sleep(0.1)
        print("SOUND_STRONG={}".format(SoundSensor.read_sound_strong(id=1, link=link)))
        sleep(0.1)
        print("BRIGHTNESS={}".format(LuxSensor.read_brightness(id=1, link=link)))
        sleep(0.1)
        print("HUMIDITY={}".format(HumiditySensor.read_humidity(id=1, link=link)))
        sleep(0.1)
        print("TEMPERATURE_C={}".format(HumiditySensor.read_temperature(id=1, link=link)))
        sleep(0.1)
        print("TEMPERATURE_F={}".format(HumiditySensor.read_temperature_f(id=1, link=link)))
        sleep(0.1)
        print("COLOR_RED={}".format(ColorSensor.read_red_value(id=1, link=link)))
        sleep(0.1)
        print("COLOR_GREEN={}".format(ColorSensor.read_green_value(id=1, link=link)))
        sleep(0.1)
        print("COLOR_BLUE={}".format(ColorSensor.read_blue_value(id=1, link=link)))
        sleep(0.1)
        print("TOUCH_STATUS={}".format(TouchSensor.read_touch_status(id=1, link=link)))
        sleep(0.1)
        pass

    link.close()
else:
    print('Connect Failure!')
