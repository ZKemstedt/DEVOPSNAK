import threading


class AnThread(threading.Thread):

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.running = True
        self.a_text = "a"

    def run(self):
        while self.running:
            self.print_something()

    def print_something(self):
        print("\n" + "printing something")

    def print_text(self):
        print(self.a_text)


def main():
    t1 = AnThread()
    t1.start()
    t1.running = False
    t1.join()


if __name__ == "__main__":

    main()
