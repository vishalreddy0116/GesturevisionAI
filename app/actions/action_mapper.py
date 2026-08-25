import json


class ActionMapper:

    def __init__(self, config_path="config/gesture_actions.json"):

        with open(config_path, "r", encoding="utf-8") as file:
            self.actions = json.load(file)

    def map_gesture(self, gesture):
        config = self.actions.get(gesture)

        if config is None:
            return "NO_ACTION"

        return config["action"]

    def get_handler(self, gesture):
        config = self.actions.get(gesture)

        if config is None:
            return None

        return config["handler"]