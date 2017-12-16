
 #Spring 2015 CS1411
#Gomoku Final Project
#by Wei-Ping, Lee

'''
Data Model 
'''
'''
A *State* is a pair with list of intersection. State G represent the current board state.
For exampe G=([(270,-270)],[(0,0),(0,30)]).

An *intersection* is a pair of interger, where the intersection located.
For example (-270,270) is the top left coner.

A *player* is either 'black' or 'white'.
A *mode* is either 'black', 'white' or 'gameover'. 'black' indicate now is player 'black''s turn.
'white' indicate now is player 'white''s turn. 'gameover' indicate either five in row or game tie.

A *interList* is a list of all the intersection on the game board.

A *finishMsg* is a string to show the finish message of the game result.

A *restartinfo* is a string to show the information of restart the game when the game is over. 

A *state* G, *interList*, *finishMsg* and *restartinfo* are defined to be global,
so every function can access them after *init* is called.

The *FiveRow* is true if player p has five in a row either vertically, horizontally or diagonally.

The *horizontalmatch* is true if *FiveRow* is in horizontal line.

The *verticalmatch* is true if *FiveRow* is in vertical line.

The *rightdiagonallymatch* is true if *FiveRow* is in right diagonally line.

The *leftdiagonallymatch* is true if *FiveRow* is in left diagonally line. 

A *GameOver* is true if a player has won or the board is full.

A *BoardFull* is true if all intersections on the board are occupied.

A *clicked* is true if the user clicked on intersection I.

An *IntersectionCheck* is the intersection that the user clicked on. (-1, -1) if
point clicked on is not an intersection.

A *CurrentBlackStone* returns discs for every stone that the 'black' player has.

A *CurrentWhiteStone* returns discs for every stone that the 'white' player has.

A *click* is true if the left mouse button is clicked.

A *RestartButton* is the image of the restart button.

A *RestartButtonClicked* is true if the left mouse button click the restart button.

A *RestartMessage* is the text image to show the location of the restart button.

The *green*, *black*, *white*, *orange*, *red*, *blue*, and *purple* are the color that present
on the screen. 
'''


from EaselLib import *
green = (46,231,77)
black = (0,0,0)
white = (255, 255, 255)
orange = (250, 100, 0)
red=(197,32,32)
blue = (32,118,197)
purple=(162,24,210)

# G, interList and finishMsg are defined to be global, so every function can
# access them after init is called.
def init():
    global G
    global interList
    global finishMsg
    global restartinfo
    global finishMsg2

    G = ([], [])
    interList = []
    finishMsg = ''
    restartinfo = ''
    finishMsg2 = ' '

    # Create a table of all the intersections
    starty = 270
    for i in range(19):
        x = []
        subx = -270
        for j in range(19):
            x.append((subx, starty))
            subx = subx + 30
        interList.append(x)
        starty -= 30

# Window is 640 x 640 
# Actual board is540 x 540 and each line is separated by 30
# The origin is at the center of the board

# Each box is 30 wide -> returns a list of the vertical lines
def VerticalLines():
    L = []

    x = -270
    for i in range(19):
        L.append(seg((x, 270), (x, -270), black))
        x += 30
    return L

# Each box is 30 wide -> Returns a list of the horizontal lines
def HorizontalLines():
    L = []

    y = 270
    for i in range(19):
        L.append(seg((-270, y), (270, y), black))
        y -= 30
    return L

# Returns a list of 2 triangles used to simulate an orange square
def OrangeFill():
    L = []
    L.append(ftri((-270, 270), (-270, -270), (270, -270), orange))
    L.append(ftri((-270, 270), (270, 270), (270, -270), orange))

    return L

# FiveRow is true if player p has five in a row either vertically, horizontally
# or diagonally
def FiveRow(p):
    # Horizontal Row
    for i in range(15):
        for j in range(19):
            if horizontalmatch(p,i,j):
                return True

    # Vertical Row    
    for i in range(19):
        for j in range(15):
            if verticalmatch(p,i,j):
                return True

    # Diagonal with negative slope
    for i in range(15):
        for j in range(15):
            if rightdiagonallymatch(p,i,j):
                return True

    # Diagonal with positive slope 
    for i in range(4, 19):
        for j in range(15):
            if leftdiagonallymatch(p,i,j):
                return True
             
    return False


def horizontalmatch(p,i,j):
    index = 1 if p == 'white' else 0
    return interList[i][j] in G[index] and interList[i+1][j] in G[index] and interList[i+2][j] in G[index] and interList[i+3][j]in G[index] and interList[i+4][j] in G[index]


def verticalmatch(p,i,j):
    index = 1 if p == 'white' else 0
    return interList[i][j] in G[index] and interList[i][j+1] in G[index] and interList[i][j+2] in G[index] and interList[i][j+3]in G[index] and interList[i][j+4] in G[index]


def rightdiagonallymatch(p,i,j):
    index = 1 if p == 'white' else 0
    return interList[i][j] in G[index] and interList[i+1][j+1] in G[index] and interList[i+2][j+2] in G[index] and interList[i+3][j+3]in G[index] and interList[i+4][j+4] in G[index]


def leftdiagonallymatch(p,i,j):
    index = 1 if p == 'white' else 0
    return interList[i][j] in G[index] and interList[i-1][j+1] in G[index] and interList[i-2][j+2] in G[index] and interList[i-3][j+3]in G[index] and interList[i-4][j+4] in G[index]      


# GameOver is true if a player has won or the board is full
# Also sets finishMsg to the appropriate text
def GameOver():
    global finishMsg
    global restartinfo
    global finishMsg2
    if FiveRow('black') and RestartButtonClicked():
        finishMsg = ' '
        restartinfo = ' '
        finishMsg2 = ' '
        return True
    elif FiveRow('white') and RestartButtonClicked():
        finishMsg = ' '
        restartinfo = ' '
        finishMsg2 = ' '
        return True
    elif BoardFull() and RestartButtonClicked():
        finsihMsg = ' '
        restartinfo = ' '
        finishMsg2 = ' '
        return True

    elif FiveRow('black'):
        finishMsg = 'Game Over!!!'
        finishMsg2 = 'Player Black Win!!!'
        restartinfo='*click the restart button to restart the match*'
        return True
    elif FiveRow('white'):
        finishMsg = 'Game Over!!!'
        finishMsg2 = ' Player White Win!!!'
        restartinfo='*click the restart button to restart the match*'
        return True
    elif BoardFull():
        finishMsg = 'The game ended in a tie!!!'
        restartinfo='*click the restart button to restart the match*'
        return True
    
    else:
        return False

# BoardFull is true if all intersections on the board are occupied
def BoardFull():
    return len(G[0]+ G[1]) == 19**2

# Returns a list of the various components that make up the board
def gameBoard():    
    return OrangeFill() + VerticalLines() + HorizontalLines()

# windowDimensions() -> (int, int)
# Represents the dimensions of the window
def windowDimensions():
    return (640, 640)

# returns discs for every stone that the black player has
def CurrentBlackStone():
    global G
    L=[]
    for i in G[0] : 
         L.append(disc((i[0],i[1]),13,black))
    return  L                

def CurrentWhiteStone():
    global G
    L=[]
    for e in G[1] : 
       L.append(disc((e[0],e[1]),13,white))
    return L

def stones():
    return CurrentBlackStone()+CurrentWhiteStone()

def heading():
    msg='Gomoku'
    return [txt(msg,(0,300),30,blue)]

def addstone(I):
    global G
    if mode(G) == 'black':
        G[0].append(I)
    else:
        G[1].append(I)

# clicked(I) is true if the user clicked on intersection I
# += 7 to allow for user error (it is difficult to click exactly on
# the intersection
def clicked(I):
    return (mouseDown and not oldMouseDown) and ((I[0] - 7) <= mouseX <= (I[0] + 7))\
and ((I[1] - 7) <= mouseY <= (I[1] + 7))


def mode(G):
    if GameOver():
        return 'gameover'
    x = len(G[0] + G[1])
    if x % 2 == 0:
        return 'black'
    else:
        return 'white'

# IntersectionCheck is the intersection that the user clicked on. (-1, -1) if
# point clicked on is not an intersection
def IntersectionCheck():
    global interList
    for i in range(19):
        for j in range(19):
            if clicked(interList[i][j]):
                return interList[i][j]

    return (-1,-1)

def click():
    return mouseDown and not oldMouseDown

def RestartButtonClicked():
    return click() and 275<mouseX<305 and 285<mouseY<315

def update():
    global G
    if GameOver() and RestartButtonClicked():
        G=([],[])
        return G
    if GameOver():
        return
    if RestartButtonClicked():
        G=([],[])
        return G
    
    # Determine where the user clicked
    C = IntersectionCheck()
    
    # If not a valid cell, do not update anything
    if C == (-1,-1):
        return
    
    # If intersection has been previously clicked, do not update anything
    elif C in G[0] or C in G[1]:
        return
    
    # Add the appropriate stone to the board
    else:
        addstone(C)

def RestartButton():
    return  [disc((290,300),15,red)]

def RestartMessage():
    msg='Restart Button:'
    return [txt(msg,(195,300),30,purple)]

def display():
    global finishMsg
    global restartinfo
    finishText = [txt(finishMsg,(0,0),55,green)]
    finishText2 = [txt(finishMsg2,(0,-60),55,green)]
    RestartText =[txt(restartinfo,(170,-312),20,black)]
    return heading() + gameBoard() + stones() + finishText + RestartButton() + RestartMessage()\
           +RestartText + finishText2
