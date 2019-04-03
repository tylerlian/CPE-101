################################
# CPE 101
# Section: 15
# Lab #5 : Program
# Name: Tyler Lian
# Cal Poly ID: tklian
################################

# squares every value in list
def square_list(int_list):
    y = [(int_list[i] ** 2) for i in range(len(int_list))]
    return y

# adds n to every value in list
def add_n_all(int_list, n):
    x = 0
    y = []
    while x != len(int_list):
        y.append(int_list[x] + n)
        x += 1
    return y

# returns if values in list are even or not
def is_even_all(int_list):
    y = []
    for i in range(len(int_list)):
        y.append((int_list[i] % 2) == 0)
    return y

# only returns positive numbers from list
def are_positive(int_list):
    y = [(int_list[i]) for i in range(len(int_list)) if(int_list[i] > 0)]
    return y

# only returns numbers greater than n from list
def are_greater_than_n(int_list, n):
    y = []
    for i in range(len(int_list)):
        if int_list[i] > n:
            y.append(int_list[i])
    return y

# only returns numbers divisible by n
def are_divisible_by_n(int_list, n):
    y = []
    x = 0
    while x != len(int_list):
        if(int_list[x] % n) == 0:
            y.append(int_list[x])
        x += 1
    return y

# returns sum of list
def sum_101(my_list):
    y = 0
    for i in range(len(my_list)):
        y += my_list[i]
    return y

# returns index of smallest number in list
def index_of_smallest(my_list):
    
    # initializes variables
    y = []
    x = 0

    # initialzes y list as my_list
    while x != len(my_list):
        y.append(my_list[x])
        x += 1

    # if list doesn't have any values return '-1'
    x = 0
    if len(my_list) == 0:
        return -1
    
    # removes numbers from list to find smallest number
    while (x+1) != len(my_list):

        # remove greater number
        if my_list[x] < my_list[x+1]:
            my_list.pop(x+1)
        elif my_list[x] > my_list[x+1]:
            my_list.pop(x)
        
        # remove number to right if equal
        elif my_list[x] == my_list[x+1]:
            my_list.pop(x+1)

    # returns index of smallest number        
    return y.index(my_list[x])