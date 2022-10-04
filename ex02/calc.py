import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"{txt}のボタンが押されました。")

# root = tk.Tk()
# root.title("(*´Д｀)")
# root.geometry("500x200")

# label = tk.Label(root, 
# text="らべるを書いてみた件", 
# font = ("Ricty Diminished", 30))
# label.pack()

# button = tk.Button(root, 
# text = "押すなよ。絶対に押すなよ", 
# font = ("", 10), bg = "azure")
# button.bind("<1>", button_click)
# button.pack()

# entry = tk.Entry(root, width=30, font = ("", 20), bg = "azure")
# entry.insert(tk.END, "fugapiyo")
# entry.pack()

# #tkm.showwarning("警告", "ボタン押したらアカン言うたやろ、ボケナス")

# root.mainloop()

den = tk.Tk()
den.title("電卓")
den.geometry("300x500")

r, c = 0, 0
for i, num in enumerate(range(9, -1, -1), 1):
    button = tk.Button(den, text = f"{num}", font=("Times New Roman", 30), width = 4, height = 2)
    button.grid(row=r, column = c)
    c += 1
    if i % 3 == 0:
        r += 1
        c = 0
    

#button_1 = tk.Button(den, text="1", font=("Times New Roman", 30))


den.mainloop()