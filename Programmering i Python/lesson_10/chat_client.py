import tkinter as tk
import threading
import queue
import socket


class Chat(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padx=20)
        self.queue = parent.socketHandler.queue
        self.create_widgets()
        self.bind_widgets()
        self.pack()
        self.fetch_data()

    def create_widgets(self):
        self.chat_label = tk.Label(
            self,
            text="Hello Chat",
            font=('helvetica', 22),
            pady=10
        )
        self.chat_label.grid(
            row=0,
            columnspan=5
        )

        self.chat_entry = tk.Entry(
            self,
            font=("helvetica", 14)
        )
        self.chat_entry.grid(
            row=2,
            column=0,
            sticky=tk.EW,
            columnspan=4,
            pady=20
        )

        self.chat_button = tk.Button(
            self,
            text="Send message"
        )
        self.chat_button.grid(
            row=2,
            column=4,
            sticky=tk.EW,
            padx=(20, 0)
        )

        self.chat_text = tk.Text(
            self,
            font=("helvetica", 14),
            state=tk.DISABLED
        )

        self.chat_text.grid(
            row=1,
            sticky=tk.EW,
            columnspan=5,
            column=0
        )

    def bind_widgets(self):
        self.chat_entry.bind("<Return>", self.submit_chat_message)
        self.chat_button.bind("<Return>", self.submit_chat_message,)
        self.chat_button.bind("<Button-1>", self.submit_chat_message, "+")

    def submit_chat_message(self, event=None):
        self.save_text()
        self.clear_entry_text()

    def save_text(self):
        text = self.chat_entry.get()
        # This is not a good way, which thread will call?
        # What about error handling
        self.master.socketHandler.send(text.encode())
        self.set_text(text)

    def set_text(self, text):
        self.chat_text.configure(state=tk.NORMAL)
        self.chat_text.insert(tk.END, f'> {text}\n')
        self.chat_text.configure(state=tk.DISABLED)

    def clear_entry_text(self):
        self.chat_entry.delete(0, tk.END)

    def fetch_data(self):
        # This should probably be in a class with base Text
        # See [https://effbot.org/zone/tkinter-threads.htm]
        # Fetching from queue and sleep 100ms
        while not self.queue.empty():
            try:
                # get_nowait vs get? look in queue docs, (blocking vs non blocking)
                line = self.queue.get_nowait()
                self.set_text(line)
                # Why this line? look in queue docs
                self.queue.task_done()
            except queue.Empty:
                pass
        self.after(100, self.fetch_data)


class MainWindow(tk.Tk):
    def __init__(self, parent, socketHandler):
        super().__init__(parent)
        self.socketHandler = socketHandler
        self.create_chat()
        # this is needed to handle shutdown
        self.protocol("WM_DELETE_WINDOW", self.handler)

    def create_chat(self):
        self.chat = Chat(self)

    def handler(self):
        # this is strange, needs refactoring
        self.socketHandler.close()
        try:
            self.destroy()
        except Exception:
            pass


class SocketHandler(threading.Thread):

    def __init__(self, queue, sock, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.queue = queue
        self.running = True
        self.sock = sock

    def run(self):

        while self.running:
            try:
                data = self.sock.recv(4096)
                if(data):
                    self.queue.put(data.decode())
                if(data == b''):
                    pass
            except BlockingIOError:
                pass
            except Exception as e:
                print(e)

    def send(self, message):
        print(threading.current_thread())
        self.sock.sendall(message)

    def close(self):
        print("Sockethandler running set to false")
        self.running = False
        print("sockethandler closing socket")
        self.sock.close()
        print("sockethandler joining")
        self.join()


def open_connection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 12345))
    return sock


def main():
    # this queue should probably be owned by a instance instead
    q = queue.Queue()
    # This has no handling if the socket breaks
    # This could be in a App class, setting, starting closing etc.
    socketHandler = SocketHandler(q, open_connection(), daemon=True)
    socketHandler.start()
    mw = MainWindow(None, socketHandler)
    mw.mainloop()


if __name__ == "__main__":
    main()
