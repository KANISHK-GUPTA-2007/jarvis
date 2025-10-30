import requests
from jarvis_speak.speak import speak_safe

from jarvis_listen.listen import *
def get_random_advice():
    res = requests.get('https://api.adviceslip.com/advice').json()
    return res['slip']['advice']

def advice():
    while True:
       
        
        
        speak_safe('ok sir')
        advice = get_random_advice()
        speak_safe(advice)
            
        
