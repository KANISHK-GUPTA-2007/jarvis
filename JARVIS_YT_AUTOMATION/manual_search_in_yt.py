import pyautogui as ui
import time
import random
from jarvis_speak.speak import speak_safe
from dlg import s1, s2




def search_manually(text):
    text = text.replace('search','')
    ui.press('/')
    ui.write(text)
    s12 = random.choice(s1)
    speak_safe(s12)
    time.sleep(0.5)
    ui.press('enter')
    s12 = random.choice(s2)
    speak_safe(s12)

