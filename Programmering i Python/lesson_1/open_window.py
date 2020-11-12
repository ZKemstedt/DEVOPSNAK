import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="hello tk", font=("impact", 40))
label.pack(side=tk.RIGHT)
text = tk.Text(root)

root.mainloop()
