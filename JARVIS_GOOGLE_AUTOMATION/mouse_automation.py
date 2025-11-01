import pyautogui
from jarvis_speak.speak import speak_safe
from jarvis_listen.listen import listen  # your existing voice input function

def control_mouse_with_voice():
    """Control the mouse fully by voice — no coordinates."""
    command = listen().lower()

    try:
        if "left" in command:
            pyautogui.moveRel(-150, 0, duration=0.2)
            speak_safe("Moved mouse left.")

        elif "right" in command:
            pyautogui.moveRel(150, 0, duration=0.2)
            speak_safe("Moved mouse right.")

        elif "up" in command:
            pyautogui.moveRel(0, -150, duration=0.2)
            speak_safe("Moved mouse up.")

        elif "down" in command:
            pyautogui.moveRel(0, 150, duration=0.2)
            speak_safe("Moved mouse down.")

        elif "double click" in command:
            pyautogui.doubleClick()
            speak_safe("Double click done.")

        elif "right click" in command:
            pyautogui.rightClick()
            speak_safe("Right click done.")

        elif "click" in command:
            pyautogui.click()
            speak_safe("Click done.")

        elif "stop" in command or "exit" in command:
            speak_safe("Exiting mouse control.")
            return

        else:
            speak_safe("I didn’t understand that mouse command.")

    except Exception as e:
        speak_safe(f"Error controlling mouse: {e}")
