import turtle

class Circuito():
    Corredores =[]
    TurtleColor = ("red","blue","green","purple")
    __posStartY = (-60, -20, 20, 60)
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor("lightgray")
        self.__startline = -width/2+20
        self.__finishtline = width/2-20
        
        for i in range (4):
            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.shape("turtle")
            new_turtle.color(self.TurtleColor[i])
            new_turtle.setpos(self.__startline, self.__posStartY[i])
            
            self.Corredores.append(new_turtle)
        
        
if __name__ == "__main__":
    circuito = Circuito(640, 480)