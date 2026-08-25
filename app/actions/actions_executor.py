from app.actions.input_controller import InputController


class ActionExecutor:

    def __init__(self):

        self.controller = InputController()

        self.actions = {
            "PAUSE": self.controller.pause,
            "STOP": self.controller.stop,
            "CONFIRM": self.controller.confirm,
            "NEXT": self.controller.next,
        }

    def execute(self, action):

        action_function = self.actions.get(action)

        if action_function is None:
            print(f"No action mapped for: {action}")
            return

        action_function()