class ActionRegistry:

    def __init__(self):
        self.handlers = {}

    def register(self, name, handler):
        self.handlers[name] = handler

    def get_handler(self, name):
        return self.handlers.get(name)