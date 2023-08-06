from time import sleep

from ukitai import *


def _print_identify_result(name: str, result: list):
    if result is None:
        print('{} Result is None'.format(name.upper()))
        return
    print('{} Result is'.format(name.upper()))
    for _i in range(len(result)):
        print('\tNo.{} - {}'.format(_i, result[_i]))


link = uKitAiSerialLink.create("/dev/ttyUSB0")
if link.open():
    # Vision
    for i in range(10):
        print("MID_OFFSET={}".format(Vision.get_mid_offset(link=link)))
        sleep(0.5)

    for i in range(10):
        print("FACE_NUM={}".format(Vision.face_num_identify(link=link)))
        sleep(0.5)

    for i in range(10):
        _print_identify_result('traffic_identify', Vision.traffic_identify(link=link))
        sleep(0.5)

    for i in range(10):
        _print_identify_result('face_identify', Vision.face_identify(link=link))
        sleep(0.5)

    for i in range(10):
        _print_identify_result('gender_identify', Vision.gender_identify(link=link))
        sleep(0.5)

    for i in range(10):
        _print_identify_result('mask_identify', Vision.mask_identify(link=link))
        sleep(0.5)

    for i in range(10):
        _print_identify_result('emotion_identify', Vision.emotion_identify(link=link))
        sleep(0.5)

    for i in range(10):
        _print_identify_result('gesture_identify', Vision.gesture_identify(link=link))
        sleep(0.5)

    for i in range(10):
        _print_identify_result('garbage_identify', Vision.garbage_identify(link=link))
        sleep(0.5)

    for i in range(10):
        _print_identify_result('model_toys_identify', Vision.model_toys_identify(link=link))
        sleep(0.5)

    for i in range(10):
        _print_identify_result('traffic_light_identify', Vision.traffic_light_identify(link=link))
        sleep(0.5)

    for i in range(10):
        _print_identify_result('handwritten_digit_identify', Vision.handwritten_digit_identify(link=link))
        sleep(0.5)

    for i in range(10):
        _print_identify_result('handwritten_letter_identify', Vision.handwritten_letter_identify(link=link))
        sleep(0.5)

    for i in range(10):
        _print_identify_result('color_identify', Vision.color_identify(link=link))
        sleep(0.5)

    for i in range(10):
        _print_identify_result('custom_color_identify', Vision.custom_color_identify(link=link))
        sleep(0.5)

    link.close()
else:
    print('Connect Failure!')

