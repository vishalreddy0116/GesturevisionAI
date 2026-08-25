class GestureDebouncer:

    def __init__(self):
        self.previous_gesture = None

    def should_trigger(self, gesture):

        # No gesture detected
        if gesture is None:
            self.previous_gesture = None
            return False

        # First gesture after no gesture
        if self.previous_gesture is None:
            self.previous_gesture = gesture
            return True

        # Same gesture still being held
        if gesture == self.previous_gesture:
            return False

        # Gesture changed
        self.previous_gesture = gesture
        return True