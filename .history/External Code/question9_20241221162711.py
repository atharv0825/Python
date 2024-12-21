import tkinter as tk

root = tk.Tk()

root.title("My GUI App")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenwidth()
root.geometry('500x500')
# Create a label and a button
message = tk.Label(root,text = "HELLO WORLD!")
message.pack()

root.mainloop()

