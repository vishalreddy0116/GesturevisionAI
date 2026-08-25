from app.actions.action_handler import ActionHandler
from app.actions.input_controller import InputController


class KeyboardActionHandler(ActionHandler):

    def __init__(self):
        self.controller = InputController()

    def execute(self, action):

        if action == "PAUSE":
            self.controller.pause()

        elif action == "STOP":
            self.controller.stop()

        elif action == "CONFIRM":
            self.controller.confirm()

        elif action == "NEXT":
            self.controller.next()

        else:
            print(f"Unknown keyboard action: {action}")