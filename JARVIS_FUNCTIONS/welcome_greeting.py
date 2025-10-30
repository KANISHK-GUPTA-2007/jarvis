import random
from jarvis_speak.speak import speak_safe
from dlg import *
import threading


def welcome():
    speak_safe(random.choice(welcome_adv))