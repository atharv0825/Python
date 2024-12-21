import tkinter as tk

root = tk.Tk()

root.title("My GUI App")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f'{screen_width}x{screen_height}')
# Create a label and a button
message = tk.Label(root,text = "HELLO WORLD!")
message.pack()

root.resizable(False,False)
root.mainloop()

