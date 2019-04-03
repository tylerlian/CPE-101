
#The Reverse of Input String
def reverse_string(string):
    s = str(string)
    a = str(string)
    i = len(s)
    n = 0
    while(i!=0):
        t = n
        n = n+1
        i = i - 1
        s = s[0:t] + a[i] + s[n:]
    return(s)
    #returns reverse of input string


#Converting Rows to Columns and Columns to Rows
def transpose_string(string, row_len):
    s = str(string)
    a = str(string)
    l = len(s)
    rl = int(row_len)
    i = l - 1
    r = 0
    n = 0
    while (n!=l):
        t = n
        n = n + 1
        s = s[0:t] + a[r] + s[n:]
        r = r + rl
        if r > i:
            b = i - (r - rl)
            r = (rl - b)
        else:
            r = r
    return(s)

# Searching Puzzle for Given Word
def find_word(puzzle, word):
    p = str(puzzle)
    w = str(word)
    l = len(word)
    t = transpose_string(p,10)
    f = p.find(w)
    rw = reverse_string(word)
    frw = p.find(rw)
    ft = t.find(w)
    frt = t.find(rw)
    while(f == -1):
        if frw != -1:
            row = 0
            i = 10
            while (frw >= i):
                row += 1
                i += 10
            row = row
            x = l + frw - 1
            col = x%10
            if x%10 == 0:
                col = 10
            return('%s: (BACKWARD) row: %s column: %s'%(w,row,col))
        elif ft != -1:
            row = ft%10
            col = 0
            i = 10
            while (ft >= i):
                col += 1
                i += 10
            col = col
            return ('%s: (DOWN) row: %s column: %s' % (w, row, col))
        elif frt != -1:
            g = l + frt - 1
            row = g%10
            col = frt//10
            return ('%s: (UP) row: %s column: %s' % (w, row, col))
        else:
            return ('%s: word not found' % w)
    row = 0
    i = 10
    while (f>=i):
        row +=1
        i+=10
    row = row
    col = f%10
    return ('%s: (FORWARD) row: %s column: %s' % (w,row, col))

    # return ' Word: (FORWARD) row: 1 column: 0

def display_puzzle(puzzle):
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

#Main Function
def main():
    puzzle = input('Enter a 100-character string: ')
    words = input('Enter words to search for: ')
    puzzle = puzzle.strip()
    words = words.strip()
    print('')
    print('10x10 Wordsearch Puzzle:')
    print('')
    display_puzzle(puzzle)
    print('')
    while(words.find(' ') != -1):
        p = words.find(' ')
        w = words[0:p]
        words = words[p+1:]
        print(find_word(puzzle, w))
    print(find_word(puzzle,words))

if __name__ == '__main__':
    main()



