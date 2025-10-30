import pywhatkit
import random
from jarvis_speak.speak import speak_safe
from dlg import search_result

def search_google(text):
    dlg = random.choice(search_result)
    pywhatkit.search(text)
    speak_safe(dlg)

