from JARVIS_YT_AUTOMATION.other_automation import *
from dlg import *
from jarvis_listen.listen import listen
from JARVIS_YT_AUTOMATION.captions_for_yt_videos import *
from jarvis_speak.speak import speak_safe
from JARVIS_YT_AUTOMATION.manual_search_in_yt import *
from JARVIS_YT_AUTOMATION.play_music_on_yt import *
from JARVIS_YT_AUTOMATION.play_pause_yt_videos import *
from JARVIS_YT_AUTOMATION.search_on_yt import *
from JARVIS_YT_AUTOMATION.video_playback_in_yt import *

def youtube_cmd(text):
    

    # Music play command
    if text in x:  # x contains triggers like "play music"
        speak_safe(random.choice(q))
        # If text already contains song info, use it; otherwise ask
        song_text = listen().lower()
        play_music_on_youtube(song_text)
        

    # Basic playback controls
    elif text in x1:
        play()
    elif text in x2:
        pause()
    elif text in ['increase volume', 'volume badao']:
        volume_increase()
    elif text in ['decrease volume', 'volume kam karo']:
        volume_decrease()
    elif text in ['10 seconds forward', '10 second aage']:
        seek_forward_10()
    elif text in ['10 seconds backward', '10 second peeche']:
        seek_backward_10()
    elif text in ['5 seconds forward', '5 second aage']:
        seek_forward_5()
    elif text in ['5 seconds backward', '5 second peeche']:
        seek_backward_5()
    elif text in ['forward frame', 'aage frame']:
        frame_forward()
    elif text in ['backward frame', 'peeche frame']:
        frame_backward()
    elif text in ['seek to beginning', 'video ki shuruaat par jao']:
        seek_beginning()
    elif text in ['seek to end', 'video ke end par jao']:
        seek_end()
    elif text in ['seek to previous chapter', 'previous chapter par jao']:
        previous_chapter()
    elif text in ['seek to next chapter', 'next chapter par jao']:
        next_chapter()
    elif text in ['decrease playback speed', 'playback speed kam karo']:
        decrease_playback_speed()
    elif text in ['increase playback speed', 'playback speed badhao']:
        increase_playback_speed()
    elif text in ['move to next video', 'next video par jao']:
        next_video()
    elif text in ['move to previous video', 'previous video par jao']:
        previous_video()
    elif text in ['toggle subtitles', 'captions on karo', 'captions off karo']:
        toggle_captions()
    elif text in ['increase font size', 'font size badao']:
        increase_font_size()
    elif text in ['decrease font size', 'font size kam karo']:
        decrease_font_size()
    elif text in ['rotate text opacity', 'text opacity badlo']:
        cycle_text_opacity()
    elif text in ['rotate window opacity', 'window opacity badlo']:
        cycle_window_opacity()
    elif text in ['pan up', 'upar jao']:
        pan_up()
    elif text in ['pan down', 'neeche jao']:
        pan_down()
    elif text in ['pan left', 'left jao']:
        pan_left()
    elif text in ['pan right', 'right jao']:
        pan_right()
    elif text in ['zoom in', 'zoom in karo']:
        zoom_in()
    elif text in ['zoom out', 'zoom out karo']:
        zoom_out()
    elif text in ['go to search box', 'search box par jao']:
        go_to_search_box()
    elif text in ['toggle play pause', 'play pause karo']:
        toggle_play_pause()
    elif text in ['toggle mute', 'mute unmute karo']:
        toggle_mute()
    elif text in ['toggle fullscreen', 'fullscreen karo']:
        toggle_fullscreen()
    elif text in ['toggle theater mode', 'theater mode karo']:
        toggle_theater_mode()
    elif text in ['toggle miniplayer', 'miniplayer karo']:
        toggle_miniplayer()
    elif text in ['exit modes', 'exit karo']:
        exit_modes()
    elif text in ['toggle party mode', 'party mode karo']:
        toggle_party_mode()
    elif text in ['navigate forward', 'aage jao']:
        navigate_forward()
    elif text in ['navigate backward', 'peeche jao']:
        navigate_backward()

    # Search on YouTube
    elif 'search in youtube' in text or 'search on youtube' in text:
        search_text = text.replace('search on youtube','').replace('search in youtube','').replace('search','').strip()
        youtube_search(search_text)

    elif 'search in current youtube window' in text or 'search on current youtube window' in text or 'search current youtube window' in text or 'search' in text:
        search_text = text.replace('search on current youtube window','')\
                          .replace('search in current youtube window','')\
                          .replace('search current youtube window','')\
                          .replace('search','').strip()
        search_manually(search_text)

    else:
        pass


