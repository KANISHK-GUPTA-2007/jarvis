import pyautogui
from jarvis_speak.speak import speak_safe

def control_mouse_with_voice(text):
    """Control the mouse fully by voice — no coordinates."""
    text = text.lower()

    try:
        if "left" in text:
            pyautogui.moveRel(-150, 0, duration=0.2)
            speak_safe("Moved mouse left.")

        elif "right" in text:
            pyautogui.moveRel(150, 0, duration=0.2)
            speak_safe("Moved mouse right.")

        elif "up" in text:
            pyautogui.moveRel(0, -150, duration=0.2)
            speak_safe("Moved mouse up.")

        elif "down" in text:
            pyautogui.moveRel(0, 150, duration=0.2)
            speak_safe("Moved mouse down.")

        elif "double click" in text:
            pyautogui.doubleClick()
            speak_safe("Double click done.")

        elif "right click" in text:
            pyautogui.rightClick()
            speak_safe("Right click done.")

        elif "press" in text:
            pyautogui.click()
            speak_safe("Click done.")

        elif "stop" in text or "exit" in text:
            speak_safe("Exiting mouse control.")
            return

        else:
            speak_safe("I didn’t understand that mouse text.")

    except Exception as e:
        speak_safe(f"Error controlling mouse: {e}")

