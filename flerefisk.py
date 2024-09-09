from Vectoropg import Vector
import pygame

class Fisk:
    def __init__(self, position, velocity,imglink) -> None:
        self.__img = pygame.image.load(imglink)
        self.__position = position
        self.__velocity = velocity

    def update(self,screen):
        screen.blit(self.__img, (self.__position.getx(), self.__position.gety()))
        self.move()
        self.bordercheck()

    def move(self):
        self.__position = self.__position + self.__velocity

    def changeVelova(self):
        self.__velocity = Vector(self.__velocity.getx() + (1 - (self.__position.getx() / self.d)), self.__velocity.gety())

    def changeVelolo(self):
        self.__velocity = Vector(self.__velocity.getx(), self.__velocity.gety() + (1 - (self.__position.gety() / self.d)))

    
    def bordercheck(self):
        self.d = 100
        if self.__position.getx() <= self.d or self.__position.getx() >= 800-255-100:
            self.changeVelova()
 
        if self.__position.gety() <= self.d or self.__position.gety() >= 600-128-100:
            self.changeVelolo()
    
    

    
    