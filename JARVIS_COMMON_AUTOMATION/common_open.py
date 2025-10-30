import pyautogui as ui
from jarvis_speak.speak import *
import time
import random
from dlg import open_dld
def open(text):
    
    speak_safe(random.choice(open_dld) + ' ' + text)
    
    ui.hotkey('win')
    time.sleep(3)
    ui.write(text)
    time.sleep(0.5)
    ui.press('enter')

