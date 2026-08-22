import cv2
import time

from app.input.camera import Camera
from app.vision.hand_tracker import HandTracker


def main():

    camera = Camera()
    tracker = HandTracker()

    camera.open()

    while True:

        frame = camera.read()

        timestamp = int(time.time() * 1000)

        result = tracker.detect(frame, timestamp)

        if result.hand_landmarks:

            h, w, _ = frame.shape

            for hand in result.hand_landmarks:
                for landmark in hand:

                    x = int(landmark.x * w)
                    y = int(landmark.y * h)

                    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

            print(f"Detected {len(result.hand_landmarks)} hand(s)")

        cv2.imshow("GestureVisionAI", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()