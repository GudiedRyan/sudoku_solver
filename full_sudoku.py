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

test_2 = [[0,0,8,0,0,0,4,0,6],
          [0,0,7,0,0,8,0,0,0],
          [0,0,0,9,0,1,8,0,0],
          [2,0,1,0,9,0,3,7,0],
          [0,0,9,2,0,4,6,0,0],
          [0,3,5,0,1,0,2,0,9],
          [0,0,6,1,0,9,0,0,0],
          [0,0,0,4,0,0,7,0,0],
          [5,0,2,0,0,0,1,0,0]]

easy_test = [[0,3,0,0,9,0,0,0,8],
             [4,0,0,1,5,0,6,0,9],
             [8,0,9,0,0,3,0,5,0],
             [0,0,0,0,3,7,9,2,0],
             [7,5,0,0,0,9,0,0,0],
             [2,9,0,4,1,0,0,8,5],
             [5,0,8,0,4,0,1,7,0],
             [0,0,7,3,0,0,0,6,4],
             [3,0,1,6,0,5,0,0,0]]

easy_test = [[8,0,0,0,0,0,0,0,0],
             [0,0,3,6,0,0,0,0,0],
             [0,7,0,0,9,0,2,0,0],
             [0,5,0,0,0,7,0,0,0],
             [0,0,0,0,4,5,7,0,0],
             [0,0,0,1,0,0,0,3,0],
             [0,0,1,0,0,0,0,6,8],
             [0,0,8,5,0,0,0,1,0],
             [0,9,0,0,0,0,4,0,0]]

blanktest = [[0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0]]

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


columns = []
boxes = [[],[],[],[],[],[],[],[],[]]
possible_numbers = [1,2,3,4,5,6,7,8,9]
change_list = []
back_log = []

def box_cleaner(boxes):
    "Cleans out the box data to prevent false data from staying"
    for t in range(9):
        boxes[t].clear()
        continue
    return boxes

def sudoku_solver(rows,n,m):
    "Takes the rows and the position, identifies the candidates, then puts the candidates into rows, puts the position data and candidates into the change_list, then returns rows"
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
    # print("Inserted", candidates[0], "at [", n, ",", m, "]")
    # candidates.pop(0)
    # Why am I removing this line? In the case where there is only one option, we will be fed a contradiction via the empty list. This way we don't shorten a list too far
    change = [n,m,candidates]
    change_list.append(change)
    box_cleaner(boxes)
    return rows
        
def sudoku_plumber(rows, fixed):
    "This goes back to the problematic position and inserts the next candidate"
    #if len(change_list) == 0:
        # If somehow the list is empty and this function is called, then we need to exit before the program runs into an error.
        # In fact, this really shouldn't even be necessary. Need to rethink this.
        #print("Empty")
        #return rows
    if fixed == True:
        return rows
    changes = change_list[-1]
    p = changes[0] # Not required to identify n and m, but it makes it easier for me, so deal with it.
    q = changes[1]
    if len(changes[2]) == 0:
        # This means there were no viable candidates, therefore we could not have inserted anything into rows
        change_list.pop(-1)
        sudoku_plumber(rows, fixed)
        return rows
    elif len(changes[2]) == 1 and fixed == False:
        # If there was only one candidate, then clearly we can't just move to the next one, so we're going to have to iterate back one more (At least)
        rows[p].pop(q)
        rows[p].insert(q,0)
        change_list.pop(-1)
        #print("deleted")
        sudoku_plumber(rows, fixed)
        # Here we call it again to basically repeat this process as needed
        return rows
    else:
        changes[2].pop(0)
        rows[p].pop(q)
        rows[p].insert(q,changes[2][0])
        change_list.pop()
        change = [p,q,changes[2]]
        change_list.append(change)
        #print("Re-Inserted", changes[0], "at [", p, ",", q, "]")
        fixed = True
        return rows


def sudoku_king(rows):
    "The sudoku solver manager"
    #for n in range(9):
    n = 0
    while n < 9:
        m = 0
        while m < 9: 
        #for m in range(9):
            if rows[n][m] == 0:
                sudoku_solver(rows,n,m)
                if len(change_list[-1][2]) == 0:
                    # Here is where we check the most recent change to see if we ran into a contraction. It will ignore this check if it works, but it will begin the backtracking process if it failed
                    fixed = False
                    sudoku_plumber(rows, fixed)
                    if len(change_list) != 0:
                        n = change_list[-1][0]
                        m = change_list[-1][1]
                    continue
            m += 1
        n += 1
                               
    #print(change_list)
    print(rows)      
    return rows
                

#sudoku_king(test_puzzle_rows)
#sudoku_king(easy_test)
#sudoku_king(test_2)
#sudoku_king(blanktest)

######################### FUNCTION TWO ###########################
# This will be the staging area for the additonal features. This first one will simply return a hint.
# When this one is called, a copy of rows will be saved to know which are the original points and which are new, so it can select
# a hint accordingly.

# Algorithm:
# 1. Create a copy of the rows
# 2. Call sudoku_king (the solver) on the copy.
# 3. Parse through the original rows, at the first 0, take the index
# 4. Use this index to get the solved answer, and stick this in
# 5. Return the rows with the hint added in