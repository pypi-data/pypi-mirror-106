from time import sleep

from ukitai import *

link = uKitAiSerialLink.create("/dev/ttyUSB0")
if link.open():
    # Screen
    ack, response = Screen.clear(link=link)
    print("Ack={}".format(ack))

    ack, response = Screen.show_words(text='这是一段静态的文本内容', link=link)
    print("Ack={}".format(ack))
    sleep(3)

    ack, response = Screen.show_marquee_words(text='这是一段动态的文本内容', color=Screen.Color.RED, y=100, link=link)
    print("Ack={}".format(ack))
    sleep(5)

    for color in Screen.Color:
        ack, response = Screen.set_background_color(color=color, link=link)
        print("Ack={}".format(ack))
        sleep(0.5)

    for emotion in Screen.Emotion:
        ack, response = Screen.show_emotion(emotion=emotion, link=link)
        print("Ack={}".format(ack))
        sleep(0.5)

    for traffic_sign in Screen.TrafficSign:
        ack, response = Screen.show_traffic_sign(traffic_sign=traffic_sign, link=link)
        print("Ack={}".format(ack))
        sleep(0.5)

    for fruit in Screen.Fruit:
        ack, response = Screen.show_fruit(fruit=fruit, link=link)
        print("Ack={}".format(ack))
        sleep(0.5)

    for i in range(5):
        ack, response = Screen.set_brightness(brightness=i*20, link=link)
        print("Ack={}".format(ack))
        sleep(0.5)

    ack, response = Screen.start_display_sensor_data(link=link, sensor_type=Screen.SensorType.INFRARED)
    print("Ack={}".format(ack))
    sleep(5)

    ack, response = Screen.start_display_sensor_data(link=link, sensor_type=Screen.SensorType.ULTRASONIC)
    print("Ack={}".format(ack))
    sleep(5)

    ack, response = Screen.start_display_sensor_data(link=link, sensor_type=Screen.SensorType.SOUND)
    print("Ack={}".format(ack))
    sleep(5)

    ack, response = Screen.start_display_sensor_data(link=link, sensor_type=Screen.SensorType.LIGHT)
    print("Ack={}".format(ack))
    sleep(5)

    ack, response = Screen.start_display_sensor_data(link=link, sensor_type=Screen.SensorType.COLOR)
    print("Ack={}".format(ack))
    sleep(5)

    ack, response = Screen.start_display_sensor_data(link=link, sensor_type=Screen.SensorType.HUMITURE)
    print("Ack={}".format(ack))
    sleep(5)

    ack, response = Screen.stop_display_sensor_data(link=link)
    print("Ack={}".format(ack))
    sleep(2)

    ack, response = Screen.show_custom_emotion(name='abc1.jpg', link=link)
    print("Ack={}".format(ack))
    sleep(2)

    ack, response = Screen.set_status_info(visible=True, link=link)
    print("Ack={}".format(ack))
    sleep(2)

    ack, response = Screen.set_status_info(visible=False, link=link)
    print("Ack={}".format(ack))
    sleep(2)

    ack, response = Screen.show_custom_picture(name='abc.jpg', link=link)
    print("Ack={}".format(ack))
    sleep(2)

    ack, response = Screen.off(link=link)
    print("Ack={}".format(ack))

    link.close()
else:
    print('Connect Failure!')

