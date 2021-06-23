import sys
import pygame
from file_load import *
import math
import random


pygame.init()

SIZE = (WIDTH, HIGHT)
FPS = 60
TIME = 0 #60 per second
BG_SPEED = 2.2
COINS = 3
SPIKES = 3
JETPACK_POWER = 8
GRAVITY = 5
SCORE = 0

#Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.display.set_caption('Jetpacker')
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

#usefull functions
def get_d(o1, o2):
    return int(math.sqrt((math.pow(o2[0]-o1[0],2)) + (math.pow(o2[1]-o1[1],2))))
def isCollision(object_1, object_2):
    return (get_d(object_1, object_2) <= 30)



#Character
class Character:
    def __init__(self, img, x, y):
        self.x = x
        self.y = y
        self.img = img
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    
    def key_press(self):
        keys = pygame.key.get_pressed()
        self.img = imgs["01"]
        if (self.y + GRAVITY) <= (HIGHT - self.img.get_height()):
            self.move(0, GRAVITY)
        if keys[pygame.K_UP]:
            self.img = imgs["02"]
            if (self.y - JETPACK_POWER) >= 0:
                self.move(0, -JETPACK_POWER)
    
    def render(self):
        self.key_press()
        screen.blit(self.img, (self.x, self.y))


#Objects
class object:
    def __init__(self, img, ground_only = False, roof_only = False):
        self.img = img
        self.ground_only = ground_only
        self.roof_only = roof_only
    
    def generate(self):
        self.x = random.randint(WIDTH//2, WIDTH-(self.img.get_width()))
        if self.ground_only == False and (self.roof_only == False):
            self.y = random.randint(0, HIGHT-(self.img.get_height()))
        elif self.ground_only:
            self.y = HIGHT-self.img.get_height()
        elif self.roof_only:
            self.y = self.img.get_height()
    def render(self):
        self.x -= BG_SPEED
        screen.blit(self.img, (self.x, self.y))
        if (self.x < WIDTH//10):
            self.generate()
        

class write:
    def __init__(self, x = 10, y = 10, font = imgs["font"]):
        self.font = font
        self.x = x
        self.y = y
    
    def render(self, score):
        self.score = score
        text = self.font.render(f"Score: {self.score}", True, RED, None)
        screen.blit(text, (self.x, self.y))

#Menu
class menu_object:
    def __init__(self, img, x, y):
        self.img = img
        self.show = True
        self.x = x
        self.y = y
    def render(self):
        if self.show:
            screen.blit(self.img, (self.x, self.y))
    def clicked(self):
        self.show = False




#Background
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
        self.bgx -= BG_SPEED
        self.bgx2 -= BG_SPEED


#Menu init
menu_bg = menu_object(imgs["menu_bg"], 0, 0)
start_bar = imgs["start"]
start_bar_cen_x = start_bar.get_width()/2
start_bar_cen_y = start_bar.get_height()/2

start = menu_object(start_bar, (WIDTH/2 - start_bar_cen_x), (HIGHT/2 + start_bar_cen_y))
start_bar_pos = (start.x + start_bar_cen_x-20, start.y + start_bar_cen_y)

#BG init
bg1 = Moving_background(imgs["lvl2"])

#Char init
char1 = Character(imgs["01"], WIDTH//4, HIGHT-imgs["01"].get_height())

#Coins init
coins_dic = {}
for x in range(COINS):
    coins_dic[f"coin_{x}"] = object(imgs["coin"])
coins_v_list = list(coins_dic.values())
for i in range(len(coins_v_list)):
    coins_v_list[i].generate()


#Spikes init
spikes_dic = {}
for s in range(SPIKES):
    if s%2 == 0:
        spikes_dic[f"spike_{s}"] = object(imgs["spikes_ground"], True)
    else:
        spikes_dic[f"spike_{s}"] = object(imgs["spikes_roof"], False, True)
spikes_v_list = list(spikes_dic.values())
for k in range(len(spikes_v_list)):
    spikes_v_list[k].generate()
    
#Collision
Score = write(x=10, y=10)

running = True
while running:
    
    #Exit loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            running = False
        if (event.type == pygame.MOUSEBUTTONDOWN) and get_d(pygame.mouse.get_pos(), start_bar_pos) < 30:
            start.clicked()
    
    
    
    #Screen move
    menu_bg.render()
    start.render()
    
    
    
    if not (start.show):
        #Background rend
        bg1.bg_blit()
        #Character rend
        char1.render()
        #Coin rend
        for coin in range(len(coins_v_list)):
            if get_d((coins_v_list[coin].x, coins_v_list[coin].y), (char1.x, char1.y)) < 50:
                SCORE += 1
                coins_v_list[coin].generate()
            
            if (coins_v_list[k].x - coins_v_list[k-1].x) <= WIDTH//20:
                coins_v_list[k].generate()
            coins_v_list[coin].render()
        Score.render(SCORE)
            
        
        for spike in range(len(spikes_v_list)):
            if get_d((spikes_v_list[spike].x, spikes_v_list[spike].y), (char1.x, char1.y)) < 50:
                SCORE = 0
                #coins_v_list[coin].generate()
            
            if (spikes_v_list[k].x - spikes_v_list[k-1].x) <= WIDTH//20:
                spikes_v_list[k].generate()
            spikes_v_list[spike].render()
    
    pygame.display.update()
    clock.tick(FPS)
    
    #Music
    if not (pygame.mixer.music.get_busy()):
        load_music()




pygame.quit()