#TurtleGraphics.py
#Name: Andrew Conyers Miller
#Date:11/19/24
#Assignment:TurtleGraphics

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)
        
def fillCorner(alice, corner):
    #draw big square
    drawSquare(alice, 100)
    
    if corner == 1:
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
        alice.stamp()
    elif corner == 3:
        alice.penup()
        alice.forward(50)
        alice.right(90)
        alice.forward(50)
        alice.pendown()
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()


def squaresInSquares(myTurtle, numSquares):
    size = 100 # Starting size of the largest square 
    
    sides_list = [4, 5, 6]
    

    for i in range(numSquares):
        sides = sides_list[i]
        
        drawPolygon(myTurtle, sides)
        
        myTurtle.penup()
        myTurtle.forward(10)
        myTurtle.right(90)
        myTurtle.forward(10)
        myTurtle.left(90)
        myTurtle.pendown()
        
        size -= 20

def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    #drawPolygon(myTurtle, 3)

   #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
  # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

  # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    
    squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
