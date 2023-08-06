from time import sleep

from ukitai import *

link = uKitAiSerialLink.create("/dev/ttyUSB0")
if link.open():
    # Audio
    print("VOLUME={}".format(Audio.read_volume(link=link)))
    ack, response = Audio.set_volume(volume=Audio.Volume.MAXIMUM, link=link)
    print("Ack={}".format(ack))
    print("VOLUME={}".format(Audio.read_volume(link=link)))
    ack, response = Audio.play_tone(tone=Audio.Tone.C5, beat=Audio.Beat.ONE, link=link)
    print("Ack={}".format(ack))
    sleep(3)
    ack, response = Audio.set_volume(volume=Audio.Volume.MINIMUM, link=link)
    print("Ack={}".format(ack))
    print("VOLUME={}".format(Audio.read_volume(link=link)))
    ack, response = Audio.play_tone(tone=Audio.Tone.C5, beat=Audio.Beat.ONE, link=link)
    print("Ack={}".format(ack))
    sleep(3)
    ack, response = Audio.set_volume(volume=Audio.Volume.MEDIUM, link=link)
    print("Ack={}".format(ack))
    print("VOLUME={}".format(Audio.read_volume(link=link)))
    ack, response = Audio.play_tone(tone=Audio.Tone.C5, beat=Audio.Beat.ONE, link=link)
    print("Ack={}".format(ack))
    sleep(3)

    ack, response = Audio.play_sound(sound=Audio.Machine.CAR_HORN1, link=link)
    print("Ack={}".format(ack))
    sleep(3)
    ack, response = Audio.play_sound(sound=Audio.Animal.ELEPHANT, link=link)
    print("Ack={}".format(ack))
    sleep(3)
    ack, response = Audio.play_sound(sound=Audio.Emotion.HAPPY, link=link)
    print("Ack={}".format(ack))
    sleep(3)
    ack, response = Audio.play_sound(sound=Audio.Command.COVER, link=link)
    print("Ack={}".format(ack))
    sleep(3)

    record_nums = Audio.read_record_nums(link=link)
    print("RECORD_NUMS={}".format(record_nums))
    if record_nums > 0:
        records = Audio.read_records(link=link)
        print("RECORDS={}".format(records))
        for name, duration in records.items():
            if duration == 0:
                continue
            ack, response = Audio.play_record(name=name, link=link)
            print("Ack={}".format(ack))
            sleep(3)
            ack, response = Audio.stop_play(link=link)
            print("Ack={}".format(ack))

    ack, response = Audio.play_tts(content='这是TTS接口示例', link=link)
    print("Ack={}".format(ack))
    sleep(3)

    print("VOICE_DIRECTION={}".format(Audio.read_voice_direction(link=link)))
    sleep(3)

    asrResult = Audio.read_asr(link=link)
    print("ASR={}".format(asrResult))
    if asrResult is not None:
        ack, response = Audio.play_tts(content=asrResult, link=link)
        print("Ack={}".format(ack))
        sleep(3)

    link.close()
else:
    print('Connect Failure!')

