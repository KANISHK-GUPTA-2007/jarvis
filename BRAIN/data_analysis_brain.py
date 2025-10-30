
from gpt4 import *
from BRAIN.google_big_data import *
from BRAIN.google_small_data import *
from BRAIN.LLM import *
from jarvis_speak.speak import *
def brain_cmd(text):
    if 'jarvis' in text:
        text = text.replace('jarvis','')
        text = text.strip()
        if 'who is' in text or 'search about' in text or 'check who is' in text or 'is' in text:
            speak_safe(get_brief_summary(text))
        elif 'generate' in text or 'write' in text or 'make' in text:
            response = llm2(text).strip()
            speak_safe(response)
        elif 'analysis' in text or 'check on internet' in text or 'reasearch' in text:
            text.replace('analysis','')
            text.replace('check on internet','')
            text.replace('reasearch','')

            speak_safe(run_chat(text))
        else:
            x = llm1(text)
            speak_safe(x)



