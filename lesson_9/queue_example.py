import threading
import time
import queue


class PrintSomething(threading.Thread):
    def __init__(self, q, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.running = True
        self.q = q

    def run(self):
        while self.running:
            try:
                q.get()
                self.print_something()
                q.task_done()
            except Exception as e:
                print(e)
                pass

    def print_something(self):
        print(f"current {threading.current_thread()}")
        for _ in range(10):
            print("hello")


q = queue.Queue()
printSomething = PrintSomething(q, daemon=True)
printSomething.start()
while True:
    for i in range(10):
        print(f"main loop iteration {i}")
        time.sleep(1)
        if(i == 5):
            q.put("do some work")
