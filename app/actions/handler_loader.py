import importlib
import pkgutil

from app.actions.action_handler import ActionHandler


class HandlerLoader:

    def load_handlers(self):

        handlers = {}

        package = importlib.import_module("app.actions")

        for module_info in pkgutil.iter_modules(package.__path__):

            module_name = module_info.name

            if not module_name.endswith("_handler"):
                continue

            module = importlib.import_module(
                f"app.actions.{module_name}"
            )

            for name in dir(module):

                obj = getattr(module, name)

                if (
                    isinstance(obj, type)
                    and issubclass(obj, ActionHandler)
                    and obj is not ActionHandler
                ):

                    handler_instance = obj()

                    handler_name = (
                        name.replace("ActionHandler", "")
                        .upper()
                    )

                    handlers[handler_name] = handler_instance

        return handlers