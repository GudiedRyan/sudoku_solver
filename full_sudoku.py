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


test_2 = [[0,0,3,0,4,2,0,9,0],
          [0,9,0,0,6,0,5,0,0],
          [5,0,0,0,0,0,0,1,0],
          [0,0,1,7,0,0,2,8,5],
          [0,0,8,0,0,0,1,0,1],
          [3,2,9,0,0,8,7,0,6],
          [0,3,0,0,0,0,0,0,1],
          [0,0,5,0,9,0,0,2,0],
          [0,8,0,2,1,0,6,0,0]]

easy_test = [[0,3,0,0,9,0,0,0,8],
             [4,0,0,1,5,0,6,0,9],
             [8,0,9,0,0,3,0,5,0],
             [0,0,0,0,3,7,9,2,0],
             [7,5,0,0,0,9,0,0,0],
             [2,9,0,4,1,0,0,8,5],
             [5,0,8,0,4,0,1,7,0],
             [0,0,7,3,0,0,0,6,4],
             [3,0,1,6,0,5,0,0,0]]

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


possible_numbers = [1,2,3,4,5,6,7,8,9]

def solver(rows):
    "Solves the sudoku puzzle, ideally"
    candidates = []
    create_boxes(rows)
    create_columns(rows)
    b = 0
    run = False
    for n in range(9):
        for m in range(9):
            if rows[n][m] == 0:
                b = identify_box(n,m)
                for r in range(9):
                    if possible_numbers[r] not in rows[n] and possible_numbers[r] not in columns[m] and possible_numbers not in boxes[b]:
                        candidates.append(possible_numbers[r])
                        continue
                    continue
                if len(candidates) == 1:
                    rows[n].pop(m)
                    rows[n].insert(m,candidates[0])
                    candidates.clear()
                    run = True
                    print("Found one")
                    break
                else:
                    candidates.clear()
                    continue
                continue
            continue
        continue
    candidates.clear()
    for y in range(9):
        if 0 in rows[y] and run == True:
            columns.clear()
            for x in range(9):
                boxes[x].clear()
                continue
            solver(rows)
        else:
            #print(changes)
            break
    columns.clear()
    for x in range(9):
        boxes[x].clear()
        continue
    return rows
#print(solver(test_puzzle_rows))
#print(solver(easy_test))
#print(solver([[6, 3, 5, 7, 9, 4, 2, 1, 8], [4, 7, 2, 1, 5, 8, 6, 3, 9], [8, 0, 9, 0, 0, 3, 4, 5, 0], [1, 8, 4, 0, 3, 7, 9, 2, 0], [7, 5, 6, 0, 0, 9, 0, 4, 0], [2, 9, 3, 4, 1, 6, 7, 8, 5], [5, 6, 8, 9, 4, 2, 1, 7, 3], [9, 0, 7, 3, 0, 1, 0, 6, 4], [3, 0, 1, 6, 0, 5, 0, 9, 0]]))
#print(solver([[6, 3, 5, 7, 9, 4, 2, 1, 8], [4, 7, 2, 1, 5, 8, 6, 3, 9], [8, 0, 9, 2, 0, 3, 4, 5, 0], [1, 8, 4, 5, 3, 7, 9, 2, 0], [7, 5, 6, 0, 0, 9, 0, 4, 0], [2, 9, 3, 4, 1, 6, 7, 8, 5], [5, 6, 8, 9, 4, 2, 1, 7, 3], [9, 2, 7, 3, 0, 1, 0, 6, 4], [3, 0, 1, 6, 0, 5, 8, 9, 0]]))
#print(solver([[6, 3, 5, 7, 9, 4, 2, 1, 8], [4, 7, 2, 1, 5, 8, 6, 3, 9], [8, 1, 9, 2, 0, 3, 4, 5, 0], [1, 8, 4, 5, 3, 7, 9, 2, 6], [7, 5, 6, 8, 0, 9, 0, 4, 0], [2, 9, 3, 4, 1, 6, 7, 8, 5], [5, 6, 8, 9, 4, 2, 1, 7, 3], [9, 2, 7, 3, 8, 1, 0, 6, 4], [3, 4, 1, 6, 0, 5, 8, 9, 0]]))
#print(solver([[6, 3, 5, 7, 9, 4, 2, 1, 8], [4, 7, 2, 1, 5, 8, 6, 3, 9], [8, 1, 9, 2, 0, 3, 4, 5, 7], [1, 8, 4, 5, 3, 7, 9, 2, 6], [7, 5, 6, 8, 2, 9, 0, 4, 0], [2, 9, 3, 4, 1, 6, 7, 8, 5], [5, 6, 8, 9, 4, 2, 1, 7, 3], [9, 2, 7, 3, 8, 1, 5, 6, 4], [3, 4, 1, 6, 0, 5, 8, 9, 0]]))
#print(solver([[6, 3, 5, 7, 9, 4, 2, 1, 8], [4, 7, 2, 1, 5, 8, 6, 3, 9], [8, 1, 9, 2, 6, 3, 4, 5, 7], [1, 8, 4, 5, 3, 7, 9, 2, 6], [7, 5, 6, 8, 2, 9, 3, 4, 0], [2, 9, 3, 4, 1, 6, 7, 8, 5], [5, 6, 8, 9, 4, 2, 1, 7, 3], [9, 2, 7, 3, 8, 1, 5, 6, 4], [3, 4, 1, 6, 7, 5, 8, 9, 0]]))
# After 6 iterations, the puzzle is solved for easy_test

# In depth Algorithm:
# Check each row for a 0
# If there are no 0's, return the rows
# Generate the column and box data
# At the first zero, check the corresponding row, column, and box to see which numbers are candidates
# If there is only one candidate, remove the 0 and put that candidate in, 
    # then remake the column and box data, clear the candidates and continue to the next 0
# If there there are at least 2 candidates, input the first candidate, and save a copy of the candidates list with the used number removed.
    # Store the row, column, box, and copied list in an array called changes
    # Remake the column and box data, and clear the candidates list
    # Continue to the next 0
# If there are NO candidates, grab the last piece of information from the changes list
    # This will be the last edited number, so go back to that position and remove the number
    # Replace it with the first number from the copied candidates list, then pop that number from the copied candidates list
    # Remake column and box data, then proceed from the position that was most recently changed
        # IF the copied candidates list is EMPTY, remove the entire data entry from the changes list
        # obtain the information from the last changed data entry repeat the process
# Continue until all 0's have been correctly replaced
# Return the rows 


#To speed up this one, we may consider running the original solver to try to reduce the load
columns = []
boxes = [[],[],[],[],[],[],[],[],[]]
possible_numbers = [1,2,3,4,5,6,7,8,9]
change_list = []
def better_solver(rows):
    "Better solver using the newer algorithm"
    create_columns(rows)
    create_boxes(rows)
    b = 0
    for n in range(9):
        for m in range(9):
            if rows[n][m] == 0:
                b = identify_box(n,m)
                candidates = []
                for r in possible_numbers:
                    if possible_numbers[r] not in rows[n] and possible_numbers[r] not in columns[m] and possible_numbers[r] not in boxes[b]:
                        candidates.append(possible_numbers[r])
                        continue
                    continue
                if len(candidates) >= 1:
                    rows[n].pop(m)
                    rows[n].insert(m,candidates[0])
                    candidates.pop(0)
                    change = [n,m,b,candidates]
                    change_list.insert(0, change)
                    columns.clear()
                    boxes.clear()
                    create_boxes(rows)
                    create_columns(rows)
                    candidates.clear()
                elif len(candidates) == 0:
                    change = change_list[0]
                    if len(change[3]) == 0:
                        n = change[0]
                        m = change[1]
                        b = change[2]
                        rows[n].pop(m)
                        rows[n].insert(m,0)
                        change_list.pop(0)
                        # Here we need to make it do this again, but with the next entry.
                        # We also need to consider the case where it's not messy, which is easy
                        # We could try while len(change[3]) == 0 
                    


