board = [[".",".",".",".",".",".","5",".","."]
         ,[".",".",".",".",".",".",".",".","."]
         ,[".",".",".",".",".",".",".",".","3"]
         ,[".","2",".","7",".",".",".",".","."],
         ["8","3","6","5",".",".",".",".","1"],
         [".",".",".",".",".","1",".",".","."],
         ["2",".",".",".",".",".",".",".","5"],
         [".",".",".",".",".",".",".",".","7"],
         [".",".",".","4",".",".",".","7","."]]





def isValidSudoku(board):
    for i in range(0,9):
        set1 = set()
        for j in range(0,9):
            if board[i][j] == ".":
                continue
            elif board[i][j] in set1:
                return (False)
            else:
                set1.add(board[i][j])

    for i in range(0,9):
        set1 = set()
        for j in range(0,9):
            if board[j][i] == ".":
                continue
            elif board[j][i] in set1:
                return (False)
            else:
                set1.add(board[j][i])


    # To check in all 3x3 grid
    set1 = set()
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == ".":
                    continue
            elif board[i][j] in set1:
                return (False)
            else:
                set1.add(board[i][j])

    set1 = set()
    for i in range(0,3):
        for j in range(3,6):
            if board[i][j] == ".":
                    continue
            elif board[i][j] in set1:
                return(False)
            else:
                set1.add(board[i][j])


    set1 = set()
    for i in range(0,3):
        for j in range(6,9):
            if board[i][j] == ".":
                    continue
            elif board[i][j] in set1:
                return(False)
            else:
                set1.add(board[i][j])

    set1 = set()
    for i in range(3,6):
        for j in range(0,3):
            if board[i][j] == ".":
                    continue
            elif board[i][j] in set1:
                return(False)
            else:
                set1.add(board[i][j])
    

    set1 = set()
    for i in range(3,6):
        for j in range(3,6):
            if board[i][j] == ".":
                    continue
            elif board[i][j] in set1:
                return(False)
            else:
                set1.add(board[i][j])


    set1 = set()
    for i in range(3,6):
        for j in range(6,9):
            if board[i][j] == ".":
                    continue
            elif board[i][j] in set1:
                return(False)
            else:
                set1.add(board[i][j])

    
    set1 = set()
    for i in range(6,9):
        for j in range(0,3):
            if board[i][j] == ".":
                    continue
            elif board[i][j] in set1:
                return(False)
            else:
                set1.add(board[i][j])


    set1 = set()
    for i in range(6,9):
        for j in range(3,6):
            if board[i][j] == ".":
                    continue
            elif board[i][j] in set1:
                return(False)
            else:
                set1.add(board[i][j])

    
    set1 = set()
    for i in range(6,9):
        for j in range(6,9):
            if board[i][j] == ".":
                    continue
            elif board[i][j] in set1:
                return(False)
            else:
                set1.add(board[i][j])

    return True


print(isValidSudoku(board))
    

    
        


