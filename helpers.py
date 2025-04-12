def create_board_string(solution: list[tuple[int, int]], n=8) -> list[str]: 
    board = [["." for _ in range(n)] for _ in range(n)]

    for row, col in solution:
        board[row][col] = "B"

    return board


def print_board(solution: list[str], start_pos: tuple[int, int], n=8) -> None:
    """
    Prints out a pretty chess board with solution

    Args:
        solution (list[str]): Board solution for N bishop problem
        figure   (str)      : Single ascii char representing a chess piece ('B')
        n        (int)      : Board size
    """


    def create_cell(figure: str) -> str:
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