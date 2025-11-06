import speech_recognition as sr
from colorama import Fore, init
from deep_translator import GoogleTranslator
init(autoreset=True)



def translate_hindi_to_english(text):
    t = GoogleTranslator(
        source='auto',
        target='en'
    )
    tr_word = t.translate(text)
    return tr_word
def listen():
    

    recognizer = sr.Recognizer()

    # Optimized for natural-speed speaking (no cutting off)
    recognizer.dynamic_energy_threshold = False      # fixed sensitivity (faster, stable)
    recognizer.energy_threshold = 150            # moderate sensitivity (adjust 120–200 based on mic)
    recognizer.pause_threshold = 0.9                 # wait ~1 second after you stop speaking
    recognizer.non_speaking_duration = 0.3           # detects speech slightly earlier
    recognizer.operation_timeout = None


    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print(Fore.LIGHTGREEN_EX + 'LISTENING...', end='', flush=True)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

            print('\r' + Fore.LIGHTBLUE_EX + 'Recognizing...', end='', flush=True)
            recognized_txt = recognizer.recognize_google(audio, language='hi-IN').lower()

            if recognized_txt:
                translated_txt = translate_hindi_to_english(recognized_txt)
                print('\r' + Fore.LIGHTYELLOW_EX + f'Mr KANISHK : {translated_txt}')
                return translated_txt
            else:
                return listen()  # retry if nothing recognized

        except sr.WaitTimeoutError:
            print('\r' + Fore.RED + 'JARVIS : No speech detected. Retrying...', flush=True)
            return listen()  # retry on timeout

        except sr.UnknownValueError:
            print('\r' + Fore.RED + 'JARVIS : Could not understand audio. Retrying...', flush=True)
            return listen()  # retry on unknown speech

        finally:
            print('\r', end='', flush=True)


def hearing():
    

    recognizer = sr.Recognizer()

    # Optimized for natural-speed speaking (no cutting off)
    recognizer.dynamic_energy_threshold = False      # fixed sensitivity (faster, stable)
    recognizer.energy_threshold = 100                # moderate sensitivity (adjust 120–200 based on mic)
    recognizer.pause_threshold = 0.9                 # wait ~1 second after you stop speaking
    recognizer.non_speaking_duration = 0.3           # detects speech slightly earlier
    recognizer.operation_timeout = None

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print(Fore.LIGHTGREEN_EX + "Waiting for the JARVIS command...", end='', flush=True)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
            print('\r' + Fore.LIGHTBLUE_EX + "Recognizing...", end='', flush=True)
            recognized_txt = recognizer.recognize_google(audio, language='hi-IN').lower()

            if recognized_txt:
                translated_txt = translate_hindi_to_english(recognized_txt)
                print('\r' + Fore.LIGHTYELLOW_EX + f'Heard: {translated_txt}')
                return translated_txt
            else:
                return ''
        except sr.WaitTimeoutError:
            print('\r' + Fore.RED + "JARVIS : No speech detected.")
            return ''
        except sr.UnknownValueError:
            print('\r' + Fore.RED + "JARVIS : Could not understand audio.")
            return ''
        except sr.RequestError:
            print('\r' + Fore.RED + "JARVIS : Network error while recognizing speech.")
            return ''
        finally:
            print('\r', end='', flush=True)
    
