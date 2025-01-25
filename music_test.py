import pygame
import os

pygame.mixer.init()

if os.path.exists("music.mp3"):
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        print("playing")

    pygame.mixer.quit()
else:
    print("Error: music.mp3 not found")
