################################
# CPE 101
# Section: 15
# Assignment #2 : Program
# Name: Tyler Lian
# Cal Poly ID: tklian
################################

# shows the crossword
def display(line):
    
    # initializes variables
    x = 0
    y = 10

    # loops through making 10 character lines
    for i in range(10):
        print(line[x:y])
        x += 10
        y += 10
    print("")

    return

# searches for given word
def find_word(puzzle, word):
    
    x = puzzle.find(word)

    return x

# reverses all strings in list
def reverse_string(line):
    
    for i in range(len(line)):
        r_line = line[::-1]

    return r_line

# tranposes all strings in list
def transpose_string(line, row_len, transpose_line):
    
    z = ""
    x = 0 + transpose_line

    for j in range(row_len):
        y = line[x]
        z += y
        x += row_len

    return z

# runs the functions
def main():

    # obtains lines from files
    line = input()
    word = input().strip("/n")
    w = word.count(" ")
    display(line)

    for i in range(w + 1):
        x = 0
        y = 10
        transpose_line = 0
        not_found = 0
        found = 0
        col = 0
        done = 0

        w = word.find(" ")

        if w == -1:
            z = word[0:len(word)]
        else:
            z = word[0:w]

        for j in range(10):
            
            if done == 0:
                
                position = ""
                puzzle = line[x:y]
   
                if -1 != find_word(puzzle, z):
                    col = find_word(puzzle, z)
                    position = "(FORWARD)"
                    found += 1

                puzzle_r = reverse_string(puzzle)
                if (-1 != find_word(puzzle_r, z)) and (col == 0):
                    col = find_word(puzzle_r, z)
                    col = 9 - col
                    position = "(BACKWARD)"
                    found += 1

                puzzle_t = transpose_string(line, 10, transpose_line)
                if (-1 != find_word(puzzle_t, z)) and (col == 0):
                    col = find_word(puzzle_t, z)
                    position = "(DOWN)"
                    found += 2

                puzzle_tr = reverse_string(puzzle_t)
                if (-1 != find_word(puzzle_tr, z)) and (col == 0):
                    col = find_word(puzzle_tr, z)
                    col = 9 - col
                    position = "(UP)"
                    found += 2

                if (found != 0):

                    row = int(x / 10)

                    if found == 2:
                        print(z + ": " + position + " row: " + str(col) + " col: " + str(transpose_line))
                    elif found == 1:
                        print(z + ": " + position + " row: " + str(row) + " col: " + str(col))
                    
                    done = 1

                x += 10
                y += 10
                transpose_line += 1  

        if done == 0:
            print(z + ": word not found")  

        word = word[(w+1):len(word)]

# runs the main function
if __name__ == "__main__":
    main()