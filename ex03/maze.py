import tkinter as tk
from maze_maker import *

def key_up(event):
    global key
    key = ""

def key_down(event):
    global key
    key = event.keysym

def main_proc():
    global mx, my
    global cx, cy
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    cx, cy = mx*100+50, my*100+50

    canv.coords("tori", cx, cy)
    root.after(80, main_proc)
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    maze_lst = make_maze(15, 9)
    show_maze(canv, maze_lst)

    tori = tk.PhotoImage(file="./ex03/fig/9.png")
    cx, cy = 300, 400
    mx, my = 1, 1
    canv.create_image(cx, cy, image=tori, tag="tori")

    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()