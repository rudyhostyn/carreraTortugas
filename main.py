import turtle

class Circuito():
    Corredores =[]
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor("lightgray")
        
        for i in Range (4):
            new_turtle = turtle.Turtle()
            self.Corredores.append(new_turtle)
        
        
if __name__ == "__main__":
    circuito = Circuito(640, 480)