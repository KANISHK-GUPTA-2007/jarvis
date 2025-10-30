import datetime
from jarvis_speak.speak import speak_safe

def what_is_the_time():
    try:
        current_time = datetime.datetime.now().strftime("%I:%M:%p")
        speak_safe(f'the time is {current_time}')
    except Exception as e:
        error_message = f'An error occurred {e}'
        speak_safe(error_message)
