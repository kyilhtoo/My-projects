import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

displaysurf = pygame.display.set_mode((600,400))
pygame.display.set_caption("MY game")

white = (255,255,255)
flagImg = pygame.image.load(r'C:\Users\Kyi Htoo\Desktop\Python\21 flag\flag.png')
flagImg_small = pygame.transform.scale(flagImg, (60,60))
backgroundImg = pygame.image.load(r'C:\Users\Kyi Htoo\Desktop\Python\21 flag\background.jpg')

while True:
    displaysurf.blit(backgroundImg, (0,0))    
    displaysurf.blit(flagImg_small, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

