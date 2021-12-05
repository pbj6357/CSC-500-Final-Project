import turtle
import random
import math

def CreateScreen():
    """This function will be used to create the board on which the ladybug will walk"""
    BLOCK_SIZE = 60
    BORDER = 13
    STAMP_SIZE = 20  # Default value used to get pixel-level control of turtle size
    ROWS = 7
    COLUMNS = 7

    screen = turtle.Screen()
    WIDTH = COLUMNS * (BLOCK_SIZE + BORDER)
    HEIGHT = ROWS * (BLOCK_SIZE + BORDER)
    screen.setup(WIDTH, HEIGHT)
    
    screen.title("Random Walks Demo")
    screen.setworldcoordinates(0, screen.window_height(), screen.window_width(), 0)
    screen.bgcolor("black")
    screen.tracer(0)  # Pause animation to get instant drawing

    builder = turtle.Turtle(visible=False)
    builder.shape("square")
    builder.color("green")
    builder.shapesize(BLOCK_SIZE / STAMP_SIZE)
    builder.penup()


    for row_num in range(ROWS):
        for col_num in range(COLUMNS):
            builder.goto((BLOCK_SIZE // 2) + col_num * (BLOCK_SIZE + BORDER),
                         (BLOCK_SIZE // 2) + row_num * (BLOCK_SIZE + BORDER))
            builder.stamp()

    screen.tracer(1)  # Restore animation
    
def PickDirection(ladybug):
    """This function will utilize the current X and Y coordinates of the ladybug to determine what
    directions the ladybug can travel in. It will also randomly select a direction out of the available choices."""

    #TOP LEFT = (30,28)
    #TOP RIGHT = (468,28)
    #BOTTOM LEFT = (30,468)
    #BOTTOM RIGHT = (468,468)

    xCor = round(ladybug.xcor())
    yCor = round(ladybug.ycor())

    if xCor > 432 and xCor < 550 and yCor < 50 and yCor > -100:     #Top Right Corner
        return topright[random.randint(0,2)]
    elif xCor < 60 and xCor > -100 and yCor < 50 and yCor > -100:   #Top Left Corner
        return topleft[random.randint(0,2)]
    elif xCor > 432 and xCor < 550 and yCor > 430 and yCor < 550:   #Bottom Right Corner
        return bottomright[random.randint(0,2)]
    elif xCor < 60 and xCor > -100 and yCor > 430 and yCor < 550:   #Bottom Left Corner
        return bottomleft[random.randint(0,2)]
    elif xCor > 432 and xCor < 550:                                 #Right Wall
        return rightwall[random.randint(0,4)]
    elif xCor < 60 and xCor > -100:                                 #Left Wall
        return leftwall[random.randint(0,4)]
    elif yCor < 50 and yCor > -100:                                 #Top Wall
        return topwall[random.randint(0,4)]
    elif yCor > 430 and yCor < 550:                                 #Bottom Wall
        return bottomwall[random.randint(0,4)]
    elif xCor != 30 and xCor != 468 and yCor != 28 and yCor != 468: #Any direction
        return normaldirections[random.randint(0,7)]


def MoveBug(ladybug):
    """This function will use the direction chosen by the PickDirection function to move the ladybug"""

    move = PickDirection(ladybug)

    if move == 'east':
        ladybug.setheading(0)
        ladybug.forward(72)
    elif move == 'southeast':
        ladybug.setheading(45)
        ladybug.forward(math.sqrt(10368))
    elif move == 'south':
        ladybug.setheading(90)
        ladybug.forward(72)
    elif move == 'southwest':
        ladybug.setheading(135)
        ladybug.forward(math.sqrt(10368))
    elif move == 'west':
        ladybug.setheading(180)
        ladybug.forward(72)
    elif move == 'northwest':
        ladybug.setheading(225)
        ladybug.forward(math.sqrt(10368))
    elif move == 'north':
        ladybug.setheading(270)
        ladybug.forward(72)
    elif move == 'northeast':
        ladybug.setheading(315)
        ladybug.forward(math.sqrt(10368))

## MAIN
    
print('Welcome to the Ladybug Walk experiment!\n')
print('In this simulation, you will choose how many steps our ladybug friend will take,\nand we will see how far they will go!\n')

steps = int(input('Now, please enter an integer for as many steps as you would like the ladybug to take.\nPositive integers only, please! '))

CreateScreen()

#Create the Ladybug

ladybug = turtle.Turtle()
ladybug.hideturtle()
turtle.addshape('ladybug2.gif')
ladybug.shape('ladybug2.gif')
ladybug.penup()
ladybug.setposition(250,250)
ladybug.showturtle()
ladybug.speed('slowest')

#Move the bug
normaldirections = ['north','south','east','west','northeast','southeast','southwest','northwest']
rightwall = ['north','south','northwest','southwest','west']
leftwall = ['north','south','northeast','southeast','east']
topwall = ['south','west','east','southeast','southwest']
bottomwall = ['north','west','east','northeast','northwest']
topright = ['west','south','southwest']
topleft = ['east','south','southeast']
bottomright = ['west','north','northwest']
bottomleft = ['east','north','northeast']


current = 0
while current < steps:
    MoveBug(ladybug)
    current = current + 1

BX = 250
BY = 250
CX = round(ladybug.xcor())
CY = round(ladybug.ycor())
distance = math.sqrt(((CX-BX)**2)+((CY-BY)**2))
print("n/The ladybug's current location is:",str(round(ladybug.xcor()))+',',str(round(ladybug.ycor())))
print("n/The distance from the ladybug's start location to the current location is: ",str(format(distance,'.3f')))
