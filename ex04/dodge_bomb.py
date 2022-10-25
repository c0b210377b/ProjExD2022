import random as rm
import pygame as pg
import sys


def main():
    pg.display.set_caption("KFCから逃げろやｯｯ!!こうかとん")
    scrn = pg.display.set_mode((1600, 900))
    scrn_r = scrn.get_rect()
    r = rm.randint(0, 9)
    
    back = pg.image.load("./ex04/pg_bg.jpg")        #背景画像
    back_r = back.get_rect()

    tori = pg.image.load(f"./ex04/fig/{r}.png")     #こうかとん画像
    tori = pg.transform.rotozoom(tori, 0, 2)
    tori_r = tori.get_rect()
    tori_r.center = 900, 400

    kfc = pg.image.load("./ex04/KFC.jpg")           #カーネルサンダース
    kfc = pg.transform.rotozoom(kfc, 0, 0.3)

    bomb = pg.Surface((20, 20))
    pg.draw.circle(bomb, (255, 0, 0), (10, 10), 10) #円を描く
    bomb.set_colorkey((0, 0, 0))                    #四隅の黒い部分を等価させる
    bomb_r = bomb.get_rect()
    bomb_r.centerx, bomb_r.centery = rm.randint(0, scrn_r.width), rm.randint(0, scrn_r.height)

    clock =  pg.time.Clock()    

    while True:
        scrn.blit(back, back_r)         #スクリーンに背景を貼る
        scrn.blit(kfc, (200, 500))      

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_state = pg.key.get_pressed()
        if key_state[pg.K_UP]:          #こうかとんの縦座標を-1
            tori_r.centery -= 1
        if key_state[pg.K_DOWN]:        #こうかとんの縦座標を+1
            tori_r.centery += 1
        if key_state[pg.K_LEFT]:        #こうかとんの横座標を-1
            tori_r.centerx -= 1
        if key_state[pg.K_RIGHT]:       #こうかとんの横座標を+1
            tori_r.centerx += 1
        scrn.blit(tori, tori_r)         #スクリーンにこうかとんを貼る

        scrn.blit(bomb, bomb_r)
        
        pg.display.update()
        clock.tick(1000)
                

if __name__ == "__main__":
    pg.init()   #ゲーム初期化
    main()      #
    pg.quit()   #
    sys.exit()  #