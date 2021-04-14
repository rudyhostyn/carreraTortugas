import turtle
import random

class Circuito():
    Corredores =[]
    TurtleColor = ("red","blue","green","purple")
    __posStartY = (-60, -20, 20, 60)
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor("lightblue")
        self.__startline = -width/2+20
        self.__finishline = width/2-20
        
        self.__createrunners()
        
        
    def __createrunners(self):
        for i in range (4):
            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.shape("turtle")
            new_turtle.color(self.TurtleColor[i])
            new_turtle.setpos(self.__startline, self.__posStartY[i])
            
            self.Corredores.append(new_turtle)
    
    def competir(self):
        avance = 0
        while avance < self.__finishline:
            for i in range(4):
                dado = random.randint(1,6)
                self.Corredores[i].fd(dado)
                '''vale self.Corredores y circuito.Corredores. Este ultimo es el que funciona cuando la funcion esta fuera de la Class'''
                if self.Corredores[i].xcor() > avance:
                    avance = self.Corredores[i].xcor()
        
        CoordGanador = 0
        ganador = 0
        for i in range(4):
            if circuito.Corredores[i].xcor() > CoordGanador:
                CoordGanador = circuito.Corredores[i].xcor()
                ganador = i
        print("La Tortuga ganadora ha sido la tortuga {}.\nEnhorabuena ".format(circuito.Corredores[ganador].color()[0]))
         
        
if __name__ == "__main__":
    circuito = Circuito(600, 300)
    circuito.competir()


