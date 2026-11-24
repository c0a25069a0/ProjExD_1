import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    original1 = pg.image.load("fig/pg_bg.jpg")
    flipped1 = pg.image.load("fig/pg_bg.jpg")
    flipped1 = pg.transform.flip(flipped1, True, False)
    original2 = pg.image.load("fig/pg_bg.jpg")
    koukaton = pg.image.load("fig/3.png")
    koukaton = pg.transform.flip(koukaton, True, False)
    koukaton_rect = koukaton.get_rect()
    koukaton_rect.center = 300, 200
    tmr = 0
    bg_x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(original1, [-bg_x, 0])
        screen.blit(koukaton, koukaton_rect)
        pg.display.update()
        bg_x += 1
        
        screen.blit(flipped1, [(-bg_x + 1600), 0])
        screen.blit(original2, [(-bg_x + 3200), 0])
        
        tmr += 1
        if(bg_x == 3200):
            bg_x = 0

        key_lst = pg.key.get_pressed() 
        koukaton_rect.move_ip((-1, 0)) 
        if key_lst[pg.K_UP]:
            koukaton_rect.move_ip((0, -1))   
        if key_lst[pg.K_DOWN]:
            koukaton_rect.move_ip((0, 1))  
        if key_lst[pg.K_RIGHT]:
            koukaton_rect.move_ip((2, 0))        
        if key_lst[pg.K_LEFT]:
            koukaton_rect.move_ip((-1, 0))   
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()