
import sys
from backtracking import SudokuBacktracker

def read_grid_from_file(path):
    lines = []
    with open(path, 'r', encoding='utf-8') as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            # keep only first 9 chars that are digits or . _ or 0
            filtered = []
            for ch in line:
                if ch.isdigit() or ch in '._':
                    filtered.append(ch)
                if len(filtered) == 9:
                    break
            if len(filtered) == 9:
                lines.append(''.join(filtered))
            else:
                # if line shorter, pad with _
                lines.append(''.join(filtered).ljust(9, '_'))
            if len(lines) == 9:
                break
    if len(lines) != 9:
        raise ValueError('Le fichier doit contenir 9 lignes valides représentant une grille 9x9.')
    return lines

def solve_file(path):
    grid = read_grid_from_file(path)
    solver = SudokuBacktracker(grid)
    print("Grille lue depuis:", path)
    print("Grille initiale:")
    print(solver.pretty_print(mark_new=False))
    solved = solver.solve()
    if solved:
        print("\nSolution trouvée:")
        print(solver.pretty_print(mark_new=True))
    else:
        print("Aucune solution trouvée pour cette grille.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py <fichier_grille.txt>")
        sys.exit(1)
    solve_file(sys.argv[1])
