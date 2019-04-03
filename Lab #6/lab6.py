################################
# CPE 101
# Section: 15
# Lab #6 : Program
# Name: Tyler Lian
# Cal Poly ID: tklian
################################

# imports system package
import sys

# makes args list
args = sys.argv

# strips list of new line characters
def strip(array):
    for i in range(len(array)):
        array[i] = array[i].strip()
    return array

# splits all values from file into a list
def line_sep(array):
    new_array = []
    flat_array = []
    for i in range(len(array)):
        new_array.append(array[i].split("\t"))
    for lists in new_array:
        for value in lists:
            flat_array.append(value)
    return flat_array

# checks for ints & floats to add to sum
def check_values(array):
    value = [0,0,0,0]
    for i in range(len(array)):
        try:
            int(array[i])
            value[0] += 1
            value[3] += int(array[i])
        except ValueError:
            try:
                float(array[i])
                value[1] += 1
                value[3] += float(array[i])
            except ValueError:
                value[2] += 1
    return value

# displays final
def display(args, value):

    print("int: " + str(value[0]))
    print("float: " + str(value[1]))
    print("other: " + str(value[2]))
    if '-s' in args:
        print("sum: " + str(value[3]))
    return

# reads file and creates info list
def split_file(file_name):
    try: 
        f = open(file_name, 'r')
        info = f.readlines()
        info = strip(info)
        info = line_sep(info)
    except FileNotFoundError or PermissionError:
        print("Unable to open " + file_name)
        exit()
    return info

# checks if user inputted correct # of args
def arg_check():
    if len(args) < 2 or len(args) > 3:
        print("Usage: [-s] file_name")
        exit()
    elif len(args) == 2:
        file_name = args[1]
    elif len(args) == 3:
        if '-s' not in args:
            print("Usage: [-s] file_name")
            exit()
        elif '-s' == args[1]:
            file_name = args[2]
        elif '-s' == args[2]:
            file_name = args[1]
    return file_name

# runs all functions of program
def main():

    # checks user input
    file_name = arg_check()

    # puts info into a list
    info = split_file(file_name)

    # checks for ints and floats
    value = check_values(info)

    # display values found
    display(args, value)

# if program is ran as main file run
if __name__ == "__main__":
    
    # runs main function
    main()