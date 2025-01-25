import pygame
import os

pygame.mixer.init()
path = os.getcwd() + "/groot_sounds"
sound_files = ["I_am_groot_1.mp3", 
               "I_am_groot_2.mp3", 
               "I_am_groot_3.mp3", 
               "I_am_groot_4.mp3"]
pygame.mixer.music.set_volume(1)

for sound_file in sound_files:
    pygame.mixer.music.load(path + sound_file)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
    	continue
        
# if os.path.exists("test_music.wav"):
#     pygame.mixer.music.load("test_music.wav")
#     pygame.mixer.music.play()

#     while pygame.mixer.music.get_busy():
#         print("playing")

#     pygame.mixer.quit()
# else:
#     print("Error: test_music.wav not found")

