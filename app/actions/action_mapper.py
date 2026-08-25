class ActionMapper:

    def __init__(self):
        self.actions = {
            "OPEN_PALM": "PAUSE",
            "FIST": "STOP",
            "THUMBS_UP": "CONFIRM",
            "VICTORY": "NEXT",
        }

    def map_gesture(self, gesture):
        return self.actions.get(gesture, "NO_ACTION")