test_puzzle_rows = [[5,3,0,0,7,0,0,0,0],
                    [6,0,0,1,9,5,0,0,0],
                    [0,9,8,0,0,0,0,6,0],
                    [8,0,0,0,6,0,0,0,3],
                    [4,0,0,8,0,3,0,0,1],
                    [7,0,0,0,2,0,0,0,6],
                    [0,6,0,0,0,0,2,8,0],
                    [0,0,0,4,1,9,0,0,5],
                    [0,0,0,0,8,0,0,7,9]]

test_solution = [[5,3,4,6,7,8,9,1,2],
                 [6,7,2,1,9,5,3,4,8],
                 [1,9,8,3,4,2,5,6,7],
                 [8,5,9,7,6,1,4,2,3],
                 [4,2,6,8,5,3,7,9,1],
                 [7,1,3,9,2,4,8,5,6],
                 [9,6,1,5,3,7,2,8,4],
                 [2,8,7,4,1,9,6,3,5],
                 [3,4,5,2,8,6,1,7,9]]
#Important idea: Rather than have a set number of loops, have it check changes
#Each time it changes, increase change count.
#If change count doesnt increase, end

columns = []
boxes = [[],[],[],[],[],[],[],[],[]]
def create_columns(rows):
    "Translates the rows into columns"
    for n in range(9):
        column = []
        for m in range(9):
            column.insert(m, rows[m][n])
            continue
        columns.insert(n, column)
        continue
    return columns

def create_boxes(rows):
    "Translates the rows into the respective boxes"
    for n in range(3):
        for m in range(3):
            boxes[0].append(rows[n][m])
            continue
        for m in range(3,6):
            boxes[1].append(rows[n][m])
            continue
        for m in range(6,9):
            boxes[2].append(rows[n][m])
            continue
    for n in range(3,6):
        for m in range(3):
            boxes[3].append(rows[n][m])
            continue
        for m in range(3,6):
            boxes[4].append(rows[n][m])
            continue
        for m in range(6,9):
            boxes[5].append(rows[n][m])
            continue
    for n in range(6,9):
        for m in range(3):
            boxes[6].append(rows[n][m])
            continue
        for m in range(3,6):
            boxes[7].append(rows[n][m])
            continue
        for m in range(6,9):
            boxes[8].append(rows[n][m])
            continue
    return boxes

def identify_box(n,m):
    "Determines which elements correspond to which box"
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

# def box_checker(rows):
#     for n in range(9):
#         for m in range(9):
#             b = identify_box(n,m)
#             print(b)
#             continue

possible_numbers = [1,2,3,4,5,6,7,8,9]

def solver(rows, changes):
    "Solves the sudoku puzzle, ideally"
    changes = 0
    candidates = []
    create_boxes(rows)
    create_columns(rows)
    b = 0
    for n in range(9):
        for m in range(9):
            if rows[n][m] == 0:
                b = identify_box(n,m)
                for r in range(9):
                    if possible_numbers[r] not in rows[n] and possible_numbers[r] not in columns[m] and possible_numbers not in boxes[b]:
                        candidates.append(possible_numbers[r])
                        continue
                    continue
                print(candidates)
                if len(candidates) == 1:
                    rows[n].pop(m)
                    rows[n].insert(m,candidates[0])
                    candidates.clear()
                    changes += 1
                    continue
                else:
                    candidates.clear()
                    continue
                continue
            continue
        continue
    candidates.clear()
    for y in range(9):
        if 0 in rows[y] and changes != 0:
            #print(changes)
            solver(rows, changes)
        else:
            #print(changes)
            break
    columns.clear()
    for x in range(9):
        boxes[x].clear()
        continue
    return rows
print(solver(test_puzzle_rows, 0))