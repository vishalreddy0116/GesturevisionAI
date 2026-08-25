class ActionExecutor:

    def execute(self, action):
        if action == "PAUSE":
            self.pause()

        elif action == "STOP":
            self.stop()

        elif action == "CONFIRM":
            self.confirm()

        elif action == "NEXT":
            self.next()

        else:
            print("No action executed.")

    def pause(self):
        print("PAUSE action executed")

    def stop(self):
        print("STOP action executed")

    def confirm(self):
        print("CONFIRM action executed")

    def next(self):
        print("NEXT action executed")