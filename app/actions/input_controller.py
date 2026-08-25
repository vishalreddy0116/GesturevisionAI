from pynput.keyboard import Controller, Key


class InputController:

    def __init__(self):
        self.keyboard = Controller()

    def press_key(self, key):
        print(f"KEY PRESS: {key}")
        self.keyboard.press(key)
        self.keyboard.release(key)

    def confirm(self):
        self.press_key(Key.enter)

    def pause(self):
        self.press_key(Key.space)

    def stop(self):
        self.press_key(Key.esc)

    def next(self):
        self.press_key(Key.right)