import random as rm
import pygame as pg
import sys


def main():
    pg.display.set_caption("初めてのPyGame")
    scrn = pg.display.set_mode((1600, 900))
    r = rm.randint(0, 9)
    kfc = pg.image.load("./ex04/KFC.jpg")
    back = pg.image.load("./ex04/pg_bg.jpg")
    tori = pg.image.load(f"./ex04/fig/{r}.png")
    kfc = pg.transform.rotozoom(kfc, 0, 0.25)
    tori = pg.transform.rotozoom(tori, 0, 2)
    back = pg.transform.rotozoom(back, 0, 1)

    key_lst = pg.key.get_pressed()
    

    while True:
        pg.display.update()
        pg.time.Clock().tick(1000)
        scrn.blit(back, (0, 0))
        scrn.blit(tori, (900, 400))
        scrn.blit(kfc, (200, 500))

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_x:
                    return
                

if __name__ == "__main__":
    pg.init()   #ゲーム初期化
    main()      #
    pg.quit()   #
    sys.exit()  #