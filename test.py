from pynput.keyboard import Key, Controller

import time

def tag(n):
    keyboard = Controller()
    keyboard.press('@')
    keyboard.release('@')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    for i in range(1,n-1):
        keyboard.press('@')
        keyboard.release('@')
        for j in range(i):
            keyboard.press(Key.down)
            keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

print("hello world")