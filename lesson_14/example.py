

persons = ["person1", "person2"]


def sender(to, msg):
    print(f"send message {msg} to {to}")


def send_something(msg):
    for person in persons:
        sender(person, msg)


def main():
    send_something("halloj")


if __name__ == "__main__":
    main()
