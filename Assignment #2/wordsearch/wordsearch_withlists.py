################################
# CPE 101
# Section: 15
# Assignment #2 : Program
# Name: Tyler Lian
# Cal Poly ID: tklian
################################

# shows the crossword
def display(list):
    
    # initializes variables
    x = 0
    y = 10

    # initializes list
    row = []

    # loops through making 10 character lines
    for i in range(10):
        print(list[x:y])
        row.append(list[x:y])
        x += 10
        y += 10
    return row

def forward_check():
    
# searches for given word
def find_word(puzzle, word):
    
    # initialzes list
    y = []

    # intiizles length of list
    x = len(word)

    # word not found
    w = 0

    # searches for: "FORWARD" words
    placement = "(FORWARD)"
    for j in range(10):
        column = puzzle[j].find(word[0])
        if(column != -1):
            x = (word[0] + ": " + placement + " row: " + str(j) + " column: " + str(column))
            w = 1
    
    # searches for: "BACKWARD" words
    placement = "(BACKWARD)"
    puzzle_changed = reverse_string(puzzle)
    for j in range(10):
        column = puzzle_changed[j].find(word[0])
        if(column != -1):
            column = 9 - column
            x = (word[0] + ": " + placement + " row: " + str(j) + " column: " + str(column))
            w = 1
    
    # searches for: "DOWN" words
    placement = "(DOWN)"
    row_len = len(puzzle[0])        
    puzzle_changed = transpose_string(puzzle, row_len)
    word_c = word
    for j in range(10):
        column = puzzle_changed[j].find(word[0])
        if(column != -1):
            x = (word[0] + ": " + placement + " row: " + str(column) + " column: " + str(j))
            w = 1

    # searches for: "UP" words
    placement = "(UP)"
    row_len = len(puzzle[0])        
    puzzle_changed = transpose_string(puzzle, row_len)
    puzzle_changed = reverse_string(puzzle_changed)
    for j in range(10):
        column = puzzle_changed[j].find(word[0])
        if(column != -1):
            column = 9 - column
            x = (word[0] + ": " + placement + " row: " + str(column) + " column: " + str(j))
            w = 1
    
    # if word not found: "word not found"
    if w == 0:
        x = (word[0] + ": word not found")
    
    # returns string
    return x

# reverses all strings in list
def reverse_string(string):
    
    # initializes list
    y = []

    # reverses all strings in list
    for i in range(len(string)):
        x = string[i]
        y.append(x[::-1])
    return y

# tranposes all strings in list
def transpose_string(string, row_len):
    
    # initializes the lists
    transpose = []
    finished = []

    # transposes all strings in list
    for i in range(row_len):
        
        # appends all the string together
        for j in range(len(string)):
            line = string[j]
            transpose.append(line[i])
        
        # join together string of characters
        z = ''.join(transpose)
        z = str(z)
        finished.append(z)

        # take out last string appended
        for x in range(len(string)):
            transpose.pop(0) 
    
    # return transposed puzzle
    return finished

# appends the words into a list
def word_list(word):

    # initializes the lists
    y = []

    # counts how many spaces are in the string
    x = word.count(" ")

    # loops appending words into list y
    for i in range(x + 1):
        z = word.find(" ")
        
        # last word gets appended
        if word.find(" ") == -1:
            y.append(word)
            return y
        
        # removes word once appended
        string = word[0:z]
        y.append(string)
        word = word[(z+1):]


# runs the functions
def main():

    # initializes list
    word = []

    # obtains lines from files
    line = input()
    word = input().strip("/n")

    # creates word list
    word = word_list(word)

    # prints the puzzle and initializes 'puzzle'
    puzzle = display(line)

    # checks for puzzle words
    for i in range(len(word)):
        x = find_word(puzzle, word)
        print(x)
        word.pop(0)

# runs the main function
if __name__ == "__main__":
    main()