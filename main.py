import warnings
warnings.filterwarnings("ignore")
import threading
import random
from jarvis_listen.listen import listen, hearing
from _integration_automation import Automation
from _integration_function import Function_cmd
from JARVIS_FUNCTIONS.welcome_greeting import welcome
from JARVIS_FUNCTIONS.wish_greeting import greeting
from JARVIS_FUNCTIONS.advices import advice
from JARVIS_FUNCTIONS.jokes import jokes
from JARVIS_BATTERY_AUTOMATION.battery_alert import battery_alert1
from JARVIS_BATTERY_AUTOMATION.battery_plug_check import check_plug_status
from BRAIN.data_analysis_brain import brain_cmd
from dlg import wake_up_dlg, good_bye_dlg
from jarvis_speak.speak import speak_safe
from BRAIN.gpt4 import generate_and_show_image
from JARVIS_FUNCTIONS.check_online_offline_status import real_time_online_checker
# -------------------- Main listening loop --------------------


def co_main():
    while True:
        text = listen().lower()
        Automation(text)
        Function_cmd(text)
        greeting(text)

        if 'good bye' in text or 'goodbye jarvis' in text or 'goodbye' in text or 'goodbye jar' in text:
            speak_safe(random.choice(good_bye_dlg))
            break
        elif 'jarvis' in text:
            brain_cmd(text)
            
        elif 'give some advice' in text or 'advice' in text:
            advice()

        elif 'crack a joke' in text or 'jokes' in text:
            jokes()
        elif 'generate an image' in text or 'create an image' in text:
            text = text.replace('generate an image', '').replace('create an image', '').replace('jarvis', '')
            generate_and_show_image(text.strip())
        else:
            pass
def main_loop():
    
    while True:
        wake_cmd = hearing().lower()
        if wake_cmd in wake_up_dlg:
            
            welcome()
            co_main() 
        else:
            pass
# -------------------- Jarvis startup --------------------
def jarvis():
    t1 = threading.Thread(target=main_loop)
    t2 = threading.Thread(target=check_plug_status)
    t3 = threading.Thread(target=battery_alert1)
    t4 = threading.Thread(target=real_time_online_checker)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

# -------------------- Entry point --------------------
if __name__ == "__main__":
    jarvis()

