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
while r:
    for e in event.get():
        if e.type == QUIT:
            r = False
    display.update()
    c.tick(60)
