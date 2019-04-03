def find_word(puzzle, word):
    """
    Finds a word in a string
    :param puzzle: The input puzzle to search through
    :param word: The word being looked for
    :return: Column, row, and direction of the word
    """
    if puzzle.find(word) != -1:
        row = 0
        column = puzzle.find(word)
        while column > 9:
            column += -10
            row += 1
        if len(word) + column > 10:
            return '%s: word not found' % word
        return '%s: (FORWARD) row: %s column: %s' % (word, row, column)

    elif reverse_string(puzzle).find(word) != -1:
        row = 0
        column = reverse_string(puzzle).find(word)
        while column > 9:
            column += -10
            row += 1
        if len(word) + column > 10:
            return '%s: word not found' % word
        row = 9 - row
        column = 9 - column
        return '%s: (BACKWARD) row: %s column: %s' % (word, row, column)

    elif reverse_string(transpose_string(puzzle, 10)).find(word) != -1:
        row = 0
        column = reverse_string(transpose_string(puzzle, 10)).find(word)
        while column > 9:
            column += -10
            row += 1
        if len(word) + column > 10:
            return '%s: word not found' % word
        row = 9 - row
        column = 9 - column
        transfer = column
        column = row
        row = transfer
        return '%s: (UP) row: %s column: %s' % (word, row, column)

    elif transpose_string(puzzle, 10).find(word) != -1:
        row = 0
        column = transpose_string(puzzle, 10).find(word)
        while column > 9:
            column += -10
            row += 1
        if len(word) + column > 10:
            return '%s: word not found' % word
        transfer = column
        column = row
        row = transfer
        return '%s: (DOWN) row: %s column: %s' % (word, row, column)

    else:
        return '%s: word not found' % word


def reverse_string(string):
    """
    Flips a string around so that it's backwards
    :param string: Input string
    :return: Backwards string
    """
    return ''.join(reversed(string))


def transpose_string(string, row_len):
    """
    Flips the rows/columns of a string
    :param string: Input string
    :param row_len: Row length
    :return: Transposed string
    """
    trans_string = ""
    for n in range(len(string)):
        column = n
        row = 0
        while column > row_len - 1:
            column += -1 * row_len
            row += 1
        transfer = row
        row = column
        column = transfer
        while row > 0:
            column += row_len
            row += -1
        trans_string += string[column]

    return trans_string


def print_puzzle(puzzle):
    """
    Prints the input string as a 10x10 grid
    :param puzzle: Input string
    :return: None
    """
    print(puzzle[0:10])
    print(puzzle[10:20])
    print(puzzle[20:30])
    print(puzzle[30:40])
    print(puzzle[40:50])
    print(puzzle[50:60])
    print(puzzle[60:70])
    print(puzzle[70:80])
    print(puzzle[80:90])
    print(puzzle[90:100])
    print()


def main():

    puzzle = input()
    words = input()

    print_puzzle(puzzle)

    j = 0
    for i in range(len(words)):
        if words[i] == ' ':
            new_str = words[j:i]
            j = i + 1
            print(find_word(puzzle, new_str))
        elif i == len(words) - 1:
            print(find_word(puzzle, words[j:(i+1)]))


if __name__ == '__main__':
    main()
