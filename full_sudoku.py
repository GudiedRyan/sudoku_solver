import copy
import puzzles as puzzle

# Create file, puzzle.py with all my tests in there
# Remove continues
# Remove global state/variables
# Fix the variables names

columns = []
boxes = [[],[],[],[],[],[],[],[],[]]
# Remove Global Variables ^

# for i,m in lst:
# Make the iterater nicer
# use Puzzle as def, for like for row in puzzle
# Don't use n and m
#OLD
def create_columns(puzzle):
    for n in range(9):
        column = []
        for m in range(9):
            column.insert(m, puzzle[m][n])
        columns.insert(n, column)
    return columns
#NEW
def generate_columns(puzzle):
    columns = []
    for row in range(9):
        column = []
        for number in range(9):
            column.insert(number, puzzle[number][row])
        columns.insert(row, column)
    return columns

# Rework with MODULO, change names, get rid of global variables

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


def generate_boxes(puzzle):
    boxes = []
    
    return boxes

# similar rework and rethink the entire concept

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

# Fix box creater and this

def box_cleaner(boxes):
    "Cleans out the box data to prevent false data from staying"
    for t in range(9):
        boxes[t].clear()
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
        #return False
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
    #Test for errors:
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
                


############################ PREVENTING INFINITE RUNTIME ################################
# There will be a global variable, kill_switch set by default to false.
# What makes a puzzle unsolvable?
#### In terms of the program, we reach an unsolvable issue when we've tried every possible combination.

# Problematic Puzzle checker
#### Run checks that no rows, columns, or boxes have two of the same number in them. If they do, immediately activate kill_switch
#### This will increase runtime sadly, but not so much so that it becomes unreasonable. This will NOT capture every fail, but it will
#### stop obvious failures before they can begin
def sudoku_filter(rows):
    "Prevents us from wasting time on rubbish by identifying mistakes in puzzle"
    # Check rows for dupes
    for n in range(len(rows)):
        no_zeroes = []
        for m in range(9):
            if rows[n][m] != 0:
                no_zeroes.append(rows[n][m])
                continue
            continue
        if len(no_zeroes) != len(set(no_zeroes)):
            # Activate kill switch
            print(rows[n])
            return False
        continue
    # Check columns for dupes
    create_columns(rows)
    for n in range(len(columns)):
        no_zeroes = []
        for m in range(9):
            if columns[n][m] != 0:
                no_zeroes.append(columns[n][m])
                continue
            continue
        if len(no_zeroes) != len(set(no_zeroes)):
            # Activate kill switch
            print(columns[n])
            return False
        continue
    # Check boxes for dupes
    create_boxes(rows)
    for n in range(9):
        no_zeroes = []
        for m in range(9):
            if boxes[n][m] != 0:
                no_zeroes.append(boxes[n][m])
                continue
            continue
        if len(no_zeroes) != len(set(no_zeroes)):
            print(boxes[n])
            return False
        continue
    return True


####### So sudoku Filter will only be able to detect the issues, and I can fix it so it returns feedback based on whether it finds an error.
# I will need to go back to the original idea.

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

def sudoku_hint(puzzle):
    "Calls the solver and returns the puzzle with a hint"
    puzzle_copy = copy.deepcopy(puzzle)
    if sudoku_king(puzzle) is False:
        return "Unsolvable Puzzle"
    for row in range(9):
        for number in range(9):
            if puzzle_copy[row][number] == 0:
                puzzle_copy[row].pop(number)
                puzzle_copy[row].insert(number,puzzle[row][number])
                return puzzle_copy
            continue
        continue
    print(puzzle_copy)
    return puzzle_copy

#sudoku_hint(puzzle.test_puzzle_rows)




# When I check to see if the change_list is empty, it returns and exits the function, or at least, should.
# However, it is going into an infinite loop and I cannot determine why.
# Here, let me tell you why Ryan.
# You are calling plumber from within plumber.
# So it exits plumber and goes back into plumber, which calls it again.