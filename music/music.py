import pygame

class Music():
    def __init__(self, music_link):
        self.music = music_link
    
    def start_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play()
    
    def end_music(self):
        pygame.quit()

    def is_music_playing(self):
        return pygame.mixer.music.get_busy()