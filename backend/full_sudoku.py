import copy

columns = []
boxes = [[],[],[],[],[],[],[],[],[]]

def create_columns(puzzle):
    for n in range(9):
        column = []
        for m in range(9):
            column.insert(m, puzzle[m][n])
        columns.insert(n, column)
    return columns

def generate_columns(puzzle):
    columns = []
    for row in range(9):
        column = []
        for number in range(9):
            column.insert(number, puzzle[number][row])
        columns.insert(row, column)
    return columns

def create_boxes(rows):
    for n in range(3):
        for m in range(3):
            boxes[0].append(rows[n][m])
        for m in range(3,6):
            boxes[1].append(rows[n][m])
        for m in range(6,9):
            boxes[2].append(rows[n][m])
    for n in range(3,6):
        for m in range(3):
            boxes[3].append(rows[n][m])
        for m in range(3,6):
            boxes[4].append(rows[n][m])
        for m in range(6,9):
            boxes[5].append(rows[n][m])
    for n in range(6,9):
        for m in range(3):
            boxes[6].append(rows[n][m])
        for m in range(3,6):
            boxes[7].append(rows[n][m])
        for m in range(6,9):
            boxes[8].append(rows[n][m])
    return boxes


def identify_box(n,m):
    if n in range(3):
        if m in range(3):
            return 0
        elif m in range(3,6):
            return 1
        elif m in range(6,9):
            return 2
    elif n in range(3,6):
        if m in range(3):
            return 3
        elif m in range(3,6):
            return 4
        elif m in range(6,9):
            return 5
    elif n in range(6,9):
        if m in range(3):
            return 6
        elif m in range(3,6):
            return 7
        elif m in range(6,9):
            return 8


columns = []
boxes = [[],[],[],[],[],[],[],[],[]]
possible_numbers = [1,2,3,4,5,6,7,8,9]
change_list = []

def box_cleaner(boxes):
    for t in range(9):
        boxes[t].clear()
    return boxes

def sudoku_solver(rows,n,m):
    create_boxes(rows)
    create_columns(rows)
    b = identify_box(n,m)
    candidates = []
    for r in range(9):
        if possible_numbers[r] not in rows[n] and possible_numbers[r] not in columns[m] and possible_numbers[r] not in boxes[b]:
            candidates.append(possible_numbers[r])
            continue
        continue
    if len(candidates) == 0:
        change = [n,m,candidates]
        change_list.append(change)
        box_cleaner(boxes)
        return rows
    rows[n].pop(m)
    rows[n].insert(m, candidates[0])
    change = [n,m,candidates]
    change_list.append(change)
    box_cleaner(boxes)
    return rows

def sudoku_plumber(rows, fixed):
    if fixed == True:
        return rows
    if len(change_list) == 0:
        return rows
    changes = change_list[-1]
    p = changes[0]
    q = changes[1]
    if len(changes[2]) == 0:
        change_list.pop(-1)
        sudoku_plumber(rows, fixed)
        return rows
    elif len(changes[2]) == 1 and fixed == False:
        rows[p].pop(q)
        rows[p].insert(q,0)
        change_list.pop(-1)
        sudoku_plumber(rows, fixed)
        return rows
    else:
        changes[2].pop(0)
        rows[p].pop(q)
        rows[p].insert(q,changes[2][0])
        change_list.pop()
        change = [p,q,changes[2]]
        change_list.append(change)
        fixed = True
        return rows


def sudoku_king(rows):
    if sudoku_filter(rows) == False:
        return False
    box_cleaner(boxes)
    n = 0
    while n < 9:
        m = 0
        while m < 9:
            if rows[n][m] == 0:
                sudoku_solver(rows,n,m)
                if len(change_list[-1][2]) == 0:
                    fixed = False
                    sudoku_plumber(rows, fixed)
                    if len(change_list) == 0:
                        return False
                    n = change_list[-1][0]
                    m = change_list[-1][1]
                    continue
            m += 1
        n += 1
    return rows


def sudoku_filter(rows):
    for n in range(len(rows)):
        no_zeroes = []
        for m in range(9):
            if rows[n][m] != 0:
                no_zeroes.append(rows[n][m])
                continue
            continue
        if len(no_zeroes) != len(set(no_zeroes)):
            return False
        continue
    create_columns(rows)
    for n in range(len(columns)):
        no_zeroes = []
        for m in range(9):
            if columns[n][m] != 0:
                no_zeroes.append(columns[n][m])
                continue
            continue
        if len(no_zeroes) != len(set(no_zeroes)):
            return False
        continue
    create_boxes(rows)
    for n in range(9):
        no_zeroes = []
        for m in range(9):
            if boxes[n][m] != 0:
                no_zeroes.append(boxes[n][m])
                continue
            continue
        if len(no_zeroes) != len(set(no_zeroes)):
            return False
        continue
    return True


def sudoku_hint(puzzle):
    puzzle_copy = copy.deepcopy(puzzle)
    if sudoku_king(puzzle) is False:
        return "Unsolvable Puzzle"
    for row in range(9):
        for number in range(9):
            if puzzle_copy[row][number] == 0:
                puzzle_copy[row].pop(number)
                puzzle_copy[row].insert(number, puzzle[row][number])
                return puzzle_copy
            continue
        continue
    return puzzle_copy
