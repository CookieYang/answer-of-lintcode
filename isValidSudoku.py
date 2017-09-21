a = set([])
def check(c):
    if c == '.':
        return True
    elif c >= '1' and c <= '9':
        if c in a:
            return False
        else:
            a.add(c)
            return True
    else:
        return False

def isValidSudoku(board):
    for i in range(9):
        for j in range(9):
            if not check(board[i][j]):
                return False
        a.clear()
    for i in range(9):
        for j in range(9):
            if not check(board[j][i]):
                return False
        a.clear()
    for i in range(9):
        for j in range(9):
            if not check(board[int(i/3)*3 + int(j/3)][i%3*3 + j%3]):
                return False
        a.clear()
    return True


print(isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]))