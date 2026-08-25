from app.actions.action_handler import ActionHandler


class MouseActionHandler(ActionHandler):

    def execute(self, action):

        if action == "CLICK":
            print("MOUSE CLICK")

        elif action == "DOUBLE_CLICK":
            print("MOUSE DOUBLE CLICK")

        else:
            print(f"Unknown mouse action: {action}")