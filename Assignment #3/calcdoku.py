################################
# CPE 101
# Section: 15
# Assignment #3 : Program
# Name: Tyler Lian
# Cal Poly ID: 015896500
################################

# checks for: row dupes, col dupes, and cage additions
def validate_all(grid, cages):

    # checks for: row dupes
    if validate_rows(grid) == False:
        return False
    
    # checks for: col dupes
    elif validate_cols(grid) == False:
        return False
    
    # checks for: cage additions
    elif validate_cages(grid, cages) == False:
        return False
    
    # if all tests pass: return True
    else:
        return True

# checks for: row dupes
def validate_rows(grid):
    
    # loops through row
    for i in range(5):

        # loops through row indexes
        for j in range(5):

            # if (count of number 1-5 > 1) there are dupes
            if grid[i].count(j) > 1:
                return False

    # if no dupes: return True
    return True

# checks for col dupes
def validate_cols(grid):

    # makes rows into cols
    transpose(grid)

    # loops through cols
    for i in range(5):

        # loops through col indexes
        for j in range(5):

            # if (count of number 1-5 > 1) there are dupes
            if grid[i].count(j) > 1:
                return False
    
    # if no dupes: return True
    return True

# turns rows into cols
def transpose(grid):
    # initializes the lists
    transpose = []
    finished = []

    # transposes all strings in list
    for i in range(5):
        
        # appends all the string together
        for j in range(5):
            line = grid[j]
            transpose.append(line[i])
        
        # join together string of characters
        z = ''.join(transpose)
        z = str(z)
        finished.append(z)

        # take out last string appended
        for x in range(5):
            transpose.pop(0) 
    
    # return transposed puzzle
    return finished

# checks if cages add up to correct amount
def validate_cages(grid, cages):

    # initialize variables & lists
    y = []
    z = 0

    # adds together the rows into one list
    for i in range(5):
        y += grid[i]

    # gets first number in cage list (sum value)
    for j in range(len(cages)):
        x = cages[(j,0)]

        # 
        for k in range(len(cages[j])):
            k += 1
            z += y[cages[(j,k)]]
        if x != z:
            return False
    return True

# creates 5 lists with 5 zeroes in each
def create_initial():
    zero = [0,0,0,0,0]
    y = []
    [(y.append(zero)) for i in range(5)]
    return y 

# cage array is created
def cages(cages):
    y = []
    for i in range(cages):
        y.append(input())
    return y
        

def main():
    
    # number of cages to be made
    n_cages = input()

    # initial base arrays created
    init = create_initial()

    
if __name__ == "__main__":

    main()