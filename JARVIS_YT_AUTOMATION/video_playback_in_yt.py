import pyautogui as ui



# Volume
def volume_increase():
    """Increase volume by 5% (Up arrow)."""
    ui.press('up')

def volume_decrease():
    """Decrease volume by 5% (Down arrow)."""
    ui.press('down')

# Seeking (seconds)
def seek_backward_5():
    """Seek backward 5 seconds (Left arrow)."""
    ui.press('left')

def seek_forward_5():
    """Seek forward 5 seconds (Right arrow)."""
    ui.press('right')

def seek_backward_10():
    """Seek backward 10 seconds ('j')."""
    ui.press('j')

def seek_forward_10():
    """Seek forward 10 seconds ('l')."""
    ui.press('l')

# Frame-by-frame when paused
def frame_backward():
    """, (comma) - seek backward 1 frame when paused."""
    ui.press(',')

def frame_forward():
    """. (period) - seek forward 1 frame when paused."""
    ui.press('.')

# Beginning / End
def seek_beginning():
    """Seek to beginning of the video (Home key)."""
    ui.press('home')

def seek_end():
    """Seek to end of the video (End key)."""
    ui.press('end')

# Chapters (Ctrl + Left/Right)
def previous_chapter():
    """Seek to previous chapter (Ctrl + Left)."""
    ui.hotkey('ctrl', 'left')

def next_chapter():
    """Seek to next chapter (Ctrl + Right)."""
    ui.hotkey('ctrl', 'right')

# Playback speed adjustments (< and > correspond to Shift + , or Shift + .)
def decrease_playback_speed():
    """Decrease playback speed (< => Shift + ,)."""
    ui.hotkey('shift', ',')

def increase_playback_speed():
    """> (Shift + .) - increase playback speed."""
    ui.hotkey('shift', '.')

# Playlist navigation
def next_video():
    """Move to the next video (Shift + n)."""
    ui.hotkey('shift', 'n')

def previous_video():
    """Move to the previous video in playlist (Shift + p)."""
    ui.hotkey('shift', 'p')