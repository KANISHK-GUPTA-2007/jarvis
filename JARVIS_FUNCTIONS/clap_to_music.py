import sounddevice as sd
import numpy as np
from scipy.signal import butter, lfilter
import time
import random
from yt_dlp import YoutubeDL
import vlc
from dlg import playsong_1
from jarvis_speak.speak import speak_safe

# === Audio settings ===
SAMPLE_RATE = 44100
BLOCK_DURATION = 0.01
LOW_CUT = 2000
HIGH_CUT = 5000
SENSITIVITY = 4.0
DOUBLE_CLAP_WINDOW = 0.6
MIN_CLAP_GAP = 0.25

# --- Band-pass filter ---
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

b, a = butter_bandpass(LOW_CUT, HIGH_CUT, SAMPLE_RATE)

def apply_filter(data):
    return lfilter(b, a, data)

def rms(sig):
    return np.sqrt(np.mean(np.square(sig)))

# --- Globals ---
avg_rms = 0.0
clap_times = []
player = None
music_playing = False

def get_audio_url(url):
    ydl_opts = {
        "format": "bestaudio/best",
        "noplaylist": True,
        "quiet": True,
        "skip_download": True
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info["url"]

def play_music():
    global player, music_playing
    if not music_playing:
        song_name = random.choice(list(playsong_1.keys()))
        url = playsong_1[song_name]
        speak_safe(f"Playing '{song_name}'")
        audio_url = get_audio_url(url)
        player = vlc.MediaPlayer(audio_url)
        player.play()
        music_playing = True
    else:
        speak_safe("Music already playing.")

def stop_music():
    global player, music_playing
    if music_playing:
        speak_safe("Stopping music...")
        player.stop()
        player = None
        music_playing = False

def callback(indata, frames, time_info, status):
    global avg_rms, clap_times
    data = indata[:, 0]
    filtered = apply_filter(data)
    current_rms = rms(filtered)
    avg_rms = 0.9 * avg_rms + 0.1 * current_rms
    now = time.time()
    if avg_rms > 0 and current_rms > avg_rms * SENSITIVITY:
        if len(clap_times) == 0 or now - clap_times[-1] > MIN_CLAP_GAP:
            clap_times.append(now)
            print(f"👏 Clap detected ")

# --- Main entry function ---
def start_clap_detector():
    global clap_times
    with sd.InputStream(channels=1, samplerate=SAMPLE_RATE,
                        blocksize=int(SAMPLE_RATE * BLOCK_DURATION),
                        callback=callback):
        try:
            while True:
                now = time.time()
                clap_times = [t for t in clap_times if now - t <= DOUBLE_CLAP_WINDOW]

                if len(clap_times) == 1 and music_playing:
                    stop_music()
                    clap_times = []
                elif len(clap_times) >= 2:
                    play_music()
                    clap_times = []

                time.sleep(0.01)

        except KeyboardInterrupt:
            speak_safe("Exiting...")
            stop_music()


