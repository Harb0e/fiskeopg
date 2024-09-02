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
        return sqrt(self.getx()**2 + self.gety **2)
    
    def __add__(self, korr2): 
        return Vector(self.__x + korr2.__x ,self.__y + korr2.__y) 
    
    
    def __sub__(self,korr2):
        return Vector(self.__x - korr2.__x ,self.__y - korr2.__y )
    
    
    def __mul__(self,korr2):
        return Vector(self.__x * korr2.__x,self.__y * korr2.__y)
    
    def dotPro(self,korr2):
        return self.__x * korr2.__x + self.__y * korr2.__y
    
    def __truediv__(self,korr2):
        pass



    def __str__(self) -> str:
        return 'x: %d y: %d' % (self.__x,self.__y)
    

