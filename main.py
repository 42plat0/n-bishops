class NBishopSolver:
    def __init__(self, board_size: int = 8, col_start: int = 1, row_start: int = 1) -> None:
        """
        Initialize the N Bishops solver.
        
        Args:
            n         (int): Size of the chessboard (default is 8x8)
            row_start (int): Starting row for first bishop placement (1-indexed)
            col_start (int): Starting column for first bishop placement (1-indexed)
        """

        self.n = board_size
        self._validate_input(col_start, row_start) # Validate input before doing anything else

        self.row_start = row_start - 1 # Adjust for 0 indexing
        self.col_start = col_start - 1 # Adjust for 0 indexing

        self.bishop = "B"
        self.results = [] # Returning list, could be used to get more than 1 sol
        self.board = [["." for _ in range(self.n)] for _ in range(self.n)] # Chess board holding solutions (verified or not), passed through each bactrack
        self.diags_pos = set() # Set of numbers representing constraints in positive(↗) diagonal direction
        self.diags_neg = set() # Set of numbers representing constraints in negative(↘) diagonal direction


    def _validate_input(self, col_start, row_start) -> None:
        """
        Validate the input parameters for board size and starting position.

        Args:
            col_start (int): Input row number (1 indexing)
            row_start (int): Input row number (1 indexing)
        
        Raises:
            AssertionError: If starting row or column is out of board bounds  
        """

        assert col_start <= self.n, f"Stulpelio pradzia negali buti didesne nei {self.n}"
        assert row_start <= self.n, f"Eiles pradzia negali buti didesne nei {self.n}"
        assert col_start > 0,       f"Stulpelio pradzia negali buti mazesne nei 0"
        assert row_start > 0,       f"Eiles pradzia negali buti mazesne nei 0"


    def _add_figure(self, col: int, row: int) -> None:
        """
        Add bishop to the board at row[col] and stores positions diagonal constraints

        Args:
            row   (int)             : Row number
            col   (int)             : Column number
        Returns:
            None
        """

        self.board[row][col] = self.bishop 
        self.diags_neg.add(row - col)
        self.diags_pos.add(row + col)


    def _del_figure(self, col: int, row: int) -> None:
        """
        Removes bishop from the board at row[col] and removes its diagonal constraints

        Args:
            row   (int)             : Row number
            col   (int)             : Column number
        """
        self.board[row][col] = "."
        self.diags_neg.remove(row - col)
        self.diags_pos.remove(row + col)
   
    def _backtrack(self, col: int, row: int) -> None:
        """
        Backtracks through the board searching for solution to the N bishop problem

        Args:
            row (int)        : Row to backtrack from
            col (int)        : Column to backtract from
        """
        figure_count = len(self.diags_neg or self.diags_pos) 

        if len(self.results):
            return

        if figure_count >= self.n:
            str_res = ["".join(r) for r in self.board]
            self.results.append(str_res)
            return

        if col >= self.n or row >= self.n:
            return

        for r in range(self.n):
            for c in range(self.n):
                # Check if doesn't violate constraints
                if (r - c) in self.diags_neg or (r + c) in self.diags_pos:
                    continue

                self._add_figure(c, r)
                self._backtrack (c, r)
                self._del_figure(c, r)

    def solve(self) -> list[str]:
        """
        Solve the N Bishops problem.
        
        Return:
            list[str]: A solution with N bishops placed without conflicts

        Raises:
            ValueError: If no solutions were found
        """

        self._add_figure(self.col_start, self.row_start)
        self._backtrack(0, 0)

        if not self.results:
            raise ValueError(f"Sprendimu {self.n} dydzio lentoje su pradzia f{self.col_start}f{self.row_start} nerasta")

        return self.results[0]

    @staticmethod
    def print_board(solution: list[str], figure: str = "B", n: int = 8) -> None:
        """
        Prints out a pretty chess board with solution

        Args:
            solution (list[str]): Board solution for N bishop problem
            figure   (str)      : Single ascii char representing a chess piece ('B')
            n        (int)      : Board size
        """

        top_line = "  " + "_" * (n * 3 - 2)

        empty_cell = "|_|"
        figure_cell = f"|{figure}|"

        print(top_line)

        for row in range(n - 1, -1, -1):
            print(row + 1, end="")  # Row numbers
            for col in range(n):
                if solution[row][col] == figure:
                    print(figure_cell, end="")  # Print figure
                    continue
                print(empty_cell, end="")  # Print empty cell
            print()  # Separate rows

        print(" ", end="")  # Space for letter alignment
        for i in range(n):
            print(f" {chr(i + 97)} ", end="")  # Col letters

        print()

solver = NBishopSolver(col_start=5, row_start=3)
solution = solver.solve()
solver.print_board(solution)