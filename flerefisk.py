from Vectoropg import Vector
import numpy as np
import pygame

class Fisk:
    def __init__(self, position, velocity,imglink,screen,sight=300) -> None:
        self.d = sight
        self.__scale = 50
        self.__img = pygame.transform.scale(pygame.image.load(imglink), (self.__scale,self.__scale))
        self.__position = position
        self.__velocity = velocity
        self.__screen = screen


    def update(self,flok):
        seperation_change = self.seperation(flok,200,0.5)
        alignment_change = self.alignment(flok,250,0.3)
        cohesion_change = self.cohesion(flok,0.2)
        

        self.__velocity += seperation_change + alignment_change + cohesion_change

        self.draw()
        self.move()
        self.bordercheck()
        
    
    def draw(self):
        self.__screen.blit(self.__img, (self.__position.getx(), self.__position.gety()))

    def move(self): 
        self.__position = self.__position + self.__velocity.limit()

    def changeVelova(self):
        if self.__position.getx() <= self.d:
            self.__velocity = Vector(self.__velocity.getx() + (1 - self.__position.getx() / self.d), self.__velocity.gety())
        elif self.__position.getx() >= self.w-self.d:
            self.__velocity = Vector(self.__velocity.getx() - (1 - ((self.w - self.__position.getx()) / self.d)), self.__velocity.gety())

    def changeVelolo(self):
        if self.__position.gety() <= self.d:
            self.__velocity = Vector(self.__velocity.getx(), self.__velocity.gety() + (1 - self.__position.gety() / self.d))
        elif self.__position.gety() >= self.h-self.d:
            self.__velocity = Vector(self.__velocity.getx(), self.__velocity.gety() - (1 - (self.h - self.__position.gety()) / self.d))

    def changeVelovaAlternative(self):
        if self.__position.getx() <= self.d:
            self.__velocity = Vector(self.__velocity.getx() + (1 - (self.__position.getx() / self.d)**2), self.__velocity.gety())
        elif self.__position.getx() >= self.w-self.d:
            self.__velocity = Vector(self.__velocity.getx() - (1 - ((self.w - self.__position.getx()) / self.d)**2), self.__velocity.gety())

    def changeVeloloAlternative(self):
        if self.__position.gety() <= self.d:
            self.__velocity = Vector(self.__velocity.getx(), self.__velocity.gety() + (1 - (self.__position.gety() / self.d))**2)
        elif self.__position.gety() >= self.h-self.d:
            self.__velocity = Vector(self.__velocity.getx(), self.__velocity.gety() - (1 - ((self.h - self.__position.gety()) / self.d)**2))
    
    def bordercheck(self):
        self.w, self.h = pygame.display.get_surface().get_size()
        self.changeVelova()
        self.changeVelolo()
    
    
    def seperation(self,flok,tooClose,separation_factor):
        separation_vector = Vector(0,0)
        for fisk in flok.getFlok():
            if fisk != self:
                afstand = self.__position.getDistance(fisk.get_pos())
                if afstand <= tooClose:
                    dif = self.__position - fisk.get_pos()
                    separation_vector = Vector(dif.getx()/afstand,dif.gety()/afstand)
        return(separation_vector * separation_factor)
    
    def alignment(self, flok, visible_distance=50, alignment_factor=1.2):
        alignment_vector = Vector(0, 0)
        count = 0
        for fish in flok.getFlok():
            if fish != self:
                distance = self.__position.getDistance(fish.get_pos())
                if distance < visible_distance:
                    alignment_vector += fish.get_velo()
                    count += 1
        if count > 0:
            alignment_vector /= count
            alignment_vector = (alignment_vector - self.__velocity)
            return (alignment_vector.norm() * alignment_factor)
        return alignment_vector

    def cohesion(self,flok,cohesion_factor):
        cohesion_vector = Vector(0,0)
        count = 0
        for fisk in flok.getFlok():
            if fisk != self:
                cohesion_vector += fisk.get_pos()
                count += 1

        if count > 0:
            cohesion_vector = (cohesion_vector / count) - self.__position
            return (cohesion_vector.norm()) * cohesion_factor



                    
                    

    def get_pos(self):
        return self.__position
    def get_velo(self):
        return self.__velocity

                
        
    

  

    
    

    
    