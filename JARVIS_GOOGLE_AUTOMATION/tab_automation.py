import pyautogui


def open_new_tab():
    pyautogui.hotkey('ctrl', 't')

# 2. Close current tab
def close_tab():
    pyautogui.hotkey('ctrl', 'w')
def refresh_page():
    pyautogui.hotkey('ctrl', 'r')

# 6. Go back
def go_back():
    pyautogui.hotkey('alt', 'left')

# 7. Go forward
def go_forward():
    pyautogui.hotkey('alt', 'right')

# 8. Zoom in
def zoom_in():
    pyautogui.hotkey('ctrl', '+')

# 9. Zoom out
def zoom_out():
    pyautogui.hotkey('ctrl', '-')
def next_tab():
    pyautogui.hotkey('ctrl', 'tab')

# 2. Switch to previous tab
def previous_tab():
    pyautogui.hotkey('ctrl', 'shift', 'tab')

# 3. Open incognito/private window
def open_incognito():
    pyautogui.hotkey('ctrl', 'shift', 'n')

# 4. Save current page (Ctrl + S)
def save_page():
    pyautogui.hotkey('ctrl', 's')

# 5. Open browser history (Ctrl + H)
def open_history():
    pyautogui.hotkey('ctrl', 'h')

# 6. Open downloads page (Ctrl + J)
def open_downloads():
    pyautogui.hotkey('ctrl', 'j')

# 7. Find on page (Ctrl + F)
def find_on_page():
    pyautogui.hotkey('ctrl', 'f')

# 8. Open developer tools (F12)
def open_dev_tools():
    pyautogui.press('f12')

# 9. Mute/unmute tab (Alt + M for some browsers)
def mute_tab():
    pyautogui.hotkey('alt', 'm')

