import threading
import time


class AThread(threading.Thread):

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.running = True

    def run(self):
        self.set_default_values()
        self.loop()

    def set_default_values(self):
        self.a = 1
        self.b = 2

    def loop(self):
        while self.running:
            time.sleep(1)
            print("Do something\n"*10)
