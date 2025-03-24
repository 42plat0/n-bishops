# Is different solution cause bishops can go in the same row, so updates are needed


def solveNBishops(n):
    queen   = "R"
    results, stack = [], []
    board_row = ["." for i in range(n)]
    diagsPos, diagsNeg = set(), set()
    
    """
         For neighbor:
        #################
         dP = row + col
         dN = col - row
        ###############3
    """
    def backtracking(row):
        if row == n:                                                                # Row out of bounds, reached limit
            str_stack = ["".join(col) for col in stack]                             # Turn into strings
            results.append(str_stack[:])                                            # Append string lists to result list 
            return

        for col in range(n):
            # Check if doesn't violate constraints
            if (row - col) in diagsNeg or (row + col) in diagsPos:
                continue
        
            diagsPos.add(row + col); diagsNeg.add(row - col)                        # Add to set of vals to enforce constrains 

            board_current_col = board_row[:]                                        # Copy board row
            board_current_col[col] = queen
            stack.append(board_current_col)                                         # Found solution, go next row

            backtracking(row + 1)                                                   # Go next row tree
            stack.pop()                                                             # Remove solution
            diagsPos.remove(row + col); diagsNeg.remove(row-col)                    # Remove after backtracking from solution to try different ones


    backtracking(0)
    return results

for sol in solveNBishops(2):
    print(sol)

n2 = len(solveNBishops(2)) == 4