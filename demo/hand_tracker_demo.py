import cv2
import time

from app.input.camera import Camera
from app.vision.hand_tracker import HandTracker
from app.vision.gesture_recognizer import GestureRecognizer
from app.vision.gesture_registry import GestureRegistry
from app.vision.gesture_debouncer import GestureDebouncer
from app.actions.action_mapper import ActionMapper
from app.actions.actions_executor import ActionExecutor


def main():

    camera = Camera()
    tracker = HandTracker()
    recognizer = GestureRecognizer()
    registry = GestureRegistry()
    action_mapper = ActionMapper()
    executor = ActionExecutor()
    debouncer = GestureDebouncer()

    camera.open()

    while True:

        frame = camera.read()

        timestamp = int(time.time() * 1000)

        result = tracker.detect(frame, timestamp)

        if result.hand_landmarks:

            h, w, _ = frame.shape

            for hand in result.hand_landmarks:

                # -----------------------------
                # Recognize gesture
                # -----------------------------
                gesture = recognizer.recognize(hand)

                gesture_name = registry.get_name(gesture)

                # -----------------------------
                # Map gesture to action
                # -----------------------------
                action = action_mapper.map_gesture(gesture)

                # -----------------------------
                # Trigger action only once
                # when gesture appears/changes
                # -----------------------------
                if debouncer.should_trigger(gesture):

                    print(
                        f"Gesture: {gesture_name} | "
                        f"Action: {action}"
                    )

                    executor.execute(action)

                # -----------------------------
                # Draw hand landmarks
                # -----------------------------
                for landmark in hand:

                    x = int(landmark.x * w)
                    y = int(landmark.y * h)

                    cv2.circle(
                        frame,
                        (x, y),
                        5,
                        (0, 255, 0),
                        -1
                    )

                # -----------------------------
                # Display gesture and action
                # -----------------------------
                cv2.putText(
                    frame,
                    f"{gesture_name} -> {action}",
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

        else:

            # -----------------------------
            # No hand detected
            # Reset gesture state so that
            # the same gesture can trigger
            # again when shown
            # -----------------------------
            debouncer.should_trigger(None)

            cv2.putText(
                frame,
                "No hand detected",
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        # -----------------------------
        # Display camera
        # -----------------------------
        cv2.imshow(
            "GestureVisionAI",
            frame
        )

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()