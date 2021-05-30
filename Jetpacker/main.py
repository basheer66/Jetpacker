import sys
import pygame
from file_load import *

pygame.init()

SIZE = (WIDTH//1, HIGHT)
pygame.display.set_caption('Jetpacker')
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
'''
class Character:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
'''









bg = imgs["lvl2"]
#bg2 = imgs["lvl3"] # after score test
bgx = 0
bgx2 = bg.get_width()
def render():
    screen.blit(bg, (bgx,0))
    screen.blit(bg, (bgx2, 0))


speed = 30
running = True
while running:
    #Exit loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            running = False

    
    #Screen move
    if bgx < bg.get_width()*-1:
        bgx = bg.get_width()
    if bgx2 < bg.get_width()*-1:
        bgx2 = bg.get_width()
    bgx -= 4.4
    bgx2 -= 4.4
    render()
    pygame.display.update()
    clock.tick(speed)
    
    #Music
    if not (pygame.mixer.music.get_busy()):
        load_music()