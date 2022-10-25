import pygame as pg
import sys

def main():
    pg.display.set_caption("初めてのPyGame")
    scrn_sfc = pg.display.set_mode((800, 600))

    tori_scrn = pg.image.load("./ex04/fig/4.png")
    tori_scrn = pg.transform.rotozoom(tori_scrn, 0, 2)
    tori_rct = tori_scrn.get_rect()
    tori_rct.center = 700, 400
    scrn_sfc.blit(tori_scrn, tori_rct)
    
    clock = pg.time.Clock()
    clock.tick(1)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()