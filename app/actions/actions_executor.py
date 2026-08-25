from app.actions.input_controller import InputController


class ActionExecutor:

    def __init__(self):
        self.controller = InputController()

    def execute(self, action):

        if action == "PAUSE":
            self.pause()

        elif action == "STOP":
            self.stop()

        elif action == "CONFIRM":
            self.confirm()

        elif action == "NEXT":
            self.next()

        else:
            print(f"No action mapped for: {action}")

    def pause(self):
        self.controller.pause()

    def stop(self):
        self.controller.stop()

    def confirm(self):
        self.controller.confirm()

    def next(self):
        self.controller.next()