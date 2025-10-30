import webbrowser
import random
import time
from dlg import *
from jarvis_speak.speak import speak_safe
def open_website(text):
    website_name = text.lower().strip()

    if website_name in websites:
        random_dlg = random.choice(open_dlg)
        speak_safe(random_dlg + ' ' + website_name)
        # ✅ Get URL safely
        url = websites[website_name]
        

        # ✅ Open site on main thread (more reliable)
        try:
            webbrowser.open(url, new=2)  # new=2 → open in new tab
            time.sleep(1)
            speak_safe(random.choice(success_open))
        except Exception as e:
            print(f"[Error opening site]: {e}")
            speak_safe("Sorry sir, I could not open the website.")
            return

        

    else:
        randomsorry = random.choice(sorry_open)
        speak_safe(randomsorry + 'named' + website_name)
