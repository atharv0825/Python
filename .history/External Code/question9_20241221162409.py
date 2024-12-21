import tkinter as tk

root = tk.Tk()

root.title("My GUI App")
root.geometry('')
# Create a label and a button
message = tk.Label(root,text = "HELLO WORLD!")
message.pack()

root.mainloop()

