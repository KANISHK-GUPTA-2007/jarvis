import pyautogui as ui



def scroll_up():
    ui.press('up')
    ui.press('up')
    ui.press('up')
    ui.press('up')
    ui.press('up')

def scroll_down():
    ui.press('down')
    ui.press('down')
    ui.press('down')
    ui.press('down')
    ui.press('down')
    
def scroll_to_top():
    ui.hotkey('home')
def scroll_to_bottom():
    ui.hotkey('end')