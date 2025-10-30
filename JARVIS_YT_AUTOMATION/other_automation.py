import pyautogui as ui

def pan_up():
    """Pan up (W)."""
    ui.press('w')

def pan_down():
    """Pan down (S)."""
    ui.press('s')

def pan_left():
    """Pan left (A)."""
    ui.press('a')

def pan_right():
    """Pan right (D)."""
    ui.press('d')

def zoom_in():
    """Zoom in (+ on numpad or ])."""
    # YouTube accepts either + or ] for zooming in
    ui.press('+')  # primary key
    # ui.press(']')  # optional alternate key

def zoom_out():
    """Zoom out (- on numpad or [)."""
    # YouTube accepts either - or [ for zooming out
    ui.press('-')  # primary key
    # ui.press('[')  # optional alternate key

def go_to_search_box():
    """Go to the YouTube search box (/ or : on AZERTY keyboard)."""
    ui.press('/')

def toggle_play_pause():
    """Toggle Play/Pause (K)."""
    ui.press('k')

def toggle_mute():
    """Toggle Mute/Unmute (M)."""
    ui.press('m')

def toggle_fullscreen():
    """Toggle Full Screen mode (F)."""
    ui.press('f')

def toggle_theater_mode():
    """Toggle Theater mode (T)."""
    ui.press('t')

def toggle_miniplayer():
    """Toggle Miniplayer mode (I)."""
    ui.press('i')

def exit_modes():
    """Exit Full Screen / Miniplayer / Close dialogs (Escape)."""
    ui.press('esc')

def toggle_party_mode():
    """Toggle YouTube's 'Party mode' (blinking progress bar) — Easter egg."""
    ui.typewrite('awesome')

def navigate_forward():
    """Navigate forward through controls (Tab)."""
    ui.press('tab')

def navigate_backward():
    """Navigate backward through controls (Shift + Tab)."""
    ui.hotkey('shift', 'tab')

def use_selected_control_space():
    """Activate selected control (Spacebar)."""
    ui.press('space')

def use_selected_control_enter():
    """Activate selected control (Enter)."""
    ui.press('enter')

def navigate_up():
    """Move up in settings menu (Up Arrow)."""
    ui.press('up')

def navigate_down():
    """Move down in settings menu (Down Arrow)."""
    ui.press('down')

def navigate_left():
    """Move left in settings menu (Left Arrow)."""
    ui.press('left')

def navigate_right():
    """Move right in settings menu (Right Arrow)."""
    ui.press('right')

def close_settings_menu():
    """Close the settings menu or exit a dialog (Escape)."""
    ui.press('esc')
    