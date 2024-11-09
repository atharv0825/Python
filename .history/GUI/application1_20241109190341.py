import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("My first TKINTER APP")
window.geometry("500x500")

label = tk.Label(window,text="Hello, TKINTER !")
label.pack(pady=20)

def change_text():
    label.config(text="You clicked the button!")

button = tk.Button(window, text="Click Me", command=change_text)
button.pack(pady=10)

window.mainloop()