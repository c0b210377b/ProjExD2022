import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event):
    btn = event.widget
    num = (btn["text"])
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END, num)

den = tk.Tk()
den.title("電卓")
den.geometry("300x555")

entry = tk.Entry(den, width = 10, font = ("", 40), justify = "right")
entry.grid(row = 0, column = 0, columnspan = 3)

r, c = 1, 0
num_list = list(range(9, -1, -1))
add_btn = ["+"]
equal_btn = ["="]
for i, num in enumerate(num_list+add_btn+equal_btn, 1):
    button = tk.Button(den, text = f"{num}", 
    font=("Times New Roman", 30), width = 4, height = 2)
    button.bind("<1>", click_number)
    button.grid(row=r, column = c)
    c += 1
    if i % 3 == 0:
        r += 1
        c = 0
    
den.mainloop()