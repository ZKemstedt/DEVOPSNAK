import tkinter as tk


class Chat(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padx=20)
        self.create_widgets()
        self.bind_widgets()
        self.pack()

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
        self.chat_text.configure(state=tk.NORMAL)
        self.chat_text.insert(tk.END, f'> {text}\n')
        self.chat_text.configure(state=tk.DISABLED)

    def clear_entry_text(self):
        self.chat_entry.delete(0, tk.END)


class MainWindow(tk.Tk):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_chat()

    def create_chat(self):
        self.chat = Chat(self)


def main():
    mw = MainWindow(None)
    mw.mainloop()


if __name__ == "__main__":
    main()
