class Car:

    def __init__(self):
        self.started = False

    def horn(self):
        return "loud sound"

    def start(self):
        self.started = True

    def stop(self):
        self.started = False
