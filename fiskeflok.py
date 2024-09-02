from flerefisk import Fisk
import pygame


class Flok:
    def __init__(self,fiskearr) -> None:
        self.__fiskarr = fiskearr
        self.__screen = pygame.display.set_mode((800, 600))
    
    def update(self):
        self.__screen.fill((0, 128, 255))
        for fisk in self.__fiskarr:
            fisk.update(self.__screen)
        pygame.display.flip()
