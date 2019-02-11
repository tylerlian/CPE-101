################################
# CPE 101
# Section: 15
# Assignment #3 : Tests
# Name: Tyler Lian
# Cal Poly ID: 015896500
################################

def flip(items):

    length = len(items)

    for i in range(length//2):

        temp = items[i]

        items[i] = items[length-1-i]

        items[length-1-i] = temp
    return items



my_list = [1,4,3,5,2]

my_string = ['e','d','c','b','a']

print(flip(my_list))

print(flip(my_string))

