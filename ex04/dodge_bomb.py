import random as rm
import pygame as pg
import sys


def main():
    pg.display.set_caption("KFCから逃げろやｯｯ!!こうかとん")
    scrn = pg.display.set_mode((1600, 900))

    r = rm.randint(0, 9)
    
    back = pg.image.load("./ex04/pg_bg.jpg")        #背景画像
    back_r = back.get_rect()

    tori = pg.image.load(f"./ex04/fig/{r}.png") 
    tori = pg.transform.rotozoom(tori, 0, 2)
    tori_r = tori.get_rect()
    tori_r.center = 800, 450

    kfc = pg.image.load("./ex04/KFC.jpg")
    kfc = pg.transform.rotozoom(kfc, 0, 0.25)

    key_lst = pg.key.get_pressed()
    

    while True:
        pg.display.update()
        pg.time.Clock().tick(1000)
        scrn.blit(back, back_r)
        scrn.blit(tori, tori_r)
        scrn.blit(kfc, (200, 500))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

            # if event.type == pg.KEYDOWN:
            #     if event.key == pg.K_x:
            #         return
                

if __name__ == "__main__":
    pg.init()   #ゲーム初期化
    main()      #
    pg.quit()   #
    sys.exit()  #