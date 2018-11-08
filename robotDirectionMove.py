#
# Complete the 'roverMove' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER matrixSize
#  2. STRING_ARRAY cmds
#

def roverMove(matrixSize, cmds):
    # Write your code here
    
    
    row= 0
    col= 0
    pos = [0,0]
    
    data = 0
    array = [[0]*matrixSize for index in range(matrixSize)]
    while(row < matrixSize):
        if(col < matrixSize):
            array[row][col] = (row * matrixSize) + col
            col += 1
        else:
            row += 1
            col = 0
    
#     
    
    for comd in cmds:
        if comd == "RIGHT":
            currentPos = right(array, pos)
        if comd == "LEFT":
            currentPos = left(array, pos)
        if comd == "UP":
            currentPos = up(array, pos)
        if comd == "DOWN":
            currentPos = down(array, pos)
        pos = currentPos
        print(pos)
        
               
#     value = array[(pos[0])][(pos[1])]
#     return value
    

def right(array, pos):
    if (pos[1] >= (len(array)-1)):
        print("in right ", pos, " ", pos[1], " no movement")
        return pos
    else:
        print("in right ", pos, " ", pos[1], " before movement")
        y = pos[1 ]+ 1
        pos[1] = y
        print("in right ", pos, " ", pos[1], "move one step")
        return pos
    
def left(array, pos):
    if (pos[1] <= 0):
        return pos
    else:
        pos[1] = pos[1] - 1
        return pos
    
def up(array, pos):
    if (pos[0] <= 0):
        return pos
    else:
        pos[0] = pos[0] - 1
        return pos
    
def down(array, pos):
    if (pos[0] >= (len(array)-1)):
        return pos
    else:
        pos[0] = pos[0] + 1
        return pos
    