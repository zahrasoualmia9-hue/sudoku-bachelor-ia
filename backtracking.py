
class SudokuBacktracker:
    """Classe orientée-objet pour résoudre un Sudoku 9x9 par backtracking."""
    def __init__(self, grid):
        # grid: list of 9 strings or list of lists with 9 elements each (0 or '_' for empty)
        self.original = [[0]*9 for _ in range(9)]
        self.grid = [[0]*9 for _ in range(9)]
        for i, row in enumerate(grid):
            # accept string or list
            if isinstance(row, str):
                chars = list(row.strip())
            else:
                chars = list(row)
            for j, ch in enumerate(chars):
                if ch in '0_' or ch == '.':
                    v = 0
                elif ch.isdigit():
                    v = int(ch)
                else:
                    v = 0
                self.grid[i][j] = v
                self.original[i][j] = v

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None

    def is_valid(self, row, col, val):
        # check row
        for c in range(9):
            if self.grid[row][c] == val:
                return False
        # check column
        for r in range(9):
            if self.grid[r][col] == val:
                return False
        # check 3x3 box
        br = (row // 3) * 3
        bc = (col // 3) * 3
        for r in range(br, br+3):
            for c in range(bc, bc+3):
                if self.grid[r][c] == val:
                    return False
        return True

    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True
        r, c = empty
        for val in range(1, 10):
            if self.is_valid(r, c, val):
                self.grid[r][c] = val
                if self.solve():
                    return True
                self.grid[r][c] = 0
        return False

    def solution(self):
        return self.grid

    def pretty_print(self, mark_new=True):
        """Return a printable string showing original numbers vs filled numbers.
           mark_new: if True, newly filled numbers will be wrapped with brackets [n]
        """
        lines = []
        sep = "+-------+-------+-------+"
        for i in range(9):
            if i % 3 == 0:
                lines.append(sep)
            row_elems = []
            for j in range(9):
                v = self.grid[i][j]
                if v == 0:
                    s = '.'
                else:
                    if self.original[i][j] == 0 and mark_new:
                        s = f'[{v}]'  # newly filled
                    else:
                        s = str(v)
                row_elems.append(s)
                if (j+1) % 3 == 0 and j < 8:
                    row_elems.append('|')
            lines.append('| ' + ' '.join(row_elems) + ' |')
        lines.append(sep)
        return '\n'.join(lines)
