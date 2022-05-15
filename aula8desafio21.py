import pygame  # Precisou instalar o módulo externo pygame
pygame.init()
pygame.mixer.music.load('aula8desafio21.mp3')
pygame.mixer.music.play()
input()  # Alteração necessária devido à atualização do pygame
pygame.event.wait()
