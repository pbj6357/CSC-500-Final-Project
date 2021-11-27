def PickDirection(ladybug):
    """This function will utilize the current X and Y coordinates of the ladybug to determine what
    directions the ladybug can travel in. It will also randomly select a direction out of the available choices."""

    xCor = round(ladybug.xcor())
    yCor = round(ladybug.ycor())

    if xCor != 300 and xCor != -300 and yCor != 300 and yCor != -300:
        return normaldirections[random.randint(0,7)]
    elif xCor == 300 and yCor == 300:
        return topright[random.randint(0,2)]
    elif xCor == -300 and yCor == 300:
        return topleft[random.randint(0,2)]
    elif xCor == 300 and yCor == -300:
        return bottomright[random.randint(0,2)]
    elif xCor == -300 and yCor == -300:
        return bottomleft[random.randint(0,2)]
    elif xCor == 300:
        return rightwall[random.randint(0,4)]
    elif xCor == -300:
        return leftwall[random.randint(0,4)]
    elif yCor == 300:
        return topwall[random.randint(0,4)]
    elif yCor == -300:
        return bottomwall[random.randint(0,4)]

def MoveBug(ladybug):
    """This function will use the direction chosen by the PickDirection function to move the ladybug"""

    move = PickDirection(ladybug)

    if move == 'east':
        ladybug.setheading(0)
        ladybug.forward(100)
    elif move == 'southeast':
        ladybug.setheading(45)
        ladybug.forward(math.sqrt(20000))
    elif move == 'south':
        ladybug.setheading(90)
        ladybug.forward(100)
    elif move == 'southwest':
        ladybug.setheading(135)
        ladybug.forward(math.sqrt(20000))
    elif move == 'west':
        ladybug.setheading(180)
        ladybug.forward(100)
    elif move == 'northwest':
        ladybug.setheading(225)
        ladybug.forward(math.sqrt(20000))
    elif move == 'north':
        ladybug.setheading(270)
        ladybug.forward(100)
    elif move == 'northeast':
        ladybug.setheading(315)
        ladybug.forward(math.sqrt(20000))

# MAIN
    
print('Welcome to the "Drunken Bug" ladybug experiment!\n')
print('In this simulation, you will choose how many steps our ladybug friend will take,\nand we will see how far they will go!\n')

steps = int(input('Now, please enter an integer for as many steps as you would like the ladybug to take.\nPositive integers only, please! '))

#Create the board
#Create the bug

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
while current <= steps:
    MoveBug(ladybug)
