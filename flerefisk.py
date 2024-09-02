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

    def changeVeloho(self):
        self.__velocity = Vector(self.__velocity.getx() * -1, self.__velocity.gety())

    def changeVelolo(self):
        self.__velocity = Vector(self.__velocity.getx(), self.__velocity.gety() * -1)

    
    def bordercheck(self):
        if self.__position.getx() <= 0 or self.__position.getx() >= 800-255:
            self.changeVeloho()
 
        if self.__position.gety() <= 0 or self.__position.gety() >= 600-128:
            self.changeVelolo()
    
    

    
    