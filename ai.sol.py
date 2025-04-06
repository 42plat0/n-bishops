def is_attacking(bishop1, bishop2):
    """Check if two bishops attack each other"""
    row1, col1 = bishop1
    row2, col2 = bishop2
    return abs(row1 - row2) == abs(col1 - col2)

def get_covered_squares(bishops):
    """Return set of squares covered by the bishops"""
    covered = set()
    
    for row, col in bishops:
        # Add the bishop's position
        covered.add((row, col))
        
        # Add all squares on diagonals
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                covered.add((r, c))
                r += dr
                c += dc
    
    return covered

def find_all_solutions(n=8):
    """Find all valid bishop configurations using backtracking"""
    solutions = []
    
    def backtrack(bishops, next_pos=0):
        # If we have placed all bishops
        if len(bishops) == n:
            # Check if they cover all squares
            if len(get_covered_squares(bishops)) == 64:  # 8x8 = 64 squares
                solutions.append(bishops.copy())
            return
        
        # Try each position from next_pos to 63 (8x8 board)
        for pos in range(next_pos, 64):
            row, col = pos // 8, pos % 8
            
            # Check if the new bishop attacks any existing bishop
            new_bishop = (row, col)
            if not any(is_attacking(new_bishop, b) for b in bishops):
                bishops.append(new_bishop)
                backtrack(bishops, pos + 1)  # Continue from next position
                bishops.pop()
    
    backtrack([])
    return solutions

# Run the algorithm
solutions = find_all_solutions()
print(solutions)