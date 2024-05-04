import pygame as pg

pg.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pg.display.set_caption('Snake')

clock = pg.time.Clock()

run = True
while run:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
    clock.tick(60)
pg.quit()