from numpy import sqrt

class Vector:
    def __init__(self,x,y) -> None:
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    
    
    def getLength(self):
        return sqrt(self.__x**2 + self.__y**2)
    
    def __add__(self, korr2): 
        return Vector(self.__x + korr2.__x ,self.__y + korr2.__y) 
    
    
    def __sub__(self,korr2):
        return Vector(self.__x - korr2.getx() ,self.__y - korr2.gety() )
    
    
    def __mul__(self,num):
        return Vector(self.__x * num , self.__y * num)
    
    def dotPro(self,korr2):
        return self.__x * korr2.getx() + self.__y * korr2.gety()
    
    def __truediv__(self,number):
        return Vector(self.__x/number,self.__y/number)

    def getDistance(self,vector):
        distance_vector = self- vector
        return distance_vector.getLength()

    def __str__(self) -> str:
        return 'x: %d y: %d' % (self.__x,self.__y)
    

