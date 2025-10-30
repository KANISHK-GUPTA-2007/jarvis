import random
import time
import webbrowser
from jarvis_speak.speak import speak_safe
from dlg import yt_search,s2,s1
import pyautogui as ui 
def youtube_search(text):
    dlg = random.choice(yt_search)
    speak_safe(dlg)
    webbrowser.open('https://www.youtube.com')
    time.sleep(4)
    ui.press('/')
    ui.write(text)
    s12 = random.choice(s1)
    speak_safe(s12)
    time.sleep(0.5)
    ui.press('enter')
    s12 = random.choice(s2)
    speak_safe(s12)


