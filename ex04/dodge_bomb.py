import pygame as pg
import sys

def main():
    pg.display.set_caption("初めてのPyGame")
    scrn_sfc = pg.display.set_mode((1600, 900))
    back = pg.image.load("./ex04/pg_bg.jpg")
    back = pg.transform.rotozoom(back, 0, 1)
    scrn_sfc.blit(back, (0, 0))
    clock = pg.time.Clock()
    clock.tick(0.5)
    pg.display.update()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()