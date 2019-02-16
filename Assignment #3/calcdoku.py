################################
# CPE 101
# Section: 15
# Assignment #3 : Program
# Name: Tyler Lian
# Cal Poly ID: tklian
################################

# cage array is created
def cage_store():

    # obtains # of cages
    n_cages = int(input())

    # initialize variables & list
    b = []
    z = ""
    x = 0

    # creates list of lists of cages
    for i in range(n_cages):

        # obtains line from file
        z = input()

        # initializes list
        y = []

        # runs through all numbers in cage
        for j in range(z.count(" ") + 1):

            # if theres a space find index
            if z.find(" ") != -1:
                a = z.find(" ")
            
            # append number 
            y.append(int(z[0:a]))

            # remove appended number
            a = len(z) - a
            z = z[1+-a:]
        
        # append cage to b
        b.append(y)
    
    # return list of cages
    return b

# checks for: row dupes, col dupes, and cage additions
def validate_all(grid, cages):

    # checks if all situations are true
    return validate_rows(grid) and validate_cols(grid) and validate_cages(grid, cages)
    
# checks for: row dupes
def validate_rows(grid):

    # loops through rows
    for i in range(5):
        for j in range(5):

            # dupes & no zeros: False
            if grid[i].count(grid[i][j]) > 1 and grid[i][j] > 0:
                return False
    
    # no dupes & zeros: True
    return True

# checks for col dupes
def validate_cols(grid):
    
    # transposes 2D grid
    grid = transpose(grid)

    # loops through cols
    for i in range(5):
        for j in range(5):

            # dupes & no zeros: False
            if grid[i].count(grid[i][j]) > 1 and grid[i][j] > 0:
                return False

    # no dupes & zeros: True
    return True

# transposes 2D grid
def transpose(grid):

    # initialize list
    z = []

    # turns rows to columns
    for i in range(5):
        y = []
        for j in range(5):
            y.append(grid[j][i])
        z.append(y)
    
    # return columns
    return z

# checks if cages add up to correct amount
def validate_cages(grid, cages):
    
    # runs for # of cages
    for i in range(len(cages)):
        
        # first digit of cage = sum
        target_sum = cages[i][0]

        # second digit of cage = # of cells
        number_of_cages = cages[i][1]

        # variables & list initialized
        actual_sum = 0
        zero = 0
        y = []

        # appends index 2 to len(cage) into y
        for j in range(2, len(cages[i])):
            y.append(cages[i][j])

        # sum of all indexes in cage
        for k in range(len(y)):
            actual_sum += grid[y[k] // 5][y[k] % 5]

            # if theres a zero in index: False
            if grid[y[k] // 5][y[k] % 5] == 0:
                zero += 1

        # if sum is not right & there is no zeros: False
        if actual_sum != target_sum and zero == 0:
            return False

        # if sum is right and there was a zero: False
        if actual_sum >= target_sum and zero == 1:
            return False

    # if sum is right and there is no zeros: True
    return True       

# displays grid in format
def display(grid):

    # prints grid into visible 2D grid 
    for i in range(5):
        print(str(grid[i][0]) + " " + str(grid[i][1]) + " " + \
            str(grid[i][2]) + " " + str(grid[i][3]) + " " + str(grid[i][4]))
    
    # return nothing
    return

def init(n):

    # initializes list
    grid = []

    # 5 x 5 "0" list
    for i in range(5):
        grid.append([n] * 5)

    # returns list
    return grid

def main():   

    # cages initialized into lists of list
    cages = cage_store()
    print(cages)
    # 2D grid created
    grid = init(0)

    # variable initialized
    i = 0
    
    # program run until i = 25
    while i < 25:

        # add one to index
        grid[i // 5][i % 5] += 1

        # if validated & less than six: increase index
        if validate_all(grid, cages) and grid[i // 5][i % 5] < 6:
            i += 1
        
        # if number is less than five: continue adding
        elif grid[i // 5][i % 5] < 5:
            continue

        # if number is not valid: reset to zero & backtrack index
        else:
            grid[i // 5][i % 5] = 0
            i -= 1
    
    # displays final 
    display(grid)  

# if program run as main: run
if __name__ == "__main__":

    # runs main function
    main()