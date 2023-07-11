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


def handle_click(event):
    participants = Element("numparticipants").element.value
    time = Element("time").element.value
    print(participants, time)

participants = Element("numparticipants").element.value
time = Element("time").element.value

buttons = js.document.querySelectorAll("#tag")
for button in buttons:
    button.onclick = handle_click