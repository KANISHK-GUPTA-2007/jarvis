from http import client
import os
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
from io import BytesIO
from PIL import Image, ImageTk
import urllib.parse
import tkinter as tk
import threading


def speak_safe(msg):
    print("JARVIS:", msg)


def generate_and_show_image(prompt):
    """Generate and show an AI image quickly (no saving, manual close to exit)."""

    def fetch_image():
        try:
            speak_safe("Generating AI image, please wait for some time.")

            # Pollinations API (no API key required)
            encoded_prompt = urllib.parse.quote(prompt)
            url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

            response = requests.get(url, timeout=20)
            response.raise_for_status()

            # Convert to image in memory
            img = Image.open(BytesIO(response.content)).resize((800, 800))

            # Schedule GUI creation in main thread
            root.after(0, lambda: show_image_window(prompt, img))

        except Exception as e:
            speak_safe(f"[Error generating image]: {e}")

    def show_image_window(title, img):
        """Display image and allow manual close to quit."""
        win = tk.Toplevel(root)
        win.title(title)
        win.geometry("820x820")

        # Display image
        tk_img = ImageTk.PhotoImage(img)
        label = tk.Label(win, image=tk_img)
        label.image = tk_img
        label.pack(fill="both", expand=True)

        speak_safe("Image displayed successfully.")

        # When user closes window, quit Tkinter completely
        win.protocol("WM_DELETE_WINDOW", lambda: (win.destroy(), root.quit()))

    # Fetch in background to keep UI responsive
    threading.Thread(target=fetch_image, daemon=True).start()


# --- MAIN ---
    root = tk.Tk()
    root.withdraw()  # Hide main window (we only use Toplevel)

# Call the function (non-blocking)


# Run Tkinter event loop — ends when window is closed
    root.mainloop()

