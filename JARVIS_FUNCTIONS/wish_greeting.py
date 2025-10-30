from datetime import date
import datetime
from jarvis_speak.speak import speak_safe
today = date.today()
formatted_date = today.strftime("%D %B %y")
nowx = datetime.datetime.now()

def wish():
    current_hour = nowx.hour
    if 5<= current_hour < 12:
        speak_safe('good morning sir')
    elif 12<= current_hour < 17:
        speak_safe('goog afternoon sir ')
    elif 17 <= current_hour < 21:
        speak_safe('good evening sir ')
    else:
        speak_safe('good night sir ')

def greeting(text):
    if 'good morning' in text or 'good afternoon' in text or 'good evening' in text or 'good night' in text:
        wish()
    else:
        pass