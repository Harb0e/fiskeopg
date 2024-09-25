from flerefisk import Fisk
import pygame


class Flok:
    def __init__(self,fiskearr) -> None:
        self.__fiskarr = fiskearr
        self.__antal = len(fiskearr)
    
    def update(self,screen):
        screen.fill((0, 128, 255))
        for fisk in self.__fiskarr:
            fisk.update(self)
        pygame.display.flip()

    def getFlok(self):
        return self.__fiskarr
    
    