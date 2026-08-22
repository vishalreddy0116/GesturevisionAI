import cv2
import time

from app.input.camera import Camera
from app.vision.hand_tracker import HandTracker
from app.vision.gesture_recognizer import GestureRecognizer
from app.vision.gesture_registry import GestureRegistry


def main():

    camera = Camera()
    tracker = HandTracker()
    recognizer = GestureRecognizer()
    registry = GestureRegistry()

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

                # Convert gesture ID/code to readable name
                gesture_name = registry.get_name(gesture)

                print(f"Gesture: {gesture_name}")

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
                # Display gesture
                # -----------------------------
                cv2.putText(
                    frame,
                    gesture_name,
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

        else:
            # No hand detected
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
        cv2.imshow("GestureVisionAI", frame)

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()