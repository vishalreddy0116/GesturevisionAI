"""
GestureVisionAI

Application bootstrap.
"""

from app.core.logger import setup_logger


class GestureVisionApp:
    """Application entry point."""

    def __init__(self):

        self.logger = setup_logger()

        self.logger.info("GestureVisionAI starting...")