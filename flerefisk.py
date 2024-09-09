from Vectoropg import Vector
import pygame

class Fisk:
    def __init__(self, position, velocity,imglink) -> None:
        self.__img = pygame.image.load(imglink)
        self.__position = position
        self.__velocity = velocity


    def getvelo(self):
        return self.__velocity

    def update(self,screen):
        screen.blit(self.__img, (self.__position.getx(), self.__position.gety()))
        self.move()
        self.bordercheck()

    def move(self):
        self.__position = self.__position + self.__velocity

    def changeVelova(self):
        if self.__position.getx() <= self.d:
            self.__velocity = Vector(self.__velocity.getx() + (1 - (self.__position.getx() / self.d)), self.__velocity.gety())
        elif self.__position.getx() >= 800-244-self.d:
            self.__velocity = Vector(self.__velocity.getx() + (1 - ((self.__position.getx() -350) / self.d)), self.__velocity.gety())

    def changeVelolo(self):
        if self.__position.gety() <= self.d:
            self.__velocity = Vector(self.__velocity.getx(), self.__velocity.gety() + (1 - (self.__position.gety() / self.d)))
        elif self.__position.gety() >= 600-124-self.d:
            self.__velocity = Vector(self.__velocity.getx(), self.__velocity.gety() + (1 - ((self.__position.gety()-250) / self.d)))

    
    def bordercheck(self):
        self.d = 100
        self.changevelova()
        self.changeVelolo()
    

  

    
    

    
    