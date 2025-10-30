import psutil
import random
from jarvis_speak.speak import speak_safe
from dlg import plug_in,plug_out

message1 = ['charger is plugged ,check confirmed','battery is charging, that means charger is plugged, check confirmed']
message2 = ['charger status unplugged','battery is not charging, that means charger is unplugged, check confirmed']

def check_plug_status():
    battery = psutil.sensors_battery()
    previous_state = battery.power_plugged

    while True:

        battery = psutil.sensors_battery()
        if battery.power_plugged != previous_state:
            if battery.power_plugged:
                random_plug = random.choice(message1)
                speak_safe(random_plug)
            else:
                random_low = random.choice(message2)
                speak_safe(random_low)
            previous_state = battery.power_plugged

previous_state = None
def check_plug_status1():
    global previous_state
    battery = psutil.sensors_battery()
    if battery.power_plugged != previous_state:
        if battery.power_plugged:
            random_plug = random.choice(plug_in)
            speak_safe(random_plug)
        else:
            random_low = random.choice(plug_out)
            speak_safe(random_low)
        previous_state = battery.power_plugged
