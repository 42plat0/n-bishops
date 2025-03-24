# Is different solution cause bishops can go in the same row, so updates are needed
from copy import copy, deepcopy

def solveNBishops(n):
    bishop = "B"
    results = set()
    board = [["." for _ in range(n)] for _ in range(n)]
    diagsPos, diagsNeg = set(), set()
    
    def backtracking(row, col, curr_board=[]):
        bish_cnt = len(diagsNeg) # Or positive, doesnt matter

        if bish_cnt >= n:
            # if diagsPos not in totalDP and diagsNeg not in totalDN:
            str_res = "".join(["".join(r) for r in curr_board])

            results.add(str_res)
            return

        if col >= n or row >= n:
            return

        for r in range(n):
            for c in range(n):
                # Check if doesn't violate constraints
                if (r - c) in diagsNeg or (r + c) in diagsPos:
                    continue

                # Add bishop to board
                curr_board[r][c] = bishop

                # Add diagonal constraints
                diagsPos.add(r + c); diagsNeg.add(r - c)

                backtracking(r, c, curr_board)

                # Remove last bishop
                curr_board[r][c] = "."
                diagsPos.remove(r + c); diagsNeg.remove(r-c)

    cp = deepcopy(board)
    backtracking(0, 0, cp)
    return results

sol = solveNBishops(8)
for _ in sol:
    print(_)
print( len(sol))

"""
    2x2 for 2 bishops solutions: 4
     +                       +       + 
    B B         B .         . .     . B
    . .         B .         B B     . B 

"""
