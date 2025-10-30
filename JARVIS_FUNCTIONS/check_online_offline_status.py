import pyttsx3
import requests
import time

from jarvis_speak.speak import speak_safe

# --- Persistent Engine Setup ---
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Try to select a female voice
female_voice = None
for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.name.lower() or "susan" in voice.name.lower():
        female_voice = voice.id
        break

engine.setProperty('voice', female_voice or voices[0].id)
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)


def speak(text: str):
    """Speak text using the pre-initialized engine (fast, no delay)."""
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        speak_safe(f"[Error in speak()]: {e}")


# --- Internet Checkers ---
def is_online(url='https://www.google.com', timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return 200 <= response.status_code <= 300
    except requests.ConnectionError:
        return False


def internet_status2():
    if is_online():
        return 'hey sir, where are you? Jarvis is online now. System status: ONLINE'
    else:
        return 'hey sir, system status: OFFLINE'


def real_time_online_checker():
    
    prev_state = None
    while True:
        try:
            current_status = internet_status2()

            if current_status != prev_state:
                print(current_status)
                speak(current_status)
                prev_state = current_status

            # Small delay to prevent constant pinging
            time.sleep(5)

        except Exception as e:
            speak_safe(e)
            pass
