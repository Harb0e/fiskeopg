import pygame
from random import randint
from Vectoropg import * 
from flerefisk import Fisk
from fiskeflok import Flok


def main():
    screen = pygame.display.set_mode((800, 600))
    fisklst = []
    for _ in range(4):
        fisklst.append(Fisk(Vector(randint(0,800-240),randint(0,600-128)),Vector(2,2),"fisk.jpg",screen))
    pygame.init()
    flok = Flok(fisklst)
    clock = pygame.time.Clock()
    running = True
    while running:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
        flok.update(screen)
        clock.tick(60)  
    pygame.quit()
main()