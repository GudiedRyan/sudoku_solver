rows = [[1,0,0,0],
        [0,0,2,0],
        [0,0,0,3],
        [0,4,0,0]]

columns = []
boxes = [[],[],[],[]]
def column_maker(rows):
    "Translates the rows into columns"
    for n in range(4):
        column = []
        for m in range(4):
            column.insert(m, rows[m][n])
            continue
        columns.insert(n, column)
        continue
    return columns

def box_maker(data):
    "Creates the boxes"
    for n in range(2):
        for m in range(2):
            boxes[0].append(data[n][m])
            continue
    for n in range(2):
        for m in range(2,4):
            boxes[1].append(data[n][m])
            continue
    for n in range(2,4):
        for m in range(2):
            boxes[2].append(data[n][m])
            continue
    for n in range(2,4):
        for m in range(2,4):
            boxes[3].append(data[n][m])
            continue
    return boxes

def which_box(n,m):
    "Determines which elements go in which box"
    if n in range(2) and m in range(2):
        return 0
    elif n in range(2) and m in range(2,4):
        return 1
    elif n in range(2,4) and m in range(2):
        return 2
    else:
        return 3

def clear_boxes(boxes):
    "Clears the box data"
    for x in range(4):
        boxes[x].clear()
        continue
    # print(boxes)
    return boxes

# clear_boxes([[0,0,1,0],[0,2,0,0],[4,0,0,0],[0,0,0,3]])

possible_numbers = [1,2,3,4]
change_list = []


def sudoku_solver(rows,n,m):
    "Given the row and column positions, attempt to fill in the spot"
    column_maker(rows)
    box_maker(rows)
    b = which_box(n,m)
    candidates = []
    for r in range(4):
        a = possible_numbers[r]
        if a not in rows[n] and a not in columns[m] and a not in boxes[b]:
            candidates.append(a)
            continue
        #else:
            #print(a, "is in", rows[n], ",", columns[m], "or", boxes[b])
        continue
    if len(candidates) == 0:
        # print("Contradiction at [",n,",",m,"]")
        change = [n,m,candidates]
        change_list.append(change)
        clear_boxes(boxes)
        return rows
    rows[n].pop(m)
    rows[n].insert(m,candidates[0])
    #print("Inserted", candidates[0], "at [", n, ",", m, "]")
    change = [n,m,candidates]
    change_list.append(change)
    clear_boxes(boxes)
    return rows

def sudoku_mechanic(rows):
    "Undoes changes until a new candidate can be entered"
    #print(change_list)
    change = change_list[-1]
    p = change[0]
    q = change[1]
    cand = change[2]
    if len(cand) == 0:
        change_list.pop(-1)
        sudoku_mechanic(rows)
        return rows
    elif len(cand) == 1:
        rows[p].pop(q)
        rows[p].insert(q,0)
        change_list.pop()
        sudoku_mechanic(rows)
        return rows
    else:
        rows[p].pop(q)
        cand.pop(0)
        rows[p].insert(q,cand[0])
        #print("Re-inserted, ",cand[0],"at [",p,",",q,"]")
        change_list.pop()
        change = [p,q,cand]
        change_list.append(change)
        return rows
        
def sudoku_prince(rows):
    "This will manage the loops"
    n = 0
    while n < 4:
        m = 0
        while m < 4:
            if rows[n][m] == 0:
                sudoku_solver(rows,n,m)
                if len(change_list[-1][2]) == 0:
                    sudoku_mechanic(rows)
                    m = change_list[-1][1]
            m += 1
        n += 1
    print(change_list)
    print(rows)
    return rows

sudoku_prince(rows)
# Here it breaks at rows[1][1]

sudoku_prince([[0,0,1,0],[0,2,0,0],[4,0,0,0],[0,0,0,3]])

#sudoku_prince([[1, 2, 3, 4], [4, 0, 2, 1], [2, 1, 4, 3], [3, 4, 1, 2]])
# Here it works