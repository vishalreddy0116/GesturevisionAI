from app.core.logger import setup_logger
from app.core.config import Config

from app.input.camera import Camera

from app.vision.hand_tracker import HandTracker
from app.vision.gesture_recognizer import GestureRecognizer
from app.vision.gesture_registry import GestureRegistry
from app.vision.gesture_debouncer import GestureDebouncer

from app.actions.action_mapper import ActionMapper
from app.actions.actions_executor import ActionExecutor


class Bootstrap:

    def __init__(self):

        self.logger = setup_logger()

        self.config = Config()

        self.camera = Camera()

        self.tracker = HandTracker()

        self.recognizer = GestureRecognizer()

        self.gesture_registry = GestureRegistry()

        self.action_mapper = ActionMapper()

        self.action_executor = ActionExecutor()

        self.debouncer = GestureDebouncer()

        self.logger.info("GestureVisionAI initialized")