import json


class ActionMapper:

    def __init__(self, config_path="config/gesture_actions.json"):

        with open(config_path, "r", encoding="utf-8") as file:
            self.actions = json.load(file)

    def map_gesture(self, gesture):
        return self.actions.get(gesture, "NO_ACTION")