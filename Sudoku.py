import time

board = []
print("Please enter a Sudoku board and click Enter:")
for i in range(11):
    row = []
    inp=str(input())
    for j in inp:
        if j==".":
            row.append(0)
        elif j.isnumeric():
            row.append(int(j))
    if len(row)!=0:
        board.append(row)

def printBoard(board):
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print('|', end=" ")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ",end=" ")

def solve(board):
    find =findEmpty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(board,i,(row,col)):
            board[row][col]=i

            if solve(board):
                return True
            board[row][col]=0
    return False

def valid(board,num,pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1]!=i:
            return False
    for i in range(len(board)):
        if board[i][pos[1]]==num and pos[0]!=i:
            return False
    box_r = pos[0]//3
    box_c = pos[1]//3
    for i in range(box_r*3,box_r*3+3):
        for j in range(box_c * 3, box_c * 3 + 3):
            if board[i][j]==num and (i,j)!=pos:
                return False
    return True
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i,j)
    return None

print()
start_time = time.time()
solve(board)
end_time = time.time()
print("Computed a solution in",round(end_time-start_time,2),"seconds\n")
printBoard(board)
