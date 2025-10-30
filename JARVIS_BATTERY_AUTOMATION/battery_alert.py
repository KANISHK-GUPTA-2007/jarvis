import time
import psutil
import random
from jarvis_speak.speak import speak_safe
from dlg import low_b, last_low, full_battery

def battery_alert():
    while True:
        time.sleep(10)
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent<30:
            random_low = random.choice(low_b)
            speak_safe(random_low)
        
        elif percent<10:
            random_low = random.choice(last_low)
            speak_safe(random_low)
        
        elif percent == 100:
            random_low = random.choice(full_battery)
            speak_safe(random_low)

        else:
            pass



def battery_alert1():
    
    time.sleep(8)
    battery = psutil.sensors_battery()
    percent = int(battery.percent)

    if percent<30:
        random_low = random.choice(low_b)
        speak_safe(random_low)
                
    elif percent<10:
        random_low = random.choice(last_low)
        speak_safe(random_low)
                
    elif percent == 100:
        random_low = random.choice(full_battery)
        speak_safe(random_low)

    else:
        pass