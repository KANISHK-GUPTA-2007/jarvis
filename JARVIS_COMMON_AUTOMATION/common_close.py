import random
import pyautogui as ui
from dlg import close_dld
from jarvis_speak.speak import speak_safe
close_dlg = random.choice(close_dld)
def close():
    speak_safe(close_dlg)
    ui.hotkey('alt','f4')