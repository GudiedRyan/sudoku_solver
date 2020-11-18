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
                 
#change_list can have an additional condition: single
# The single modifier will determine if we need to just undo this one also and go back to the next one. 
# Not exactly pretty, but it will negate the issue from earlier
#print(better_solver(test_puzzle_rows))     

# Note: Setting n, m, and b will not change the loop position. This is fine. We can work around this.
# Keep the deletion, but put the coordinates in a new list so that you know to go back and fix it'

# IDEA:
# Whenever we place a number, return that new one, then call the function again.
# Similar to before, we will log the change into an array with positional information.
# When there is a contradiction, return to previous result in stack or queue, (DECIDE WHICH), then use a different number from that stack/queue


columns = []
boxes = [[],[],[],[],[],[],[],[],[]]
possible_numbers = [1,2,3,4,5,6,7,8,9]
change_list = []
back_log = []

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
        return candidates
    rows[n].pop(m)
    rows[n].insert(m, candidates[0])
    print("Inserted", candidates[0], "at [", n, ",", m, "]")
    # candidates.pop(0)
    # Why am I removing this line? In the case where there is only one option, we will be fed a contradiction via the empty list. This way we don't shorten a list too far
    change = [n,m,candidates]
    change_list.append(change)
    return candidates
        
def sudoku_plumber(rows):
    "This goes back to the problematic position and inserts the next candidate"
    if len(change_list) == 0:
        # If somehow the list is empty and this function is called, then we need to exit before the program runs into an error.
        # In fact, this really shouldn't even be necessary. Need to rethink this.
        print("Empty")
        return rows
    changes = change_list[-1]
    p = changes[0] # Not required to identify n and m, but it makes it easier for me, so deal with it.
    q = changes[1]
    if len(changes[2]) == 1:
        # If there was only one candidate, then clearly we can't just move to the next one, so we're going to have to iterate back one more (At least)
        rows[p].pop(q)
        rows[p].insert(q,0)
        # backdata = [p,q]
        # back_log.insert(0,backdata)
        change_list.pop(-1)
        print("deleted")
        sudoku_plumber(rows)
        # Here we call it again to basically repeat this process as needed
        return rows
    else:
        changes[2].pop(0)
        rows[p].pop(q)
        rows[p].insert(q,changes[2][0])
        change_list.pop()
        change = [p,q,changes[2]]
        change_list.append(change)
        print("Re-Inserted", changes[0], "at [", p, ",", q, "]")
        return rows
        
def sudoku_flush(rows):
    "Iterate through the back_log stuff and work via that"
    if len(back_log) > 0:
        back = back_log[0]
        u = back[0]
        v = back[1]
        if rows[u][v] != 0:
            back_log.pop(0) #This takes care of the possibility that we get duplicate points from plumber
            sudoku_flush(rows)
        sudoku_solver(rows,u,v) # Call the sudoku solver to do the back_log points
        if len(change_list[-1][2]) == 0:
            # If this runs into a contradiction, then we need to fix this
            rows[u].pop(v)
            rows[u].insert(v,0)
            change_list.pop(-1)
            sudoku_plumber(rows)
        else:
            back_log.pop(0)
            sudoku_flush(rows)
    else:
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
                    rows[n].pop(m) # This might be jumping the gun here. By having this outside of the plumber function, we limit ourselves to this routine. Perhaps this needs to be integrated into the plumber function.
                    rows[n].insert(m,0)
                    # backdata = [n,m]
                    # back_log.insert(0,backdata) #Stick the coordinates into the back_log queue
                    change_list.pop(-1) # Remove the last entry with the empty candidates list
                    #changes = change_list[-1] #Grab the next entry, important to know
                    sudoku_plumber(rows)
                    # sudoku_flush(rows)
                    if len(change_list) != 0:
                        n = change_list[-1][0]
                        m = change_list[-1][1]
            m += 1
        n += 1
                
                    
    print(change_list)
    # print(back_log)
    print(rows)      
    return rows
                
    # Code segment for after we fix a backtrack:
    # while len(back_log) > 0:
    #     sudoku_solver(back_log[-1][0],back_log[-1][1])
    #     back_log.pop(-1)
    # TO KEEP IN MIND:
    # If we run into a contradiction, we will have to make sure we run through and fix. Find a way to implement this without rewriting everything
    # Ideally we can just merge this as part of the sudoku_king function

            

sudoku_king(test_puzzle_rows)

# Full final Algo:
# 1. Given an input of rows, where rows is a list of lists containing the contents of each row, we will check for blank spots or '0's using the king function.
# 2. The "king" function uses 2 for loops to check each entry within the sublists
# 3. Upon identifying a zero, call the solver function, which will call the functions to generate box/column data and create a list of candidates for that position.
# 4. The candidates list will be a queue, first in will be the first used for the 0.
# 5. pop the 0 from rows, and insert the first candidate, then pop the first candidate from the list of candidates
# 5. At this point, the row number, the column number, and the candidates list will all be put into a list, then inserted to the end of the changes_list.
# 6. At this point, exit the solver function and return the new rows data.
# 6.5. Once the rows are returned, check the end of the change_list, change_list[-1][2]. If this is EMPTY, we need to backtrack.
# 7. The king function will now proceed to the next 0, where it will call the solver function again to find the candidates.
# 8. If there are no candidates available at that particular point, we have reached a contradiction, which means there was a mistake. From here we take the last element added to the changes_list stack
# 9. If the candidates list is empty, then we take the row and column position, pop the number at that position and insert 0, then put the row, column coordinates into a list called back_log, then pop data from the changes_list stack
# 10. If the candidates list is not empty, then we pop the element at the specified row and column position, then insert the next item in the queue, and pop that from the candidates queue. From here, we pop the data from changes_list, and insert the new data with the updated candidates list
# 11. If the back_log queue is empty, then the king function will return to the point that caused the contradiction and try again
# 12. If there is a back_log, then the king function will call the sovler at the points listed in the back_log queue, which will act the same as the regular process
# 13. This will continue until no 0's are left, upon which the king function will return the solved rows.

# Ammendments:
# Keep the change_list/plumber tools.
# Switch for loops to while loops and after running plumber, rather than creating a back_log, just iterate after the change was made.
# Basically if rows[4][1] has no candidates, go back to the previous entry. If there's another candidate, switch to that.
# This WILL NOT change the functionality of the change_list stack, it will simply nullify the back_log rubbish.