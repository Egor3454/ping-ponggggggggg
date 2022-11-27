from pygame import *
from time import time as timer
from random import *
b = (200,255,255)
win_width = 600
win_height = 500
w = display.set_mode((win_width,win_height))
w.fill(b)
display.set_caption('ping-pong')
c = time.Clock()
r = True
class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, size_x, size_y, p_speed):
        super().__init__()
        self.image = transform.scale(image.load(p_image),(size_x,size_y))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        w.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        kp = key.get_pressed()
        if kp[K_UP] and self.rect.y>0:
            self.rect.y -= self.speed
        if kp[K_DOWN] and self.rect.y<400:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        kp = key.get_pressed()
        if kp[K_w] and self.rect.y>0:
            self.rect.y -= self.speed
        if kp[K_s] and self.rect.y<400:
            self.rect.y += self.speed
p1 = Player('racketka.jpg',10,200,80, 100, 10)
p2 = Player2('racketka.jpg',510,200,80, 100, 10)
ba = GameSprite('Myach.jpg',250, 200, 50, 50, 4)
s_x = 3
s_y = 3
font.init()
font = font.SysFont('Arial',80)
finish = False
g_o = False
lose1 = font.render('Проиграл 1', True, (0,170,220))
lose2 = font.render('Проиграл 2', True, (0,170,220))
while r:
    for e in event.get():
        if e.type == QUIT:
            r = False
    w.fill(b) 
    ba.rect.x += s_x
    ba.rect.y += s_y
    p1.update()
    p1.reset()
    p2.update()
    p2.reset()
    ba.update()
    ba.reset()
    if sprite.collide_rect(p1, ba) or sprite.collide_rect(p2, ba):
        s_x *= -1
        s_y *= 1
    if ba.rect.y > win_height - 50 or ba.rect.y < 0:
        s_y *= -1
    if ba.rect.x < 0:
        finish = True
        w.blit(lose1, (90, 200))
        g_o = True
    if ba.rect.x > win_width:
        finish = True
        w.blit(lose2, (90, 200))
        g_o = True
    display.update()
    c.tick(60)
