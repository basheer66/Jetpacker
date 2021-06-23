import pygame
from file_load import *
from main import screen
#bg2 = imgs["lvl3"] # after score test

class Moving_background:
    def __init__(self, bg):
        self.bgx = 0
        self.bg = bg
        self.bgx2 = self.bg.get_width()
    def bg_blit(self):
        screen.blit(self.bg, (self.bgx,0))
        screen.blit(self.bg, (self.bgx2, 0))
        if self.bgx < self.bg.get_width()*-1:
            self.bgx = self.bg.get_width()
        if self.bgx2 < self.bg.get_width()*-1:
            self.bgx2 = self.bg.get_width()
        self.bgx -= 2.2
        self.bgx2 -= 2.2