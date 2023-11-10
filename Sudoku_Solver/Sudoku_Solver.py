import math

def print_board (Board):
    size=len(Board)
    a=int(math.sqrt(size))
    for i in range(size):
        if i % a == 0 and i != 0:
            print("-------------------------------------")
        for j in range(len(Board[0])):
            if j % a == 0 and j != 0:
                print(" | ", end="")
            if j == (size-1):
                print(Board[i][j])
            else:
                print(Board[i][j],"",end="")


def find_empty(Board):
    for i in range (len(Board)):
        for j in range(len(Board[0])):
            if Board[i][j] == 0:
                return (i, j)
    return None

def valid(Board, num, pos):
    size=len(Board)
    a=int(math.sqrt(size))

    #check row
    for i in range(len(Board[0])):
        if Board[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(Board)):
        if Board[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // a
    box_y = pos[0] // a

    for i in range(box_y * a, box_y *a+a):
        for j in range (box_x*a, box_x*a+a):
            if Board[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(Board,list):
    find = find_empty(Board)
    if not find:
        return True
    else:
        row, col = find
        #print(row,col)

    for i in list:
        if valid(Board, i, (row, col)):
            Board[row][col] = i
            if solve(Board,list):
                return True
            else:
                Board[row][col] = 0
    return False

def soln(board,list):
    print_board(board)
    print("")
    print("******************************************")
    print("")
    solve(board,list)
    print_board(board)

