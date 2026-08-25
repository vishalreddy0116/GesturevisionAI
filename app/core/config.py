import json


class Config:

    def __init__(self, path="config/gesture_actions.json"):

        self.path = path
        self.data = self._load()

    def _load(self):

        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_gesture_config(self, gesture):

        return self.data.get(gesture)