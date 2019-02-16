################################
# CPE 101
# Section: 15
# Assignment #3 : Tests
# Name: Tyler Lian
# Cal Poly ID: tklian
################################

# imports calcdoku.py file
import calcdoku as cd

# initializes lists
x = []
y = []
z = []

# creates 2D grids
for i in range(5):
    x.append([0]*5)
for i in range(5):
    y.append([1]*5)
for i in range(5):
    z.append([2]*5)

# uses init function to create 2D grids
grid0 = cd.init(0)
grid1 = cd.init(1)
grid2 = cd.init(2)

# tests init function
assert cd.init(0) == x
assert cd.init(1) == y
assert cd.init(2) == z

# output 5x10 grid of same #
assert cd.display(grid0) == cd.display(grid0)
assert cd.display(grid1) == cd.display(grid1)
assert cd.display(grid2) == cd.display(grid2)

# tests transpose function
assert cd.transpose(grid0) == x
assert cd.transpose(grid1) == y
assert cd.transpose(grid2) == z

# initializes non-dupe grid
grid = [[1,2,3,4,5],
        [2,3,4,5,1],
        [3,4,5,1,2],
        [4,5,1,2,3],
        [5,1,2,3,4]]

# creates cage list of lists
cage = [[1,1,0],[4,2,1,5],[9,3,2,6,10],[16,4,3,7,11,15],[25,5,4,8,12,16,20]]
cage0 = [[0,3,4,5,8],[0,2,7,9]]
cage1 = [[3,3,1,2,3],[4,4,13,17,24,12]]

# tests all validate functions
assert cd.validate_cols(grid0) == True
assert cd.validate_cols(grid1) == False
assert cd.validate_cols(grid) == True
assert cd.validate_rows(grid0) == True
assert cd.validate_rows(grid1) == False
assert cd.validate_rows(grid) == True
assert cd.validate_cages(grid0, cage0) == True
assert cd.validate_cages(grid1, cage1) == True
assert cd.validate_cages(grid, cage) == True
assert cd.validate_all(grid0, cage0) == True
assert cd.validate_all(grid1, cage1) == False
assert cd.validate_all(grid, cage) == True

# user input: "2" | "0 3 4 5 8" | "0 2 7 9"
assert cd.cage_store() == cage0
print("Correct Cage!\n")
# user input: "1" | "4 2 5 3 4"
assert cd.cage_store() != cage1
print("Incorrect Cage!\n")
# user input: "5" | "1 1 0" | "4 2 1 5" | "9 3 2 6 10" | "16 4 3 7 11 15" | "25 5 4 8 12 16 20"
assert cd.cage_store() == cage
print("Correct Cage!\n")