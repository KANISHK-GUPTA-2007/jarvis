import random
from jarvis_speak.speak import speak_safe
from dlg import *

def welcome():
    speak_safe(random.choice(welcome_adv))