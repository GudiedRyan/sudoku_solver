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

test_solution_columns = [[5, 6, 1, 8, 4, 7, 9, 2, 3], 
                         [3, 7, 9, 5, 2, 1, 6, 8, 4], 
                         [4, 2, 8, 9, 6, 3, 1, 7, 5], 
                         [6, 1, 3, 7, 8, 9, 5, 4, 2], 
                         [7, 9, 4, 6, 5, 2, 3, 1, 8], 
                         [8, 5, 2, 1, 3, 4, 7, 9, 6], 
                         [9, 3, 5, 4, 7, 8, 2, 6, 1], 
                         [1, 4, 6, 2, 9, 5, 8, 3, 7], 
                         [2, 8, 7, 3, 1, 6, 4, 5, 9]]

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

easy_test2 = [[8,0,0,0,0,0,0,0,0],
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

fail_puzzle_rows = [[5,1,6,8,4,9,7,3,2],
                    [3,0,7,6,0,5,0,0,0],
                    [8,0,9,7,0,0,0,6,5],
                    [1,3,5,0,6,0,9,0,7],
                    [4,7,2,5,9,1,0,0,6],
                    [9,6,8,3,7,0,0,5,0],
                    [2,5,3,1,8,6,0,7,4],
                    [6,8,4,2,0,7,5,0,0],
                    [7,9,1,0,5,0,6,0,8]]
