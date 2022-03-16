import tkinter as tk
import random
window = tk.Tk()

button = tk.Button(text='clik here', bg="white", fg="black")
button.pack(pady = 20, padx = 20)
lijst = ["blue", "pink", "green", "orange"]


# schijf hier tussen je code
buttonclick = 0
def clicked():
    global buttonclick
    if buttonclick == 0:
        print("on")
        window.config(bg=random.choice(lijst))
        button = tk.Button(text="hello there", bg ="black", fg="white")
        buttonclick += 1
    elif buttonclick == 1:
        print("off")
        window.config(bg=random.choice(lijst))
        button = tk.Button(text="Hello there", bg="white", fg="black")
        buttonclick -= 1
button.config(command=clicked)
# schijf hier tussen je code

window.mainloop()