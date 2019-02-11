################################
# CPE 101
# Section: 15
# Assignment #2 : Program
# Name: Tyler Lian
# Cal Poly ID: 015896500
################################

# shows the crossword
def display(list):
    x = 0
    y = 10
    row = []
    for i in range(10):
        print(list[x:y])
        row.append(list[x:y])
        x += 10
        y += 10
    return row

# searches for given word
def find_word(z, puzzle, word):
    
    # initialzes list
    y = []
    word_c = word

    # intiizles length of list
    x = len(word)

    # searches for: "FORWARD" words
    if z == 0:
        placement = "(FORWARD)"
        for i in range(len(word)):
            for j in range(10):
                column = puzzle[j].find(word[i])
                if(column != -1):
                    print(word[i] + ": " + placement + " row: " + str(j) + " column: " + str(column))
                    word_c.pop(i)
                    word_c.insert(i, "0")
        return word_c
    
    # searches for: "BACKWARD" words
    elif z == 1:
        placement = "(BACKWARD)"
        puzzle_changed = reverse_string(puzzle)
        word_c = word
        for i in range(len(word)):
            for j in range(10):
                column = puzzle_changed[j].find(word[i])
                if(column != -1):
                    column = 9 - column
                    print(word[i] + ": " + placement + " row: " + str(j) + " column: " + str(column))
                    word_c.pop(i)
                    word_c.insert(i, "0")
        return word_c
    
    # searches for: "DOWN" words
    elif z == 2:
        placement = "(DOWN)"
        row_len = len(puzzle[0])        
        puzzle_changed = transpose_string(puzzle, row_len)
        word_c = word
        for i in range(len(word)):
            for j in range(10):
                column = puzzle_changed[j].find(word[i])
                if(column != -1):
                    print(word[i] + ": " + placement + " row: " + str(column) + " column: " + str(j))
                    word_c.pop(i)
                    word_c.insert(i, "0")
        return word_c
    
    # searches for: "UP" words
    elif z == 3:
        placement = "(UP)"
        row_len = len(puzzle[0])        
        puzzle_changed = transpose_string(puzzle, row_len)
        puzzle_changed = reverse_string(puzzle_changed)
        for i in range(len(word)):
            for j in range(10):
                column = puzzle_changed[j].find(word[i])
                if(column != -1):
                    column = 9 - column
                    print(word[i] + ": " + placement + " row: " + str(column) + " column: " + str(j))
                    word_c.pop(i)
                    word_c.insert(i, "0")
        return word_c

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
    
    # initializes all arrays
    transpose = []
    finished = []

    # transposes all strings in list
    for i in range(row_len):
        for j in range(len(string)):
            line = string[j]
            transpose.append(line[i])
        z = ''.join(transpose)
        z = str(z)
        finished.append(z)
        for x in range(len(string)):
            transpose.pop(0) 
    return finished

# takes out all of the 0's in list
def not_found(word):

    # if no 0's: returns
    if word.count("0") == 0:
        return word

    # if 0's: delete them
    elif word.count("0") != 0:
        x = word.index("0")
        if x != -1:
            word.pop(x)
        return not_found(word)

# prints all of words not found
def print_not_found(word):

    # prints words in list then deletes
    for i in range(len(word)):
        print(word[0] + ": word not found")
        word.pop(0)
    return

# runs the functions
def main():

    # initializes list
    word = []

    # user inputs file name
    letters = input()

    # obtains lines from files
    file = open(letters, 'r')
    line = file.readline()
    word = file.readline()

    # creates word list
    word = word.split()

    # prints the puzzle and initializes 'puzzle'
    puzzle = display(line)

    # checks for puzzle: regular
    word = find_word(0, puzzle, word)

    # checks for puzzle: backwards
    word = find_word(1, puzzle, word)

    # checks for puzzle: transpose
    word = find_word(2, puzzle, word)

    # checks for puzzle: backwards transpose
    word = find_word(3, puzzle, word)

    # displays words not found in puzzle
    word = not_found(word)
    print_not_found(word)
    
# runs the main function
if __name__ == "__main__":
    main()