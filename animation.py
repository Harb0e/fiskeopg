import pygame
from random import randint
from Vectoropg import * 
from flerefisk import Fisk
from fiskeflok import Flok


def main():
    fisklst = []
    for _ in range(2):
        fisklst.append(Fisk(Vector(randint(0,800-255),randint(0,600-128)),Vector(2,2),"fisk.jpg"))
    pygame.init()
    flok = Flok(fisklst)
    clock = pygame.time.Clock()
    running = True
    while running:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
        flok.update()
        clock.tick(60)  
    pygame.quit()
main()