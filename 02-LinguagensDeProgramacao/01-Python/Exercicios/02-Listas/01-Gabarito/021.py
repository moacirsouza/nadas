print('[-- Faça um programa em Python que abra e reproduza o Áudio de um arquivo MP3. --]\n')
musica = '/home/moacir/Downloads/essaPassou.mp3'

# Método 1, usando uma biblioteca externa: playsound
# Para instalar essa biblioteca em seu ambiente, execute:
# $ pip install playsound
""" from playsound import playsound
print('Para suspender a reprodução, pressione CTRL+Z')
playsound(musica) """

# Método 2, usando uma biblioteca externa: pygame
# Para instalar essa biblioteca em seu ambiente, execute:
# $ pip install pygame
""" import pygame
pygame.init()
pygame.mixer_music.load(musica)
pygame.mixer_music.play(-1) """

# Método 3, usando um reprodutor instalado no S.O.
# através de uma biblioteca interna (builtin): os
""" import os
print('Usando o "mplayer" para reproduzir o áudio.')
print('Os comandos tradicionais do programa funcionam aqui.\nPressione "q" para suspender a reprodução')
os.system('mplayer ' + musica) """
