from Vectoropg import Vector
import pygame

class Fisk:
    def __init__(self, position, velocity,imglink,screen,sight=100) -> None:
        self.__sight = sight
        self.__scale = 50
        self.__img = pygame.transform.scale(pygame.image.load(imglink), (self.__scale,self.__scale))
        self.__position = position
        self.__velocity = velocity
        self.__screen = screen


    def update(self):
        self.draw()
        self.move()
        self.bordercheck()
    
    def draw(self):
        self.__screen.blit(self.__img, (self.__position.getx(), self.__position.gety()))

    def move(self):
        self.__position = self.__position + self.__velocity

    def changeVelova(self):
        if self.__position.getx() <= self.d+self.__sight:
            self.__velocity = Vector(self.__velocity.getx() + (1 - ((self.__position.getx()) / (self.d+self.__sight))), self.__velocity.gety())
        elif self.__position.getx() >= self.w-self.d-self.__sight:
            self.__velocity = Vector(self.__velocity.getx() - (1 - ((self.w - self.__position.getx()) / (self.d+self.__sight))), self.__velocity.gety())

    def changeVelolo(self):
        if self.__position.gety() <= self.d+self.__sight:
            self.__velocity = Vector(self.__velocity.getx(), self.__velocity.gety() + (1 - ((self.__position.gety()) / (self.d+self.__sight))))
        elif self.__position.gety() >= self.h-self.d-self.__sight:
            self.__velocity = Vector(self.__velocity.getx(), self.__velocity.gety() - (1 - (self.h - self.__position.gety()) / (self.d+self.__sight)))

    
    def bordercheck(self):
        self.w, self.h = pygame.display.get_surface().get_size()
        self.d = 100
        self.changeVelova()
        self.changeVelolo()
    

  

    
    

    
    