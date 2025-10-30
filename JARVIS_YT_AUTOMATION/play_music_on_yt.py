from dlg import playing_dlg,playsong
import time
import webbrowser

import random

from jarvis_speak.speak import speak_safe
def play_music_on_youtube(text):
    playdlg = random.choice(playing_dlg)
    speak_safe(playdlg)
    
    time.sleep(1)
    if text in playsong:
        webbrowser.open(playsong[text])
    else:
        speak_safe("Sorry sir, I don't have that song in my playlist.")
        
    

