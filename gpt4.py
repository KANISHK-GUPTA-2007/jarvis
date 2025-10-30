import threading

from g4f.client import Client

from jarvis_speak.speak import speak_safe

def llm2(text: str) -> str:
    
    try:
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Jarvis, an advanced AI assistant created to help the user with respect. "
                        "Always address the user as 'sir' and respond politely, clearly, and intelligently."
                    ),
                },
                {"role": "user", "content": text},
            ],
        )

        reply = response.choices[0].message.content.strip()
        return reply

    except Exception as e:
        speak_safe(f"[Error in llm2]: {e}")  # for debugging/logs
        return "Apologies sir, I encountered a small issue while processing your request."
import requests
from PIL import Image, ImageTk
from io import BytesIO
import urllib.parse
import tkinter as tk
import multiprocessing
from jarvis_speak.speak import speak_safe

def _show_image_window(prompt, img_data):
    root = tk.Tk()
    root.title(prompt)
    root.geometry("800x800")

    img = Image.open(BytesIO(img_data))
    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=tk_img)
    label.image = tk_img
    label.pack()

    root.mainloop()


def generate_and_show_image(prompt):
    speak_safe("Generating AI image, please wait for some time")

    encoded_prompt = urllib.parse.quote(prompt)
    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

    try:
        response = requests.get(image_url, timeout=60)
        response.raise_for_status()

        # Open the image directly in memory — no saving
        img_data = response.content

        # Start a separate process for Tkinter display
        p = multiprocessing.Process(target=_show_image_window, args=(prompt, img_data))
        p.start()

        speak_safe("Image displayed successfully.")

    except Exception as e:
        speak_safe(f"[Error generating image]: {e}")



generate_and_show_image(" futuristic cityscape at sunset, vibrant colors, high detail ")
