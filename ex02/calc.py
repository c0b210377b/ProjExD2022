import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END, num)

def click_equal(evenet):
    eqn = entry.get()
    result = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

def click_delete(event):
    entry.delete(0, tk.END)

den = tk.Tk()
den.title("電卓")
den.geometry("500x800")

entry = tk.Entry(den, width = 10, font = ("", 40), justify = "right")
entry.grid(row = 0, column = 0, columnspan = 3)

r, c = 2, 0
num_list = [7, 8, 9, 4, 5, 6, 1, 2, 3, 0, "00"]
ope1_btn = ["."]
for i, num in enumerate(num_list+ope1_btn, 1):
    button = tk.Button(den, text = f"{num}", 
    font=("Times New Roman", 30), width = 4, height = 2, bg="white")
    button.bind("<1>", click_number)
    button.grid(row=r, column = c)
    c += 1
    if i % 3 == 0:
        r += 1
        c = 0

btn = tk.Button(den, text = "AC", font = ("Times New Roman", 30), width = 4, height = 2, bg="azure")
btn.bind("<1>", click_delete)
btn.grid(row = 2, column = 5)

en_lst = ["+", "-", "*", "/"]
for i, en in enumerate(en_lst, 2):
    btn = tk.Button(den, text=en, font=("Times New Roman", 30), width = 4, height = 2, bg="azure")
    btn.bind("<1>", click_number)
    btn.grid(row = i, column = 4)

btn = tk.Button(den, text=f"=", font=("Times New Roman", 30), width = 4, height = 2, bg="azure")
btn.bind("<1>", click_equal)
btn.grid(row = 3, column = 5)

den.mainloop()