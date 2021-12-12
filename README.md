# Sudoku solver using backtrack algorithm 

This project uses **backtracking algorithm** to solve **9x9** sudoku problem. The same can be implemented for other sizes of sudoku. 

**Backtracking** - Backtracking is a general algorithm for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. _(https://en.wikipedia.org/wiki/Backtracking)_

In order to show how the code is working, I have used basic **pygame** to visualise this. 

**Implementation-**

**1. emptsq()**- this function checks the squares of the matrix to find square where the value is 0, which means it is an empty square. 

**2. isval()**- this function checks if the value "nu" can be written in that empty square or not as it checks the corrosponding row, column and the whole 3x3 block as well to see if the same value is already present or not.

**3. sudokusol()**- this takes the sudoku matrix as in argument and then calls the other functions one by one. 

**4. drawgrd()**- this includes the pygame part of the whole program. This function draws the grid for sudoku and also writes the currently checking digit on the canvas as the program runs, so the user can understand the working of the algorithm.  
