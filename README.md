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
1. 
