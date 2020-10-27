import threading


class AThread(threading.Thread):

    def __init__(self, *arg, **kwargs):
        (super().__init__)(*arg, **kwargs)
        self.running = True

    def run(self):
        self.loop()

    def loop(self):
        while self.running:
            pass
