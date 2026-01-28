# 🤖 JARVIS – AI Desktop Voice Assistant

JARVIS is a Python-based desktop voice assistant inspired by fictional AI systems. It integrates speech recognition, text-to-speech, AI-powered responses, image generation, automation tools, and a graphical interface using Tkinter to provide an interactive and intelligent desktop experience.

---

## ✨ Features

- 🎙️ Voice recognition (Speech-to-Text)
- 🔊 Text-to-speech (Edge TTS)
- 🧠 AI-powered conversation (g4f / language models)
- 🖼️ AI image generation using Pollinations API
- 🪟 Tkinter-based GUI windows
- ⚡ Multithreaded design for smooth performance
- 🌐 Web search & Wikipedia queries
- 🖱️ Desktop automation (keyboard & mouse control)
- 🎵 Media control & YouTube playback
- 🛠 Modular project structure for easy expansion

---

## 🏗️ Project Structure

```
JARVIS/
│
├── BRAIN/
│   ├── gpt4.py
│   ├── logic.py
│   └── image_generator.py
│
├── UI/
│   └── main_window.py
│
├── voice/
│   ├── speech_recognition.py
│   └── tts.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 📘 Setup & Usage Instructions

### Step 1: Install Python

Install **Python 3.10 or 3.11 (recommended)**

Check:

```
python --version
```

Download from:

https://www.python.org/downloads/

---

### Step 2: Create Virtual Environment (Recommended)

```
python -m venv venv
```

Activate:

**Windows**
```
venv\Scripts\activate
```

**Linux / macOS**
```
source venv/bin/activate
```

---

### Step 3: Install Dependencies

If you have `requirements.txt`:

```
pip install -r requirements.txt
```

Or install manually:

```
pip install speechrecognition edge-tts pillow requests sounddevice soundfile pyautogui pywhatkit wikipedia colorama deep-translator g4f flask pygame yt-dlp pandas numpy scipy nltk beautifulsoup4 lxml
```

---

### Step 4: Check Microphone

Ensure:

- Microphone is connected
- Windows microphone permission is enabled
- No other app is using the mic

Test:

```
python -m speech_recognition
```

---

### Step 5: Run JARVIS

From the project root folder:

```
python main.py
```

---

## 🎮 How to Use JARVIS

1. Start the program
2. Wait for initialization
3. Speak commands clearly

Example commands:

- What is artificial intelligence
- Generate an image of a cyberpunk city
- Open YouTube
- Play music
- Tell me a joke
- Search Wikipedia for Albert Einstein

AI images will open in a new window automatically.

---

## 🖼️ AI Image Generation

JARVIS uses the **Pollinations AI API** to generate images from text prompts.

Example:

Generate an image of a futuristic robot assistant

Images are displayed in a Tkinter window and are not saved to disk by default.

---

## 🛑 Common Issues & Fixes

### Microphone not working
- Reconnect microphone
- Reinstall sounddevice & SpeechRecognition
- Run terminal as Administrator

### Tkinter image error
Ensure this line exists in your code:

```
label.image = tk_img
```

### Slow responses
- Check internet connection
- Reduce background applications

---

## 🔄 Update Project

```
git pull origin main
```

---

## 🧹 Exit Assistant

Say:

```
exit
```

or

```
quit
```

Or close the terminal window.

---

## 📌 Future Improvements

- Wake word detection
- Face recognition
- Plugin system
- Offline AI models
- UI themes
- Mobile integration
- Task scheduling

---

## 📜 License

MIT License

---

## 👤 Author

Kanishk  
Student & Developer

---

## ⭐ Acknowledgements

OpenAI  
Pollinations AI  
Python Community  
Edge TTS  
Tkinter Developers  

---

If you find this project useful, consider giving it a ⭐ on GitHub!


