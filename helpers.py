"""Helper functions for N-Bishops problem visualization."""

def create_board_string(solution: list[tuple[int, int]], n=8) -> list[str]:
    """Creates a 2D list representation of the board from bishop coordinates.

    Args:
        solution (list[tuple[int, int]]): A list of (row, col) tuples representing bishop positions.
        n        (int)                  : The size of the chessboard (default is 8).

    Returns:
        A list of lists (2D list) representing the board,
        with 'B' for bishops and '.' for empty squares.
    """
    board = [["." for _ in range(n)] for _ in range(n)]

    for row, col in solution:
        board[row][col] = "B"

    return board


def print_board(solution: list[str], start_pos: tuple[int, int], n=8) -> None:
    """Prints a formatted chessboard with bishop positions.

    Highlights the starting bishop position.

    Args:
        solution  (list[str])         : A 2D list representing the board state (from create_board_string).
        start_pos (tuple[int, int])   : A tuple (row, col) indicating the first placed bishop.
        n         (int)               : The size of the chessboard (default is 8).
    """


    def create_cell(figure: str) -> str:
        """Creates a formatted cell string for the chessboard.

        Args:
            figure (str): A single character representing the cell content.

        Returns:
            A formatted string for the cell, including borders.
        """
        return f"|{figure}|"
    
    empty_cell   = create_cell("_")
    figure_cell  = create_cell("B")
    ffigure_cell = create_cell("𝕭")
    
    top_line = "  " + "_" * (n * 3 - 2)
    print(top_line)

    for row in range(n - 1, -1, -1):
        print(row + 1, end="")  # Row numbers
        for col in range(n):
            if solution[row][col] != ".":
                if (start_pos[0] == row and start_pos[1] == col):
                    print(ffigure_cell, end="")
                    continue
                print(figure_cell, end="")  # Print figure
                continue
            print(empty_cell, end="")  # Print empty cell
        print()  # Separate rows

    print(" ", end="")  # Space for letter alignment
    for i in range(n):
        print(f" {chr(i + 97)} ", end="")  # Col letters

    print()