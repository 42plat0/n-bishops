# Is different solution cause bishops can go in the same row, so updates are needed
from copy import copy, deepcopy

def solveNBishops(n):
    bishop = "B"
    results = []
    board = [["." for _ in range(n)] for _ in range(n)]
    diagsPos, diagsNeg = set(), set()
    
    def backtracking(row, col, curr_board=[]):
        bish_cnt = len(diagsNeg) # Or positive, doesnt matter
        
        if bish_cnt >= n:
            results.append(deepcopy(curr_board))
            curr_board = board[:]
            return

        if col >= n:
            col, row = 0, row+1
        elif row >= n:
            return

        for col in range(n):
            
            for row in range(n):
                # Check if doesn't violate constraints
                if (row - col) in diagsNeg or (row + col) in diagsPos:
                    continue

                # Add bishop to board
                curr_board[row][col] = bishop

                # Add diagonal constraints
                diagsPos.add(row + col); diagsNeg.add(row - col)

                backtracking(row, col, curr_board)

                # Remove last bishop
                curr_board[row][col] = "."
                diagsPos.remove(row + col); diagsNeg.remove(row-col)
        
        

    cp = deepcopy(board)
    backtracking(0, 0, cp)
    return results

for _ in solveNBishops(2):
    print(_)

"""
    2x2 for 2 bishops solutions: 4
     +                       +       + 
    B B         B .         . .     . B
    . .         B .         B B     . B 

"""
