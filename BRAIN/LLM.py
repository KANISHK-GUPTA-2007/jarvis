import languagemodels as llm

from jarvis_speak.speak import speak_safe

def llm1(text: str) -> str:
    
    try:
        response = llm.do(text)
        return str(response).strip() if response else "I'm sorry sir, I couldn't generate a response."

    except Exception as e:
        speak_safe(f"[Error in llm1]: {e}")  # for debugging or logging
        return None
