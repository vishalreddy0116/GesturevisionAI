import cv2
import time

from app.core.bootstrap import Bootstrap


def main():

    # Initialize GestureVisionAI
    system = Bootstrap()

    camera = system.camera
    tracker = system.tracker
    recognizer = system.recognizer
    registry = system.gesture_registry
    action_mapper = system.action_mapper
    executor = system.action_executor
    debouncer = system.debouncer

    camera.open()

    system.logger.info("Camera started")

    while True:

        frame = camera.read()

        timestamp = int(time.time() * 1000)

        result = tracker.detect(frame, timestamp)

        if result.hand_landmarks:

            h, w, _ = frame.shape

            for hand in result.hand_landmarks:

                # Recognize gesture
                gesture = recognizer.recognize(hand)

                # Convert internal gesture to display name
                gesture_name = registry.get_name(gesture)

                # Map gesture to action
                action = action_mapper.map_gesture(gesture)

                # Get handler
                handler_name = action_mapper.get_handler(gesture)

                # Execute only when gesture changes
                if debouncer.should_trigger(gesture):

                    system.logger.info(
                        f"Gesture: {gesture_name} | "
                        f"Action: {action} | "
                        f"Handler: {handler_name}"
                    )

                    if handler_name is not None:
                        executor.execute(
                            action,
                            handler_name
                        )

                # Draw landmarks
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

                # Display gesture and action
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

            cv2.putText(
                frame,
                "No hand detected",
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        cv2.imshow(
            "GestureVisionAI",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

    system.logger.info("GestureVisionAI stopped")


if __name__ == "__main__":
    main()