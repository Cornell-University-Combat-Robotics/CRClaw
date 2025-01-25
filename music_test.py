import os

import pygame

pygame.mixer.init()

if os.path.exists("test_music.wav"):
    pygame.mixer.music.load("test_music.wav")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        print("playing")

    pygame.mixer.quit()
else:
    print("Error: test_music.wav not found")
