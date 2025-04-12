from helpers import *

def solveNBishops(row_start: int, col_start: int, n: int = 8) -> list[str]:
    results = []
    diagsPos, diagsNeg = set(), set()
    # Start from 0
    board_result = []

    if row_start >= n or col_start >= n:
        raise IndexError(f"Stulpelio/eiles pradzia negali buti didesne nei {n}")
    elif row_start < 0 or col_start < 0:
        raise IndexError(f"Stulpelio/eiles pradzia negali buti mazesne nei 0")

    def get_covered_squares(board: list[list[str]]) -> set:
        """Return set of squares covered by the bishops"""
        covered = set()
        
        for r, c in board_result:
            # Add the bishop's position
            covered.add((r, c))
            
            # Add all squares on diagonals
            directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < n and 0 <= nc < n:
                    covered.add((nr, nc))
                    nr += dr
                    nc += dc
        
        return covered

    def addBishop(board: list[list[str]], row: int, col: int, dN: set[int], dP: set[int]) -> None:
        """
        Adds chess piece to the board and stores its diagonal constraints

        Parameters:
            row   (int)             : Row number
            col   (int)             : Column number
            dN    (set[int])        : Set of numbers representing constraints in positive(↗) diagonal direction
            dP    (set[int])        : Set of numbers representing constraints in negative(↘) diagonal direction
        
        Returns:
            None
        """
        # Add bishop to board
        # Add diagonal constraints
        board_result.append((row, col,))
        dN.add(row - col)
        dP.add(row + col)

    def delBishop(board: list[list[str]], row: int, col: int, dN: set[int], dP: set[int]) -> None:
        """
        Removes chess piece from the board and removes its diagonal constraints 

        Parameters:
            row   (int)             : Row number
            col   (int)             : Column number
            dN    (set[int])        : Set of numbers representing constraints in positive(↗) diagonal direction
            dP    (set[int])        : Set of numbers representing constraints in negative(↘) diagonal direction
        
        Returns:
            None
        """

        board_result.pop()
        dN.remove(row - col)
        dP.remove(row + col)

    def backtracking(row: int, col: int, curr_board: list[tuple[int, int]]) -> None:
        """
        Backtracks through the board searching for solution to the N bishop problem. Checking based on diagonal constraints defined above.

        Parameters:
            row (int)        : Row to backtrack from
            col (int)        : Column to backtract from
            curr_board(list) : Chess board holding solutions (verified or not), passed through each bactrack 

        Return:
            None
        """
        bish_cnt = len(diagsNeg)  # Or positive, doesnt matter

        if len(results):
            return

        if bish_cnt >= n:
            # Check if bishops cover all squares
            if len(get_covered_squares(curr_board)) == n * n:
                for tuple in board_result:
                    results.append(tuple)
            return

        if row >= n:
            return

        for r in range(row, n):
            start_col = col if row == r else 0
            for c in range(start_col, n):
                # Check if doesn't violate constraints
                if (r - c) in diagsNeg or (r + c) in diagsPos:
                    continue

                addBishop(curr_board, r, c, diagsNeg, diagsPos)

                backtracking(r, c + 1, curr_board)

                delBishop(curr_board, r, c, diagsNeg, diagsPos)


    addBishop(board_result, row_start, col_start, diagsNeg, diagsPos)
    backtracking(0, 0, board_result)

    try:
        return results
    except:
        print(f"Nerasta sprendimu {row_start}:{col_start}")
        return []


if __name__ ==  "__main__":
    sol = solveNBishops(row_start=3, col_start=3)
    print_board(create_board_string(sol), start_pos=(3,3,))

