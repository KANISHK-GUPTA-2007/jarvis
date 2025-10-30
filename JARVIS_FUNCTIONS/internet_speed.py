import speedtest
from jarvis_speak.speak import speak_safe

def check_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    
    download_speed = st.download() / 1_000_000  # Convert bits to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert bits to Mbps

    
    speak_safe(f'sir your current internet speed is {round(download_speed)} Mbps download and {round(upload_speed)} Mbps upload')

