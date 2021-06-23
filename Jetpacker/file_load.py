import os, pygame
WIDTH, HIGHT = 1000, 300

pygame.font.init()
#Background
imgs = {}
imgs["lvl2"] = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "lvl2.png")), (WIDTH, HIGHT))
imgs["lvl3"] = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "lvl3.png")), (WIDTH, HIGHT))


#Menu
imgs["menu_bg"] = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "menu.png")), (WIDTH, HIGHT))
imgs["start"] = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "start.png")), (WIDTH//10, HIGHT//10))

#Character
imgs["01"] = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "01.png")), (45, 64))
imgs["02"] = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "02.png")), (45, 64))
imgs["03"] = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "03.png")), (45, 64))
imgs["04"] = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "04.png")), (45, 64))

#Objects
imgs["coin"] = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "thecoin.png")), (20, 20))
imgs["fire"] = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "fire.png")), (30, 25))
imgs["spikes_roof"] = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "spike_on_roof.png")), (60, 25))
imgs["spikes_ground"] = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "spike_on_floor.png")), (60, 25))


#Font
imgs["font"] = pygame.font.Font(os.path.join("imgs", "FreeSansBold.ttf"), 20)


#Music
music = {}
# music["theme1"] = os.path.join("music", "theme1.mp3")
# music["theme2"] = os.path.join("music", "theme2.mp3")
first_song = 1
play_turn = first_song
def load_music():
    global first_song
    global play_turn
    if play_turn == 0:
        pygame.mixer.music.load(music["theme1"])
        play_turn += 1
    elif play_turn == 1:
        pygame.mixer.music.load(music["theme2"])
        play_turn = first_song
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(0)
