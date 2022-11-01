import random as rm
import pygame as pg
import sys
import os

# パス名の
main_dir = os.path.split(os.path.abspath(__file__))[0]

# 画面を生成するクラス
class Screen:
    def __init__(self, title, wh, bg_image):
        pg.display.set_caption(title)       
        self.sfc = pg.display.set_mode(wh)    
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bg_image)   
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

# こうかとんを設定を行うクラス
class Bird:
    key_delta = {
    pg.K_UP:    [0, -3],
    pg.K_DOWN:  [0, +3],
    pg.K_LEFT:  [-3, 0],
    pg.K_RIGHT: [+3, 0],
    }

    def __init__(self, image, zoom, xy):
        sfc = pg.image.load(image)      
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)     
        self.rct = self.sfc.get_rect()
        self.rct.center = xy        

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)    # 練習3

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr)

# 爆弾の設定を行うクラス
class Bomb:
    bai1 = 1.0005
    bai2 = 1.0003

    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((2*radius, 2*radius)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く    # (255, 0, 0)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = rm.randint(100, scr.rct.width-100)
        self.rct.centery = rm.randint(100, scr.rct.height-100)
        self.vx, self.vy = vxy 

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) 

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko * Bomb.bai1
        self.vy *= tate * Bomb.bai2
        self.blit(scr)

# 爆弾以外の動く物体の設定を行うクラス
class Rival:
    bai1 = 1.0005
    bai2 = 1.0003

    def __init__(self, image, zoom, xy, scr:Screen):
        sfc = pg.image.load(image)
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = rm.randint(100, scr.rct.width-100)
        self.rct.centery = rm.randint(100, scr.rct.height-100)
        self.x, self.y = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) 

    def update(self, scr:Screen):
        self.rct.move_ip(self.x, self.y)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.x *= yoko * Bomb.bai1
        self.y *= tate * Bomb.bai2
        self.blit(scr)


def check_bound(obj_r, scrn_r):
    """
    obj_r  : こうかとん_r または 爆弾_r
    scrn_r : スクリーン_r
    領域内：+1 / 領域外: -1
    """

    yoko, tate = +1, +1
    if obj_r.left < scrn_r.left or scrn_r.right < obj_r.right:
        yoko = -1
    if obj_r.top < scrn_r.top or scrn_r.bottom < obj_r.bottom:
        tate = -1
    return yoko, tate

# BGMや効果音をロードする関数
def load_sound(file):
    if not pg.mixer:
        return None
    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print("Warning, unable to load, %s" % file)
    return None


def main():
    scr = Screen("逃げなよ！こうかとん", (1600, 900), "./ex05/data/pg_bg.jpg")
    r = rm.randint(0, 9)
    kkt = Bird(f"./ex05/fig/{r}.png", 2.0, (900, 400))  # 出力する度に画像が変更される
    bomb = Bomb((255, 0, 0), 10, (+1, +1), scr)
    kfc = Rival("./ex05/data/KFC.jpg", 0.3, (+1, +1), scr)
    chicken = Rival("./ex05/data/chicken_honetsuki.png", 0.3, (+1, +1), scr)

    clock =  pg.time.Clock()    

    screem_sound = load_sound("「ぐああーーっ！」.mp3") # 効果音の設定
    agemono_sound = load_sound("餃子を揚げる.mp3")  # 効果音の設定
    if pg.mixer:
        music = os.path.join(main_dir, "data", "漢祭り.mp3")    # BGMの設定
        pg.mixer.music.load(music)
        pg.mixer.music.set_volume(0.1)  # BGMの音量を下げる
        pg.mixer.music.play(-1)

    while True:
        scr.blit()  #スクリーンの設置

        #終了イベントの処理
        for event in pg.event.get():    
            if event.type == pg.QUIT:
                return

        kkt.update(scr) # こうかとんの設置

        bomb.update(scr)    # 爆弾の設置

        kfc.update(scr) # KFCの設置

        chicken.update(scr) # チキンの設置

        key_state = pg.key.get_pressed()
        
        if kkt.rct.colliderect(bomb.rct): # こうかとんが爆弾と重なったら終わり
            return
        
        if kkt.rct.colliderect(kfc.rct):   #こうかとんとKFCが重なったら悲鳴をあげる
            if pg.mixer:
                screem_sound.set_volume(0.3)    # 効果音の音量を下げる
                screem_sound.play()
            clock.tick(10)
            
        if kkt.rct.colliderect(chicken.rct):    # こうかとんがチキンと重なったら揚げものの音がする
            agemono_sound.set_volume(0.3)   # 効果音の音量を下げる
            agemono_sound.play()
            clock.tick(10)

        if key_state[pg.K_r]:           #やり直し機能
            main()
            return

        pg.display.update()
        clock.tick(1000)
        agemono_sound.stop()    # チキンから離れたら、揚げ物の音をストップ

if __name__ == "__main__":
    pg.init()   #ゲーム初期化
    main()      #ゲーム本体
    pg.quit()   #初期化の解除
    sys.exit()  