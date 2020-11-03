import threading
import time

# see [https://docs.python.org/3.8/library/threading.html#lock-objects]


def say_hello_to_person(to_person, from_person, times, lock):
    lock.acquire()
    for i, say in enumerate(range(times)):
        time.sleep(1)
        print(f"hello {to_person} from {from_person} for the {i} time")
    lock.release()


def main():
    lock = threading.Lock()
    t1 = threading.Thread(target=say_hello_to_person, args=("Pelle", "Gustav", 7, lock))
    t2 = threading.Thread(target=say_hello_to_person, args=("Alexander", "Martin", 5, lock))

    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
