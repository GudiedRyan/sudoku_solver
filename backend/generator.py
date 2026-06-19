import copy
import random

import full_sudoku as fs

DIFFICULTY_CLUES = {
    'easy': 38,
    'medium': 30,
    'hard': 24,
}


def _base_grid():
    return [[(3 * (r % 3) + r // 3 + c) % 9 + 1 for c in range(9)] for r in range(9)]


def _shuffle_grid(grid):
    digits = list(range(1, 10))
    shuffled_digits = digits[:]
    random.shuffle(shuffled_digits)
    mapping = dict(zip(digits, shuffled_digits))
    grid = [[mapping[v] for v in row] for row in grid]

    if random.random() < 0.5:
        grid = [list(row) for row in zip(*grid)]

    for band in range(3):
        rows = list(range(band * 3, band * 3 + 3))
        random.shuffle(rows)
        grid[band * 3:band * 3 + 3] = [grid[r] for r in rows]

    band_order = [0, 1, 2]
    random.shuffle(band_order)
    grid = sum((grid[b * 3:b * 3 + 3] for b in band_order), [])

    col_order = []
    stack_order = [0, 1, 2]
    random.shuffle(stack_order)
    for stack in stack_order:
        stack_cols = list(range(stack * 3, stack * 3 + 3))
        random.shuffle(stack_cols)
        col_order.extend(stack_cols)
    grid = [[row[c] for c in col_order] for row in grid]

    return grid


def generate_solved_grid():
    return _shuffle_grid(_base_grid())


def _is_solvable(puzzle):
    fs.columns = []
    fs.boxes = [[], [], [], [], [], [], [], [], []]
    fs.change_list = []
    return fs.sudoku_king(copy.deepcopy(puzzle)) is not False


def generate_puzzle(difficulty='medium'):
    clues = DIFFICULTY_CLUES.get(difficulty, DIFFICULTY_CLUES['medium'])
    solution = generate_solved_grid()
    puzzle = [row[:] for row in solution]

    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)
    blanks_target = 81 - clues

    removed = 0
    for r, c in cells:
        if removed >= blanks_target:
            break
        saved = puzzle[r][c]
        puzzle[r][c] = 0
        if _is_solvable(puzzle):
            removed += 1
        else:
            puzzle[r][c] = saved

    return puzzle, solution
