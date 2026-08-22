class GestureRegistry:

    def __init__(self):
        self.gestures = {
            "OPEN_PALM": "Open Palm",
            "FIST": "Fist",
            "THUMBS_UP": "Thumbs Up",
            "VICTORY": "Victory",
        }

    def get_name(self, gesture_id):
        return self.gestures.get(gesture_id, "Unknown")

    def register(self, gesture_id, display_name):
        self.gestures[gesture_id] = display_name