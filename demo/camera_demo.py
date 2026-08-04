import cv2

from app.input.camera import Camera


def main():
    camera = Camera()

    try:
        camera.open()

        while True:
            frame = camera.read()

            cv2.imshow("GestureVisionAI - Camera Demo", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()