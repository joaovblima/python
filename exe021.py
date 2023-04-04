import pygame
pygame.init()
pygame.mixer.music.load("arquivo.mp3.mp3")
pygame.mixer_music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)