import random
import tkinter as tk
from maze_maker import *
import tkinter.messagebox as tkm

def key_up(event):  #キーを離したら
    global key
    key = ""

def key_down(event):    #キーを押したら
    global key
    key = event.keysym

def main_proc():    #メインの関数
    global mx, my
    global cx, cy
    #上下左右の処理
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    #道とスタート地点の上にいるときの処理
    if maze_lst[my][mx] == 0 or maze_lst[my][mx] == 3:
        cx, cy = mx*100+50, my*100+50
    #ゴール地点の上にいるときの処理
    elif maze_lst[my][mx] == 2:
        cx, cy = mx*100+50, my*100+50
        canv.coords("tori", cx, cy)
        tkm.showinfo("goal", "ｺﾞｰﾙｵﾒﾃﾞﾄｰ")
        return
    #壁の時の処理
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    canv.coords("tori", cx, cy)
    root.after(80, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    maze_lst = make_maze(15, 9)
    #rx, ry はスタート地点とゴール地点の候補座標
    rx = [1, 1, 7, 7]
    ry = [1, 13, 1, 13]
    r1 = random.randint(1, len(rx)-1)       #ランダム関数を定義 
    rxr, ryr = rx.pop(r1), ry.pop(r1)
    maze_lst[rxr][ryr] = 2                  #ランダムでゴール地点を設定
    r1 = random.randint(1, len(rx)-1)       #ランダム関数を再定義
    maze_lst[rx[r1]][ry[r1]] = 3            #ランダムでスタート地点を設定
    
    show_maze(canv, maze_lst)

    r = random.randint(1, 9)
    tori = tk.PhotoImage(file=f"./ex03/fig/{r}.png")    #実行する度にこうかとんの画像を変更
    cx, cy = 0, 0
    mx, my = ry[r1], rx[r1]         #こうかとんの位置をスタート地点の上にする

    canv.create_image(cx, cy, image=tori, tag="tori")

    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()