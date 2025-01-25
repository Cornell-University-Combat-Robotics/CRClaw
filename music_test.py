import pygame
import os

pygame.mixer.init()

if os.path.exists("music.wav"):
    pygame.mixer.music.load("music.wav")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        print("playing")

    pygame.mixer.quit()
else:
    print("Error: music.wav not found")
