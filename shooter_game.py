from pygame import *
from time import time as timer
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
p1 = Player('racketka.jpg',515,400,80, 100, 10)
p2 = Player2('racketka.jpg',5,400,80, 100, 10)
while r:
    for e in event.get():
        if e.type == QUIT:
            r = False
    w.fill(b)      
    p1.update()
    p1.reset()
    p2.update()
    p2.reset()
    display.update()
    c.tick(60)
