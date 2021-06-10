import numpy as np
import sys
from termcolor import colored, cprint
board=[[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
#ablove will create black board
def printBoard(): #this will print updated print each time when called
    cprint ("1   2   3   4   5   6   7") #this print index for column above the board
    for i in board:
        for j in i:
            if j == "X":
                cprint(j,"red",end="   ")        #print X in red colour
            if j == "O":
                cprint(j,"green",end="   ")      #print O in green colour
            if j == " ":
                cprint(" ", "green","on_red",end="   ")  # this will print blank value in red background
        print("")
        print ("-------------------------")



def ConnectCheck(): # when called it will check for four Connect
    count = 0
    for j in board:
        for k in range(0,len(j)):
            bv=j[k]                                       #it will cheak fro horizontal connect
            if k>len(j)-4:
                break
            if j[k]==j[k+1]==j[k+2]==j[k+3]!=" ":
                return bv
        count+=1
    for j in range(0,len(board[0])):

        for k in range(0,len(board)):
            bv=board[k][j]
            if k>len(board)-4:                           #it will cheak for vertical  connect
                break
            if board[k][j]==board[k+1][j]==board[k+2][j]==board[k+3][j]!=" ":
                return bv
    matrix=np.array(board)
    diags = [matrix[::-1, :].diagonal(i) for i in range(-5, 7)]
    diags.extend(matrix.diagonal(i) for i in range(6, -6, -1))          #this will collect all possible digonal list in list
    samp = [n.tolist() for n in diags]

    for sa in samp:
        if len(sa)<4:
            continue
        for k in range(0,len(sa)):
            bv=sa[k]
            if k>len(sa)-4:                      #it will check for diagonal check
                break
            if sa[k]==sa[k+1]==sa[k+2]==sa[k+3]!=" ":
                return bv

    return False

printBoard()

player="X"
while(True): #this main infinite loop and will not stop until winner is found
    playername="Player_One" if player=="X" else "Player_Two"
    try:
        move=int(input(playername+" Move(please enter column_index)\n"))
    except:
        printBoard()
        print("Please give input from 1 to 7")
        continue
    move=move-1


    if move>len(board[0])-1:
        printBoard()
        print("Please give input from 1 to 7")
        continue

    if board[0][move]!=" ":
        printBoard()
        print("this column is full")
        continue

    for i, e in reversed(list(enumerate(board))):
        if e[move] == " ":                         #this for loop will enter given value
            board[i][move]=player
            break

    printBoard()
    cc=ConnectCheck()
    if cc!=False:
        if cc=="X":
            print("Player_One Is Winner")
            break
        elif cc=="O":
            print("Player_Two Is Winner")
            break


    if player=="X":
        player="O"                #this will switch betwwen palyer
    else:
        player="X"
