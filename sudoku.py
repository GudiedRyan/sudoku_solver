# Drafting:

#Input: Massive list, so we're going to start with a much smaller case of the ole
#1-4 sudoku puzzle

#Idea: Basically for this program we will input the info row by row

#Phase I: identifying a missing number:

#A known number will be put in where it is known, otherwise, place a 0.
#This is just to get a general feel for things, we'll worry about efficiency later.
#The initial test will be to get it to fill in the missing number

# possible_numbers = [1,2,3,4]
# matrix = [4,1,0,2]
def find_missing_num(matrix):
    #Uncomment lines 11 and 12 to make this function work lmao
    for n in range(4):
        if possible_numbers[n] in matrix:
            continue
        else:
            for m in range(4):
                if matrix[m] == 0:
                    matrix.pop(m)
                    matrix.insert(m,possible_numbers[n])
                    print("Missing number is ",possible_numbers[n], " Matrix:", matrix)
                    return True
                else:
                    continue
    print("No missing numbers :D ", matrix)
# find_missing_num(matrix)

#Here we have established that we can in fact identify the missing number with a given row
#The next challenge is to test a 1-4 sudoku puzzle using similar logic on a larger scale.
#THE ONLY ISSUE HERE is if there are 2 zeros. If someone inputs two 0s, they will get the first missing number
#In order to ameliorate this, we need additional checks: Row, Column, and Box.

#Phase II: Looking at rows and columns for the 4x4 board
rows = [[0,0,2,0],[1,0,0,0],[0,3,0,0],[0,0,4,0]]
# solution = [[3,4,2,1],[1,2,3,4],[4,3,1,2],[2,1,4,3]] #This is here for me to make sure it's working.
#Idea: First, we will simplify this by creating a series of new lists to check.
#Rows: board is already the display with rows
#Columns: Basically all the elements with the same indices in their sets. Easy enough to obtain.
#Boxes: Boxes are a little more messy. Fortunately in the 4x4 board it's not ugly. 

#Two ways to do this, one, type it out, which would be rather tedious, especially when we go to the 9x9 board
#OR, create loops that do it for me. Seems like a nice way to abstract the annoying part out.

# column_maker(rows)
 
#Phase III: Data sets

#Each coordinate has its own datapoint. In fact, the function I just created could be used to help classify it.

# ATTRIBUTES - Each number on the board has 4 data points.
# Ex: point = [value, row, column, box]
# If value is unknown, we give it a 0, similar to our earlier functions

data = [[1,2,3,0],
        [3,4,1,2],
        [0,1,2,3],
        [2,0,4,1]]
data2 = [[1,2,0,0],
        [3,4,1,2],
        [0,1,2,3],
        [2,0,4,1]]
data3 = [[1,2,0,0],
        [0,4,1,2],
        [0,1,0,3],
        [2,0,4,1]]
data4 = [[1,0,0,4],
        [0,0,0,2],
        [0,1,0,3],
        [2,0,4,0]]
columns = []
def column_maker(rows):
    for n in range(4):
        column = []
        for m in range(4):
            column.insert(m, rows[m][n])
            continue
        columns.insert(n, column)
        continue
    return columns

def missing_num_row_and_col(data):
    possible_numbers = [1,2,3,4]
    column_maker(data)
    for n in range(4):
        for m in range(4):
            if data[n][m] == 0:
                for x in range(4):
                    if columns[m][x] == 0:
                        for y in range(4):
                            if possible_numbers[y] not in data[n] and possible_numbers[y] not in columns[m]:
                                data[n].pop(m)
                                data[n].insert(m, possible_numbers[y])
                        continue
                    continue
                continue
            continue
        continue
    print(data)
# missing_num_row_and_col(data)
# missing_num_row_and_col(data2)
# missing_num_row_and_col(data3)
# missing_num_row_and_col(data4)
#data, data2, and data3 are solved correctly. data4 is not.
#Now we have the ability to identify the column that the missing number is, given only the row. Next we need to insert that number

#Loop through a row, find the 0
#If no 0's, next row
#If 0,take that index and run through the column with that index to find what numbers are in there.
#Find number that's not in either.

#Phase IV: Box logic
#Box logic will be necessary to determine when items numbers can't be found
boxes = [[],[],[],[]]
def create_boxes(data):
    column_maker(data)
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

#create_boxes(data)
#We now have functions that can generate columns and rows based off of an input of rows