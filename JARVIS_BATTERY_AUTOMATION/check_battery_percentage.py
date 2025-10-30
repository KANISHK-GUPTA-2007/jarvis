import psutil
from jarvis_speak.speak import speak_safe
def battery_percentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)

    speak_safe(f'the device is running on {percent} percent battery power')