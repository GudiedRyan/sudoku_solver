# sudoku_solver
A program to solve sudoku puzzles.

To use the program, you need to call sudoku_king() on an list of lists. The data should be in the format that follows:
test_puzzle_rows = [[5,3,0,0,7,0,0,0,0],
                    [6,0,0,1,9,5,0,0,0],
                    [0,9,8,0,0,0,0,6,0],
                    [8,0,0,0,6,0,0,0,3],
                    [4,0,0,8,0,3,0,0,1],
                    [7,0,0,0,2,0,0,0,6],
                    [0,6,0,0,0,0,2,8,0],
                    [0,0,0,4,1,9,0,0,5],
                    [0,0,0,0,8,0,0,7,9]]
Here each list within the list represents the data from each list. While not pleasing visually, this is the format that is required to run this program.
For each spot where this is no number, place a 0, so that way the program knows to fill that in.

When you call sudoku_king(rows), the following steps will take place:
1. Given an input of rows, where rows is a list of lists containing the contents of each row, we will check for blank spots or '0's using the king function.
2. The "king" function uses 2 for loops to check each entry within the sublists
3. Upon identifying a zero, call the solver function, which will call the functions to generate box/column data and create a list of candidates for that position.
4. The candidates list will be a queue, first in will be the first used for the 0.
5. pop the 0 from rows, and insert the first candidate, then pop the first candidate from the list of candidates
5. At this point, the row number, the column number, and the candidates list will all be put into a list, then inserted to the end of the changes_list.
6. At this point, exit the solver function and return the new rows data.
7. Once the rows are returned, check the end of the change_list, change_list[-1][2]. If this is EMPTY, we need to backtrack.
8. The king function will now proceed to the next 0, where it will call the solver function again to find the candidates.
9. If there are no candidates available at that particular point, we have reached a contradiction, which means there was a mistake. From here we take the last element added to the changes_list stack
10. If the candidates list is empty, then we take the row and column position, pop the number at that position and insert 0, then put the row, column coordinates into a list called back_log, then pop data from the changes_list stack
11. If the candidates list is not empty, then we pop the element at the specified row and column position, then insert the next item in the queue, and pop that from the candidates queue. From here, we pop the data from changes_list, and insert the new data with the updated candidates list
12. If the back_log queue is empty, then the king function will return to the point that caused the contradiction and try again
13. If there is a back_log, then the king function will call the sovler at the points listed in the back_log queue, which will act the same as the regular process
14. This will continue until no 0's are left, upon which the king function will return the solved rows.

# Hint Provider:
The solver has a secondary function, sudoku_hint, that will solve the puzzle behind the scenes then provide a hint to the user.

When called, here's what happens:
1. Create a copy of the rows and set a hint counter to 0.
2. Call sudoku_king (the solver) on the original.
3. Parse through the copy_rows, at the first 0, take the index
4. Use this index to get the solved answer, and insert it into the copy, and increase the hint counter to 1 so that the loop stops.
5. Return the copied rows with the hint included.
