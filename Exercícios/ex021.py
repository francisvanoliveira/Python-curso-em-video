#Faça um programa em pyton que abra e respoduza o áudio de arquivo em mp3.

import pygame
pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
