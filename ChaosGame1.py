import turtle
import random

while 1:
    # Screen
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.setup(width = 1.0, height = 1.0)
    wn.tracer(0)

    # Variables
    colors = ["white", "green", "red", "purple", "yellow", "blue", "brown", "orange"]
    # Je doit créer 3 points random
    hauteur = 300
    largeur = 500

    '''
    xA = random.randint(-largeur, largeur)
    yA = random.randint(-hauteur, hauteur)

    xB = random.randint(-largeur, largeur)
    yB = random.randint(-hauteur, hauteur)

    xC = random.randint(-largeur, largeur)
    yC = random.randint(-hauteur, hauteur)

    ''' 
    xA = 0
    yA = hauteur

    xB = -largeur
    yB = -hauteur

    xC = largeur
    yC = -hauteur
    


    x = random.randint(-largeur, largeur)
    y = random.randint(-hauteur,hauteur)

    # Stylo

    stylo = turtle.Turtle()
    stylo.speed(0)
    stylo.ht()
    stylo.pu()
    stylo.color("purple")

    # Création des Trois points

    stylo.goto(xA, yA)
    stylo.dot(10)
    stylo.goto(xB, yB)
    stylo.dot(10)
    stylo.goto(xC, yC)
    stylo.dot(10)

    # Main loop
    stylo.color("black")
    #while 1:



    for i in range(2000):
        wn.update()
    
        randomNumber = random.randint(0,2)
        #randomColor = random.choice(colors)
        #stylo.color(randomColor)
        if randomNumber == 0:
            x = x/2 + xA/2
            y = y/2 + yA/2
            stylo.goto(x, y)
            stylo.dot(2)
            stylo.color("cyan")
        elif randomNumber == 1:
            x = x/2 + xB/2
            y = y/2 + yB/2
            stylo.goto(x, y)
            stylo.dot(2)
            stylo.color("yellow")
        if randomNumber == 2:
            x = x/2 + xC/2
            y = y/2 + yC/2
            stylo.goto(x, y)
            stylo.dot(2)
            stylo.color("red")
    wn.clearscreen()


wn.mainloop()