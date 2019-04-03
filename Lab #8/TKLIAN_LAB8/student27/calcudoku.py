def validate_rows(grid):
    i = 0
    j = 0
    counts = [0, 0, 0, 0, 0]
    while j < 5:
        while i < 5:
            if str(grid[5 * j + i]) == "1":
                counts[0] += 1
            elif str(grid[5 * j + i]) == "2":
                counts[1] += 1
            elif str(grid[5 * j + i]) == "3":
                counts[2] += 1
            elif str(grid[5 * j + i]) == "4":
                counts[3] += 1
            elif str(grid[5 * j + i]) == "5":
                counts[4] += 1
            i += 1
        if not contains_greater_one(counts):
            return False
        counts = [0, 0, 0, 0, 0]
        i = 0
        j += 1
    return True

def contains_greater_one(array):
    i = 0
    for i in array:
        if i > 1:
            return False
    return True

def validate_cols(grid):
    i = 0
    j = 0
    counts = [0, 0, 0, 0, 0]
    while j < 5:
        while i < 5:
            if str(grid[5 * i + j]) == "1":
                counts[0] += 1
            elif str(grid[5 * i + j]) == "2":
                counts[1] += 1
            elif str(grid[5 * i + j]) == "3":
                counts[2] += 1
            elif str(grid[5 * i + j]) == "4":
                counts[3] += 1
            elif str(grid[5 * i + j]) == "5":
                counts[4] += 1
            elif str(grid[5 * i + j]) != "0":
                return False
            i += 1
        if not contains_greater_one(counts):
            return False
        counts = [0, 0, 0, 0, 0]
        i = 0
        j += 1
    return True

def validate_cage(grid, cages):
    is_ok = True
    for i in cages:
        temp_sum = 0
        x_sum = i[0]
        zeros = False
        j = 2
        while j < i[1] + 2:
            temp_sum += grid[i[j]]
            if grid[i[j]] == 0:
                zeros = True
            j += 1
        if (temp_sum < x_sum and zeros == False) or (temp_sum >= x_sum and zeros == True):
            is_ok = False
    return is_ok


def main():
    numOfCages = None
    while numOfCages is None:
        try:
            numOfCages = int(input("Input the number of cages: "))
            assert numOfCages > 0
        except:
            numOfCages = None
            print("The input was invalid. ")
            pass
    cages = []
    while len(cages)  < numOfCages:
        tempCage = input("Input Cage Information")
        tempCageList = []
        tempNum = ""
        for i in tempCage:
            if i == " ":
                tempCageList.append(int(tempNum))
                tempNum = ""
            else:
                tempNum += i
        try:
            tempCageList.append(int(tempNum))
        except:
            pass
        cages.append(tempCageList)
    puzzle = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0]
    c = 0
    while c <= 24 or not(validate_cage(puzzle, cages) and validate_rows(puzzle) and validate_cols(puzzle)):
        puzzle[c] += 1
        if validate_cage(puzzle, cages) and validate_rows(puzzle) and validate_cols(puzzle):
            c += 1
        elif puzzle[c] >= 5:
            puzzle[c] = 0
            c += - 1
    print(str(puzzle[0]) + " " +  str(puzzle[1]) + " " + str(puzzle[2]) + " " + str(puzzle[3]) + " " + str(puzzle[4]))
    print(str(puzzle[5]) + " " + str(puzzle[6]) + " " + str(puzzle[7]) + " " + str(puzzle[8]) + " " + str(puzzle[9]))
    print(str(puzzle[10]) + " " + str(puzzle[11]) + " " + str(puzzle[12]) + " " + str(puzzle[13]) + " " + str(puzzle[14]))
    print(str(puzzle[15]) + " " + str(puzzle[16]) + " " + str(puzzle[17]) + " " + str(puzzle[18]) + " " + str(puzzle[19]))
    print(str(puzzle[20]) + " " + str(puzzle[21]) + " " + str(puzzle[22]) + " " + str(puzzle[23]) + " " + str(puzzle[24]))



if __name__ == '__main__':
    main()
    assert validate_cols([1, 2, 3 , 4, 5, 2, 3, 4, 5, 1, 3, 4, 5, 1, 2, 4, 5, 1, 2, 3, 5, 1, 2, 3, 4, 5]) == True
    assert validate_cols([1, 2, 3, 4, 5, 2, 3, 4, 5, 1, 3, 4, 5, 1, 2, 4, 5, 1, 2, 3, 5, 1, 2, 3, 5, 5]) == False
    assert validate_cols([3, 2, 1, 4, 5, 2, 3, 4, 5, 1, 3, 4, 5, 1, 2, 4, 5, 1, 2, 3, 5, 1, 2, 3, 4, 5]) == False
    assert validate_rows([1, 2, 3, 4, 5, 2, 3, 4, 5, 1, 3, 4, 5, 1, 2, 4, 5, 1, 2, 3, 5, 1, 2, 3, 4, 5]) == True
    assert validate_rows([2, 2, 3, 4, 5, 1, 3, 4, 5, 1, 3, 4, 5, 1, 2, 4, 5, 1, 2, 3, 5, 1, 2, 3, 4, 5]) == False
    assert validate_rows([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 1, 2, 3, 5, 1, 2, 3, 4, 5]) == False
    assert validate_cage([4, 2, 4, 3, 5, 3, 2], [[9, 3, 2, 3, 5]]) == True
    assert validate_cage([4, 2, 4, 3, 5, 3, 2], [[9, 2, 2, 0]]) == False
    assert validate_cage([4, 2, 4, 3, 5, 3, 2], [[5, 2, 1, 3]]) == True
