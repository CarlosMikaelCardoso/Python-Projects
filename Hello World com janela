import string
import tkinter as tk

def start_typing(text):
    index = 0
    result.config(text="")
    
    def type_next():
        nonlocal index
        if index < len(text):
            result.config(text=result.cget("text") + text[index])
            index += 1
            result.after(90, type_next)  # Typing speed (20 milliseconds here)

    type_next()

root = tk.Tk()
root.title("Typewriter Effect")

start_button = tk.Button(root, text="Start", command=lambda: start_typing("A"))
start_button.pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()
