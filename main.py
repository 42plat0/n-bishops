# Is different solution cause bishops can go in the same row, so updates are needed
from copy import copy, deepcopy


def solveNBishops(n: int = 8, row_start: int = 0, col_start: int = 0) -> list[str]:
    bishop = "B"
    results = []
    board = [["." for _ in range(n)] for _ in range(n)]
    diagsPos, diagsNeg = set(), set()

    # Start from 0
    row_start -= 1
    col_start -= 1

    if row_start > n or col_start > n:
        raise IndexError(f"Stulpelio/eiles pradzia negali buti didesne nei {n}")
    elif row_start < 0 or col_start < 0:
        raise IndexError(f"Stulpelio/eiles pradzia negali buti mazesne nei 0")

    def addBishop(board: list[list], col: int, row: int, dN: set, dP: set) -> None:
        # Add bishop to board
        # Add diagonal constraints
        board[row][col] = bishop
        dN.add(row - col)
        dP.add(row + col)

    def delBishop(board: list[list], col: int, row: int, dN: set, dP: set) -> None:
        # Remove last bishop
        board[row][col] = "."
        dN.remove(row - col)
        dP.remove(row + col)

    def backtracking(row: int, col: int, curr_board: list = []) -> None:
        bish_cnt = len(diagsNeg)  # Or positive, doesnt matter

        if len(results) > 1000:
            return

        if bish_cnt >= n:
            str_res = ["".join(r) for r in curr_board]
            results.append(str_res)
            return

        if col >= n or row >= n:
            return

        for r in range(n):
            for c in range(n):
                # Check if doesn't violate constraints
                if (r - c) in diagsNeg or (r + c) in diagsPos:
                    continue

                addBishop(curr_board, c, r, diagsNeg, diagsPos)

                backtracking(r, c, curr_board)

                delBishop(curr_board, c, r, diagsNeg, diagsPos)

    cp = deepcopy(board)
    addBishop(cp, col_start, row_start, diagsNeg, diagsPos)
    backtracking(0, 0, cp)

    return results


def print_board(solution: list[str], figure: str, n: int = 8) -> None :
    top_line = "  " + "_" * (n * 3 - 2)

    empty_cell = "|_|"
    figure_cell = f"|{figure}|"

    print(top_line)

    for row in range(n):
        print(n - row, end="")  # Row numbers
        for col in range(n):
            if solution[row][col] == figure:
                print(figure_cell, end="") # Print figure
                continue
            print(empty_cell, end="") # Print empty cell
        else:
            print() # Separate rows

    print(" ", end="") # Space for letter alignment
    for i in range(n):
        print(f" {chr(i + 97)} ", end="")  # Col letters

    print()


sol = solveNBishops(col_start=1, row_start=1)
print(sol)
# print_board(sol, "B")
# print(sol)

"""
    2x2 for 2 bishops solutions: 4
     +                       +       + 
    B B         B .         . .     . B
    . .         B .         B B     . B 

"""
