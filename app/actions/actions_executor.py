from app.actions.action_registry import ActionRegistry
from app.actions.handler_loader import HandlerLoader


class ActionExecutor:

    def __init__(self):

        self.registry = ActionRegistry()

        loader = HandlerLoader()

        handlers = loader.load_handlers()

        for name, handler in handlers.items():
            self.registry.register(name, handler)

    def execute(self, action, handler_name):

        handler = self.registry.get_handler(handler_name)

        if handler is None:
            print(f"No handler registered for: {handler_name}")
            return

        handler.execute(action)