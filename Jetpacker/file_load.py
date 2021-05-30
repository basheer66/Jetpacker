import os, pygame
WIDTH, HIGHT = 1000, 300

#Images
imgs = {}
imgs["lvl2"] = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "lvl2.png")), (WIDTH, HIGHT))
imgs["lvl3"] = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "lvl3.png")), (WIDTH, HIGHT))



#Music
music = {}
music["theme1"] = os.path.join("music", "theme1.mp3")
music["theme2"] = os.path.join("music", "theme2.mp3")
first_song = 0
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
