import requests

from jarvis_speak.speak import speak_safe

from jarvis_listen.listen import *
def get_random_joke():
    headers = {
        'Accept':'application/json'
    }
    res = requests.get('https://icanhazdadjoke.com/',headers=headers).json()
    return res['joke']

def jokes():
    while True:
        
        
        speak_safe('ok sir')
      
        advice = get_random_joke()
        speak_safe(advice)
           
    
