from helpers import *

def solveNBishops(row_start: int = 3, col_start: int = 3, n: int = 8) -> list[tuple[int, int]]:
    """Finds a single solution for the N-Bishops problem.
    Args:
        row_start (int): The row index for the mandatory first bishop.
        col_start (int): The column index for the mandatory first bishop.
        n (int)        : The size of the chessboard (default is 8).

    Returns:
        A list of (row, col) tuples representing the bishop positions in the
        first found valid solution, or an empty list if no solution is found.
    """
    
    results = []
    diagsPos, diagsNeg = set(), set()

    if row_start >= n or col_start >= n:
        raise IndexError(f"Stulpelio/eiles pradzia negali buti didesne nei {n}")
    elif row_start < 0 or col_start < 0:
        raise IndexError(f"Stulpelio/eiles pradzia negali buti mazesne nei 0")

    def get_covered_squares(board: list[tuple[int, int]]) -> set:
        """Calculates the set of squares covered by the given bishops.

        Args:
            board (list[tuple[int, int]]): A list of (row, col) tuples representing current bishop positions.

        Returns:
            A set of (row, col) tuples for all squares occupied or attacked
            by the bishops.
        """
        covered = set()
        
        for r, c in board:
            # Add the bishop's position
            covered.add((r, c))
            
            # Add all squares on diagonals
            directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dr, dc in directions:
                row_covered, col_covered = r + dr, c + dc
                while 0 <= row_covered < n and 0 <= col_covered < n:
                    covered.add((row_covered, col_covered))
                    row_covered += dr
                    col_covered += dc
        
        return covered

    def addBishop(board: list[tuple[int, int]], row: int, col: int, dN: set[int], dP: set[int]) -> None:
        """
        Adds chess piece to the board and stores its diagonal constraints

        Parameters:
            board (list[tuple[int, int]]) : The list representing the current bishop positions.
            row   (int)             : Row number
            col   (int)             : Column number
        Returns:
            None
        """
        # Add bishop to board
        # Add diagonal constraints
        board.append((row, col,))
        dN.add(row - col)
        dP.add(row + col)

    def delBishop(board: list[tuple[int, int]], row: int, col: int, dN: set[int], dP: set[int]) -> None:
        """
        Removes chess piece from the board and removes its diagonal constraints 

        Parameters:
            board (list[tuple[int, int]]) : The list representing the current bishop positions.
            row   (int)             : Row number
            col   (int)             : Column number
            dN    (set[int])        : Set of numbers representing constraints in positive(↗) diagonal direction
            dP    (set[int])        : Set of numbers representing constraints in negative(↘) diagonal direction
        
        Returns:
            None
        """

        board.pop()
        dN.remove(row - col)
        dP.remove(row + col)

    def backtracking(row: int, col: int, curr_board: list[tuple[int, int]]) -> None:
        """
        Backtracks through the board searching for solution to the N bishop problem

        Args:
            row (int)        : Row to backtrack from
            col (int)        : Column to backtract from
            curr_board(list[tuple[int,int]]): The list of (row, col) tuples for currently placed bishops.

        Return:
            None
        """
        figure_count = len(self.diags_neg or self.diags_pos) 

        if len(self.results):
            return

        if bish_cnt >= n:
            # Check if bishops cover all squares
            if len(get_covered_squares(curr_board)) == n * n:
                for tuple in curr_board:
                    results.append(tuple)
            return

        if row >= n:
            return

        for r in range(row, n):
            start_col = col if row == r else 0
            for c in range(start_col, n):
                # Check if doesn't violate constraints
                if (r - c) in self.diags_neg or (r + c) in self.diags_pos:
                    continue

                addBishop(curr_board, r, c, diagsNeg, diagsPos)

                backtracking(r, c + 1, curr_board)

                delBishop(curr_board, r, c, diagsNeg, diagsPos)

        Raises:
            ValueError: If no solutions were found
        """

    init_board = []
    addBishop(init_board , row_start, col_start, diagsNeg, diagsPos)
    backtracking(0, 0, init_board)

    try:
        return results
    except:
        print(f"Nerasta sprendimu {row_start}:{col_start}")
        return []


if __name__ ==  "__main__":
    start = (0, 3)
    sol = solveNBishops(row_start=start[0], col_start=start[1])
    print_board(create_board_string(sol), start_pos=start)

