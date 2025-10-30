import pyautogui as ui

def toggle_captions():
    """Toggle On/Off subtitles/closed captions if available (C)."""
    ui.press('c')

def increase_font_size():
    """Rotate through font sizes (increasing) (+)."""
    ui.press('+')

def decrease_font_size():
    """Rotate through font sizes (decreasing) (-)."""
    ui.press('-')

def cycle_text_opacity():
    """Rotate through different text opacity levels (O)."""
    ui.press('o')

def cycle_window_opacity():
    """Rotate through different window opacity levels (W)."""
    ui.press('w')